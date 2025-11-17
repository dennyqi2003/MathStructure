Exercise 8.3.6b Let $q \in \mathbb{Z}$ be a prime with $q \equiv 3 \bmod 4$. Prove that the quotient ring $\mathbb{Z}[i] /(q)$ is a field with $q^{2}$ elements.
Proof.
The division algorithm gives us that every element of $\mathbb{Z}[i] /\langle q\rangle$ is represented by an element $a+b i$ such that $0 \leq a, b<q$. Each such choice is distinct since if $a_1+b_1 i+\langle q\rangle=a_2+b_2 i+\langle q\rangle$, then $\left(a_1-a_2\right)+\left(b_1-b_2\right) i$ is divisible by $q$, so $a_1 \equiv a_2 \bmod q$ and $b_1 \equiv b_2 \bmod q$. So $\mathbb{Z}[i] /\langle q\rangle$ has order $q^2$.

Since $q \equiv 3 \bmod 4, q$ is irreducible, hence prime in $\mathbb{Z}[i]$. Therefore $\langle q\rangle$ is a prime ideal in $\mathbb{Z}[i]$, and so $\mathbb{Z}[i] /\langle q\rangle$ is an integral domain. So $\mathbb{Z}[i] /\langle q\rangle$ is a field.
Qed.