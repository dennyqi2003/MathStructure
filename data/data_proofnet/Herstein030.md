Exercise 4.2.5 Let $R$ be a ring in which $x^3 = x$ for every $x \in R$. Prove that $R$ is commutative.
Proof.
To begin with
$$
2 x=(2 x)^3=8 x^3=8 x .
$$
Therefore $6 x=0 \quad \forall x$.
Also
$$
(x+y)=(x+y)^3=x^3+x^2 y+x y x+y x^2+x y^2+y x y+y^2 x+y^3
$$
and
$$
(x-y)=(x-y)^3=x^3-x^2 y-x y x-y x^2+x y^2+y x y+y^2 x-y^3
$$
Subtracting we get
$$
2\left(x^2 y+x y x+y x^2\right)=0
$$
Multiply the last relation by $x$ on the left and right to get
$$
2\left(x y+x^2 y x+x y x^2\right)=0 \quad 2\left(x^2 y x+x y x^2+y x\right)=0 .
$$
Subtracting the last two relations we have
$$
2(x y-y x)=0 .
$$
We then show that $3\left(x+x^2\right)=0 \forall x$. You get this from
$$
x+x^2=\left(x+x^2\right)^3=x^3+3 x^4+3 x^5+x^6=4\left(x+x^2\right) .
$$
In particular
$$
3\left(x+y+(x+y)^2\right)=3\left(x+x^2+y+y^2+x y+y x\right)=0
$$
we end-up with $3(x y+y x)=0$. But since $6 x y=0$, we have $3(x y-y x)=0$. Then subtract $2(x y-y x)=0$ to get $x y-y x=0$.
Qed.