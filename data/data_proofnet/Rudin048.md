Exercise 4.21a Suppose $K$ and $F$ are disjoint sets in a metric space $X, K$ is compact, $F$ is closed. Prove that there exists $\delta>0$ such that $d(p, q)>\delta$ if $p \in K, q \in F$.
Proof.
Following the hint, we observe that $\rho_F(x)$ must attain its minimum value on $K$, i.e., there is some point $r \in K$ such that
$$
\rho_F(r)=\min _{q \in K} \rho_F(q) .
$$
Since $F$ is closed and $r \notin F$, it follows from Exercise $4.20$ that $\rho_F(r)>0$. Let $\delta$ be any positive number smaller than $\rho_F(r)$. Then for any $p \in F, q \in K$, we have
$$
d(p, q) \geq \rho_F(q) \geq \rho_F(r)>\delta .
$$
This proves the positive assertion.
Qed.