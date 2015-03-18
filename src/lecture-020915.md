#{Gerbes and cohomology 02-09-2015}

###{Stacks from cohomology classes}

Let $\mathcal{C}$ be a site with a final object $X$.  In general, we think of $\mathcal{C}$ as the fppf, or \'etale site associated to a scheme.  We will assume that $\mathcal{C}$ has whatever properties we need so that our statements make sense.
\par

We define the global sections functor
$$
\Gamma:\mathrm{Sheaves}/C\to \mathrm{Set}
$$
to be the functor taking a sheaf $M$ (of sets) to the value of $M$ on $X$, $\Gamma(M)=M(X)$.  Then for any $S$ in $X$ we have a unique map $S\to X$ in $C$ and induced restriction map $\Gamma(M)\to M(S)$, $m\mapsto m|S$.
\par

Let $A$ be a sheaf of abelian groups on $C$ and consider an injective resolution $0\to A\to I^0\to I^1\to \cdots$.  Then we get a complex $\Gamma(I^\bullet)=0\to \Gamma(I^0)\to \Gamma(I^1)\to\cdots$ and take the cohomology to get $H^\bullet(C,A)$.  Let $d$ denote the differential on our complex $\Gamma(I^\bullet)$.  Below we will also employ the notation $I^\bullet(S)=0\to I^0(S)\to I^1(S)\to\cdots$, and $d|S$ for the differential on $I^\bullet(S)$.

<div class="definition">
Let $a\in \Gamma(I^2)$ be any cocycle, i.e. any element with $d(a)=0$.  We define the ``stack of trivializations of $a$" to be the CFG $\mathscr{G}_a$ with fibers $\mathscr{G}_a(S)$ given by the sets $\{b\in I^1(S):d(b)=a|S\}$.  Morphisms between objects $b$ and $b'$ in $\mathscr{G}_a(S)$ and $\mathscr{G}_a(S)$ are given by a map $S\to S'$ and $\gamma\in I^0(S)$ with $g(\gamma)=b-b'|S$.
</div>

<div class="claim">
$\mathscr{G}_a$ is in fact a stack.  This follows form the fact that all the $I^k$ are sheaves on $\mathcal{C}$.
</div>

###{Properties of $\mathscr{G}_a$ and gerbs}

Note that the automorphisms of a given $b$ in $\mathscr{G}_a(S)$ are exactly equal to the kernel of $d^0|S$.  However, by left exactness of the functor taking sections over $S$, the sequence $0\to A(S)\to I^0(S)\to I^1(S)$ is exact for all $S$.  So we have an identification $A(S)\mathcal{O]verset{\cong}\to \ker(d_S^0)$ for all $S$.  Furthermore, we will have diagrams
$$
\require{AMScd} \begin{CD}
A(S) @>>>> \mathrm{Aut}(b) \\
@V{\mathrm{restrict}}VV @VV{\mathrm{restrict}}V \\
A(S') @>>>> \mathrm{Aut}(b|S') \\
\end{CD}
$$
for each $S'\to S$.  So we get an isomorphism of sheaves $A_S\to \underline{\mathrm{Aut}}(b)$ for each $b$ in $\mathscr{G}(S)$.
\par

Since our original sequence $0\to A\to I^\bullet$ was exact, the cocycle $a\in I^2(X)$ will be a boundary locally.  That is to say, there is a covering $U\to X$ in $\mathcal{C}$ with $a|U=d(b)$ for some $b\in I^1(U)$.  Which is to say, $\mathscr{G}_a(U)$ is nonempty.  This is also true if we replace $X$ with any other object $S$ in $\mathcal{C}$.  Indeed, the cover $U\times_X S\to S$ will have $\mathscr{G}_a(U\times_X S)\neq \emptyset$.  A similar argument shows that for any $b,b'$ in $\mathscr{G}(S)$, there is some cover $V\to S$ on which we have a map $\gamma:b|V\to b'|V$ in $\mathscr{G}(V)$.  We record all this information below.

<div class="proposition">
The stack $\mathscr{G}_a$ has the following properties:
- (1) For any $S$ in $\mathcal{C}$ there is a cover $U\to S$ with $\mathscr{G}_a(U)$ nonempty.
- (2) For $S$, and any $b,b'$ in $\mathscr{G}_a(S)$, there is a cover $V\to S$ such that the restrictions $b|S$ and $b'|S$ admit an isomorphism $\gamma:b|S\to b'|S$.
- (3) For any $b$ in $\mathscr{G}_a(S)$ there is an isomorphism of sheaves $A_S\to \underline{\mathrm{Aut}}(b)$.
</div>

<div class="definition">
Any stack $\mathscr{G}$ with the above three properties is called an $A$-gerbe.
</div>

As an example we can consider the stack $B\mathbb{G}_m$, which we interpret here as the stack of line bundles on a fixed base scheme $X$.  Objects in $B\mathbb{G}_m$ will be line bundles, and morphisms will be given by isomorphisms of line bundles.  Here $\mathcal{C}$ will be the fppf site on $X$.  
\par

Obviously $B\mathbb{G}_m(X)$ is nonempty, since $\mathcal{O]_X$ is a global line bundle.  So condition (1) will be satisfied.  For any $S\to X$, and line bundles $L$ and $L'$ on $S$, we can choose a cover $\{V_i\to S\}$ such that $L|V_i$ and $L'|V_i$ are free, and hence admit an isomorphism $L|V_i\mathcal{O]verset{\cong}\to L|V_i$.  Whence we can take $V=\coprod_i V_i$ to get a cover $V\to S$ on which $L|V$ and $L'|V$ are isomorphic.  This gives (2).  For (3) we simply note that, for any line bundle $L$ on $S$, the canonical map $\mathcal{O]_S\to \underline{\mathrm{End}}_{\mathcal{O]_S}(L)$ given by left multiplication will be an isomoprhism.  This isomorphism restricts to give a natural isomorphism $\mathbb{G}_m(S)=\mathcal{O]_S^\ast(S)\to \mathrm{Aut}_{\mathcal{O]_S}(L)$, and subsequent sheaf isomorphism $(\mathbb{G}_m)_S\to \underline{\mathrm{Aut}}_{B\mathbb{G}_m}(L)$.

###{Isoclasses of gerbs and $H^2(\mathcal{C},A)$}

<div class="question">
What happens if we replace $a\in \Gamma(I^2)$ with $a+d(b)$, for some $b\in \Gamma(I^1)$?
</div>

The answer is that we get an isomorphism of stacks $\mathscr{G}_a\to \mathscr{G}_{a+d(b)}$.  On each fiber, this isomorphism $\mathscr{G}_a(S)\to \mathscr{G}_a(S)$ is given on objects as the map $b'\mapsto b'+b|S$, and on morphisms simply by $\gamma\mapsto \gamma$.  (If $\gamma=b'-b''|S$ then $\gamma=(b'-b|S)-(b''|S-b|S)$.)  Whence we get a well defined map
$$
H^2(\mathcal{C},A)\to \{\text{Isocalasses of $A$-gerbs}\}
$$

<div class="questions">
- Are all gerbs of the form $\mathscr{G}_a$?
- Is the above map an isomorphism?
</div>

\end{document}










