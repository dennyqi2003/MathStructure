Exercise 30.13 Show that if $X$ has a countable dense subset, every collection of disjoint open sets in $X$ is countable.
Proof.
Let $\mathcal{U}$ be a collection of disjoint open sets in $X$ and let $A$ be a countable dense subset of $X$.
Since $A$ is dense in $X$, every $U \in \mathcal{U}$ intesects $S$. Therefore, there exists a point $x_U \in U \cap S$.
Let $U_1, U_2 \in \mathcal{U}, U_1 \neq U_2$. Then $x_{U_1} \neq x_{U_2}$ since $U_1 \cap U_2=\emptyset$.
Thus, the function $\mathcal{U} \rightarrow S$ given by $U \mapsto x_U$ is injective and therefore, since $S$ is countable, it follows that $\mathcal{U}$ is countable.
Qed.