Exercise 3.5 Show that the equation $7 x^{3}+2=y^{3}$ has no solution in integers.
Proof.
If $7x^2 + 2 = y^3,\ x,y \in \mathbb{Z}$, then $y^3 \equiv 2 \pmod 7$ (so $y \not \equiv 0 \pmod 7$)

From Fermat's Little Theorem, $y^6 \equiv 1 \pmod 7$, so $2^2 \equiv y^6 \equiv 1 \pmod 7$, which implies $7 \mid 2^2-1 = 3$ : this is a contradiction. Thus the equation $7x^2 + 2 = y^3$ has no solution in integers.
Qed.