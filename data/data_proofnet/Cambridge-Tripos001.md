Exercise 2022.IA.4-I-1E-a Show that there are infinitely many primes of the form $3 n+2$ with $n \in \mathbb{N}$.
Proof.
The general strategy is to find a (large) number $n$ that is relatively prime to each of the existing list of such primes, and is also congruent to 2 modulo 3 . The prime factorization of $n$ cannot consist only of primes congruent to 1 modulo 3 , since the product of any number of such is still 1 modulo 3 . Hence there must be some prime factor of $n$ that is congruent to 2 modulo 3 , which must be not on our list by the construction of $n$.
Now, how to construct such an $n$ ? Suppose the finite list is $\left\{p_1, p_2, \ldots, p_k\right\}$. If $k$ is even, then take $n=p_1 p_2 \cdots p_k+1$. If $k$ is odd, then take $n=\left(p_1 p_2 \cdots p_k\right) p_k+1$.
Qed.