# Grothendieck topologies, presheaves, and sheaves


Recall the definition of a Grothendieck topology.

<div class="definition">
  A *Grothendieck topology* is a category $C$ with a collection of coverings $\{U_i\to U\}{i\in I}$ for each $U\in C$ such that 

  (1) Any isomorphism is a covering.
  (2) If $\{U_i\to U\}$ is a covering, and for each $i$ we have a covering $\{V_{ij}\to U_i\}$, the total collection $\{V_{ij}\to U\}$ is a covering.
  (3) If $\{U_i\to U\}$ is a covering and $V\to U$ is arbitrary, then each $U_i\times_U V$ exists and $\{U_i\times V\to V\}$ is a covering.
</div>

**IMPORTANT**: we have to let $i=j$ in the above!!!

A category with a Grothendieck topology is often called a *site*.

<div class="example">
The category of open subsets of a topological space is a Grothendieck topology in a natural way.
</div>

<div class="example">
Let $C$ be the category of sets, and suppose a covering $\{U_i\to U\}$ is a collection of maps whose union is surjective. Let's check the three properties.

1. An isomorphism is surjective.
2. If $A=\cup B_i$ and $B_i = \cup D_{ij}$, then certainly $A=\cup D_{ij}$. Now apply this to images.
3.  If $A\to B$ is a surjective map of sets and $D\to B$ is arbitrary, then $A\times_B D\to D$ is surjective.
</div>

<div class="example">
What about letting $C$ be the category of *schemes*, and taking coverings to be collections of maps $\{U_i\to U\}$ such that $\sqcup U_i\to U$ is scheme-theoretically surjective. Does this work? (If you feel weird, use varieties or some such thing.)
</div>

<div class="example">
Let $C$ be the category of $C^\infty$-manifolds, and say that a covering is a collection of submersions $\{U_i\to U\}$ such that $\sqcup U_i\to U$ is surjective. One funny quirk: a submersion has local sections everywhere. Does this mean that this topology can be compared to the classical one somehow? For example, do they have the same sheaves? (What is a sheaf?) 
</div>

<div class="example">
We can modify the above example: fix a manifold $X$, and define the category of interest to be maps of manifolds $Y\to X$ that are everywhere local isomorphisms. This is equivalent to the statement that the tangent map is an isomorphism everywhere.

Why is this closed under fiber products? What else do we have to check?

Let's call this the *small submersion topology*.
</div>

<div class="example">
Given any Grothendieck topology on $C$ and an object $X\in\C$, we get one on the slice category $C_{/X}$, by working relative to $X$ everywhere. What are the coverings of $X$ in this topology?
</div>

### The canonical topology

Every category comes with a *canonical* topology.

<div class="definition">
A morphism $f: X \to Y$ in a catagory $C$ is an *epimorphism* if for any two morphism $g_1, g_2: Y \to Z$, $g_1 \circ f = g_2 \circ f$ implies $g_1=g_2$. 
</div>

An alternative way to say this is that a morphism $f: X \to Y$ is an epimorphism if the $\Hom(-,Z)$ functor sends $f$ to an injection:
$$ \forall Z \in C, \Hom(Y, Z) \hookrightarrow \Hom(X,Z). $$ 

In the category of sets, epimorphism are surjective maps. In the catagory of rings however, the map $\mathbf{Z} \to \mathbf{Q}$ is an epimorphism but not a surjection.
</div>

<div class="definition">
In a category $C$ that admits fiber products, an epimorphism $f: X \to Y$ is *effective* if for all $Z$, the diagram
$$\Hom(Y,Z)\to\Hom(X,Z)\rightrightarrows\Hom(Y\times_X Y, Z).$$ is exact.
</div>

Another way to view this property is to say that the following diagram is both Cartesian and Cocartesian, i.e. that the fiber product is the limit and that $Y$ is the colimit:

$$
\begin{array}{ccc}
  X \times_Y X & \rightarrow  & X \\
  \downarrow & & \downarrow \\
  X & \rightarrow & Y
\end{array}
$$

In an abelian category all epimorphisms are effective. For an example of an epimorphism that is not effective consider the identity map between the real line with the discrete topology and the real line with the standard topology. This map is continuous and since it is surjective it is an epimorphism.  This is not an effective epimorphism since the diagram above fails to be Cocartesian. The map from the discrete line to itself that swaps two points does not factor through the standard line. Another example is the map $\mathbf{Z} \to \mathbf{Q}$ from before.
</div>

<div class="definition">
An effective epimorphism is *universal* if it is stable under base change, i.e. given a map $W \to Y$ the map $X \times_Y W \to W$ is also an effective epimorphism.
</div>

<div class="definition">
The *canonical topology* on $C$ is the topology with coverings given by collections of maps $\{U_i\to U\}$ such that $\sqcup U_i\to U$ is a universal effective epimorphism.
</div>

### Presheaves and sheaves

Now we can mimic the old (categorical) definitions! Fix a category $S$ that is closed under products (for example, sets, abelian groups, rings, schemes, sheaves on a fixed topological space, etc.).

<div class="definition">
A *presheaf* on $C$ with values in $S$ is a functor $$F:C^\circ\to S.$$
</div>

<div class="definition">
A presheaf $F:C^\circ\to S$ is a *sheaf* if for every covering $\{U_i\to U\}$, the diagram $$F(U)\to\prod F(U_i)\rightrightarrows\prod F(U_i\times_U U_j)$$ is exact.
</div>

<div class="example">
In the canonical topology on $C$, the functor $h_X:C^\circ\to\Set$ is a sheaf. (Why?)
</div>

<div class="exercise">
Is the canonical topology the "smallest" topology such that every representable functor is a sheaf? Is it the "largest"? Is it anythingest?
</div>

### Example: the sheaves on the "submersion topology" of a manifold

Let $C$ be the small submersion topology of a manifold $X$. Among the objects of $C$ are the open subsets $U\subset X$; open coverings of open sets are coverings in the small submersion topology.

<div class="claim">
Restricting to the subcategory of open subsets of $X$ gives an equivalence between sheaves of sets on $C$ and sheaves on the topological space of $X$.
</div>
**Proof**. Any covering $\{U_i\to U\}$ can be covered as $\{V_{ij}\to U_i\}$ such that each $V_{ij}\to X$ is an open embedding. QED

<div class="exercise">
What are the universal effective epimorphisms in the category $C$?
</div>

### Morphisms of topologies

Now that we have our categorical analogue of topological spaces, how do we simulate continuous maps?

<div class="definition">
Given categories $C$ and $C'$ with Grothendieck topologies, a *morphism of topologies* is a functor $F:C\to C'$ such that

- for every covering $\{U_i\to U\}$ in $C$, the image $\{F(U_i)\to F(U)\}$ is a covering
- for every covering $\{U_i\to U\}$ in $C$ and every morphism $V\to U$ in $C$, the canonical map $$F(U_i\times_U V)\to F(U_i)\times_{F(U)} F(V).$$ (Special case of this condition: $C$ and $C'$ have fiber products and $F$ preserves them. This is equilavent to $F$ preserving finite limits, also sometimes called "continuous" -- now you know why!)
</div>

Everybody's favorite example: $C=\Open(X)$, $C'=\Open(Y)$, $F$ is the pullback map induced from a continuous map $Y\to X$.

<div class="question">
Does a continuous map of topological spaces induce a morphism of *big* topologies? Does a morphism of big topologies always come from a continuous map of topological spaces?
</div>
