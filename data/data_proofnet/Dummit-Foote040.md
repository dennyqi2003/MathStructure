Exercise 4.2.9a Prove that if $p$ is a prime and $G$ is a group of order $p^{\alpha}$ for some $\alpha \in \mathbb{Z}^{+}$, then every subgroup of index $p$ is normal in $G$.
Proof.
Solution: Let $G$ be a group of order $p^k$ and $H \leq G$ a subgroup with $[G: H]=p$. Now $G$ acts on the conjugates $g H g^{-1}$ by conjugation, since
$$
g_1 g_2 \cdot H=\left(g_1 g_2\right) H\left(g_1 g_2\right)^{-1}=g_1\left(g_2 H g_2^{-1}\right) g_1^{-1}=g_1 \cdot\left(g_2 \cdot H\right)
$$
and $1 \cdot H=1 H 1=H$. Moreover, under this action we have $H \leq \operatorname{stab}(H)$. By Exercise 3.2.11, we have
$$
[G: \operatorname{stab}(H)][\operatorname{stab}(H): H]=[G: H]=p,
$$
a prime.
If $[G: \operatorname{stab}(H)]=p$, then $[\operatorname{stab}(H): H]=1$ and we have $H=\operatorname{stab}(H)$; moreover, $H$ has exactly $p$ conjugates in $G$. Let $\varphi: G \rightarrow S_p$ be the permutation representation induced by the action of $G$ on the conjugates of $H$, and let $K$ be the kernel of this representation. Now $K \leq \operatorname{stab}(H)=H$. By the first isomorphism theorem, the induced map $\bar{\varphi}: G / K \rightarrow S_p$ is injective, so that $|G / K|$ divides $p$ !. Note, however, that $|G / K|$ is a power of $p$ and that the only powers of $p$ that divide $p$ ! are 1 and $p$. So $[G: K]$ is 1 or $p$. If $[G: K]=1$, then $G=K$ so that $g H g^{-1}=H$ for all $g \in G$; then $\operatorname{stab}(H)=G$ and we have $[G: \operatorname{stab}(H)]=1$, a contradiction. Now suppose $[G: K]=p$. Again by Exercise $3.2$.11 we have $[G: K]=[G: H][H: K]$, so that $[H: K]=1$, hence $H=K$. Again, this implies that $H$ is normal so that $g H g^{-1}=H$ for all $g \in G$, and we have $[G: \operatorname{stab}(H)]=1$, a contradiction. Thus $[G: \operatorname{stab}(H)] \neq p$
If $[G: \operatorname{stab}(H)]=1$, then $G=\operatorname{stab}(H)$. That is, $g H g^{-1}=H$ for all $g \in G$; thus $H \leq G$ is normal.
Qed.