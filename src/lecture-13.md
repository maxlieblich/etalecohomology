# Central simple algebras

In this lecture, we will see a few beautiful things about the building blocks of the Brauer group, the algebras themselves. A bunch of the proofs here are inspired by (or cribbed from) the beautiful book by Farb and Dennis on non-commutative algebra.

### Divison algebras, central simple algebras, and Donald Rumsfeld

In studying division algebras, we are naturally led to apply one of Rumsfeld's famous rules: "If you can't solve a problem, make it bigger." (He was *very* good at this.)

One of the deepest insights of 20th Century mathematics is the observation that rather than investigate the inner workings of a single object, it often pays to investigate associated categories. We usually think this means that we should look at the category of objects of a similar flavor, but "classical" algebra gives us a prime example this idea, due to Morita theory. I will not go into detail about Morita theory, except for its incarnation in our specific case. 

### Simple categories and matrix rings

Call an abelian category $C$ *simple* if is semisimple and there is a simple object $c$ in $C$ such that every object of $C$ can be written as a direct sum of copies of $c$ (up to isomorphism).

<div class="theorem"> (Morita-ish)
Fix an Artinian ring $A$. The category of $A$-modules is simple if and only if $A\cong M_n(D)$, the ring of matrices over a division ring $D$.
<div>
**Proof**. If the category is simple, then we can write $A$ itself as $c^{\oplus n}$ for some natural number $n$. But then $A$ (acting on the right) is the ring of endomorphisms of $A$ as a left $A$-module, while we can also compute this endomorphism ring as $M_n(\End(c))$. By Schur's lemma, $\End(c)$ is a division ring. QED

Why do we care?

<div class="lemma">
For any ring $R$, there is a natural equivalence of categories between $\Mod_R$ and $\Mod_{M_n(R)}$ for any $n>0$.
</div>
**Proof**. Exercise! (Too hard?) QED

### The Artin-Wedderburn Theorem

There is an amazing result governing the Artinian rings with simple module categories: they can be characterized algebraically!

Recall that a ring is *simple* if it has no non-trivial two-sided ideals.

