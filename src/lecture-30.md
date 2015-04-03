#The Brauer group is torsion

We can consider the two exact sequences 

$$ \require{AMScd} \begin{CD} 
1 @>>> \mu_n @>>> SL_n @>>> PGL_n @>>>1\\
@.      @VVV       @VVV     @|      @.\\
1 @>>> \mathbb{G}_m @>>> GL_n @>>> PGL_n @>>>1
\end{CD} $$

by taking cohomology we have the following commutative diagram

$$ \require{AMScd} \begin{CD} 
H^1(X, PGL_n) @>>> H^2(X,\mu_n)\\
@|                   @V\iota_nVV\\
H^1(X, PGL_n) @>>> H^2(X,\mathbb{G}_m)
\end{CD} $$

Now observe that $H^i(X,\mu_n)$ is $n$-torsion for every $i$, as multiplication by $n$ maps everything to the identity in $\mu_n$. This means that the class of every Azumaya algebra of degree $n$ gets mapped to an $n$-torsion element in $H^2(X,\mu_n)$, and hence to an  $n$-torsion element in $ H^2(X,\mathbb{G}_m)$.

Actually, one san see that $$ H^2(X,\mathbb{G}_m)_{tors} = \cup_n \text{Im}\iota_n $$

##A different trivialization experience
So far we have considered a trivialization of the form:
$$
H^1(X, PGL_n) \to H^2(X,\mathbb{G}_m)
$$
mapping the class of $A$ to the stack of pairs $(V, \phi)$.

Alternatively we can consider the map
$$
H^1(X, PGL_n) \to H^2(X,\mu_n)
$$
that sends $A$ to the triple $(V,\lambda, \phi)$, where $V$ is locally free of rank $n$, $\lambda: \bigwedge^n V \stackrel{\sim}{\to}\mathcal{O}$, $\phi: End(V) \to A$.
A map between two triples of the form $(V,\lambda, \phi)$ can be defined in a very similar fashion as in the previous case. This actually gives a CFG that we will denote by $\mathcal{X}^\tau_A$.

It's interesting to look at automorphisms of an object: an automorphism of $(V, \lambda, \phi)$ is an isomorphism $f:V\to V$ such that $ad(f) = id$ and $\bigwedge^n f = Id$, that is $f\in \mu_n$. Therefore there's a canonical identification $\text{Aut}(V, \lambda, \phi) \simeq \mu_n$. This implies that $\mathcal{X}^\tau_A \to X$ is a $\mu_n-gerbe$.

Observe that there's a canonical morphism of stacks over $X$
$$
c: \mathcal{X}^\tau_A \to \mathcal{X}^_A
$$
that induces the canonical inclusion $\mu_n \to \mathbb{G}_m$.

We also have the decomposition
$$
\text{QCoh}(\mathcal{X}^\tau_A) \simeq \bigoplus_{\chi} \text{QCoh}^{\chi}(\mathcal{X}^\tau_A)
$$
where the sum is over $\chi\in \mathbb{Z}/(n)$ and $\text{QCoh}^{\chi}(\mathcal{X}^\tau_A)$ are sheaves where the $\mu_n$-action is given after multiplication by $\chi$.

Also there are equivalence of categories
$$
c_*: \text{QCoh}^{i}(\mathcal{X}^\tau_A) \to \text{QCoh}^{i}(\mathcal{X}_A), c^*: \text{QCoh}^{i}(\mathcal{X}_A)\to\text{QCoh}^{i}(\mathcal{X}^\tau_A)
$$

What are the advantages of working with $\mu_n$?

Assume the order of $\mathcal{X}^\tau_A$ in $H^2(X, \mu_n)$ is $n$. It's an interesting exercise to prove that if $V$ is a locally free $\mathcal{X}^\tau_A$-twisted sheaf then $n$ divides the rank of $\mathcal{X}^\tau_A$.

We also have the following
<div class="theorem">
If $X$ is regular of dimension $\leq 2$, then $Br(X) \stackrel{\sim}{\to} H^2(X,\mathbb{G}_m)$ and the restriction map $Br(X)\to Br(k(X))$ is injective.
</div>