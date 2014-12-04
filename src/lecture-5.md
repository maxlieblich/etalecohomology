# Cech cohomology of presheaves

Fix a site $C$, and an object $U \in C$. Then for any presheaf $F \in \PreSh(C)$ and covering $\{U_i \rightarrow U\}$, we can define the Cech complex $C(\{U_i \rightarrow U\}, F)$

$$ F(U) \rightarrow \prod F(U_i) \rightarrow \prod \prod F(U_i \times_U U_j) \rightarrow \cdots,$$

with differentials $d(s)_{i_0, \dots, \i_{p+1}} = \sum_{j = 0}^{p+1} s_{i_0, \dots, \hat{i}_j, \dots, s_{p+1}} |_{U_{i_0} \times_U \cdots \times_U U_{i_{p+1}}}$, restricting via the projection map.

Since this is a complex we can compute its cohomology $H^i(\{U_i \rightarrow U \}, F) = h^i(C(\{U_i \rightarrow U\}, F))$.

<div class="lemma">
$H^0(\{U_i \rightarrow U\}, F) = \lim (\prod F(U_i) \rightrightarrows \prod \prod F(U_i \times_U U_j))$ and furthermore, $R^p H^0(\{U_i \rightarrow U\}, -) = H^p(\{U_i \rightarrow U\},-)$.
</div>
**Proof.** The first statement is a careful interpretation of the definition of H^0 as the 0th cohomology of the Cech complex: the kernal of the first map is exactly the equalizer of the given diagram.

For the next, we can prove $H^p(\{U_i \rightarrow U\},-)$ is an effacable $\delta$-functor (see Hartshorne III.1). This is done for us here: http://stacks.math.columbia.edu/tag/03AU
QED.


The formation of $C(\{U_i \rightarrow U\}, F)$ is functorial in both the covering and $F$, so we can define a functor

$$\check{H}^i(U,F) = \colim_{\Cov_U} H^i(\{U_i \rightarrow U \}, F)$$
