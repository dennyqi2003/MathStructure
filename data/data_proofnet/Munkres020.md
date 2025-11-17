Exercise 20.2 Show that $\mathbb{R} \times \mathbb{R}$ in the dictionary order topology is metrizable.
Proof.
The dictionary order topology on $\mathbb{R} \times \mathbb{R}$ is the same as the product topology $\mathbb{R}_d \times \mathbb{R}$, where $\mathbb{R}_d$ denotes $\mathbb{R}$ with the discrete topology. We know that $\mathbb{R}_d$ and $\mathbb{R}$ are metrisable. Thus, it suffices to show that the product of two metrisable spaces is metrisable.
So let $X$ and $Y$ be metrisable spaces, with metrics $d$ and $d^{\prime}$ respectively. On $X \times Y$, define
$$
\rho(x \times y, w \times z)=\max \left\{d(x, w), d^{\prime}(y, z)\right\} .
$$
Then $\rho$ is a metric on $X \times Y$; it remains to prove that it induces the product topology on $X \times Y$. If $B_d\left(x, r_1\right) \times B_d\left(y, r_2\right)$ is a basis element for the product space $X \times Y$, and $r=\min \left\{r_1, r_2\right\}$, then $x \times y \in B_\rho(x \times y, r) \subset B_d\left(x, r_1\right) \times B_d\left(y, r_2\right)$, so the product topology is coarser than the $\rho$-topology. Conversely, if $B_\rho(x \times y, \delta)$ is a basis element for the $\rho$-topology, then $x \times y \in B_d(x, \delta) \times B_{d^{\prime}}(y, \delta) \subset$ $B_\rho(x \times y, \delta)$, so the product topology is finer than the $\rho$-topology. It follows that both topologies are equal, so the product space $X \times Y$ is metrisable.
Qed.