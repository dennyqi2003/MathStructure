Exercise 5.5 Suppose $f$ is defined and differentiable for every $x>0$, and $f^{\prime}(x) \rightarrow 0$ as $x \rightarrow+\infty$. Put $g(x)=f(x+1)-f(x)$. Prove that $g(x) \rightarrow 0$ as $x \rightarrow+\infty$.
Proof.
Let $\varepsilon>0$. Choose $x_0$ such that $\left|f^{\prime}(x)\right|<\varepsilon$ if $x>x_0$. Then for any $x \geq x_0$ there exists $x_1 \in(x, x+1)$ such that
$$
f(x+1)-f(x)=f^{\prime}\left(x_1\right) .
$$
Since $\left|f^{\prime}\left(x_1\right)\right|<\varepsilon$, it follows that $|f(x+1)-f(x)|<\varepsilon$, as required.
Qed.