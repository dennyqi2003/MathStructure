Exercise 1.1.15 Prove that $(a_1a_2\dots a_n)^{-1} = a_n^{-1}a_{n-1}^{-1}\dots a_1^{-1}$ for all $a_1, a_2, \dots, a_n\in G$.
Proof.
For $n=1$, note that for all $a_1 \in G$ we have $a_1^{-1}=a_1^{-1}$.
Now for $n \geq 2$ we proceed by induction on $n$. For the base case, note that for all $a_1, a_2 \in G$ we have
$$
\left(a_1 \cdot a_2\right)^{-1}=a_2^{-1} \cdot a_1^{-1}
$$
since
$$
a_1 \cdot a_2 \cdot a_2^{-1} a_1^{-1}=1 .
$$
For the inductive step, suppose that for some $n \geq 2$, for all $a_i \in G$ we have
$$
\left(a_1 \cdot \ldots \cdot a_n\right)^{-1}=a_n^{-1} \cdot \ldots \cdot a_1^{-1} .
$$
Then given some $a_{n+1} \in G$, we have
$$
\begin{aligned}
\left(a_1 \cdot \ldots \cdot a_n \cdot a_{n+1}\right)^{-1} &=\left(\left(a_1 \cdot \ldots \cdot a_n\right) \cdot a_{n+1}\right)^{-1} \\
&=a_{n+1}^{-1} \cdot\left(a_1 \cdot \ldots \cdot a_n\right)^{-1} \\
&=a_{n+1}^{-1} \cdot a_n^{-1} \cdot \ldots \cdot a_1^{-1},
\end{aligned}
$$
using associativity and the base case where necessary.
Qed.