Exercise 5.13 Show that any prime divisor of $x^{4}-x^{2}+1$ is congruent to 1 modulo 12 .
Proof.
\newcommand{\legendre}[2]{\genfrac{(}{)}{}{}{#1}{#2}}
$\bullet$ As $a^6 +1 = (a^2+1)(a^4-a^2+1)$, $p\mid a^4 - a^2+1$ implies $p \mid a^6 + 1$, so $\legendre{-1}{p} = 1$ and $p\equiv 1 \pmod 4$.

$\bullet$ $p \mid 4a^4 - 4 a^2 +4 = (2a-1)^2 + 3$, so $\legendre{-3}{p} = 1$.

As $-3 \equiv 1 \pmod 4$, $\legendre{-3}{p} = \legendre{p}{3}$, so $\legendre{p}{3} = 1$, thus $p \equiv 1 \pmod 3$.

$4 \mid p-1$ and $3 \mid p-1$, thus $12 \mid p-1$ : $$p \equiv 1 \pmod {12}.$$
Qed.