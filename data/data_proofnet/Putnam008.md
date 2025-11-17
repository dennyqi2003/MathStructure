Exercise 2001.a5 Prove that there are unique positive integers $a, n$ such that $a^{n+1}-(a+1)^n=2001$.
Proof.
Suppose $a^{n+1} - (a+1)^n = 2001$.
Notice that $a^{n+1} + [(a+1)^n - 1]$ is a multiple of $a$; thus
$a$ divides $2002 = 2 \times 7 \times 11 \times 13$.

Since $2001$ is divisible by 3, we must have $a \equiv 1 \pmod{3}$,
otherwise one of $a^{n+1}$ and $(a+1)^n$ is a multiple of 3 and the
other is not, so their difference cannot be divisible by 3. Now
$a^{n+1} \equiv 1 \pmod{3}$, so we must have $(a+1)^n \equiv 1
\pmod{3}$, which forces $n$ to be even, and in particular at least 2.

If $a$ is even, then $a^{n+1} - (a+1)^n \equiv -(a+1)^n \pmod{4}$.
Since $n$ is even, $-(a+1)^n \equiv -1 \pmod{4}$. Since $2001 \equiv 1
\pmod{4}$, this is impossible. Thus $a$ is odd, and so must divide
$1001 = 7 \times 11 \times 13$. Moreover, $a^{n+1} - (a+1)^n \equiv a
\pmod{4}$, so $a \equiv 1 \pmod{4}$.

Of the divisors of $7 \times 11 \times 13$, those congruent to 1 mod 3
are precisely those not divisible by 11 (since 7 and 13 are both
congruent to 1 mod 3). Thus $a$ divides $7 \times 13$. Now
$a \equiv 1 \pmod{4}$ is only possible if $a$ divides $13$.

We cannot have $a=1$, since $1 - 2^n \neq 2001$ for any $n$. Thus
the only possibility is $a = 13$. One easily checks that $a=13, n=2$ is a
solution; all that remains is to check that no other $n$ works. In fact,
if $n > 2$, then $13^{n+1} \equiv 2001 \equiv 1 \pmod{8}$.
But $13^{n+1} \equiv 13 \pmod{8}$ since $n$ is even, contradiction.
Thus $a=13, n=2$ is the unique solution.

Note: once one has that $n$ is even, one can use that $2002
=a^{n+1} + 1 - (a+1)^n$ is divisible by $a+1$ to rule out cases.
Qed.