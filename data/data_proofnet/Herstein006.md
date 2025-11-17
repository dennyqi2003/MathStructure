Exercise 2.2.5 Let $G$ be a group in which $(a b)^{3}=a^{3} b^{3}$ and $(a b)^{5}=a^{5} b^{5}$ for all $a, b \in G$. Show that $G$ is abelian.
Proof.
We have
$$
\begin{aligned}
& (a b)^3=a^3 b^3, \text { for all } a, b \in G \\
\Longrightarrow & (a b)(a b)(a b)=a\left(a^2 b^2\right) b \\
\Longrightarrow & a(b a)(b a) b=a\left(a^2 b^2\right) b \\
\Longrightarrow & (b a)^2=a^2 b^2, \text { by cancellation law. }
\end{aligned}
$$
Again,
$$
\begin{aligned}
& (a b)^5=a^5 b^5, \text { for all } a, b \in G \\
\Longrightarrow & (a b)(a b)(a b)(a b)(a b)=a\left(a^4 b^4\right) b \\
\Longrightarrow & a(b a)(b a)(b a)(b a) b=a\left(a^4 b^4\right) b \\
\Longrightarrow & (b a)^4=a^4 b^4, \text { by cancellation law. }
\end{aligned}
$$
Now by combining two cases we have
$$
\begin{aligned}
& (b a)^4=a^4 b^4 \\
\Longrightarrow & \left((b a)^2\right)^2=a^2\left(a^2 b^2\right) b^2 \\
\Longrightarrow & \left(a^2 b^2\right)^2=a^2\left(a^2 b^2\right) b^2 \\
\Longrightarrow & \left(a^2 b^2\right)\left(a^2 b^2\right)=a^2\left(a^2 b^2\right) b^2 \\
\Longrightarrow & a^2\left(b^2 a^2\right) b^2=a^2\left(a^2 b^2\right) b^2 \\
\Longrightarrow & b^2 a^2=a^2 b^2, \text { by cancellation law. } \\
\Longrightarrow & b^2 a^2=(b a)^2, \text { since }(b a)^2=a^2 b^2 \\
\Longrightarrow & b(b a) a=(b a)(b a) \\
\Longrightarrow & b(b a) a=b(a b) a \\
\Longrightarrow & b a=a b, \text { by cancellation law. }
\end{aligned}
$$
It follows that, $a b=b a$ for all $a, b \in G$. Hence $G$ is abelian
Qed.