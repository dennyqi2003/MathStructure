Exercise 3.63b Prove that $\sum 1/k(\log(k))^p$ diverges when $p \leq 1$.
Proof.
Using the integral test, for a set $a$, we see
$$
\lim _{b \rightarrow \infty} \int_a^b \frac{1}{x \log (x)^c} d x=\lim _{b \rightarrow \infty}\left(\frac{\log (b)^{1-c}}{1-c}-\frac{\log (a)^{1-c}}{1-c}\right)
$$
which goes to infinity if $c \leq 1$ and converges if $c>1$. Thus,
$$
\sum_{n=2}^{\infty} \frac{1}{n \log (n)^c}
$$
converges if and only if $c>1$.
Qed.