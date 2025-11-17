Exercise 26.12 Let $p: X \rightarrow Y$ be a closed continuous surjective map such that $p^{-1}(\{y\})$ is compact, for each $y \in Y$. (Such a map is called a perfect map.) Show that if $Y$ is compact, then $X$ is compact.
Proof.
We first show that if $U$ is an open set containing $p^{-1}(\{y\})$, then there is a neighbourhood $W$ of $y$ such that $p^{-1}(W)$ is contained in $U$. Since $X-U$ is closed in $X$, $p(X-U)$ is closed in $Y$ and does not contain $y$, so $W=Y \backslash p(X \backslash U)$ is a neighbourhood of $y$. Moreover, since $X \backslash U \subset p^{-1}(p(X \backslash U)$ ) (by elementary set theory), we have
$$
p^{-1}(W)=p^{-1}(Y \backslash p(X \backslash U))=p^{-1}(Y) \backslash p^{-1}(p(X \backslash U)) \subset X \backslash(X \backslash U)=U .
$$
Now let $\mathcal{A}$ be an open covering of $X$. For each $y \in Y$, let $\mathcal{A}_y$ be a subcollection of $\mathcal{A}$ such that
$$
p^{-1}(\{y\}) \subset \bigcup_{A \in \mathcal{A}_y} A .
$$
Since $p^{-1}(\{y\})$ is compact, there exists a finite subcollection of $\mathcal{A}_y$ that also covers $p^{-1}(\{y\})$, say $\left\{A_y^1, \ldots, A_y^{n_y}\right\}$. Thus $\bigcup_{i=1}^{n_y} A_y^i$ is open and contains $p^{-1}(\{y\})$, so there exists a neighbourhood $W_y$ of $y$ such that $p^{-1}\left(W_y\right)$ is contained in $\bigcup_{i=1}^{n_y} A_y^i$. Then $\left\{W_y\right\}_{y \in Y}$ is an open covering of $Y$, so there exist $y_1, \ldots, y_k \in Y$ such that $\left\{W_{y_j}\right\}_{j=1}^k$ also covers $Y$. Then
$$
X=p^{-1}(Y) \subset p^{-1}\left(\bigcup_{j=1}^k W_{y_j}\right)=\bigcup_{j=1}^k p^{-1}\left(W_{y_j}\right) \subset \bigcup_{j=1}^k\left(\bigcup_{i=1}^{n_{y_j}} A_{y_j}^i\right)
$$
so
$$
\left\{A_{y_j}^i\right\}_{\substack{j=1, \ldots, k . \\ i=1, \ldots, n_{y_j}}}
$$
is a finite subcollection of $\mathcal{A}$ that also covers $X$. Therefore, $X$ is compact.
Qed.