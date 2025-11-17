Exercise 3.1 Assume that $f \colon \mathbb{R} \rightarrow \mathbb{R}$ satisfies $|f(t)-f(x)| \leq|t-x|^{2}$ for all $t, x$. Prove that $f$ is constant.
Proof.
We have $|f(t)-f(x)| \leq|t-x|^2, \forall t, x \in \mathbb{R}$. Fix $x \in \mathbb{R}$ and let $t \neq x$. Then
$$
\left|\frac{f(t)-f(x)}{t-x}\right| \leq|t-x| \text {, hence } \lim _{t \rightarrow x}\left|\frac{f(t)-f(x)}{t-x}\right|=0 \text {, }
$$
so $f$ is differentiable in $\mathbb{R}$ and $f^{\prime}=0$. This implies that $f$ is constant, as seen in class.
Qed.