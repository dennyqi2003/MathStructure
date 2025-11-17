Exercise 6.2 Suppose $u, v \in V$. Prove that $\langle u, v\rangle=0$ if and only if $\|u\| \leq\|u+a v\|$ for all $a \in \mathbf{F}$.
Proof.
First off, let us suppose that $(u, v)=0$.
Now, let $a \in \mathbb{F}$. Next, $u, a v$ are orthogonal.
The Pythagorean theorem thus implies that
$$
\begin{aligned}
\|u+a v\|^2 & =\|u\|^2+\|a v\|^2 \\
& \geq\|u\|^2
\end{aligned}
$$
So, by taking the square roots, this will now give us $\|u\| \leq\|u+a v\|$.
Now, to prove the implication in the other direction, we must now let $\|u\| \leq$ $\|u+a v\|$ for all $a \in \mathbb{F}$. Squaring this inequality, we get both:
$$
\begin{gathered}
\|u\|^2 a n d \leq\|u+a v\|^2 \\
=(u+a v, u+a v) \\
=(u, u)+(u, a v)+(a v, u)+(a v, a v) \\
=\|u\|^2+\bar{a}(u, v)+a \overline{(u, v)}+|a|^2\|v\|^2 \\
\|u\|^2+2 \Re \bar{a}(u, v)+|a|^2\|v\|^2
\end{gathered}
$$
for all $a \in \mathbb{F}$.
Therefore,
$$
-2 \Re \bar{a}(u, v) \leq|a|^2\|v\|^2
$$
for all $a \in \mathbb{F}$. In particular, we can let $a$ equal $-t(u, v)$ for $t>0$. Substituting this value for $a$ into the inequality above gives
$$
2 t|(u, v)|^2 \leq t^2|(u, v)|^2\|v\|^2
$$
for all $t>0$.
Step 4
4 of 4
Divide both sides of the inequality above by $t$, getting
$$
2|(u, v)|^2 \leq t \mid(u, v)^2\|v\|^2
$$
for all $t>0$. If $v=0$, then $(u, v)=0$, as desired. If $v \neq 0$, set $t$ equal to $1 /\|v\|^2$ in the inequality above, getting
$$
2|(u, v)|^2 \leq|(u, v)|^2,
$$
which implies that $(u, v)=0$.
Qed.