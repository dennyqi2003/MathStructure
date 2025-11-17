Exercise 33.8 Let $X$ be completely regular, let $A$ and $B$ be disjoint closed subsets of $X$. Show that if $A$ is compact, there is a continuous function $f \colon X \rightarrow [0, 1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.
Proof.
Since $X$ is completely regular $\forall a \in A, \exists f_a: X \rightarrow[0,1]: f_a(a)=0$ and $f_a(B)=\{1\}$. For some $\epsilon_a \in(0,1)$ we have that $U_a:=f_a^{-1}([0, \epsilon))$ is an open neighborhood of $a$ that does not intersect $B$. We therefore have an open covering $\left\{U_a \mid a \in A\right\}$ of $A$, so since $A$ is compact we have a finite subcover $\left\{U_{a_i} \mid 1 \leq i \leq m\right\}$. For each $1 \leq i \leq m$ define
$$
\begin{aligned}
\tilde{f}_{a_i}: X & \rightarrow[0,1] \\
x & \mapsto \frac{\max \left(f_{a_i}(x), \epsilon_{a_i}\right)-\epsilon_{a_i}}{1-\epsilon_{a_i}}
\end{aligned}
$$
so that $\forall x \in U_{a_i}: \tilde{f}_{a_i}(x)=0$ and $\forall x \in B, \forall 1 \leq i \leq m: \tilde{f}_{a_i}(x)=1$, and define $f:=$ $\prod_{i=1}^m \tilde{f}_{a_i}$. Then since $A \subset \cup_{i=1}^m U_{a_i}$ we have that $f(A)=\{0\}$ and also we have $f(B)=\{1\}$.
Qed.