# Introduction: why do this?

Let's start with a simple example.

## An example

Let's start with an example. Consider the polynomial
$$F(x, t) = x^2 + b(t)x + c(t)\in k[x,t]$$
for some field $k$. This defines a curve $C\subset\A^2$, and projecting to the $t$-coordinate gives a morphism $$f:C\to\A^1.$$

<div class="question">
Where does $f$ ramify? I.e., where does $f$ have a double root?
</div>

If $\ch(k)\neq 2$, then we can just use the quadratic formula. The roots of $F(x, \alpha)$ are given by 
$$\frac{-b(t)\pm\sqrt{b(t)^2-4c(t)}}{2},$$
so there is a double root exactly when $b(t)^2 = 4c(t)$. When $k$ is algebraically closed and $b^2$ and $c$ are linearly independent (e.g., have different degrees!), this is guaranteed.

Since every degree $2$ extension of $k(t)$ is quadratic, this has a very concrete consequence.

<div class="theorem"> 
Any finite map $C\to\A^1$ of degree $2$ must ramify if $\operatorname{char}(k)\neq 2$.
</div>

But what happens when $\operatorname{char}(k)=2$? The fun starts! Consider the special case $b(t)=-1$. If $a$ is a root of $F(x,\alpha)$, then so is $a+1$. In other words, **when $\operatorname{char}(k)=2$, the polynomial $F(x,t) = x^2 - x + c(t)$ never has a double root**.

What does this mean? What is a double root?

### Measuring double roots

A polynomial $f(x)$ has a multiple root precisely when $f(x)$ and its derivative $f'(x)$ have an irreducible factor in common. How can we interpret this geometrically?

#### The tangent map

If you think of a complex polyonomial as a function $f:\C\to\C$, the derivative $f'$ at a point computes the tangent map. If the derivative is relatively prime to $f$, then *for any element $c\in\mathbf{C}$ such that $f(c)=0$, the tangent map $$T_c\C\to T_{f(c)}\C$$
is an isomorphism*. More generally, a family of polynomials $F(x,t)$ as above gives a map of Riemann surfaces $\phi:X\to\C$ (really, $X$ might just be a complex analytic curve), and the $F(x, \alpha)$ is unramified at a point if and only if the tangent map at each preimage of $\alpha$ is bijective.

<div class="exercise">
Is it possible for a polynomial $f:\C\to\C$ to give an isomorphism of tangent spaces at *every* point?
</div>

#### Local isomorphism 

As you learned in complex analysis, the tangent map of $\phi$ is an isomorphism if and only if the map $\phi$ is itself a *local isomorphism*. (A quirky proof: $\phi$ induces an isomorphism of complete local rings, hence of rings of germs of holomorphic functions, which lets us invert $\phi$ locally. Or use calculus.) What about algebraically? The function $F$ defines a map of rings $k[t]\to k[x, t]/(F)$. We claim that if $F(x, 0)$ is relatively prime to $F_x(x, 0)$ then this map gives an isomorphism of *complete local rings*.

<div class="lemma">
  Let $g:A\to B$ be a finite map of regular complete local Noetherian rings that induces an isomorphism of residue fields, and suppose that the induced map $$m_A/m_A^2\to m_B/m_B^2$$ is an isomorphism. Then $g$ is an isomorphism.
</div>

**Proof**. Since $A$ and $B$ are regular, we know that $m^n/m^{n+1}$ is $\operatorname{Sym}^n{m/m^2}$ (where $m$ denotes either maximal ideal). We conclude that the maps on the graded pieces $m_A^n/m_A^{n+1}\to m_B^n/m_B^{n+1}$ are isomorphisms for all $n$. Thus, the map $\operatorname{gr}(A)\to\operatorname{gr}(B)$ is an isomorphism. By Krull's theorem, $g$ must be injective. 

To see that $g$ is surjective: any element of $B$ agrees with the image of an element of $A$ modulo $m$. But any element of $m$ is in the image of $A$ modulo $m^2$. Etc. We use the fact that Cauchy sequences in $A$ converge, i.e., that $A$ is complete! QED

#### Uniformization 

If you think of $F$ as giving a ring map $$k[t]\to k[t, x]/(F)$$ as above, the condition that $F(x, 0)$ and $F_x(x, 0)$ are relative prime is the same as saying that $t$ generates a radical ideal $k[t, x]/(F)$. In other words, the uniformizer $t$ at $0$ maps to a uniformizer at each root of $F(x, 0)$. Now this looks like *number theory*.

### Local isomorphism in algebraic geometry

We will take the conditions above and use them to define a good notion of *local isomorphism* in algebraic geometry that mimics the one we see in complex geometry. Let's start with varieties over an algebraically closed field to keep the analogy close.

<div class="definition">
Let $k$ be an algebraically closed field. A morphism of $k$-varieties $f:X\to Y$ is *etale* if for every point $x\in X$ with image $y=f(x)\in Y$, the induced map of complete local rings 
$$\widehat{\ms{O}}_{Y,y}\to\widehat{\ms{O}}_{X,x}$$ 
is an isomorphism.
</div>

When $X$ is smooth at $x$ and $Y$ is smooth at $y$, this is equivalent to $f$ inducing an isomorphism of tangent spaces. (What about in the absence of smoothness conditions?)

We will spend some time (later in the course) really trying to understand and generalize this definition. For example, what about a separable field extension $K\subset L$? Should that count as a local isomorphism?

### Why "etale cohomology"?

