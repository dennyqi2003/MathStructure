Exercise 3.9 Show that $\int_0^1 \log(\sin \pi x) dx = - \log 2$.
Proof.
Consider
$$
\begin{gathered}
f(z)=\log \left(1-e^{2 \pi z i}\right)=\log \left(e^{\pi z i}\left(e^{-\pi z i}-e^{\pi z i}\right)\right)=\log (-2 i)+\pi z i+\log \\
(\sin (\pi z))
\end{gathered}
$$
Then we have
$$
\begin{aligned}
\int_0^1 f(z) d z & =\log (-2 i)+\frac{i \pi}{2}+\int_0^1 \log (\sin (\pi z)) d z \\
& =\int_0^1 \log (\sin (\pi z)) d z+\log (-2 i)+\log (i) \\
& =\log (2)+\int_0^1 \log (\sin (\pi z)) d z
\end{aligned}
$$
Now it suffices to show that $\int_0^1 f(z) d z=0$. Consider the contour $C(\epsilon, R)$ (which is the contour given in your question) given by the following.
1. $C_1(\epsilon, R)$ : The vertical line along the imaginary axis from $i R$ to $i \epsilon$.
2. $C_2(\epsilon)$ : The quarter turn of radius $\epsilon$ about 0 .
3. $C_3(\epsilon)$ : Along the real axis from $(\epsilon, 1-\epsilon)$.
4. $C_4(\epsilon)$ : The quarter turn of radius $\epsilon$ about 1 .
5. $C_5(\epsilon, R)$ : The vertical line from $1+i \epsilon$ to $1+i R$.
6. $C_6(R)$ : The horizontal line from $1+i R$ to $i R$.
$f(z)$ is analytic inside the contour $C$ and hence $\oint_C f(z)=0$. This gives us
$$
\begin{aligned}
\int_{C_1(\epsilon, R)} f d z+\int_{C_2(\epsilon)} f d z+\int_{C_3(\epsilon)} f d z+\int_{C_4(\epsilon)} f d z+\int_{C_5(\epsilon, R)} f d z+\int_{C_6(R)} f d z \\
=0
\end{aligned}
$$
Now the integral along 1 cancels with the integral along 5 due to symmetry. Integrals along 2 and 4 scale as $\epsilon \log (\epsilon)$. Integral along 6 goes to 0 as $R \rightarrow \infty$. This gives us
$$
\lim _{\epsilon \rightarrow 0} \int_{C_3(\epsilon)} f d z=0
$$
which is what we need.
Qed.