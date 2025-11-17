Exercise 5.15 Suppose $a \in R^{1}, f$ is a twice-differentiable real function on $(a, \infty)$, and $M_{0}, M_{1}, M_{2}$ are the least upper bounds of $|f(x)|,\left|f^{\prime}(x)\right|,\left|f^{\prime \prime}(x)\right|$, respectively, on $(a, \infty)$. Prove that $M_{1}^{2} \leq 4 M_{0} M_{2} .$
Proof.
The inequality is obvious if $M_0=+\infty$ or $M_2=+\infty$, so we shall assume that $M_0$ and $M_2$ are both finite. We need to show that
$$
\left|f^{\prime}(x)\right| \leq 2 \sqrt{M_0 M_2}
$$
for all $x>a$. We note that this is obvious if $M_2=0$, since in that case $f^{\prime}(x)$ is constant, $f(x)$ is a linear function, and the only bounded linear function is a constant, whose derivative is zero. Hence we shall assume from now on that $0<M_2<+\infty$ and $0<M_0<+\infty$.
Following the hint, we need only choose $h=\sqrt{\frac{M_0}{M_2}}$, and we obtain
$$
\left|f^{\prime}(x)\right| \leq 2 \sqrt{M_0 M_2},
$$
which is precisely the desired inequality.
The case of equality follows, since the example proposed satisfies
$$
f(x)=1-\frac{2}{x^2+1}
$$
for $x \geq 0$. We see easily that $|f(x)| \leq 1$ for all $x>-1$. Now $f^{\prime}(x)=\frac{4 x}{\left(x^2+1\right)^2}$ for $x>0$ and $f^{\prime}(x)=4 x$ for $x<0$. It thus follows from Exercise 9 above that $f^{\prime}(0)=0$, and that $f^{\prime}(x)$ is continuous. Likewise $f^{\prime \prime}(x)=4$ for $x<0$ and $f^{\prime \prime}(x)=\frac{4-4 x^2}{\left(x^2+1\right)^3}=-4 \frac{x^2-1}{\left(x^2+1\right)^3}$. This shows that $\left|f^{\prime \prime}(x)\right|<4$ for $x>0$ and also that $\lim _{x \rightarrow 0} f^{\prime \prime}(x)=4$. Hence Exercise 9 again implies that $f^{\prime \prime}(x)$ is continuous and $f^{\prime \prime}(0)=4$.

On $n$-dimensional space let $\mathbf{f}(x)=\left(f_1(x), \ldots, f_n(x)\right), M_0=\sup |\mathbf{f}(x)|$, $M_1=\sup \left|\mathbf{f}^{\prime}(x)\right|$, and $M_2=\sup \left|\mathbf{f}^{\prime \prime}(x)\right|$. Just as in the numerical case, there is nothing to prove if $M_2=0$ or $M_0=+\infty$ or $M_2=+\infty$, and so we assume $0<M_0<+\infty$ and $0<M_2<\infty$. Let $a$ be any positive number less than $M_1$, let $x_0$ be such that $\left|\mathbf{f}^{\prime}\left(x_0\right)\right|>a$, and let $\mathbf{u}=\frac{1}{\left|\mathbf{f}^{\prime}\left(x_0\right)\right|} \mathbf{f}^{\prime}\left(x_0\right)$. Consider the real-valued function $\varphi(x)=\mathrm{u} \cdot \mathrm{f}(x)$. Let $N_0, N_1$, and $N_2$ be the suprema of $|\varphi(x)|,\left|\varphi^{\prime}(x)\right|$, and $\left|\varphi^{\prime \prime}(x)\right|$ respectively. By the Schwarz inequality we have (since $|\mathbf{u}|=1) N_0 \leq M_0$ and $N_2 \leq M_2$, while $N_1 \geq \varphi\left(x_0\right)=\left|\mathbf{f}^{\prime}\left(x_0\right)\right|>a$. We therefore have $a^2<4 N_0 N_2 \leq 4 M_0 M_2$. Since $a$ was any positive number less than $M_1$, we have $M_1^2 \leq 4 M_0 M_2$, i.e., the result holds also for vector-valued functions.

Equality can hold on any $R^n$, as we see by taking $\mathbf{f}(x)=(f(x), 0, \ldots, 0)$ or $\mathbf{f}(x)=(f(x), f(x), \ldots, f(x))$, where $f(x)$ is a real-valued function for which equality holds.
Qed.