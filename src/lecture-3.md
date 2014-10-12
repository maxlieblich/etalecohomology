# Standard examples

### $G$-sets

Let $G$ be a group, and let $C$ be the category of sets with a left $G$-action. **Variant**: let $G$ be a *profinite* group, and let $C$ be the category of finite sets with a *continuous* (left) action. Define a covering to be a collection of $G$-equivariant maps $\{U_i\to U\}$ such that $\sqcup U_i\to U$ is surjective.

<div class="exercise">
Show that we have just described the canonical topology on $C$.
</div>

Given a sheaf $F:C^\circ\to\Set$, we can make $F(G)$ into a $G$-set: (first, $G$ acts on the left on $G$ by translation) $$g:F(G)\to F(G)$$ is defined to be the map induced by the map of left $G$-sets $$G\to G: a\mapsto a g.$$
(Thanks to Hao and Bharathwaj for pointing out that the contravariance of $G$ makes this the natural left action, not $a\mapsto a g^{-1}$!)

<div class="claim">
Every sheaf $F$ on $C$ is representable by $F(G)$ with the above action.
</div>
**Proof**. Given a $G$-set $U$, we need to find a functorial isomorphism $$F(U)\to\Hom_C(U, F(G)).$$ We can write $U$ is a disjoint union of orbits $U=\sqcup U_i$, and **the sheaf property tells** us that this decomposition induces a canonical isomorphism $F(U)=\prod F(U_i)$. Thus, it suffices to show this for $U$ that consist of a single $G$-orbit.

But then there is a covering of the form $G\to U$ (given by choosing an element $u\in U$ and letting $G$ act). The sheaf property says that $F(U)$ is idenfied with the the equalizer of $$F(G)\rightrightarrows F(G\times_U G).$$ Having chosen $u$, let's write $U = G/H$ for $H$ a subgroup of $G$. Two elements of $G$ map to the same element of $G/H$ if and only if they are in the same coset. Thus, an element of $G\times_U G$ has the form $(g, gh)$ for some $h\in H$. This gives an isomorphism of $G$-sets $$G\times_U G\to G\times H,$$ where the $H$ factor in the latter has a trivial $G$-action. In other words, $$G\times_U G\cong \sqcup_{h\in H} G$$ as $G$-sets. This admits a right $H$-action that simply permutes the factors.

By the sheaf property, we conclude that
$$F(G\times_U G)\cong \prod_{h\in H} F(G).$$
What are the maps $F(G)\to \prod_HF(G)$? The first one is the diagonal map, while the second one is the product of the maps $F(G)\to F(G)$ given by the right action of $H$. The equalizer of the maps is precisely the $H$-invariant part of $F(G)$.(Question from Hao: Why is the first map diagonal and second map as claimed? )

Answer(Hao): Let $\varphi: G \times H \to G \times_U \G : (g,h) \mapsto (g,gh)$. It is a isomorphism of $G$-sets. Let $\pi_1, \pi_2$ be the two projections
from $G \times_U G$. Then $\pi_1 \circ \varphi(g,h) = g$ and $\pi_2 \circ \varphi(g,h) = gh$. Under the identification $\Phi: F(G \times H ) \cong \prod_H F(G)$,
each factor on the right hand side is the image of $F(G \times \{h\})$ for some $h$. But $G \times {h}$ is isomorphic to $G$ canonically and we used this
canonical isomorphism to define $\Phi$, so the first map $F(G) \to F(G\times_U G)$ is the diagonal. The second map on the h-piece of $\prod_H F(G)$ induced from $g (\mapsto (g,h)) \mapsto gh$. Hence it corresponds to the action of $h^{-1}$ on $F(G)$. So the second map is $F(G)$ hitted with all elements of $H$ on the right.

