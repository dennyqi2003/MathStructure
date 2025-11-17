Exercise 34.9 Let $X$ be a compact Hausdorff space that is the union of the closed subspaces $X_1$ and $X_2$. If $X_1$ and $X_2$ are metrizable, show that $X$ is metrizable.
Proof.
Both $X_1$ and $X_2$ are compact, Hausdorff and metrizable, so by exercise 3 they are second countable, i.e. there are countable bases $\left\{U_{i, n} \subset X_i \mid n \in \mathbb{N}\right\}$ for $i \in\{1,2\}$. By the same exercise it is enough to show that $X$ is second countable. If $X_1 \cap X_2=\emptyset$ both $X_1$ and $X_2$ are open and the union $\left\{U_{i, n} \mid i \in\{1,2\} ; n \in \mathbb{N}\right\}$ of their countable bases form a countable base for $X$.

Suppose now $X_1 \cap X_2 \neq \emptyset$. Let $x \in X$ and $U \subset X$ be an open neighborhood of $x$. If $x \in X_i-X_j=X-$ $X_j$ then $U \cap X_i$ is open in $X_i$ and there is a basis neighborhood $U_{i, n}$ of $x$ such that $x \in U_{i, n} \cap X-X_j$ is an open neighborhood of $x$ in the open subset $X-X_j$, so $U_{i, n} \cap X-X_j$ is also open in $X$.
Suppose now that $x \in X_1 \cap X_2$. We have that $U \cap X_i$ is open in $X_i$ so there is a basis neighborhood $U_{i, n_i}$ contained in $U \cap X_i$. By definition of sub-space topology there is some open subset $V_{i, n_i} \subset X$ such that $U_{i, n_i}=$ $X_i \cap V_{i, n_i}$. Then
$$
x \in V_{1, n_1} \cap V_{2, n_2}=\left(V_{1, n_1} \cap V_{2, n_2} \cap X_1\right) \cup\left(V_{1, n_1} \cap V_{2, n_2} \cap X_2\right)=\left(U_{1, n_1} \cap V_{2, n_2}\right) \cup\left(V_{1, n_1} \cap U_{2, n_2}\right) \subset U
$$
Therefore the open subsets $U_{i, n} \cap X-X_j$ and $V_{1, n_1} \cap V_{2, n_2}$ form a countable base for $X$.
Qed.