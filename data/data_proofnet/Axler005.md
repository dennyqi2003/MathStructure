Exercise 1.7 Give an example of a nonempty subset $U$ of $\mathbf{R}^2$ such that $U$ is closed under scalar multiplication, but $U$ is not a subspace of $\mathbf{R}^2$.
Proof.
$$
U=\left\{(x, y) \in \mathbf{R}^2:|x|=|y|\right\}
$$
For $(x, y) \in U$ and $\lambda \in \mathbb{R}$, it follows $\lambda(x, y)=$ $(\lambda x, \lambda y)$, so $|\lambda x|=|\lambda||x|=|\lambda||y|=|\lambda y|$. Therefore, $\lambda(x, y) \in U$.

On the other hand, consider $a=(1,-1), b=$ $(1,1) \in U$. Then, $a+b=(1,-1)+(1,1)=$ $(2,0) \notin U$. So, $U$ is not a subspace of $\mathbb{R}^2$.
Qed.