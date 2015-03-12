# Moduli space of length $1$ $\mathfrak{X}$-twisted sheaves

### The classical setting

First we consider the classical setting. Let $X$ be a proper scheme over a field $k$, and consider the moduli space of length one quasi-coherent sheaves with finite presentation (qcfp sheaves) on $X$. 
We can define a moduli functor $\mathcal{M}$ can be defined as follows, for all $k$-schemes $T$, $\mathcal{M} ( T )$ is the set of all qcfp sheaves $F$ on $X_{T} =X \times_{k} T$ such that

(M1) $F$ is $T$-flat (more generally $F$ is $T$-flat with $T$-proper support)
  
(M2) if $\bar{t} \to T$ is a geometric point then $F_{\bar{t}}$ has length $1$. 

This defines a pseudofunctor / CFG.

Question: Is $\mathcal{M}$ a stack / sheaf / scheme?

The CFG $\mathcal{M}$ is a sub-CFG of Qcoh$( X/k )$, where the latter is a stack. To show that $\mathcal{M}$ is a substack, we have to show that conditions (M1) and (M2) above are preserved by descent. 
Condition (M1) is preserved by descent since we can checkvflatness fppf locally. Condition (M2) is preserved since geometric point conditions automatically glue if they are invariant under algebraically closed field extensions.

Note: The notion of length is poorly behaved over non-geometric points.

