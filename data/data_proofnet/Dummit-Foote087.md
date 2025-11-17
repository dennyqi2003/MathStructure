Exercise 11.1.13 Prove that as vector spaces over $\mathbb{Q}, \mathbb{R}^n \cong \mathbb{R}$, for all $n \in \mathbb{Z}^{+}$.
Proof.
Since $B$ is a basis of $V$, every element of $V$ can be written uniquely as a finite linear combination of elements of $B$. Let $X$ be the set of all such finite linear combinations. Then $X$ has the same cardinality as $V$, since the map from $X$ to $V$ that takes each linear combination to the corresponding element of $V$ is a bijection.

We will show that $X$ has the same cardinality as $B$. Since $B$ is countable and $X$ is a union of countable sets, it suffices to show that each set $X_n$, consisting of all finite linear combinations of $n$ elements of $B$, is countable.

Let $P_n(X)$ be the set of all subsets of $X$ with cardinality $n$. Then we have $X_n \subseteq P_n(B)$. Since $B$ is countable, we have $\mathrm{card}(P_n(B)) \leq \mathrm{card}(B^n) = \mathrm{card}(B)$, where $B^n$ is the Cartesian product of $n$ copies of $B$.

Thus, we have $\mathrm{card}(X_n) \leq \mathrm{card}(P_n(B)) \leq \mathrm{card}(B)$, so $X_n$ is countable. It follows that $X$ is countable, and hence has the same cardinality as $B$.

Therefore, we have shown that the cardinality of $V$ is equal to the cardinality of $B$. Since $F$ is countable, it follows that the cardinality of $V$ is countable as well.

Now let $Q$ be a countable field, and let $R$ be a vector space over $Q$. Let $n$ be a positive integer. Then any basis of $R^n$ over $Q$ has the same cardinality as $R^n$, which is countable. Since $R$ is a direct sum of $n$ copies of $R^n$, it follows that any basis of $R$ over $Q$ has the same cardinality as $R$. Hence, the cardinality of $R$ is countable.

Finally, since $R$ is a countable vector space and $Q$ is a countable field, it follows that $R$ and $Q^{\oplus \mathrm{card}(R)}$ are isomorphic as additive abelian groups. Therefore, we have $R \cong_Q Q^{\oplus \mathrm{card}(R)}$, and in particular $R \cong_Q R^n$ for any positive integer $n$.
Qed.