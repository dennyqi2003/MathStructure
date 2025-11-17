Exercise 26.11 Let $X$ be a compact Hausdorff space. Let $\mathcal{A}$ be a collection of closed connected subsets of $X$ that is simply ordered by proper inclusion. Then $Y=\bigcap_{A \in \mathcal{A}} A$ is connected.
Proof.
Since each $A \in \mathcal{A}$ is closed, $Y$ is closed. Suppose that $C$ and $D$ form a separation of $Y$. Then $C$ and $D$ are closed in $Y$, hence closed in $X$. Since $X$ is compact, $C$ and $D$ are compact by Theorem 26.2. Since $X$ is Hausdorff, by Exercise 26.5, there exist $U$ and $V$ open in $X$ and disjoint containing $C$ and $D$, respectively. We show that
$$
\bigcap_{A \in \mathcal{A}}(A \backslash(U \cup V))
$$
is not empty. Let $\left\{A_1, \ldots, A_n\right\}$ be a finite subcollection of elements of $\mathcal{A}$. We may assume that $A_i \subsetneq A_{i+1}$ for all $i=1, \ldots, n-1$. Then
$$
\bigcap_{i=1}^n\left(A_i \backslash(U \cup V)\right)=A_1 \backslash(U \cup V) \text {. }
$$
Suppose that $A_1 \backslash(U \cup V)=\emptyset$. Then $A_1 \subset U \cup V$. Since $A_1$ is connected and $U \cap V=\emptyset, A_1$ lies within either $U$ or $V$, say $A_1 \subset U$. Then $Y \subset A_1 \subset U$, so that $C=Y \cap C \subset Y \cap V=\emptyset$, contradicting the fact that $C$ and $D$ form a separation of $Y$. Hence, $\bigcap_{i=1}^n\left(A_i \backslash(U \cup V)\right)$ is non-empty. Therefore, the collection $\{A \backslash(U \cup V) \mid A \in \mathcal{A}\}$ has the finite intersection property, so
$$
\bigcap_{A \in \mathcal{A}}(A \backslash(U \cup V))=\left(\bigcap_{A \in \mathcal{A}} A\right) \backslash(U \cup V)=Y \backslash(U \cup V)
$$
is non-empty. So there exists $y \in Y$ such that $y \notin U \cup V \supset C \cup D$, contradicting the fact that $C$ and $D$ form a separation of $Y$. We conclude that there is no such separation, so that $Y$ is connected.
Qed.