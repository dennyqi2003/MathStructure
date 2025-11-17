Exercise 2.5.44 Prove that a group of order $p^2$, $p$ a prime, has a normal subgroup of order $p$.
Proof.
We use the result from problem 40 which is as follows: Suppose $G$ is a group, $H$ is a subgroup and $|G|=n$ and $n \nmid\left(i_G(H)\right) !$. Then there exists a normal subgroup $K \neq \{ e \}$ and $K \subseteq H$.

So, we have now a group $G$ of order $p^2$. Suppose that the group is cyclic, then it is abelian and any subgroup of order $p$ is normal. Now let us suppose that $G$ is not cyclic, then there exists an element $a$ of order $p$, and $A=\langle a\rangle$. Now $i_G(A)=p$, so $p^2 \nmid p$ ! , hence by the above result there is a normal subgroup $K$, non-trivial and $K \subseteq A$. But $|A|=p$, a prime order subgroup, hence has no non-trivial subgroup, so $K=A$. so $A$ is normal subgroup.
Qed.