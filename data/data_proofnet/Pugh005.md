Exercise 2.41 Let $\|\cdot\|$ be any norm on $\mathbb{R}^{m}$ and let $B=\left\{x \in \mathbb{R}^{m}:\|x\| \leq 1\right\}$. Prove that $B$ is compact.
Proof.
Let us call $\|\cdot\|_E$ the Euclidean norm in $\mathbb{R}^m$. We start by claiming that there exist constants $C_1, C_2>0$ such that
$$
C_1\|x\|_E \leq\|x\| \leq C_2\|x\|_E, \forall x \in \mathbb{R}^m .
$$
Assuming (1) to be true, let us finish the problem. First let us show that $B$ is bounded w.r.t. $d_E$, which is how we call the Euclidean distance in $\mathbb{R}^m$. Indeed, given $x \in B,\|x\|_E \leq \frac{1}{C_1}\|x\| \leq \frac{1}{C_1}$. Hence $B \subset\left\{x \in \mathbb{R}^m: d_E(x, 0)<\frac{1}{C_1}+1\right\}$, which means $B$ is bounded w.r.t $d_E$.
Now let us show that $B$ is closed w.r.t. $d_E$. Let $x_n \rightarrow x$ w.r.t. $d_E$, where $x_n \in B$. Notice that this implies that $x_n \rightarrow x$ w.r.t. $d(x, y)=\|x-y\|$, the distance coming from $\|\cdot\|$, since by (1) we have
$$
d\left(x_n, x\right)=\left\|x_n-x\right\| \leq C_2\left\|x_n-x\right\|_E \rightarrow 0 .
$$
Also, notice that
$$
\|x\| \leq\left\|x_n-x\right\|+\left\|x_n\right\| \leq\left\|x_n-x\right\|+1,
$$
hence passing to the limit we obtain that $\|x\| \leq 1$, therefore $x \in B$ and so $B$ is closed w.r.t. $d_E$. Since $B$ is closed and bounded w.r.t. $d_E$, it must be compact. Now we claim that the identity function, $i d:\left(\mathbb{R}^m, d_E\right) \rightarrow\left(\mathbb{R}^m, d\right)$ where $\left(\mathbb{R}^m, d_E\right)$ means we are using the distance $d_E$ in $\mathbb{R}^m$ and $\left(\mathbb{R}^m, d\right)$ means we are using the distance $d$ in $\mathbb{R}^m$, is a homeomorphism. This follows by (1), since $i d$ is always a bijection, and it is continuous and its inverse is continuous by (1) (if $x_n \rightarrow x$ w.r.t. $d_E$, then $x_n \rightarrow x$ w.r.t. $d$ and vice-versa, by (1)). By a result we saw in class, since $B$ is compact in $\left(\mathbb{R}^m, d_E\right)$ and $i d$ is a homeomorphism, then $i d(B)=B$ is compact w.r.t. $d$.

We are left with proving (1). Notice that it suffices to prove that $C_1 \leq\|x\| \leq$ $C_2, \forall x \in \mathbb{R}^m$ with $\|x\|_E=1$. Indeed, if this is true, given $x \in \mathbb{R}^m$, either $\|x\|_E=0$ (which implies $x=0$ and (1) holds in this case), or $x /\|x\|_E=y$ is such that $\|y\|_E=1$, so $C_1 \leq\|y\| \leq C_2$, which implies $C_1\|x\|_E \leq\|x\| \leq C_2\|x\|_E$.
We want to show now that $\|\cdot\|$ is continuous w.r.t. $d_E$, that is, given $\varepsilon>0$ and $x \in \mathbb{R}^m$, there exists $\delta>0$ such that if $d_E(x, y)<\delta$, then $\|\mid x\|-\|y\| \|<\varepsilon$.

By the triangle inequality, $\|x\|-\|y\| \leq\|x-y\|$, and $\|y\|-\|x\| \leq\|x-y\|$, therefore
$$
|\|x||-\| y|\|\leq\| x-y \| .
$$
Writing now $x=\sum_{i=1}^m a_i e_i, y=\sum_{i=1}^m b_i e_i$, where $e_i=(0, \ldots, 1,0, \ldots, 0)$ (with 1 in the i-th component), we obtain by the triangle inequality,
$$
\begin{aligned}
\|x-y\| & =\left\|\sum_{i=1}^m\left(a_i-b_i\right) e_i\right\| \leq \sum_{i=1}^m\left|a_i-b_i\left\|\left|\left\|e_i\right\| \leq \max _{i=1, \ldots, m}\left\|e_i\right\| \sum_{i=1}^m\right| a_i-b_i \mid\right.\right. \\
& =\max _{i=1, \ldots, m}\left\|e_i\right\| d_{s u m}(x, y) \leq \max _{i=1, \ldots, m}\left\|e_i\right\| m d_{\max }(x, y) \\
& \leq \max _{i=1, \ldots, m}\left\|e_i\right\| m d_E(x, y) .
\end{aligned}
$$
Let $\delta=\frac{\varepsilon}{m \max _{i=1, \ldots, m}\left\|e_i\right\|}$. Then if $d_E(x, y)<\delta,\|x\|-\|y\|||<\varepsilon$.
Since $\|\cdot\|$ is continuous w.r.t. $d_E$ and $K=\left\{x \in \mathbb{R}^m:\|x\|_E=1\right\}$ is compact w.r.t. $d_E$, then the function $\|\cdot\|$ achieves a maximum and a minimum value on $K$. Call $C_1=\min _{x \in K}\|x\|, C_2=\max _{x \in K}\|x\|$. Then
$$
C_1 \leq\|x\| \leq C_2, \forall x \in \mathbb{R}^m \text { such that }\|x\|_E=1,
$$
which is what we needed.
Qed.