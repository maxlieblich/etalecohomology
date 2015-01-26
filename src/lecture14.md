Let's start with the short exact sequence 
$$ 1 \rightarrow \G_m \rightarrow GL_n \rightarrow PGL_n \rightarrow 1. $$

What is $PGL_n$ ? The following are equivalent (which we state without proof for now). 
1.  $PGL_n$ is defined to be the sheafification of the cokernel presheaf $GL_n / \G_m$. 
2.  $PGL_n$ is defined to be $Aut(P^{n-1})$.
3.  $PGL_n$ is defined to be  $Aut(M_n)$.
4.  We can define $PGL_n / Spec(Z)$ to be the sheaf represented by the element $Spec S$, where $S$ is the degree zero part of  $Z[x_0 \ldots, x_n , det^{-1}]$ . And $PGL_n$ over any scheme $S$ is obtained via base change. 

When $n \geq 2$, the sheaves $GL_n$ and $PGL_n$ do not always take values in the category of abelian groups. So we need to be a little careful when describing cohomology. Remember though that for abelian sheaf cohomology in the etale or fppf site, $H^1$ for abelian sheaf cohomology can be given by Cech cohomology $\hat{H}^1$ for presheaves.  Let's motivate the definition for non-abelian $H^1$ by recalling what happens in the abelian case. First, some definitions.  In what follows, $H^1$ would denote Cech $H^1$. 

**Torsors** : Let $G$ be a sheaf of groups on $\Et(X)$. Let $S$ be a sheaf of sets on which $G$ acts by the right. Then, $S$ is called a torsor for $G$ if 
- there exists an etale covering $U \rightarrow X$ such that $S(U) \neq \emptyset$.
- for every etale $U \rightarrow X$ and $s \in \Gamma(U,S)$, the map $G|U \rightarrow S|U$ given by $g \rightarrow s \cdot g$ is an isomorphism of sheaves.

A torsor $S$ is called the trivial torsor if it is isomorphic as a sheaf to $S=G$ (with $G$ acting on $S=G$ by right multiplication). 

##### An exercise : Cech $H^1$ in terms of iso-classes ? 

Let $G$ be an abelian sheaf on the small etale site $\Et(X)$. Prove that elements of $\hat{H}^1(X, G)$ are in one-to-one bijection with the set of iso-classes of left $G$-torsors in the etale topology. 

**Proof** See Proposition 11.1 in Milne's notes on [Etale cohomology](http://www.jmilne.org/math/CourseNotes/LEC210.pdf). 

**TWisted forms**
Two schemes $X$ and $Y$ are forms of each  other if $X \times k^{sep} \cong Y \times k^{sep}$. Let's work over the small etale side of a field $Spec(k)$. We saw last quarter that sheaves on this site are representable, by evaluating the sheaf $\F$ on $\colim_{L \subset k^{sep}} \F(k^{sep}/L)$.  

<div class="lemma">
Let $k$ be a field.  There exists a bijection between elements of $H^1(spec(k),Aut(F))$ and isomorphism classes of (twisted) forms of $F$.
</div> 

See Theorem 14.89 in[Algebraic Geometry - Schemes with Examples and exercises](https://www.math.ucdavis.edu/~blnli/buildings/bag.pdf). As an immediate corollary, we get the following corollary. 

### A geometric construction relating the two descriptions of $H^1(X,PGL_n)$ :

<div class="corollary">
We have two description for the elements of $H^1(Speck, PGL_n)$
1. Isomorphism classes of central simple algebras of degree $n$. 
2. Isomorphism classes of varieties over $spec(k)$ that are isomorphic over $\bar{k}$ to $\P^{n-1}$.  These varieties are called **Severi-Brauer varieties**. 
</div>

What is the map relating these two descriptions ? 

$$ f : \{\text{C.S.A.'s over $k$ of degree $n$} \} \rightarrow \{\text{Severi-Brauer varieties that are forms of $\P^{n-1}$}\}  $$

We shall simply construct this map but won't give a proof of its bijection. For a proof, one can look at Chapter 8 and Chapter 14 in [Algebraic Geometry - Schemes with Examples and exercises](https://www.math.ucdavis.edu/~blnli/buildings/bag.pdf)

Let $A$ be a CSA over $k$. Then we shall give a description of the functor that the variety $f(A)$ represents. 

$$
f(A) : k-schemes \rightarrow Sets 
$$
$$
f(A) (T) = \{I \subset A_T | \text{ is a left ideal such that } A_T/I \text{ is a locally free sheaf of rank } n^2-n \}.
$$

For example, if $k=\R$, then the non-trivial element in the Brauer group given by the quarternions gets sent to the 
variety given by the conic $x^2 + y^2 + z^2 = 0$. 

Aside : What are the left ideals of $M_n(k) = End(V)$, where $V=k^n$. The left ideals are in $1-1$ correspondence with the subspaces of $V$. Every left ideal $I \subset Hom(V,V)$ corresponds to a subspace $W$ of $V$ where $W$ is the set of points in $V$ that vanish on all elements of $I$, i.e. $I=Hom(V/W,V)$. What are the right ideals $J$ of $End(V)$ ? They are also given by subspaces $W$ with the correspondence given by $J = Hom(V,W)$.

The functor given by $f(M_n(k))$ is representable by $P^{n-1}$. To see this, we note that $Hom(X,\P^{n-1})$ is in bijection with invertible quotients of $O_X^{n+1}$. 

<div class="corollary">
Let $X$ be a Severi-Brauer variety over $Spec(k)$. Then $X \cong \P_k^{n-1}$ if and only if $X(k) \neq \emptyset$.
</div>

**Proof** It suffices to show that $X(k) \neq \emptyset$ will imply that $X \cong P_k^{n-1}$. Let $A$ be the CSA over $Spec(k)$ that corresponds to the variety $X$ in the construction above. The construction given above tells us that if $X(k) \neq emptyset$, then there exists a left ideal $I \subset A$ of rank $n$.  We get a non-zero map $\gamma : A \rightarrow End_k(I)$ where the vector space dimension of $A$ and $End_k(I) \cong M_n(k)$ equal $n^2$. Also, $A$ is simple. Hence, $\gamma$ has to be an isomorphism.  So, $A\cong M_n(k)$. We already saw that in this case, $f(A)$ is in fact the functor represented by $\P^{n-1}$.
