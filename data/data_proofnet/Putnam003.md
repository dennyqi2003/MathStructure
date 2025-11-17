Exercise 2018.b2 Let $n$ be a positive integer, and let $f_{n}(z)=n+(n-1) z+$ $(n-2) z^{2}+\cdots+z^{n-1}$. Prove that $f_{n}$ has no roots in the closed unit disk $\{z \in \mathbb{C}:|z| \leq 1\}$.
Proof.
Note first that $f_n(1) > 0$, so $1$ is not a root of $f_n$.
Next, note that
\[
(z-1)f_n(z) = z^n + \cdots + z - n;
\]
however, for $\left| z \right| \leq 1$, we have 
$\left| z^n + \cdots + z \right| \leq n$ by the triangle inequality;
equality can only occur if $z,\dots,z^n$ have norm 1 and the same argument, which only happens for $z=1$.
Thus there can be no root of $f_n$ with $|z| \leq 1$.
Qed.