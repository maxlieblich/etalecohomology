# Central simple algebras

In this lecture, we will see a few beautiful things about the building blocks of the Brauer group, the algebras themselves. A bunch of the proofs here are inspired by (or cribbed from) the beautiful book by Farb and Dennis on non-commutative algebra.

### Divison algebras, central simple algebras, and Donald Rumsfeld

In studying division algebras, we are naturally led to apply one of Rumsfeld's famous rules: "If you can't solve a problem, make it bigger." (He was *very* good at this.)

One of the deepest insights of 20th Century mathematics is the observation that rather than investigate the inner workings of a single object, it often pays to investigate associated categories. We usually think this means that we should look at the category of objects of a similar flavor, but "classical" algebra gives us a prime example this idea, due to Morita theory. I will not go into detail about Morita theory, except for its incarnation in our specific case.



### Simple categories and matrix rings

Call an abelian category $C$ *simple* if is semisimple and there is a simple object $c$ in $C$ such that every object of $C$ can be written as a direct sum of copies of $c$ (up to isomorphism).

<div class="theorem"> (Morita-ish)
Fix an Artinian ring $A$. The category of $A$-modules is simple if and only if $A\cong M_n(D)$, the ring of matrices over a division ring $D$.
</div>
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

So suppose that $A$ is a simple Artinian ring. First, given an $A$-module $M$, note that the annihilator of any element is a two-sided ideal of $A$ that does not contain $1$, hence is trivial. A minimal left ideal of $A$ (which exists because $A$ is Artinian!) is a simple module, so, in particular, $A$ has a faithful simple module that we will also call $M$. We will show that in fact $A$ can be written as $M^{\oplus m}$ for some $m$.

This is a clever trick: a map $$f:A\to M^{\oplus n}$$ with minimal kernel must be injective. Indeed, if not, there is some $a$ such that $f(a)=0$. But $M$ is faithful, so there is an $m$ such that $am\neq 0$. We can thus create a new map $$f':A\to M^{\oplus n}\oplus M$$ by sending $a$ to $(f(a), am)$. This will have a smaller kernel!

Now that we have an injection $A\inj M^{\oplus n}$ into a direct sum of simple modules. More generally, we are going to show that any submodule $N\subseteq M^{\oplus n}$ is free.

We will make use of the fact that if $P = \sum_{I} M_i$ is a sum, where $M_i \cong M$, then the sum is direct, i.e. $P = \oplus_{J} M_i$, where $J\subset I$. (one can prove this last fact by a maximality argument)

Let $N \subseteq M^{\oplus n}$ be a sumbmodule. The quotient $M^{\oplus n}/N$ is clearly a sum of copies of $M$, hence it's free by the quoted fact.

Now we shall prove that $N$ is a direct summand of $M^{\oplus n}$, hence a quotient, thus showing that it's free. This is swiftly achieved by considering a maximal element $J$ in the set
$$
\{ I : \bigoplus_I M \cap N = 0  \}
$$
since in this case one can easily see that $\bigoplus_J M \cap N = M^{\oplus n}$.

Now we know that $A \cong M^{\oplus m}$ for some $m$. Using the argument from above, this means that $A\cong M_n(D)$, as desired. QED

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

### Some examples of central simple algebras

A *quaternion algebra* $A$ over a field $K$ of characteristic $\neq 2$ is a $4$-dimensional algebra generated (as a $K$-algebra) by two elements $i,j$ with the relations
$$
i^2 = a, j^2, ij + ji = 0
$$
where $a,b \in K^{\times}$. If we set $k = ij$, then a basis for $A$ is given by $1, i, j, k$. The algebra $A$ is often denoted by $(a, b)$.

Given a generic element $x = a + bi + cj + dk$, then we define its *conjugate* to be $\overline{x} = a - bi - cj - dk$, and thus we can define a morphism of multiplicative monoids
$$N: (a,b)\setminus 0 \to K^{\times}, x \mapsto n\overline{x}$$
called the *norm* map.

<div class="lemma">
Let $A = (a,b)$ be a quaternion algebra. Then
(1) $A$ is central over $K$
(2) Either $A$ is a division algebra or it splits, i.e. it's isomorphic to $M_2(K)$
(3) If $A$ is a division algebra, then it splits over $K(\sqrt{a})$ and over $K(\sqrt{b})$.
</div>

Quaternion algebras play an important role in the description of the Brauer group of $K$.

<div class="theorem"> (Merkuriev–Suslin)
Assume $\text{char}K \neq 2$. Then $Br(K)[2]$ is generated by quaternion algebras.
</div>

<div class="example">
Let $F = K(x,y,z,w)$. Then one can prove that $(x,y)\otimes (z,w)$ is a central division algebra.

*Challenge questions*:
(1) Are there elements $a,b,c,d \in K(x,y,z)^{\times} such that (a,b)\otimes (c,d)$ is a CDA? What if $K$ is algebraically closed?
(2) Is every $4$-dimensional $2$-torsion CDA over $K$ a quaternion algebra?

A possible way to answer question (2) is to try to find the generatos $i,j$. Let $D$ be such a CDA, and let $i \in D\setminus K$. Then the extension $K(i) : K$ has degree $2$. WLOG we can assume $i^2 = \alpha \in K$. Try then to prove that the $K$-automorphism $K(i)\to K(i), i\mapsto -i$ is induced by conjugation by an element $j\in D$ whose square $\beta$ lies in $K$, and check that $D = (\alpha, \beta)$.
</div>

### A digression on rational points

Coming soon