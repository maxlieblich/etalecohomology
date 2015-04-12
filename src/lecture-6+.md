# Cohomology of sheaves, Cech-to-sheaf spectral sequence


###Quasi-coherent sheaves

#####ZARISKI site

Let $X$ be a scheme. On the big ZARISKI site of a scheme $X$, we define a quasi-coherent sheaf as follows. $F$ is said to be a a quasi-coherent sheaf of $O_X$-module if there exists an open covering $U \rightarrow X $ such that the following sequence is exact.
$\oplus_I O\mid_{U} \rightarrow \oplus_J O\mid_{U} \rightarrow F \mid_U \rightarrow 0$.

**Lemma**
Let $g : X \rightarrow Y$ be a map of schemes. If $F$ is a quasi-coherent sheaf of $O_Y$-modules, then $f^{*} F$ is a quasi-coherent sheaf of $O_X$-modules.

**Proof:**
See Lemma 10.4 in <http://stacks.math.columbia.edu/download/modules.pdf>.

** Lemma **
If $Y=Spec(A)$ is an affine scheme, then a quasi-coherent sheaf $F$ is "given" by an $A$-module $M$. If $g : X=Spec(B) \rightarrow Y = Spec(A)$ is a map of schemes, then $f^*(F)$ is "given" by $M \otimes_A B$.

** Proof**
See Lemma 10.5, Lemma 10.7 in <http://stacks.math.columbia.edu/download/modules.pdf>.

We state the following useful facts/terminologies/results from  Vistoli (Notes on Grothendieck topologies, fibered categories and descent theory, Page 35). Let $C$ be a category and $\{U_i \rightarrow U\}_{i \in I}$ be a set of arrows. A refinement of this set of arrows $\{U_i \rightarrow U\}_{i \in I}$ is a set of arrows $\{V_j \rightarrow V\}_{j \in J}$ such that for each index $j \in J$, there exists  an index $i \in I$ such that $V_j \rightarrow U $ factors through $U_i \rightarrow U$.

