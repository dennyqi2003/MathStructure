Exercise 4.6.2 Prove that $f(x) = x^3 + 3x + 2$ is irreducible in $Q[x]$.
Proof.
Let us assume that $f(x)$ is reducible over $\mathbb{Q}[x]$.
Then there exists a rational root of $f(x)$.
Let $p / q$ be a rational root of $f(x)$, where $\operatorname{gcd}(p, q)=1$.
Then $f(p / q)=0$.
Now,
$$
\begin{aligned}
& f(p / q)=(p / q)^3+3(p / q)+2 \\
\Longrightarrow & (p / q)^3+3(p / q)+2=0 \\
\Longrightarrow & p^3+3 p q^2=-2 q^3 \\
\Longrightarrow & p\left(p^2+3 q^2\right)=-q^3
\end{aligned}
$$
It follows that, $p$ divides $q$ which is a contradiction to the fact that $\operatorname{gcd}(p, q)=1$.
This implies that $f(x)$ has no rational root.
Now we know that, a polynomial of degree two or three over a field $F$ is reducible if and only if it has a root in $F$.
Now $f(x)$ is a 3 degree polynomial having no root in $\mathbb{Q}$.
So, $f(x)$ is irreducible in $\mathbb{Q}[x]$.
This completes the proof.
Qed.