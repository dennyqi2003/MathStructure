Exercise 1998.a3 Let $f$ be a real function on the real line with continuous third derivative. Prove that there exists a point $a$ such that
$f(a) \cdot f^{\prime}(a) \cdot f^{\prime \prime}(a) \cdot f^{\prime \prime \prime}(a) \geq 0$.
Proof.
If at least one of $f(a)$, $f'(a)$, $f''(a)$, or $f'''(a)$ vanishes
at some point $a$, then we are done.  Hence we may assume each of
$f(x)$, $f'(x)$, $f''(x)$, and $f'''(x)$ is either strictly positive
or strictly negative on the real line.  By replacing $f(x)$ by $-f(x)$
if necessary, we may assume $f''(x)>0$; by replacing $f(x)$
by $f(-x)$ if necessary, we may assume $f'''(x)>0$.  (Notice that these
substitutions do not change the sign of $f(x) f'(x) f''(x) f'''(x)$.)
Now $f''(x)>0$ implies that $f'(x)$ is increasing, and $f'''(x)>0$
implies that $f'(x)$ is convex, so that $f'(x+a)>f'(x)+a f''(x)$
for all $x$ and $a$.  By
letting $a$ increase in the latter inequality, we see that $f'(x+a)$
must be positive for sufficiently large $a$; it follows that
$f'(x)>0$
for all $x$.  Similarly, $f'(x)>0$ and $f''(x)>0$ imply
that $f(x)>0$ for all $x$.  Therefore $f(x) f'(x) f''(x) f'''(x)>0$ for
all $x$, and we are done.
Qed.