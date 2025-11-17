Exercise 1.13b Suppose that $f$ is holomorphic in an open set $\Omega$. Prove that if $\text{Im}(f)$ is constant, then $f$ is constant.
Proof.
Let $f(z)=f(x, y)=u(x, y)+i v(x, y)$, where $z=x+i y$.
Since $\operatorname{Im}(f)=$ constant,
$$
\frac{\partial v}{\partial x}=0, \frac{\partial v}{\partial y}=0 .
$$
By the Cauchy-Riemann equations,
$$
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}=0 .
$$
Thus in $\Omega$,
$$
f^{\prime}(z)=\frac{\partial f}{\partial x}=\frac{\partial u}{\partial x}+i \frac{\partial v}{\partial x}=0+0=0 .
$$
Thus $f$ is constant.
Qed.