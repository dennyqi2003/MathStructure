Exercise 5.1 Suppose $T \in \mathcal{L}(V)$. Prove that if $U_{1}, \ldots, U_{m}$ are subspaces of $V$ invariant under $T$, then $U_{1}+\cdots+U_{m}$ is invariant under $T$.
Proof.
First off, assume that $U_1, \ldots, U_m$ are subspaces of $V$ invariant under $T$. Now, consider a vector $u \in$ $U_1+\ldots+U_m$. There does exist $u_1 \in U_1, \ldots, u_m \in U_m$ such that $u=u_1+\ldots+u_m$.

Once you apply $T$ towards both sides of the previous equation, we would then get $T u=T u_1+\ldots+$ $T u_m$.

Since each $U_j$ is invariant under $T$, then we would have $T u_1 \in U_1+\ldots+T u_m$. This would then make the equation shows that $T u \in U_1+\ldots+T u_m$, which does imply that $U_1+. .+U_m$ is invariant under $T$
Qed.