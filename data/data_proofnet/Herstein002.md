Exercise 2.1.21 Show that a group of order 5 must be abelian.
Proof.
Suppose $G$ is a group of order 5 which is not abelian. Then there exist two non-identity elements $a, b \in G$ such that $a * b \neq$ $b * a$. Further we see that $G$ must equal $\{e, a, b, a * b, b * a\}$. To see why $a * b$ must be distinct from all the others, not that if $a *$ $b=e$, then $a$ and $b$ are inverses and hence $a * b=b * a$.
Contradiction. If $a * b=a$ (or $=b$ ), then $b=e$ (or $a=e$ ) and $e$ commutes with everything. Contradiction. We know by supposition that $a * b \neq b * a$. Hence all the elements $\{e, a, b, a * b, b * a\}$ are distinct.

Now consider $a^2$. It can't equal $a$ as then $a=e$ and it can't equal $a * b$ or $b * a$ as then $b=a$. Hence either $a^2=e$ or $a^2=b$.
Now consider $a * b * a$. It can't equal $a$ as then $b * a=e$ and hence $a * b=b * a$. Similarly it can't equal $b$. It also can't equal $a * b$ or $b * a$ as then $a=e$. Hence $a * b * a=e$.

So then we additionally see that $a^2 \neq e$ because then $a^2=e=$ $a * b * a$ and consequently $a=b * a$ (and hence $b=e$ ). So $a^2=b$. But then $a * b=a * a^2=a^2 * a=b * a$. Contradiction.
Hence starting with the assumption that there exists an order 5 abelian group $G$ leads to a contradiction. Thus there is no such group.
Qed.