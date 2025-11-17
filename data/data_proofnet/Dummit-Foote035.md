Exercise 3.4.4 Use Cauchy's Theorem and induction to show that a finite abelian group has a subgroup of order $n$ for each positive divisor $n$ of its order.
Proof.
Let $G$ be a finite abelian group. We use induction on $|G|$. Certainly the result holds for the trivial group. And if $|G|=p$ for some prime $p$, then the positive divisors of $|G|$ are 1 and $p$ and the result is again trivial.

Now assume that the statement is true for all groups of order strictly smaller than $|G|$, and let $n$ be a positive divisor of $|G|$ with $n>1$. First, if $n$ is prime then Cauchy's Theorem allows us to find an element $x \in G$ having order $n$. Then $\langle x\rangle$ is the desired subgroup. On the other hand, if $n$ is not prime, then $n$ has a prime divisor $p$, so that $n=k p$ for some integer $k$. Cauchy's Theorem allows us to find an element $x$ having order $p$. Set $N=\langle x\rangle$. By Lagrange's Theorem,
$$
|G / N|=\frac{|G|}{|N|}<|G| .
$$
Now, by the inductive hypothesis, the group $G / N$ must have a subgroup of order $k$. And by the Lattice Isomorphism Theorem, this subgroup has the form $H / N$ for some subgroup $H$ of $G$. Then $|H|=k|N|=k p=n$, so that $H$ has order $n$. This completes the inductive step.
Qed.