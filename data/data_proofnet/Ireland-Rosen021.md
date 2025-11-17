Exercise 18.4 Show that 1729 is the smallest positive integer expressible as the sum of two different integral cubes in two ways.
Proof.
Let $n=a^3+b^3$, and suppose that $\operatorname{gcd}(a, b)=1$. If a prime $p \mid a^3+b^3$, then
$$
\left(a b^{-1}\right)^3 \equiv_p-1
$$
Thus $3 \mid \frac{p-1}{2}$, that is, $p \equiv_6 1$.
If we have $n=a^3+b^3=c^3+d^3$, then we can factor $n$ as
$$
\begin{aligned}
& n=(a+b)\left(a^2-a b+b^2\right) \\
& n=(c+d)\left(c^2-c d+d^2\right)
\end{aligned}
$$
Thus we need $n$ to have atleast 3 disctinct prime factors, and so the smallest taxicab number is on the form
$$
n=(6 k+1)(12 k+1)(18 k+1)
$$
Qed.