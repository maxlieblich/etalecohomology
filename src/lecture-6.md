# Cohomology of sheaves, Cech-to-sheaf spectral sequence

Fix a site $C$ and an object $U \in C$. For any covering $\{U_i \rightarrow U\}$, consider the composition of the forgetful functor $\Phi : \Sh(C) \rightarrow \PreSh(C)$ and the functor $H^0(\{U_i \rightarrow U \}, -) : \PreSh(C) \rightarrow \Ab$.

For any sheaf F, the composition gives (by the lemma in the previus section) $\lim (\prod F(U_i) \rightrightarrows \prod \prod F(U_i \times_U U_j))$, but by the definition of a sheaf this is $F(U)$, so the composition is just $\Gamma(U, -)$.

Then since any injective sheaf is an injective presheaf, the Grothendieck spectral sequence of these functors computes sheaf cohomology

<div class="theorem">
There is a spectral sequence
$$ E_2^{pq} = H^p(\{U_i \rightarrow U\}, R^q \Phi(F)) \Rightarrow H^{p+q}(U,F)$$
</div>
**Proof.** This is just the Grothendieck spectral sequence applied as described above and using the derived functor interpretation of Cech cohomology as in the previous section. QED

We can do the same thing with $\check{H}$, too.

<div class="theorem">
There is a spectral sequence
$$ E_2^{pq} = \check{H}^p(U, R^q \Phi(F)) \Rightarrow H^{p+q}(U,F)$$
</div>

Of course, these are only useful if we have some idea what $R^q \Phi(F)$ is:

<div class="lemma">
For any sheaf $F$, $R^q \Phi(F)(V)$ = H^q(V,F)$.
</div>
**Proof.** Note that $H^q(-,F)$ is indeed a presheaf, call this $\mathscr{H}^q(F)$. Then $\mathscr{H}^q$ is a $\delta$-functor as it has the appropriate long exact sequence from the same on $H$, and it is effacable as it is zero for $q > 0$ on any injective sheaf. Since $\mathscr{H}^0 = \Phi$, we are done. QED


