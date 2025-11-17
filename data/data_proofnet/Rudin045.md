Exercise 4.12 A uniformly continuous function of a uniformly continuous function is uniformly continuous.
Proof.
Let $f: X \rightarrow Y$ and $g: Y \rightarrow Z$ be uniformly continuous. Then $g \circ f: X \rightarrow Z$ is uniformly continuous, where $g \circ f(x)=g(f(x))$ for all $x \in X$.
To prove this fact, let $\varepsilon>0$ be given. Then, since $g$ is uniformly continuous, there exists $\eta>0$ such that $d_Z(g(u), g(v))<\varepsilon$ if $d_Y(u, v)<\eta$. Since $f$ is uniformly continuous, there exists $\delta>0$ such that $d_Y(f(x), f(y))<\eta$ if $d_X(x, y)<\delta$

It is then obvious that $d_Z(g(f(x)), g(f(y)))<\varepsilon$ if $d_X(x, y)<\delta$, so that $g \circ f$ is uniformly continuous.
Qed.