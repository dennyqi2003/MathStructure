Exercise 3.7.2 Let $V$ be a vector space over an infinite field $F$. Prove that $V$ is not the union of finitely many proper subspaces.
Proof.
If $V$ is the set-theoretic union of $n$ proper subspaces $W_i$ ( $1 \leq i \leq n$ ), then $|F| \leq n-1$.
Proof. We may suppose no $W_i$ is contained in the union of the other subspaces. Let $u \in W_i, \quad u \notin \bigcup_{j \neq i} W_j$ and $v \notin W_i$.
Then $(v+F u) \cap W_i=\varnothing$ and $(v+F u) \cap W_j(j \neq i)$ contains at most one vector since otherwise $W_j$ would contain $u$. Hence
$$
|v+F u|=|F| \leq n-1 .
$$
Corollary: Avoidance lemma for vector spaces.
Let $E$ be a vector space over an infinite field. If a subspace is contained in a finite union of subspaces, it is contained in one of them.
Qed.