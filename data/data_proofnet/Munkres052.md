Exercise 32.2a Show that if $\prod X_\alpha$ is Hausdorff, then so is $X_\alpha$. Assume that each $X_\alpha$ is nonempty.
Proof.
Suppose that $X=\prod_\beta X_\beta$ is Hausdorff and let $\alpha$ be any index.
Let $x, y \in X_\alpha$ be any points such that $x \neq y$. Since all $X_\beta$ are nonempty, there exist points $\mathbf{x}, \mathbf{y} \in X$ such that $x_\beta=y_\beta$ for every $\beta \neq \alpha$ and $x_\alpha=x, y_\alpha=y$.
Since $x \neq y$, it follows that $\mathbf{x} \neq \mathbf{y}$. Since $X$ is Hausdorff, there exist open disjoint sets $U, V \subseteq X$ such that $\mathbf{x} \in U$ and $\mathbf{y} \in V$.
For $\beta \neq \alpha$ we have that $x_\beta=y_\beta \in \pi_\beta(U) \cap \pi_\beta(V)$, hence $\pi_\beta(U)$ and $\pi_\beta(V)$ are not disjoint.
Since $U$ and $V$ are disjoint, it follows that $\pi_\alpha(U) \cap \pi_\alpha(V)=\emptyset$.
We also have that $x \in \pi_\alpha(U)$ and $y \in \pi_\alpha(V)$ and since the projections are open maps, it follows that the sets $\pi_\alpha(U)$ and $\pi_\alpha(V)$ are open.
This proves that $x$ and $y$ can be separated by open sets, so $X_\alpha$ is Hausdorff.
Qed.