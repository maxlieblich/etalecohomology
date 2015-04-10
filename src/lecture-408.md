# (Semi) Stability

If $F$ is a sheaf, we say $F$ is stable (resp. semi-stable) if, for all $E \subset F$, $p(E) < p(F)$ (resp. $p(E) \le p(F)$), where $p = P / \alpha_d $ is the reduced Hilbert polynomial.  

Note that $P$, the Hilbert polynomial is additive; $P: K(X) \to \mathbf{Z}[t]$, while $p$ is not, and that this definition is `relative' in the sense that we have to fix $\mathcal{O}(1)$.  

In the origins of the subject, curves, we can come up with an `absolute' definition.  Given a coherent sheaf $F$ on a curve $C$, we define the slope of the curve as $$\mu (F) = \text{deg} F / \text{rank} F.$$  (Recall that the degree of a $F$ is defined as $$ \text{deg} F = \text{deg} \det F ,$$ where $\det F = \Lambda^{\text{rk}F} F$.)

<div class="proposition"> 
Given coherent sheaves $F$, $G$ on a curve $C$, $p(F) \le p(G)$ if and only if $\mu(F) \le \mu(G)$.  
</div>

**Proof**  For a coherent sheaf $F$, let $r = \text{rank}(F)$.  We have $$P(F)(n) = \chi (C, F(n)) = \text{deg} F(n) + r(1-g) $$ by Riemann Roch.  But, $$ \text{deg} F(n) = \text{deg} \Lambda^{r} F(n) = \text{deg}( \Lambda^{r} F \otimes \mathcal{O}(nr) ) = \text{deg} F + nr \text{deg} \mathcal{O}(1).$$  

Substituting, we see that $$P(F)(n) = nr \text{ deg} \mathcal{O}(1) + \text{deg} F + r(1-g).$$  But, $r \text{ deg} \mathcal{O}(1) = \alpha_d$ (and, for later use, note that $ \alpha_{d-1} = \text{deg} F + r(1-g)$).  Therefore, $$p(F) = n + \frac{\text{deg} F + r(1-g)}{r \text{ deg} \mathcal{O}(1)} = n + \frac{\mu(F) + 1 - g}{\text{deg} \mathcal{O}(1)}$$  and we see that $p(F) \le p(G)$ if and only if $\mu(F) \le \mu(G)$, independent of $\mathcal{O}(1)$.  QED.

