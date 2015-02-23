# Quotient stacks

Let $C$ be site (with a final object). Let $X$ be a sheaf on $C$ on which $G$ (a sheaf of groups on $C$) acts. 

### X/G

We have a category fibered in groupoids $p: X/G \rightarrow C$ (which we denote by $[X/G]$) as follows. The objects of X/G are $(T,F)$ where $T$ is an object in $C$ and $F$ fits in the following commutative diagram 

$$
\require{AMScd} \begin{CD}
F @>{G-equivariant}>> X \\
 @V{G-torsor}VV \\
 T \\
\end{CD}
$$

Morphisms between two objects $(T,F) \rightarrow (T',F')$ should fit in the following commutative diagram

$$
\require{AMScd} \begin{CD}
X @>{Identity}>> X \\
@A{G-equivariant}AA  @A{G-equivariant}AA\\
F @>{G-equivariant}>>  F' \\
 @V{G-torsor}VV  @V{G-torsor}VV\\
 T @>>> T' \\
\end{CD}
$$

The functor $p$ should take $(F,T)$ to $T$. The meta claim is that this is the right way to model quotients. As a subexample, let $S$ be a scheme and let $C=Sch_S$, the category of schemes over $S$. Let $X=S$ have the trivial action of $G$. Then, $[S/G] = BG$..

Claim : $[X/G]$ is a stack.  I don't understand the proof of the claim. But apparently this follows because amongst the numerous things that we have to check, we check that descent is effective. 

1. Descent being effective is true for sheaves.
2. Descent being effective is true for arrows observing that $Hom(\star,\star)$ is a sheaf.
3. Descent is effective for $Func(I,Sh)$ where $I$ is any category.

### Examples of non-effective descent 

1. See Section 6 in the book  [Algebraic Stacks by Kai Behrend, Brian Conrad, Dan Edidin, William Fulton, Barbara Fantechi, Lothar Göttsche and Andrew Kresch](http://www.math.uzh.ch/index.php?file&key1=5171).
2. Section 6.7 in Bosch-Lutkebohmert-Raynaud.

#### Weighted projective space

Let $X=A^{n+1} / \{0\}$ and $G=\G_m$. $We fix integers $g_0,\ldots,g_n \in \Z$.  Let's take the base scheme to be $spec(k)$, where $k$ is algebraically closed. We note that $\Hom(\G_m,\G_m)=\Z$. We can describe an action of $\G_m$ on $A^{n+1} / \{0\}$ as follows.
$$
t cdot(a_0,\ldots,a_n) = (t^{g_0}a_0, \ldots t^{g_n} a_n).
$$
for every $t \in \G_m$. If all the $g_i$'s are $\pm 1$, we are in the classical situation and we get $A^{n+1} /\{ 0\} / \G_m = P^{n}$.

We calculate the Automorphisms of objects of $[A^{n+1} / \{0\}/\G_m](k)$. WLOG, we can assume the object $T=\G_m$ as a left $\G_m$-torsor (using Hilbert's theorem 90). 

$$
\require{AMScd} \begin{CD}
1 @>>> x \\
\\
G_m @>{G-equivariant}>>  X  \\
 @V{G-torsor}VV \\
 Spec(k) \\
\end{CD}
$$

For $x,y \in X(k)$,  $Hom(x,y) =\{\alpha \in \G_m \ | \ \alpha \cdot x = y\}$ and we get that 
$$ Aut([0 : \ldots : 1 : \ldots: 0]) = \mu_{g_i}$$ as sheaves whcih is non-trivial if $g_i$ is not equal to $\pm 1$.

Another meta point : As a space, the weighted projective space could have quotient singularities. As a stack, weighted projective stack is smooth.
