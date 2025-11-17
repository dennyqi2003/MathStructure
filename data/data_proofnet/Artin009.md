Exercise 6.1.14 Let $Z$ be the center of a group $G$. Prove that if $G / Z$ is a cyclic group, then $G$ is abelian and hence $G=Z$.
Proof.
We have that $G / Z(G)$ is cyclic, and so there is an element $x \in G$ such that $G / Z(G)=\langle x Z(G)\rangle$, where $x Z(G)$ is the coset with representative $x$. Now let $g \in G$
We know that $g Z(G)=(x Z(G))^m$ for some $m$, and by definition $(x Z(G))^m=x^m Z(G)$.
Now, in general, if $H \leq G$, we have by definition too that $a H=b H$ if and only if $b^{-1} a \in H$.
In our case, we have that $g Z(G)=x^m Z(G)$, and this happens if and only if $\left(x^m\right)^{-1} g \in Z(G)$.
Then, there's a $z \in Z(G)$ such that $\left(x^m\right)^{-1} g=z$, and so $g=x^m z$.

$g, h \in G$ implies that $g=x^{a_1} z_1$ and $h=x^{a_2} z_2$, so
$$
\begin{aligned}
g h & =\left(x^{a_1} z_1\right)\left(x^{a_2} z_2\right) \\
& =x^{a_1} x^{a_2} z_1 z_2 \\
& =x^{a_1+a_2} z_2 z_1 \\
& =\ldots=\left(x^{a_2} z_2\right)\left(x^{a_1} z_1\right)=h g .
\end{aligned}
$$
Therefore, $G$ is abelian.
Qed.