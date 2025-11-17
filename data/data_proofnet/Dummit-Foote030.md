Exercise 3.2.11 Let $H \leq K \leq G$. Prove that $|G: H|=|G: K| \cdot|K: H|$ (do not assume $G$ is finite).
Proof.
Proof. Let $G$ be a group and let $I$ be a nonempty set of indices, not necessarily countable. Consider the collection of subgroups $\left\{N_\alpha \mid \alpha \in I\right\}$, where $N_\alpha \unlhd G$ for each $\alpha \in I$. Let
$$
N=\bigcap_{\alpha \in I} N_\alpha .
$$
We know $N$ is a subgroup of $G$. 
For any $g \in G$ and any $n \in N$, we must have $n \in N_\alpha$ for each $\alpha$. And since $N_\alpha \unlhd G$, we have $g n g^{-1} \in N_\alpha$ for each $\alpha$. Therefore $g n g^{-1} \in N$, which shows that $g N g^{-1} \subseteq N$ for each $g \in G$. As before, this is enough to complete the proof.
Qed.