Exercise 2.2.6c Let $G$ be a group in which $(a b)^{n}=a^{n} b^{n}$ for some fixed integer $n>1$ for all $a, b \in G$. For all $a, b \in G$, prove that $\left(a b a^{-1} b^{-1}\right)^{n(n-1)}=e$.
Proof.
We start with the following two intermediate results.
(1) $(a b)^{n-1}=b^{n-1} a^{n-1}$.
(2) $a^n b^{n-1}=b^{n-1} a^n$.
To prove (1), notice by the given condition for all $a, b \in G$
$(b a)^n=b^n a^n$, for some fixed integers $n>1$.
Then,
$(b a)^n=b^n a^n \Longrightarrow b .(a b)(a b) \ldots .(a b) . a=b\left(b^{n-1} a^{n-1}\right) a$, where $(a b)$ occurs $n-1$ times $\Longrightarrow(a b)^{n-1}=b^{n-1} a^{n-1}$, by cancellation law.
Hence, for all $a, b \in G$
$$
(a b)^{n-1}=b^{n-1} a^{n-1} .
$$
To prove (2), notice by the given condition for all $a, b \in G$
$(b a)^n=b^n a^n$, for some fixed integers $n>1$.
Then we have
$$
\begin{aligned}
& (b a)^n=b^n a^n \\
\Longrightarrow & b \cdot(a b)(a b) \ldots(a b) \cdot a=b\left(b^{n-1} a^{n-1}\right) a, \text { where }(a b) \text { occurs } n-1 \text { times } \\
\Longrightarrow & (a b)^{n-1}=b^{n-1} a^{n-1}, \text { by cancellation law } \\
\Longrightarrow & (a b)^{n-1}(a b)=\left(b^{n-1} a^{n-1}\right)(a b) \\
\Longrightarrow & (a b)^n=b^{n-1} a^n b \\
\Longrightarrow & a^n b^n=b^{n-1} a^n b, \text { given condition } \\
\Longrightarrow & a^n b^{n-1}=b^{n-1} a^n, \text { by cancellation law. }
\end{aligned}
$$
Therefore for all $a, b \in G$ we have
$$
a^n b^{n-1}=b^{n-1} a^n
$$
In order to show that
$$
\left(a b a^{-1} b^{-1}\right)^{n(n-1)}=e, \text { for all } a, b \in G
$$
it is enough to show that
$$
(a b)^{n(n-1)}=(b a)^{n(n-1)}, \quad \forall x, y \in G .
$$
Step 3
This is because of
$$
\begin{aligned}
(a b)^{n(n-1)}=(b a)^{n(n-1)} & \left.\Longrightarrow(b a)^{-1}\right)^{n(n-1)}(a b)^{n(n-1)}=e \\
& \Longrightarrow\left(a^{-1} b^{-1}\right)^{n(n-1)}(a b)^{n(n-1)}=e \\
& \Longrightarrow\left(\left(a^{-1} b^{-1}\right)^n\right)^{n-1}\left((a b)^n\right)(n-1)=e \\
& \Longrightarrow\left((a b)^n\left(a^{-1} b^{-1}\right)^n\right)^{n-1}=e, \text { by }(1) \\
& \Longrightarrow\left(a b a^{-1} b^{-1}\right)^{n(n-1)}=e, \text { ( given condition) }
\end{aligned}
$$
Now, it suffices to show that
$$
(a b)^{n(n-1)}=(b a)^{n(n-1)}, \quad \forall x, y \in G .
$$
Now, we have
$$
\begin{aligned}
(a b)^{n(n-1)} & =\left(a^n b^n\right)^{n-1}, \text { by the given condition } \\
& =\left(a^n b^{n-1} b\right)^{n-1} \\
& =\left(b^{n-1} a^n b\right)^{n-1}, \text { by }(2) \\
& =\left(a^n b\right)^{n-1}\left(b^{n-1}\right)^{n-1}, \text { by }(1) \\
& =b^{n-1}\left(a^n\right)^{n-1}\left(b^{n-1}\right)^{n-1}, \text { by }(1) \\
& =\left(b^{n-1}\left(a^{n-1}\right)^n\right)\left(b^{n-1}\right)^{n-1} \\
& =\left(a^{n-1}\right)^n b^{n-1}\left(b^{n-1}\right)^{n-1}, \text { by }(2) \\
& =\left(a^{n-1}\right)^n\left(b^{n-1}\right)^n \\
& =\left(a^{n-1} b^{n-1}\right)^n, \text { by }(1) \\
& =(b a)^{n(n-1)}, \text { by }(1) .
\end{aligned}
$$
This completes our proof.
Qed.