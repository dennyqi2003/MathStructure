Exercise 3.8 Suppose that $V$ is finite dimensional and that $T \in \mathcal{L}(V, W)$. Prove that there exists a subspace $U$ of $V$ such that $U \cap \operatorname{null} T=\{0\}$ and range $T=\{T u: u \in U\}$.
Proof.
The point here is to note that every subspace of a vector space has a complementary subspace.
In this example, $U$ will precisely turn out to be the complementary subspace of null $T$. That is, $V=U \oplus \operatorname{null} T$
How should we characterize $U$ ? This can be achieved by extending a basis $B_1=\left\{v_1, v_2, \ldots, v_m\right\}$ of null $T$ to a basis of $V$. Let $B_2=\left\{u_1, u_2, \ldots, u_n\right\}$ be such that $B=B_1 \cup B_2$ is a basis of $V$.

Define $U=\operatorname{span}\left(B_2\right)$. Now, since $B_1$ and $B_2$ are complementary subsets of the basis $B$ of $V$, their spans will turn out to be complementary subspaces of $V$. Let's prove that $V=U \oplus$ null $T$.

Let $v \in V$. Then, $v$ can be expressed as a linear combination of the vectors in $B$.
Let $v=a_1 u_1+\cdots+a_n u_n+c_1 v_1+\cdots+c_m v_m$. However, since $\left\{u_1, u_2, \ldots, u_n\right\}$ is a basis of $U, a_1 u_1+$ $\cdots+a_n u_n=u \in U$ and since $\left\{v_1, v_2, \ldots, v_m\right\}$ is a basis of null $T, c_1 v_1+\cdots+c_m v_m=w \in$ null $T$.
Hence, $v=u+w \in U+\operatorname{null} T$. This shows that
$$
V=U+\operatorname{null} T
$$
Now, let $v \in U \cap \operatorname{null} T$.
Since $v \in U, u$ can be expressed as a linear combination of basis vectors of $U$. Let
$$
v=a_1 u_1+\cdots+a_n u_n
$$
Similarly, since $v \in \operatorname{null} T$, it can also be expressed as a tinear combination of the basis vectors of null $T$. Let
$$
v=c_1 v_1+\cdots+c_m v_m
$$
The left hand sides of the above two equations are equal. Therefore, we can equate the right hand sides.
$$
\begin{aligned}
& a_1 u_1+\cdots+a_n u_n=v=c_1 v_1+\cdots+c_m v_m \\
& a_1 u_1+\cdots+a_n u_n-c_1 v_1-\cdots-c_m v_m=0
\end{aligned}
$$
We have found a linear combination of $u_i^{\prime}$ 's and $v_i$ 's which is equal to zero. However, they are basis vectors of $V$. Hence, all the multipliers $c_i$ 's and $a_i$ 's must be zero implying that $v=0$.
Therefore, if $v \in U \cap$ null $T$, then $v=0$. this means that
$$
U \cap \operatorname{null} T=\{0\}
$$
The above shows that $U$ satisfies the first of the required conditions.
Now let $w \in$ range $T$. Then, there exists $v \in V$ such that $T v=w$. This allows us to write $v=u+w$ where $u \in U$ and $w \in$ null $T$. This implies
$$
\begin{aligned}
w & =T v \\
& =T(u+w) \\
& =T u+T w \\
& =T u+0 \quad \quad(\text { since } w \in \operatorname{null} T) \\
& =T u
\end{aligned}
$$
This shows that if $w \in$ range $T$ then $w=T u$ for some $u \in U$. Therefore, range $T \subseteq\{T u \mid u \in U\}$.
Since $U$ is a subspace of $V$, it follows that $T u \in$ range $T$ for all $u \in U$. Thus, $\{T u \mid u \in U\} \subseteq$ range $T$.
Therefore, range $T=\{T u \mid u \in U\}$.
This shows that $U$ satisfies the second required condition as well.
Qed.