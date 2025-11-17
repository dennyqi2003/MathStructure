Exercise 2.4 If $a$ is a nonzero integer, then for $n>m$ show that $\left(a^{2^{n}}+1, a^{2^{m}}+1\right)=1$ or 2 depending on whether $a$ is odd or even.
Proof.
\begin{align*}
\operatorname{ord}_p\, n!  &= \sum_{k\geq 1} \left \lfloor \frac{n}{p^{k}}\right \rfloor \leq  \sum_{k\geq 1}  \frac{n}{p^{k}} = \frac{n}{p} \frac{1}{1 - \frac{1}{p}} = \frac{n}{p-1}
\end{align*}

The decomposition of $n!$ in prime factors is

$n! = p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_k^{\alpha_k}$ 
where $\alpha_i = \operatorname{ord}_{p_i}\, n! \leq \frac{n}{p_i-1}$, and $p_i \leq n, \ i=1,2,\cdots,k$.

Then
\begin{align*}
n! &\leq p_1^{\frac{n}{p_1-1}}p_2^{\frac{n}{p_2-1}}\cdots p_k^{\frac{n}{p_n-1}}\\
\sqrt[n]{n!} &\leq p_1^{\frac{1}{p_1-1}}p_2^{\frac{1}{p_2-1}}\cdots p_k^{\frac{1}{p_n-1}}\\
&\leq \prod_{p\leq n} p^{\frac{1}{p-1}}
\end{align*}
(the values of $p$ in this product describe all prime numbers $p\leq n$.)
Qed.