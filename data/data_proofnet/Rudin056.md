Exercise 5.7 Suppose $f^{\prime}(x), g^{\prime}(x)$ exist, $g^{\prime}(x) \neq 0$, and $f(x)=g(x)=0$. Prove that $\lim _{t \rightarrow x} \frac{f(t)}{g(t)}=\frac{f^{\prime}(x)}{g^{\prime}(x)}.$
Proof.
Since $f(x)=g(x)=0$, we have
$$
\begin{aligned}
\lim _{t \rightarrow x} \frac{f(t)}{g(t)} &=\lim _{t \rightarrow x} \frac{\frac{f(t)-f(x)}{t-x}}{\frac{g(t)-g(x)}{t-x}} \\
&=\frac{\lim _{t \rightarrow x} \frac{f(t)-f(x)}{t-x}}{\lim _{t \rightarrow x} \frac{g(t)-g(x)}{t-x}} \\
&=\frac{f^{\prime}(x)}{g^{\prime}(x)}
\end{aligned}
$$
Qed.