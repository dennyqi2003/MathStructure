Exercise 4.4 Consider a prime $p$ of the form $4 t+1$. Show that $a$ is a primitive root modulo $p$ iff $-a$ is a primitive root modulo $p$.
Proof.
Suppose that $a$ is a primitive root modulo $p$. As $p-1$ is even, $(-a)^{p-1}=a^{p-1} \equiv 1$ $(\bmod p)$
If $(-a)^n \equiv 1(\bmod p)$, with $n \in \mathbb{N}$, then $a^n \equiv(-1)^n(\bmod p)$.
Therefore $a^{2 n} \equiv 1(\bmod p)$. As $a$ is a primitive root modulo $p, p-1|2 n, 2 t| n$, so $n$ is even.

Hence $a^n \equiv 1(\bmod p)$, and $p-1 \mid n$. So the least $n \in \mathbb{N}^*$ such that $(-a)^n \equiv 1$ $(\bmod p)$ is $p-1:$ the order of $-a$ modulo $p$ is $p-1,-a$ is a primitive root modulo $p$. Conversely, if $-a$ is a primitive root modulo $p$, we apply the previous result at $-a$ to to obtain that $-(-a)=a$ is a primitive root.
Qed.