Exercise 6.7 Prove that if $V$ is a complex inner-product space, then $\langle u, v\rangle=\frac{\|u+v\|^{2}-\|u-v\|^{2}+\|u+i v\|^{2} i-\|u-i v\|^{2} i}{4}$ for all $u, v \in V$.
Proof.
Let $V$ be an inner-product space and $u, v\in V$. Then 
$$
\begin{aligned}
\|u+v\|^2 & =\langle u+v, v+v\rangle \\
& =\|u\|^2+\langle u, v\rangle+\langle v, u\rangle+\|v\|^2 \\
-\|u-v\|^2 & =-\langle u-v, u-v\rangle \\
& =-\|u\|^2+\langle u, v\rangle+\langle v, u\rangle-\|v\|^2 \\
i\|u+i v\|^2 & =i\langle u+i v, u+i v\rangle \\
& =i\|u\|^2+\langle u, v\rangle-\langle v, u\rangle+i\|v\|^2 \\
-i\|u-i v\|^2 & =-i\langle u-i v, u-i v\rangle \\
& =-i\|u\|^2+\langle u, v\rangle-\langle v, u\rangle-i\|v\|^2 .
\end{aligned}
$$
Thus $\left(\|u+v\|^2\right)-\|u-v\|^2+\left(i\|u+i v\|^2\right)-i\|u-i v\|^2=4\langle u, v\rangle.$
Qed.