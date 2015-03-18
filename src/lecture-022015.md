# Sheaves on stacks

Let $\pi: X \to S$ be a stack. We want to talk about sheaves on $X$, and in order to do that, we will define a site associated to the stack $X$. It makes sense to use the site structure on $S$: we declare $\{y_i \to x\}$ to be a covering on $X$ if $\{\pi(y_i)\to\pi(x)\}$ is a covering in $S$.

<div class="example">
One can build a sheaf of groups on every stack, by considering the functor
$$
x\mapsto Aut(x)
$$
where $Aut(x)$ is the group of automorphisms of $x$ in the fibered category, i.e. the isomorphisms $\psi:x\to x$ such that $\pi(\psi) = Id$.

We claim that it is a sheaf. The functoriality follows from the CFG properties. If $f:y\to x$ is a map in $X$ and $\alpha\in Aut(x)$, then teh fact that every arrow is Cartesian implies the existence of an isomorphism of $y$ making every appropriate square commute.
Moreover, the stack conditions ensure that $Iso(x,y)$ is a sheaf, so $Iso(x,x)$ is a sheaf.
</div>

<div class="example">
Let $A$ be an Azumaya algebra on a scheme $X$. We defined $\mathcal{X}_A$ the stack of pairs $(U, \phi: \mathcal{E}nd U \simeq A)$. One can check that
$$
(U, \phi) \mapsto \Gamma(T, U)
$$
is a sheaf on $\mathcal{X}_A$, that we will call $\mathcal{V}$.
</div>

### The inertia action

<div class="proposition">
Given a stack $X$, let $I$ be the sheaf of the automorphism groups. For any sheaf of sets $F$ on $X$, there's a canonical right action $F\times I \to F$, called the \emph{inertial action}.
</div>

**Proof**: We know that $I(x) = Aut(x)$, so we will describe an action $F(x)\times I(x) \to F(x)$. Given an automorphism $\alpha:x\to x$, then $F(\alpha): F(X) \to F(x)$ is an automorphism of sets. We can then define $\alpha\cdot y = F(\alpha)[y]$ for all $y\in F(x)$. This yields a right action.

What is $I$ for our beloved stack $\mathcal{X}_A$?

The question is really about the automorphisms of a pair $(V,\phi)$. By our definition of $\mathcal{X}_A$, it's an isomorphism $\psi: V\to V$ such that $\phi\circ \text{Ad}(\psi) = \phi$, where $\text{Ad}(\psi): \mathcal{E}nd V \to \mathcal{E}nd V$. Since $\phi$ is an automorphism, then $\text{Ad}(\psi) = \text{Id}$, hence by the Skolem-Noether theorem $\psi\in\mathbb{G}_m$.

Putting everything together, there's an action $\mathcal{V} \times \mathbb{G}_m \to \mathcal{V}$, that gives rises to a sheaf of representations of $\mathbb{G}_m$. As it turns out, their structure is known:

<div class="proposition">
Let $X$ ve a scheme and let $\mathcal{F}$ be a quasi-coherent sheaf on $X$ in the fppf topology. Given an action $\mathbb{G}_m \times \mathcal{F} \to \mathcal{F}$, there is a decomposition $\mathcal{F} = \bigoplus_i \mathcal{F}_i$ into eigensheaves such that the restriction of the action to $\mathcal{F}_i$ is of the form
$$
\mathbb{G}_m \times \mathcal{F}_i \to \mathcal{F}_i, (\alpha, f)\mapsto \alpha^i f
$$
</div>

Question: what are the eigensheaves for our action $\mathcal{V} \times \mathbb{G}_m \to \mathcal{V}$?