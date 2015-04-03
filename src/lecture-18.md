Lecture notes from January 16, 2015.

(Below is Yannick's reformating of Sid's LaTeX file based off of Yannick's handwritten notes.  Naturally, all mistakes are due to Sid.)

Given a CSA over $k$, set
$$
I = {\operatorname{Isom}}(A, M_n)
$$
Then $I$ is a sheaf in the fppf topology and a torsor under ${\operatorname{Isom}}(M_n, M_n)$.  Furthermore, there exists $n$ such that $I(\bar{k}) \neq 0$.

Last time we proved the Skolem-Noether theorem: The sequence of sheaves
$$
1 \rightarrow {\bf{G}}_m \rightarrow GL_n \rightarrow \underline{{\operatorname{Aut}}}(M_n) \rightarrow 1
$$
is exact in the fppf topology.  This sequence is actually exact in the Zariski topology.

In particular, we showed that if $R$ is a local ring, then all automorphisms of $M_n(R)$ arise as elements of $GL_n(R)$.  It is natural to ask if the same is true for all rings $R$.  We begin by showing this is not true.

Notation: We will denote $\underline{{\operatorname{Aut}}}(M_n)$ by $PGL_n$.

We can rephrase the claim above as follows: It is not always true that
$$
PGL_n(R) = \frac{GL_n(R)}{R^\times}
$$
That is, there exist rings $R$ for which the equality above does not hold.

For example, consider the following cartesian square:
$$
\require{AMScd} \begin{CD}
GL_n @>a>> {\bf{A}}^{n^2}\backslash\{0\} \\
@VbVV @VVcV \\
PGL_n @>>d> {\bf{P}}^{n^2 - 1} \\
\end{CD}
$$
$GL_n$ is the distinguished open of ${\bf{A}}^{n^2}$ defined by $\det$ and $PGL_n$ is defined as the nonvanvanishing of the homogeneous form $\overline{\det}$ and is therefore affine.  Let us write $PGL_n = {\operatorname{Spec}}A$.

Next, if we plug in ${\operatorname{Spec}}A$ to the exact sequence above it is easy to see surjectivity would imply that $Id_{PGL_n}$ is in the image of $GL_n({\operatorname{Spec}}A)$. In other words, surjectivity would imply there is a section of $b: GL_n \to PGL_n$. In the next paragraph we show this is impossible. 

Note that the map $c$ defines a ${\bf{G}}_m$-torsor on ${\bf{P}}^{n^2-1}$. Indeed, if one considers the geometric line bundle: $\pi: {\mathscr{Spec}}\mathbf{Sym}\mathcal{O}(1) \to \mathbf{P}^{n^2-1}$, and removes the zero section then they are left with the map $c$. Thus a section of $c$ would yield a nonvanishing section of $\pi$ but the sheaf of all sections of $\pi$ is $\mathcal{O}(-1)|{PGL_n}$. To finish the argument it suffices to understand why $\mathcal{O}(-1)|{PGL_n}$ has no nonvanishing global sections, or in other words, why it isn't the trivial bundle. This follows immediately from the exact sequence of class groups
$$
{\bf{Z}} \rightarrow Pic(\mathbf{P}^{n^2-1}) \rightarrow Pic(PGL_n) \rightarrow 0
$$
where the first map sends $1 \mapsto \mathcal{O}(n)$.

Now our aim is to show that a Central Simple Algebra $\mathcal{A}$ over $k$ is split over a separable field extension. We do this in three steps: first we define a functor parametrizing families of splittings, then we show this functor is representable by a smooth $k$-scheme, and finally we show that all smooth $k$-schemes have a point over ${\operatorname{Spec}}(k^{sep})$. Put $I: Sch_k \to Set$ to be $Y \mapsto {\operatorname{Isom}}(A|_Y, M_n(\mathcal{O}_Y))$. Now we make a few observations: $I$ is a sheaf of sets in the fppf topology. Moreover, it is a sheaf of ${\operatorname{Aut}}(M_n)=PGL_n$-sets that is locally trivial in the fppf topology. The first follows from the fact that $I$ is quasicoherent and last quarter we saw quasicoherent presheaves are sheaves in the fppf topology. The reason it is locally trivial is because there is a finite extension $l/k$ such that $A|_{{\operatorname{Spec}} (l)} \cong M_n(l)$ (we proved this last time), so $I({\operatorname{Spec}}(l))$ is noncanonically isomorphic to $PGL_n(l)$ as a $PGL_n(1)$-set (such an isomorphism depends on the choice of isomorphism $A|_{{\operatorname{Spec}} (l)} \cong M_n(l)$). 

What we have shown is that $I$ restricted to the subcategory $Sch_l$ is isomorphic to $PGL_n(l)$ a functor represented by a smooth affine scheme. Thus, by fppf descent for relatively affine schemes (Proposition 2.23 on pg. 19 in Milne's Etale Cohomology text) because there is a descent datum on $I|_{Sch/l}$ that respects the $l$-algebra structure on $PGL_n(l)(PGL_n(l))$ it follows that $I$ is represented by an affine scheme on $Sch/k$. That it is reprsented by a smooth scheme is also something we can check fppf locally (Proposition 1.15 in Vistoli's Grothendieck topologies notes).

Finally we need to show that smooth $k$-schemes have $k^{sep}$-points. We follow the stacks project and use the following fact: If $f: X \to Y$ is smooth of relative dimension $d$ then there are affine opens $ U \subset X$ and $V \subset Y$ with $f(U) \subset V$ and an etale morphism $\pi$ making the diagram commute
$$
\require{AMScd} \begin{CD}
X @<<open< U @>{\pi}>> {\bf{A}}^{d}_V \\
@V{f}VV @V{f|_{U}}VV @VV{pr_2}V\\
Y @<<open< V @= V \\
\end{CD}
$$
where $\pi$ is &eacute;tale. Now in our situation $V=Y= {\operatorname{Spec}}(k)$. The image of $\pi(U)$ is open because it is \'etale and hence must contain a $k$-point (because $k$-points are dense in affine $k$-space!). Call this point $x$ and choose $y \in U$ such that $\pi(y)=x$. Because $\pi$ is &eacute;tale we know that the field extension $k=k(x) \subset k(y)$ is finite and separable. In other words $U$ has a point over $k^{sep}$.

This result seemed heavy-handed and so I (Sid) asked in class if there were non-smooth morphisms over $k$ with no points over a separable closure. The answer is yes: consider ${\operatorname{Spec}}(k(x)) \rightarrow {\operatorname{Spec}}(k(x^p))$ where $k$ has characteristic $p$. This is not a smooth morphism because the Kahler differentials is nonzero. Moreover ${\operatorname{Spec}}(k(x))$ cannot have a point over the separable closure $k(x^p)^{sep}$. Indeed, if it did that would imply that the field extension $k(x^p) \subset k(x)$ was separable. 
