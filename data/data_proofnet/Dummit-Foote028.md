Exercise 3.1.22b Prove that the intersection of an arbitrary nonempty collection of normal subgroups of a group is a normal subgroup (do not assume the collection is countable).
Proof.
Let $\left\{H_i \mid i \in I\right\}$ be an arbitrary collection of normal subgroups of $G$ and consider the intersection
$$
\bigcap_{i \in I} H_i
$$
Take an element $a$ in the intersection and an arbitrary element $g \in G$. Then $g a g^{-1} \in H_i$ because $H_i$ is normal for any $i \in H$
By the definition of the intersection, this shows that $g a g^{-1} \in \bigcap_{i \in I} H_i$ and therefore it is a normal subgroup.
Qed.