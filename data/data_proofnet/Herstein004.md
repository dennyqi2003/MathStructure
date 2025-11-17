Exercise 2.1.27 If $G$ is a finite group, prove that there is an integer $m > 0$ such that $a^m = e$ for all $a \in G$.
Proof.
Let $n_1, n_2, \ldots, n_k$ be the orders of all $k$ elements of $G=$ $\left\{a_1, a_2, \ldots, a_k\right\}$. Let $m=\operatorname{lcm}\left(n_1, n_2, \ldots, n_k\right)$. Then, for any $i=$ $1, \ldots, k$, there exists an integer $c$ such that $m=n_i c$. Thus
$$
a_i^m=a_i^{n_i c}=\left(a_i^{n_i}\right)^c=e^c=e
$$
Hence $m$ is a positive integer such that $a^m=e$ for all $a \in G$.
Qed.