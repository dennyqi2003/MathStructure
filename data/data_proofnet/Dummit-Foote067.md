Exercise 7.2.2 Let $p(x)=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0}$ be an element of the polynomial ring $R[x]$. Prove that $p(x)$ is a zero divisor in $R[x]$ if and only if there is a nonzero $b \in R$ such that $b p(x)=0$.
Proof.
Solution: If $b p(x)=0$ for some nonzero $b \in R$, then it is clear that $p(x)$ is a zero divisor.
Now suppose $p(x)$ is a zero divisor; that is, for some $q(x)=\sum_{i=0}^m b_i x^i$, we have $p(x) q(x)=0$. We may choose $q(x)$ to have minimal degree among the nonzero polynomials with this property.
We will now show by induction that $a_i q(x)=0$ for all $0 \leq i \leq n$.
For the base case, note that
$$
p(x) q(x)=\sum_{k=0}^{n+m}\left(\sum_{i+j=k} a_i b_j\right) x^k=0 .
$$
The coefficient of $x^{n+m}$ in this product is $a_n b_m$ on one hand, and 0 on the other. Thus $a_n b_m=0$. Now $a_n q(x) p(x)=0$, and the coefficient of $x^m$ in $q$ is $a_n b_m=0$. Thus the degree of $a_n q(x)$ is strictly less than that of $q(x)$; since $q(x)$ has minimal degree among the nonzero polynomials which multiply $p(x)$ to 0 , in fact $a_n q(x)=0$. More specifically, $a_n b_i=0$ for all $0 \leq i \leq m$.
For the inductive step, suppose that for some $0 \leq t<n$, we have $a_r q(x)=0$ for all $t<r \leq n$. Now
$$
p(x) q(x)=\sum_{k=0}^{n+m}\left(\sum_{i+j=k} a_i b_j\right) x^k=0 .
$$
On one hand, the coefficient of $x^{m+t}$ is $\sum_{i+j=m+t} a_i b_j$, and on the other hand, it is 0 . Thus
$$
\sum_{i+j=m+t} a_i b_j=0 .
$$
By the induction hypothesis, if $i \geq t$, then $a_i b_j=0$. Thus all terms such that $i \geq t$ are zero. If $i<t$, then we must have $j>m$, a contradiction. Thus we have $a_t b_m=0$. As in the base case,
$$
a_t q(x) p(x)=0
$$
and $a_t q(x)$ has degree strictly less than that of $q(x)$, so that by minimality, $a_t q(x)=0$.
By induction, $a_i q(x)=0$ for all $0 \leq i \leq n$. In particular, $a_i b_m=0$. Thus $b_m p(x)=0$.
Qed.