Exercise 32.2c Show that if $\prod X_\alpha$ is normal, then so is $X_\alpha$. Assume that each $X_\alpha$ is nonempty.
Proof.
Suppose that $X=\prod_\beta X_\beta$ is normal and let $\alpha$ be any index.
Since $X$ is normal, it follows that $X$ is Hausdorff (or regular), which then implies that $X_\alpha$ is Hausdorff (or regular). This imples that $X_\alpha$ satisfies the $T_1$ axiom.
Now the proof that $X_\alpha$ satisfies the $T_4$ axiom is the same as for regular spaces.
If $F, G \subseteq X_\alpha$ are disjoint closed sets, then $\prod_\beta F_\beta$ and $\prod_\beta G_\beta$, where $F_\alpha=F, G_\alpha=G$ and $F_\beta=G_\beta=X_\beta$ for $\beta \neq \alpha$, are disjoint closed sets in $X$.
Since $X$ is normal (and therefore satisfies the $T_4$ axiom), there exist disjoint open sets $U, V \subseteq X$ such that $\prod_\beta F_\beta \subseteq U$ and $\prod_\beta G_\beta \subseteq V$
Then $\pi_\alpha(U)$ and $\pi_\alpha(V)$ are disjoint open sets in $X_\alpha$ such that $F \subseteq \pi_\alpha(U)$ and $G \subseteq \pi_\alpha(V)$.
Qed.