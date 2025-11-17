Exercise 23.9 Let $A$ be a proper subset of $X$, and let $B$ be a proper subset of $Y$. If $X$ and $Y$ are connected, show that $(X \times Y)-(A \times B)$ is connected.
Proof.
This is similar to the proof of Theorem 23.6. Take $c \times d \in(X \backslash A) \times(Y \backslash B)$. For each $x \in X \backslash A$, the set
$$
U_x=(X \times\{d\}) \cup(\{x\} \times Y)
$$
is connected since $X \times\{d\}$ and $\{x\} \times Y$ are connected and have the common point $x \times d$. Then $U=\bigcup_{x \in X \backslash A} U_x$ is connected because it is the union of the connected spaces $U_x$ which have the point $c \times d$ in common. Similarly, for each $y \in Y \backslash B$ the set
$$
V_y=(X \times\{y\}) \cup(\{c\} \times Y)
$$
is connected, so $V=\bigcup_{y \in Y \backslash B} V_y$ is connected. Thus $(X \times Y) \backslash(A \times B)=U \cup V$ is connected since $c \times d$ is a common point of $U$ and $V$.
Qed.