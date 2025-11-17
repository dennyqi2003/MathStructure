Exercise 2014.a5 Let
$P_n(x)=1+2 x+3 x^2+\cdots+n x^{n-1} .$ Prove that the polynomials $P_j(x)$ and $P_k(x)$ are relatively prime for all positive integers $j$ and $k$ with $j \neq k$.
Proof.
Suppose to the contrary that there exist positive integers $i \neq j$ and a complex number $z$ such that $P_i(z) = P_j(z) = 0$. Note that $z$ cannot be a nonnegative real number or else $P_i(z), P_j(z) > 0$; we may put $w = z^{-1} \neq 0,1$. For $n \in \{i+1,j+1\}$ we compute that
\[
w^n = n w - n + 1,
\qquad \overline{w}^n =  n \overline{w} - n + 1;
\]
note crucially that these equations also hold for $n \in \{0,1\}$.
Therefore, the function $f: [0, +\infty) \to \mathbb{R}$ given by
\[
f(t) = \left| w \right|^{2t} - t^2 \left| w \right|^2 + 2t(t-1)\mathrm{Re}(w) - (t-1)^2
\]
satisfies $f(t) = 0$ for $t \in \{0,1,i+1,j+1\}$. On the other hand, for all $t \geq 0$ we have
\[
f'''(t) = (2 \log \left| w \right|)^3 \left| w \right|^{2t} > 0,
\]
so by Rolle's theorem, the equation $f^{(3-k)}(t) = 0$ has at most $k$ distinct solutions for $k=0,1,2,3$. This yields the desired contradiction.
Qed.