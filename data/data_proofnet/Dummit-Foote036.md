Exercise 3.4.5a Prove that subgroups of a solvable group are solvable.
Proof.
Let $G$ be a solvable group and let $H \leq G$. Since $G$ is solvable, we may find a chain of subgroups
$$
1=G_0 \unlhd G_1 \unlhd G_2 \unlhd \cdots \unlhd G_n=G
$$
so that each quotient $G_{i+1} / G_i$ is abelian. For each $i$, define
$$
H_i=G_i \cap H, \quad 0 \leq i \leq n .
$$
Then $H_i \leq H_{i+1}$ for each $i$. Moreover, if $g \in H_{i+1}$ and $x \in H_i$, then in particular $g \in G_{i+1}$ and $x \in G_i$, so that
$$
g x g^{-1} \in G_i
$$
because $G_i \unlhd G_{i+1}$. But $g$ and $x$ also belong to $H$, so
$$
g x g^{-1} \in H_i,
$$
which shows that $H_i \unlhd H_{i+1}$ for each $i$.
Next, note that
$$
H_i=G_i \cap H=\left(G_i \cap G_{i+1}\right) \cap H=G_i \cap H_{i+1} .
$$
By the Second Isomorphism Theorem, we then have
$$
H_{i+1} / H_i=H_{i+1} /\left(H_{i+1} \cap G_i\right) \cong H_{i+1} G_i / G_i \leq G_{i+1} / G_i .
$$
Since $H_{i+1} / H_i$ is isomorphic to a subgroup of the abelian group $G_{i+1} / G_i$, it follows that $H_{i+1} / H_i$ is also abelian. This completes the proof that $H$ is solvable.
Qed.