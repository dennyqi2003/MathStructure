Exercise 30.10 Show that if $X$ is a countable product of spaces having countable dense subsets, then $X$ has a countable dense subset.
Proof.
Let $\left(X_n\right)$ be spaces having countable dense subsets $\left(A_n\right)$. For each $n$, fix an arbitrary $x_n \in X_n$. Consider the subset $A$ of $X$ defined by
$$
A=\bigcup\left\{\prod U_n: U_n=A_n \text { for finitely many } n \text { and is }\left\{x_n\right\} \text { otherwise }\right\} .
$$
This set is countable because the set of finite subsets of $\mathbb{N}$ is countable and each of the inner sets is countable. Now, let $x \in X$ and $V=\prod V_n$ be a basis element containing $x$ such that each $V_n$ is open in $X_n$ and $V_n=X_n$ for all but finitely many $n$. For each $n$, if $V_n \neq X_n$, choose a $y_n \in\left(A_n \cap V_n\right)$ (such a $y_n$ exists since $A_n$ is dense in $\left.X_n\right)$. Otherwise, let $y_n=x_n$. Then $\left(y_n\right) \in(A \cap V)$, proving that $A$ is dense in $X$.
Qed.