Exercise 3.3 Show that $ \int_{-\infty}^{\infty} \frac{\cos x}{x^2 + a^2} dx = \pi \frac{e^{-a}}{a}$ for $a > 0$.
Proof.
$\cos x=\frac{e^{i x}+e^{-i x}}{2}$. changing $x \rightarrow-x$ we see that we can just integrate $e^{i x} /\left(x^2+a^2\right)$ and we'll get the same answer. Again, we use the same semicircle and part of the real line. The only pole is $x=i a$, it has order 1 and the residue at it is $\lim _{x \rightarrow i a} \frac{e^{i x}}{x^2+a^2}(x-i a)=\frac{e^{-a}}{2 i a}$, which multiplied by $2 \pi i$ gives the answer.
Qed.