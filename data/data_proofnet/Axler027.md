Exercise 7.11 Suppose $V$ is a complex inner-product space. Prove that every normal operator on $V$ has a square root. (An operator $S \in \mathcal{L}(V)$ is called a square root of $T \in \mathcal{L}(V)$ if $S^{2}=T$.)
Proof.
Let $V$ be a complex inner product space.
It is known that an operator $S \in \mathcal{L}(V)$ is called a square root of $T \in \mathcal{L}(V)$ if
$$
S^2=T
$$
Now, suppose that $T$ is a normal operator on $V$.
By the Complex Spectral Theorem, there is $e_1, \ldots, e_n$ an orthonormal basis of $V$ consisting of eigenvalues of $T$ and let $\lambda_1, \ldots, \lambda_n$ denote their corresponding eigenvalues.
Define $S$ by
$$
S e_j=\sqrt{\lambda_j} e_j,
$$
for each $j=1, \ldots, n$.
Obviously, $S^2 e_j=\lambda_j e_j=T e_j$.
Hence, $S^2=T$ so there exist a square root of $T$.
Qed.