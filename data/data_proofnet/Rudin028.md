Exercise 3.7 Prove that the convergence of $\Sigma a_{n}$ implies the convergence of $\sum \frac{\sqrt{a_{n}}}{n}$ if $a_n\geq 0$.
Proof.
Since $\left(\sqrt{a_n}-\frac{1}{n}\right)^2 \geq 0$, it follows that
$$
\frac{\sqrt{a_n}}{n} \leq \frac{1}{2}\left(a_n^2+\frac{1}{n^2}\right) .
$$
Now $\Sigma a_n^2$ converges by comparison with $\Sigma a_n$ (since $\Sigma a_n$ converges, we have $a_n<1$ for large $n$, and hence $\left.a_n^2<a_n\right)$. Since $\Sigma \frac{1}{n^2}$ also converges ($p$ series, $p=2$ ), it follows that $\Sigma \frac{\sqrt{a_n}}{n}$ converges.
Qed.