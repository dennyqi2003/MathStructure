Exercise 4.24 Assume that $f$ is a continuous real function defined in $(a, b)$ such that $f\left(\frac{x+y}{2}\right) \leq \frac{f(x)+f(y)}{2}$ for all $x, y \in(a, b)$. Prove that $f$ is convex.
Proof.
We shall prove that
$$
f(\lambda x+(1-\lambda) y) \leq \lambda f(x)+(1-\lambda) f(y)
$$
for all "dyadic rational" numbers, i.e., all numbers of the form $\lambda=\frac{k}{2^n}$, where $k$ is a nonnegative integer not larger than $2^n$. We do this by induction on $n$. The case $n=0$ is trivial (since $\lambda=0$ or $\lambda=1$ ). In the case $n=1$ we have $\lambda=0$ or $\lambda=1$ or $\lambda=\frac{1}{2}$. The first two cases are again trivial, and the third is precisely the hypothesis of the theorem. Suppose the result is proved for $n \leq r$, and consider $\lambda=\frac{k}{2^{r+1}}$. If $k$ is even, say $k=2 l$, then $\frac{k}{2^{r+1}}=\frac{l}{2^r}$, and we can appeal to the induction hypothesis. Now suppose $k$ is odd. Then $1 \leq k \leq 2^{r+1}-1$, and so the numbers $l=\frac{k-1}{2}$ and $m=\frac{k+1}{2}$ are integers with $0 \leq l<m \leq 2^r$. We can now write
$$
\lambda=\frac{s+t}{2},
$$
where $s=\frac{k-1}{2^{r+1}}=\frac{l}{2^r}$ and $t=\frac{k+1}{2^{r+1}}=\frac{m}{2^r}$. We then have
$$
\lambda x+(1-\lambda) y=\frac{[s x+(1-s) y]+[t x+(1-t) y]}{2}
$$
Hence by the hypothesis of the theorem and the induction hypothesis we have
$$
\begin{aligned}
f(\lambda x+(1-\lambda) y) & \leq \frac{f(s x+(1-s) y)+f(t x+(1-t) y)}{2} \\
& \leq \frac{s f(x)+(1-s) f(y)+t f(x)+(1-t) f(y)}{2} \\
&=\left(\frac{s+t}{2}\right) f(x)+\left(1-\frac{s+t}{2}\right) f(y) \\
&=\lambda f(x)+(1-\lambda) f(y)
\end{aligned}
$$
This completes the induction.
Now for each fixed $x$ and $y$ both sides of the inequality
$$
f(\lambda x+(1-\lambda) y) \leq \lambda f(x)+(1-\lambda) f(y)
$$
are continuous functions of $\lambda$. Hence the set on which this inequality holds (the inverse image of the closed set $[0, \infty)$ under the mapping $\lambda \mapsto \lambda f(x)+(1-$ $\lambda) f(y)-f(\lambda x+(1-\lambda) y))$ is a closed set. Since it contains all the points $\frac{k}{2^n}$, $0 \leq k \leq n, n=1,2, \ldots$, it must contain the closure of this set of points, i.e., it must contain all of $[0,1]$. Thus $f$ is convex.
Qed.