Exercise 18.8b Let $Y$ be an ordered set in the order topology. Let $f, g: X \rightarrow Y$ be continuous. Let $h: X \rightarrow Y$ be the function $h(x)=\min \{f(x), g(x)\}.$ Show that $h$ is continuous.
Proof.
Let $A=\{x \mid f(x) \leq g(x)\}$ and $B=\{x \mid g(x) \leq f(x)\}$. Then $A$ and $B$ are closed in $X$ by (a), $A \cap B=\{x \mid f(x)=g(x)\}$, and $X=A \cup B$. Since $f$ and $g$ are continuous, their restrictions $f^{\prime}: A \rightarrow Y$ and $g^{\prime}: B \rightarrow Y$ are continuous. It follows from the pasting lemma that
$$
h: X \rightarrow Y, \quad h(x)=\min \{f(x), g(x)\}= \begin{cases}f^{\prime}(x) & \text { if } x \in A \\ g^{\prime}(x) & \text { if } x \in B\end{cases}
$$
is continuous
Qed.