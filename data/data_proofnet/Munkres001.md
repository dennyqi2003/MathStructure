Exercise 13.1 Let $X$ be a topological space; let $A$ be a subset of $X$. Suppose that for each $x \in A$ there is an open set $U$ containing $x$ such that $U \subset A$. Show that $A$ is open in $X$.
Proof.
Since, from the given hypothesis given any $x \in A$ there exists an open set containing $x$ say, $U_x$ such that $U_x \subset A$. Thus, we claim that
$$
A=\bigcup_{x \in A} U_x
$$
Observe that if we prove the above claim, then $A$ will be open, being a union of arbitrary open sets. Since, for each $x \in A, U_x \subset A \Longrightarrow \cup U_x \subset A$. For the converse, observe that given any $x \in A, x \in U_x$ and hence in the union. Thus we proved our claim, and hence $A$ is an open set.
Qed.