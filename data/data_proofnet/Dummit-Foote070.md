Exercise 7.3.37 An ideal $N$ is called nilpotent if $N^{n}$ is the zero ideal for some $n \geq 1$. Prove that the ideal $p \mathbb{Z} / p^{m} \mathbb{Z}$ is a nilpotent ideal in the ring $\mathbb{Z} / p^{m} \mathbb{Z}$.
Proof.
First we prove a lemma.
Lemma: Let $R$ be a ring, and let $I_1, I_2, J \subseteq R$ be ideals such that $J \subseteq I_1, I_2$. Then $\left(I_1 / J\right)\left(I_2 / J\right)=I_1 I_2 / J$.
Proof: ( $\subseteq$ ) Let
$$
\alpha=\sum\left(x_i+J\right)\left(y_i+J\right) \in\left(I_1 / J\right)\left(I_2 / J\right) .
$$
Then
$$
\alpha=\sum\left(x_i y_i+J\right)=\left(\sum x_i y_i\right)+J \in\left(I_1 I_2\right) / J .
$$
Now let $\alpha=\left(\sum x_i y_i\right)+J \in\left(I_1 I_2\right) / J$. Then
$$
\alpha=\sum\left(x_i+J\right)\left(y_i+J\right) \in\left(I_1 / J\right)\left(I_2 / J\right) .
$$
From this lemma and the lemma to Exercise 7.3.36, it follows by an easy induction that
$$
\left(p \mathbb{Z} / p^m \mathbb{Z}\right)^m=(p \mathbb{Z})^m / p^m \mathbb{Z}=p^m \mathbb{Z} / p^m \mathbb{Z} \cong 0 .
$$
Thus $p \mathbb{Z} / p^m \mathbb{Z}$ is nilpotent in $\mathbb{Z} / p^m \mathbb{Z}$.
Qed.