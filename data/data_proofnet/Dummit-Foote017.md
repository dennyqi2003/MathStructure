Exercise 1.6.11 Let $A$ and $B$ be groups. Prove that $A \times B \cong B \times A$.
Proof.
We know from set theory that the mapping $\varphi: A \times B \rightarrow B \times A$ given by $\varphi((a, b))=(b, a)$ is a bijection with inverse $\psi: B \times A \rightarrow A \times B$ given by $\psi((b, a))=(a, b)$. Also $\varphi$ is a homomorphism, as we show below.
Let $a_1, a_2 \in A$ and $b_1, b_2 \in B$. Then
$$
\begin{aligned}
\varphi\left(\left(a_1, b_1\right) \cdot\left(a_2, b_2\right)\right) &=\varphi\left(\left(a_1 a_2, b_1 b_2\right)\right) \\
&=\left(b_1 b_2, a_1 a_2\right) \\
&=\left(b_1, a_1\right) \cdot\left(b_2, a_2\right) \\
&=\varphi\left(\left(a_1, b_1\right)\right) \cdot \varphi\left(\left(a_2, b_2\right)\right)
\end{aligned}
$$
Hence $A \times B \cong B \times A$.
Qed.