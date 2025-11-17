Exercise 2.29 Prove that every open set in $\mathbb{R}$ is the union of an at most countable collection of disjoint segments.
Proof.
Let $O$ be open. For each pair of points $x \in O, y \in O$, we define an equivalence relation $x \sim y$ by saying $x \sim y$ if and only if $[\min (x, y), \max (x, y)] \subset$ 0 . This is an equivalence relation, since $x \sim x([x, x] \subset O$ if $x \in O)$; if $x \sim y$, then $y \sim x$ (since $\min (x, y)=\min (y, x)$ and $\max (x, y)=\max (y, x))$; and if $x \sim y$ and $y \sim z$, then $x \sim z([\min (x, z), \max (x, z)] \subseteq[\min (x, y), \max (x, y)] \cup$ $[\min (y, z), \max (y, z)] \subseteq O)$. In fact it is easy to prove that
$$
\min (x, z) \geq \min (\min (x, y), \min (y, z))
$$
and
$$
\max (x, z) \leq \max (\max (x, y), \max (y, z))
$$
It follows that $O$ can be written as a disjoint union of pairwise disjoint equivalence classes. We claim that each equivalence class is an open interval.

To show this, for each $x \in O$; let $A=\{z:[z, x] \subseteq O\}$ and $B=\{z:[x, z] \subseteq$ $O\}$, and let $a=\inf A, b=\sup B$. We claim that $(a, b) \subset O$. Indeed if $a<z<b$, there exists $c \in A$ with $c<z$ and $d \in B$ with $d>z$. Then $z \in[c, x] \cup[x, d] \subseteq O$. We now claim that $(a, b)$ is the equivalence class containing $x$. It is clear that each element of $(a, b)$ is equivalent to $x$ by the way in which $a$ and $b$ were chosen. We need to show that if $z \notin(a, b)$, then $z$ is not equivalent to $x$. Suppose that $z<a$. If $z$ were equivalent to $x$, then $[z, x]$ would be contained in $O$, and so we would have $z \in A$. Hence $a$ would not be a lower bound for $A$. Similarly if $z>b$ and $z \sim x$, then $b$ could not be an upper bound for $B$.

We have now established that $O$ is a union of pairwise disjoint open intervals. Such a union must be at most countable, since each open interval contains a rational number not in any other interval.
Qed.