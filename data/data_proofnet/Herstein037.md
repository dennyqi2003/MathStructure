Exercise 4.5.23 Let $F = \mathbb{Z}_7$ and let $p(x) = x^3 - 2$ and $q(x) = x^3 + 2$ be in $F[x]$. Show that $p(x)$ and $q(x)$ are irreducible in $F[x]$ and that the fields $F[x]/(p(x))$ and $F[x]/(q(x))$ are isomorphic.
Proof.
We have that $p(x)$ and $q(x)$ are irreducible if they have no roots in $\mathbb{Z}_7$, which can easily be checked. E.g. for $p(x)$ we have that $p(0)=5, p(1)=6, p(2)=6, p(3)=4, p(4)=6$, $p(5)=4, p(6)=4$, and similarly for $q(x)$.

We have that every element of $F[x] /(p(x))$ is equal to $a x^2+b x+c+(p(x))$, and likewise for $F[x] /(q(x))$. We consider a map $\tau$ : $F[x] /(p(x)) \rightarrow F[x] /(q(x))$ given by
$$
\tau\left(a x^2+b x+c+(p(x))\right)=a x^2-b x+c+(q(x)) .
$$
This map is obviously onto, and since $|F[x] /(p(x))|=|F[x] /(q(x))|=7^3$ by Problem 16, it is also one-to-one. We claim that it is a homomorphism. Additivity of $\tau$ is immediate by the linearity of addition of polynomial coefficient, so we just have to check the multiplicativity; if $n=a x^2+b x+$ $c+(p(x))$ and $m=d x^2+e x+f+(p(x))$ then
$$
\begin{aligned}
\tau(n m) & =\tau\left(a d x^4+(a e+b d) x^3+(a f+b e+c d) x^2+(b f+c e) x+c f+(p(x))\right) \\
& =\tau\left(2 a d x+2(a e+b d)+(a f+b e+c d) x^2+(b f+c e) x+c f+(p(x))\right) \\
& =\tau\left((a f+b e+c d) x^2+(b f+c e+2 a d) x+(c f+2 a e+2 b d)+(p(x))\right) \\
& =(a f+b e+c d) x^2-(b f+c e+2 a d) x+c f+2 a e+2 b d+(q(x)) \\
& =a d x^4-(a e+b d) x^3+(a f+b e+c d) x^2-(b f+c e) x+c f+(q(x)) \\
& =\left(a x^2-b x+c+(q(x))\right)\left(d x^2-e x+f+(q(x))\right) \\
& =\tau(n) \tau(m) .
\end{aligned}
$$
where in the second equality we used that $x^3+p(x)=2+p(x)$ and in the fifth we used that $x^3+$ $q(x)=-2+q(x)$
Qed.