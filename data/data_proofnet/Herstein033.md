Exercise 4.3.1 If $R$ is a commutative ring and $a \in R$, let $L(a) = \{x \in R \mid xa = 0\}$. Prove that $L(a)$ is an ideal of $R$.
Proof.
First, note that if $x \in L(a)$ and $y \in L(a)$ then $x a=0$ and $y a=0$, so that
$$
\begin{aligned}
x a-y a & =0 \\
(x-y) a & =0,
\end{aligned}
$$
i.e. $L(a)$ is an additive subgroup of $R$. (We have used the criterion that $H$ is a subgroup of $G$ if for any $h_1, h_2 \in H$ we have that $h_1 h_2^{-1} \in H$. 

Now we prove the conclusion. Let $r \in R$ and $b \in L(a)$, then $b a=0$, and so $x b a=0$ which by associativity of multiplication in $R$ is equivalent to
$$
(x b) a=0,
$$
so that $x b \in L(a)$. Since $R$ is commutative, (1) implies that $(bx)a=0$, so that $b x \in L(a)$, which concludes the proof that $L(a)$ is an ideal.
Qed.