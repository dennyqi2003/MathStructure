Exercise 2.1.26 If $G$ is a finite group, prove that, given $a \in G$, there is a positive integer $n$, depending on $a$, such that $a^n = e$.
Proof.
Because there are only a finite number of elements of $G$, it's clear that the set $\left\{a, a^2, a^3, \ldots\right\}$ must be a finite set and in particular, there should exist some $i$ and $j$ such that $i \neq j$ and $a^i=a^j$. WLOG suppose further that $i>j$ (just reverse the roles of $i$ and $j$ otherwise). Then multiply both sides by $\left(a^j\right)^{-1}=a^{-j}$ to get
$$
a^i * a^{-j}=a^{i-j}=e
$$
Thus the $n=i-j$ is a positive integer such that $a^n=e$.
Qed.