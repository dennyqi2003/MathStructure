Exercise 4.1.34 Let $T$ be the group of $2\times 2$ matrices $A$ with entries in the field $\mathbb{Z}_2$ such that $\det A$ is not equal to 0. Prove that $T$ is isomorphic to $S_3$, the symmetric group of degree 3.
Proof.
The order of $T$ is $2^4-2^3-2^2+2=6$; we now find those six matrices:
$$
\begin{array}{ll}
A_1=\left(\begin{array}{ll}
1 & 0 \\
0 & 1
\end{array}\right), & A_2=\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right) \\
A_3=\left(\begin{array}{ll}
1 & 0 \\
1 & 1
\end{array}\right), & A_4=\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right) \\
A_5=\left(\begin{array}{ll}
0 & 1 \\
1 & 1
\end{array}\right), & A_6=\left(\begin{array}{ll}
1 & 1 \\
1 & 0
\end{array}\right)
\end{array}
$$
with orders $1,2,2,2,3,3$ respectively.
Note that $S_3$ is composed of elements
$$
\text{ id, (1 2), (1 3), (2 3), (1 2 3), (1 3 2)} 
$$
with orders 1, 2, 2, 2, 3, 3 respectively. Also note that, by Problem 17 of generate $S_3$. We also have that $\left(\begin{array}{llll}1 & 3 & 2\end{array}\right)=\left(\begin{array}{llll}1 & 2 & 3\end{array}\right)\left(\begin{array}{lll}1 & 2 & 3\end{array}\right)$, that $\left(\begin{array}{lll}1 & 3\end{array}\right)=\left(\begin{array}{lll}1 & 2 & 3\end{array}\right)\left(\begin{array}{ll}1 & 2\end{array}\right)$, $\left(\begin{array}{ll}1 & 2\end{array}\right)\left(\begin{array}{lll}1 & 2 & 3\end{array}\right)=\left(\begin{array}{ll}2 & 3\end{array}\right)$ and $\left(\begin{array}{lll}1 & 2\end{array}\right)\left(\begin{array}{ll}1 & 2\end{array}\right)=\mathrm{id}$

Now we can check that $\tau\left(A_2\right)=\left(\begin{array}{ll}1 & 2\end{array}\right), \tau\left(A_5\right)=\left(\begin{array}{lll}1 & 2 & 3\end{array}\right)$ induces an isomorphism. We compute
$$
\begin{aligned}
& \tau\left(A_1\right)=\tau\left(A_2 A_2\right)=\tau\left(A_2\right) \tau\left(A_2\right)=\mathrm{id} \\
& \tau\left(A_3\right)=\tau\left(A_5 A_2\right)=\tau\left(A_5\right) \tau\left(A_2\right)=\left(\begin{array}{llll}
1 & 2 & 3
\end{array}\right)\left(\begin{array}{lll}
1 & 2
\end{array}\right)=\left(\begin{array}{ll}
1 & 3
\end{array}\right) \\
& \tau\left(A_4\right)=\tau\left(A_2 A_5\right)=\tau\left(A_2\right) \tau\left(A_5\right)=\left(\begin{array}{lll}
1 & 2
\end{array}\right)\left(\begin{array}{lll}
1 & 2 & 3
\end{array}\right)=\left(\begin{array}{ll}
2 & 3
\end{array}\right) \\
& \tau\left(A_6\right)=\tau\left(A_5 A_5\right)=\tau\left(A_5\right) \tau\left(A_5\right)=\left(\begin{array}{lll}
1 & 3 & 2
\end{array}\right)
\end{aligned}
$$
Thus we see that $\tau$ extendeds to an isomorphism, since $A_2$ and $A_5$ generate $T$, so that $\tau\left(A_i A_j\right)=\tau\left(A_i\right) \tau\left(A_j\right)$ follows from writing $A_i$ and $A_j$ in terms of $A_2$ and $A_5$ and using the equlities and relations shown above.
Qed.