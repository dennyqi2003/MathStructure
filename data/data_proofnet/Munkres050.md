Exercise 31.3 Show that every order topology is regular.
Proof.
Let $X$ be an ordered set.
First we show that $X$ is a $T_1$-space. For $x \in X$ we have that
$$
X \backslash\{x\}=\langle-\infty, x\rangle \cup\langle x,+\infty\rangle
$$
which is an open set as an union of two open intervals. Therefore, the set $\{x\}$ is closed.
Step 2
2 of 3
Now to prove that $X$ is regular we use Lemma $\mathbf{3 1 . 1 .}$
Let $x \in X$ be any point and $U \subseteq X$ any open neighborhood of $x$. Then there exist $a, b \in X$ such that $x \in\langle a, b\rangle \subseteq U$. Now we have four possibilities.
1. If there exist $x_1, x_2 \in U$ such that $a<x_1<x<x_2<b$, then
$$
x \in\left\langle x_1, x_2\right\rangle \subseteq \overline{\left\langle x_1, x_2\right\rangle} \subseteq\left[x_1, x_2\right] \subseteq\langle a, b\rangle \subseteq U
$$
2. If there exists $x_1 \in U$ such that $a<x_1<x$, but there's no $x_2 \in U$ such that $x<x_2<b$, then
$$
x \in\left\langle x_1, b\right\rangle=\left(x_1, x\right] \subseteq \overline{\left(x_1, x\right]} \subseteq\left[x_1, x\right] \subseteq\langle a, b\rangle \subseteq U
$$
3. If there exists $x_2 \in U$ such that $x<x_2<b$, but there's no $x_1 \in U$ such that $a<x_1<x$, then
$$
x \in\left\langle a, x_2\right\rangle=\left[x, x_2\right) \subseteq \overline{\left[x, x_2\right)} \subseteq\left[x, x_2\right] \subseteq\langle a, b\rangle \subseteq U
$$
4. If there's no $x_1 \in U$ such that $a<x_1<x$ and no $x_2 \in U$ such that $x<x_2<b$, then
$$
x \in\langle a, b\rangle=\{x\}=\overline{\{x\}}=\{x\} \subseteq U
$$
We have that $\overline{\{x\}}=\{x\}$ because $X$ is a $T_1$-space.
In all four cases we proved that there exists an open interval $V$ such that $x \in V \subseteq \bar{V} \subseteq U$, so $X$ is regular.
Qed.