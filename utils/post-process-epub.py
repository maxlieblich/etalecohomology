import itertools
import os
import re
import tempfile
import zipfile

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

import xml.etree.ElementTree as ElementTree

MIME_TYPES = {
        '.js': 'application/x-javascript',
        '.woff': 'application/font-woff',
        '.otf': 'font/opentype',
        '.png': 'image/png',
        '.eot': 'application/vnd.ms-fontobject',
        '.svg': 'image/svg+xml',
        '.html': 'text/html',
        '.md': 'text/x-markdown',
        '.txt': 'text/plain',
        '.json': 'application/json',
        '.gif': 'image/gif',
        }

MATHJAX_CONFIG = r'''
<script type="text/x-mathjax-config">
//<![CDATA[
MathJax.Hub.Config({
    jax: [
        "input/MathML",
        "output/SVG",
    ],
    extensions: [
        "mml2jax.js",
        "MathEvents.js",
    ],
    MathMenu: {
        showRenderer: false
    },
    menuSettings: {
        zoom: "Click"
    },
    messageStyle: "none"
});
//]]>
</script>
'''
MATHJAX_SCRIPT = r'<script type="text/javascript" src="MathJax/MathJax.js" />'
MATHJAX_FILES = (
        'MathJax.js',
        'images',
        'jax/element',
        'jax/input/MathML',
#        'jax/input/TeX',
#        'extensions/MathML',
        'jax/output/SVG/autoload',
        'jax/output/SVG/config.js',
        'jax/output/SVG/fonts/TeX',
        'jax/output/SVG/jax.js',
        'extensions/TeX',
#        'extensions/FontWarnings.js',
#        'extensions/HelpDialog.js',
        'extensions/MathEvents.js',
        'extensions/MathMenu.js',
        'extensions/MathZoom.js',
        'extensions/mml2jax.js',
#        'extensions/tex2jax.js',
        )

EPUB_URI = 'http://www.idpf.org/2007/opf'
XHTML_URI = 'http://www.w3.org/1999/xhtml'
MATHML_URI = 'http://www.w3.org/1998/Math/MathML'

URI_REGEX = re.compile(r'^{(.*)}')

CHAPTER_REGEX = re.compile(r'ch\d+\.xhtml')

def parse_xml(file, uri=XHTML_URI):
    # the ElementTree module seems poorly written, with registering
    # namespaces globally (it should be able to figure out the namespaces
    # from parsing the xml correctly)
    ElementTree.register_namespace('', uri)
    if uri == XHTML_URI:
        ElementTree.register_namespace('epub', EPUB_URI)

    xmltree = ElementTree.parse(file)
    # silly hack to deal with ElementTree ignoring multiple namespaces
    if uri == XHTML_URI:
        xmltree.getroot().set('xmlns:epub', EPUB_URI)

    return xmltree

class EpubUpdater:
    def __init__(self, oldpath, newpath):
        self._old = zipfile.ZipFile(oldpath, 'r')
        self._new = zipfile.ZipFile(newpath, 'w')
        self._contentopf = parse_xml(self._old.open('content.opf'), uri=EPUB_URI)
        self._manifest = self._contentopf.find('{%s}manifest'%EPUB_URI)
        self._extra_headers = []
        self._closed = False

    def __del__(self):
        self.close()

    def close(self):
        if self._closed:
            return
        self._write_headers()
        self._write_xml('content.opf', self._contentopf, uri=EPUB_URI)
        self._copy_missing()
        self._old.close()
        self._new.close()
        self._closed = True

    def _write_xml(self, path, xmltree, uri=XHTML_URI):
        # the ElementTree module seems poorly written, with registering
        # namespaces globally (it should be able to figure out the namespaces
        # from parsing the xml correctly)
        ElementTree.register_namespace('', uri)
        if uri == XHTML_URI:
            ElementTree.register_namespace('epub', EPUB_URI)
            for elem in xmltree.getiterator():
                match = URI_REGEX.match(elem.tag)
                if match is None:
                    continue
                uri = match.group(1)
                if uri != XHTML_URI:
                    elem.tag = URI_REGEX.sub('{%s}'%XHTML_URI, elem.tag)
                    elem.set('xmlns', uri)

        # as far as I can tell you have to dump to a file to get the
        # xml_declaration, so we use BytesIO to emulate a file
        buf = BytesIO()
        xmltree.write(buf, encoding='UTF-8', xml_declaration=True)
        self._new.writestr(self._old.getinfo(path), buf.getvalue())
        buf.close()

    def _write_headers(self):
        if not self._extra_headers:
            return
        for item in self._manifest:
            href = item.get('href')
            if not CHAPTER_REGEX.match(href):
                continue

            xmltree = parse_xml(self._old.open(href))
            head = xmltree.find('{%s}head'%XHTML_URI)
            for header in self._extra_headers:
                head.append(header)
            self._write_xml(href, xmltree)

            item.set('properties', 'scripted')

    def _copy_missing(self):
        updated = {info.filename for info in self._new.filelist}
        for info in self._old.filelist:
            if info.filename not in updated:
                self._new.writestr(info, self._old.read(info))

    def _add_files(self, files, path_mutator=lambda path: path):
        paths = set()
        for opath in files:
            if os.path.basename(opath) == '.DS_Store':
                # TODO: make this check a regex
                # since we will want to skip other silly OS/application files
                continue
            path = path_mutator(opath)
            self._new.write(opath, path, zipfile.ZIP_DEFLATED)
            paths.add(path)

        for path in paths:
            self._manifest.append(
                    ElementTree.SubElement(self._manifest, 'item',
                        attrib = {
                            'id': path.replace(os.sep, '_').replace('.', '_'),
                            'href': path,
                            'media-type': MIME_TYPES[os.path.splitext(path)[1]],
                            },
                        )
                    )

    def _add_file(self, file, *args, **kwds):
        self._add_files((file,), *args, **kwds)

    def add_scripts(self, scripts):
        self._add_files(scripts,
                lambda path: os.path.join('js', os.path.basename(path)))

    def add_script(self, script):
        self.add_scripts((script,))

    def add_headers(self, headers):
        for header in headers:
            self._extra_headers.append(ElementTree.fromstring(header))

    def add_header(self, header):
        self.add_headers((header,))

    def embed_mathjax(self, mathjax):
        paths = set()
        for path in MATHJAX_FILES:
            path = os.path.join(mathjax, path)
            if os.path.isdir(path):
                for root, _, files in os.walk(path):
                    paths.update(
                        itertools.imap(
                            lambda path: os.path.join(root, path), files)
                        )
            else:
                paths.add(path)

        regex = re.compile('^' + mathjax)
        self._add_files(paths, lambda path: regex.sub('MathJax', path))
        self.add_headers((MATHJAX_CONFIG, MATHJAX_SCRIPT))

def create_parser():
    import argparse
    parser = argparse.ArgumentParser(description="post-process pandoc epubs")
    parser.add_argument('--input', required=True, help='epub to post-process')
    parser.add_argument('--output', required=True, help='post-processed epub destination')
    parser.add_argument('--mathjax', help='MathJax source directory')
    parser.add_argument('--include-in-headers', help='file to include in headers')
    parser.add_argument('scripts', nargs=argparse.REMAINDER, help='extra scripts to include')

    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    try:
        epub = EpubUpdater(args.input, args.output)
        epub.add_scripts(args.scripts)

        if args.mathjax:
            epub.embed_mathjax(args.mathjax)
        if args.include_in_headers:
            epub.add_headers(open(args.include_in_headers))

        epub.close()
    except Exception:
        os.unlink(args.output)
        raise
