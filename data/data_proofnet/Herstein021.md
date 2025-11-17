Exercise 2.8.15 Prove that if $p > q$ are two primes such that $q \mid p - 1$, then any two nonabelian groups of order $pq$ are isomorphic.
Proof.
For a nonabelian group of order $p q$, the structure of the group $G$ is set by determining the relation $a b a^{-1}=b^{k^{\frac{p-1}{q}}}$ for some generator $k$ of the cyclic group. Here we are using the fact that $k^{\frac{p-1}{q}}$ is a generator for the unique subgroup of order $q$ in $U_p$ (a cyclic group of order $m$ has a unique subgroup of order $d$ for each divisor $d$ of $m$ ). The other possible generators of this subgroup are $k^{\frac{l(p-1)}{q}}$ for each $1 \leq l \leq q-1$, so these give potentially new group structures. Let $G^{\prime}$ be a group with an element $c$ of order $q$, an element $d$ of order $p$ with structure defined by the relation $c d c^{-1}=d^{k^{\frac{l(p-1)}{q}}}$. We may then define
$$
\begin{aligned}
\phi: G^{\prime} & \rightarrow G \\
c & \mapsto a^l \\
d & \mapsto b
\end{aligned}
$$
since $c$ and $a^l$ have the same order and $b$ and $d$ have the same order this is a well defined function.
Since
$$
\begin{aligned}
\phi(c) \phi(d) \phi(c)^{-1} & =a^l b a^{-l} \\
& =b^{\left(k^{\frac{p-1}{q}}\right)^l} \\
& =b^{k^{\frac{l(p-1)}{q}}} \\
& =\phi(d)^{k^{\frac{l(p-1)}{q}}}
\end{aligned}
$$
$\phi\left(c^i d^j\right)=a^{l i} b^j=e$ only if $i=j=0$, so $\phi$ is 1-to-l. Therefore $G$ and $G^{\prime}$ are isomorphic and so up to isomorphism there is only one nonabelian group of order $p q$.
Qed.