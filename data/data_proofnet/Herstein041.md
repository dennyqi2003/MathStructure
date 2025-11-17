Exercise 5.1.8 If $F$ is a field of characteristic $p \neq 0$, show that $(a + b)^m = a^m + b^m$, where $m = p^n$, for all $a, b \in F$ and any positive integer $n$.
Proof.
Since $F$ is of characteristic $p$ and we have considered arbitrary two elements $a, b$ in $F$ we have
$$
\begin{aligned}
& p a=p b=0 \\
& \Longrightarrow p^n a=p^n b=0 \\
& \Longrightarrow m a=m b=0 \text {. } \\
&
\end{aligned}
$$
Now we know from Binomial Theorem that
$$
(a+b)^m=\sum_{i=0}^m\left(\begin{array}{c}
m \\
i
\end{array}\right) a^i b^{m-i}
$$
Here
$$
\left(\begin{array}{c}
m \\
i
\end{array}\right)=\frac{m !}{i !(m-i) !} .
$$
Now we know that for any integer $n$ and any integer $k$ satisfying $1 \leq k<n, n$ always divides $\left(\begin{array}{l}n \\ k\end{array}\right)$. So in our case for $i$ in the range $1 \leq i<m, m$ divides $\left(\begin{array}{c}m \\ i\end{array}\right)$. It follows that $p$ divides $\left(\begin{array}{c}m \\ i\end{array}\right)$, for $i$ satisfying $1 \leq i<m$, since $m=p^n$ for any integer $n$. Therefore other than the terms $a^m$ and $b^m$ in the expansion $\sum_{i=0}^m\left(\begin{array}{c}m \\ i\end{array}\right) a^i b^{m-i}$ will vanish due to char $p$ nature of $F$.
Hence we have
$$
\sum_{i=0}^m\left(\begin{array}{c}
m \\
i
\end{array}\right) a^i b^{m-i}=a^m+b^m
$$
This follows that, for all $a, b \in F$
$$
(a+b)^m=a^m+b^m .
$$
This completes the proof.
Qed.