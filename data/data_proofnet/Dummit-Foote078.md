Exercise 9.1.6 Prove that $(x, y)$ is not a principal ideal in $\mathbb{Q}[x, y]$.
Proof.
Suppose, to the contrary, that $(x, y)=p$ for some polynomial $p \in \mathbb{Q}[x, y]$. From $x, y \in$ $(x, y)=(p)$ there are $s, t \in \mathbb{Q}[x, y]$ such that $x=s p$ and $y=t p$.
Then:
$$
\begin{aligned}
& 0=\operatorname{deg}_y(x)=\operatorname{deg}_y(s)+\operatorname{deg}_y(p) \text { so } \\
& 0=\operatorname{deg}_y(p) \\
& 0=\operatorname{deg}_x(y)=\operatorname{deg}_x(s)+\operatorname{deg}_x(p) \text { so } \\
& 0=\operatorname{deg}_x(p) \text { so }
\end{aligned}
$$
From : $\quad 0=\operatorname{deg}_y(p)=\operatorname{deg}_x(p)$ we get $\operatorname{deg}(p)=0$ and $p \in \mathbb{Q}$.
But $p \in(p)=(x, y)$ so $p=a x+b y$ for some $a, b \in \mathbb{Q}[x, y]$
$$
\begin{aligned}
\operatorname{deg}(p) & =\operatorname{deg}(a x+b y) \\
& =\min (\operatorname{deg}(a)+\operatorname{deg}(x), \operatorname{deg}(b)+\operatorname{deg}(y)) \\
& =\min (\operatorname{deg}(a)+1, \operatorname{deg}(b)+1) \geqslant 1
\end{aligned}
$$
which contradicts $\operatorname{deg}(p)=0$.
So we conclude that $(x, y)$ is not principal ideal in $\mathbb{Q}[x, y]$
Qed.