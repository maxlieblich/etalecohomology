# Floppy Isom is Not a Scheme 

Given a scheme $X$ and an Azumaya algebra $A$ on $X$, we've defined $I_A$ to be the stack of trivializations of $A$, i.e. $I_A (T) = \{ V, \phi: End(V) \to A_T \}$ such that $V$ is locally free on $T$ and $\phi$ is an isomorphism of algebras.  This is a $\mathbf{G}_m$ gerbe, and we can ask ourselves: why is it not a scheme?  

### Clarifying the question

Last quarter we showed that we can consider any $X \in Sch_S $ as a sheaf in the fppf site, and any sheaf has an associated stack: given $F \in Sh(S)$, $F$ is a functor (so a psuedofunctor) from $S^{op}$ to $Set$, and any set is canonically a discrete groupoid (a groupoid with no non-identity arrows).  In this setting, descent theory is equivalent to the sheaf condition, so descent theory is effective, so $F$ is a stack. 
Therefore, for any scheme, we can associate a sheaf to which we can associate a stack.  So, when we ask, "why is $I_A$ not a scheme?", we're really asking, "why is $I_A$ not isomorphic to a stack associated to a sheaf associated to a scheme?" 
But, we could actually skip the scheme part and ask an intermediate question: "Why is $I_A$ not isomorphic to a stack associated to a sheaf?"  
Note that when we discuss isomorphisms of stacks, we mean 1-isomorphisms.  A morphism of stacks on $S$ is a morphism of categories fibered in groupoids over $S$, and a 1-isomorphism is an equivalence of categories.  

### Answering the Question

<div class="proposition">
A stack $\mathcal{X}$ on $S$ is 1-isomorphic to the stack associated to a sheaf of sets if and only if
(1) the fiber categories $\mathcal{X}(T)$ are essentially small and
(2) any $x \in \mathcal{X}(T)$ satisfies $Aut(x) = \{id\}$.  
</div>
**Proof** An isomorphism $F$ to $\mathcal{X}$ would induce equivalences of fiber categories $F(T) \cong \mathcal{X}(T)$, but the automorphisms of any object in $F(T)$ are $\{id\}$ because $F(T)$ is discrete.  
Conversely, if these two conditions are satisfied, descent theory is equivalent ot the sheaf condition for objects. QED

Now, to show $I_A$ is not a sheaf, we observe that for any $T \in Sch_S$, the automorphism group of any object in $I_A(T)$ is $\mathbf{G}_m$, which is not $\{id\}$, hence $I_A$ is not a sheaf.   

We could also ask ourselves: is $I_A(T)$ essentially small?  The answer here is yes; the category of finitely generated modules over a ring $R$ is essentially small, which implies the category of finitely generated quasicoherent sheaves on $T$ is essentially small, which implies the category of locally free sheaves is essentiall small, which implies $I_A(T)$ is essentially small.  