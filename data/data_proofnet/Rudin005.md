Exercise 1.5 Let $A$ be a nonempty set of real numbers which is bounded below. Let $-A$ be the set of all numbers $-x$, where $x \in A$. Prove that $\inf A=-\sup (-A)$.
Proof.
We need to prove that $-\sup (-A)$ is the greatest lower bound of $A$. For brevity, let $\alpha=-\sup (-A)$. We need to show that $\alpha \leq x$ for all $x \in A$ and $\alpha \geq \beta$ if $\beta$ is any lower bound of $A$.

Suppose $x \in A$. Then, $-x \in-A$, and, hence $-x \leq \sup (-A)$. It follows that $x \geq-\sup (-A)$, i.e., $\alpha \leq x$. Thus $\alpha$ is a lower bound of $A$.

Now let $\beta$ be any lower bound of $A$. This means $\beta \leq x$ for all $x$ in $A$. Hence $-x \leq-\beta$ for all $x \in A$, which says $y \leq-\beta$ for all $y \in-A$. This means $-\beta$ is an upper bound of $-A$. Hence $-\beta \geq \sup (-A)$ by definition of sup, i.e., $\beta \leq-\sup (-A)$, and so $-\sup (-A)$ is the greatest lower bound of $A$.
Qed.