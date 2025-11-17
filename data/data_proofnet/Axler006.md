Exercise 1.8 Prove that the intersection of any collection of subspaces of $V$ is a subspace of $V$.
Proof.
Let $V_1, V_2, \ldots, V_n$ be subspaces of the vector space $V$ over the field $F$. We must show that their intersection $V_1 \cap V_2 \cap \ldots \cap V_n$ is also a subspace of $V$.

To begin, we observe that the additive identity $0$ of $V$ is in $V_1 \cap V_2 \cap \ldots \cap V_n$. This is because $0$ is in each subspace $V_i$, as they are subspaces and hence contain the additive identity.

Next, we show that the intersection of subspaces is closed under addition. Let $u$ and $v$ be vectors in $V_1 \cap V_2 \cap \ldots \cap V_n$. By definition, $u$ and $v$ belong to each of the subspaces $V_i$. Since each $V_i$ is a subspace and therefore closed under addition, it follows that $u+v$ belongs to each $V_i$. Thus, $u+v$ belongs to the intersection $V_1 \cap V_2 \cap \ldots \cap V_n$.

Finally, we show that the intersection of subspaces is closed under scalar multiplication. Let $a$ be a scalar in $F$ and let $v$ be a vector in $V_1 \cap V_2 \cap \ldots \cap V_n$. Since $v$ belongs to each $V_i$, we have $av$ belongs to each $V_i$ as well, as $V_i$ are subspaces and hence closed under scalar multiplication. Therefore, $av$ belongs to the intersection $V_1 \cap V_2 \cap \ldots \cap V_n$.

Thus, we have shown that $V_1 \cap V_2 \cap \ldots \cap V_n$ is a subspace of $V$.
Qed.