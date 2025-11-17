Exercise 5.2.20 Let $V$ be a vector space over an infinite field $F$. Show that $V$ cannot be the set-theoretic union of a finite number of proper subspaces of $V$.
Proof.
Assume that $V$ can be written as the set-theoretic union of $n$ proper subspaces $U_1, U_2, \ldots, U_n$. Without loss of generality, we may assume that no $U_i$ is contained in the union of other subspaces.

Let $u \in U_i$ but $u \notin \bigcup_{j \neq i} U_j$ and $v \notin U_i$. Then, we have $(v + Fu) \cap U_i = \varnothing$, and $(v + Fu) \cap U_j$ for $j \neq i$ contains at most one vector, since otherwise $U_j$ would contain $u$.

Therefore, we have $|v + Fu| \leq |F| \leq n-1$. However, since $n$ is a finite natural number, this contradicts the fact that the field $F$ is finite.

Thus, our assumption that $V$ can be written as the set-theoretic union of proper subspaces is wrong, and the claim is proven.
Qed.