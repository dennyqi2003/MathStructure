Exercise 4.4b Let $f$ and $g$ be continuous mappings of a metric space $X$ into a metric space $Y$, and let $E$ be a dense subset of $X$. Prove that if $g(p) = f(p)$ for all $p \in P$ then $g(p) = f(p)$ for all $p \in X$.
Proof.
The function $\varphi: X \rightarrow R^1$ given by
$$
\varphi(p)=d_Y(f(p), g(p))
$$
is continuous, since
$$
\left|d_Y(f(p), g(p))-d_Y(f(q), g(q))\right| \leq d_Y(f(p), f(q))+d_Y(g(p), g(q))
$$
(This inequality follows from the triangle inequality, since
$$
d_Y(f(p), g(p)) \leq d_Y(f(p), f(q))+d_Y(f(q), g(q))+d_Y(g(q), g(p)),
$$
and the same inequality holds with $p$ and $q$ interchanged. The absolute value $\left|d_Y(f(p), g(p))-d_Y(f(q), g(q))\right|$ must be either $d_Y(f(p), g(p))-d_Y(f(q), g(q))$ or $d_Y(f(q), g(q))-d_Y(f(p), g(p))$, and the triangle inequality shows that both of these numbers are at most $d_Y(f(p), f(q))+d_Y(g(p), g(q))$.)
By the previous problem, the zero set of $\varphi$ is closed. But by definition
$$
Z(\varphi)=\{p: f(p)=g(p)\} .
$$
Hence the set of $p$ for which $f(p)=g(p)$ is closed. Since by hypothesis it is dense, it must be $X$.
Qed.