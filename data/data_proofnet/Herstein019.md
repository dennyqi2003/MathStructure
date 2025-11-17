Exercise 2.7.7 If $\varphi$ is a homomorphism of $G$ onto $G'$ and $N \triangleleft G$, show that $\varphi(N) \triangleleft G'$.
Proof.
We first claim that $\varphi(N)$ is a subgroup of $G'$. To see this, note that since $N$ is a subgroup of $G$, the identity element $e_G$ of $G$ belongs to $N$. Therefore, the element $\varphi(e_G) \in \varphi(N)$, so $\varphi(N)$ is a non-empty subset of $G'$.

Now, let $a', b' \in \varphi(N)$. Then there exist elements $a, b \in N$ such that $\varphi(a) = a'$ and $\varphi(b) = b'$. Since $N$ is a subgroup of $G$, we have $a, b \in N$, so $ab^{-1} \in N$. Thus, we have
$$\varphi(ab^{-1}) = \varphi(a) \varphi(b^{-1}) = a'b'^{-1} \in \varphi(N),$$
which shows that $a', b' \in \varphi(N)$ implies $a'b'^{-1} \in \varphi(N)$. Therefore, $\varphi(N)$ is a subgroup of $G'$.

Next, we will show that $\varphi(N)$ is a normal subgroup of $G'$. Let $\varphi(N) = N'$, a subgroup of $G'$. Let $x' \in G'$ and $h' \in N'$. Since $\varphi$ is onto, there exist elements $x \in G$ and $h \in N$ such that $\varphi(x) = x'$ and $\varphi(h) = h'$.

Since $N$ is a normal subgroup of $G$, we have $xhx^{-1} \in N$. Thus,
$$\varphi(xhx^{-1}) = \varphi(x)\varphi(h)\varphi(x^{-1}) = x'h'x'^{-1} \in \varphi(N),$$
which shows that $x' \in G'$ and $h' \in N'$ implies $x'h'x'^{-1} \in \varphi(N)$. Therefore, $\varphi(N)$ is a normal subgroup of $G'$. This completes the proof.
Qed.