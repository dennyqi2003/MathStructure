Exercise 4.5.16 Let $F = \mathbb{Z}_p$ be the field of integers $\mod p$, where $p$ is a prime, and let $q(x) \in F[x]$ be irreducible of degree $n$. Show that $F[x]/(q(x))$ is a field having at exactly $p^n$ elements.
Proof.
In the previous problem we have shown that any for any $p(x) \in F[x]$, we have that
$$
p(x)+(q(x))=a_{n-1} x^{n-1}+\cdots+a_1 x+a_0+(q(x))
$$
for some $a_{n-1}, \ldots, a_0 \in F$, and that there are $p^n$ choices for these numbers, so that $F[x] /(q(x)) \leq p^n$. In order to show that equality holds, we have to show that each of these choices induces a different element of $F[x] /(q(x))$; in other words, that each different polynomial of degree $n-1$ or lower belongs to a different coset of $(q(x))$ in $F[x]$.

Suppose now, then, that
$$
a_{n-1} x^{n-1}+\cdots+a_1 x+a_0+(q(x))=b_{n-1} x^{n-1}+\cdots+b_1 x+b_0+(q(x))
$$
which is equivalent with $\left(a_{n-1}-b_{n-1}\right)^{n-1}+\cdots\left(a_1-b_1\right) x+\left(a_0-b_0\right) \in(q(x))$, which is in turn equivalent with there being a $w(x) \in F[x]$ such that
$$
q(x) w(x)=\left(a_{n-1}-b_{n-1}\right)^{n-1}+\cdots\left(a_1-b_1\right) x+\left(a_0-b_0\right) .
$$
Degree of the right hand side is strictly smaller than $n$, while the degree of the left hand side is greater or equal to $n$ except if $w(x)=0$, so that if equality is hold we must have that $w(x)=0$, but then since polynomials are equal iff all of their coefficient are equal we get that $a_{n-1}-b_{n-1}=$ $0, \ldots, a_1-b_1=0, a_0-b_0=0$, i.e.
$$
a_{n-1}=b_{n-1}, \ldots, a_1=b_1, a_0=b_0
$$
which is what we needed to prove.
Qed.