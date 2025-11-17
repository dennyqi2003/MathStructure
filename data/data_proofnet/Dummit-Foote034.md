Exercise 3.4.1 Prove that if $G$ is an abelian simple group then $G \cong Z_{p}$ for some prime $p$ (do not assume $G$ is a finite group).
Proof.
Solution: Let $G$ be an abelian simple group.
Suppose $G$ is infinite. If $x \in G$ is a nonidentity element of finite order, then $\langle x\rangle<G$ is a nontrivial normal subgroup, hence $G$ is not simple. If $x \in G$ is an element of infinite order, then $\left\langle x^2\right\rangle$ is a nontrivial normal subgroup, so $G$ is not simple.

Suppose $G$ is finite; say $|G|=n$. If $n$ is composite, say $n=p m$ for some prime $p$ with $m \neq 1$, then by Cauchy's Theorem $G$ contains an element $x$ of order $p$ and $\langle x\rangle$ is a nontrivial normal subgroup. Hence $G$ is not simple. Thus if $G$ is an abelian simple group, then $|G|=p$ is prime. We saw previously that the only such group up to isomorphism is $\mathbb{Z} /(p)$, so that $G \cong \mathbb{Z} /(p)$. Moreover, these groups are indeed simple.
Qed.