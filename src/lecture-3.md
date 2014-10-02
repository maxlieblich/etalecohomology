# Standard examples

### $G$-sets

Let $G$ be a group, and let $C$ be the category of sets with a left $G$-action. **Variant**: let $G$ be a *profinite* group, and let $C$ be the category of finite sets with a *continuous* (left) action. Define a covering to be a collection of $G$-equivariant maps $\{U_i\to U\}$ such that $\sqcup U_i\to U$ is surjective.

<div class="exercise">
Show that we have just described the canonical topology on $C$.
</div>

Given a sheaf $F:C^\circ\to\Set$, we can make $F(G)$ into a $G$-set: (first, $G$ acts on the left on $G$ by translation) $$g:F(G)\to F(G)$$ is defined to be the map induced by the map of left $G$-sets $$G\to G: a\mapsto a g^{-1}.$$

<div class="claim">
Every sheaf $F$ on $C$ is representable by $F(G)$ with the above action.
</div>
**Proof**. Given a $G$-set $U$, we need to find a functorial isomorphism $$F(U)\to\Hom_C(U, F(G)).$$ We can write $U$ is a disjoint union of orbits $U=\sqcup U_i$, and **the sheaf property tells** us that this decomposition induces a canonical isomorphism $F(U)=\prod F(U_i)$. Thus, it suffices to show this for $U$ that consist of a single $G$-orbit.

But then there is a covering of the form $G\to U$ (given by choosing an element $u\in U$ and letting $G$ act). The sheaf property says that $F(U)$ is idenfied with the the equalizer of $$F(G)\rightrightarrows F(G\times_U G).$$ Having chosen $u$, let's write $U = G/H$ for $H$ a subgroup of $G$. Two elements of $G$ map to the same element of $G/H$ if and only if they are in the same coset. Thus, an element of $G\times_U G$ has the form $(g, gh)$ for some $h\in H$. This gives an isomorphism of $G$-sets $$G\times_U G\to G\times H,$$ where the $H$ factor in the latter has a trivial $G$-action. In other words, $$G\times_U G\cong \sqcup_{h\in H} G$$ as $G$-sets. This admits a right $H$-action that simply permutes the factors.

By the sheaf property, we conclude that 
$$F(G\times_U G)\cong \prod_{h\in H} F(G).$$
What are the maps $F(G)\to \prod_HF(G)$? The first one is the diagonal map, while the second one is the product of the maps $F(G)\to F(G)$ given by the right action of $H$. The equalizer of the maps is precisely the $H$-invariant part of $F(G)$.(Question from Hao: Why is the first map diagonal and second map as claimed?)

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

Let $K$ be a field. Let $\Et(K)$ be the opposite of the category of finite semisimple commutative $K$-algebras. By the classical structure theory, the objects of $C$ are $K$-algebras of the form $\prod L_i$ where each $L_i$ is a finite separable extension of $K$. In other words, $\Et(K)$ is the category of $K$-schemes of the form $\sqcup\Spec L_i$ with each $L_i$ a finite separable extenson of $K$.

A covering $\{U_i\to U\}$ in $C$ is a collection of maps such that $\sqcup U_i\to U$ is set-theoretically surjective.

<div class="exercise">
Show that this is a site. Please.
</div>

Fix a separable closure $K\subset K^s$. Let $G$ be the Galois group of $K$. Define a functor
$$\varepsilon:\Et(K)\to G-\FinSet$$
that sends $L_i$ to the set of embeddings of $K$-algebras $L_i\hookrightarrow K^s$.

<div class="theorem">
$\varepsilon$ is an equivalence of categories that preserves the topologies.
</div>
**Proof**. Given an extension of separable extensions of $K$, say $L\subset M$, you already know from your algebra childhoods that any embedding $L\hookrightarrow K^s$ extends to an embedding $M\hookrightarrow K^s$. The rest is up to you. QED

<div class="corollary">
There is a natural equivalence of categories between sheaves of finite abelian groups on $\Et(K)$ and finite abelian $G_K$-modules.
</div>

Do you see where this is going? Cohomology!
