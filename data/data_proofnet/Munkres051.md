Exercise 32.1 Show that a closed subspace of a normal space is normal.
Proof.
Let $X$ be a normal space and $Y$ a closed subspace of $X$.
First we shows that $Y$ is a $T_1$-space.
Let $y \in Y$ be any point. Since $X$ is normal, $X$ is also a $T_1$ space and therefore $\{y\}$ is closed in $X$.
Then it follows that $\{y\}=\{y\} \cap Y$ is closed in $Y$ (in relative topology).
Now let's prove that $X$ is a $T_4$-space.
Let $F, G \subseteq Y$ be disjoint closed sets. Since $F$ and $G$ are closed in $Y$ and $Y$ is closed in $X$, it follows that $F$ and $G$ are closed in $X$.

Since $X$ is normal, $X$ is also a $T_4$-space and therefore there exist disjoint open sets $U, V \subseteq$ $X$ such that $F \subseteq U$ and $G \subseteq V$.
However, then $U \cap Y$ and $V \cap Y$ are open disjoint sets in $Y$ (in relative topology) which separate $F$ and $G$.
Qed.