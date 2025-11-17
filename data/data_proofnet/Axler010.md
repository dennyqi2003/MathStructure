Exercise 4.4 Suppose $p \in \mathcal{P}(\mathbf{C})$ has degree $m$. Prove that $p$ has $m$ distinct roots if and only if $p$ and its derivative $p^{\prime}$ have no roots in common.
Proof.
First, let $p$ have $m$ distinct roots. Since $p$ has the degree of $m$, then this could imply that $p$ can be actually written in the form of $p(z)=c\left(z-\lambda_1\right) \ldots\left(z-\lambda_m\right)$, which you have $\lambda_1, \ldots, \lambda_m$ being distinct.
To prove that both $p$ and $p^{\prime}$ have no roots in commons, we must now show that $p^{\prime}\left(\lambda_j\right) \neq 0$ for every $j$. So, to do so, just fix $j$. The previous expression for $p$ shows that we can now write $p$ in the form of $p(z)=\left(z-\lambda_j\right) q(z)$, which $q$ is a polynomial such that $q\left(\lambda_j\right) \neq 0$.

When you differentiate both sides of the previous equation, then you would then have $p^{\prime}(z)=(z-$ $\left.\lambda_j\right) q^{\prime}(z)+q(z)$

Therefore: $\left.=p^{\prime}\left(\lambda_j\right)=q \lambda_j\right)$
Equals: $p^{\prime}\left(\lambda_j\right) \neq 0$

Now, to prove the other direction, we would now prove the contrapositive, which means that we will be proving that if $p$ has actually less than $m$ distinct roots, then both $p$ and $p^{\prime}$ have at least one root in common.

Now, for some root of $\lambda$ of $p$, we can write $p$ is in the form of $\left.p(z)=(z-\lambda)^n q(z)\right)$, which is where both $n \geq 2$ and $q$ is a polynomial. When differentiating both sides of the previous equations, we would then have $p^{\prime}(z)=(z-\lambda)^n q^{\prime}(z)+n(z-\lambda)^{n-1} q(z)$.
Therefore, $p^{\prime}(\lambda)=0$, which would make $\lambda$ is a common root of both $p$ and $p^{\prime}$.
Qed.