Exercise 1.1.29 Prove that $A \times B$ is an abelian group if and only if both $A$ and $B$ are abelian.
Proof.
$(\Rightarrow)$ Suppose $a_1, a_2 \in A$ and $b_1, b_2 \in B$. Then
$$
\left(a_1 a_2, b_1 b_2\right)=\left(a_1, b_1\right) \cdot\left(a_2, b_2\right)=\left(a_2, b_2\right) \cdot\left(a_1, b_1\right)=\left(a_2 a_1, b_2 b_1\right) .
$$
Since two pairs are equal precisely when their corresponding entries are equal, we have $a_1 a_2=a_2 a_1$ and $b_1 b_2=b_2 b_1$. Hence $A$ and $B$ are abelian.
$(\Leftarrow)$ Suppose $\left(a_1, b_1\right),\left(a_2, b_2\right) \in A \times B$. Then we have
$$
\left(a_1, b_1\right) \cdot\left(a_2, b_2\right)=\left(a_1 a_2, b_1 b_2\right)=\left(a_2 a_1, b_2 b_1\right)=\left(a_2, b_2\right) \cdot\left(a_1, b_1\right) .
$$
Hence $A \times B$ is abelian.
Qed.