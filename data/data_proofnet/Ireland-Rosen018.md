Exercise 5.28 Show that $x^{4} \equiv 2(p)$ has a solution for $p \equiv 1(4)$ iff $p$ is of the form $A^{2}+64 B^{2}$.
Proof.
If  $p\equiv 1\ [4]$ and if there exists $x \in \mathbb{Z}$ such that $x^4 \equiv 2\ [p]$, then
$$2^{\frac{p-1}{4} }\equiv  x^{p-1} \equiv 1 \ [p].$$ 

From Ex. 5.27, where $p = a^2 +b^2, a$ odd,  we know that $$f^{\frac{ab}{2}} \equiv 2^{\frac{p-1}{4} } \equiv 1 \ [p].$$

Since $f^2 \equiv -1\ [p]$, the order of $f$ modulo $p$ is 4, thus $4 \mid \frac{ab}{2}$, so $8\mid ab$.

As $a$ is odd, $8 | b$, then $p = A^2 + 64 B^2$ (with $A = a, B = b/8$).

\bigskip

Conversely, if $p=A^2+64 B^2$, then $p\equiv A^2 \equiv 1 \ [4]$.

Let $a=A,b=8B$. Then $$2^{\frac{p-1}{4} } \equiv f^{\frac{ab}{2}} \equiv f^{4AB} \equiv (-1)^{2AB} \equiv 1 \ [p].$$

As $2^{\frac{p-1}{4} } \equiv 1 \ [p]$, $x^4 \equiv 2 \ [p]$ has a solution in $\mathbb{Z}$ (Prop. 4.2.1) : $2$ is a biquadratic residue modulo $p$.

Conclusion : 

$$\exists A \in \mathbb{Z}, \exists B \in \mathbb{Z}\,, p = A^2+64 B^2 \iff( p\equiv 1 \ [4] \ \mathrm{and} \ \exists x \in \mathbb{Z}, \, x^4 \equiv 2 \ [p]).$$
Qed.