Exercise 2.4.36 If $a > 1$ is an integer, show that $n \mid \varphi(a^n - 1)$, where $\phi$ is the Euler $\varphi$-function.
Proof.
Proof: We have $a>1$. First we propose to prove that
$$
\operatorname{Gcd}\left(a, a^n-1\right)=1 .
$$
If possible, let us assume that
$\operatorname{Gcd}\left(a, a^n-1\right)=d$, where $d>1$.
Then
$d$ divides $a$ as well as $a^n-1$.
Now,
$d$ divides $a \Longrightarrow d$ divides $a^n$.
This is an impossibility, since $d$ divides $a^n-1$ by our assumption. Consequently, $d$ divides 1 , which implies $d=1$. Hence we are contradict to the fact that $d>1$. Therefore
$$
\operatorname{Gcd}\left(a, a^n-1\right)=1 .
$$
Then $a \in U_{a^n-1}$, where $U_n$ is a group defined by
$$
U_n:=\left\{\bar{a} \in \mathbb{Z}_n \mid \operatorname{Gcd}(a, n)=1\right\} .
$$
We know that order of an element divides the order of the group. Here order of the group $U_{a^n-1}$ is $\phi\left(a^n-1\right)$ and $a \in U_{a^n-1}$. This follows that $\mathrm{o}(a)$ divides $\phi\left(a^n-1\right)$.
Qed.