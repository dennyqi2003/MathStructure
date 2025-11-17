Exercise 3.14 Let $p$ and $q$ be distinct odd primes such that $p-1$ divides $q-1$. If $(n, p q)=1$, show that $n^{q-1} \equiv 1(p q)$.
Proof.
As $n \wedge pq = 1, n\wedge p=1, n \wedge q = 1$, so from Fermat's Little Theorem
$$n^{q-1} \equiv 1 \pmod q,\qquad n^{p-1} \equiv 1 \pmod p.$$
$p-1 \mid q-1$, so there exists $k \in \mathbb{Z}$ such that $q-1 = k(p-1)$.
Thus
$$n^{q-1} = (n^{p-1})^k \equiv 1 \pmod p.$$
$p \mid n^{q-1} - 1, q \mid n^{q-1} - 1$, and $p\wedge q = 1$, so $pq \mid n^{q-1} - 1$ :
$$n^{q-1} \equiv 1 \pmod{pq}.$$
Qed.