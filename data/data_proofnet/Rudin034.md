Exercise 4.1a Suppose $f$ is a real function defined on $\mathbb{R}$ which satisfies $\lim_{h \rightarrow 0} f(x + h) - f(x - h) = 0$ for every $x \in \mathbb{R}$. Show that $f$ does not need to be continuous.
Proof.
$$
f(x)= \begin{cases}1 & \text { if } x \text { is an integer } \\ 0 & \text { if } x \text { is not an integer. }\end{cases}
$$
(If $x$ is an integer, then $f(x+h)-f(x-h) \equiv 0$ for all $h$; while if $x$ is not an integer, $f(x+h)-f(x-h)=0$ for $|h|<\min (x-[x], 1+[x]-x)$.
Qed.