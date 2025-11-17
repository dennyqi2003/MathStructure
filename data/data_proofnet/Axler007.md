Exercise 1.9 Prove that the union of two subspaces of $V$ is a subspace of $V$ if and only if one of the subspaces is contained in the other.
Proof.
To prove this one way, suppose for purposes of contradiction that for $U_1$ and $U_2$, which are subspaces of $V$, that $U_1 \cup U_2$ is a subspace and neither is completely contained within the other. In other words, $U_1 \nsubseteq U_2$ and $U_2 \nsubseteq U_1$. We will show that you can pick a vector $v \in U_1$ and a vector $u \in U_2$ such that $v+u \notin U_1 \cup U_2$, proving that if $U_1 \cup U_2$ is a subspace, one must be completely contained inside the other.

If $U_1 \nsubseteq U_2$, we can pick a $v \in U_1$ such that $v \notin U_2$. Since $v$ is in the subspace $U_1$, then $(-v)$ must also be, by definition. Similarly, if $U_2 \nsubseteq U_1$, then we can pick a $u \in U_2$ such that $u \notin U_1$. Since $u$ is in the subspace $U_2$, then $(-u)$ must also be, by definition.

If $v+u \in U_1 \cup U_2$, then $v+u$ must be in $U_1$ or $U_2$. But, $v+u \in U_1 \Rightarrow v+u+(-v) \in U_1 \Rightarrow u \in U_1$
Similarly,
$$
v+u \in U_2 \Rightarrow v+u+(-u) \in U_2 \Rightarrow v \in U_2
$$
This is clearly a contradiction, as each element was defined to not be in these subspaces. Thus our initial assumption must have been wrong, and $U_1 \subseteq U_2$ or $U_2 \subseteq U_1$
To prove the other way, Let $U_1 \subseteq U_2$ (WLOG). $U_1 \subseteq U_2 \Rightarrow U_1 \cup U_2=U_2$. Since $U_2$ is a subspace, $U_1 \cup U_2$ is as well. QED.
Qed.