Exercise 2.9 Let $\Omega$ be a bounded open subset of $\mathbb{C}$, and $\varphi: \Omega \rightarrow \Omega$ a holomorphic function. Prove that if there exists a point $z_{0} \in \Omega$ such that $\varphi\left(z_{0}\right)=z_{0} \quad \text { and } \quad \varphi^{\prime}\left(z_{0}\right)=1$ then $\varphi$ is linear.
Proof.
When $\Omega$ is connected, if $\varphi$ is not linear, then there exists $n \geq 2$ and $a_n \neq 0$, such that
$$
\varphi(z)=z+a_n\left(z-z_0\right)^n+O\left(\left(z-z_0\right)^{n+1}\right) .
$$
As you have noticed, by induction, it follows that for every $k \geq 1$,
$$
\varphi^k(z)=z+k a_n\left(z-z_0\right)^n+O\left(\left(z-z_0\right)^{n+1}\right) .
$$
Let $r>0$ be such that when $\left|z-z_0\right| \leq r$, then $z \in \Omega$. Then by (1),
$$
k a_n=\frac{1}{2 \pi i} \int_{\left|z-z_0\right|=r} \frac{\varphi^k(z)}{\left(z-z_0\right)^{n+1}} d z .
$$
Since $\varphi^k(\Omega) \subset \Omega$ and since $\Omega$ is bounded, there exists $M>0$, independent of $k$, such that $\left|\varphi^k\right| \leq M$ on $\Omega$. Then by (2),
$$
k\left|a_n\right| \leq M r^{-n} .
$$
Since $k$ is arbitrary, $a_n=0$, a contradiction.
Qed.