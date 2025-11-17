Exercise 1.1.20 For $x$ an element in $G$ show that $x$ and $x^{-1}$ have the same order.
Proof.
Recall that the order of a group element is either a positive integer or infinity.
Suppose $|x|$ is infinite and that $\left|x^{-1}\right|=n$ for some $n$. Then
$$
x^n=x^{(-1) \cdot n \cdot(-1)}=\left(\left(x^{-1}\right)^n\right)^{-1}=1^{-1}=1,
$$
a contradiction. So if $|x|$ is infinite, $\left|x^{-1}\right|$ must also be infinite. Likewise, if $\left|x^{-1}\right|$ is infinite, then $\left|\left(x^{-1}\right)^{-1}\right|=|x|$ is also infinite.
Suppose now that $|x|=n$ and $\left|x^{-1}\right|=m$ are both finite. Then we have
$$
\left(x^{-1}\right)^n=\left(x^n\right)^{-1}=1^{-1}=1,
$$
so that $m \leq n$. Likewise, $n \leq m$. Hence $m=n$ and $x$ and $x^{-1}$ have the same order.
Qed.