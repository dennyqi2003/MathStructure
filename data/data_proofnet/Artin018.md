Exercise 10.4.7a Let $I, J$ be ideals of a ring $R$ such that $I+J=R$. Prove that $I J=I \cap J$.
Proof.
We have seen that $IJ \subset I \cap J$, so it remains to show that $I \cap J \subset IJ$.  Since $I+J = (1)$, there are elements $i \in I$ and $j \in J$ such that $i+j = 1$.  Let $k \in I \cap J$, and multiply $i+j=1$ through by $k$ to get $ki+kj = k$.  Write this more suggestively as
\[ k = ik+kj. \]
The first term is in $IJ$ because $k \in J$, and the second term is in $IJ$ because $k \in I$, so $k \in IJ$ as desired.
Qed.