Exercise 31.1 Show that if $X$ is regular, every pair of points of $X$ have neighborhoods whose closures are disjoint.
Proof.
Let $x, y \in X$ be two points such that $x \neq y$. Since $X$ is regular (and thus Hausdorff), there exist disjoint open sets $U, V \subseteq X$ such that $x \in U$ and $y \in V$.
Note that $y \notin \bar{U}$. Otherwise $V$ must intersect $U$ in a point different from $y$ since $V$ is an open neighborhood of $y$, which is a contradiction since $U$ and $V$ are disjoint.
Since $X$ is regular and $\bar{U}$ is closed, there exist disjoint open sets $U^{\prime}, V^{\prime} \subseteq X$ such that $\bar{U} \subseteq U^{\prime}$ and $y \in V^{\prime}$.

And now $U$ and $V^{\prime}$ are neighborhoods of $x$ and $y$ whose closures are disjoint. If $\bar{U} \cap \overline{V^{\prime}} \neq \emptyset$, then it follows that $U^{\prime} \supseteq U$ intersects $\overline{V^{\prime}}$. Since $U^{\prime}$ is open, it follows that $U^{\prime}$ intersects $V^{\prime}$, which is a contradiction.
Qed.