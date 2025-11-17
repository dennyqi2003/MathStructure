Exercise 3.1.3a Let $A$ be an abelian group and let $B$ be a subgroup of $A$. Prove that $A / B$ is abelian.
Proof.
Lemma: Let $G$ be a group. If $|G|=2$, then $G \cong Z_2$.
Proof: Since $G=\{e a\}$ has an identity element, say $e$, we know that $e e=e, e a=a$, and $a e=a$. If $a^2=a$, we have $a=e$, a contradiction. Thus $a^2=e$. We can easily see that $G \cong Z_2$.

If $A$ is abelian, every subgroup of $A$ is normal; in particular, $B$ is normal, so $A / B$ is a group. Now let $x B, y B \in A / B$. Then
$$
(x B)(y B)=(x y) B=(y x) B=(y B)(x B) .
$$
Hence $A / B$ is abelian.
Qed.