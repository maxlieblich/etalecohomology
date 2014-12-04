# Descent theory

In the world, you learned about gluing sheaves together. I.e., given an open cover $\{U_i\subset X\}$ of a topological space, some sheaves $F_i$ on $U_i$, and gluing isomorphisms $\phi_{ij}:F_i\to F_j$ over $U_i\cap U_j$ that satisfy

- $\phi_{ii}=\id$
- $\phi_{jk}\circ\phi_{ij}=\phi_{ik}$ over $U_i\cap U_j\cap U_k$, 

you can "glue" these sheaves together to form a sheaf over all of $X$. This is a fundamental operation that helps you do everything you do.

What about for these exotic topologies? What does gluing even mean? Can we do it?

## Gluing = "descent theory"

One of the triumph's of Grothendieck's theory is that the gluing operation from your youth aligns perfectly with the theory of descent that started appearing in the 1930s (I made this date up...fix and make a pull request). Here's our first pass at it.

### Restricting sheaves

Let $C$ be a site and $X$ an object of $C$. Given a sheaf $F$ on $C$, we can define the *restriction* of $F$ to $X$, denoted $$F|_X:C_{/X}\circ\to\Set$$ by sending an arrow $Y\to X$ to $F(Y)$. (Why is this a sheaf?) From the description, it is clear that restriction to $X$ is a functor $$\Sh(C)\to\Sh(C_{/X}).$$

We can further restrict: given a morphism $Y\to X$ and a sheaf $F$ "on" $X$ (i.e., a sheaf on $C_{/X}$), we can further restrict it to $Y$. In particular, we can restrict a sheaf to all elements of a covering.

Note: this is just $f_i^{-1}$, where $f_i:U_i\to X$ is the structure map. As such, restriction is exact.

### The category of descent data

Given a covering $\{U_i\to X\}$ in a site $C$, define a category $$\Desc_{\{U_i\}}$$ as follows: the objects are tuples $(F_i, \phi_{ij})$, where $F_i\in\Sh(U_i)$ and $\phi_{ij}:F_i|_{U_i\times_X U_j}\to F_j|_{U_i\times_X U_j}$$ are isomorphisms between the restriction such that 

- $\phi_{ii}=\id$ for all $i$, and
- for all $i, j, k$, we have $\phi_{jk}\circ\phi_{ij}=\phi_{ik}$ on $U_i\times_X U_j\times_X U_k$. (Worry: what does it mean to restrict a sheaf, and then to restrict a map? Is it truly canonical? Should we panic?)

Given a sheaf $F$ on $X$, we get an object of $\Desc_{\{U_i\}}$ by sending $F$ to $(F|_{U_i})$, with the $\phi_{ij}$ given by the canonical composition of restriction functors. This gives a functor
$$\delta:\Sh(X)\to\Desc_{\{U_i\}}.$$
The classical idea of gluing sheaves can be incarnated like this:

