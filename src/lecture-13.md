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
**Proof**. If the module category is simple, we have just seen that $A\cong\M_n(D)$, and it is an exercise that this ring is simple. (Just do linear algebra over a division ring! More precisely, why not classify all ideals -- left, right, two-sided -- in these rings while you're at it?) 

So suppose that $A$ is a simple Artinian ring. First, given an $A$-module $M$, note that the annihilator of any element is a two-sided ideal of $A$ that does not contain $1$, hence is trivial. A minimal left ideal of $A$ (which exists because $A$ is Artinian!) is a simple module, so, in particular, $A$ has a faithful simple module that we will also call $M$. We will show that in fact $A$ can be written as $M^{\oplus m}$ for some $m$.

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

Because of the following awesome result.

<div class="proposition">
If $A$ be a central simple algebra over $k$ and $L$ is a field extension of $k$, then $A\tensor_k L$ is a central simple algebra over $L$.
</div>
**Proof**. Centrality: the condition that $A$ is central can be written like this. There is a natural map $\alpha:A\to \Hom(A, A)$ that sends $a$ to the map sending $b$ to $ab-ba$. The center is precisely the kernel of this map. By flatness of everything over a field, if $k\to A$ identifies $k$ with $\ker(\alpha)$, the same is true of $L\to A\tensor_k L$.

Simplicity: the key here is the following amusing claim.

**Claim**. Any non-zero two-sided ideal $J$ of $A\tensor_k L$ has non-zero intersection with $L$.

**Proof**. (Farb and Dennis, Lemma 3.7) Choose $x$ in $J$ that has an expression $x=\sum a_i\tensor\lambda_i$ with minimal length. This implies that the $\{a_i\}$ and $\{\lambda_i\}$ are linearly independent over $k$. Since $a_1\neq 0$ and $A$ is simple, we have that $Aa_1A=A$, so there are $x_j, y_j$ such that $\sum x_j a_1 y_j=1$. This means that
$$x':=\sum_j x_j\tensor 1\left(\sum_i a_i\tensor\lambda_i\right)y_j\tensor 1=\sum_i a_i'\tensor\lambda_i$$
is also in $J$, and $a_1'=1$ (so, in particular, $x'\neq 0$). For any $a\in A$, we have $$(a\tensor 1)x'-x'(a\tensor 1)=\sum_{i\geq 2}(aa'_i-a'_ia)\tensor\lambda_i$$ (as $a'_1=1$, so it is central). But $x$ had minimal length, when we conclude that $aa'_i=a'_ia$ for all $a$. Since $A$ is central, we have that each $a_i'$ is in $k$, whence $\sum a'_i\lambda_i=0$. But the $\lambda_i$ are assumed to be linearly independent! QED the claim.

Conclusion: any non-zero two-sided ideal $J$ contains $(J\cap L)\cdot A\tensor L$, which is $A\tensor_k L$. But then any non-zero two-sided ideal is the whole ring, as desired. QED

<div class="corollary">
Any central simple algebra $A$ over $k$ has the property that $A\tensor\overline k\cong M_n(\overline k)$ for some $n$. In fact, this is true over the *separable closure* of $k$.
</div>
**Proof**. The last statement: the scheme of isomorphisms between $A$ and $M_n$ is smooth and non-empty, hence has a point over a separable extension. QED

### A digression on rational points

Coming soon