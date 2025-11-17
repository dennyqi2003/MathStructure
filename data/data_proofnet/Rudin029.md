Exercise 3.8 If $\Sigma a_{n}$ converges, and if $\left\{b_{n}\right\}$ is monotonic and bounded, prove that $\Sigma a_{n} b_{n}$ converges.
Proof.
We shall show that the partial sums of this series form a Cauchy sequence, i.e., given $\varepsilon>0$ there exists $N$ such that $\left|\sum_{k=m+1}^n a_k b_k\right|\langle\varepsilon$ if $n\rangle$ $m \geq N$. To do this, let $S_n=\sum_{k=1}^n a_k\left(S_0=0\right)$, so that $a_k=S_k-S_{k-1}$ for $k=1,2, \ldots$ Let $M$ be an uppper bound for both $\left|b_n\right|$ and $\left|S_n\right|$, and let $S=\sum a_n$ and $b=\lim b_n$. Choose $N$ so large that the following three inequalities hold for all $m>N$ and $n>N$ :
$$
\left|b_n S_n-b S\right|<\frac{\varepsilon}{3} ; \quad\left|b_m S_m-b S\right|<\frac{\varepsilon}{3} ; \quad\left|b_m-b_n\right|<\frac{\varepsilon}{3 M} .
$$
Then if $n>m>N$, we have, from the formula for summation by parts,
$$
\sum_{k=m+1}^n a_n b_n=b_n S_n-b_m S_m+\sum_{k=m}^{n-1}\left(b_k-b_{k+1}\right) S_k
$$
Our assumptions yield immediately that $\left|b_n S_n-b_m S_m\right|<\frac{2 \varepsilon}{3}$, and
$$
\left|\sum_{k=m}^{n-1}\left(b_k-b_{k+1}\right) S_k\right| \leq M \sum_{k=m}^{n-1}\left|b_k-b_{k+1}\right| .
$$
Since the sequence $\left\{b_n\right\}$ is monotonic, we have
$$
\sum_{k=m}^{n-1}\left|b_k-b_{k+1}\right|=\left|\sum_{k=m}^{n-1}\left(b_k-b_{k+1}\right)\right|=\left|b_m-b_n\right|<\frac{\varepsilon}{3 M},
$$
from which the desired inequality follows.
Qed.