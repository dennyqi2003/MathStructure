Exercise 5.6 Suppose (a) $f$ is continuous for $x \geq 0$, (b) $f^{\prime}(x)$ exists for $x>0$, (c) $f(0)=0$, (d) $f^{\prime}$ is monotonically increasing. Put $g(x)=\frac{f(x)}{x} \quad(x>0)$ and prove that $g$ is monotonically increasing.
Proof.
Put
$$
g(x)=\frac{f(x)}{x} \quad(x>0)
$$
and prove that $g$ is monotonically increasing.
By the mean-value theorem
$$
f(x)=f(x)-f(0)=f^{\prime}(c) x
$$
for some $c \in(0, x)$. Since $f^{\prime}$ is monotonically increasing, this result implies that $f(x)<x f^{\prime}(x)$. It therefore follows that
$$
g^{\prime}(x)=\frac{x f^{\prime}(x)-f(x)}{x^2}>0,
$$
so that $g$ is also monotonically increasing.
Qed.