Exercise 1998.b6 Prove that, for any integers $a, b, c$, there exists a positive integer $n$ such that $\sqrt{n^3+a n^2+b n+c}$ is not an integer.
Proof.
We prove more generally that for any polynomial $P(z)$ with integer
coefficients which is not a perfect square, there exists a positive
integer $n$ such that $P(n)$ is not a perfect square. Of course it
suffices to assume $P(z)$ has no repeated factors, which is to say $P(z)$
and its derivative $P'(z)$ are relatively prime.

In particular, if we carry out the Euclidean algorithm on $P(z)$ and $P'(z)$
without dividing, we get an integer $D$ (the discriminant of $P$) such that
the greatest common divisor of $P(n)$ and $P'(n)$ divides $D$ for any $n$.
Now there exist infinitely many primes $p$ such that $p$ divides $P(n)$ for
some $n$: if there were only finitely many, say, $p_1, \dots, p_k$, then
for any $n$ divisible by $m = P(0) p_1 p_2 \cdots p_k$, we have $P(n)
\equiv P(0) \pmod{m}$, that is, $P(n)/P(0)$ is not divisible by $p_1,
\dots, p_k$, so must be $\pm 1$, but then $P$ takes some value infinitely
many times, contradiction. In particular, we can choose some such $p$ not
dividing $D$, and choose $n$ such that $p$ divides $P(n)$. Then $P(n+kp)
\equiv P(n) + kp P'(n) (\mathrm{mod}\,p)$
(write out the Taylor series of the left side);
in particular, since $p$ does not divide $P'(n)$, we can find some $k$
such that $P(n+kp)$ is divisible by $p$ but not by $p^2$, and so
is not a perfect square.
Qed.