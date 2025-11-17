Exercise 3.2.21 If $\sigma, \tau$ are two permutations that disturb no common element and $\sigma \tau = e$, prove that $\sigma = \tau = e$.
Proof.
Note that $\sigma \tau=e$ can equivalentnly be phrased as $\tau$ being the inverse of $\sigma$. Our statement is then equivalent to the statement that an inverse of a nonidentity permutation disturbs at least one same element as that permutation. To prove this, let $\sigma$ be a nonidentity permutation, then let $\left(i_1 \cdots i_n\right)$ be a cycle in $\sigma$. Then we have that
$$
\sigma\left(i_1\right)=i_2, \sigma\left(i_2\right)=i_2, \ldots, \sigma\left(i_{n-1}\right)=i_n, \sigma\left(i_n\right)=i_1,
$$
but then also
$$
i_1=\tau\left(i_2\right), i_2=\tau\left(i_3\right), \ldots, i_{n-1}=\tau\left(i_n\right), i_n=\tau\left(i_1\right),
$$
i.e. its inverse disturbs $i_1, \ldots, i_n$.
Qed.