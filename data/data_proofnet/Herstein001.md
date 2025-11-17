Exercise 2.1.18 If $G$ is a finite group of even order, show that there must be an element $a \neq e$ such that $a=a^{-1}$.
Proof.
First note that $a=a^{-1}$ is the same as saying $a^2=e$, where $e$ is the identity. I.e. the statement is that there exists at least one element of order 2 in $G$.
Every element $a$ of $G$ of order at least 3 has an inverse $a^{-1}$ that is not itself -- that is, $a \neq a^{-1}$. So the subset of all such elements has an even cardinality (/size). There's exactly one element with order 1 : the identity $e^1=e$. So $G$ contains an even number of elements -call it $2 k$-- of which an even number are elements of order 3 or above -- call that $2 n$ where $n<k$-- and exactly one element of order 1 . Hence the number of elements of order 2 is
$$
2 k-2 n-1=2(k-n)-1
$$
This cannot equal 0 as $2(k-n)$ is even and 1 is odd. Hence there's at least one element of order 2 in $G$, which concludes the proof.
Qed.