Exercise 1.4 Prove that if $a \in \mathbf{F}$, $v \in V$, and $av = 0$, then $a = 0$ or $v = 0$.
Proof.
If $a=0$, then we immediately have our result. So suppose $a \neq 0$. Then, because $a$ is some nonzero real or complex number, it has a multiplicative inverse $\frac{1}{a}$. Now suppose that $v$ is some vector such that
$$
a v=0
$$
Multiply by $\frac{1}{a}$ on both sides of this equation to get
$$
\begin{aligned}
\frac{1}{a}(a v) & =\frac{1}{a} 0 & & \\
\frac{1}{a}(a v) & =0 & & \\
\left(\frac{1}{a} \cdot a\right) v & =0 & & \text { (associativity) } \\
1 v & =0 & & \text { (definition of } 1/a) \\
v & =0 & & \text { (multiplicative identity) }
\end{aligned}
$$
Hence either $a=0$ or, if $a \neq 0$, then $v=0$.
Qed.