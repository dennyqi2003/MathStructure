Exercise 5.6.14 If $F$ is of characteristic $p \neq 0$, show that all the roots of $x^m - x$, where $m = p^n$, are distinct.
Proof.
Let us consider $f(x)=x^m-x$. Then $f \in F[x]$.
Claim: $f(x)$ has a multiple root in some extension of $F$ if and only if $f(x)$ is not relatively prime to its formal derivative, $f^{\prime}(x)$. 

Proof of the Claim: Let us assume that $f(x)$ has a multiple root in some extension of $F$. Let $y$ be a multiple root of $f(x)$. Then over a splitting field, we have
$$
f(x)=(x-y)^n g(x), \text { for some integer } n \geq 2 .
$$
Here $g(x)$ is a polynomial such that $g(y) \neq 0$. Now taking derivative of $f$ we get
$$
f^{\prime}(x)=n \cdot(x-y)^{n-1} g(x)+(x-y)^n g^{\prime}(x)
$$
here $g^{\prime}(x)$ implies derivative of $g$ with respect to $x$. Since we have $n \geq 2$, this implies $(n-1) \geq 1$. Hence, (1) shows that $f^{\prime}(x)$ has $y$ as a root. Therefore, $f(x)$ is not relatively prime to $f^{\prime}(x)$. We now prove the other direction.
Conversely, let us assume that $f(x)$ is not relatively prime to $f^{\prime}(x)$. Let $y$ is a root of both $f(x)$ and $f^{\prime}(x)$. Since $y$ is a root of $f(x)$, we can write
$$
f(x)=(x-y) \cdot g(x)
$$
for some polynomial $g(x)$. then taking derivative of $f(x)$ we have
$$
f^{\prime}(x)=g(x)+(x-y) \cdot g^{\prime}(x)
$$
where $g^{\prime}(x)$ is the derivative of $g(x)$ with respect to $x$. Since $y$ is a root of $f^{\prime}(x)$ also we have
$$
f^{\prime}(y)=0
$$
Then we have
$$
\begin{aligned}
& f^{\prime}(y)=g(y)+(y-y) \cdot g^{\prime}(y) \\
\Longrightarrow & f^{\prime}(y)=g(y) \\
\Longrightarrow & g(y)=0 .
\end{aligned}
$$
This implies $y$ is a root of $g(x)$ also. Therefore we have
$$
g(x)=(x-y) \cdot h(x)
$$
for some polynomial $h(x)$. Now form (2) we have
$$
f(x)=(x-y)^2 \cdot h(x) .
$$
This follows that $y$ is a multiple root of $f(x)$. Therefore, $f(x)$ has a multiple root in some extension of the field $F$. This completes the proof of the Claim.

In our case, $f(x)=x^m-x$, where $m=p^n$. Now we calculate the derivative of $f$. That is
$$
f^{\prime}(x)=m x^{m-1}-1=-1(\bmod p) .
$$
By the above condition it follows that, $f^{\prime}$ has no root same as $f$, that is, $f(x)$ and $f^{\prime}(x)$ are relatively prime. Hence, $f(x)$ has no multiple root in $F$. Since $f(x)=x^m-x$ is a polynomial of degree $m$, it follows that $f(x)$ has $m$ distinct roots in $F$, where $m=p^n$. This completes the proof.
Qed.