Exercise 2.26 Prove that a set $U \subset M$ is open if and only if none of its points are limits of its complement.
Proof.
Assume that none of the points of $U$ are limits of its complement, and let us prove that $U$ is open. Assume by contradiction that $U$ is not open, so there exists $p \in M$ so that $\forall r>0$ there exists $q \in M$ with $d(p, q)<r$ but $q \notin U$. Applying this to $r=1 / n$ we obtain $q_n \in U^c$ such that $d\left(q_n, p\right)<1 / n$. But then $q_n \rightarrow p$ and $p$ is a limit of a sequence of points in $U^c$, a contradiction.

Assume now that $U$ is open. Assume by contradiction there exists $p \in U$ and $p_n \in U^c$ such that $p_n \rightarrow p$. Since $U$ is open, there exists $r>0$ such that $d(p, x)<r$ for $x \in M$ implies $x \in U$. But since $p_n \rightarrow p$, there exists $n_0 \in \mathbb{N}$ such that $n \geq n_0$ implies $d\left(p_n, p\right)<r$, therefore $p_n \in U$ for $n \geq n_0$, a contradiction since $p_n \in U^c$.
Qed.