Exercise 4.2.8 Prove that if $H$ has finite index $n$ then there is a normal subgroup $K$ of $G$ with $K \leq H$ and $|G: K| \leq n!$.
Proof.
Solution: $G$ acts on the cosets $G / H$ by left multiplication. Let $\lambda: G \rightarrow S_{G / H}$ be the permutation representation induced by this action, and let $K$ be the kernel of the representation.
Now $K$ is normal in $G$, and $K \leq \operatorname{stab}_G(H)=H$. By the First Isomorphism Theorem, we have an injective group homomorphism $\bar{\lambda}: G / K \rightarrow S_{G / H}$. Since $\left|S_{G / H}\right|=n !$, we have $[G: K] \leq n !$.
Qed.