Exercise 2.5.52 Let $G$ be a finite group and $\varphi$ an automorphism of $G$ such that $\varphi(x) = x^{-1}$ for more than three-fourths of the elements of $G$. Prove that $\varphi(y) = y^{-1}$ for all $y \in G$, and so $G$ is abelian.
Proof.
Let us start with considering $b$ to be an arbitrary element in $A$. 

1. Show that $\left|A \cap\left(b^{-1} A\right)\right|>\frac{|G|}{2}$, where
$$
b^{-1} A=\left\{b^{-1} a \mid a \in A\right\}
$$
First notice that if we consider a map $f: A \rightarrow b^{-1} A$ defined by $f(a)=b^{-1} a$, for all $a \in A$, then $f$ is a 1-1 map and so $\left|b^{-1} A\right| \geq|A|>\frac{3}{4}|G|$. Now using inclusion-exclusion principle we have
$$
\left|A \cap\left(b^{-1} A\right)\right|=|A|+\left|b^{-1} A\right|-\left|A \cup\left(b^{-1} A\right)\right|>\frac{3}{4}|G|+\frac{3}{4}|G|-|G|=\frac{1}{2}|G|
$$
2. Argue that $A \cap\left(b^{-1} A\right) \subseteq C(b)$, where $C(b)$ is the centralizer of $b$ in $G$.

Suppose $x \in A \cap\left(b^{-1} A\right)$, that means, $x \in A$ and $x \in b^{-1} A$. Thus there exist an element $a \in A$ such that $x=$ $b^{-1} a$, which gives us $x b=a \in A$. Now notice that $x, b \in A$ and $x b \in A$, therefore we get
$$
\phi(x b)=(x b)^{-1} \Longrightarrow \phi(x) \phi(b)=(x b)^{-1} \Longrightarrow x^{-1} b^{-1}=b^{-1} x^{-1} \Longrightarrow x b=b x
$$
Therefore, we get $x b=b x$, for any $x \in A \cap\left(b^{-1} A\right)$, that means, $x \in C(b)$.

3. Argue that $C(b)=G$.
We know that centralizer of an element in a group $G$ is a subgroup (See Page 53). Therefore $C(b)$ is a subgroup of $G$. From statements $\mathbf{1}$ and $\mathbf{2}$, we have
$$
|C(b)| \geq\left|A \cap\left(b^{-1} A\right)\right|>\frac{|G|}{2}
$$
We need to use the following remark to argue $C(b)=G$ from the above step.
Remark. Let $G$ be a finite group and $H$ be a subgroup with more then $|G| / 2$ elements then $H=G$.

Proof of Remark. Suppose $|H|=p$ Then by Lagrange Theorem, there exist an $n \in \mathbb{N}$, such that $|G|=n p$, as $|H|$ divide $|G|$. Now by hypothesis $p>\frac{G]}{2}$ gives us,
$$
p>\frac{|G|}{2} \Longrightarrow n p>\frac{n|G|}{2} \Longrightarrow n<2 \Longrightarrow n=1
$$
Therefore we get $H=G$.

Now notice that $C(b)$ is a subgroup of $G$ with $C(b)$ having more than $|G| / 2$ elements. Therefore, $C(b)=G$.

4. Show that $A \in Z(G)$.

We know that $x \in Z(G)$ if and only if $C(a)=G$. Now notice that, for any $b \in A$ we have $C(b)=G$. Therefore, every element of $A$ is in the center of $G$, that means, $A \subseteq Z(G)$.

5. 5how that $Z(G)=G$.

As it is given that $|A|>\frac{3|G|}{4}$ and $A \leq|Z(G)|$, therefore we get
$$
|Z(G)|>\frac{3}{4}|G|>\frac{1}{2}|G| .
$$
As $Z(G)$ is a subgroup of $G$, so by the above Remark we have $Z(G)=G$. Hence $G$ is abelian.

6. Finally show that $A=G$.

First notice that $A$ is a subgroup of $G$. To show this let $p, q \in A$. Then we have
$$
\phi(p q)=\phi(p) \phi(q)=p^{-1} q^{-1}=(q p)^{-1}=(p q)^{-1}, \quad \text { As } G \text { is abelian. }
$$
Therefore, $p q \in A$ and so we have $A$ is a subgroup of $G$. Again by applying the above remark. we get $A=G$. Therefore we have
$$
\phi(y)=y^{-1}, \quad \text { for all } y \in G
$$
Qed.