Exercise 3.5 For any two real sequences $\left\{a_{n}\right\},\left\{b_{n}\right\}$, prove that $\limsup _{n \rightarrow \infty}\left(a_{n}+b_{n}\right) \leq \limsup _{n \rightarrow \infty} a_{n}+\limsup _{n \rightarrow \infty} b_{n},$ provided the sum on the right is not of the form $\infty-\infty$.
Proof.
Since the case when $\limsup _{n \rightarrow \infty} a_n=+\infty$ and $\limsup _{n \rightarrow \infty} b_n=-\infty$ has been excluded from consideration, we note that the inequality is obvious if $\limsup _{n \rightarrow \infty} a_n=+\infty$. Hence we shall assume that $\left\{a_n\right\}$ is bounded above.

Let $\left\{n_k\right\}$ be a subsequence of the positive integers such that $\lim _{k \rightarrow \infty}\left(a_{n_k}+\right.$ $\left.b_{n_k}\right)=\limsup _{n \rightarrow \infty}\left(a_n+b_n\right)$. Then choose a subsequence of the positive integers $\left\{k_m\right\}$ such that
$$
\lim _{m \rightarrow \infty} a_{n_{k_m}}=\limsup _{k \rightarrow \infty} a_{n_k} .
$$
The subsequence $a_{n_{k_m}}+b_{n_{k_m}}$ still converges to the same limit as $a_{n_k}+b_{n_k}$, i.e., to $\limsup _{n \rightarrow \infty}\left(a_n+b_n\right)$. Hence, since $a_{n_k}$ is bounded above (so that $\limsup _{k \rightarrow \infty} a_{n_k}$ is finite), it follows that $b_{n_{k_m}}$ converges to the difference
$$
\lim _{m \rightarrow \infty} b_{n_{k_m}}=\lim _{m \rightarrow \infty}\left(a_{n_{k_m}}+b_{n_{k_m}}\right)-\lim _{m \rightarrow \infty} a_{n_{k_m}} .
$$
Thus we have proved that there exist subsequences $\left\{a_{n_{k_m}}\right\}$ and $\left\{b_{n_{k_m}}\right\}$ which converge to limits $a$ and $b$ respectively such that $a+b=\limsup _{n \rightarrow \infty}\left(a_n+b_n^*\right)$. Since $a$ is the limit of a subsequence of $\left\{a_n\right\}$ and $b$ is the limit of a subsequence of $\left\{b_n\right\}$, it follows that $a \leq \limsup _{n \rightarrow \infty} a_n$ and $b \leq \limsup _{n \rightarrow \infty} b_n$, from which the desired inequality follows.
Qed.