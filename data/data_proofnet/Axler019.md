Exercise 6.3 Prove that $\left(\sum_{j=1}^{n} a_{j} b_{j}\right)^{2} \leq\left(\sum_{j=1}^{n} j a_{j}{ }^{2}\right)\left(\sum_{j=1}^{n} \frac{b_{j}{ }^{2}}{j}\right)$ for all real numbers $a_{1}, \ldots, a_{n}$ and $b_{1}, \ldots, b_{n}$.
Proof.
Let $a_1, a_2, \ldots, a_n, b_1, b_2, \ldots, b_n \in R$.
We have that
$$
\left(\sum_{j=1}^n a_j b_j\right)^2
$$
is equal to the
$$
\left(\sum_{j=1}^n a_j b_j \frac{\sqrt{j}}{\sqrt{j}}\right)^2=\left(\sum_{j=1}^n\left(\sqrt{j} a_j\right)\left(b_j \frac{1}{\sqrt{j}}\right)\right)^2
$$
This can be observed as an inner product, and using the Cauchy-Schwarz Inequality, we get
$$
\begin{aligned}
&\left(\sum_{j=1}^n a_j b_j\right)^2=\left(\sum_{j=1}^n\left(\sqrt{j} a_j\right)\left(b_j \frac{1}{\sqrt{j}}\right)\right)^2 \\
&=\left\langle\left(a, \sqrt{2} a_2, \ldots, \sqrt{n} a_n\right),\left(b_1, \frac{b_2}{\sqrt{2}}, \ldots, \frac{b_n}{\sqrt{n}}\right)\right\rangle \\
& \leq\left\|\left(a, \sqrt{2} a_2, \ldots, \sqrt{n} a_n\right)\right\|^2\left\|\left(b_1, \frac{b_2}{\sqrt{2}}, \ldots, \frac{b_n}{\sqrt{n}}\right)\right\|^2 \\
&=\left(\sum_{j=1}^n j a_j^2\right)\left(\sum_{j=1}^n \frac{b_j^2}{j}\right) \\
& \text { Hence, }\left(\sum_{j=1}^n a_j b_j\right)^2=\left(\sum_{j=1}^n j a_j^2\right)\left(\sum_{j=1}^n \frac{b_j^2}{j}\right) .
\end{aligned}
$$
Qed.