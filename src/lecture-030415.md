** Bens Question ** 
Let $G$ be a complex group scheme.  What quasi-coherent sheaves on $BG$ coorrespond to characters?
Answer:
Quasi-coherent sheaves on $BG$ correspond precisely to representations of $G$.  In this correspondence, the group characters are exactly the invertible sheaves.  In other words $\textnormal{Pic}(G) = \widehat{G}$.

** Bens Other Question **
What does semisimplicity correspond to?
Answer:
Let $G$ be a group scheme.  Then $G$ is semisimple if and only if for all quasicooherent sheaves $F$ on $BG$, and for all $i>0$, $H^i(BG,F) = 0$.

** Chriss Question **
What is $H^0(BG,F)$?
Answer:
Last time we showed that $\pi_*F = F^G$ for $\pi: BG\rightarrow X$.  Therefore $H^0(BG,F) = H^0(X,\pi_*F) = F(X)^G$.

** Missions Last Time **
What are the sheaves on $\mathcal{X}_A$ with trivial stabilizer action?
We argued that $\pi: BG\rightarrow X$ satisfies $pi^*\pi_* = \text{id}_{BG}$ and therefore that $\pi^*$ defines an equivalence of categories between the category of quasicoherent sheaves on $S$ and the category of quasicoherent sheaves on $BG$ with trivial action.
What about for $\pi: \mathcal{X}_A\rightarrow X$?

** Claim **
$\pi^*$ also gives an equivalence of categories $\text{Qcoh}(X)\rightarrow \text{Qcoh}(\mathcal{X}_A)^0$

We saw that the construction of $\mathcal{X}_A$ also comes equipped with a natural locally free sheaf $\mathcal{V}$ on $\mathcal X_A$ of rank equal to the rank of $A$.  We briefly recall its definition:
Morphisms $T\rightarrow \mathcal{X}_A$, correspond to trivializations $(V,\varphi)$ with $V$ a locally free sheaf on $T$ and $\varphi$ an isomorphism $\mathcal{End}(V)\rightarrow A_T$.  Using this correspondence, $\mathcal V$ is defined by
$$\mathcal{V}: (V,\varphi) \mapsto \Gamma(T,V).$$

Now set $\mathcal A = \mathcal{End}(\mathcal{V})$ on $\mathcal{X}_A$.
Then $\mathcal{A}$ is a quasi-coherent sheaf of $\mathcal{O}_{\mathcal{X}_A}$-algebras.
This has scalar $\mathbb{G}_m$-action!  Why?
The current note-takers understanding is that the reason is the following:
The action of $\mathbb{G}_m$ on $\mathcal{V}$ is by scalar multiplication, so as a representation, $\mathcal{V}$ decomposes into a direct sum $\mathcal{V}\cong\chi^{\oplus n}$ (with $n$ the rank of $A$).  Therefore since $\chi^{\oplus n}\otimes \chi^* = k^n$, we have that
$$\mathcal{End}(V)\cong \mathcal{End}(k^n),$$
the latter set having trivial action.

The projection then defines an iso. $\mathcal{End}(\mathcal{V})\cong \pi^*A$, and since $\pi^*$ is an equivalence, we see that $\pi_*\mathcal{End}(\mathcal{V})\cong A$.

In fact, the situation is even better than this.  Take any locally free sheaf $\mathcal{W}$ of rank $n$ on $\mathcal{X}_A$ for which $\mathbb{G}_m$ acts on by scalar multiplication.  Then
$$\mathcal{End}(\mathcal V)\otimes\\mathcal{End}(\mathcal{M})\cong \mathcal{End}(\mathcal W)\otimes\mathcal{End}(\mathcal{N})$$
for $\mathcal M = \mathcal{Hom}(\mathcal{W},\mathcal{V})$ and $\mathcal N = \mathcal{Hom}(\mathcal{V},\mathcal{W})$.  The fact that $\mathcal M$ has trivial action implies that $\pi_*\mathcal{End}(\mathcal{M}) = \mathcal{End}(\pi_*\mathcal{M})$ and similarly for $\mathcal N$.  Hence we see that:
$$\pi_*\mathcal{End}(\mathcal{V})\otimes\mathcal{End}(\pi_*\mathcal{M})\cong \pi_*\mathcal{End}(\mathcal{W})\otimes\mathcal{End}(\pi_*\mathcal{N})$$
Thus $\pi_*\mathcal{End}(\mathcal{V})$ and $\pi_*\mathcal{End}(\mathcal{W})$ are (Morita) equivalent (ie. belong to the same class in the Brauer group of $X$).

** Basic Theorem **
$\pi_*$ defines an equivalence between things of the form
$$\{\mathcal{End}(\mathcal{W}): \mathcal{W}\ \text{locally free, finite rank on $\mathcal{X}_A$ with scalar $\mathbb{G}_m$-action}\}$$
and the set
$$\{\text{Azumaya algebras $\mathcal B$ on $X$ isomorphic to $A$}\}$$

** Claim **
If $A$ and $B$ are equivalent Azumaya algebras, then $\mathcal X_A$ and $\mathcal X_B$ are isomorphic as $\mathbb{G}_m$-gerbs over $X$.
Justification:
Assume $A$ and $B$ are equivalent.  Then there exists locally free $\mathcal O_X$-modules $V$ and $W$ on $X$ such that $A\otimes\mathcal{End}(V) \cong B\otimes \mathcal{End}(W)$.  Without loss of generality, may take $W = \mathcal O_X$.  In this case define $\mathcal{X}_A\rightarrow\mathcal{X}_B$ by
$$(V_0,\varphi_0)\mapsto (V_0\otimes V,\varphi_0\otimes\mathcal{End}(V)).$$
Max remarks: this is like a dismembered head on a turtle -- it is just going.

In this way, the association $A\mapsto \mathcal{X}_A$ defines an injection
$$\text{Br}(X)\hookrightarrow \{\text{iso classes of $\mathbb{G}_m$-gerbes on $X$}\} = H^2(X,\bbg_m).$$
(The last equality comes from the fact that we can make gerbes from derived functor cohomology)

** A down-to-earth version of this map **
Our old universal trivialization of an Azumaya algebra $A$ on $X$ is as the $\mathbb{PGL}_n$-torsor $V\rightarrow X$ represented by the isom functor
$$T\mapsto \text{Isom}_{$T$-\text{alg}}(\sheaf O_T^n,A_T).$$
In other words, the old universal trivialization gives us an element of $H^1(X,\mathbb{PGL}_n)$.
The new universal trivialization gives us an element of $H^2(X,\mathbb{G}_m)$.
How do we relate these?  By Skolem-Noether, we have a short exact sequence of group schemes
$$1\rightarrow\mathbb{G}_m\rightarrow\mathbb{GL}_n\rightarrow\mathbb{PGL}_n\rightarrow 1$$
Then France (Giraurd) tells us we get a long exact sequence of pointed sets
$$H^1(X,\mathbb{G}_m)\rightarrow H^1(X,\mathbb{GL}_n)\rightarrow H^1(X,\mathbb{PGL}_n)\xrightarrow{\delta} H^2(X,\mathbb{G}_m).$$
Here this last map $\delta$ sends a $\mathbb{PGL}_n$-torsor to the stack of reductions of the structure group of $T$ to $\mathbb{GL}_n$.




