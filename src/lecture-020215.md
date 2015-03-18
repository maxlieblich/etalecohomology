# Trivializing an Azumaya algebra via stacks 02-02-2015

\subsection{A CFG $\mathscr{I}=\mathscr{I}_A$}
Given an Azumaya algebra $A$ on a scheme $X$ we consider the pseudo-functor
$$
\mathscr{I}=\mathscr{I}_A:X\text{-schemes}\to \mathrm{Groupoid}
$$
which takes an $X$-scheme $T$ to the groupoid with
$$
\mathrm{Objects}\mathscr{I}(T)=\left\{\begin{array}{c}\text{Pairs }(V,\phi)\text{ where }V\text{ is a vector bundle on }X\\
\text{and }\phi\text{ is an $\mathcal{O]_X$-algebra isomorphism }\phi:A_T\to\underline{\End}_{\mathscr{O}_X}(V)\end{array}\right\}.
$$
Here by ``vector bundle" we mean specifically a quasi-coherent sheaf $V$ on $X$ which is locally free of finite rank.  The morphisms between objects $\phi:A_T\to \underline{\End}_{\mathscr{O}_T}(V)$ and $\phi':A_T\to\underline{\End}_{\mathscr{O}_T}(V')$ in $\mathscr{I}(T)$ are given by vector bundle maps $\alpha:V\to V'$ fitting into the appropriate diagram, i.e. with $ad_{\alpha}\phi=\phi'$.
\par

