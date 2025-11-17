Exercise 9.3.2 Prove that if $f(x)$ and $g(x)$ are polynomials with rational coefficients whose product $f(x) g(x)$ has integer coefficients, then the product of any coefficient of $g(x)$ with any coefficient of $f(x)$ is an integer.
Proof.
Let $f(x), g(x) \in \mathbb{Q}[x]$ be such that $f(x) g(x) \in \mathbb{Z}[x]$.
By Gauss' Lemma there exists $r, s \in \mathbb{Q}$ such that $r f(x), s g(x) \in \mathbb{Z}[x]$, and $(r f(x))(s g(x))=r s f(x) g(x)=f(x) g(x)$. From this last relation we can conclude that $s=r^{-1}$.

Therefore for any coefficient $f_i$ of $f(x)$ and $g_j$ of $g(x)$ we have that $r f_i, r^{-1} g_j \in$ $\mathbb{Z}$ and by multiplicative closure and commutativity of $\mathbb{Z}$ we have that $r f_i r^{-1} g_j=$ $f_i g_j \in \mathbb{Z}$
Qed.