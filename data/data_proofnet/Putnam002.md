Exercise 2018.a5 Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be an infinitely differentiable function satisfying $f(0)=0, f(1)=1$, and $f(x) \geq 0$ for all $x \in$ $\mathbb{R}$. Show that there exist a positive integer $n$ and a real number $x$ such that $f^{(n)}(x)<0$.
Proof.
Call a function $f\colon \mathbb{R} \to \mathbb{R}$ \textit{ultraconvex} if $f$ is infinitely differentiable and $f^{(n)}(x) \geq 0$ for all $n \geq 0$ and all $x \in \mathbb{R}$, where $f^{(0)}(x) = f(x)$;
note that if $f$ is ultraconvex, then so is $f'$.
Define the set
\[
S = \{ f :\thinspace \mathbb{R} \to \mathbb{R} \,|\,f \text{ ultraconvex and } f(0)=0\}.
\]
For $f \in S$, we must have $f(x) = 0$ for all $x < 0$: if $f(x_0) > 0$ for some $x_0 < 0$, then
by the mean value theorem there exists $x \in (0,x_0)$ for which $f'(x) = \frac{f(x_0)}{x_0} < 0$.
In particular, $f'(0) = 0$, so $f' \in S$ also.

We show by induction that for all $n \geq 0$,
\[
f(x) \leq \frac{f^{(n)}(1)}{n!} x^n \qquad (f \in S, x \in [0,1]).
\]
We induct with base case $n=0$, which holds because any $f \in S$ is nondecreasing. Given the claim for $n=m$,
we apply the induction hypothesis to $f' \in S$ to see that
\[
f'(t) \leq \frac{f^{(n+1)}(1)}{n!} t^n \qquad (t \in [0,1]),
\]
then integrate both sides from $0$ to $x$ to conclude.

Now for $f \in S$, we have $0 \leq f(1) \leq \frac{f^{(n)}(1)}{n!}$ for all $n \geq 0$. 
On the other hand, by Taylor's theorem with remainder,
\[
f(x) \geq \sum_{k=0}^n \frac{f^{(k)}(1)}{k!}(x-1)^k \qquad (x \geq 1).
\]
Applying this with $x=2$, we obtain $f(2) \geq \sum_{k=0}^n \frac{f^{(k)}(1)}{k!}$ for all $n$;
this implies that $\lim_{n\to\infty}  \frac{f^{(n)}(1)}{n!} = 0$.
Since $f(1) \leq \frac{f^{(n)}(1)}{n!}$, we must have $f(1) = 0$.

For $f \in S$, we proved earlier that $f(x) = 0$ for all $x\leq 0$, as well as for $x=1$. Since
the function $g(x) = f(cx)$ is also ultraconvex for $c>0$, we also have $f(x) = 0$ for all $x>0$;
hence $f$ is identically zero.

To sum up, if $f\colon \mathbb{R} \to \mathbb{R}$ is infinitely differentiable, $f(0)=0$, and $f(1) = 1$,
then $f$ cannot be ultraconvex. This implies the desired result.
Qed.