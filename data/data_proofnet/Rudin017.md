Exercise 2.24 Let $X$ be a metric space in which every infinite subset has a limit point. Prove that $X$ is separable.
Proof.
We observe that if the process of constructing $x_j$ did not terminate, the result would be an infinite set of points $x_j, j=1,2, \ldots$, such that $d\left(x_i, x_j\right) \geq \delta$ for $i \neq j$. It would then follow that for any $x \in X$, the open ball $B_{\frac{\delta}{2}}(x)$ contains at most one point of the infinite set, hence that no point could be a limit point of this set, contrary to hypothesis. Hence $X$ is totally bounded, i.e., for each $\delta>0$ there is a finite set $x_1, \ldots, x_{N\delta}$such that $X=\bigcup_{j / 1}^{N\delta} B_\delta\left(x_j\right)$

Let $x_{n_1}, \ldots, x_{n N_n}$ be such that $X=\bigcup_{j / 1}^{N_n} B_{\frac{1}{n}}\left(x_{n j}\right), n=1,2, \ldots$ We claim that $\left\{x_{n j}: 1 \leq j \leq N_n ; n=1,2, \ldots\right\}$ is a countable dense subset of $X$. Indeed
25
if $x \in X$ and $\delta>0$, then $x \in B_{\frac{1}{n}}\left(x_{n j}\right)$ for some $x_{n j}$ for some $n>\frac{1}{\delta}$, and hence $d\left(x, x_{n j}\right)<\delta$. By definition, this means that $\left\{x_{n j}\right\}$ is dense in $X$.
Qed.