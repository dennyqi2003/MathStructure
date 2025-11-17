Exercise 1.1.34 If $x$ is an element of infinite order in $G$, prove that the elements $x^{n}, n \in \mathbb{Z}$ are all distinct.
Proof.
Solution: Suppose to the contrary that $x^a=x^b$ for some $0 \leq a<b \leq n-1$. Then we have $x^{b-a}=1$, with $1 \leq b-a<n$. However, recall that $n$ is by definition the least integer $k$ such that $x^k=1$, so we have a contradiction. Thus all the $x^i$, $0 \leq i \leq n-1$, are distinct. In particular, we have
$$
\left\{x^i \mid 0 \leq i \leq n-1\right\} \subseteq G,
$$
so that $|x|=n \leq|G|$
Qed.