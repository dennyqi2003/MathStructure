Exercise 2022.IB.3-II-13G-a-i Let $U \subset \mathbb{C}$ be a (non-empty) connected open set and let $f_n$ be a sequence of holomorphic functions defined on $U$. Suppose that $f_n$ converges uniformly to a function $f$ on every compact subset of $U$. Show that $f$ is holomorphic in $U$.
Proof.
Let $\Delta \subset D$ be a closed triangle. Since each $f_n$ is holomorphic, by Cauchy's theorem, you have $\int_{\partial \Delta} f_n(z) d z=0$ for all $n$.
$\partial \Delta$ is a compact subset of $D$, so you know that $f_n \rightarrow f$ uniformly on $\partial \Delta$.
So you get, for all $n$,
$$
\left|\int_{\partial \Delta} f(z) d z\right|=\left|\int_{\partial \Delta}\left(f(z)-f_n(z)\right) d z\right| \leq \operatorname{length}(\partial \Delta)
$$
By letting $n \rightarrow \infty$, you find that $\int_{\partial \Delta} f(z) d z=0$.
By Morera's theorem, $f$ is holomorphic.
Qed.