What is $\Hom_C(G/H, F(G))$? Well, $\Hom_C(G, S)$ for any $G$-set $S$ is the same as $S$, so $\Hom_C(G/H, F(G))\subset F(G)$. It is the subset consisting of elements of $F(G)$ that are fixed by $H$, that is, $\alpha\in F(G)$ such that for all $h\in H$, the map $g\mapsto gh^{-1}$ sends $\alpha$ to $\alpha$. Call this $F(G)^{H}$.

This identifies $F(U)$ with $\Hom_C(U, F(G))$, as desired. QED

**Upshot**: a sheaf on $G$-set is a $G$-set, and a sheaf of abelian group is a $G$-module. (Be careful about profinite groups and continuity/discreteness conditions!)

### Topological spaces, big and small

Given a topological space $X$, we have the category of open subsets, $\Open(X)$. This has a Grothendieck topology that you know and love (because you described it, or maybe we did this in class). This is called the *small site* of $X$.

We can also consider the slice category $\Top_{/X}$ of all topological spaces over $X$, like $Y\to X$. A covering is a collection of $X$-maps $\{U_i\to U\}$ that form a covering of $U$ in the usual way. This is called the *big site* of $X$.

There are two natural functors
$$\Top_{/X}\to\Sh(\Open(X))$$
and
$$\Top_{/X}\to\Sh(\Top_{/X}).$$

<div class="question">
Are either of these functors fully faithful? Are they both fully faithful?
</div>

### The etale site of a field

Let $K$ be a field. Let $\Et(K)$ be the category of etale $K$-schemes; by facts we will review soon, $\Et(K)$ is the category of $K$-schemes of the form $\sqcup\Spec L_i$ with each $L_i$ a finite separable extenson of $K$.

A covering $\{U_i\to U\}$ in $C$ is a collection of maps such that $\sqcup U_i\to U$ is set-theoretically surjective.

<div class="exercise">
Show that this is a site. Please.
</div>

Fix a separable closure $K\subset K^s$. Let $G$ be the Galois group of $K$. Define a functor
$$\varepsilon:\Et(K)\to G-\Set$$
that sends $L_i$ to the set of embeddings of $K$-algebras $L_i\hookrightarrow K^s$.

<div class="theorem">
$\varepsilon$ is an equivalence of categories that preserves the topologies.
</div>
**Proof**. Given an extension of separable extensions of $K$, say $L\subset M$, you already know from your algebra childhoods that any embedding $L\hookrightarrow K^s$ extends to an embedding $M\hookrightarrow K^s$. The rest is up to you. QED

<div class="corollary">
There is a natural equivalence of categories between sheaves of abelian groups on $\Et(K)$ and discrete continuous $G_K$-modules.
</div>

This is why Galois cohomology is a special case of etale cohomology. Don't worry, we'll dig into this later.

### The etale site of a scheme

#### Quick reminder about etale maps

<div class="lemma">
Let $f:U\to X$ be a morphism of schemes that is locally of finite presentation.
The following are equivalent:

