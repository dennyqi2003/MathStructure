Exercise 27.4 Show that a connected metric space having more than one point is uncountable.
Proof.
The distance function $d: X \times X \rightarrow \mathbb{R}$ is continuous by Exercise 20.3(a), so given $x \in X$, the function $d_x: X \rightarrow \mathbb{R}$ given by $d_x(y)=d(x, y)$ is continuous by Exercise 19.11. Since $X$ is connected, the image $d_x(X)$ is a connected subspace of $\mathbb{R}$, and contains 0 since $d_x(x)=0$. Thus, if $y \in X$ and $y \neq x$, then $d_x(X)$ contains the set $[0, \delta]$, where $\delta=d_x(y)>0$. Therefore $X$ must be uncountable.
Qed.