Exercise 5.12 Suppose $T \in \mathcal{L}(V)$ is such that every vector in $V$ is an eigenvector of $T$. Prove that $T$ is a scalar multiple of the identity operator.
Proof.
For every single $v \in V$, there does exist $a_v \in F$ such that $T v=a_v v$. Since $T 0=0$, then we have to make $a_0$ be the any number in F. However, for every single $v \in V\{0\}$, then the value of $a_V$ is uniquely determined by the previous equation of $T v=a_v v$.

Now, to show that $T$ is a scalar multiple of the identity, then me must show that $a_v$ is independent of $v$ for $v \in V\{0\}$. We would now want to show that $a_v=a_w$.

First, just make the case of where $(v, w)$ is linearly dependent. Then, there does exist $b \in F$ such that $w=b v$. Now, you would have the following: $a_W w=T w=T(b v)=b T v=b\left(a_v v\right)=a_v w$. This is showing that $a_v=a_w$.
Finally, make the consideration to make $(v, w)$ be linearly independent. Now, we would have the following: $\left.a_{(} v+w\right)(v+w)=T(v+w)=T v+T w=a_v v+a_w w$.

That previous equation implies the following: $\left.\left.\left(a_{(} v+w\right)-a_v\right) v+\left(a_{(} v+w\right)-a_w\right) w=0$. Since $(v, w)$ is linearly independent, this would imply that both $\left.a_{(} v+w\right)=a_v$ and $\left.a_{(} v+w\right)=a_w$. Therefore, $a_v=a_w$.
Qed.