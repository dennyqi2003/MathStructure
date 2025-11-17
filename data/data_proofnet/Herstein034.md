Exercise 4.3.25 Let $R$ be the ring of $2 \times 2$ matrices over the real numbers; suppose that $I$ is an ideal of $R$. Show that $I = (0)$ or $I = R$.
Proof.
Suppose that $I$ is a nontrivial ideal of $R$, and let
$$
A=\left(\begin{array}{ll}
a & b \\
c & d
\end{array}\right)
$$
where not all of $a, b, c d$ are zero. Suppose, without loss of generality -- our steps would be completely analogous, modulo some different placement of 1 s in our matrices, if we assumed some other element to be nonzero -- that $a \neq 0$. Then we have that
$$
\left(\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right)\left(\begin{array}{ll}
a & b \\
c & d
\end{array}\right)=\left(\begin{array}{ll}
a & b \\
0 & 0
\end{array}\right) \in I
$$
and so
$$
\left(\begin{array}{ll}
a & b \\
0 & 0
\end{array}\right)\left(\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right)=\left(\begin{array}{ll}
a & 0 \\
0 & 0
\end{array}\right) \in I
$$
so that
$$
\left(\begin{array}{ll}
x & 0 \\
0 & 0
\end{array}\right) \in I
$$
for any real $x$. Now, also for any real $x$,
$$
\left(\begin{array}{ll}
x & 0 \\
0 & 0
\end{array}\right)\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)=\left(\begin{array}{ll}
0 & x \\
0 & 0
\end{array}\right) \in I .
$$
Likewise
$$
\left(\begin{array}{ll}
0 & 0 \\
1 & 0
\end{array}\right)\left(\begin{array}{ll}
0 & x \\
0 & 0
\end{array}\right)=\left(\begin{array}{ll}
0 & 0 \\
0 & x
\end{array}\right) \in I
$$
and
$$
\left(\begin{array}{ll}
0 & 0 \\
0 & x
\end{array}\right)\left(\begin{array}{ll}
0 & 0 \\
1 & 0
\end{array}\right)=\left(\begin{array}{ll}
0 & 0 \\
x & 0
\end{array}\right)
$$
Thus, as
$$
\left(\begin{array}{ll}
a & b \\
c & d
\end{array}\right)=\left(\begin{array}{ll}
a & 0 \\
0 & 0
\end{array}\right)+\left(\begin{array}{ll}
0 & b \\
0 & 0
\end{array}\right)+\left(\begin{array}{ll}
0 & 0 \\
c & 0
\end{array}\right)+\left(\begin{array}{ll}
0 & 0 \\
0 & d
\end{array}\right)
$$
and since all the terms on the right side are in $I$ and $I$ is an additive group, it follows that
$$
\left(\begin{array}{ll}
a & b \\
c & d
\end{array}\right)
$$
for arbitrary $a, b, c, d$ is in $I$, i.e. $I=R$
Note that the intuition for picking these matrices is that, if we denote by $E_{i j}$ the matrix with 1 at position $(i, j)$ and 0 elsewhere, then
$$
E_{i j}\left(\begin{array}{ll}
a_{1,1} & a_{1,2} \\
a_{2,1} & a_{2,2}
\end{array}\right) E_{n m}=a_{j, n} E_{i m}
$$
Qed.