Exercise 9.4.2d Prove that $\frac{(x+2)^p-2^p}{x}$, where $p$ is an odd prime, is irreducible in $\mathbb{Z}[x]$.
Proof.
$\frac{(x+2)^p-2^p}{x} \quad \quad p$ is on add pprime $Z[x]$
$$
\frac{(x+2)^p-2^p}{x} \quad \text { as a polynomial we expand }(x+2)^p
$$
$2^p$ cancels with $-2^p$, every remaining term has $x$ as $a$ factor
$$
\begin{aligned}
& x^{p-1}+2\left(\begin{array}{l}
p \\
1
\end{array}\right) x^{p-2}+2^2\left(\begin{array}{l}
p \\
2
\end{array}\right) x^{p-3}+\ldots+2^{p-1}\left(\begin{array}{c}
p \\
p-1
\end{array}\right) \\
& 2^k\left(\begin{array}{l}
p \\
k
\end{array}\right) x^{p-k-1}=2^k \cdot p \cdot(p-1) \ldots(p-k-1), \quad 0<k<p
\end{aligned}
$$
Every lower order coef. has $p$ as a factor but doesnt have $\$ \mathrm{p}^{\wedge} 2 \$$ as a fuction so the polynomial is irreducible by Eisensteins Criterion.
Qed.