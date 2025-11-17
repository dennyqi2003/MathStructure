Exercise 5.24 Suppose $V$ is a real vector space and $T \in \mathcal{L}(V)$ has no eigenvalues. Prove that every subspace of $V$ invariant under $T$ has even dimension.
Proof.
First off, let us assume that $U$ is a subspace of $V$ that is invariant under $T$. Therefore, $\left.T\right|_U \in \mathcal{L}(U)$. If $\operatorname{dim}$ $U$ were odd, then $\left.T\right|_U$ would have an eigenvalue $\lambda \in \mathbb{R}$, so there would exist a nonzero vector $u \in U$ such that
$$
\left.T\right|_U u=\lambda u .
$$
So, this would imply that $T_u=\lambda u$, which would imply that $\lambda$ is an eigenvalue of $T$. But $T$ has no eigenvalues, so $\operatorname{dim} U$ must be even.
Qed.