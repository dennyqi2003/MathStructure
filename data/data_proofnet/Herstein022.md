Exercise 2.9.2 If $G_1$ and $G_2$ are cyclic groups of orders $m$ and $n$, respectively, prove that $G_1 \times G_2$ is cyclic if and only if $m$ and $n$ are relatively prime.
Proof.
The order of $G \times H$ is $n$. $m$. Thus, $G \times H$ is cyclic iff it has an element with order n. $m$. Suppose $\operatorname{gcd}(n . m)=1$. This implies that $g^m$ has order $n$, and analogously $h^n$ has order $m$. That is, $g \times h$ has order $n$. $m$, and therefore $G \times H$ is cyclic.

Suppose now that $\operatorname{gcd}(n . m)>1$. Let $g^k$ be an element of $G$ and $h^j$ be an element of $H$. Since the lowest common multiple of $n$ and $m$ is lower than the product $n . m$, that is, $\operatorname{lcm}(n, m)<n$. $m$, and since $\left(g^k\right)^{l c m(n, m)}=e_G,\left(h^j\right)^{l c m(n, m)}=e_H$, we have $\left(g^k \times h^j\right)^{l c m(n, m)}=e_{G \times H}$. It follows that every element of $G \times H$ has order lower than $n . m$, and therefore $G \times H$ is not cyclic.
Qed.