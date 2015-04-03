## Some examples of Azumaya algebras

Let $R$ be a (unital) ring such that $2\in R^{\times}$ and let $a,b \in R^{\times}$. Inspired by quaternion algeras, one can define an algebra $(a,b)$ generated over $R$ by $i,j$ with the relations $$i^2 = a, j^2 = b, ij+ji = 0$$.
One can check that it gives rise to an Azumaya algebra over $\text{Spec}R$, as it splits over $R[\alpha]/(\alpha^2 - a)$.

For example, consider the algebra $A = (-1,-1)$ over $\mathbf{Z}[1/2]$. Since the generic fiber $(-1,-1)_{\mathbf{Q}}$ is not split, then $A$ is not trivial, yet one can see that for every closed point $\mathfrak{p}\in\text{Spec}\mathbf{Z}[1/2]$ the algebra $(-1,-1)_{k(\mathfrak{p})}$ is trivial. Also, for every prime $p\neq 2$, the algebra $(-1,-1)_{\mathbf{Z}_p}$ is trivial.

### The Brauer group of a scheme

<div class="definition">
Let $X$ be a scheme. The Brauer group of $X$ is the set of Azumaya algebras on $X$ modulo the following equivalence: $\mathcal{A}\sim\mathcal{B}$ if there are two locally free nowhere zero sheaves $V,W$ of finite rank such that $\mathscr{A}\oplus\mathcal{E}nd(V)\simeq\mathscr{B}\oplus\mathcal{E}nd(W)$.
</div>

This is actually a group, and the group operation is given, as one can imagine, by taking the tensor product of two Azumaya algebras.

A few remarks:
- We have that $$\mathscr{E}nd(V)\otimes\mathscr{E}nd(W)\simeq\mathscr{E}nd(\otimes W)$$, just like $M_n(k)\otimes_k M_m(k)\simeq M_{mn}(k)$.
- The identity element of $Br(X)$ is the class of $\mathscr{O}_X$: indeed, one can check that $\mathscr{A}\sim$ \mathscr{O}_X$ iff there is a locally free sheaf $V$ such that $\mathscr{A}\simeq \mathscr{E}nd(V)$, i.e. $\mathscr{A}$ is trivial.
- If $X=\text{Spec} k$ for some field $k$, then an Azumaya algebra on $X$ corresponds to a central simple algebra over $k$, and $Br(X)\simeq Br(k)$.

As for computing inverses, exactly like in the case of central simple algebras over a field, there is an isomorphism
$$
\mathscr{A}\otimes \mathscr{A}^o \to \mathscr{E}nd(\mathscr{A})
$$
Thus $[\mathscr{A}^o] = -[\mathscr{A}]$ in $Br(X)$.

Actually, one can prove that $\mathscr{A}\sim \mathscr{B}$ iff $\mathscr{A}\otimes\mathscr{B}^o \simeq \mathscr{E}nd(V)$ for some locally free sheaf $V$ of finite rank.

We will see that the Brauer group of $\mathbb{P}^n_{\mathbf{C}}$ is trivial: this really means that any Azumaya algebra on $\mathbb{P}^n_{\mathbf{C}}$ is the endomorphism ring of a locally free sheaf!

### Structure theory

Let $\mathscr{A}$ be an Azumaya algebra on $X$ of rank $n^2$: we say that $n$ is the degree of $\mathscr{A}$. In the same way as we did for central simple algebras, we can define a functor
$$
I: Sch_X\to \Set
$$
by $I(Y) = Isom_Y(\mathscr{A}_Y, \mathscr{M}_n(\mathscr{O}_Y))$. Observe that $I\to X$ is a $PGL_n$-torsor, and the same argument as in the case of fields allows us to get bijections from $H^1(X_{et}, PGL_n)$ to the set of Azumaya algebras of degree $n$ on $X$ and to the set of all proper smooth morphisms $P\to X$ that etale-locally look like $\mathbb{P}^n_X\to X$.
