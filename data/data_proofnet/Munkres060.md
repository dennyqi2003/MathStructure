Exercise 43.2 Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces; let $Y$ be complete. Let $A \subset X$. Show that if $f \colon A \rightarrow Y$ is uniformly continuous, then $f$ can be uniquely extended to a continuous function $g \colon \bar{A} \rightarrow Y$, and $g$ is uniformly continuous.
Proof.
Let $\left(X, d_X\right)$ and $\left(Y, d_Y\right)$ be metric spaces; let $Y$ be complete. Let $A \subset X$. It is also given that $f: A \longrightarrow X$ is a uniformly continuous function. Then we have to show that $f$ can be uniquely extended to a continuous function $g: \bar{A} \longrightarrow Y$, and $g$ is uniformly coninuous.
We define the function $g$ as follows:
$$
g(x)= \begin{cases}f(x) & \text { if } x \in A \\ \lim _{n \rightarrow \infty} f\left(x_n\right) & \text { if } x \in \bar{A},\end{cases}
$$
where $\left\{x_n\right\} \subset A$ is some sequence in $A$ such that $\lim _{n \rightarrow \infty} x_n=x$. Now we have to check that the above definition is well defined. We first note that since $\left\{x_n\right\} \subset A$ is convergent in $X,\left\{x_n\right\}$ is Cauchy in $A$ and since $f$ is uniformly continuous on $A,\left\{f\left(x_n\right)\right\}$ is Cauchy in $Y$. Further, since $Y$ is complete $\left\{f\left(x_n\right)\right\}$ is convergent. So let us now consider two sequences $\left\{x_n\right\}$ and $\left\{y_n\right\}$ such that $\lim _{n \rightarrow \infty} x_n=\lim _{n \rightarrow \infty} y_n=x$. Then we need to prove that $\lim _{n \rightarrow \infty} f\left(x_n\right)=\lim _{n \rightarrow \infty} f\left(y_n\right)=f(x)$. Let
$$
\lim _{n \rightarrow \infty} f\left(x_n\right)=a \text { and } b=\lim _{n \rightarrow \infty} f\left(y_n\right)
$$
Now since $f$ is uniformly continuous for any given $\epsilon>0$ there exists $\delta>0$ such that
$$
d_Y(f(x), f(y))<\epsilon \text { whenever } d_X(x, y)<\delta \text { and } x, y \in A
$$
So for this $\delta>0$ there exists $N \in \mathbb{N}$ such that
$$
d_X\left(x_n, x\right)<\frac{\delta}{2} \text { and } d_X\left(y_n, x\right)<\frac{\delta}{2}, \text { foe all } n \geq N .
$$
Therefore, we have that for all $n \geq N$,
$$
d_X\left(x_n, y_n\right)<\delta
$$
Thus the equation (1) yields us that
$$
d_Y\left(f\left(x_n\right), f\left(y_n\right)\right)<\epsilon \text { for all } n \geq N .
$$
Now since $\lim _{n \rightarrow \infty} f\left(x_n\right)=a$ and $b=\lim _{n \rightarrow \infty} f\left(y_n\right)$, so for the above $\epsilon>0$ we have a natural number $K \geq N$ such that
$$
\begin{gathered}
d_Y\left(f\left(x_n\right), a\right)<\epsilon \text { for all } n \geq K \text { and } \\
d_Y\left(f\left(y_n\right), b\right)<\epsilon \text { for all } n \geq K .
\end{gathered}
$$
Moreover, since $K \geq N$, from $(2)$ we get
$$
d_Y\left(f\left(x_n\right), f\left(y_n\right)\right)<\epsilon \text { for all } n \geq K .
$$
Now we calculate the following, for $n \geq K$,
$$
\begin{array}{rlr}
d_Y(a, b) & \leq & d_Y\left(a, f\left(x_n\right)\right)+d_Y\left(f\left(x_n\right), f\left(y_n\right)\right)+d\left(f\left(y_n\right), b\right) \\
& < & \epsilon+\epsilon+\epsilon \text { by }(3),(4) \text { and }(5) \\
& = & 3 \epsilon
\end{array}
$$
where the first inequality holds because of triangular inequality. Since $\epsilon>0$ is arbitrary the above calculation shows that $d_Y(a, b)=0$. Thus, the above definition is independent of the choice of the sequence $\left\{x_n\right\}$ and hence the map $g$ is well defined. Moreover, from the construction it follows that $g$ is continuous on $\bar{A}$.
Moreover, we observe that $g$ is unique extension of $f$ by the construction.
So it remains to show that $g$ is uniformly continuous. In order to that we take a Cauchy sequence $\left\{a_n\right\} \subset \bar{A}$. Then since $\bar{A}$ is a closed set so the sequence $\left\{a_n\right\}$ is convergent and hence $\left\{g\left(a_n\right)\right\}$ is also a convergent sequence as $g$ is continuous on $\bar{A}$. So $\left\{g\left(a_n\right)\right\}$ is a Cauchy sequence in $Y$. Since a function is uniformly continuous if and only if it sends Cauchy sequences to Cauchy sequences, we conclude that $g$ is uniformly continuous.
Qed.