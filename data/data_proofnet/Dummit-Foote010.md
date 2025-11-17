Exercise 1.1.22a If $x$ and $g$ are elements of the group $G$, prove that $|x|=\left|g^{-1} x g\right|$.
Proof.
First we prove a technical lemma:

    {\bf Lemma.} For all $a, b \in G$ and $n \in \mathbb{Z},\left(b^{-1} a b\right)^n=b^{-1} a^n b$.
The statement is clear for $n=0$. We prove the case $n>0$ by induction; the base case $n=1$ is clear. Now suppose $\left(b^{-1} a b\right)^n=b^{-1} a^n b$ for some $n \geq 1$; then
$$
\left(b^{-1} a b\right)^{n+1}=\left(b^{-1} a b\right)\left(b^{-1} a b\right)^n=b^{-1} a b b^{-1} a^n b=b^{-1} a^{n+1} b .
$$
By induction the statement holds for all positive $n$.
Now suppose $n<0$; we have
$$
\left(b^{-1} a b\right)^n=\left(\left(b^{-1} a b\right)^{-n}\right)^{-1}=\left(b^{-1} a^{-n} b\right)^{-1}=b^{-1} a^n b .
$$
Hence, the statement holds for all integers $n$.
Now to the main result. Suppose first that $|x|$ is infinity and that $\left|g^{-1} x g\right|=n$ for some positive integer $n$. Then we have
$$
\left(g^{-1} x g\right)^n=g^{-1} x^n g=1,
$$
and multiplying on the left by $g$ and on the right by $g^{-1}$ gives us that $x^n=1$, a contradiction. Thus if $|x|$ is infinity, so is $\left|g^{-1} x g\right|$. Similarly, if $\left|g^{-1} x g\right|$ is infinite and $|x|=n$, we have
$$
\left(g^{-1} x g\right)^n=g^{-1} x^n g=g^{-1} g=1,
$$
a contradiction. Hence if $\left|g^{-1} x g\right|$ is infinite, so is $|x|$.
Suppose now that $|x|=n$ and $\left|g^{-1} x g\right|=m$ for some positive integers $n$ and $m$. We have
$$
\left(g^{-1} x g\right)^n=g^{-1} x^n g=g^{-1} g=1,
$$
So that $m \leq n$, and
$$
\left(g^{-1} x g\right)^m=g^{-1} x^m g=1,
$$
so that $x^m=1$ and $n \leq m$. Thus $n=m$.
Qed.