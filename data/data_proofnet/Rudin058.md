Exercise 5.17 Suppose $f$ is a real, three times differentiable function on $[-1,1]$, such that $f(-1)=0, \quad f(0)=0, \quad f(1)=1, \quad f^{\prime}(0)=0 .$ Prove that $f^{(3)}(x) \geq 3$ for some $x \in(-1,1)$.
Proof.
Following the hint, we observe that Theorem $5.15$ (Taylor's formula with remainder) implies that
$$
\begin{aligned}
f(1) &=f(0)+f^{\prime}(0)+\frac{1}{2} f^{\prime \prime}(0)+\frac{1}{6} f^{(3)}(s) \\
f(-1) &=f(0)-f^{\prime}(0)+\frac{1}{2} f^{\prime \prime}(0)-\frac{1}{6} f^{(3)}(t)
\end{aligned}
$$
for some $s \in(0,1), t \in(-1,0)$. By subtracting the second equation from the first and using the given values of $f(1), f(-1)$, and $f^{\prime}(0)$, we obtain
$$
1=\frac{1}{6}\left(f^{(3)}(s)+f^{(3)}(t)\right),
$$
which is the desired result. Note that we made no use of the hypothesis $f(0)=0$.
Qed.