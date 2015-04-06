Speaker : Dan 
Date : April 3, 2015
Typed up by : Ken / Bharath

Semistability
=============

Let $X$ be a noetherian scheme and $E \in \mathsf{\mathrm{Coh}} ( X )$.

The <span><span>**<span>dimension</span>**</span></span> of $E$ is
defined as $\dim  E= \dim   \mathrm{supp}
E$.

The sheaf $E$ is <span><span>**<span>pure</span>**</span></span> if for
all subsheaves $F \hookrightarrow E$ then $\dim  F= \dim  E$ or $F=0$.

Let $F \subset E$ be a subsheaf, the
<span><span>**<span>saturation</span>**</span></span> $F'$ of $F$ in $E$
is the minimal sheaf $F \subseteq F' \subseteq E$ such that $E/F'$ is
pure of dimenison $d$ or $0$.

Alternatively, the saturation of $F$ is the kernel of the composition
$$E \longrightarrow E/F \longrightarrow ( E/F ) /T_{d-1} ( E/F )$$ where
$T_{d-1}$ is the maximal subsheaf of dimension $\leqslant d-1$.

Now assume $X$ is projective over a field $k$, fix a very ample line
bundle $\mathcal{O} ( 1 ) \in \mathrm{Pic}  X$. Let
$E \in \mathsf{\mathrm{Coh}} ( E )$ with $\dim  E=d$. Recall that the
<span><span>**<span>Hilbert polynomial</span>**</span></span>,
$P_{E} ( m )$ of $E$ is given by

$$\begin{aligned}
  m & \mapsto & \chi ( E \otimes \mathcal{O} ( m ) )\end{aligned}$$

Fact: $P_{E} ( m ) = \sum_{i=1}^{\dim  E} \alpha_{i} ( E ) m^{i} /i!$
for some $\alpha_{i} ( E ) \in \mathbb{Q}$. Also $\alpha_{d} ( E ) >0$
if $E \neq 0$.

The <span><span>**<span>reduced Hilbert
polynomial</span>**</span></span> of $E$ is

$$\begin{aligned}
  p_{E} ( m ) & = & \frac{P_{E} ( m )}{\alpha_{d} ( E )}\end{aligned}$$

Fact: $\alpha_{d} ( \mathcal{O}_{X} )$ is the degree of the embedding $X \rightarrow {P}^{n}$.

If $f,g \in \mathbb{Q} [ x ]$ we say that $f<g$ if $f ( m ) <g ( m )$
for $m
\gg 0$. Similarly for $f \leqslant g$.

We say that $E \in \mathsf{\mathrm{Coh}} ( E )$ is
<span><span>**<span>semistable</span>**</span></span> (resp.
<span><span>**<span>stable</span>**</span></span>) if it is pure of
dimension, say $d$, and for all proper subsheaves
$F  \hookrightarrow E$ we have
$p_{F} \leqslant p_{E}$ (resp. $p_{F} <p_{E}$).

Let $E \in \mathsf{\mathrm{Coh}} ( X )$ and suppose $E$ has dimension
$d$. Then the following are equivalent

1.  $E$ is semistable (resp. stable)

2.  for all proper dimension $d$ quotients, $E \longrightarrow G$ of
    $E$, we have $p_{E} \leqslant p_{G}$ (resp. $p_{E} <p_{G}$).

Assume $E$ is semistable. We first show that (1) implies (2). Let
$F= \ker (
  E \longrightarrow G )$, then $\dim  F=d= \dim  G$. Since $\chi$ and
$\alpha_{d}$ are both additive, we have $P_{F} +P_{G} =P_{E}$ and
$\alpha_{d} ( F ) + \alpha_{d} ( G ) = \alpha_{d} ( E )$. Hence

$$\begin{aligned}
    \alpha_{d} ( F ) ( p_{F} -p_{E} ) & = & \alpha_{d} ( G ) ( p_{E} -p_{G} )
  \end{aligned}$$

so $p_{F} \leqslant p_{E}$ implies $p_{E} \leqslant p_{G}$. Conversely,
let $F  \hookrightarrow E$ and $F'$ be the
saturation of $F$ in $E$. Then the same reasoning as above implies
$p_{F'} \leqslant p_{E}$. Finally $p_{F}
  \leqslant p_{F'}$ since $P_{F} \leqslant P_{F'}$ (again by additivity
of $\chi$) and $\alpha_{d} ( F ) = \alpha_{d} ( F' )$. The latter
follows from

$$\begin{aligned}
    \alpha_{d} \left( \frac{E/F}{T_{d-1} ( E/F )} \right) & = & \alpha_{d} ( E
    ) - \alpha_{d} ( F ) - \alpha_{d} ( T_{d-1} ( E/F ) )\\
    & = & \alpha_{d} ( E ) - \alpha_{d} ( F )\\
    \alpha_{d} ( E/F' ) & = & \alpha_{d} ( E ) - \alpha_{d} ( F' ) .
  \end{aligned}$$

The proof for (1) $\Leftrightarrow$ (2) for $E$ stable is similar.

Let $F,G$ be semistable sheaves which are pure of dimension $d$.

1.  If $p_{F} >p_{G}$ then $\mathrm{Hom}_{X} ( F,G ) =0$

2.  If $p_{F} =p_{G}$ and $f:F \longrightarrow G$ is nontrivial then

    1.  $F$ stable implies $f$ injective

    2.  $G$ stable implies $f$ surjective

3.  If $p_{F} =p_{G}$ with $\alpha_{d} ( F ) = \alpha_{d} ( G )$ and
    $f:F \longrightarrow G$ is nontrivial then $f$ is an isomorphism

Let $f:F \longrightarrow G$ be nontrivial. Let
$E=  \mathsf{\mathrm{im}}  f$ and we factor $f$ as follows
$F \overset{\beta}{\longrightarrow} E
  \overset{\alpha}{\longrightarrow} G$. Semistability of $F$ and $G$
give $p_{F} \leqslant p_{E} \leqslant p_{G}$. This proves (1). If, in
addition, $F$ is stable and $p_{F} =p_{G}$, then
$p_{F} <p_{E} \leqslant p_{G}$ unless $F \cong E$. Hence $\beta$ is an
isomorphism, i.e. $f$ is injective. This proves (2a). The proof of (2b)
is similar. Part (3) follows since $P_{F}
  =P_{G}$ and by (2) $f$ is either injective or surjective, hence is an
isomorphism.

If $E$ is stable then $\mathrm{End}  E$ is a division algebra.

<span><span>$\mbox{}$</span></span>

1.  Assume $X$ is integral, then any line bundle is stable.

2.  If $F$ is decomposable, i.e. $F \cong F_{1} \oplus F_{2}$ where
    $F_{i} \neq 0$, then $F$ is not stable.
