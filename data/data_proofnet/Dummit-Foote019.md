Exercise 1.6.23 Let $G$ be a finite group which possesses an automorphism $\sigma$ such that $\sigma(g)=g$ if and only if $g=1$. If $\sigma^{2}$ is the identity map from $G$ to $G$, prove that $G$ is abelian.
Proof.
Solution: We define a mapping $f: G \rightarrow G$ by $f(x)=x^{-1} \sigma(x)$.
Claim: $f$ is injective.
Proof of claim: Suppose $f(x)=f(y)$. Then $y^{-1} \sigma(y)=x^{-1} \sigma(x)$, so that $x y^{-1}=\sigma(x) \sigma\left(y^{-1}\right)$, and $x y^{-1}=\sigma\left(x y^{-1}\right)$. Then we have $x y^{-1}=1$, hence $x=y$. So $f$ is injective.

Since $G$ is finite and $f$ is injective, $f$ is also surjective. Then every $z \in G$ is of the form $x^{-1} \sigma(x)$ for some $x$. Now let $z \in G$ with $z=x^{-1} \sigma(x)$. We have
$$
\sigma(z)=\sigma\left(x^{-1} \sigma(x)\right)=\sigma(x)^{-1} x=\left(x^{-1} \sigma(x)\right)^{-1}=z^{-1} .
$$
Thus $\sigma$ is in fact the inversion mapping, and we assumed that $\sigma$ is a homomorphism. By a previous example, then, $G$ is abelian.
Qed.