Exercise 2.6.15 If $G$ is an abelian group and if $G$ has an element of order $m$ and one of order $n$, where $m$ and $n$ are relatively prime, prove that $G$ has an element of order $mn$.
Proof.
Let $G$ be an abelian group, and let $a$ and $b$ be elements in $G$ of order $m$ and $n$, respectively, where $m$ and $n$ are relatively prime. We will show that the product $ab$ has order $mn$ in $G$, which will prove that $G$ has an element of order $mn$.

To show that $ab$ has order $mn$, let $k$ be the order of $ab$ in $G$. We have $a^m = e$, $b^n = e$, and $(ab)^k = e$, where $e$ denotes the identity element of $G$. Since $G$ is abelian, we have
$$(ab)^{mn} = a^{mn}b^{mn} = e \cdot e = e.$$
Thus, $k$ is a divisor of $mn$.

Now, observe that $a^k = b^{-k}$. Since $m$ and $n$ are relatively prime, there exist integers $x$ and $y$ such that $mx + ny = 1$. Taking $kx$ on both sides of the equation, we get $a^{kx} = b^{-kx}$, or equivalently, $(a^k)^x = (b^k)^{-x}$. It follows that $a^{kx} = (a^m)^{xny} = e$, and similarly, $b^{ky} = (b^n)^{mxk} = e$. Therefore, $m$ divides $ky$ and $n$ divides $kx$. Since $m$ and $n$ are relatively prime, it follows that $mn$ divides $k$. Hence, $k = mn$, and $ab$ has order $mn$ in $G$. This completes the proof.
Qed.