Exercise 6.13 Suppose $\left(e_{1}, \ldots, e_{m}\right)$ is an or thonormal list of vectors in $V$. Let $v \in V$. Prove that $\|v\|^{2}=\left|\left\langle v, e_{1}\right\rangle\right|^{2}+\cdots+\left|\left\langle v, e_{m}\right\rangle\right|^{2}$ if and only if $v \in \operatorname{span}\left(e_{1}, \ldots, e_{m}\right)$.
Proof.
If $v \in \operatorname{span}\left(e_1, \ldots, e_m\right)$, it means that
$$
v=\alpha_1 e_1+\ldots+\alpha_m e_m .
$$
for some scalars $\alpha_i$. We know that $\alpha_k=\left\langle v, e_k\right\rangle, \forall k \in\{1, \ldots, m\}$. Therefore,
$$
\begin{aligned}
\|v\|^2 & =\langle v, v\rangle \\
& =\left\langle\alpha_1 e_1+\ldots+\alpha_m e_m, \alpha_1 e_1+\ldots+\alpha_m e_m\right\rangle \\
& =\left|\alpha_1\right|^2\left\langle e_1, e_1\right\rangle+\ldots+\left|\alpha_m\right|^2\left\langle e_m, e_m\right\rangle \\
& =\left|\alpha_1\right|^2+\ldots+\left|\alpha_m\right|^2 \\
& =\left|\left\langle v, e_1\right\rangle\right|^2+\ldots+\left|\left\langle v, e_m\right\rangle\right|^2 .
\end{aligned}
$$
$\Rightarrow$ Assume that $v \notin \operatorname{span}\left(e_1, \ldots, e_m\right)$. Then, we must have
$$
v=v_{m+1}+\frac{\left\langle v, v_0\right\rangle}{\left\|v_0\right\|^2} v_0,
$$
where $v_0=\alpha_1 e_1+\ldots+\alpha_m e_m, \alpha_k=\left\langle v, e_k\right\rangle, \forall k \in\{1, \ldots, m\}$, and $v_{m+1}=v-$ $\frac{\left\langle v, v_0\right\rangle}{\left\|v_0\right\|^2} v_0 \neq 0$.

We have $\left\langle v_0, v_{m+1}\right\rangle=0$ (from which we get $\left\langle v, v_0\right\rangle=\left\langle v_0, v_0\right\rangle$ and $\left\langle v, v_{m+1}\right\rangle=$ $\left.\left\langle v_{m+1}, v_{m+1}\right\rangle\right)$. Now,
$$
\begin{aligned}
\|v\|^2 & =\langle v, v\rangle \\
& =\left\langle v, v_{m+1}+\frac{\left\langle v, v_0\right\rangle}{\left\|v_0\right\|^2} v_0\right\rangle \\
& =\left\langle v, v_{m+1}\right\rangle+\left\langle v, \frac{\left\langle v, v_0\right\rangle}{\left\|v_0\right\|^2} v_0\right\rangle \\
& =\left\langle v_{m+1}, v_{m+1}\right\rangle+\frac{\left\langle v_0, v_0\right\rangle}{\left\|v_0\right\|^2}\left\langle v_0, v_0\right\rangle \\
& =\left\|v_{m+1}\right\|^2+\left\|v_0\right\|^2 \\
& >\left\|v_0\right\|^2 \\
& =\left|\alpha_1\right|^2+\ldots+\left|\alpha_m\right|^2 \\
& =\left|\left\langle v, e_1\right\rangle\right|^2+\ldots+\left|\left\langle v, e_m\right\rangle\right|^2 .
\end{aligned}
$$
By contrapositive, if $\left\|v_1\right\|^2=\left|\left\langle v, e_1\right\rangle\right|^2+\ldots+\left|\left\langle v, e_m\right\rangle\right|^2$, then $v \in \operatorname{span}\left(e_1, \ldots, e_m\right)$.
Qed.