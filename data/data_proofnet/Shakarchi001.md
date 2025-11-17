Exercise 1.13a Suppose that $f$ is holomorphic in an open set $\Omega$. Prove that if $\text{Re}(f)$ is constant, then $f$ is constant.
Proof.
Let $f(z)=f(x, y)=u(x, y)+i v(x, y)$, where $z=x+i y$.
Since $\operatorname{Re}(f)=$ constant,
$$
\frac{\partial u}{\partial x}=0, \frac{\partial u}{\partial y}=0 .
$$
By the Cauchy-Riemann equations,
$$
\frac{\partial v}{\partial x}=-\frac{\partial u}{\partial y}=0 .
$$
Thus, in $\Omega$,
$$
f^{\prime}(z)=\frac{\partial f}{\partial x}=\frac{\partial u}{\partial x}+i \frac{\partial v}{\partial x}=0+0=0 .
$$
3
Thus $f(z)$ is constant.
Qed.