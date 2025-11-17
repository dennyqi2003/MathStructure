Exercise 2.13 Suppose $f$ is an analytic function defined everywhere in $\mathbb{C}$ and such that for each $z_0 \in \mathbb{C}$ at least one coefficient in the expansion $f(z) = \sum_{n=0}^\infty c_n(z - z_0)^n$ is equal to 0. Prove that $f$ is a polynomial.
Proof.
Say that at least one of the coefficients of the Taylor series vanishes is the same as saying that for every $a \in \mathbb{C}$ there is $m \in \mathbb{N}$ such that $f^{(m)}(a)=0$.
Consider $A_n:=\left\{z \in \mathbb{C}: f^{(n)}(z)=0\right\}$ for each $n \in \mathbb{N}$. Note that:
$f$ is polynomial iff $A_n$ is not countable for some $n \in \mathbb{N}$.
Indeed, if $f$ is polynomial of degree $n$, then $f^{(n+1)}(z)=0$ for all $z \in \mathbb{C}$, then $A_{n+1}=\mathbb{C}$, so, $A_{n+1}$ is not countable. Conversely, if there is $n \in \mathbb{C}$ such that $A_n$ is not countable, then $A_n$ has a limit point, then by Identity principle we have $f^{(n)}(z)=0$ for all $z \in \mathbb{C}$, so, $f$ is a polynomial of degree at most $n-1$.

Therefore, tt suffices to show that there is $n \in \mathbb{N}$ such that $A_n$ is not countable. Indeed, consider $\bigcup_{n \in \mathbb{N}} A_n$, by hypothesis for each $a \in \mathbb{C}$ there is $m \in \mathbb{N}$ such that $f^{(m)}(a)=0$, then $\mathbb{C} \subseteq \bigcup_{n \in \mathbb{N}} A_n$. Therefore, $\bigcup_{n \in \mathbb{N}} A_n$ is not countable, then there is $n \in \mathbb{N}$ such that $A_n$ is not countable.
Qed.