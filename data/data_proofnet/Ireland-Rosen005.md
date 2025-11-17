Exercise 2.21 Define $\wedge(n)=\log p$ if $n$ is a power of $p$ and zero otherwise. Prove that $\sum_{A \mid n} \mu(n / d) \log d$ $=\wedge(n)$.
Proof.
$$
\left\{
\begin{array}{cccl}
    \land(n)& =  & \log p & \mathrm{if}\  n =p^\alpha,\ \alpha \in \mathbb{N}^*  \\
  &  = &   0 & \mathrm{otherwise }.
\end{array}
\right.
$$
Let $n = p_1^{\alpha_1}\cdots p_t^{\alpha_t}$ the decomposition of $n$ in prime factors. As $\land(d) = 0$ for all divisors of $n$, except for $d = p_j^i, i>0, j=1,\ldots t$,
\begin{align*}
\sum_{d \mid n} \land(d)&= \sum_{i=1}^{\alpha_1} \land(p_1^{i}) + \cdots+ \sum_{i=1}^{\alpha_t} \land(p_t^{i})\\ 
&= \alpha_1 \log p_1+\cdots + \alpha_t \log p_t\\
&= \log n
\end{align*}
By Mobius Inversion Theorem,
$$\land(n) = \sum_{d \mid n} \mu\left (\frac{n}{d}\right ) \log d.$$
Qed.