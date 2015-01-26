Let's start with the short exact sequence 
$$ 1 \rightarrow \G_m \rightarrow GL_n \rightarrow PGL_n \rightarrow 1. $$

Here, $PGL_n$ is defined to be the sheafification of the cokernel presheaf $GL_n / \G_m$. We don't have sheaves of abelian groups and so we are not necessarily working with an abelian category (unless $n=1$). So how do we define derived functors ? We shall restrict ourselves to $H^1$ and motivate the definition in the non-abelian setting by first recalling properties of $H^1$ in the abelian sheaf setting.  First, some definitions.  

**Torsors** : Let $G$ be a sheaf of groups on $\Et(X)$. Let $S$ be a sheaf of sets on which $G$ acts by the right. Then, $S$ is called a torsor for $G$ if 
- there exists an etale covering $U \rightarrow X$ such that $S(U) \neq \emptyset$.
- for every etale $U \rightarrow X$ and $s \in \Gamma(U,S)$, the map $G|U \rightarrow S|U$ given by $g \rightarrow s \cdot g$ is an isomorphism of sheaves.

A torsor $S$ is called the trivial torsor if it is isomorphic as a sheaf to $S=G$ (with $G$ acting on $S=G$ by right multiplication). 

##### An exercise : $H^1$ in terms of iso-classes ? 

Let $G$ be an abelian sheaf on the small etale site $\Et(X)$. Prove that elements of $H^1(\Et(X), G)$ are in one-to-one bijection with the set of iso-classes of left $G$-torsors in the etale topology. 

**Proof** The proof is given in Milne's notes on Etale cohomology and we provide a sketch here. We proved last quarter that $H^1$ for sheaf cohomology on the etale site can actually be calculated using Cech cohomology. 


### Non abelian $H^1$. 

### Two descriptions of $H^1(\Et(X),PGL_n)$ :

$$ f : \{\text{C.S.A.'s over $k$ of degree $n$} \} \rightarrow \{\text{Varieties of left ideals of $A$ of rank $n$}\}  $$

### A geometric construction : 

Now we won't give a proof of why the map $\F$ gives a bijection. However, let's give a description of the map. If $A$ is a CSA over $k$, then $f(A)$ is a functor that sends a $k$-scheme $T$ to the ideal $I_{A,T} \subset A_T$

### Severi-Brauer varieties  

A Severi-Brauer variety over a field $k$ is an algebraic variety $X$ of dimension $n$ such that $X \times_k \overline{k} \cong \P^{n-1}_k$.

Aside : What are the left ideals of $M_n(k) = End(V)$, where $V=k^n$. The left ideals are in $1-1$ correspondence with the subspaces of $V$. Every left ideal $I \subset Hom(V,V)$ corresponds to a subspace $W$ of $V$ where $W$ is the set of points in $V$ that vanish on all elements of $I$, i.e. $I=Hom(V/W,V)$. What are the right ideals $J$ of $End(V)$ ? They are also given by subspaces $W$ with the correspondence given by $J = Hom(V,W)$.


<div class="corollary">
Let $X$ be a Severi-Brauer variety over $Spec(k)$. Then $X \cong \P_k^{n-1}$ if and only if $X(k) \neq \emptyset$.
</div>

**Proof** It suffices to show that $X(k) \neq \emptyset$ will imply that $X \cong P_k^{n-1}$. Let $A$ be the CSA over $Spec(k)$ that corresponds to the variety $X$ in the construction above. The construction given above tells us that if $X(k) \neq emptyset$, then there exists a left ideal $I \subset A$ of rank $n$.  We get a map $\gamma : A \rightarrow End_k(I)$ where the vector space dimension of $A$ and $End_k(I) \cong M_n(k)$ equal $n^2$. Also, $A$ is simple. Hence, $\gamma$ has to be an isomorphism.  
