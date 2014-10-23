# Sheafification and exact sequences

Fix a Grothendieck topology on a category $C$.

### Sheaves are presheaves, but not the other way around

Let's just think about sheaves and presheaves of sets for now.

Any sheaf is a presheaf: we just forget the sheaf condition. This gives us a fully faithful functor $$\Phi:\Sh(C)\to\PreSh(C).$$

Not every presheaf is a sheaf. What are some examples? Can you think of any "organic" examples?

<div class="theorem">
There is a left adjoint to $\Phi$, that is, a functor $$F\mapsto F^s:\PreSh(C)\to\Sh(C)$$ such that for all presheaves $F$ and sheaves $G$ we have a functorial isomorphism $$\Hom(F, \Phi(G))=\Hom(F^s,G).$$
</div>
This functor is called *sheafification*.

**Idea of Proof**. The proof is somewhat messy, so I have chosen not to present it in class. What is the idea? Given $F$ define a new presheaf $F^+$ like this: 

- for an object $U\in C$, let $\Cov(U)$ be the category of coverings $\{U_i\to U\}_{i\in I}$. A map from $\{U_i\to U\}_I$ to $\{U'_j\to U\}_J$ is a map $\iota:I\to J$ and maps $U_i\to U'_{\iota(i)}$ over $U$.
- for any object $c=\{U_i\to U\}\in\Cov(U)$, we can form a diagram $$d(c):\prod F(U_i)\rightrightarrows\prod F(U_i\times_U U_j)\cdots,$$ and these diagrams are functorial in $\Cov(U)$. Each diagram gives us a new set $\lim d(c)$, that is functorial in $c$.
- Define $F^+(U)=\colim d(c)$.
- DO THIS AGAIN to get $F^s(U)=F^{++}(U)$.
- Check (it hurts) that the result is in fact a sheaf.

Now, since $G^+$ is *canonically* isomorphic to $G$ for any sheaf $G$, it is straightforward to show that the resulting map $F\to F^s$ is universal for maps to sheaves. QED

<div class="exercise">
(Possibly hard?) Find an example of a sheaf on the big Zariski site of $X$ that is not a sheaf in the etale topology and whose sheafification is trivial (i.e., the sheaf of singletons).
</div>

#### An example of a sheaf/non-sheaf

Here's somewhat quirky example of a sheaf in the big Zariski topology on $X$ that is not a sheaf in the etale topology. Feel free to make more! This one fits in with the theme we used to launch the course: $\Z/2\Z$-torsors.

Fix a scheme $X$. Define a sheaf $T$ on $X_{\ZAR}$ as follows.

- First, let's make a silly presheaf. Let $\widebar{T}(Y)$ be the set of isomorphism classes of $\Z/2\Z$-torsors, that is, of finite etale morphisms $Z\to Y$ together with a $\Z/2\Z$-action $\Z/2\Z\times Z\to Z$ over $Y$ that acts simply transitively on the fiber over any geometric point of $Y$.
- We let $T$ be the sheafification in the Zariski topology of $\widebar{T}$.
- Here's a weird remark: the restriction of $\widebar{T}$ to any regular scheme $Y$ over $X$ is actually already a Zariski sheaf. Proof: two $\Z/2\Z$-torsors $Z\to Y$ and $Z\to Y$ are isomorphic if and only if the are isomorphic over the generic point of $Y$; even better, isomorphisms extend uniquely from generic fibers. This shows that if a torsor extends, it extends uniquely up to unique isomorphism. Thus, the isomorphism classes are actually a sheaf.
- Also, note that there is *always* some $X$-scheme $Y\to X$ such that $T(Y)$ is not a singleton. (Why?!)

What happens if we sheafify $T$ in the *etale* topology? Well, by definition, any torsor is locally *trivial* in the etale topology, so the sheafification must be the sheaf of singletons! Voila!

#### Quasi-coherent sheaves: all good

Let $C$ be the fppf site of a scheme $X$. Given a quasi-coherent sheaf $M$ of $\ms{O}_X$-modules, we can define a functor $\underline{M}:\Sch_X\to\Set$ by sending $g:T\to X$ to $\Gamma(T, g^\ast M).$

<div class="theorem">
For any quasi-coherent sheaf $M$ on $X$, the presheaf $\underline{M}$ is a sheaf in the fppf topology.
</div>
**Proof**. Do you remember how this went with $\ms{O}$? Can we use the same trick? QED

### Morphisms of topologies

Now that we have our categorical analogue of topological spaces, how do we simulate continuous maps? For psychological reasons, given a category $C$ with a Grothendieck topology, we will write $\Site(C)$ to denote the "site of $C$". You'll see why we do this in a moment.

<div class="definition">
Given categories $C$ and $C'$ with Grothendieck topologies, a *morphism of sites* $$f:\Site(C')\to\Site(C)$$ is a functor $F:C\to C'$ such that

