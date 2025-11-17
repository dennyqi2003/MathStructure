Exercise 2020.b5 For $j \in\{1,2,3,4\}$, let $z_{j}$ be a complex number with $\left|z_{j}\right|=1$ and $z_{j} \neq 1$. Prove that $3-z_{1}-z_{2}-z_{3}-z_{4}+z_{1} z_{2} z_{3} z_{4} \neq 0 .$
Proof.
It will suffice to show that for any $z_1, z_2, z_3, z_4 \in \mathbb{C}$ of modulus 1 such that $|3-z_1-z_2-z_3-z_4| = |z_1z_2z_3z_4|$, at least one of $z_1, z_2, z_3$ is equal to 1.

To this end, let $z_1=e^{\alpha i}, z_2=e^{\beta i}, z_3=e^{\gamma i}$ and 
\[
f(\alpha, \beta, \gamma)=|3-z_1-z_2-z_3|^2-|1-z_1z_2z_3|^2.
\]
 A routine calculation shows that 
\begin{align*}
f(\alpha, \beta, \gamma)&=
10 - 6\cos(\alpha) - 6\cos(\beta) - 6\cos(\gamma) \\
&\quad + 2\cos(\alpha + \beta + \gamma) + 2\cos(\alpha - \beta) \\
&\quad + 2\cos(\beta - \gamma) + 2\cos(\gamma - \alpha).
\end{align*}
Since the function $f$ is continuously differentiable, and periodic in each variable, $f$ has a maximum and a minimum and it attains these values only at points where $\nabla f=(0,0,0)$.  A routine calculation now shows that 
\begin{align*}
\frac{\partial f}{\partial \alpha} + \frac{\partial f}{\partial \beta} + \frac{\partial f}{\partial \gamma} &=
6(\sin(\alpha) +\sin(\beta)+\sin(\gamma)-  \sin(\alpha + \beta + \gamma)) \\
&=
24\sin\left(\frac{\alpha+\beta}{2}\right) \sin\left(\frac{\beta+\gamma}{2}\right)
\sin\left(\frac{\gamma+\alpha}{2}\right).
\end{align*}
Hence every critical point of $f$ must satisfy one of $z_1z_2=1$, $z_2z_3=1$, or $z_3z_1=1$. By symmetry, let us assume that $z_1z_2=1$. Then 
\[
f = |3-2\mathrm{Re}(z_1)-z_3|^2-|1-z_3|^2;
\]
since $3-2\mathrm{Re}(z_1)\ge 1$, $f$ is nonnegative and can be zero only if the real part of $z_1$, and hence also $z_1$ itself, is equal to $1$.
Qed.