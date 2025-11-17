Exercise 2.4.16b Show that the subgroup of all rotations in a dihedral group is a maximal subgroup.
Proof.
Fix a positive integer $n>1$ and let $H \leq D_{2 n}$ consist of the rotations of $D_{2 n}$. That is, $H=\langle r\rangle$. Now, this subgroup is proper since it does not contain $s$. If $H$ is not maximal, then by the previous proof we know there is a maximal subset $K$ containing $H$. Then $K$ must contain a reflection $s r^k$ for $k \in\{0,1, \ldots, n-1\}$. Then since $s r^k \in K$ and $r^{n-k} \in K$, it follows by closure that
$$
s=\left(s r^k\right)\left(r^{n-k}\right) \in K .
$$
But $D_{2 n}=\langle r, s\rangle$, so this shows that $K=D_{2 n}$, which is a contradiction. Therefore $H$ must be maximal.
Qed.