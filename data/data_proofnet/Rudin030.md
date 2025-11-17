Exercise 3.13 Prove that the Cauchy product of two absolutely convergent series converges absolutely.
Proof.
Since both the hypothesis and conclusion refer to absolute convergence, we may assume both series consist of nonnegative terms. We let $S_n=\sum_{k=0}^n a_n, T_n=\sum_{k=0}^n b_n$, and $U_n=\sum_{k=0}^n \sum_{l=0}^k a_l b_{k-l}$. We need to show that $U_n$ remains bounded, given that $S_n$ and $T_n$ are bounded. To do this we make the convention that $a_{-1}=T_{-1}=0$, in order to save ourselves from having to separate off the first and last terms when we sum by parts. We then have
$$
\begin{aligned}
U_n &=\sum_{k=0}^n \sum_{l=0}^k a_l b_{k-l} \\
&=\sum_{k=0}^n \sum_{l=0}^k a_l\left(T_{k-l}-T_{k-l-1}\right) \\
&=\sum_{k=0}^n \sum_{j=0}^k a_{k-j}\left(T_j-T_{j-1}\right) \\
&=\sum_{k=0}^n \sum_{j=0}^k\left(a_{k-j}-a_{k-j-1}\right) T_j \\
&=\sum_{j=0}^n \sum_{k=j}^n\left(a_{k-j}-a_{k-j-1}\right) T_j
&=\sum_{j=0}^n a_{n-j} T_j \\
&\leq T \sum_{m=0}^n a_m \\
&=T S_n \\
&\leq S T .
\end{aligned}
$$
Thus $U_n$ is bounded, and hence approaches a finite limit.
Qed.