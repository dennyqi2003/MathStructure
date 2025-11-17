Exercise 5.37 Show that if $a$ is negative then $p \equiv q(4 a) together with p\not | a$ imply $(a / p)=(a / q)$.
Proof.
\newcommand{\legendre}[2]{\genfrac{(}{)}{}{}{#1}{#2}}
Write $a = -A, A>0$. As $p \equiv q \pmod {4a}$, we know from Prop. 5.3.3. (b) that $(A/p) = (A/q)$.

Moreover,
\begin{align*}
\legendre{a}{p}&= \legendre{-A}{p} = (-1)^{(p-1)/2} \legendre{A}{p}\\
\legendre{a}{q}&= \legendre{-A}{q} = (-1^{(q-1)/2} \legendre{A}{q}
\end{align*}
As  $p \equiv q \pmod {4a}$, $ p = q + 4ak, k\in \mathbb{Z}$, so
$$(-1)^{(p-1)/2} = (-1)^{(q+4ak-1)/2} = (-1)^{(q-1)/2},$$
so $(a/p) = (a/q)$.
Qed.