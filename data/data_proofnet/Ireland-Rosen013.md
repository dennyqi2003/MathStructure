Exercise 4.5 Consider a prime $p$ of the form $4 t+3$. Show that $a$ is a primitive root modulo $p$ iff $-a$ has order $(p-1) / 2$.
Proof.
Let $a$ a primitive root modulo $p$.
As $a^{p-1} \equiv 1(\bmod p), p \mid\left(a^{(p-1) / 2}-1\right)\left(a^{(p-1) / 2}+1\right)$, so $p \mid a^{(p-1) / 2}-1$ or $p \mid$ $a^{(p-1) / 2}+1$. As $a$ is a primitive root modulo $p, a^{(p-1) / 2} \not \equiv 1(\bmod p)$, so
$$
a^{(p-1) / 2} \equiv-1 \quad(\bmod p) .
$$
Hence $(-a)^{(p-1) / 2}=(-1)^{2 t+1} a^{(p-1) / 2} \equiv(-1) \times(-1)=1(\bmod p)$.
Suppose that $(-a)^n \equiv 1(\bmod p)$, with $n \in \mathbb{N}$.
Then $a^{2 n}=(-a)^{2 n} \equiv 1(\bmod p)$, so $p-1\left|2 n, \frac{p-1}{2}\right| n$.
So $-a$ has order $(p-1) / 2$ modulo $p$.
Conversely, suppose that $-a$ has order $(p-1) / 2=2 t+1$ modulo $p$. Let $2, p_1, \ldots p_k$ the prime factors of $p-1$, where $p_i$ are odd.
$a^{(p-1) / 2}=a^{2 t+1}=-(-a)^{2 t+1}=-(-a)^{(p-1) / 2} \equiv-1$, so $a^{(p-1) / 2} \not \equiv 1(\bmod 2)$.
As $p-1$ is even, $(p-1) / p_i$ is even, so $a^{(p-1) / p_i}=(-a)^{(p-1) / p_i} \not \equiv 1(\bmod p)($ since $-a$ has order $p-1)$.
So the order of $a$ is $p-1$ (see Ex. 4.8) : $a$ is a primitive root modulo $p$.
Qed.