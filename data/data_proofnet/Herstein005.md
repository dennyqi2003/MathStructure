Exercise 2.2.3 If $G$ is a group in which $(a b)^{i}=a^{i} b^{i}$ for three consecutive integers $i$, prove that $G$ is abelian.
Proof.
Let $G$ be a group, $a, b \in G$ and $i$ be any integer. Then from given condition,
$$
\begin{aligned}
(a b)^i & =a^i b^i \\
(a b)^{i+1} & =a^{i+1} b^{i+1} \\
(a b)^{i+2} & =a^{i+2} b^{i+2}
\end{aligned}
$$
From first and second, we get
$$
a^{i+1} b^{i+1}=(a b)^i(a b)=a^i b^i a b \Longrightarrow b^i a=a b^i
$$
From first and third, we get
$$
a^{i+2} b^{i+2}=(a b)^i(a b)^2=a^i b^i a b a b \Longrightarrow a^2 b^{i+1}=b^i a b a
$$
This gives
$$
a^2 b^{i+1}=a\left(a b^i\right) b=a b^i a b=b^i a^2 b
$$
Finally, we get
$$
b^i a b a=b^i a^2 b \Longrightarrow b a=a b
$$
This shows that $G$ is Abelian.
Qed.