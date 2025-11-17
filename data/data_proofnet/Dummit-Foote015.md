Exercise 1.3.8 Prove that if $\Omega=\{1,2,3, \ldots\}$ then $S_{\Omega}$ is an infinite group
Proof.
Recall that the codomain of an injective function must be at least as large (in cardinality) as the domain of the function. With that in mind, define the function
$$
\begin{gathered}
f: \mathbb{N} \rightarrow S_{\mathbb{N}} \\
f(n)=(1 n)
\end{gathered}
$$
where $(1 n)$ is the cycle decomposition of an element of $S_{\mathbb{N}}$ (specifically it's the function given by $g(1)=n, g(2)=2, g(3)=3, \ldots)$. The function $f$ maps every natural number to a distinct one of these functions. Hence $f$ is injective. Hence $\infty=|\mathbb{N}| \leq\left|S_{\mathbb{N}}\right|$.
Qed.