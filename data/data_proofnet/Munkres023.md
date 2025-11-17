Exercise 21.8 Let $X$ be a topological space and let $Y$ be a metric space. Let $f_{n}: X \rightarrow Y$ be a sequence of continuous functions. Let $x_{n}$ be a sequence of points of $X$ converging to $x$. Show that if the sequence $\left(f_{n}\right)$ converges uniformly to $f$, then $\left(f_{n}\left(x_{n}\right)\right)$ converges to $f(x)$.
Proof.
Let $d$ be the metric on $Y$. Let $V$ be a neighbourhood of $f(x)$, and let $\varepsilon>0$ be such that $f(x) \in B_d(f(x), \varepsilon) \subset V$. Since $\left(f_n\right)_n$ converges uniformly to $f$, there exists $N_1 \in \mathbb{Z}_{+}$such that $d\left(f_n(x), f(x)\right)<\varepsilon / 2$ for all $x \in X$ and all $n \geq N_1$, so that $d\left(f_n\left(x_n\right), f\left(x_n\right)\right)<\varepsilon / 2$ for all $n \geq N_1$. Moreover, $f$ is continuous, so there exists $N_2 \in \mathbb{Z}_{+}$such that $d\left(f\left(x_n\right), f(x)\right)<\varepsilon / 2$ for all $n \geq N_2$. Thus, if $N>\max \left\{N_1, N_2\right\}$, then
$$
d\left(f_n\left(x_n\right), f(x)\right) \leq d\left(f_n\left(x_n\right), f\left(x_n\right)\right)+d\left(f\left(x_n\right), f(x)\right)<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon
$$
for all $n \geq N$, so $f_n\left(x_n\right) \in V$ for all $n \geq N$. It follows that $\left(f_n\left(x_n\right)\right)_n$ converges to $f(x)$.
Qed.