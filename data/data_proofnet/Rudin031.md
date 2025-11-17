Exercise 3.20 Suppose $\left\{p_{n}\right\}$ is a Cauchy sequence in a metric space $X$, and some sequence $\left\{p_{n l}\right\}$ converges to a point $p \in X$. Prove that the full sequence $\left\{p_{n}\right\}$ converges to $p$.
Proof.
Let $\varepsilon>0$. Choose $N_1$ so large that $d\left(p_m, p_n\right)<\frac{\varepsilon}{2}$ if $m>N_1$ and $n>N_1$. Then choose $N \geq N_1$ so large that $d\left(p_{n_k}, p\right)<\frac{\varepsilon}{2}$ if $k>N$. Then if $n>N$, we have
$$
d\left(p_n, p\right) \leq d\left(p_n, p_{n_{N+1}}\right)+d\left(p_{n_{N+1}}, p\right)<\varepsilon
$$
For the first term on the right is less than $\frac{\varepsilon}{2}$ since $n>N_1$ and $n_{N+1}>N+1>$ $N_1$. The second term is less than $\frac{\varepsilon}{2}$ by the choice of $N$.
Qed.