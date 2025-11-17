Exercise 5.13 Suppose $T \in \mathcal{L}(V)$ is such that every subspace of $V$ with dimension $\operatorname{dim} V-1$ is invariant under $T$. Prove that $T$ is a scalar multiple of the identity operator.
Proof.
First off, let $T$ isn't a scalar multiple of the identity operator. So, there does exists that $v \in V$ such that $u$ isn't an eigenvector of $T$. Therefore, $(u, T u)$ is linearly independent.

Next, you should extend $(u, T u)$ to a basis of $\left(u, T u, v_1, \ldots, v_n\right)$ of $V$. So, let $U=\operatorname{span}\left(u, v_1, \ldots, v_n\right)$. Then, $U$ is a subspace of $V$ and $\operatorname{dim} U=\operatorname{dim} V-1$. However, $U$ isn't invariant under $T$ since both $u \in U$ and $T u \in U$. This given contradiction to our hypothesis about $T$ actually shows us that our guess that $T$ is not a scalar multiple of the identity must have been false.
Qed.