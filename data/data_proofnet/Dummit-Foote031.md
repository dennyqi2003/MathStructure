Exercise 3.2.16 Use Lagrange's Theorem in the multiplicative group $(\mathbb{Z} / p \mathbb{Z})^{\times}$to prove Fermat's Little Theorem: if $p$ is a prime then $a^{p} \equiv a(\bmod p)$ for all $a \in \mathbb{Z}$.
Proof.
Solution: If $p$ is prime, then $\varphi(p)=p-1$ (where $\varphi$ denotes the Euler totient). Thus
$$
\mid\left((\mathbb{Z} /(p))^{\times} \mid=p-1 .\right.
$$
So for all $a \in(\mathbb{Z} /(p))^{\times}$, we have $|a|$ divides $p-1$. Hence
$$
a=1 \cdot a=a^{p-1} a=a^p \quad(\bmod p) .
$$
Qed.