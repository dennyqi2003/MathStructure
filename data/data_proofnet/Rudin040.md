Exercise 4.5b Show that there exist a set $E \subset \mathbb{R}$ and a real continuous function $f$ defined on $E$, such that there does not exist a continuous real function $g$ on $\mathbb{R}$ such that $g(x)=f(x)$ for all $x \in E$.
Proof.
Let $E:=(0,1)$, and define $f(x):=1 / x$ for all $x \in E$. If $f$ has a continuous extension $g$ to $\mathbb{R}$, then $g$ is continuous on $[-1,1]$, and therefore bounded by the intermediate value theorem. However, $f$ is not bounded in any neighborhood of $x=0$, so therefore $g$ is not bounded either, a contradiction.
Qed.