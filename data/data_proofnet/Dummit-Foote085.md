Exercise 9.4.9 Prove that the polynomial $x^{2}-\sqrt{2}$ is irreducible over $\mathbb{Z}[\sqrt{2}]$. You may assume that $\mathbb{Z}[\sqrt{2}]$ is a U.F.D.
Proof.
$Z[\sqrt{2}]$ is an Euclidean domain, and so a unique factorization domain.
We have to prove $p(x)=x^2-\sqrt{2}$ irreducible.
Suppose to the contrary.
if $p(x)$ is reducible then it must have root.
Let $a+b \sqrt{2}$ be a root of $x^2-\sqrt{2}$.
Now we have
$$
a^2+2 b^2+2 a b \sqrt{2}=\sqrt{2}
$$
By comparing the coefficients we get $2 a b=1$ for some pair of integers $a$ and $b$, a contradiction.
So $p(x)$ is irredicible over $Z[\sqrt{2}]$.
Qed.