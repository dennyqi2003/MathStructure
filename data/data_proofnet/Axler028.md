Exercise 7.14 Suppose $T \in \mathcal{L}(V)$ is self-adjoint, $\lambda \in \mathbf{F}$, and $\epsilon>0$. Prove that if there exists $v \in V$ such that $\|v\|=1$ and $\|T v-\lambda v\|<\epsilon,$ then $T$ has an eigenvalue $\lambda^{\prime}$ such that $\left|\lambda-\lambda^{\prime}\right|<\epsilon$.
Proof.
Let $T \in \mathcal{L}(V)$ be a self-adjoint, and let $\lambda \in \mathbf{F}$ and $\epsilon>0$.
By the Spectral Theorem, there is $e_1, \ldots, e_n$ an orthonormal basis of $V$ consisting of eigenvectors of $T$ and let $\lambda_1, \ldots, \lambda_n$ denote their corresponding eigenvalues.
Choose an eigenvalue $\lambda^{\prime}$ of $T$ such that $\left|\lambda^{\prime}-\lambda\right|^2$ is minimized.
There are $a_1, \ldots, a_n \in \mathbb{F}$ such that
$$
v=a_1 e_1+\cdots+a_n e_n .
$$
Thus, we have
$$
\begin{aligned}
\epsilon^2 & >|| T v-\left.\lambda v\right|^2 \\
& =\left|\left\langle T v-\lambda v, e_1\right\rangle\right|^2+\cdots+\left|\left\langle T v-\lambda v, e_n\right\rangle\right|^2 \\
& =\left|\lambda_1 a_1-\lambda a_1\right|^2+\cdots+\left|\lambda_n a_n-\lambda a_n\right|^2 \\
& =\left|a_1\right|^2\left|\lambda_1-\lambda\right|^2+\cdots+\left|a_n\right|^2\left|\lambda_n-\lambda\right|^2 \\
& \geq\left|a_1\right|^2\left|\lambda^{\prime}-\lambda\right|^2+\cdots+\left|a_n\right|^2\left|\lambda^{\prime}-\lambda\right|^2 \\
& =\left|\lambda^{\prime}-\lambda\right|^2
\end{aligned}
$$
where the second and fifth lines follow from $6.30$ (the fifth because $\|v\|=1$ ). Now, we taking the square root.
Hence, $T$ has an eigenvalue $\lambda^{\prime}$ such that $\left|\lambda^{\prime}-\lambda\right|<\epsilon$
Qed.