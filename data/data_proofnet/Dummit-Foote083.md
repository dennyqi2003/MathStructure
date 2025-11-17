Exercise 9.4.2c Prove that $x^4+4x^3+6x^2+2x+1$ is irreducible in $\mathbb{Z}[x]$.
Proof.
$$
p(x)=x^4+6 x^3+4 x^2+2 x+1
$$
We calculate $p(x-1)$
$$
\begin{aligned}
(x-1)^4 & =x^4-4 x^3+6 x^2-4 x+1 \\
6(x-1)^3 & =6 x^3-18 x^2+18 x-6 \\
4(x-1)^2 & =4 x^2-8 x+4 \\
2(x-1) & =2 x-2 \\
1 & =1
\end{aligned}
$$
$$
\begin{aligned}
& p(x-1)=(x-1)^4+6(x-1)^3+4(x-1)^2+2(x-1)+1=x^4+2 x^3-8 x^2+ \\
& 8 x-2 \\
& q(x)=x^4+2 x^3-8 x^2+8 x-2
\end{aligned}
$$
$q(x)$ is irreducible by Eisenstiens Criterion since the prime $\$ 2 \$$ divides the lower coefficient but $\$ 2^{\wedge} 2 \$$ doesnt divide constant $-2$. Any factorization of $p(x)$ would provide a factor of $p(x)(x-1)$
Since:
$$
\begin{aligned}
& p(x)=a(x) b(x) \\
& q(x)=p(x)(x-1)=a(x-1) b(x-1)
\end{aligned}
$$
We get a contradiction with the irreducibility of $p(x-1)$, so $p(x)$ is irreducible in $Z[x]$
Qed.