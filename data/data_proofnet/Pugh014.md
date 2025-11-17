Exercise 4.15a A continuous, strictly increasing function $\mu \colon (0, \infty) \rightarrow (0, \infty)$ is a modulus of continuity if $\mu(s) \rightarrow 0$ as $s \rightarrow 0$. A function $f \colon [a, b] \rightarrow \mathbb{R}$ has modulus of continuity $\mu$ if $|f(s) - f(t)| \leq \mu(|s - t|)$ for all $s, t \in [a, b]$. Prove that a function is uniformly continuous if and only if it has a modulus of continuity.
Proof.
Suppose there exists a modulus of continuity $w$ for $f$, then fix $\varepsilon>0$, since $\lim _{s \rightarrow 0} w(s)=0$, there exists $\delta>0$ such that for any $|s|<\delta$, we have $w(s)<\varepsilon$, then we have for any $x, z \in X$ such that $d_X(x, z)<\delta$, we have $d_Y(f(x), f(z)) \leq w\left(d_X(x, z)\right)<\varepsilon$, which means $f$ is uniformly continuous.

Suppose $f:\left(X, d_X\right) \rightarrow\left(Y, d_Y\right)$ is uniformly continuous.
Let $\delta_1>0$ be such that $d_X(a, b)<\delta_1$ implies $d_Y(f(a), f(b))<1$.
Define $w:[0, \infty) \rightarrow[0, \infty]$ by
$$
w(s)= \begin{cases}\left.\sup \left\{d_Y(f(a), f(b))\right\} \mid d_X(a, b) \leq s\right\} & \text { if } s \leq \delta_1 \\ \infty & \text { if } s>\delta_1\end{cases}
$$
We'll show that $w$ is a modulus of continuity for $f \ldots$
By definition of $w$, it's immediate that $w(0)=0$ and it's clear that
$$
d_Y(f(a), f(b)) \leq w\left(d_X(a, b)\right)
$$
for all $a, b \in X$.
It remains to show $\lim _{s \rightarrow 0^{+}} w(s)=0$.
It's easily seen that $w$ is nonnegative and non-decreasing, hence $\lim _{s \rightarrow 0^{+}}=L$ for some $L \geq 0$, where $L=\inf w((0, \infty))$
Let $\epsilon>0$.
By uniform continuity of $f$, there exists $\delta>0$ such that $d_X(a, b)<\delta$ implies $d_Y(f(a), f(b))<\epsilon$, hence by definition of $w$, we get $w(\delta) \leq \epsilon$.
Thus $L \leq \epsilon$ for all $\epsilon>0$, hence $L=0$.
This completes the proof.
Qed.