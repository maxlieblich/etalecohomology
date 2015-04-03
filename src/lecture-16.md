# Examples of Stacks

It is recommended that everyone read Barbara Fantechi's [Stacks for Everybody](http://www.mathematik.uni-bielefeld.de/~rehmann/ECM/cdrom/3ecm/pdfs/pant3/fantechi.pdf)

### Reminder: Definition of a Stack

Recall the following definition: if $C$ is a site and $G$ is a category fibered in groupoids over $C$, then $G$ is a *stack* if for all $c \in C$, $g, g' \in G(c)$, $\text{Isom}(g,g') : C/c \rightarrow \underline{\text{Set}}$ is a sheaf and for any cover $d \rightarrow c$, descent is effective, i.e. $G(c) \rightarrow D_{d/c}^G$ is an equivalence.

### Example 1: Quasi-coherent Sheaves

Let $C$ be the category of schemes with fppf topology, $G$ the category of quasi-coherent sheaves (one can see this is a CFG by thinking of the pseudo-functor sending schemes $X$ to the category of quasi-coherent sheaves over $X$ and $f$ to $f^*$).

<div class="theorem"> $G \rightarrow C$ is a stack. </div>
**Proof**. Given any scheme $X$, and quasi-coherent sheaves $Q_1, Q_2$, then $\text{Isom}(Q_1, Q_2) : \text{Sch}_X \rightarrow \underline{\text{Set}}$ sending $Y \rightarrow X$ to $\text{Isom}(Q_1|_Y, Q_2|_Y)$ is an fppf sheaf on $X$, in fact a subsheaf of the Hom sheaf: $f : Q_1 \rightarrow Q_2$ is an isomorphism if and only if there exists a $Y \rightarrow X$ an fppf cover such that $f_Y$ is an isomorphism.

Next, descent is effective for quasi-coherent sheaves; this was shown last quarter: reduce to the affine case and use Grothendieck's trick.

### Example 2: Sheaves

We don't need to restrict the above to quasi-coherent sheaves. If $C$ is the category of schemes, $G$ the category of all sheaves, then $G \rightarrow C$ also forms a stack.

### Example 3: Torsors

If $C$ is any site, $\Gamma$ a sheaf of groups on $C$, then define for each $c \in C$ $B\Gamma(c)$ to be the groupoid of left $\Gamma|_c$-torsors in $Sh(C/c)$. This consists of $T$ with a map $\Gamma \times T \rightarrow T$ such that:
* "Whenever $T$ has a point $t$, the map $\Gamma \rightarrow T$ by $\gamma \mapsto \gamma t$ is an isomorphism"
* "$T$ has a point over a covering"

A subexample of this is $C = \text{Sch}$ and $\Gamma = \mathbb{G}_m$, so $B\mathbb{G}_m$ is the groupoid of invertible sheaves on $C$.

There is also the stack of "representations of $\Gamma$", which is the stack of sheaves on $B\Gamma$.

### Example 4: Quotient Stacks

Let $X$ be a scheme acted on by a group scheme $G$. Then define the stack $[X/G]$ via sending $Y$ to the groupoid of $\{Y \leftarrow T \rightarrow X \}$ where $T\rightarrow Y$ is a $G$-torsor and $T \rightarrow X$ is $G$-equivariant, where isomorphisms of such objects are isomophisms of the torsors where all diagrams commute.

The idea here is we are forming out of thin air an ideal quotient: $X \rightarrow [X/G]$ is a $G$-torsor and it is specifically constructed such that for any morphism $Y \rightarrow [X/G]$, a $G$-torsor $T$ over $Y$ must have a compatible $G$-map through $X$.

A concrete subexample of this is the action of $\mathbb{G}_m$ on $\mathbb{A}^{n+1}/\{0\}$ via $\gamma(a_1, \dots, a_{n+1}) = (\gamma^{p_1} a_1, \dots, \gamma^{p_{n+1}} a_{n+1})$ where the $p_i$'s are some power.
