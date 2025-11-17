Exercise 2.3.17 If $G$ is a group and $a, x \in G$, prove that $C\left(x^{-1} a x\right)=x^{-1} C(a) x$
Proof.
Note that
$$
C(a):=\{x \in G \mid x a=a x\} .
$$
Let us assume $p \in C\left(x^{-1} a x\right)$. Then,
$$
\begin{aligned}
& p\left(x^{-1} a x\right)=\left(x^{-1} a x\right) p \\
\Longrightarrow & \left(p x^{-1} a\right) x=x^{-1}(a x p) \\
\Longrightarrow & x\left(p x^{-1} a\right)=(a x p) x^{-1} \\
\Longrightarrow & \left(x p x^{-1}\right) a=a\left(x p x^{-1}\right) \\
\Longrightarrow & x p x^{-1} \in C(a) .
\end{aligned}
$$
Therefore,
$$
p \in C\left(x^{-1} a x\right) \Longrightarrow x p x^{-1} \in C(a) .
$$
Thus,
$$
C\left(x^{-1} a x\right) \subset x^{-1} C(a) x .
$$
Let us assume
$$
q \in x^{-1} C(a) x .
$$
Then there exists an element $y$ in $C(a)$ such that
$$
q=x^{-1} y x
$$
Now,
$$
y \in C(a) \Longrightarrow y a=a y .
$$
Also,
$$
q\left(x^{-1} a x\right)=\left(x^{-1} y x\right)\left(x^{-1} a x\right)=x^{-1}(y a) x=x^{-1}(y a) x=\left(x^{-1} y x\right)\left(x^{-1} a x\right)=\left(x^{-1} y x\right) q .
$$
Therefore,
$$
q\left(x^{-1} a x\right)=\left(x^{-1} y x\right) q
$$
So,
$$
q \in C\left(x^{-1} a x\right) .
$$
Consequently we have
$$
x^{-1} C(a) x \subset C\left(x^{-1} a x\right) .
$$
It follows from the aforesaid argument
$$
C\left(x^{-1} a x\right)=x^{-1} C(a) x .
$$
This completes the proof.
Qed.