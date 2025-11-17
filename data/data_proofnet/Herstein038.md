Exercise 4.5.25 If $p$ is a prime, show that $q(x) = 1 + x + x^2 + \cdots x^{p - 1}$ is irreducible in $Q[x]$.
Proof.
Lemma: Let $F$ be a field and $f(x) \in F[x]$. If $c \in F$ and $f(x+c)$ is irreducible in $F[x]$, then $f(x)$ is irreducible in $F[x]$.
Proof of the Lemma: Suppose that $f(x)$ is reducible, i.e., there exist non-constant $g(x), h(x) \in F[x]$ so that
$$
f(x)=g(x) h(x) .
$$
In particular, then we have
$$
f(x+c)=g(x+c) h(x+c) .
$$
Note that $g(x+c)$ and $h(x+c)$ have the same degree at $g(x)$ and $h(x)$ respectively; in particular, they are non-constant polynomials. So our assumption is wrong.
Hence, $f(x)$ is irreducible in $F[x]$. This proves our Lemma.

Now recall the identity
$$
\frac{x^p-1}{x-1}=x^{p-1}+x^{p-2}+\ldots \ldots+x^2+x+1 .
$$
We prove that $f(x+1)$ is $\$$ |textbffirreducible in $\mathbb{Q}[x]$ and then apply the Lemma to conclude that $f(x)$ is irreducible in $\mathbb{Q}[x] .3 \$$ Note that
$$
\begin{aligned}
& f(x+1)=\frac{(x+1)^p-1}{x} \\
& =\frac{x^p+p x^{p-1}+\ldots+p x}{x} \\
& =x^{p-1}+p x^{p-2}+\ldots .+p .
\end{aligned}
$$
Using that the binomial coefficients occurring above are all divisible by $p$, we have that $f(x+1)$ is irreducible $\mathbb{Q}[x]$ by Eisenstein's criterion applied with prime $p$. 

Then by the lemma $f(x)$ is irreducible $\mathbb{Q}[x]$. This completes the proof.
Qed.