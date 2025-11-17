Exercise 11.13.3 Prove that there are infinitely many primes congruent to $-1$ (modulo $4$).
Proof.
First we show a lemma: if $a \equiv 3(\bmod 4)$ then there exists a prime $p$ such that $p \mid a$ and $p \equiv 3(\bmod 4)$.

    Clearly, all primes dividing $a$ are odd. Suppose all of them would be $\equiv 1(\bmod 4)$. Then their product would also be $a \equiv 1(\bmod 4)$, which is a contradiction.

To prove the main claim, suppose that $p_1, \ldots, p_n$ would be all such primes. (In particular, we have $p_1=3$.) Consider $a=4 p_2 \cdots p_n+3$. (Or you can take $a=4 p_2 \cdots p_n-1$.) Show that $p_i \nmid a$ for $i=1, \ldots, n$. (The case $3 \nmid a$ is solved differently than the other primes - this is the reason for omitting $p_1$ in the definition of $a$.) Then use the above lemma to get a contradiction.
Qed.