## Gerbes, Bands, and Quasi-Coherent Sheaves
<!--
Custom macros can be found in raw file index.md in the src folder.
Some examples are C: "{\\bf{C}}" and Hom: "{\\operatorname{Hom}}"
-->
<!--
Simple commutative diagrams can be made using the AMScd package, but require the command "\require{AMScd}".
For example:
$$
\require{AMScd} \begin{CD}
A @>f>> B \\
@VgVV @VVhV \\
C @>>j> D \\
\end{CD}
$$
-->

Lecture notes for 25 February, 2015.  They could use some cleaning up and buffing up.

### What is a gerbe and where is $G$?

Let $S$ be a site and $X \rightarrow S$ a stack.  X is a gerbe if
- for all $s \in S$, there exists a covering $u \rightarrow s$ such that $X(u) \neq \emptyset$
- for all $s \in S$ and $x, y \in X(s)$, there exists a covering $u \rightarrow s$ such that $x|_{u} \cong y|_{u}$

Consequence: $F(s) = $ isomorphism classes in $X(s)$, $F^s = $ sheaf of singletons

Example: $BG$ stack of $G$-torsors

Question: Can we recover $G$ from BG?

Answer: Yes, but only if we think of $G$ as a *band* (lien).

### What is a band?

How would we try and recover $G$?

$BG(S)$ contains the trivial torsor $G \times S \rightarrow S$ for which $\operatorname{Aut} \cong G^{op}$.

Na&iuml;ve idea: Recover $G$ in general by searching for objects $x_i \in X(s_i)$ and glue.

Issue: Gluing can have an inner automorphism obstruction.

Upshot: We can associate to any gerbe $X$ a band that is locally made of groups, but inner automorphismims have to be decreed to equal the identity.

The stack of bands on $S$:
- start with stack of groups on $S$: $\operatorname{Grp}_S$
- make new fiber category $PB(S)$
  - objects: groups
  - $\operatorname{Hom}(G,H) = \operatorname{Inn}(H)\backslash\operatorname{Isom}(G,H)/\operatorname{Inn}(G)$
- bands: stackification of $PB$.

There is a map of stacks: $\operatorname{Grp}_S \rightarrow \operatorname{Band}_S$.  This map is not essentially surjective.

Better: The composition $\operatorname{Ab}_S \subseteq \operatorname{Grp}_S \rightarrow \operatorname{Band}_S$ is fully faithful.

Any gerbe $X$ has a canonically associated band: $\exists ! B \in \operatorname{Band}(S)$ and isomorphism $B_{X} \overset{\sim}{\rightarrow}\operatorname{band}(I)$.  Here, $I$ denotes the inertia stack and $B_X = \pi^{-1}B$, where $\pi: X \rightarrow S$.

Given $G \in \operatorname{Grp}$, any inner form of $G$ is canonically isomorphic to $G$ in $\operatorname{Band}_S$.

Inner form examples:
Let $A$ be an Azumaya algebra and let $A^\times$ denote the functor of units: $A^{\times}(T) = \Gamma(T, A_T)^{\times}$.
- $A^\times$ is an inner form of $\operatorname{GL}_n$
- $A_1^\times = \ker(\operatorname{Nrd}:A^\times \rightarrow \bf{G}_m)$ is an inner form of $\operatorname{SL}_n$

Subexample: Let $X$ be a proper, smooth, geometrically connected variety over $k$.  Let $V$ on $X$ be a geometrically simple vector bundle, e.g. a geometrically stable vector bundle: 
$\operatorname{Hom}_{{\scr{O}}_X}(V, V) = k$, $A = \operatorname{End}(V,V)$, $A^\times(X) = k^\times$.

###Quasi-coherent sheaves

Quasi-coherent sheaves on the fppf site of a scheme $X$: $(T \overset{f}{\rightarrow} X) \mapsto \Gamma(T, f^*F)$, ${\scr{F}} \in \operatorname{QCoh}(X_{zar})$.

Warning: $\operatorname{QCoh} \rightarrow {\scr{O}}_X-\operatorname{Mod}$ is not exact in the big sites!

Let $X$ be a stack on $S_{fppf}$.  A sheaf $F$ on $X$ is quasi-coherent if for all $T \overset{f}{\rightarrow} X$ (equivalently, for all $f \in X(T)$), $f^{-1}F \in {\scr{O}}_{T_{fppf}}-\operatorname{Mod}$ is quasi-coherent.  Here
$$
\begin{array}{rccc}
f^{-1}F : &  \operatorname{Sch}_T & \rightarrow & \underline{\operatorname{Set}} \\
& U \underset{g}{\rightarrow} T & \mapsto & F(fg) \\
\end{array}
$$

Confusing point: If $U \overset{f}{\rightarrow} T$ and $F \in \operatorname{QCoh}(T_{fppf})$, then 
$$
f^{-1}F = f^{*}F
$$
Here, $f^{-1}F$ denotes the restriction in $T_{fppf}$ while $f^*F$ denotes the Zariski pullback.

Look for "Cartesian sheaves" in Laumon & Morret-Bailly (*Champs Alg&eacute;briques* (?)), Stacks Project, or elsewhere.

Example: $G$ a finite group over $\bf{C}$.  What is $\operatorname{QCoh}(BG)$?

First thought:
$$
\begin{array}{ccc}
\operatorname{Spec}{\bf{C}} & \rightarrow &  BG \\
\\
V & --- & F \\
\mathrm{vector \; space}
\end{array}
$$
