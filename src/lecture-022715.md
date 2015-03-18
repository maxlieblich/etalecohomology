First we will discuss a fun example.  Consider $L/k$ a separable field extension of degree $n$.  Recall that $L\otimes_kk^{\mbox{sep}}\cong(k^{\mbox{sep}})^n$.  This means that $L$ is an \’{e}tale form of $k^n$.  Because $S_n=\mbox{Aut}_kk^n$, this means that $L$ is classified by an element of $H^1(\mbox{Spec},S_n)=\mbox{Isom}_k(L,k^n)$.  Thus, the sheaf
$$\mbox{Aut}_{L/k}:\mbox{Sch_k}^{\mbox{op}}\rightarrow\mbox{Grp}$$
given by $x\mapsto\mbox{Aut}_X(X\otimes_kL)$ is an \’{e}tale form of the sheaf $\mbox{Aut}_{k^n/k}\cong\underline{S_n}$.  So, $\mbox{Aut}_{L/k}$ is an inner form of $S_n$, and its global sections are given by $\mbox{Aut}_{L/k}(\mbox{Spec}(k))=\mbox{Aut}_k(L)$.  

Now lets resume talking about quasi-coherent sheaves on $BG$.  (I think this is better handled by the next person).  

# Sheaves on Stacks

Let $\pi:X\rightarrow S$ be a stack on $S$.  Last time, we defined the site associated to $X$ to be the category $X$, equiped with the topology whose given by

$$\{y_i\rightarrow x\}\in \mbox{Cov}(X)\Leftrightarrow\{\pi(y_i)\rightarrow\pi(x)\}\in\mbox{Cov}(S)$$

A sheaf on the stack $X$ is a a sheaf on the site associated to $X$.  Here is a useful example of a sheaf of groups on $X$:


<div class="example">
For $x\in X$, define $I(x)$ to be the automorphism group of $x$.  That is, $I(x)$ is the group of arrows $\psi:x\rightarrow x$ in the category $X$ such that $\pi(\psi)=\mbox{id}$.  

We will show that this is a sheaf.  First we need to see that it is a presheaf.  Suppose we have an arrow $y\rightarrow x$ in $X$.  Take a morphism $x\in\mbox{Aut}(x)$.  Because every arrow is cartesian, there exists a unique map $\beta:y\rightarrow y$ that fits into the diagram

$$\require{AMScd} \begin{CD} y @>>> x\\ @VVV @VVV \\ y @>>> x\end{CD}$$

Because of the uniqueness of $\beta$, this is functorial.

Next, we check that this is a sheaf.  This is immediate by applying the stack condition to $\mbox{Isom}(x,y)$.
</div>


We call this sheaf the inertia sheaf (or inertia stack) of $X$.  Here is an important fact about it:

<div class="proposition">
Suppose we have a stack $X$, and write $I$ for its inertia sheaf.  For any sheaf $F$ on $X$, there is a canonical right action $F\times I\rightarrow F$, called the inertial action.
</div>

<div class="proof">
We have $I(x)=\mbox{Aut}(x)$.  So, we need a map 
$$F(x)\times\mbox{Aut}(x)\rightarrow F(x)$$.
$F$ is a functor, so if we have an automorphism $\alpha:x\rightarrow x$, we get a map $\alpha^*:F(x)\rightarrow F(x)$.  Furthermore, if we have
$$x\rightarrow x\rightarrow x$$
where the first map is $\alpha$ and the second $\beta$, we see that $\alpha^*\beta^*=(\beta\alpha)^*$.  This is a left action of the opposite group of $\mbox{Aut}(x)$, which is the same thing as a right action of $\mbox{Aut}(x)$.
</div>

Lets return to our isom sheaf example.  Let $X$ be a scheme, and $A$ an Azumaya algebra on $X$.  Recall the definition of $\mathcal{X}_A$.  What is the inertia sheaf of $\mathcal{X}_A$?  Take $(v,\varphi)$ in $\mathcal{X}_A$.  An automorphism of this element is a map $\psi:v\rightarrow v$, such that the map $\mbox{ad}(\psi):\mbox{End}(v)\rightarrow\mbox{End}(v)$ is compatible with the maps $\varphi$ to $A$.  By Skolem noether, we see that $\varphi\in\mathbb{G}_m(T)$.  What this shows is that
$$I=\mathbb{G}_{m,\mathcal{X}_A}$$,
where
$$\mathbb{G}_{m,\mathcal{X}_A}((v,\varphi))=\mathcal{O}(T)^\times$$.


