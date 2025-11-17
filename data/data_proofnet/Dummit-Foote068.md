Exercise 7.2.12 Let $G=\left\{g_{1}, \ldots, g_{n}\right\}$ be a finite group. Prove that the element $N=g_{1}+g_{2}+\ldots+g_{n}$ is in the center of the group ring $R G$.
Proof.
Let $M=\sum_{i=1}^n r_i g_i$ be an element of $R[G]$. Note that for each $g_i \in G$, the action of $g_i$ on $G$ by conjugation permutes the subscripts. Then we have the following.
$$
\begin{aligned}
N M &=\left(\sum_{i=1}^n g_i\right)\left(\sum_{j=1}^n r_j g_j\right) \\
&=\sum_{j=1}^n \sum_{i=1}^n r_j g_i g_j \\
&=\sum_{j=1}^n \sum_{i=1}^n r_j g_j g_j^{-1} g_i g_j \\
&=\sum_{j=1}^n r_j g_j\left(\sum_{i=1}^n g_j^{-1} g_i g_j\right) \\
&=\sum_{j=1}^n r_j g_j\left(\sum_{i=1}^n g_i\right) \\
&=\left(\sum_{j=1}^n r_j g_j\right)\left(\sum_{i=1}^n g_i\right) \\
&=M N .
\end{aligned}
$$
Thus $N \in Z(R[G])$.
Qed.