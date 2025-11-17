Exercise 1999.b4 Let $f$ be a real function with a continuous third derivative such that $f(x), f^{\prime}(x), f^{\prime \prime}(x), f^{\prime \prime \prime}(x)$ are positive for all $x$. Suppose that $f^{\prime \prime \prime}(x) \leq f(x)$ for all $x$. Show that $f^{\prime}(x)<2 f(x)$ for all $x$.
Proof.
\setcounter{equation}{0}
We make repeated use of the following fact: if $f$ is a differentiable function on all of
$\mathbb{R}$, $\lim_{x \to -\infty} f(x) \geq 0$, and $f'(x) > 0$ for all $x \in \mathbb{R}$, then
$f(x) > 0$ for all $x \in \mathbb{R}$. (Proof: if $f(y) < 0$ for some $x$, then $f(x)< f(y)$ for all
$x<y$ since $f'>0$, but then $\lim_{x \to -\infty} f(x) \leq f(y) < 0$.)

From the inequality $f'''(x) \leq f(x)$ we obtain
\[
f'' f'''(x) \leq f''(x) f(x) < f''(x) f(x) + f'(x)^2
\]
since $f'(x)$ is positive. Applying the fact to the difference between the right and left sides,
we get
\begin{equation}
\frac{1}{2} (f''(x))^2 < f(x) f'(x).
\end{equation}

On the other hand, since $f(x)$ and $f'''(x)$ are both positive for all $x$,
we have
\[
2f'(x) f''(x) < 2f'(x)f''(x) + 2f(x) f'''(x).
\]
Applying the fact to the difference between the sides yields
\begin{equation}
f'(x)^2 \leq 2f(x) f''(x).
\end{equation}
Combining (1) and (2), we obtain
\begin{align*}
\frac{1}{2} \left( \frac{f'(x)^2}{2f(x)} \right)^2
&< \frac{1}{2} (f''(x))^2 \\
&< f(x) f'(x),
\end{align*}
or $(f'(x))^3 < 8 f(x)^3$. We conclude $f'(x) < 2f(x)$, as desired.
Qed.