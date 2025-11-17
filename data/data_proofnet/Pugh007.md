Exercise 2.57 Show that if $S$ is connected, it is not true in general that its interior is connected.
Proof.
Consider $X=\mathbb{R}^2$ and
$$
A=([-2,0] \times[-2,0]) \cup([0,2] \times[0,2])
$$
which is connected, while $\operatorname{int}(A)$ is not connected.
To see this consider the continuous function $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ is defined by $f(x, y)=x+y$. Let $U=f^{-1}(0,+\infty)$ which is open in $\mathbb{R}^2$ and so $U \cap \operatorname{int}(A)$ is open in $\operatorname{int}(A)$. Also, since $(0,0) \notin \operatorname{int}(A)$, so for all $(x, y) \in \operatorname{int}(A), f(x, y) \neq 0$ and $U \cap \operatorname{int}(A)=f^{-1}[0,+\infty) \cap \operatorname{int}(A)$ is closed in $\operatorname{int}(A)$. Furthermore, $(1,1)=f^{-1}(2) \in U \cap \operatorname{int}(A)$ shows that $U \cap \operatorname{int}(A) \neq \emptyset$ while $(-1,-1) \in \operatorname{int}(A)$ and $(-1,-1) \notin U$ shows that $U \cap \operatorname{int}(A) \neq \operatorname{int}(A)$.
Qed.