1. the sheaf $\Omega_{U/X}^1$ vanishes, and $f$ is flat;
2. $f$ is smooth of relative dimension $0$
3. for every $u\in U$ with image $x\in X$, there is an affine neighborhood $\Spec A$ of $x$ in $X$ and an affine neighborhood $\Spec B$ of $u$ in $U$ such that $f(U)\subset V$ and via $f$ we have an isomorphism $$B\cong A[x_1,\ldots,x_n]/(f_1,\ldots,f_n),$$ where the Jacobian matrix $|\partial f_i/\partial x_j|$ is invertible in $B$.
4. given a square-zero extension $A\to A_0$ of rings, the map $$h_U(A)\to h_U(A_0)\times_{h_X(A_0)}h_X(A)$$ is bijective. In other words, in the commutative diagram $$\require{AMScd} \begin{CD} \Spec A_0 @>>> U\\ @VVV @VVV \\ \Spec A @>>> X\end{CD}$$ there is exactly one diagonal arrow from the lower left to the upper right. (This is the *infinitesimal lifting property*.)
</div>
**Idea of Proof**: To compare (1) and (2), we need only remark that the rank of $\Omega^1_{U/X}$ is an upper bound on the relative dimension, achieving it precisely when $f$ is smooth. To see that (1) and (3) are the same: suppose (1) is true and choose some local finite presentation $$B=A[x_1,\ldots,x_n]/(f_1,\ldots,f_m).$$ Since we assume that $\Omega_{B/A}^1=0$, we see from the usual formulae that (without loss of generality) $f_1,\ldots,f_n$ have the property that the Jacobian matrix $|\partial f_i/\partial x_j|$ is invertible (after possibly localizing slightly). In particular,  There is a natural surjective map $$g:A[x_1,\ldots,x_n]/(f_1,\ldots,f_n)\to B.$$ By the magic of flatness, are reduced to showing that $g$ is an isomorphism after base change to the residue field of $x\in\Spec A$, so we may assume that $A$ is a field. The condition on $\Omega^1$ implies that $B$ is a product of finitely many separable field extensions, and similarly for $A[x_1,\ldots,x_n]/(f_1,\ldots,f_n)$. The only surjections here are given by projecting to factors, in which case they are also localization maps (at single elements). But adding one variable $z$ and a relation of the form $zf=1$ with $f$ invertible at $u$ does not change the fact that we have a presentation with Jacobian invertible at $u$.