Remark.  This definition of degree agrees with our previous definition of degree: if $F$ has rank $r$, we defined the degree deg' to be $$\text{deg'} F = \alpha_{d-1}(F) - r \alpha_{d-1} \mathcal{O}$$ but, by above, $ \alpha_{d-1}( F)  = \text{deg} F + r(1-g)$ and $\alpha_{d-1} \mathcal{O} = 1- g$, so we see that $\text{deg'}F = \text{deg}F$.  

Remark.  While $p$ is not additive, $\mu$ satisfies the relationship $$\mu (F \otimes G) = \mu(F) + \mu (G)$$.  Why?  Note that $\det(F\otimes G) \cong (\det F)^{\text{rk}G}\otimes (\det G)^{\text{rk}F}$, so $\deg (F\otimes G) = \deg F \text{rk} G + \text{rk} F \deg G$.  Therefore, $$\mu (F \otimes G) = \frac{\deg(F\otimes G)}{\text{rk}F\otimes G} = \frac{\deg F \text{rk} G + \text{rk} F \deg G}{\text{rk} F\text{ rk} G} = \mu(F) + \mu (G).$$

Definition.  On a curve $C$, we say $F$ is semi-stable (resp. stable) if, for all $E \subset F$, $\mu(E) \le \mu(F)$ (resp. $\mu(E) < \mu(F)$). 

### An Example of a Stable Vector Bundle (that is not Geometrically Stable)

Example.  We construct a stable vector bundle $V$ on a conic $C$ over $\mathbf{R}$ such that $V \otimes \mathbf{C}$ is not stable; i.e. a vector bundle that is stable but not geometrically stable.  

Let $C = \text{Proj} (x^2 + y^2 + z^2 = 0) \subset \mathbf{P}^2_{\mathbf{R}}$.  Then, $C$ is an \'{e}tale form of $\mathbf{P}^1_{\mathbf{R}}$ and a Brauer Severi variety $C \to \text{Spec} \mathbf{R}$.  Then, $\mathbf{H} = [C] \in Br(\mathbf{R})$, so in the map $Br(\mathbf{R}) \to Br(C)$, $\mathbf{H} \mapsto 0$.  (In general, if $V$ is a Brauer Severi variety over a field $k$, the sequence $$\mathbf{Z}[V] \to Br(k) \to Br(V) $$ is exact.)  

Now, let $\phi: \mathcal{X} \to \text{Spec} \mathbf{R}$ be a $\mathbf{\mu}_2$ gerbe representing $[\mathbf{H}]$.  Then, $\mathbf{H} \cong \mathcal{E}nd(V)$, where $V$ is a locally free $\mathcal{X}$-twisted sheaf of rank 2.  Let $\pi: \mathcal{C} \to C$ be the pullback of $\mathcal{X}$ to $C$.  If $G = V|_C$, then $End(G) = \mathbf{H}$, and because the Brauer class of $\mathbf{H}$ is trivial, there exists an invertible $\mathcal{C}$-twisted sheaf $L$.  Let $F = \pi_*(G \otimes L^{\vee})$.  Then $F$ is a sheaf on $C$ satisfying $End(F) \cong \mathbf{H}$.  

Now, we note that $F \otimes \mathbf{C} \cong L \oplus L$, where $L$ is an invertible $\mathcal{X}_\mathbf{C}$-twisted sheaf (because the Brauer class of $\mathbf{H}$ becomes trivial), so $F \otimes \mathbf{C}$ is semi-stable.  It is clearly not stable, but (by a result we haven't proven yet), this implies $F$ is semi-stable.  Next, we claim that this implies $F$ is actually stable.  

If $E \subset F$ is a saturated proper subsheaf, to show $F$ is stable, we must show that $\mu (E) < \mu (F)$.  But, we must have $\text{rank}E = 1$, and $\det(F) \cong \mathcal{O}$, so we must show $\deg E < 0$.  We already know $F$ is semi-stable, so it suffices to show $\deg E \ne 0$.  

However, if $E \subset F$ has degree 0 (and is saturated), $E$ and $F/E$ are invertible sheaves (because saturated implies torsion free, which implies locally free on smooth curves) with degree 0.  Because $C$ is a conic, this implies $E \cong \mathcal{O} \cong F/E$.  However, this implies the short exact sequence $$0 \to E \to F \to F/E \to 0$$ is in fact $$0 \to \mathcal{O} \to F \to \mathcal{O} \to 0 .$$  But, for our conic $C$, $0 = H^1(C,\mathcal{O}) =  Ext^1(\mathcal{O}, \mathcal{O})$, so the sequence splits and $F \cong \mathcal{O} \oplus \mathcal{O}$.  But, this implies $End(F) \cong M_2(\mathbf{R})$, a contraction.  Therefore, $\deg E < 0$ and $F$ is stable.  

As an aside, this is a fun thing to think about: 

Conjecture: If $k$ is a field, for all Brauer Severi varieties $V \to \text{Spec }k$, there exists a curve $C \subset V$ of genus 1.  



### Harder-Narasimhan Filtration 

Definition. If $X$ is a projective scheme of dimension $d$ and $E$ a pure $d$ dimensional sheaf, then the Harder-Narasimhan filtration (HNF) of $E$ is a filtration $$ 0 = HN_0(E) \subset HN_1(E) \subset \cdots \subset HN_n(E) = E $$ such that, for $i = 1, \ldots, n$, $HN_i(E)/HN_{i-1}(E)$ is semi stable with reduced Hilbert polynomial $p_i$ and $p_1 > p_2 > \ldots p_n$.  

<div class="theorem"> 
The HNF exists and is unique (justifying the use of the word ``the'').  
</div>

Idea. to make the HNF, we want to find $F \subset E$ such that $p(F)$ is maximal among $p(G)$, $G \subset E$.  This motivates the following definition: 

Definition. A maximal destabilizing subsheaf $F$ os $E$ is a subsheaf $F$ such that, for all $G \subset E$, $p(F) \ge p(G)$ and, if $p(F) = p(G)$, then $G \subset F$.  

Remark.  By the very definition, if $F$ exists, it is unique.  

<div class="proposition"> 
A maximal destabilizing subsheaf exists.  (The proof is coming...) 
</div>

<div class="corollary"> 
The HNF exists.  
</div>

**Proof** Let $HN_1 = F$ and $E' = E/F$.  By induction on the rank, we can assume the HNF for $E'$ exists.  Then, if $$0 \subset E_1' \subset \dots \subset E_n' \subset E'$$ is the HNF for $E'$, and $\pi: E \to E'$ is the quotient map, let $E_{i+1} = \pi^{-1}(E_i')$.  We claim that $$0 \subset E_1 = F \subset E_2 \subset \dots \subset E_{n+1} \subset E$$ is the HNF for $E$.  From the HNF for $E'$, we can conclude that $E_i/E_{i-1}$ is semi stable for $i>2$ and $p_2 > p_3 > \ldots > \p_{n+1}$ (where $p_i$ is the reduced Hilbert polynomial of $E_i/E_{i-1}$).  We know $F$ is semi stable, so it suffices to show that $p(F) = p_1 > p_2$.  

But, considering the sequence $$ 0 \to F \to E_2 \to E_1' \to 0 ,$$, by assumption, $p(F) > p(E_2)$.  We want to show $p(E_2) \ge p(E_1') = p_2$ to conclude $p_1 = p(F) > p_2$.  However, $p(E_2) \ge p(E_1')$ if and only if $p(F) \ge p(E_2)$, which we know by assumption, so we conclude $p_1 > p_2$ and the HNF exists. QED.

<div class="corollary">  
The HNF is unique.  
</div>

**Proof**  Suppose $$0 = E_0 \subset E_1 \subset \ldots \subset E_n = E$$ and $$0 = E_0' \subset E_1' \subset \ldots \subset E_{n'}' = E$$ are two such filtrations.  Without loss of generality, assume that $p(E_1') \ge p(E_1)$.  To show the $n = n'$ and $E_i = E_i'$ for all $i$, it suffices to show that $E_1' \subset E_1$.  Then, because $E_1$ is semi stable, this would imply $p(E_1') \le p(E_1)$, so reversing the argument shows $E_1 = E_1'$.  Proceeding by induction on the rank would show the filtrations are the same.  

To show $E_1' \subset E_1$, let $i$ be minimal such that $E_1' \subset E_i$.  Because $i$ is minimal, the map $E_1' \to E_i/E_{i-1}$ is nonzero.  Let $Q$ be the image of $E_1'$.  Because $E_1'$ is semi stable and $Q$ is a proper quotient, $p(Q) \ge p(E_1')$.  Because $E_i/E_{i-1}$ is semi stable, if $Q$ is a subsheaf, $p(E_i/E_{i-1}) \ge p(Q)$.  Combining these two inequalities with out assumption ($p(E_1')>p(E_1)$), we see that $$p_i = p(E_i/E_{i-1}) \ge p(Q) \ge p(E_1') \ge p(E_1) = p_1.$$  However, if $i \ne 1$, this implies $p_i \ge p_1$, a contraction by definition of the HNF.  Therefore, $i = 1$, and hence $E_1' \subset E_1$, as desired.  QED.

