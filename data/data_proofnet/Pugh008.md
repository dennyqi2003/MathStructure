Exercise 2.92 Give a direct proof that the nested decreasing intersection of nonempty covering compact sets is nonempty.
Proof.
Let
$$
A_1 \supset A_2 \supset \cdots \supset A_n \supset \cdots
$$
be a nested decreasing sequence of compacts. Suppose that $\bigcap A_n=\emptyset$. Take $U_n=A_n^c$, then
$$
\bigcup U_n=\bigcup A_n^c=\left(\bigcap A_n\right)^c=A_1 .
$$
Here, I'm thinking of $A_1$ as the main metric space. Since $\left\{U_n\right\}$ is an open covering of $A_1$, we can extract a finite subcovering, that is,
$$
A_{\alpha_1}^c \cup A_{\alpha_2}^c \cup \cdots \cup A_{\alpha_m}^c \supset A_1
$$
or
$$
\left(A_1 \backslash A_{\alpha_1}\right) \cup\left(A_1 \backslash A_{\alpha_2}\right) \cup \cdots \cup\left(A_1 \backslash A_{\alpha_m}\right) \supset A_1 .
$$
But, this is true only if $A_{\alpha_i}=\emptyset$ for some $i$, a contradiction.
Qed.