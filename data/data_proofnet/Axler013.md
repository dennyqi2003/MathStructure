Exercise 5.11 Suppose $S, T \in \mathcal{L}(V)$. Prove that $S T$ and $T S$ have the same eigenvalues.
Proof.
To start, let $\lambda \in F$ be an eigenvalue of $S T$. Now, we would want $\lambda$ to be an eigenvalue of $T S$. Since $\lambda$, by itself, is an eigenvalue of $S T$, then there has to be a nonzero vector $v \in V$ such that $(S T) v=\lambda v$.
Now, With a given reference that $(S T) v=\lambda v$, you will then have the following: $(T S)(T v)=$ $T(S T v)=T(\lambda v)=\lambda T v$
If $T v \neq 0$, then the listed equation above shows that $\lambda$ is an eigenvalue of $T S$.
If $T v=0$, then $\lambda=0$, since $S(T v)=\lambda T v$. This also means that $T$ isn't invertible, which would imply that $T S$ isn't invertible, which can also be implied that $\lambda$, which equals 0 , is an eigenvalue of $T S$.
Step 3
3 of 3
Now, regardless of whether $T v=0$ or not, we would have shown that $\lambda$ is an eigenvalue of $T S$. Since $\lambda$ (was) an arbitrary eigenvalue of $S T$, we have shown that every single eigenvalue of $S T$ is an eigenvalue of $T S$. When you do reverse the roles of both $S$ and $T$, then we can conclude that that every single eigenvalue of $T S$ is also an eigenvalue of $S T$. Therefore, both $S T$ and $T S$ have the exact same eigenvalues.
Qed.