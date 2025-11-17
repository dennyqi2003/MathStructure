Exercise 24.3a Let $f \colon X \rightarrow X$ be continuous. Show that if $X = [0, 1]$, there is a point $x$ such that $f(x) = x$. (The point $x$ is called a fixed point of $f$.)
Proof.
If $f(0)=0$ or $f(1)=1$ we are done, so suppose $f(0)>0$ and $f(1)<1$. Let $g:[0,1] \rightarrow[0,1]$ be given by $g(x)=f(x)-x$. Then $g$ is continuous, $g(0)>0$ and $g(1)<0$. Since $[0,1]$ is connected and $g(1)<0<g(0)$, by the intermediate value theorem there exists $x \in(0,1)$ such that $g(x)=0$, that is, such that $f(x)=x$.
Qed.