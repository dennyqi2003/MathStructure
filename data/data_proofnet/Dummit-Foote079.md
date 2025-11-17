Exercise 9.1.10 Prove that the ring $\mathbb{Z}\left[x_{1}, x_{2}, x_{3}, \ldots\right] /\left(x_{1} x_{2}, x_{3} x_{4}, x_{5} x_{6}, \ldots\right)$ contains infinitely many minimal prime ideals.
Proof.
Let $R=\mathbb{Z}\left[x_1, x_2, \ldots, x_n\right]$ and consider the ideal $K=\left(x_{2 k+1} x_{2 k+2} \mid k \in \mathbb{Z}_{+}\right)$in $R$.
Consider the family of subsets $X=\left\{\left\{x_{2 k+1}, x_{2 k+2}\right\} \mid k \in \mathbb{Z}_{+}\right\}$, and $Y$ the set of choice function on $X$, ie the set of functions $\lambda: \mathbb{Z}_{+} \rightarrow \cup_{\mathbb{Z}_{+}}\left\{x_{2 k+1}, x_{2 k+2}\right\}$ with $\lambda(a) \in$ $\left\{x_{2 a+1}, x_{2 a+2}\right\}$
For each $\lambda \in Y$ we have the ideal $I_\lambda=(\lambda(0), \lambda(1), \ldots)$.
All these ideals are distinct, ie for $\lambda \neq \lambda^{\prime}$ we have $I_\lambda \neq I_{\lambda^{\prime}}$.
We also have that by construction $K \subset I_\lambda$ for all $\lambda \in Y$.
By the Third Isomorphism Treorem
$$
(R / K) /\left(I_\lambda / K\right) \cong R / I_\lambda
$$
Note also that $R / I_\lambda$ is isomorphic to the polynomial ring over $R$ with indeterminates the $x_i$ not in the image of $\lambda$, and since there is a countably infinite number of them we can conclude $R / I_\lambda \cong R$, an integral domain. Therefore $I_\lambda / K$ is a prime ideal of $R / K$

We prove now that $I_\lambda / K$ is a minimal prime ideal. Let $J / K \subseteq I_\lambda / K$ be a prime ideal. For each pair $\left(x_{2 k+1}, x_{2 k+2}\right)$ we have that $x_{2 k+1} x_{2 k+2} \in K$ so $x_{2 k+1} x_{2 k+2} \bmod K \in J / K$ so $J$ must contain one of the elements in $\left\{x_{2 k+1}, x_{2 k+2}\right\}$. But since $J / K \subseteq I_\lambda / K$ it must be $\lambda(k)$ for all $k \in \mathbb{Z}_{+}$. Therefore $J / K=I_\lambda / K$
Qed.