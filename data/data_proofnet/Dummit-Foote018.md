Exercise 1.6.17 Let $G$ be any group. Prove that the map from $G$ to itself defined by $g \mapsto g^{-1}$ is a homomorphism if and only if $G$ is abelian.
Proof.
$(\Rightarrow)$ Suppose $G$ is abelian. Then
$$
\varphi(a b)=(a b)^{-1}=b^{-1} a^{-1}=a^{-1} b^{-1}=\varphi(a) \varphi(b),
$$
so that $\varphi$ is a homomorphism.
$(\Leftarrow)$ Suppose $\varphi$ is a homomorphism, and let $a, b \in G$. Then
$$
a b=\left(b^{-1} a^{-1}\right)^{-1}=\varphi\left(b^{-1} a^{-1}\right)=\varphi\left(b^{-1}\right) \varphi\left(a^{-1}\right)=\left(b^{-1}\right)^{-1}\left(a^{-1}\right)^{-1}=b a,
$$
so that $G$ is abelian.
Qed.