<div class="theorem"> (Artin-Wedderburn, special case)
An Artinian ring $A$ is simple if and only if the module category $\Mod_A$ is simple.
</div>
**Proof**. If the module category is simple, we have just seen that $A\cong M_n(D)$, and it is an exercise that this ring is simple. (Just do linear algebra over a division ring! More precisely, why not classify all ideals -- left, right, two-sided -- in these rings while you're at it?) 

So suppose that $A$ is a simple Artinian ring. First, given an $A$-module $M$, note that the annihilator of $M$ is a two-sided ideal of $A$ that does not contain $1$, hence is trivial. A minimal left ideal of $A$ (which exists because $A$ is Artinian!) is a simple module, so, in particular, $A$ has a faithful simple module that we will also call $M$. We will show that in fact $A$ can be written as $M^{\oplus m}$ for some $m$.

This is a clever trick: a map $$f:A\to M^{\oplus n}$$ with minimal kernel must be injective. Indeed, if not, there is some $a$ such that $f(a)=0$. But $M$ is faithful, so there is an $m$ such that $am\neq 0$. We can thus create a new map $$f':A\to M^{\oplus n}\oplus M$$ by sending $a$ to $(f(a), am)$. This will have a smaller kernel!

Now that we have an injection $A\inj M^{\oplus n}$ into a direct sum of simple modules, it is an entertaining exercise to show that $A$ itself must be isomorphic to $M^{\oplus m}$ for some $m$. Using the argument from above, this means that $A\cong M_n(D)$, as desired. QED

### Central simple algebras

Fix a field $k$.

<div class="definition">
A $k$-algebra $A$ is called a *central simple algebra* if $A$ is finite-dimensional over $k$, has center $k\cdot 1$, and is simple.
</div>

By the above, any central simple algebra $A$ is isomorphic to one of the form $M_n(D)$ for a central division algebra over $k$. 

Putting everything together, the objects making up the Brauer group -- the central division algebras $D$ -- have the same module categories as the central simple algebras.

**Why do we care??**

Being a central division algebra is not compatible with base change (for example, $\mathbf{H}\tensor\mathbf{C}$ is isomorphic to $M_2(\mathbf{C})$), but being a central simple algebra is. 

<div class="proposition">
If $A$ be a central simple algebra over $k$ and $L$ is a field extension of $k$, then $A\tensor_k L$ is a central simple algebra over $L$.
</div> 

**Proof**. Centrality: the condition that $A$ is central can be written like this. There is a natural map $\alpha:A\to \Hom(A, A)$ that sends $a$ to the map sending $b$ to $ab-ba$. The center is precisely the kernel of this map. By flatness of everything over a field, if $k\to A$ identifies $k$ with $\ker(\alpha)$, the same is true of $L\to A\tensor_k L$, i.e. $A$ is central if and only if $A \tensor_k L$ is central.

Simplicity: the key here is the following amusing claim.

**Claim**. If $A$ is a central simple algebra over $k$ and $L$ a field extension of $k$, any non-zero two-sided ideal $J$ of $A\tensor_k L$ has non-zero intersection with $L$.

**Proof**. (Farb and Dennis, Lemma 3.7) Choose $x$ in $J$ that has an expression $x=\sum a_i\tensor\lambda_i$ with minimal length. This implies that the $\{a_i\}$ and $\{\lambda_i\}$ are linearly independent over $k$. Since $a_1\neq 0$ and $A$ is simple, we have that $Aa_1A=A$, so there are $x_j, y_j$ such that $\sum x_j a_1 y_j=1$. This means that
$$x':=\sum_j x_j\tensor 1\left(\sum_i a_i\tensor\lambda_i\right)y_j\tensor 1=\sum_i a_i'\tensor\lambda_i$$
is also in $J$, and $a_1'=1$ (so, in particular, $x'\neq 0$). For any $a\in A$, we have $$(a\tensor 1)x'-x'(a\tensor 1)=\sum_{i\geq 2}(aa'_i-a'_ia)\tensor\lambda_i$$ (as $a'_1=1$, so it is central). But $x$ had minimal length, when we conclude that $aa'_i=a'_ia$ for all $a$. Since $A$ is central, we have that each $a_i'$ is in $k$, whence $\sum a'_i\lambda_i=0$. But the $\lambda_i$ are assumed to be linearly independent! QED the claim.

Conclusion: any non-zero two-sided ideal $J$ contains $(J\cap L)\cdot A\tensor L$, which is $A\tensor_k L$. But then any non-zero two-sided ideal is the whole ring, as desired. QED

Note that in the claim above is not enough to assume that $A$ is only a simple algebra over $k$: if $k = \mathbf{R}$ and $A = L = \mathbf{C}$, then $A\tensor_k L = \mathbf{C}\tensor_\mathbf{R} \mathbf{C}$, which is just $\mathbf{C} \times \mathbf{C}$ which is not a simple $\mathbf{C}$ algebra.  

<div class="corollary">
If $A_1$ and $A_2$ are central simple algebras over $k$, then $A_1 \tensor_k A_2$ is also a central simple algebra.
</div>

<div class="corollary"> 
If $D_1$ and $D_2$ are central division algebras over $k$, then $D_1\tensor_k D_2$ is a central simple algebra, hence isomorphic to $M_n(D_3)$ for some central division algebra $D_3$.
</div>

<div class="corollary">
Any central simple algebra $A$ over $k$ has the property that $A\tensor\overline k\cong M_n(\overline k)$ for some $n$. In fact, this is true over the *separable closure* of $k$ (see below).  
</div>

### Digression: $C_1$ fields 

<div class="definition">
A field L is $C_1$ if any homogeneous polynomial in $n$ variables of degree $d < n$ has a nontrivial root. 
</div>

<div class="theorem">(Tsen's Theorem)
A finite extension of $\overline k (t)$ is $C_1$. 
</div>
**Proof**. Let p(x_1,...,x_n) be a homogeneous polynomial of degree $d < n$ in $\overline k (t)$.  We want to find $a_1(t),...,a_n(t)$ in $\overline k (t)$, not all 0, such that $p(a_1(t),...,a_n(t)) = 0$.  
Write $$a_i(t) = \sum_{j=0}^N b_{ij}t^j$$ and write $$p(t) = \sum_{l=0}^m f_l(t) q_l(x_1,...,x_n)$$ where $f_l(t) \in \overline k$, $q_l(x_1,...,x_n)$ is a degree $d$ monomial, and $m$ is the number of such monomials.  Then, 
$$p(a_1(t),...,a_n(t) = \sum_{l=0}^m f_l(t) q_l(a_1(t),...,a_n(t)) = \sum_{r=0}^{Nd+M}g_r(\underline{b}_{ij})t^r$$
where M is the max degree of the $f_l(t)$'s, for some polynomials $g_r$.  
But, thinking of the $b_{ij}$'s as $(N+1)n$ variables, $Z(g_0(\underline{b}_{ij}),...,g_{Nd+M}(\underline{b}_{ij}))$ is a nonempty affine variety over $\overline k$ defined by $Nd+M+1$ equations in $\mathbf{A}^{(N+1)n}$ (nonempty because $b_{ij} = 0$ for all $i,j$ is a solution), hence must have dimension $\ge (N+1)n-(Nd+M+1) = N(n-d)+n-M-1$.
Because $n-d > 0$, choosing $N$ sufficiently large guarantees a nontrivial solution.  Therefore $p(x_1,...,x_n)$ has a nontrivial root. QED.


### Returning to Central Simple Algebras

<div class="proposition">
Any central simple algebra $A$ over $k$ has the property that $A\tensor k^s\cong M_n(k^s)$ for some $n$, i.e. $A$ splits over a separable closure of $k$.  
</div>
**Proof**. Let \$I = Isom(A,M_n): CAlg_k \to Set$ be the functor taking a commutative $k$-algebra $R$ to the $R$-algebra isomorphism $A\tensor_k R \to $M_n(R)$.  This is a scheme because we can define $A$ and $M_n$ via generators and relations and then parametrize isomorphisms between them (linear maps with polynomial conditions).  This works in part because  $\phi: A\tensor R \to M_n(R)$ is an isomorphism if and only if, for all $\overline k$, $R\to k$, the map $\phi\tensor\overline k : A\tensor \overline k \to M_n(\overline k)$ is an isomorphism. 
$I$ is nonempty because $A$ splits over $\overline k$ ($A\tensor_k \overline k \cong M_n(\overline k)$). 
In fact, $I$ is a torsor under $Isom(M_n, M_n)$ in the fppf topology because it splits over $\overline k$ and any two elements of $I$ differ by an automorphism of $M_n$.  Using the Skolem-Noether Theorem (below) and descent in the fppf topology, we can then conclude $I$ is smooth, hence has a point over a separable extension. QED

<div class="theorem">(Skolem-Noether) 
The canonical sequence of Zariski sheaves $$ 1 \to \mathbf{G}_m \to GL_n \to Aut(M_n) \to 1 $$ is exact (with the last map conjugation by elements of $GL_n$).  
</div>
**Proof**.  First note that if $\alpha \in GL_n$ acts trivially, $\alpha t = t \alpha$ for all $t$, so $\alpha \in Z(M_n) \cap M_n^x $, hence $\alpha \in \mathbf{G}_m$.  
To see exactness on the right, we use the following lemma.  QED. 

**Lemma**. If $R$ is a local ring, then any automorphism $M_n(R) \to M_n(R)$ is conjugation by an invertible element $\alpha \in GL_n(R)$.  

**Proof**. First, consider consider the classical case $R = k$, a field.  $M_n(k)$ has a unique simple module $V$.  If $\sigma \in Aut(M_n(k))$, consider the two actions of $M_n(k)$ on $V$ given by $(\alpha, v) \mapsto \alpha v$ and $(\alpha, v) \mapsto \sigma(\alpha) v$.  
Because $V$ is simple, there is an $M_n(k)$ isomorphism of these actions, i.e. $\phi: V \to V$ such that $\phi(\alpha v) = \sigma(\alpha)\phi(v)$, but $\phi \in End(V) \cong M_n(k)$, hence $\sigma$ is conjugation by $\phi$.  
For the general case, let $\sigma \in Aut(M_n(R))$.  There exists a unique $M_n(R)$ module $V$ that is free over $R$ of rank $n$.  Such a module exists (think columns) and is free because $M_n(R) \cong V^n$.  It is unique because if $V'$ is another such module, by tensoring with the residue field $k$ of $R$, we get an isomorphism $V\tensor k \to \V'\tensor k$.  Because $V$ is projective, this lifts to a map $V \to V'$, which is surjective by Nakayama's lemma.  But, $V$ and $V'$ are free of the same rank, hence it must be an isomorphism.  
Then, the argument above implies $\sigma$ is conjugation.  QED. 

### A digression on rational points

Coming soon
