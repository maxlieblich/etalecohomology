** Last Time **
We had an algebraic and cohomological version of the association of an Azumaya algebra with a $\mathbb{G}_m$-gerb.
Cohomology version:
$$H^1(X,\mathbb{GL}_n)\rightarrow H^1(X,\mathbb{PGL}_n)\xrightarrow{\delta} H^2(X,\mathbb{G}_m)$$
Geometric version:
$$\{\text{vector bundles}\}\rightarrow \{\text{$\mathbb{PGL}_n$-torsors}\}\rightarrow \{\text{$\mathbb{G}_m$-gerbs}\}$$

In the cohomology version, info gets pushed around.  In the geometric version, gluing happens.

** General Question ** 
What is the deal with the moduli of Azumaya algebras?
Equivalently, what is the deal with the moduli space of $\mathbb{PGL}_n$-torsors?

More specific: $\alpha\in H^2(X,\mathbb{G}_m)$, what is the space of Az. algebras of degree $n$ such that $\delta([A]) = \alpha$?
We want to quantify the failure of $\delta$ to be injective.
More more specific: take $\alpha = 0$
Azumaya algebras of degree $n$ with trivial Az. class: $A = \mathcal{End}(V)$, with $V$ rank $n$
Then by Skolem-Noether, $\mathcal{End}(V) \cong \mathcal{End}(W)$ if and only if there exists an invertible line bundle $L$ such that $V = L\otimes W$.
Moral of the story: $\delta^{-1}(0) = \text{Bun}_n(X)/\text{Pic}(X)$

Discussion of this led to the following
** Kenjecture **
If $X$ is a smooth, projective variety over $k = \overline{k}$, then any locally free $\mathcal O_X$-module $V$ splits as a direct sum of invertible sheaves if and only if $X = \spec(k)$ or $X = \mathbb{P}^1_k$.

Another tidbit:
$H^2(X,\mathbb{G}_m)$ corrsponds to isomoprhism classes of $\mathbb{G}_m$-gerbs.

** Very Old Question **
When does the Brauer group surject onto the torsion component of $H^2(X,\mathbb{G}_m)$?
Geometric version of very old question:
Given a $\mathbb{G}_m$-gerb $\mathcal X\rightarrow X$, how can we tell if there is an Azumaya algebra $A$ such that $\mathcal{X}_A$ is isomorphic to $\mathcal X$ as $\mathbb{G}_m$-gerbs over $X$?

Sort of answer:
There exists $A$ such that $\mathcal{X}\cong\mathcal{X}_A$ if and only if there exists a locally free sheaf $V$ on $\mathcal X$ such that the stabilizer $\mathbb{G}_m$-action on $V$ is scalar multiplication.  Then $A = \pi_*\mathcal{End}(V)$.

This sort-of answer is useful because it is portable -- can base change it, descend, etc.

Using this, we can charaterize when $\mathcal X\in H^2(X,\mathbb{G}_m)$ is trivial.  In particular $\mathcal X$ is trivial if and only if there exists an invertible sheaf $\mathcal L$ on $\mathcal X$ such that the $\mathbb{G}_m$-action is scalar multiplication.

We also now have a silly proof that the Brauer group is torsion:
$A$ corresponds to $\mathcal{X}_A$ and a locally free sheaf $\mathcal{V}$ of rank $r = \deg(A)$.  Then $\Lambda^r\mathcal{V}$ is invertible and the $\mathbb{G}_m$-action is by $r$th powers. Therefore $r[\mathcal X_A] = 0$.