Given a map $f:T'\to T$ over $X$, we can pull back a vector bundle $V$ on $T$ to get a vector bundle $f^\ast V$ on $T'$.  We also have a natural isomorphism $f^\ast \End_{\mathscr{O}_T}(V,M)\cong \End_{\mathscr{O}_{T'}}(f^\ast V, f^\ast M)$ whenever $V$ is a vector bundle.  (It is not difficult to check this in the affine case since $V$ will be finitely generated projective, and hence a summand of a finite free module.)  So we can pull back an algebra isomorphism $\phi:A_T\to \End_{\mathscr{O}_T}(V)$ to get an isomorphism $A_{T'}\to \End_{\mathscr{O}_{T'}}(f^\ast V)$, which we denote $f^\ast \phi$ by abuse of notation.  So, modulo a few details which are not entirely insignificant, we get pullback maps $f^\ast:\mathscr{I}(T)\to\mathscr{I}(T')$.

<div class="remark">
It may be easier here to identify $\mathscr{I}$ explicitly as a category fibered in groupoid, rather than a pseudo-functor.
</div> 

The CFG $\mathscr{I}$ is also a *stack*.

<div class="remark">
According to what I think I understood, an algebraic stack on the fppf site is also a stack on the big etale site, and vice versa (whatever these words may mean).  So we use the fppf site here, but one may just as well use the etale site.
</div>

In our example the pairs $(V,\phi)$ satisfy descent in that (1) for any pair $b=(V,\phi)$, $b'=(V',\phi')$ in $\mathscr{I}(T)$ the functor
$$
\text{Isom}_T(b,b'):\mathrm{Sch}/T\to \Set,\ \ 
(U\to T)\mapsto \text{Isom}_{\mathscr{I}(U)}(b|U,b'|U)
$$
is a sheaf on the fppf site $T_{fppf}$, and (2) We can construct a pair $(V,\phi)$ fppf locally via fppf descent for vector bundles.
\par
  
Another way to make this statement is as follows: suppose we have a fppf cover $U\to T$.  Then we can consider the diagram
$$
\mathscr{I}(T)\mathcal{O]verset{(-)|U}\to\mathscr{I}(U)\mathcal{O]verset{p_2^\ast}{\underset{p_1^\ast}\rightrightarrows}\mathscr{I}(U\times_T U).
$$
We would like to say that any object $(W,\psi)$ on $U$ mapping to ``the same" objects $(p^\ast_1 W, p^\ast_1\psi)$ and $(p^\ast_2 W,p_2^\ast \psi)$ under the (pullbacks of) the two projections comes from an object in $\mathscr{I}(T)$.  However, this stament is too coarse, as we explicitly need the information of the isomorphism $\beta:(p^\ast_1 W, p^\ast_1\psi)\to (p^\ast_2 W,p_2^\ast \psi)$.  To apply descent we also need to know that this isomorphism satisfies some compatibility criterion on tripple overlaps.  So we extend our above diagram slightly to get
$$
\mathscr{I}(T)\mathcal{O]verset{(-)|U}\to\mathscr{I}(U)\mathcal{O]verset{p_2^\ast}{\underset{p_1^\ast}\rightrightarrows}\mathscr{I}(U\times_T U)\mathcal{O]verset{\to}{\underset{\to}\to}\mathscr{I}(U\times_T U\times_T U),
$$
where the three arrows are the pullbacks along the three possible projections $p_{ij}^\ast: U\times_T U\times_T U\to U\times_T U$.  With this diagram in hand we demand that any object $b$ in $\mathscr{I}(U)$ along with an isomorphism $\beta:p_1^\ast b\to p_2^\ast b$ which additionally satisfies 
$$
(p_{23}^\ast\beta)(p_{12}^\ast\beta)=p_{13}^\ast\beta
$$
has a $a\in \mathscr{I}(T)$ with $\gamma:a|U\to b$ such that $\beta$ becomes the canonical isomorphism $p_1^\ast(a|U)\to (a|U\times_T U)\to p_2^\ast(a|U)$.  This object $a$, along with the identification $\gamma:a|U\to b$, need to be unique up to unique isomorphism.  (I'm not 100\% sure this is the correct statement, to be frank.  But I think it is correct.)

### An aside

As another example of a stack we can consider the pseudo-functor
$$
QCoh:\Sch/T\to \mathrm{Groupoid}
$$
Taking a $T$-scheme $U$ to the groupoid of quasi-coherent sheaves on $U$, with morphisms given by isomorphisms.  Descent theory for quasi-coherent sheaves can be understood as the statement that $QCoh$ is a stack on $T_{fppf}$.

### A third phrasing of stacks via the category of descent data

Given a CFG $G:\mathcal{C}^{op}\to \mathrm{Groupoid}$, on some arbitrary site $C$, and a covering $U\to T$, we can construct a new category $D^G_{U/T}$ called the category of descent data for $U\to T$.  The objects of $D^G_{U/T}$ are given by descent data,
$$
\mathrm{Objects}D^G_{U/T}=\left\{\begin{array}{c}\text{Data $B$ consisting of an object $b$ in $G(U)$}\\
\text{and a map $\beta:p_1^\ast b\to p_2^\ast b$ satisfying}\\
\text{the cocycle condition $(p_{23}^\ast\beta)(p_{12}^\ast\beta)=p_{13}^\ast\beta$}\end{array}\right\}.
$$
Morphisms $B\to B'$ are given by $\gamma:b\to b'$ producing a commutative diagram
$$
\require{AMScd} \begin{CD} p_1^\ast b @>\beta>> p_2^\ast b \ @V{p_1^\ast\gamma}VV @VV{p_2^\ast \gamma}V \ p_1^\ast b' @>>{\beta'}> p_2^\ast b'. \ \end{CD}
$$
Note that $D^G_{U/T}$ is a groupoid, as all of the maps are isomorphisms.  (They are induced by maps in $G(U)$.
\par

Let's let $f$ denote our covering $U\to T$.  Recall that in the statement that $G$ is the statement that for sequences $X\mathcal{O]verset{g}\to  Y\mathcal{O]verset{h}\to Z$ in $\mathcal{C}$ there are natural, compatible, isomorphisms $(hg)^\ast\mathcal{O]verset{\cong}\to g^\ast h^\ast$.  Whence there is a canonical map of groupoids
$$
\delta_{U/T}:G(T)\to D^G_{U/T}
$$
taking an object $\bar{b}$ in $G(T)$ to $(b,\beta)$, where $b=\bar{b}|U=f^\ast \bar{b}$ and 
$$
\beta:p_1^\ast b=p_1^\ast f^\ast \bar{b}\to p_2^\ast f^\ast\bar{b}=p_2^\ast b
$$
is the isomorphism
$$
p_1^\ast f^\ast \bar{b}\to (fp_1)^\ast \bar{b}=(fp_2)^\ast \bar{b}\to p_2^\ast f^\ast\bar{b}
$$
implied by the pseudo-functor structure on $G$.

<div class="remark">
Let $G:\mathcal{C}^{op}\to \mathrm{Groupoid}$ be a pseudo-functor, as above.  We say descent is *effective* for $G$ if for any cover $U\to T$ the groupoid map $\delta_{U/T}$ is an equivalence of categories.  We say $G$ is a stack on $\mathcal{C}$ if
-descent is effective for $G$ and
-for any $a,a'\in G(T)$, the presheaf $\text{Isom}_T(a,a'):\mathcal{C}^{op}/T\to \Set$ is in fact a sheaf!
</div>
