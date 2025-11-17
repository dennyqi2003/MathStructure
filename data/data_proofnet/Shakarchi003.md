Exercise 1.13c Suppose that $f$ is holomorphic in an open set $\Omega$. Prove that if $|f|$ is constant, then $f$ is constant.
Proof.
Let $f(z)=f(x, y)=u(x, y)+i v(x, y)$, where $z=x+i y$.
We first give a mostly correct argument; the reader should pay attention to find the difficulty. Since $|f|=\sqrt{u^2+v^2}$ is constant,
$$
\left\{\begin{array}{l}
0=\frac{\partial\left(u^2+v^2\right)}{\partial x}=2 u \frac{\partial u}{\partial x}+2 v \frac{\partial v}{\partial x} . \\
0=\frac{\partial\left(u^2+v^2\right)}{\partial y}=2 u \frac{\partial u}{\partial y}+2 v \frac{\partial v}{\partial y} .
\end{array}\right.
$$
Plug in the Cauchy-Riemann equations and we get
$$
\begin{gathered}
u \frac{\partial v}{\partial y}+v \frac{\partial v}{\partial x}=0 \\
-u \frac{\partial v}{\partial x}+v \frac{\partial v}{\partial y}=0 \\
(1.14) \Rightarrow \frac{\partial v}{\partial x}=\frac{v}{u} \frac{\partial v}{\partial y}
\end{gathered}
$$
Plug (1.15) into (1.13) and we get
$$
\frac{u^2+v^2}{u} \frac{\partial v}{\partial y}=0 .
$$
So $u^2+v^2=0$ or $\frac{\partial v}{\partial y}=0$.

If $u^2+v^2=0$, then, since $u, v$ are real, $u=v=0$, and thus $f=0$ which is constant.

Thus we may assume $u^2+v^2$ equals a non-zero constant, and we may divide by it. We multiply both sides by $u$ and find $\frac{\partial v}{\partial y}=0$, then by (1.15), $\frac{\partial v}{\partial x}=0$, and by Cauchy-Riemann, $\frac{\partial u}{\partial x}=0$.
$$
f^{\prime}=\frac{\partial f}{\partial x}=\frac{\partial u}{\partial x}+i \frac{\partial v}{\partial x}=0 .
$$
Thus $f$ is constant.
Why is the above only mostly a proof? The problem is we have a division by $u$, and need to make sure everything is well-defined. Specifically, we need to know that $u$ is never zero. We do have $f^{\prime}=0$ except at points where $u=0$, but we would need to investigate that a bit more.
Let's return to
$$
\left\{\begin{array}{l}
0=\frac{\partial\left(u^2+v^2\right)}{\partial x}=2 u \frac{\partial u}{\partial x}+2 v \frac{\partial v}{\partial x} . \\
0=\frac{\partial\left(u^2+v^2\right)}{\partial y}=2 u \frac{\partial u}{\partial y}+2 v \frac{\partial v}{\partial y} .
\end{array}\right.
$$
Plug in the Cauchy-Riemann equations and we get
$$
\begin{array}{r}
u \frac{\partial v}{\partial y}+v \frac{\partial v}{\partial x}=0 \\
-u \frac{\partial v}{\partial x}+v \frac{\partial v}{\partial y}=0 .
\end{array}
$$
We multiply the first equation $u$ and the second by $v$, and obtain
$$
\begin{aligned}
u^2 \frac{\partial v}{\partial y}+u v \frac{\partial v}{\partial x} & =0 \\
-u v \frac{\partial v}{\partial x}+v^2 \frac{\partial v}{\partial y} & =0 .
\end{aligned}
$$
Adding the two yields
$$
u^2 \frac{\partial v}{\partial y}+v^2 \frac{\partial v}{\partial y}=0,
$$
or equivalently
$$
\left(u^2+v^2\right) \frac{\partial v}{\partial y}=0 .
$$
We now argue in a similar manner as before, except now we don't have the annoying $u$ in the denominator. If $u^2+v^2=0$ then $u=v=0$, else we can divide by $u^2+v^2$ and find $\partial v / \partial y=0$. Arguing along these lines finishes the proof.
Qed.