Exercise 3.1 Show that every linear map from a one-dimensional vector space to itself is multiplication by some scalar. More precisely, prove that if $\operatorname{dim} V=1$ and $T \in \mathcal{L}(V, V)$, then there exists $a \in \mathbf{F}$ such that $T v=a v$ for all $v \in V$.
Proof.
If $\operatorname{dim} V=1$, then in fact, $V=\mathbf{F}$ and it is spanned by $1 \in \mathbf{F}$.
Let $T$ be a linear map from $V$ to itself. Let $T(1)=\lambda \in V(=\mathbf{F})$.
Step 2
2 of 3
Every $v \in V$ is a scalar. Therefore,
$$
\begin{aligned}
T(v) & =T(v \cdot 1) \\
& =v T(1) \ldots .(\text { By the linearity of } T) \\
& =v \lambda
\end{aligned}
$$
Hence, $T v=\lambda v$ for every $v \in V$.
Qed.