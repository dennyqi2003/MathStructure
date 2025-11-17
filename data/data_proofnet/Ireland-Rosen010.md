Exercise 3.10 If $n$ is not a prime, show that $(n-1) ! \equiv 0(n)$, except when $n=4$.
Proof.
Suppose that $n >1$ is not a prime. Then $n = uv$, where $2 \leq u \leq v \leq n-1$.

$\bullet$ If $u \neq v$, then $n = uv \mid (n-1)! = 1\times 2 \times\cdots \times u \times\cdots \times v \times \cdots \times (n-1)$ (even if $u\wedge v \neq 1$ !).

$\bullet$ If $u=v$, $n = u^2$ is a square.

If $u$ is not prime, $u =st,\ 2\leq s \leq t \leq u-1 \leq n-1$, and $n = u' v'$, where $u' =s,v' =st^2$ verify  $2 \leq u' < v' \leq n-1$. As in the first case, $n = u'v' \mid (n-1)!$.  

If $u = p$ is a prime, then $n =p^2$.

In the case $p = 2$, $n = 4$ and $n=4  \nmid (n-1)! = 6$. In the other case $p >2$, and $(n-1)! = (p^2 - 1)!$ contains the factors $p < 2p < p^2$, so $p^2 \mid (p^2-1)!, n \mid (n-1)!$.

Conclusion : if $n$ is not a prime, $(n - 1)! \equiv 0 \pmod n$, except when $n=4$.
Qed.