We can rephrase condition (M2) equivalently as follows:
(M2') Let $q:X_{T} \to T$ be the projection, then $q_{\ast} F$ is locally free of rank $1$.

Note that Condition (M2') is compatible with base change.

<div class="lemma">
(M2) and (M2') are equivalent conditions
<\div>

**Proof** Consider the following Cartesian square
$$ \begin{array}{ccc} X_{\bar{t}} & \overset{f}{\longrightarrow} & X_{T}\\
       _{\pi} \downarrow &  & \downarrow_{q}\\
       \bar{t} & \overset{g}{\longrightarrow} & T \end{array} $$
where $\bar{t}$ is a geometric point of $T$. Then $F_{\bar{t}} =f^{\ast} F$. Suppose that $F_{\bar{t}}$ has length $1$, then $k ( \bar{t} ) \simeq \pi_{\ast} f^{\ast} F \simeq g^{\ast} q_{\ast} F$. Hence the geometric fibres of $q_{\ast} F$ are one dimensional. (This should imply $q_{\ast} F$ is locally free, at least if $T$ is reduced and $k= \bar{k}$ this is clear).
Conversely, suppose $q_{\ast} F$ is locally free of rank $1$, then $\pi_{\ast} F_{\bar{t}} \simeq g^{\ast} q_{\ast} F \simeq k ( \bar{t} )$, so $F_{\bar{t}}$ has length $1$. QED. 

### Example families 

Consider $q:X \times_{k} X \to X$ where $q$ is the second projection. Let $\mathcal{O}_{\Delta}$ be the structure sheaf of the closed subscheme $\Delta \subseteq X \times_{k} X$. 
Then $q_{\ast}\mathcal{O}_{\Delta}$ clearly satisfies (M1) and (M2) so $\mathcal{O}_{\Delta}$ is a family in $\mathcal{M} ( X )$.

More generally, assume that $X$ is separated. Given a section $\alpha :T \to X \times T$ of $q:X \times T \to T$, the $\mathcal{O}_{X_{T}}$-module $\alpha_{\ast} \mathcal{O}_{T}$ gives a family in $\mathcal{M} ( T )$.

### Conclusions about $\mathcal{M}$ 

<div class="theorem">
The pseudofunctor $\mathcal{M}$ has the following alternative description.
For every $k$-scheme $T$:
$$ \mathcal{M} ( T )  =  \{ ( \alpha , \mathcal{L} ) \mid \alpha :T \to X_{T} , q \circ \alpha =1_{T} , \mathcal{L} \in Pic ( \alpha ( T ) ) \} . $$
<\div>

<div class="theorem">
There is an isomorphism of $\mathbb{G}_{m}$-gerbes
$$ \mathcal{M} \simeq B\mathbb{G}_{m} \times X. $$
<\div>

**Point of Proof** This alternative description gives a map $F \to Supp (F)$ and $M \to X$ that, together, imply the isomorphism above. QED.

Note: The stack $\mathcal{M}$ is a ``floppification'' of ${Hilb}^{1} ( X )$; alternatively one can view the punctual Hilbert scheme ${Hilb}^{1} ( X )$ as a rigidification of $\mathcal{M}$; since ${Hilb}^{1} ( X )$ classifies sheaves of length $1$ $\mathcal{T}$ with the extra structure of a morphism $\mathcal{O} \to \mathcal{T}$.

### Extending this to $\mathfrak{X}$-twisted sheaves

Question: Let $\mathfrak{X} \to X$ be a $\mathbb{G}_{m}$-gerbe over $X$.  What is the moduli space of length $1$ $\mathfrak{X}$-twisted sheaves? 
More generally, if $\mathfrak{Y}$ is an algebraic stack, is the moduli space of length $1$ sheaves on $\mathfrak{Y}$ isomorphic to $\mathfrak{Y}$?
  
I think the answers are $\mathfrak{X}$ and $\mathfrak{Y}$ respectively. 

We conjectured in class that the moduli space of length $1$ $\mathfrak{X}$-twisted sheaves must be either $\mathfrak{X}$ or $B\mathbb{G}_{m} \times X$.  One way to distinguish the two is to determine if there is a global section over $id: X \to X$, which corresponds to the existence of an invertible $\mathfrak{X}$-twisted sheaf.  
But, such a sheaf exists if and only if $[ \mathfrak{X} ] = 0$.  So, if $[ \mathfrak{X} ] \ne 0$, this moduli space certainly can't be $B\mathbb{G}_{m} \times X$, leading us to believe it is just $\mathfrak{X}$.  

### Another proof that $\mathrm{Br} ( X )$ is torsion

Consider the cocycle formulation of twisted sheaves. Let $U \to X$ be a Cech hypercover, and $a \in \mathbb{G}_{m} ( U \times_{X} U \times_{X} U )$ be a cocycle with class $[ \mathfrak{X} ]$. 
A twisted sheaf is given by a sheaf $F$ on $U$ together with an isomorphism $\varphi : \mathrm{pr}_{1}^{\ast} F \to \mathrm{pr}_{2}^{\ast} F$ satisfying the $a$-twisted cocycle equation. Let $\delta$ be coboundary map, then $\delta \varphi =a^{-1}$.

An Azumaya algebra $A$ with class $[ \mathfrak{X} ]$ is given as the endomorphisms of locally free $\mathfrak{X}$-twisted sheaf $V$, such that $A= \pi_{\ast} \mathcal{E} n d ( V )$ (where $\pi : \mathfrak{X} \to X$).

Restrict everything to $U$: and call $V \mid_{U} =V_{0}$, $\varphi_{0} : \mathrm{pr}_{1}^{\ast} V_{0} \to \mathrm{pr}_{2}^{\ast} V_{0}$.  $\delta \varphi =a^{-1}$ so $\mathcal{E} n d ( V_{0} )$ descends.

<div class="proposition"> Let $r= \mathrm{rank}  V$, then $r [ \mathfrak{X} ] =0$. In particular, $\mathrm{Br} ( X )$ is torsion.
</div>

**Proof** Let $L_{0} = \det ( V_{0} )$. So $\wedge^{r} \varphi : \mathrm{pr}_{1}^{\ast} L_{0} \to \mathrm{pr}_{2}^{\ast} L_{0}$. Then $\delta \wedge^{r} \varphi = \wedge^{r} \delta \varphi =a^{-r}$. 
Hence the data $( L_{0} , \wedge^{r} \varphi )$ give an invertible twisted sheaf for the cocycle $a^{r}$. Hence $r [ \mathfrak{X} ]$ is trivial.  QED. 