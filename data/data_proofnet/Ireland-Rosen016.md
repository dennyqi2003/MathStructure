Exercise 4.11 Prove that $1^{k}+2^{k}+\cdots+(p-1)^{k} \equiv 0(p)$ if $p-1 \nmid k$ and $-1(p)$ if $p-1 \mid k$.
Proof.
Let $S_k = 1^k+2^k+\cdots+(p-1)^k$.

Let $g$ a primitive root modulo $p$ : $\overline{g}$ a generator of $\mathbb{F}_p^*$.

As $(\overline{1},\overline{g},\overline{g}^{2}, \ldots, \overline{g}^{p-2}) $ is a permutation of $ (\overline{1},\overline{2}, \ldots,\overline{p-1})$,
\begin{align*}
\overline{S_k} &= \overline{1}^k + \overline{2}^k+\cdots+ \overline{p-1}^k\\
&= \sum_{i=0}^{p-2} \overline{g}^{ki} =
\left\{
\begin{array}{ccc}
\overline{ p-1} = -\overline{1} &  \mathrm{if} &  p-1 \mid k  \\
 \frac{ \overline{g}^{(p-1)k} -1}{ \overline{g}^k -1} = \overline{0}&  \mathrm{if}  &   p-1 \nmid k
\end{array}
\right.
\end{align*}
since $p-1 \mid k \iff \overline{g}^k = \overline{1}$.

Conclusion :
\begin{align*}
1^k+2^k+\cdots+(p-1)^k&\equiv 0 \pmod p\ \mathrm{if} \ p-1 \nmid k\\
1^k+2^k+\cdots+(p-1)^k&\equiv -1 \pmod p\ \mathrm{if} \ p-1 \mid k\\
\end{align*}
Qed.