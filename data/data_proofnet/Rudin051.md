Exercise 5.2 Suppose $f^{\prime}(x)>0$ in $(a, b)$. Prove that $f$ is strictly increasing in $(a, b)$, and let $g$ be its inverse function. Prove that $g$ is differentiable, and that $g^{\prime}(f(x))=\frac{1}{f^{\prime}(x)} \quad(a<x<b)$.
Proof.
For any $c, d$ with $a<c<d<b$ there exists a point $p \in(c, d)$ such that $f(d)-f(c)=f^{\prime}(p)(d-c)>0$. Hence $f(c)<f(d)$

We know from Theorem $4.17$ that the inverse function $g$ is continuous. (Its restriction to each closed subinterval $[c, d]$ is continuous, and that is sufficient.) Now observe that if $f(x)=y$ and $f(x+h)=y+k$, we have
$$
\frac{g(y+k)-g(y)}{k}-\frac{1}{f^{\prime}(x)}=\frac{1}{\frac{f(x+h)-f(x)}{h}}-\frac{1}{f^{\prime}(x)}
$$
Since we know $\lim \frac{1}{\varphi(t)}=\frac{1}{\lim \varphi(t)}$ provided $\lim \varphi(t) \neq 0$, it follows that for any $\varepsilon>0$ there exists $\eta>0$ such that
$$
\left|\frac{1}{\frac{f(x+h)-f(x)}{h}}-\frac{1}{f^{\prime}(x)}\right|<\varepsilon
$$
if $0<|h|<\eta$. Since $h=g(y+k)-g(y)$, there exists $\delta>0$ such that $0<|h|<\eta$ if $0<|k|<\delta$. The proof is now complete.
Qed.