<div class="proposition">
The functor $\delta$ defined above is an equivalence of categories.
</div>
**Proof**. Given an object of $\Desc$, let's define an object $G$ of $\Sh(X)$. Here's how: first, write $f_i:U_i\to X$ for the structure map. The maps $\phi_i$ give a diagram
$$\prod (f_i)_\ast F_i\to\prod (f_{ij})_\ast (F_i)|_{U_i\times_X U_j}\to\prod (f_{ij})_\ast (F_i)|_{U_i\times_X U_j}.$$ Let $G$ be the kernel of this map. By definition and adjunction, there are maps $G|_{U_i} F_i.$ In fact, pulling the whole diagram back to $U_i$ and using the cocycle condition, we see that in fact these maps are ismorphisms. Etc. (I'll do this again below.) QED

### A "point-theoretic" view of gluing

Here's another way to think about gluing data. We will assume various things, like that $\sqcup U_i$ exists, without dwelling on them. 

**Question**: If we were to try "gluing a sheaf on a bundle" $E\to B$, what would we need in order to make the gluing work?
**Answer**: We need the sheaf to be constant on fibers. That is, we would need to have a system of comparison isomorphisms $\phi_{t_1t_2}:F_{t_1}\to F_{t_2}$ for any two points $t_1, t_2$ in a fiber of the bundle projection $E\to B$. We also need these to be consistent, so we need $\phi_{tt}=\id$ and $\phi_{t_2t_3}\phi_{t_1t_2}=\phi_{t_1t_3}$.

By Yoneda's lemma, a descent datum is precisely this, but for points of $\sqcup U_i$ mapping to a fixed point of $X$, all points having values in a fixed object $T$ of $C$.

### A formal proof of gluing

Given an object $(F_i,\phi_{ij})$ of $\Desc_{\{U_i\}}$, we get a diagram
$$\prod (f_i)_\ast F_i\rightrightarrows\prod (f_{ij})_\ast F_{i}|_{U_{ij}},$$
defined as follows: 

- the map $U_{ij}\to U_i$ defines a map (using adjunction) $$(f_i)_\ast F_i\to (f_{ij})_\ast F_{ij},$$ coming from applying $(f_i)_\ast$ to the unit $\id\to(\pr_1)_\ast(\pr_1)^{-1}$;
- we change the target of the map ending in $(F_j)|_{U_{ij}}$ by applying $\phi_{ij}$.

We claim that the sheaf $F$ defined as the limit of this diagram is the sheaf we seek. Since maps between sheaves form a sheaf, and a descent diagram is a collection of maps between sheaves, it is enough to check that $F$ is canonically identified with the descent datum locally. That is, *we will show that there is a unique isomorphism between $\delta(F)$ and the original object $(F_i, \phi_{ij})$ after restricting to each $U_i$*, and the rest will follow from the fact that maps between sheaves are a sheaf.

The construction in question is compatible with restriction, so we are immediately reduced to the case in which one of the maps $U_i\to X$ admits a section $X\to U_i$. Write $U = \sqcup U_i$ and $f:U\to X$ for the structure map (this will make life easier, but you can do without this if you want). We can rewrite the descent condition: we have $\widetilde F$ on $U$, and a map $\phi:(\pr_1)^{-1}\widetilde F\to(\pr_2)^{-1}\widetilde F$ on $U\times_X U$ that satisfies the cocycle condition on $U\times_X U\times_X U$. Using the above reformulation, we see that this is equivalent to a family of comparision maps $\phi_{st}$ for any point $(x, t)\in U(T)\times_{X(T)} U(T)$ (for any $T$ in $C$).

Now, the section $\sigma:X\to U$ gives us a universal point. That is, for any $\gamma:T\to X$, we get $\sigma\gamma\in U(T)$ mapping to $\gamma$. We claim that $\sigma^{-1}\widetilde F$ gives the *unique* sheaf $G$ such that the associated canonical descent datum $(G, \can)$ is isomorphic to $(\widetilde F,\phi)$.

How do we check this? We need to produce an isomorphism $\alpha:f^{-1}\sigma^{-1}\widetilde F\to \widetilde F$ such that for any point $(s, t)\in U(T)\times_{X(T)} U(T)$ (mapping to, say $\gamma\in X(T)$) we have that the arrows $$s^{-1}\sigma^{-1}\widetilde F\to s^{-1}F$$ and $$t^{-1}\sigma^{-1}\widetilde F\to t^{-1}F$$ commute with the identifications $$s^{-1}\sigma^{-1}=\gamma^{-1}=t^{-1}\sigma^{-1}$$ and the descent datum $$\phi_{st}:t^{-1}F\to s^{-1}F.$$ There is only one choice for $\alpha$: the maps $\sigma f$ and $\id$ both map to $f$ under the map $U(U)\to X(U)$. The required commutativity follows from the descent assumption. The uniqueness comes from the cocycle condition!

As insane as this sounds, *this establishes the proof*. Our walnut shell is now pure mush.

### Now that sheaves glue, do properties glue, too?

That is, suppose each $F_i$ is quasi-coherent. Is the glued sheaf $F$ also quasi-coherent? Or suppose that each $F_i$ is representable by a scheme. Is the glued sheaf $F$ also representable by a scheme? Same question with affine schemes, or projective schemes, or flat morphisms, or anything you can think of.

<div class="theorem">
Suppose $C$ is the fppf site of a scheme. (You can actually use a strange beast called the fpqc site, but it is too technical for us right now.) If each $F_i$ is quasi-coherent then the glued sheaf $F$ is also quasi-coherent.
</div>
**Proof**. Let's recast the problem. We already know that quasi-coherence is local in the Zariski topology, so we may assume that $X$ is affine, say $X=\Spec A$. Furthermore, any fppf covering of an affine may be refined by a finite fppf covering by affines $U_i=\Spec B_i$. What does the gluing datum become? Let $B=\prod B_i$. The sheaf $F_i$ is quasi-coherent, so it is associated to some module $M_i$ over $B_i$. We get a $B$-module $M=\prod M_i$.

We also have a formula for computing the descent, in terms of pushforwards. Note that $f_\ast M$ is the $A$-module represented by $M\tensor_A B$, and the pushforward from the double overlap space is $M\tensor_A B\tensor_A B$. It is a lemma for self-contemplation that the maps between quasi-coherent sheaves the same in the Zariski topology and the fppf topology.

Let us note that the formation of the kernel $K$ of the map $M\tensor_A B\to M\tensor_A B\tensor_A B$ is compatible with the faithfully flat base change $A\to B$. Moreover, we *already know* that the kernel is *canonically (and uniquely) isomorphic* to $M$ when we make this base change. Finally, and here's the kicker, we know this after making an **arbitrary** base change $A\to C$. That is, by reducing to $C\to C\tensor_A B$, which has a section, we know that the formation of this particular kernel is actually compatible with arbitrary base change. (More formally: the map from $K$ to the kernel of the base changed diagram over $C$ is an isomorphism for any $C$, since it is an isomorphism after making the faithfully flat base change $C\to C\tensor_A B$.) This shows that the kernel is in fact quas-coherent, as desired. QED


### Cocycles as descent data

Recall that Cech cohomology always computes $\H^1$. This tells us something very nice: that classes in $\H^1$ parametrize descent data!

Recall that a cocycle in $G$ for a covering $\{U_i\to X\}$ is given by a section $g_{ij}\in G(U_{ij})$ such that $g_{ik}=g_{jk}g_{ij}$ over $U_{ijk}$. (Wait, we can even give this definition for **non-abelian** groups! Woohoo!) This is precisely a descent datum, when $G$ is acting on a sheaf. Here's a special case.

<div class="proposition">
Suppose $G=\G_m$, so $G$ is the full automorphism group of an invertible sheaf.Then the functors $\Sh(X)\to\Desc_{\{U_i\}}$ induce a bijection between the Picard group of $X$ and $\H^1(X,\G_m)$.
</div>
**Proof**. Fix one covering $\{U_i\}$ of $X$. Given an invertible sheaf $L$ on $X$ that is trivialized on each $U_i$, the canonical gluing datum in $\Aut(L|_{U_ij})$ gets transformed into a cocycle in $\G_m(U_{ij})$ via the choices of local trivializations. Changing the local trivializations changes this cocycle by a coboundary. Refining the covering does not change the class in the colimit cohomology group (by definition!). Isomorphic invertible sheaves give the same cohomology class. Any sheaf that gives the trivial cohomology class must admit a compatible system of trivializations (a priori, over some refinement) that glue to a global trivialization. QED

We have finally computed our **first** cohomology group!

## Descending other structures

We just saw something awesome: descent theory not only respects quasi-coherent sheaves, it also respects *invertible* sheaves. And since we understand the full automorphism group, we could tie that to a cohomology group.

We could ask more generally about descent theory respecting additional structures. Here are a few sample questions.

1. What about *quasi-coherent sheaves of algebras*? 
2. What about affine schemes?
3. What about projective schemes?
4. What about quasi-projective schemes?
5. What about arbitrary schemes?
6. What about $G$-torsors?
7. What about invertible sheaves?
8. What about locally free sheaves?

<div class="corollary">
Locally free sheaves glue in the fppf topology. Yes!
</div>
