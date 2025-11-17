Exercise 8.3.6a Prove that the quotient ring $\mathbb{Z}[i] /(1+i)$ is a field of order 2.
Proof.
Let $a+b i \in \mathbb{Z}[i]$. If $a \equiv b \bmod 2$, then $a+b$ and $b-a$ are even and $(1+i)\left(\frac{a+b}{2}+\frac{b-a}{2} i\right)=a+b i \in\langle 1+i\rangle$. If $a \not \equiv b \bmod 2$ then $a-1+b i \in\langle 1+i\rangle$. Therefore every element of $\mathbb{Z}[i]$ is in either $\langle 1+i\rangle$ or $1+\langle 1+i\rangle$, so $\mathbb{Z}[i] /\langle 1+i\rangle$ is a finite ring of order 2 , which must be a field.
Qed.