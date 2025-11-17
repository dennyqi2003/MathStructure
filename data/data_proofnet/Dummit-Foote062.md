Exercise 5.4.2 Prove that a subgroup $H$ of $G$ is normal if and only if $[G, H] \leq H$.
Proof.
$H \unlhd G$ is equivalent to $g^{-1} h g \in H, \forall g \in G, \forall h \in H$. We claim that holds if and only if $h^{-1} g^{-1} h g \in H, \forall g \in G, \forall h \in H$, i.e., $\left\{h^{-1} g^{-1} h g: h \in H, g \in G\right\} \subseteq H$. That holds by the following argument:
If $g^{-1} h g \in H, \forall g \in G, \forall h \in H$, note that $h^{-1} \in H$, so multiplying them, we also obtain an element of $H$.
On the other hand, if $h^{-1} g^{-1} h g \in H, \forall g \in G, \forall h \in H$, then
$$
h h^{-1} g^{-1} h g=g^{-1} h g \in H, \forall g \in G, \forall h \in H .
$$
Since $\left\{h^{-1} g^{-1} h g: h \in H, g \in G\right\} \subseteq H \Leftrightarrow\left\langle\left\{h^{-1} g^{-1} h g: h \in H, g \in G\right\}\right\rangle \leq H$, we've solved the exercise by definition of $[H, G]$.
Qed.