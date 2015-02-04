# Brauer groups: introduction

The real numbers $\mathbf{R}$ and the complex numbers $\mathbf{C}$ are normed fields that can be interpreted as points on a line and a plane respectively. In 1843, Hamilton was looking for a way to do the same for 3-space. In retrospect this is impossible. We want an $\mathbf{R}$-linear structure so that for all nonzero $\alpha \in \mathbf{R}$ the multiplication map $T_\alpha: \mathbf{R}^3 \to \mathbf{R}^3$ is bijective. Any endomorphism of $\mathbf{R}^3$ has an eigenvector so the multiplication map fails to be injective.

As Hamilton discovered, the quaternions are a normed division algebra structure for $\mathbf{R}^4$ with center $\mathbf{R}$. The quaternions, $\mathbf{H}$ have generators $i$ and $j$ with $i^2 = j^2 = -1$ and $ij = -ji$ or equivalently by $i,j$ and $k$ with $i^2 = j^2 = k^2 = ijk = -1$. The quaternions enjoy the following properties:

1. $\mathbf{H}$ is a central $\mathbf{R}$-algebra.
2. There is a conjugation map given by $\alpha = a+bi+cj+dk \mapsto a -bi-cj-dk$ and an associated norm $N(\alpha) = \alpha \bar{\alpha}$ with $N(\alpha \beta)=N(\alpha)N(\beta)$.
3. $\mathbf{H}$ is a division algebra because $N(\alpha)=0$ if and only if $\alpha=0$ so $\alpha \frac{\bar{\alpha}}{N(\alpha)} = 1$.
  
In 1878, Frobenius proved that any finite dimensional division algebra over $\mathbf{R}$ is isomorphic to $\mathbf{R}, \mathbf{C}$ or $\mathbf{H}$. In particular every finite dimensional central division algebras (CDA) over $\mathbf{R}$ is isomorphic to $\mathbf{R}$ or $\mathbf{H}$.

<div class="question">
What about other base fields $k$? Can we classify all CAD over $k$?
</div>

The commutative answer to this question is Galois theory where we use the profinite group $Gal(k^{sep}/k)$. The noncommutaive answer given by Brauer was that we can make a torsion abelian group $Br(k)$ whose elements correspond to isomorphism classes of CDA's over $k$.

### Group structure

What is the group structure of the Brauer group? Given two CDA's, $D_1$ and $D_2$ over $k$, we have $D_1 \otimes D_2 \simeq M_n(D_3)$ where $D_3$ is the endormophism ring of the unique simple right module over $D_1 \otimes D_2$. Schur's lemma insures that $D_3$ is a division algebra. The identity element is $[k]$. Let $D^\circ$ be the opposite algebra of $D$. The map $D \otimes D^\circ \to End_k(D) \simeq M_N(k)$ given by $d \otimes e \mapsto (x \mapsto dxe)$ must be injective since $D \otimes D^\circ$ is a central simple algebra and since both spaces are the same dimension it must be an isomorphism. This tells us that the inverse $-[D]$ of an element in the Brauer group is the opposite algebra $[D^\circ]$. For example, $\mathbf{H}^\circ = \mathbf{H}$ since $\mathbf{H}$ is the only nontrivial element of $Br(\mathbf{R})$. In this case the isomorphism is by conjugation.

<div class="question">
Is there a natural topology on $Br(k)$?
</div>

<div class="question">
What is the order of $[D]$ in $Br(k)$?
</div>

Quobservation: The map $k \mapsto Br(k)$ is a functor $\underline{Fld} \to \underline{Grp}$. Given a field extension $K \hookrightarrow L$ the induced map $Br(K) \to Br(L)$ given by $[D] \mapsto D \otimes_K L$ sends a CDA over $K$ to a CDA over $L$. How do we study/find/construct $K$ such that $D \otimes L \simeq M_n(L)$?

<div class="question">
What is $gcd\{ deg(L/K) | D \otimes L \simeq M_n(L)\}$?
</div>

<div class="question">
We have seen that $Br(\mathbf{R}) \simeq Gal(\mathbf{R})$. Is this always true? (No.) Is there always a map from the Brauer group to the Galois group?
</div>

<div class="question">
What other groups can we associate with a field? A few examples are $H^i(Spec k, \mathbf{G}_m)$, $H^i(Spec k, \mathbf{Z}(m))$ and $H^i(Spec k, \mathbf{Z}/n(m))$. 
</div>

Key Goal: Relate the Brauer group to etale cohomology groups.

Cool results: let $\alpha = [D] \in Br(k)$. Define the period, $per(\alpha)$, to be the order of $\alpha$  in $Br(k)$. Define the index, $ind(\alpha)$, to be $gcd\{ deg(L/K) | D \otimes L \simeq M_n(L)\}$. Then the period divides the index and they have the same prime factors. 