To see that (4) is equivalent to the others: first, reduce to the case in which everything in sight is affine. The universal property of $\Omega^1_{X/U}$ shows that any diagonal lift is unique, so it remains to show that it exists, and we can check this locally (by uniqueness). Using an expression of the form $B=A[x_1,\ldots,x_n]/(f_1,\ldots,f_n)$, we can study lifts by lifting the $x_i$. So we need to understand how to ensure that we can choose lifts satisfying the equations $f_1,\ldots,f_n$. Well, two lifts $$\mathbf{x}:=(\widetilde{x}_1,\ldots,\widetilde{x}_n)$$ and $$\mathbf{x}':=(\widetilde{x}'_1,\ldots,\widetilde{x}'_n)$$ in $A^n$ differ by an element of $I^n$, say $$\mathbf{x}'=\mathbf{x} + \mathbf{i}.$$ Using calculus, we see that the vectors $$\underline f(\mathbf{x}') = \underline f(\mathbf{x}) + J\mathbf{i}.$$ Since $J$ is invertible, we can arrange for a lift satisfying $\underline f(\mathbf{x})=0$, as desired.

To go in the other direction, start with $B=A[x_1,\ldots,x_n]/(f_1,\ldots,f_m)$. Lifts are determined by lifting the images of the $x_i$ as before. If the Jacobian is not invertible near $u$, we can generate equations for a square $0$ extension that does not admit a lifting: just see what the Jacobian can do and force yourself to exist outside of its image! Once the unique lifting property holds, we end up having $B=A[x_1,\ldots,x_n]/(f_1,\ldots,f_n)$ near $u$, as before, and this algebra happens to be flat, which finishes the equivalence. QED

<div class="lemma">
If $f:U\to X$ and $g:V\to X$ are etale, then any $X$-map $h:U\to V$ is also etale.
</div>
**Proof**. Use the infinitesimal lifting property! QED

#### Definition of the site

The objects of $\Et(X)$ are etale morphisms $U\to X$, and the arrows are $X$-arrows. A covering is a collection of maps $\{U_i\to U\}$ that are jointly surjective.

#### The big etale site

Just like with topological spaces, we can define the *big* etale site. The category is all $X$-schemes, and the coverings are maps $\{U_i\to U\}$ that are each etale, and that are jointly surjective.

### A few examples of etale sheaves

Fix a base scheme $X$. Let's define some functors on the big etale site of $X$.

- $\G_m:U\mapsto \mathscr{O}_U(U)^\times$
- $\G_a:U\mapsto \mathscr{O}_U(U)$
- $\mu_n:U\mapsto \G_m(u)[n]$
- $\alpha_p:U\mapsto\{a\in\mathscr{O}_U(U) | a^p = 0\}$ (when $p\cdot 1=0\in\mathscr{O}_X(X)$)
- Let's make more!

Why are any of these things *sheaves* in the etale topology?

<div class="proposition">
Given a scheme $X$, the functor $$\ms O:\ET(X)^\circ\to\Set$$ that sends $Y\to X$ to $\ms{O}_Y(Y)$ is a sheaf in the etale topology.
</div>
**Proof**. First, let's treat the case of a finite covering $\{\Spec B_i\to\Spec A\}$ of affines. The ring extension $A\to\prod B_i$ is thus faithfully flat. The sheaf condition is equivalent to the statement that the diagram $$A\to B\rightrightarrows B\tensor_A B$$ is exact (i.e., $A$ is the equalizer of the two maps from $B$ to $B\tensor_A B$ given by sending $b$ to $b\tensor 1$ and $1\tensor b$.)

Here's a great trick. **Remember this trick for the rest of your lives**. To check that the sequence is exact, it is enough (in fact, it is equivalent) to check that the base change of the sequence to $B$ is exact, *because $A\to B$ is faithfully flat*. What is this good for? Well, if we replace the starting map $A\to B$ with $B\to B\tensor_A B$, then we end up with a faithfully flat ring map $A'\to B'$ that admits a retraction $B'\to A'$. In other words, we may assume that there is a map $B\to A$ retracting $A\to B$, which means that there is a decomposition $B=A\oplus M$ with $M$ a faithfully flat $A$-module.

The sequence of interest now becomes $$A\to A\oplus M\rightrightarrows (A\oplus M)\tensor_A(A\oplus M),$$
which we can write as $$A\to A\oplus M\rightrightarrows A\oplus M\oplus M\oplus M\tensor_A M,$$ and now the last two arrows send $(a, m)$ to $(a, m, 0)$ and $(a, 0, m)$. The only way these can be the same is if $m=0$, as desired.QED

<div class="corollary">
All of the functors in the above list are sheaves.
</div>
**Proof**. Do it! QED

Here's one: remember our quadratic equation $x^2-x-t\in k[x,t]$ with $\ch(k)=2$? 

<div class="exercise">
Show that the above equation defines a finite etale morphism $C\to\A^1$. Show that this is a "locally constant sheaf of finite sets in the etale topology of $A^1$.
</div>

### One more site to think about

Here is the almost-mother of all sites (the real mother is something we might or might not discuss -- it's actually quite subtle).

<div class="definition">
Given a scheme $X$, the *fppf site of $X$* is the Grothendieck topology on $\Sch_X$ whose coverings are collections of morphisms $\{U_i\to U\}$ such that 

1. each $U_i\to U$ is flat and locally of finite presentation
2. the map $\sqcup U_i\to U$ is surjective on points (i.e., is faithfully flat)
</div>

Here are a few exercises to help you feel these things out a bit.

<div class="exercise">
Try these:

1. Show that any sheaf in the fppf topology is a sheaf in the etale topology, and any sheaf in the etale topology is a sheaf in the fppf topology.
2. Make an example of a sheaf in the big etale topology of $\Spec K$ that is not a sheaf in the fppf topology.
3. Given a morphism of schemes $f:Y\to X$ and a quasi-coherent sheaf $F$ on $Y$, for each $i$ we can define a functor on $\Sch_X$ that sends $T$ to $\R^i (f_T)_\ast F_T$, the **Zariski** higher direct image of the pullback of $F$ to $Y_T$. Is this a sheaf on the big etale site of $X$? On the fppf site?
4. Is there a "small fppf site of $X$"?
</div>

### Content contributors

@maxlieblich, @haochenuw
