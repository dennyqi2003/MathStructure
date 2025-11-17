Exercise 3.1 Show that there are infinitely many primes congruent to $-1$ modulo 6 .
Proof.
Let $n$ any integer such that $n\geq 3$, and $N = n! -1 =   2 \times 3 \times\cdots\times n - 1 >1$. 

Then $N \equiv -1 \pmod 6$. As $6k +2, 6k +3, 6k +4$ are composite for all integers $k$, every prime factor of $N$ is congruent to $1$ or $-1$ modulo $6$.  If every prime factor of $N$ was congruent to 1, then $N \equiv 1 \pmod 6$ : this is a contradiction because $-1 \not \equiv 1 \pmod 6$.  So there exists a prime factor $p$ of $N$ such that $p\equiv -1 \pmod 6$.

If $p\leq n$, then $p \mid n!$, and $p \mid N = n!-1$, so $p \mid 1$. As $p$ is prime, this is a contradiction, so $p>n$. 

Conclusion :

 for any integer $n$, there exists a prime $p >n$ such that $p \equiv -1 \pmod 6$ : there are infinitely many primes congruent to $-1$ modulo $6$.
Qed.