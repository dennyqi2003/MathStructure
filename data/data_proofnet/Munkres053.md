Exercise 32.2b Show that if $\prod X_\alpha$ is regular, then so is $X_\alpha$. Assume that each $X_\alpha$ is nonempty.
Proof.
Suppose that $X=\prod_\beta X_\beta$ is regular and let $\alpha$ be any index.
We have to prove that $X_\alpha$ satisfies the $T_1$ and the $T_3$ axiom.
Since $X$ is regular, it follows that $X$ is Hausdorff, which then implies that $X_\alpha$ is Hausdorff. However, this implies that $X_\alpha$ satisfies the $T_1$ axiom.

Let now $F \subseteq X_\alpha$ be a closed set and $x \in X_\alpha \backslash F$ a point.
Then $\prod_\beta F_\beta$, where $F_\alpha=F$ and $F_\beta=X_\beta$ for $\beta \neq \alpha$, is a closed set in $X$ since $\left(\prod_\beta F_\beta\right)^c=\prod_\beta U_\beta$, where $U_\alpha=F^c$ and $U_\beta=X_\beta$ for $\beta \neq \alpha$, which is an open set because it is a base element for the product topology.
Since all $X_\beta$ are nonempty, there exists a point $\mathbf{x} \in X$ such that $x_\alpha=x$. Then $\mathbf{x} \notin \prod_\beta F_\beta$.
Now since $X$ is regular (and therefore satisfies the $T_3$ axiom), there exist disjoint open sets $U, V \subseteq X$ such that $\mathbf{x} \in U$ and $\prod_\beta F_\beta \subseteq V$.

Now for every $\beta \neq \alpha$ we have that $x_\beta \in X_\beta=\pi_\beta(V)$. However, since $x_\beta \in \pi_\beta(U)$, it follows that $\pi_\beta(U) \cap \pi_\beta(V) \neq \emptyset$.
Then $U \cap V=\emptyset$ implies that $\pi_\alpha(U) \cap \pi_\alpha(V)=\emptyset$.. Also, $x \in \pi_\alpha(U)$ and $F \subseteq \pi_\alpha(V)$ and $\pi_\alpha(U), \pi_\alpha(V)$ are open sets since $\pi_\alpha$ is an open map.
Therefore, $X_\alpha$ satisfies the $T_3$ axiom.
Qed.