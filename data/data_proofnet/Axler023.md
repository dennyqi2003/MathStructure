Exercise 7.5 Show that if $\operatorname{dim} V \geq 2$, then the set of normal operators on $V$ is not a subspace of $\mathcal{L}(V)$.
Proof.
First off, suppose that $\operatorname{dim} V \geq 2$. Next let $\left(e_1, \ldots, e_n\right)$ be an orthonormal basis of $V$. Now, define $S, T \in L(V)$ by both $S\left(a_1 e_1+\ldots+a_n e_n\right)=a_2 e_1-a_1 e_2$ and $T\left(a_1 e_1+\ldots+\right.$ $\left.a_n e_n\right)=a_2 e_1+a_1 e_2$. So, just by now doing a simple calculation verifies that $S^*\left(a_1 e_1+\right.$ $\left.\ldots+a_n e_n\right)=-a_2 e_1+a_1 e_2$

Now, based on this formula, another calculation would show that $S S^*=S^* S$. Another simple calculation would that that $T$ is self-adjoint. Therefore, both $S$ and $T$ are normal. However, $S+T$ is given by the formula of $(S+T)\left(a_1 e_1+\ldots+a_n e_n\right)=2 a_2 e_1$. In this case, a simple calculator verifies that $(S+T)^*\left(a_1 e_1+\ldots+a_n e_n\right)=2 a_1 e_2$.

Therefore, there is a final simple calculation that shows that $(S+T)(S+T)^* \neq(S+$ $T)^*(S+T)$. So, in other words, $S+T$ isn't normal. Thereofre, the set of normal operators on $V$ isn't closed under addition and hence isn't a subspace of $L(V)$.
Qed.