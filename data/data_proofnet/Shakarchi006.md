Exercise 1.19c Prove that the power series $\sum zn/n$ converges at every point of the unit circle except $z = 1$.
Proof.
If $z=1$ then $\sum z^n / n=\sum 1 / n$ is divergent (harmonic series). If $|z|=1$ and $z \neq 1$, write $z=e^{2 \pi i t}$ with $t \in(0,1)$ and apply Dirichlet's test: if $\left\{a_n\right\}$ is a sequence of real numbers and $\left\{b_n\right\}$ a sequence of complex numbers satisfying
- $a_{n+1} \leq a_n$
- $\lim _{n \rightarrow \infty} a_n=0$
- $\left|\sum_{n=1}^N b_n\right| \leq M$ for every positive integer $N$ and some $M>0$,
then $\sum a_n b_n$ converges. Let $a_n=1 / n$, so $a_n$ satisfies $a_{n+1} \leq a_n$ and $\lim _{n \rightarrow \infty} a_n=0$. Let $b_n=e^{2 \pi i n t}$, then
$$
\left|\sum_{n=1}^N b_n\right|=\left|\sum_{n=1}^N e^{2 \pi i n t}\right|=\left|\frac{e^{2 \pi i t}-e^{2 \pi i(N+1) t}}{1-e^{2 \pi i t}}\right| \leq \frac{2}{\left|1-e^{2 \pi i t}\right|}=M \text { for all } N
$$
Thus $\sum a_n b_n=\sum z^n / n$ converges for every point in the unit circle except $z=1$.
Qed.