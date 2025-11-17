Exercise 7.10 Suppose $V$ is a complex inner-product space and $T \in \mathcal{L}(V)$ is a normal operator such that $T^{9}=T^{8}$. Prove that $T$ is self-adjoint and $T^{2}=T$.
Proof.
Based on the complex spectral theorem, there is an orthonormal basis of $\left(e_1, \ldots, e_n\right)$ of $V$ consisting of eigenvectors of $T$. Now, let $\lambda_1, \ldots, \lambda_n$ be the corresponding eigenvalues. Therefore,
$$
T e_1=\lambda_j e_j
$$
for $j=1 \ldots n$.

Next, by applying $T$ repeatedly to both sides of the equation above, we get $T^9 e_j=\left(\lambda_j\right)^9 e_j$ and rei =8ej. Thus $T^8 e_j=\left(\lambda_j\right)^8 e_j$, which implies that $\lambda_j$ equals 0 or 1 . In particular, all the eigenvalues of $T$ are real. This would then imply that $T$ is self-adjoint.

Now, by applying $T$ to both sides of the equation above, we get
$$
\begin{aligned}
T^2 e_j & =\left(\lambda_j\right)^2 e_j \\
& =\lambda_j e_j \\
& =T e_j
\end{aligned}
$$
which is where the second equality holds because $\lambda_j$ equals 0 or 1 . Because $T^2$ and $T$ agree on a basis, they must be equal.
Qed.