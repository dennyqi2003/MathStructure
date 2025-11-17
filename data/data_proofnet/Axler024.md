Exercise 7.6 Prove that if $T \in \mathcal{L}(V)$ is normal, then $\operatorname{range} T=\operatorname{range} T^{*}.$
Proof.
Let $T \in \mathcal{L}(V)$ to be a normal operator.
Suppose $u \in \operatorname{null} T$. Then, by $7.20$,
$$
0=\|T u\|=\left\|T^* u\right\|,
$$
which implies that $u \in \operatorname{null} T^*$.
Hence
$$
\operatorname{null} T=\operatorname{null} T^*
$$
because $\left(T^*\right)^*=T$ and the same argument can be repeated.
Now we have
$$
\begin{aligned}
\text { range } T & =\left(\text { null } T^*\right)^{\perp} \\
& =(\text { null } T)^{\perp} \\
& =\operatorname{range} T^*,
\end{aligned}
$$
where the first and last equality follow from items (d) and (b) of 7.7.
Hence, range $T=$ range $T^*$.
Qed.