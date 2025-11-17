Exercise 5.20 Suppose that $T \in \mathcal{L}(V)$ has $\operatorname{dim} V$ distinct eigenvalues and that $S \in \mathcal{L}(V)$ has the same eigenvectors as $T$ (not necessarily with the same eigenvalues). Prove that $S T=T S$.
Proof.
First off, let $n=\operatorname{dim} V$. so, there is a basis of $\left(v_1, \ldots, v_j\right)$ of $V$ that consist of eigenvectors of $T$. Now, let $\lambda_1, \ldots, \lambda_n$ be the corresponding eigenvalues, then we would have $T v_j=\lambda_1 v_j$ for every single $j$.

Now, for every $v_j$ is also an eigenvector of S, so $S v_j=a_j v_j$ for some $a_j \in F$. For each $j$, we would then have $(S T) v_j=S\left(T v_j\right)=\lambda_j S v_j=a_j \lambda_j v_j$ and $(T S) v_j=T\left(S v_j\right)=a_j T v_j=a_j \lambda_j v_j$. Since both operators, which are $S T$ and $T S$, agree on a basis, then both are equal.
Qed.