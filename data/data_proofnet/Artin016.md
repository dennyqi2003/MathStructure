Exercise 10.6.7 Prove that every nonzero ideal in the ring of Gauss integers contains a nonzero integer.
Proof.
Let $I$ be some nonzero ideal. Then there exists some $z \in \mathbb{Z}[i], z \neq 0$ such that $z \in I$. We know that $z=a+b i$, for some $a, b \in \mathbb{Z}$. We consider three cases:
1. If $b=0$, then $z=a$, so $z \in \mathbb{Z} \cap I$, and $z \neq 0$, so the statement of the exercise holds.
2. If $a=0$, then $z=i b$. Since $z \neq 0$, we conclude that $b \neq 0$. Since $I$ is an ideal in $\mathbb{Z}[i]$, and $i \in \mathbb{Z}[i]$, we conclude that $i z \in I$. Furthermore, $i z=-b \in \mathbb{Z}$. Thus, $i z$ is a nonzero integer which is in $I$.
3. Let $a \neq 0$ and $b \neq 0$. Since $I$ is an ideal and $z \in I$, we conclude that $z^2 \in I$; that is,
$$
(a+b i)^2=a^2-b^2+2 a b i \in I
$$
Furthermore, since $-2 a \in \mathbb{Z}[i]$, and $z \in I$ and $I$ is an ideal, $-2 a z \in I$; that is,
$$
-2 a z=-2 a(a+b i)=-2 a^2-2 a b i \in I
$$
Since $I$ is closed under addition,
$$
\left(a^2-b^2+2 a b i\right)+\left(-2 a^2-2 a b i\right) \in I \Longrightarrow-a^2-b^2 \in I
$$
Notice that $-a^2-b^2 \neq 0$ since $a^2>0$ and $b^2>0$, so $-a^2-b^2<0$. Furthermore, it is an integer. Thus, we have found a nonzero integer in $I$.
Qed.