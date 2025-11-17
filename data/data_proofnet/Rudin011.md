Exercise 1.16a Suppose $k \geq 3, x, y \in \mathbb{R}^k, |x - y| = d > 0$, and $r > 0$. Prove that if $2r > d$, there are infinitely many $z \in \mathbb{R}^k$ such that $|z-x|=|z-y|=r$.
Proof.
(a) Let w be any vector satisfying the following two equations:
$$
\begin{aligned}
\mathbf{w} \cdot(\mathbf{x}-\mathbf{y}) &=0, \\
|\mathbf{w}|^2 &=r^2-\frac{d^2}{4} .
\end{aligned}
$$
From linear algebra it is known that all but one of the components of a solution $\mathbf{w}$ of the first equation can be arbitrary. The remaining component is then uniquely determined. Also, if $w$ is any non-zero solution of the first equation, there is a unique positive number $t$ such that $t$ w satisfies both equations. (For example, if $x_1 \neq y_1$, the first equation is satisfied whenever
$$
z_1=\frac{z_2\left(x_2-y_2\right)+\cdots+z_k\left(x_k-y_k\right)}{y_1-x_1} .
$$
If $\left(z_1, z_2, \ldots, z_k\right)$ satisfies this equation, so does $\left(t z_1, t z_2, \ldots, t z_k\right)$ for any real number $t$.) Since at least two of these components can vary independently, we can find a solution with these components having any prescribed ratio. This ratio does not change when we multiply by the positive number $t$ to obtain a solution of both equations. Since there are infinitely many ratios, there are infinitely many distinct solutions. For each such solution $\mathbf{w}$ the vector $\mathbf{z}=$ $\frac{1}{2} \mathrm{x}+\frac{1}{2} \mathrm{y}+\mathrm{w}$ is a solution of the required equation. For
$$
\begin{aligned}
|\mathrm{z}-\mathbf{x}|^2 &=\left|\frac{\mathbf{y}-\mathbf{x}}{2}+\mathbf{w}\right|^2 \\
&=\left|\frac{\mathbf{y}-\mathbf{x}}{2}\right|^2+2 \mathbf{w} \cdot \frac{\mathbf{x}-\mathbf{y}}{2}+|\mathbf{w}|^2 \\
&=\frac{d^2}{4}+0+r^2-\frac{d^2}{4} \\
&=r^2
\end{aligned}
$$
and a similar relation holds for $|z-y|^2$.
Qed.