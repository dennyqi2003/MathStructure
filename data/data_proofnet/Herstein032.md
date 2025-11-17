Exercise 4.2.9 Let $p$ be an odd prime and let $1 + \frac{1}{2} + ... + \frac{1}{p - 1} = \frac{a}{b}$, where $a, b$ are integers. Show that $p \mid a$.
Proof.
First we prove for prime $p=3$ and then for all prime $p>3$.
Let us take $p=3$. Then the sum
$$
\frac{1}{1}+\frac{1}{2}+\ldots+\frac{1}{(p-1)}
$$
becomes
$$
1+\frac{1}{3-1}=1+\frac{1}{2}=\frac{3}{2} .
$$
Therefore in this case $\quad \frac{a}{b}=\frac{3}{2} \quad$ implies $3 \mid a$, i.e. $p \mid a$.
Now for odd prime $p>3$.
Let us consider $f(x)=(x-1)(x-2) \ldots(x-(p-1))$.
Now, by Fermat, we know that the coefficients of $f(x)$ other than the $x^{p-1}$ and $x^0$ are divisible by $p$.
So if,
$$
\begin{array}{r}
f(x)=x^{p-1}+\sum_{i=0}^{p-2} a_i x^i \\
\text { and } p>3 .
\end{array}
$$
Then $p \mid a_2$, and
$$
f(p) \equiv a_1 p+a_0 \quad\left(\bmod p^3\right)
$$
But we see that
$$
f(x)=(-1)^{p-1} f(p-x) \text { for any } x,
$$
so if $p$ is odd,
$$
f(p)=f(0)=a_0,
$$
So it follows that:
$$
0=f(p)-a_0 \equiv a_1 p \quad\left(\bmod p^3\right)
$$
Therefore,
$$
0 \equiv a_1 \quad\left(\bmod p^2\right) .
$$
Hence,
$$
0 \equiv a_1 \quad(\bmod p) .
$$
Now our sum is just $\frac{a_1}{(p-1) !}=\frac{a}{b}$.
It follows that $p$ divides $a$. This completes the proof.
Qed.