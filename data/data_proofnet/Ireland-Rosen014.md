Exercise 4.6 If $p=2^{n}+1$ is a Fermat prime, show that 3 is a primitive root modulo $p$.
Proof.
\newcommand{\legendre}[2]{\genfrac{(}{)}{}{}{#1}{#2}}
Write $p = 2^k + 1$, with $k = 2^n$.

We suppose that $n>0$, so $k\geq 2, p \geq 5$. As $p$ is prime, $3^{p-1} \equiv 1 \pmod p$. 

In other words, $3^{2^k} \equiv 1 \pmod p$ : the order of $3$ is a divisor of $2^k$, a power of $2$.

$3$ has order $2^k$ modulo $p$ iff $3^{2^{k-1}} \not \equiv 1 \pmod p$. As $\left (3^{2^{k-1}} \right)^2 \equiv 1 \pmod p$, where $p$ is prime, this is equivalent to $3^{2^{k-1}}  \equiv -1 \pmod p$, which remains to prove.

$3^{2^{k-1}} = 3^{(p-1)/2} \equiv \legendre{3}{p} \pmod p$.

As the result is true for $p=5$, we can suppose $n\geq 2$.
From the law of quadratic reciprocity :
$$\legendre{3}{p} \legendre{p}{3} = (-1)^{(p-1)/2} = (-1)^{2^{k-1}} = 1.$$
So $\legendre{3}{p} = \legendre{p}{3}$
 
\begin{align*}
p = 2^{2^n}+1 &\equiv (-1)^{2^n} + 1 \pmod 3\\
&\equiv 2 \equiv -1 \pmod 3,
\end{align*}
so $\legendre{3}{p} = \legendre {p}{3} = -1$, that is to say
$$3^{2^{k-1}}  \equiv -1 \pmod p.$$
The order of $3$ modulo $p = 2^{2^n} + 1$ is $p-1 = 2^{2^n}$ : $3$ is a primitive root modulo $p$.

(On the other hand, if $3$ is of order $p-1$ modulo $p$, then $p$ is prime, so
$$ F_n = 2^{2^n} + 1 \ \mathrm{is}\ \mathrm{prime}\ \iff 3^{(F_n-1)/2} = 3^{2^{2^n - 1}} \equiv -1 \pmod {F_n}.)$$
Qed.