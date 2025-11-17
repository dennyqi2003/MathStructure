Exercise 4.8 Let $p$ be an odd prime. Show that $a$ is a primitive root modulo $p$ iff $a^{(p-1) / q} \not \equiv 1(p)$ for all prime divisors $q$ of $p-1$.
Proof.
$\bullet$ If $a$ is a primitive root, then $a^k \not \equiv 1$ for all $k, 1\leq k < p-1$, so $a^{(p-1)/q} \not \equiv 1 \pmod p$ for all prime divisors $q$ of $p - 1$.

$\bullet$ In the other direction, suppose $a^{(p-1)/q} \not \equiv 1 \pmod p$ for all prime divisors $q$ of $p - 1$.

Let $\delta$ the order of $a$, and $p-1 = q_1^{a_1}q_2^{a_2}\cdots q_k^{a_k}$ the decomposition of $p-1$ in prime factors. As $\delta \mid p-1, \delta = q_1^{b_1}p_2^{b_2}\cdots q_k^{b_k}$, with $b_i \leq a_i, i=1,2,\ldots,k$. If $b_i < a_i$ for some index $i$, then $\delta \mid (p-1)/q_i$, so $a^{(p-1)/q_i} \equiv 1 \pmod p$, which is in contradiction with the hypothesis. Thus $b_i = a_i$ for all $i$, and $\delta = q-1$ : $a$ is a primitive root modulo $p$.
Qed.