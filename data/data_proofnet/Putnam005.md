Exercise 2017.b3 Suppose that $f(x)=\sum_{i=0}^{\infty} c_{i} x^{i}$ is a power series for which each coefficient $c_{i}$ is 0 or 1 . Show that if $f(2 / 3)=3 / 2$, then $f(1 / 2)$ must be irrational.
Proof.
Suppose by way of contradiction that $f(1/2)$ is rational. Then $\sum_{i=0}^{\infty} c_i 2^{-i}$ is the binary expansion of a rational number, and hence must be eventually periodic; that is, there exist some integers $m,n$ such that
$c_i = c_{m+i}$ for all $i \geq n$. We may then write
\[
f(x) = \sum_{i=0}^{n-1} c_i x^i + \frac{x^n}{1-x^m} \sum_{i=0}^{m-1} c_{n+i} x^i.
\]
Evaluating at $x = 2/3$, we may equate $f(2/3) = 3/2$ with 
\[
\frac{1}{3^{n-1}} \sum_{i=0}^{n-1} c_i 2^i 3^{n-i-1} + \frac{2^n 3^m}{3^{n+m-1}(3^m-2^m)} \sum_{i=0}^{m-1} c_{n+i} 2^i 3^{m-1-i};
\]
since all terms on the right-hand side have odd denominator, the same must be true of the sum, a contradiction.
Qed.