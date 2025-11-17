Exercise 18.8a Let $Y$ be an ordered set in the order topology. Let $f, g: X \rightarrow Y$ be continuous. Show that the set $\{x \mid f(x) \leq g(x)\}$ is closed in $X$.
Proof.
We prove that $U=\{x \mid g(x)<f(x)\}$ is open in $X$. Let $a \in U$, so that $g(a)<f(a)$. If there is an element $c$ between $g(a)$ and $f(a)$, then $a \in g^{-1}((-\infty, c)) \cap f^{-1}((c,+\infty))$. If there are no elements between $g(a)$ and $f(a)$, then $a \in g^{-1}\left((-\infty, f(a)) \cap f^{-1}((g(a),+\infty))\right.$. Note that all these preimages are open since $f$ and $g$ are continuous. Thus $U=V \cup W$, where
$$
V=\bigcup_{c \in X} g^{-1}((-\infty, c)) \cap f^{-1}((c,+\infty)) \quad \text { and } \quad W=\bigcup_{\substack{g(a)<f(a) \\(g(a), f(a))=\emptyset}} g^{-1}\left((-\infty, f(a)) \cap f^{-1}((g(a),+\infty))\right.
$$
are open in $X$. So $U$ is open in $X$ and therefore $X \backslash U=\{x \mid f(x) \leq g(x)\}$ is closed in $X$.
Qed.