Let's return to the example. Our first "result" was that if $\ch(k)\neq 2$, any finite two-to-one map $C\to\A^1$ cannot be an isomorphism everywhere. Doesn't this remind you of the fundamental group? It is a teeny tiny piece of the statement that $\mathbf{A}^1$ is simply connected!

But something went horribly wrong (or horribly right) in characteristic $2$. We found many examples that *were* everywhere unramified. For example, the curve $C$ given by $x^2 - x - t=0$ in $\mathbf{A}^2$ admits (by projection to the $t$ coordinate) a finite etale map $C\to\mathbf{A}^1$ of degree $2$. What's more, we can always permute the roots (preimages of a point) by adding $1$!

That is to say, there's a group action $$\Z/2\Z \times C\to C$$ that acts simply transitively on the fibers of $C\to\A^1$. Have you every seen this before? Do you remember what classifies these things?

#### Classical topology

A map like we just described corresponds to a class in $$\Hom(\pi_1(B), \Z/2\Z) = H^1(B, \Z/2\Z).$$ Some cohomology groups capture abelian pieces of the fundamental group.

We seem to have shown that $\pi_1(\A^1_{\overline{\F_2}})$ is non-zero. ?!??!?!??!?!!!!

#### Zariski topology

So it's natural to ask: how about attacking $\A^1$ in the Zariski topology? 

<div class="lemma">
  The Zariski topology on $\A^1_k$ is simply connected.
</div>

**Proof**. Every open set is dense. QED

More generally, suppose $X$ is an integral scheme. What is the cohomology of a constant sheaf on $X$ in the Zariski topology?

### Moving forward

The Zariski topology is not the right replacement for the classical topology.

#### How do we replace the Zariski topology?

We seek some kind of "topology" on $\A^1$ such that we can really say that the zero locus of $x^1-x-t$ does indeed correspond to a class in $H^1(\A^1, \Z/2\Z)$. It turns out that we need to use a *categorical substitute* for topology, known as a Grothendieck topology. We'll spend the first few sessions studying these in general.

#### How do we compute cohomology in these a Grothendieck topology?

Can we do a single example? It took Grothendieck and Artin a while to get this to work.

#### Do algebraic computations give the right answer?

For example, is the cohomology of a curve with finite coefficients correct? Shouldn't we be nervous having just seen what happened to $\mathbf{A}^1$?

#### Can we recover classical results in differential/complex geometry?

Is the cohomology of a smooth family a local system? What does this question even mean?

#### What happened to number theory?

We'll see that once we rephrase certain things about classical results correctly (e.g., local systems), we can suddenly understand what is going on with basic ideas in number theory. For example, the Galois action on the cohomology of a variety is another way of thinking about the higher direct image in the etale topology. Etale cohomology becomes Galois cohomology. The Leray spectral sequence becomes the Hochschild-Serre spectral sequence. Etc.

## Tasting the new in the old

Let's briefly review the categorical underpinnings of the theory of sheaves that you all know and love. Fix a topogical space $T$. The open subsets of $T$ form a category $\operatorname{Open}(T)$; the maps from $U$ to $V$ are the inclusions $U\to V$ over the natural maps $U\to T$ and $V\to T$.

Here's a silly category-theoretic way to express presheaves.

<div class="definition">
  A *presheaf* (of sets; really, with values in any reasonable category) on $T$ is a functor $$\operatorname{Open}(T)^\circ\to\operatorname{Set}.$$
</div>

A sheaf is defined using **open coverings**.

<div class="definition">
  A presheaf $F$ is a *sheaf* if for every open covering $\{U_i\subset U\}$ of an open subset $U\subset T$, the diagram of sets
$$F(U) \to \prod_i F(U_i) \rightrightarrows \prod_{i, j} F(U_i\cap U_j)\cdots$$ is *exact*, i.e., the first arrow is the equalizer of the second two (stacked) arrows.
</div>

There are two full subcategories of the category of functors, $PreSh(T)$, the presheaves, and $Sh(T)$, the sheaves. Any sheaf is a presheaf, and any presheaf can be sheafified. In category language: there is an adjoint pair of functors $-:Sh(T)\to PreSh(T)$ and $+:PreSh(T)\to Sh(T)$. (The first is usually not written because sheaves form a full subcategory of presheaves, so the first is just the canonical embedding.)

### Grothendieck's version

Grothendieck realized that the two conditions above -- that there is a category fo open sets, and a distinguished collection of sets of morphisms called "open coverings" -- is enough to capture most of the fundamentals of geometry (also known as "sheaves and their cohomology"). More precisely, we have the following.

<div class="definition">
  A *Grothendieck topology* is a category $C$ with a collection of coverings $\{U_i\to U\}{i\in I}$ for each $U\in C$ such that 

  (1) Any isomorphism is a covering.
  (2) If $\{U_i\to U\}$ is a covering, and for each $i$ we have a covering $\{V_{ij}\to U_i\}$, the total collection $\{V_{ij}\to U\}$ is a covering.
  (3) If $\{U_i\to U\}$ is a covering and $V\to U$ is arbitrary, then each $U_i\times_U V$ exists and $\{U_i\times V\to V\}$ is a covering.
</div>

We are going to spend the rest of the quarter examining the amazingly profound consequences of this simple definition.

<div class="exercise">
  Verify that a topological space really does give a Grothendieck topology.
</div>

<div class="exercise">
Let $C$ be the category of sets, and define coverings to be collections of maps $\{U_i\to U\}$ such that the union of the images of the $U_i$ is all of $U$. Show that for any sheaf $F$ on $C$, the object $F(e)$ represents $F$, where $e$ is a fixed chosen singleton set.
</div>

#### Reading
Section 1 of Artin's notes. 