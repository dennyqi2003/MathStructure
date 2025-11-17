Exercise 1.12 If $z_1, \ldots, z_n$ are complex, prove that $|z_1 + z_2 + \ldots + z_n| \leq |z_1| + |z_2| + \cdots + |z_n|$.
Proof.
We can apply the case $n=2$ and induction on $n$ to get
$$
\begin{aligned}
\left|z_1+z_2+\cdots z_n\right| &=\left|\left(z_1+z_2+\cdots+z_{n-1}\right)+z_n\right| \\
& \leq\left|z_1+z_2+\cdots+z_{n-1}\right|+\left|z_n\right| \\
& \leq\left|z_1\right|+\left|z_2\right|+\cdots+\left|z_{n-1}\right|+\left|z_n\right|
\end{aligned}
$$
Qed.