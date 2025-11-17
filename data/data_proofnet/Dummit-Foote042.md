Exercise 4.3.26 Let $G$ be a transitive permutation group on the finite set $A$ with $|A|>1$. Show that there is some $\sigma \in G$ such that $\sigma(a) \neq a$ for all $a \in A$.
Proof.
Let $G$ be a transitive permutation group on the finite set $A,|A|>1$. We want to find an element $\sigma$ which doesn't stabilize anything, that is, we want a $\sigma$ such that
$$
\sigma \notin G_a
$$
for all $a \in A$.
Since the group is transitive, there is always a $g \in G$ such that $b=g \cdot a$. Let us see in what relationship the stabilizers of $a$ and $b$ are. We find
$$
\begin{aligned}
G_b & =\{h \in G \mid h \cdot b=b\} \\
& =\{h \in G \mid h g \cdot a=g \cdot a\} \\
& =\left\{h \in G \mid g^{-1} h g \cdot a=a\right\}
\end{aligned}
$$
Putting $h^{\prime}=g^{-1} h g$, we have $h=g h^{\prime} g^{-1}$ and
$$
\begin{aligned}
G_b & =g\left\{h^{\prime} \in H \mid h^{\prime} \cdot a=a\right\} g^{-1} \\
& =g G_a g^{-1}
\end{aligned}
$$
By the above, the stabilizer subgroup of any element is conjugate to some other stabilizer subgroup. Now, the stabilizer cannot be all of $G$ (else $\{a\}$ would be a orbit). Thus it is a proper subgroup of $G$. By the previous exercise, we have
$$
\bigcup_{a \in A} G_a=\bigcup_{g \in G} g G_a g^{-1} \subset G
$$
(the union of conjugates of a proper subgroup can never be all of $G$ ). This shows there is an element $\sigma$ which is not in any stabilizer of any element of $A$. Then $\sigma(a) \neq a$ for all $a \in A$, as we wanted to show.
Qed.