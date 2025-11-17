Exercise 2018.b4 Given a real number $a$, we define a sequence by $x_{0}=1$, $x_{1}=x_{2}=a$, and $x_{n+1}=2 x_{n} x_{n-1}-x_{n-2}$ for $n \geq 2$. Prove that if $x_{n}=0$ for some $n$, then the sequence is periodic.
Proof.
We first rule out the case $|a|>1$. In this case, we prove that $|x_{n+1}| \geq |x_n|$ for all $n$, meaning that we cannot have $x_n = 0$. We proceed by induction; the claim is true for $n=0,1$ by hypothesis. To prove the claim for  $n \geq 2$, write
\begin{align*}
|x_{n+1}| &= |2x_nx_{n-1}-x_{n-2}| \\
&\geq 2|x_n||x_{n-1}|-|x_{n-2}| \\
&\geq |x_n|(2|x_{n-1}|-1) \geq |x_n|,
\end{align*} 
where the last step follows from $|x_{n-1}| \geq |x_{n-2}| \geq \cdots \geq |x_0| = 1$.

We may thus assume hereafter that $|a|\leq 1$. We can then write $a = \cos b$ for some $b \in [0,\pi]$. 
Let $\{F_n\}$ be the Fibonacci sequence, defined as usual by $F_1=F_2=1$ and $F_{n+1}=F_n+F_{n-1}$. We show by induction that
\[
x_n = \cos(F_n b) \qquad (n \geq 0).
\]
Indeed, this is true for $n=0,1,2$; given that it is true for $n \leq m$, then
\begin{align*}
2x_mx_{m-1}&=2\cos(F_mb)\cos(F_{m-1}b) \\
&= \cos((F_m-F_{m-1})b)+\cos((F_m+F_{m-1})b) \\
&= \cos(F_{m-2}b)+\cos(F_{m+1}b)
\end{align*}
and so 
$x_{m+1} = 2x_mx_{m-1}-x_{m-2} = \cos(F_{m+1}b)$. This completes the induction.


Since $x_n = \cos(F_n b)$, if $x_n=0$ for some $n$ then $F_n b = \frac{k}{2} \pi$ for some odd integer $k$. In particular, we can write $b = \frac{c}{d}(2\pi)$ where $c = k$ and $d = 4F_n$ are integers.


Let $x_n$ denote the pair $(F_n,F_{n+1})$, where each entry in this pair is viewed as an element of $\mathbb{Z}/d\mathbb{Z}$. Since there are only finitely many possibilities for $x_n$, there must be some $n_2>n_1$ such that $x_{n_1}=x_{n_2}$. Now $x_n$ uniquely determines both $x_{n+1}$ and $x_{n-1}$, and it follows that the sequence $\{x_n\}$ is periodic: for $\ell = n_2-n_1$, $x_{n+\ell} = x_n$ for all $n \geq 0$. In particular, $F_{n+\ell} \equiv F_n \pmod{d}$ for all $n$. But then $\frac{F_{n+\ell}c}{d}-\frac{F_n c}{d}$ is an integer, and so
\begin{align*}
x_{n+\ell} &= \cos\left(\frac{F_{n+\ell}c}{d}(2\pi)\right)\\
& = \cos\left(\frac{F_n c}{d}(2\pi)\right) = x_n
\end{align*}
for all $n$. Thus the sequence $\{x_n\}$ is periodic, as desired.
Qed.