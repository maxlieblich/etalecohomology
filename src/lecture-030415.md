Recall we have two question:
\begin{enumerate}
  \item What are the quasicoherent sheaves on $BG$?
  \item What are sheaves on $\mathcal{X}_A$ with trivial stabalizer action?
\end{enumerate}

(1) Let $G$ be a group scheme over $S$.

Claim: Quasicoherent sheaves on $BG$ are equivalent to $Reps^{Qcoh}(G)$, the (right) $G$ equivarient quasicoherent sheaves on schemes over $S$. This equivalence is given by the functor that sends a quasicoherent sheaf $F$ to $F(S)$.

The idea we had last time was to use that $G$ is flat and finitely presented over $S$. Then we can use fppf descent. This left us with lots of questions about why it works. We will show the equivalence more directly here.

First we show that the functor described above is essentially surjective. Start with a quasicoherent sheaf $Q$ on $S$ with an action $Q \times G \to Q$. This is the same as a map $G \to Aut_{\mathcal{O}}(Q)$. This induces a map $H^1(T,G) \to H^1(T, Aut_{\mathcal{O}}(Q))$. In other words, given a $G$-torsor $V \to T$ we map to a sheaf $Q'_V$ on $T$ that is a form of $Q$. 

Our claim is that this an $F$ such that $F(S)\simeq Q$. There are a lot of things to check here, like is $F$ actually a functor, but we do not check it here. Two other important questions we might ask are why is $F$ quasicoherent and why does this give us the correct $G$ action.

One could ask if this equivalence descends to an equivalence between coherent sheaves on $BG$ and finite dimensional representations of $G$. The notion of coherent is perhaps not the correct notion and instead we should consider quasicoherent sheaves of finite presentation. Then since the correspondence $F \mapsto f(S)$ is fully faithful the answer will be yes.

(1.5) Before moving on to our second goal we first consider quasicoherent sheaves on $BG$ with trivial action. From the above discussion any quasicoherent sheaf corresponds to something with an action. Let $Qcoh^0(BG)$ be the collection of quasicoherent sheaves $F$ such that $F(S) \times G \to F(S)$ is given by the trivial action.

Claim: $Qcoh^0(BG) \simeq Qcoh(S)$. More precisly if $\pi: BG \to S$ then the desired isomorphism is given by $\pi^* \pi_* \to id$. We saw that $F$ comes from $F(S)$ by twisting via $G \to Aut_{\mathcal{O}}(F(S))$.Given a map $T \to BG$ we have a torsor $V \to T \to S$ with $p: V \to S$. Then we get $F(T) \simeq p^*F(S)$ by twisting by the cocycle giving $V$. Because the action is trivial it doesn't matter what the map $V \to T$ is so $F \simeq \pi^*F(S)$.

How do we compute $\pi_*$. Claim: Let $\pi: BG \to S$ and $F \in Qcoh(BG)$, then $\pi_* F \simeq F(S)^G$. We will use Yoneda's lemma and adjointness. Let $Q$ be any quasicoherent sheaf on $S$ and consider
\[
  Hom_S(Q, \pi_* F) = Hom_{BG}(\pi^*Q,F) = Hom_{Reps^{Qcoh}(G)}(Q(S),F(S)) = Hom_S(Q,F(S)^G)
\]

(2) We now address our final question. $\mathcal{X}_A$ is almost $B \mathbf{G}_m$. In laymans terms, choose a covering $U \to S$ such that $\mathcal{A}|_U \simeq End(V)$. This gives us $\mathcal{X}_A|_U \simeq B \mathbf{G}_{m,U}$.

Mission: show that quasicoherent sheaves on $\mathcal{X}_A$ with trivial action are precisly the pullbacks from $S$.