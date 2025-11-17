Exercise 5.4.3 If $a \in C$ is such that $p(a) = 0$, where $p(x) = x^5 + \sqrt{2}x^3 + \sqrt{5}x^2 + \sqrt{7}x + \sqrt{11}$, show that $a$ is algebraic over $\mathbb{Q}$ of degree at most 80.
Proof.
Given $a \in \mathbb{C}$ such that $p(a)=0$, where
$$
p(x)=x^5+\sqrt{2} x^3+\sqrt{5} x^2+\sqrt{7} x+\sqrt{11}
$$
Here, we note that $p(x) \in \mathbb{Q}(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11})$ and
$$
\begin{aligned}
    {[Q(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11}): \mathbb{Q}] } & =[Q(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11}): Q(\sqrt{2}, \sqrt{5}, \sqrt{7})] \cdot[\mathbb{Q}(\sqrt{2}, \sqrt{5}, \sqrt{7}): \mathbb{Q}(\sqrt{2}, \sqrt{5})] \\
& \cdot[\mathbb{Q}(\sqrt{2}, \sqrt{5}): \mathbb{Q}(\sqrt{2})] \cdot[\mathbb{Q}(\sqrt{2}): \mathbb{Q}] \\
& =2 \cdot 2 \cdot 2 \cdot 2 \\
& =16
\end{aligned}
$$
Here, we note that $p(x)$ is of degree 5 over $\mathbb{Q}(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11})$. If $a$ is root of $p(x)$, then
$$
[Q(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11}, a): \mathbb{Q}]=[Q(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11}): Q(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11})] \cdot 15
$$
and $[Q(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11}): Q(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11})] \leq 5$. We get equality if $p(x)$ is irreducible over $Q(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11})$. This gives
$$
[Q(\sqrt{2}, \sqrt{5}, \sqrt{7}, \sqrt{11}, a): \mathbb{Q}] \leq 16 \cdot 5=80
$$
Qed.