Let $C$ be a category and $T$ and $T'$ be two Grothendieck topologies on $C$. We say that $T$ is subordinate to $T'$ (and write $T < T'$) if every covering in $T$ has a refinement that is a covering in $T'$. If $T < T'$ and $T' < T$, then we say $T$ and $T'$ are equivalent to each other. Proposition 2.49 in Vistoli's notes  states the following.
** Proposition**
+Two equivalent  Grothendieck topologies $T$ and $T'$ on a category $C$ have the same sheaves.

In the cases we are interested in, $C=X_\star$, where $X$ is a scheme and $\star \in \{ZAR,ETALE, fppf, etale,zar\}$. Each of these sites comes with a Grothendieck topology. For each site and each covering $\{U_i \rightarrow U\}_{i \in I}$, it is possible to consider a refinement $\{V_j \rightarrow U\}_{j \in J}$ such that for each $j \in J$, $V_j$ is an object in the category $Sch/X$ and the set of maps $\{V_j \rightarrow V\}_{j \in J}$ is a covering in $X_\star$. This is explained in the Stacks project <http://stacks.math.columbia.edu/tag/021L>.  See Lemma 33.7.7.


Let us say $\star=fppf$. We can define a new Grothendiek topology $X_{std.fppf}$ on $Sch/X$ where the coverings $\{U_i \rightarrow U\}_{i \in I} $ are such that for each $i \in I$, $U_i$ is affine and for each object $U \in Sch(X)$ the set of arrows $\{U_i \rightarrow U\}_{i \in I}$ is a covering in $X_{fppf}$. This gives us a refinement of the fppf coverings. In the reference given to the stacks project above, they call it ``standard fppf coverings''.

The fact mentioned in the previous paragraph and Proposition 5 will allow us to consider sheaves on $X_{fppf}$ by considerng sheaves on $X_{std.fppf}$. So, we shall sort of abuse notation and use the two sites $X_{fppf}$ and $X_{std.fppf}$ interchangeably.

######fppf site

Let $X$ be a scheme. We consider the fppf site (or std.fppf) $X_{fppf}$. For each object $f: T \rightarrow X$ in $C_{/X}$, we have a map between sliced categories $C_{/X} \rightarrow C_{/T}$, which gives us a map between presheaves $f^{*} : PreSh(X) \rightarrow PreSh(T)$.  Given a quasicoherent sheaf $F$ on $X_{ZAR}$, we define a quasicoherent sheaf $\underline{F}$ on $X_{fppf}$ as follows. Note that we can consider $F$ as a presheaf on $C_{/X}$ (there are no conditions on coverings). First, we define
$$
\underline{F}(T) = f^{*}(F)(T).
$$

We need to show that $\underline{F}$ is a sheaf. We shall do the following
1.  Prove that $\underline{F}$ is a sheaf in the case when $X=Spec(A)$ is affine.
2. For the general case, use descent theory. Cover $X$ by affines $\{U_i\rightarrow X\}_{i \in I}$ and then glue the sheaves together.

###### $X=Spec(A)$
[??? At this point, I really don't understand why we can replace arbitrary affine coverings with finite affine coverings. If the category allows arbitrary disjoint unions, then I suppose it is possible to look at a covering by a single object. See proof of Lemma 2.60 in his notes ???]

Given an $A$-module $M$, our goal is to show that the presheaf $f^*(F)$ is a sheaf in the $X_{fppf}$ site (we show it for the $X_{std.fppf}$ site). Consider an affine fppf covering $T \rightarrow X$, where $T=Spec(B)$. By some Lemmas stated above, we observe that if $F$ is given by the $A$-module $M$, then $f^{*}(F)(T) = M \otimes_A B$. And we need to show that the following sequence is exact.
$$
M \rightarrow M \otimes_A B \stackrel{\rightarrow}{\rightarrow} M \otimes_A (B \otimes_A B).
$$
The usual trick is to show that the sequence above is exact after a faithfully flat base change. We tensor equation above  with $B$ (which is a faithfully flat extension of $A$). The faithfully flat extension $A' \rightarrow B'$ is such that $B' \cong A' \oplus I$ as $A$-modules. Here $A' = B$ and $B'=B \otimes_A B$. After this base change, we have the sequence
\begin{align}
M' \rightarrow   M' \otimes_{A'} B'  \stackrel{\rightarrow}{\rightarrow} M' \otimes_{A'} (B' \otimes_{A'} {B'}).
\end{align}
or equivalently
\begin{align}
M' \rightarrow  M'\oplus M' \otimes I  \stackrel{\rightarrow}{\rightarrow}  M' \oplus (M' \otimes I) \oplus (M' \otimes I) \oplus (M' \otimes I) \oplus (M' \otimes (I \otimes I)).
\end{align}
Chasing the diagram properly then gives us that the sequence above is exact.
######Descent datum

I have to check the gluing data (I suppose most importantly the cocycle condition) but I cannot get myself to descend to this level.

#######Cech cohomology of quasi-coherent sheaves for Affines

Here, $X=Spec(A)$ is an affine scheme.

**Proposition**
$\hat{H}^i(X_{fppf},\underline{F})=0$.

We will show the cohomology associated to the Cech complex $ 0 \rightarrow M \otimes_A B \rightarrow M \otimes_A (B \otimes_A B) \rightarrow \ldots$ is zero (i.e. it is exact). As usual, we will use the faithfully flat base change trick and assume that $A \rightarrow B$ has a retraction and we identify $B$ with $A \oplus I$ (as an $A$-module). In the previous section, we only showed the $0^{th}$ cohomology group equals $M$. But we can show that this sequence is in fact homotopic to a sequence where all the maps are the zero maps.

\begin{align*}
M \rightarrow & M \otimes_A B \rightarrow  & M \otimes_A (B \otimes_A B)\rightarrow & \ldots \\ \\
M \rightarrow & M \otimes_A B \rightarrow& M \otimes_A (B \otimes_A B) \rightarrow& \ldots
\end{align*}


There are  vertical maps that are all the identity maps. The horizontal maps in the bottom row are all zeroes. Every element $b \in B$ can be identified with a unique pair $(a,i)$, where $a \in A$ and $i \in I$. In addition, we also have
\begin{align*}
s_1 :& M \otimes_A B \rightarrow  M & \qquad & m \otimes (a,i) \rightarrow a\cdot m \\
s_2 :& M \otimes_A (B \otimes_A B) \rightarrow  M \otimes_A B & \qquad & m \otimes (b_1 \otimes b_2) \rightarrow m \otimes (b_1 b_2) \\
s_3 :& M \otimes_A (B \otimes_A B \otimes_A B) \rightarrow M \otimes (B \otimes_A B) & \qquad & m (b_1 \otimes b_2 \otimes b_3) \rightarrow m \otimes \left((b_1 b_2) \otimes b_3 - b_1 \otimes (b_2 b_3) \right)
\end{align*}

Similarly the map $s_4$ sends $m \otimes (b_1 \otimes b_2 \otimes b_3 \otimes b_4)$ to $$m \otimes \big( (b_1 b_2) \otimes b_3 \otimes b_4 - b_1 \otimes(b_2 b_3) \otimes b_4 + b_1 \otimes b_2 \otimes(b_3b_4) \big).$$ The other maps are defined simiarly. I suppose we needed the retraction only to define $s_1$ (?).

######Cohomology of quasi-coherent sheaves

We now assume that $X$ is quasi-compact and quasi-separated.

**Proposition : $H^i_{fppf}(X_{fppf}, \underline{F}) = \hat{H}_{Cech}^{i}(X_{ZAR},F)$.**

We give the proof in several steps.
I suppose we need to check that $\Phi(\underline{F})$ is the presheaf associated to $F$ but we omit this (??).

Then, we use spectral sequences.
\begin{align*}
Sh(X_{fppf}) \rightarrow^{\Phi} PreSh(X) \\
PreSh(X)\rightarrow^{\mathscr{G}} Ab \\
Sh(X_{fppf}) \rightarrow _{\Gamma} Ab
\end{align*}

We have the theory of spectral sequences
\begin{align*}
R^i\mathscr{G}\left(R^j\Phi\left( \underline{F} \right) \right) \implies R^{i+j}\Gamma (\underline{F})
\end{align*}

** Lemma : **
For $j >0$, we have $R^0 \mathscr{G}( R^j\Phi(\underline{F})) =0$. (This lemma does not require $\underline{F}$ to be quasi-coherent. It holds for any sheaf in general).

**Proof**
\begin{align*}
Sh(X_{fppf}) \xrightarrow {\Phi} PreSh(X) \xrightarrow {s} Sh(X_{fppf})
\end{align*}
The functor $s$ is the sheafification functor and is exact. And the composition $s \circ \Phi = id$, whose $i^{th}$derived functors vanish if $i >0$. Also we note that from the construction of the sheafification functor, we have a mono $R^0 \mathscr{G}( R^j\Phi(F)) \rightarrow R^0 \mathscr{G}( R^j\Phi(F))^s$ And $ R^0 \mathscr{G}( R^j\Phi(F))^s= R^{j}(s \circ \Phi)(F) = 0 $ if $j >0$.

** Lemma **
$R^1\Gamma(\underline{F}) = R^1 \mathscr{G}(\Phi(\underline{F}))$ (Again, this lemma does not require $\underline{F}$ to be quasi-coherent)


**Proof**
The theory of spectral sequences gives us an exact sequence
$$0 \rightarrow R^1 \mathscr{G}(\Phi(\underline{F})) \rightarrow R^1\Gamma(\underline{F})  \rightarrow R^0 \mathscr{G}(R^1(\Phi(\underline{F}))) $$
+The previous lemma tells us that $R^0 \mathscr{G}(R^1(\Phi(\underline{F}))) =0$ and the lemma follows.

Let $f : U \rightarrow X$ be an affine open fppf covering. Note that we also have a spectral sequence

\begin{align*}
Sh(X_{fppf}) \rightarrow_{f_*} Sh(U_{fppf}) \\
Sh(U_{fppf}) \rightarrow^{\Gamma} Ab \\
Sh(X_{fppf}) \rightarrow_{\Gamma_U} Ab \\
\end{align*}
which gives us that $R^i\Phi(\underline{F})(U) = H^i_{fppf}(U,\underline{F})$, since $f_*$ is exact. (again this is valid for any sheaf and not just a quasi-coherent sheaf).

**Lemma**
Let $U$ be an affine. Then $Qcoh(U_{fppf}) \subset Sh(U_{fppf})$ and $QCoh_{ZAR}(U) \subset PreSh(U)$ are abelian and have enough injectives.  So, the presheaves $R^i\Phi(\underline{F})$ are also quasi-coherent.


??? I am not exactly surely of this. I think the proof is given in section 21 of <http://stacks.math.columbia.edu/download/properties.pdf>. I also don't know if this is an overkill to prove what we want(???).

**Lemma**
In the spectral sequence above, we claim that all the terms
$R^i\Phi(R^j\mathscr{G}(F)) =0 $, if $j >0$ and $i \neq 0$.


This is sufficient to prove the proposition. However, we only prove the lemma for the case $X=U$ is affine. (??? Now, I have no idea to go from the affine to general case. Somehow the separated condition  makes it easier. Stacks project <http://stacks.math.columbia.edu/download/etale-cohomology.pdf> has a proof. See Theorem 22.4 there.???)

\begin{align*}
 Sh(U_{fppf}) \rightarrow _{\Phi} PreSh(U)\\
 PreSh(U) \rightarrow ^{\mathscr{G}_U} Ab \\
 Sh(U_{fppf}) \rightarrow_{\Gamma_U} &Ab
\end{align*}

We have the spectral sequence $ R^i\Phi R^j \mathscr{G}_U (\underline{F})\implies R^{i+j}(\Gamma_U)(\underline{F})$. We claim that (and it is equivalent to proving the lemma for the affine case since all the terms on the x-axis of the $E_2$ page also vanish) all the terms on the $E_2$ page (except possibly the $(0,0)^{th}$ term vanishes). We already showed that this is true when $i+j=1$. Now consider the $i+j=2$. We already have $R^i\mathscr{G}_U R^j\Phi (\underline{F}) =0 $ for $(i,j)$ equal to $(2,0)$ and $(0,2)$. Now $R^1\Phi (\underline{F})$ is quasi-coherent and hence $R^1 \mathscr{G}_U R^1 \Phi (\underline{F}) $ is also equal to zero.  Proceed similarly through induction/iteration on $i+j$.
