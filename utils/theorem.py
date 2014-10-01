#!/usr/bin/env python

"""
Pandoc filter to convert divs with class="theorem" to LaTeX
theorem environments in LaTeX output, and to numbered theorems
in HTML output.
"""

from pandocfilters import toJSONFilter, RawBlock, Div

theoremcount = 0

environments = ["theorem", "lemma", "corollary", "definition", "example", "exercise", "question", "claim"]

def latex(x):
  return RawBlock('latex',x)

def html(x):
  return RawBlock('html', x)

def theorems(key, value, format, meta):
  if key == 'Div':
    [[ident,classes,kvs], contents] = value
    for env in environments:
      if env in classes:
        if format == "latex":
          if ident == "":
            label = ""
          else:
            label = '\\label{' + ident + '}'
          return([latex('\\begin{{{0}}}'.format(env) + label)] + contents +
                 [latex('\\end{{{0}}}'.format(env))])
        elif format == "html" or format == "html5":
          global theoremcount
          theoremcount = theoremcount + 1
          classes.append("math")
          newcontents = [html('<dl><dt class="math">{0} '.format(env.capitalize()) + str(theoremcount) + '</dt>'),
                         html('<dd class="math">')] + contents + [html('</dd>\n</dl>')]
          return Div([ident,classes,kvs], newcontents)

if __name__ == "__main__":
  toJSONFilter(theorems)
