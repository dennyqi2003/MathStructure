Exercise 2.10.1 Let $A$ be a normal subgroup of a group $G$, and suppose that $b \in G$ is an element of prime order $p$, and that $b \not\in A$. Show that $A \cap (b) = (e)$.
Proof.
If $b \in G$ has order $p$, then $(b)$ is a cyclic group of order $p$. Since $A$ is a subgroup of $G$, we have $A \cap (b)$ is a subgroup of $G$. Also, $A \cap (b) \subseteq (b)$. So $A \cap (b)$ is a subgroup of $(b)$. Since $(b)$ is a cyclic group of order $p$, the only subgroups of $(b)$ are $(e)$ and $(b)$ itself.

Therefore, either $A \cap (b) = (e)$ or $A \cap (b) = (b)$. If $A \cap (b) = (e)$, then we are done. Otherwise, if $A \cap (b) = (b)$, then $A \subseteq (b)$. Since $A$ is a subgroup of $G$ and $A \subseteq (b)$, it follows that $A$ is a subgroup of $(b)$.

Since the only subgroups of $(b)$ are $(e)$ and $(b)$ itself, we have either $A = (e)$ or $A = (b)$. If $A = (e)$, then $A \cap (b) = (e)$ and we are done. But if $A = (b)$, then $b \in A$ as $b \in (b)$, which contradicts our hypothesis that $b \notin A$. So $A \neq (b)$.

Hence $A \cap (b) \neq (b)$. Therefore, $A \cap (b) = (e)$. This completes our proof.
Qed.