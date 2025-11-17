Exercise 13.6.10 Let $K$ be a finite field. Prove that the product of the nonzero elements of $K$ is $-1$.
Proof.
Since we are working with a finite field with $q$ elements, anyone of them is a root of the following polynomial
$$
x^q-x=0 .
$$
In particular if we rule out the 0 element, any $a_i \neq 0$ is a root of
$$
x^{q-1}-1=0 .
$$
This polynomial splits completely in $\mathbb{F}_q$ so we find
$$
\left(x-a_1\right) \cdots\left(x-a_{q-1}\right)=0
$$
in particular
$$
x^{q-1}-1=\left(x-a_1\right) \cdots\left(x-a_{q-1}\right)
$$
Thus $a_1 \cdots a_{q-1}=-1$.
Qed.