- for every covering $\{U_i\to U\}$ in $C$, the image $\{F(U_i)\to F(U)\}$ is a covering
- for every covering $\{U_i\to U\}$ in $C$ and every morphism $V\to U$ in $C$, the canonical map $$F(U_i\times_U V)\to F(U_i)\times_{F(U)} F(V).$$ (Special case of this condition: $C$ and $C'$ have fiber products and $F$ preserves them. This is equilavent to $F$ preserving finite limits, also sometimes called "continuous" -- now you know why!)
</div>

Everybody's favorite example: $C=\Open(X)$, $C'=\Open(Y)$, $F$ is the pullback map induced from a continuous map $Y\to X$. We will thus usually write $f^{-1}$ for the above $F$ to simulate this. Other examples: if $X\to Y$ is a morphism of schemes, we get morphisms of sites $X_{\ET}\to Y_{\ET}$, $X_{et}\to Y_{et}$ and $X_{fppf}\to Y_{fppf}$, where the subscripts indicate the relevant sites for the associated schemes. The associated $f^{-1}$ functor is given by pullback of schemes.

<div class="question">
Does a continuous map of topological spaces induce a morphism of *big* topologies? Does a morphism of big topologies always come from a continuous map of topological spaces?
</div>

#### Associated functors for presheaves and sheaves

Suppose $f:\Site(C')\to \Site(C)$ is a morphism of sites. We can define a functor $$f_\ast:\PreSh(C')\to\PreSh(C)$$ by $$f_\ast(F)(c) = F(f^{-1}(c)).$$ This looks just like the pushforward you are used to!

<div class="proposition">
The functor $f_\ast$ 
- has a left adjoint (that we will call $f^{-1}$; see below for the justification), and
- preserves the subcategories of sheaves.
</div>
**Proof**. For the first statement: given a presheaf $F$ on $C$, define $$f^{-1}(F)(d)=\colim F(c),$$ the colimit taken over all pairs $(c, \phi)$ with $c\in C$ and $\phi:d\to f^{-1}(c)$ an arrow in $C'$. This becomes a formal experience after this; it should look familiar -- you read exactly this in Hartshorne! For the second statement, we use the fact that $f^{-1}$ carries coverings to coverings and fiber products to fiber products, by assumption. It thus transforms the sheaf condition into the sheaf condition. QED

<div class="corollary">
The functor $f_\ast:\Sh(C')\to\Sh(C)$ admits a left adjoint $f^{-1}$.
</div>
**Proof**. This works: $$f^{-1}(F) = f^{-1}(\Phi(F))^s.$$QED

*Justification for the use of $f^{-1}$ all over when we are already using it for the "pullback map on opens"*: we claim that for any $d\in C$ we have $$f^{-1}h_d=h_{f^{-1}(d)}.$$ Here's the proof.
$$\Hom_{\PreSh(C')}(f^{-1}h_d, F)=\Hom_{\PreSh(C)}(h_d, f_\ast F)=f_\ast F(d)=F(f^{-1}(d))=\Hom_{\PreSh(C')}(f^{-1}d, F).$$ (Is this still ok for sheaves? What do you think?)

Properties of $f^{-1}:\Sh(C)\to\Sh(C')$:

- $f^{-1}$ preserves all colimits
- $f^{-1}$ preserves finite limits

The first follows from the adjointness of $f^{-1}$ and $f_\ast$. The second is equivalent to preserving fiber products: $$f^{-1}(F\times_G H)=f^{-1}F\times_{f^{-1}G}f^{-1}H.$$ This reduces to checking the presheaf version, which itself reduces to $(F\times_G H)(c)=F(c)\times_{G(c)}H(c)$ by the filtering property of the corresponding colimit. The last is a consequence of the basic fact that $\Hom(h_c, F)=F(c)$ for all presheaves $F$ and objects $c$.

#### An example of pullback

Let $C$ be the small etale site of a scheme $X$ and $C'$ the small etale site of a separably closed point $x$ that admits a map $\iota:x\to X$. There is a morphism of sites $\iota:x_{et}\to X_{et}$ as usual; moreover, the site $x_{et}$ is equivalent to sets, since there are no non-trivial separable extensions of a separably closed field. What is $\iota^{-1}\ms{O}_X$?

Well, we're supposed to sheafify a certain functor, which we can explicitly calculate: we take the direct limit of $\ms{O}_U(U)$ over the system of lifts $x\to U\to X$ with $U\to X$ an etale morphism. Since any object in $C'$ is a disjoint union of copies of $x$, the sheaf condition just tells us that this computation for $x$ gives us the right thing.

**Upshot**: $\iota^{-1}\ms{O}_X = \colim_{x\to U\to X}\ms{O}_{U}(U)$. In ring-theoretic terms, if we fix an affine neighborhood of the image of $x$ and do the natural localization, we have a local ring $A$ with a choice of embedding $A/\mf{m}\to K$ into a separably closed field, and the sheaf $\iota^{-1}\ms{O}_X$ is the sheaf associated to the ring given by taking the direct limit over all diagrams $A\to B\to K$ where $A\to B$ is an etale ring extension and $B\to K$ factors $A/\mf{m}\to K$.

In particular, the colimit is itself a *local ring* with separably closed residue field, called the *strict Henselization of $A$*. The strict Henselization of a local ring is the local ring at a geometric point in the etale topology.

<div class="question">
What if we take a point $x\in X$ above, not a geometric point. Then the site $x_{et}$ is more interesting -- it involves the Galois group of $\kappa(x)$. What is the sheaf $\iota^{-1}\ms{O}_X$?
</div>

### Exact sequences

Let's now consider presheaves and sheaves on $C$ with values in abelian groups. We will call these $\PreSh^{\ab}(C)$ and $\Sh^{\ab}(C)$.

<div class="lemma">
A sequence $0\to F\to G\to H\to 0$ in $\PreSh^{\ab}(C)$ is exact if and only if the sequence is exact when evaluated on any object of $C$. Moreover, $\PreSh^{\ab}(C)$ is an abelian category satisfying AB3, AB4, AB5, AB3*, AB4*, AB5*, and, if $C$ is small, possessing a set of generators. (More generally, presheaves taking values in an abelian category inherit the axioms of that category.)
</div>
**Proof**: The abelian category axioms follow by evaluating everything termwise. The last one is the most interesting. Given an object $c\in C$, define a presheaf of abelian groups $Z_c:C^\circ\to\Set$ by $Z_c(c')=\Z$ if $c'$ is isomorphic to $C$ and $Z_c(c')=0$ otherwise. The maps between values are given by the identity between copies of $\Z$ and the $0$ map otherwise. We claim that the $Z_c$ generate the category $\PreSh^{\ab}(C)$, that is, for any $F\in\PreSh^{\ab}(C)$, the natural map $$\oplus_{c}\Hom(Z_c, F)\times Z_c\to F$$ is surjective. To see this, it suffices to show that for any section $s\in F(c)$, there is a map $Z_c\to F$ such that $Z_c(c)(1) = s$. But we can make this happen by just making this happen. (Be careful with isomorphisms!) QED 

<div class="corollary">
If $C$ is small (do I really need this?) then $\PreSh^{\ab}(C)$ contains enough injectives. Moreover, if $F$ is an injective presheaf then for any $c\in C$, the group $F(c)$ is injective (i.e., divisible).
</div>
**Proof**: Let $c\in C$ be an object. The singleton category $S$ admits a functor $S\to C$ that sends the single object $s$ to $c$, and this gives a morphism of sites $\sigma_c:\Site(C)\to\Site(S)$ such that for all $F\in\PreSh(C)$ we have $(\sigma_c)_\ast F(s) = F(c)$. Moreover, we know that we can calculate the left adjoint $\sigma_c^{-1}$ on $d$ by the formula $$\sigma_c^{-1}(G)(d) = \colim_{d\to c} F(d).$$ Since this is a filtering colimit of abelian groups, we see that $\sigma_c^{-1}$ is exact. But any functor with an exact left adjoint must send injectives to injectives. QED

It gets better!

<div class="prop">
The category $\Sh^{\ab}(C)$ is an abelian category that admits sufficiently many injectives and that satisfies AB3* (arbitrary products exist), AB5 (coproducts exist and filtered colimits are exact). 
</div>
**Proof**: (See Chapter II of Artin.) Given a map $f:F\to G$ of sheaves, the presheaf kernel $K\to F$ is a sheaf, and is the kernel (equalizer of the map and $0$) in the category of sheaves. On the other hand, we claim that the sheafification of the presheaf cokernel of $f$ is a sheaf cokernel. Indeed, write $F\to G\to KK$ in $\PreSh^{\ab}(C)$. What do we need to check to see that $KK^s$ is the sheaf cokernel? We need to know that for any sheaf $Q$, the map 
$$0\to\Hom(KK^s, Q)\to\Hom(G, Q)\to\Hom(F, Q)$$
is exact. But, by adjunction, this sequence is isomorphic to 
$$0\to\Hom(KK, \Phi(Q))\to\Hom(G, \Phi(Q))\to\Hom(F,\Phi(Q)),$$
which is exact by the definition of $K$. The last thing to check is that the sheaf cokernel of $K\to F$ equals the sheaf kernel of $G\to KK$ by the natural map. Letting $I$ be the *presheaf* cokernel of $K\to F$, we know that $$0\to I\to G\to KK$$ is exact. On the other hand, the composition of the sheafification functor and the forgetful functor is left exact (from $\PreSh^{\ab}(C)$ to itself), so $I^s$ is the also the sheaf kernel of $G\to KK^{s}$. 

What about the injectives? Well, sheafifying the $Z_c$ gives generators!

The AB axioms are explained on p. 32 of Artin's notes. It is pretty straightforward.
QED

<div class="lemma">
Sheafification $F\mapsto F^s$ defines an *exact* functor $$\PreSh^{\ab}(C)\to\Sh^{\ab}(C).$$
</div>
**Proof**. Why is it left exact? One version: the *construction* in terms of limits shows that it is left exact because limits of abelian groups preserve injections. It remains to show that an epimorphism $F\to G$ maps to an epimorphism $F^s\to G^s$. But the epimorphism condition is detected by exactness of mapping into something, so we can use the universal property. QED

<div class="corollary">
Any injective sheaf is injective as a presheaf. In particular, its restriction to any object is an injective object.
</div>
**Proof**. Any functor with an exact left adjoint preserves injectives! QED

#### Bonkers question

So the functor $$\Phi:\Sh^{\ab}(C)\to\PreSh^{\ab}(C)$$ is left exact, and $\Sh^{\ab}(C)$ has enough injectives. Can we make derived functors of $\Phi$? What are they?

### Equivalences of sites

A morphism $f:\Site(C')\to\Site(C)$ of topologies is a *topological equivalence* if the associated functor $f_\ast:\Sh(C')\to\Sh(C)$ is an equivalence of categories. This is very different from the corresponding statement for presheaf categories.

### Content contributors
@maxlieblich