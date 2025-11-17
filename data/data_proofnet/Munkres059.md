Exercise 38.6 Let $X$ be completely regular. Show that $X$ is connected if and only if the Stone-Čech compactification of $X$ is connected.
Proof.
The closure of a connected set is connected, so if $X$ is connected so is $\beta(X)$
Suppose $X$ is the union of disjoint open subsets $U, V \subset X$. Define the continuous map
$$
\begin{aligned}
& f: X \rightarrow\{0,1\} \\
& x \mapsto \begin{cases}0, & x \in U \\
1, & x \in V\end{cases}
\end{aligned}
$$
By the fact that $\{0,1\}$ is compact and Hausdorff we can extend $f$ to a surjective map $\bar{f}: \beta(X) \rightarrow\{0,1\}$ such that $\bar{f}^{-1}(\{0\})$ and $\bar{f}^{-1}(\{1\})$ are disjoint open sets that cover $\beta(X)$, which makes this space not-connected.
Qed.