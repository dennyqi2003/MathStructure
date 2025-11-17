Exercise 2010.a4 Prove that for each positive integer $n$, the number $10^{10^{10^n}}+10^{10^n}+10^n-1$ is not prime.
Proof.
Put
\[
N = 10^{10^{10^n}} + 10^{10^n} + 10^n - 1.
\]
Write $n = 2^m k$ with $m$ a nonnegative integer and $k$ a positive odd integer.
For any nonnegative integer $j$,
\[
10^{2^m j} \equiv (-1)^j \pmod{10^{2^m} + 1}.
\]
Since $10^n \geq n \geq 2^m \geq m+1$, $10^n$ is divisible by $2^n$ and hence by $2^{m+1}$,
and similarly $10^{10^n}$ is divisible by $2^{10^n}$ and hence by $2^{m+1}$. It follows that
\[
N \equiv 1 + 1 + (-1) + (-1) \equiv 0 \pmod{10^{2^m} + 1}.
\]
Since $N \geq 10^{10^n} > 10^n + 1 \geq 10^{2^m} + 1$, it follows that $N$ is composite.
Qed.