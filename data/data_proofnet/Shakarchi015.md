Exercise 3.22 Show that there is no holomorphic function $f$ in the unit disc $D$ that extends continuously to $\partial D$ such that $f(z) = 1/z$ for $z \in \partial D$.
Proof.
Consider $g(r)=\int_{|z|=r} f(z) d z$. Cauchy theorem implies that $g(r)=0$ for all $r<1$. Now since $\left.f\right|_{\partial D}=1 / z$ we have $\lim _{r \rightarrow 1} \int_{|z|=r} f(z) d z=\int_{|z|=1} \frac{1}{z} d z=\frac{2}{\pi i} \neq 0$. Contradiction.
Qed.