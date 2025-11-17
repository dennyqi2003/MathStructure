Exercise 10.2.4 Prove that in the ring $\mathbb{Z}[x],(2) \cap(x)=(2 x)$.
Proof.
Let $f(x) \in(2 x)$. Then there exists some polynomial $g(x) \in \mathbb{Z}$ such that
$$
f(x)=2 x g(x)
$$
But this means that $f(x) \in(2)$ (because $x g(x)$ is a polynomial), and $f(x) \in$ $(x)$ (because $2 g(x)$ is a polynomial). Thus, $f(x) \in(2) \cap(x)$, and
$$
(2 x) \subseteq(2) \cap(x)
$$
On the other hand, let $p(x) \in(2) \cap(x)$. Since $p(x) \in(2)$, there exists some polynomial $h(x) \in \mathbb{Z}[x]$ such that
$$
p(x)=2 h(x)
$$
Furthermore, $p(x) \in(x)$, so
$$
p(x)=x h_2(x)
$$
So, $2 h(x)=x h_2(x)$, for some $h_2(x) \in \mathbb{Z}[x]$. This means that $h(0)=0$, so $x$ divides $h(x)$; that is,
$$
h(x)=x q(x)
$$
for some $q(x) \in \mathbb{Z}[x]$, and
$$
p(x)=2 x q(x)
$$
Thus, $p(x) \in(2 x)$, and
$$
\text { (2) } \cap(x) \subseteq(2 x)
$$
Finally,
(2) $\cap(x)=(2 x)$,
as required.
Qed.