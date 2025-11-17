Exercise 2.126 Suppose that $E$ is an uncountable subset of $\mathbb{R}$. Prove that there exists a point $p \in \mathbb{R}$ at which $E$ condenses.
Proof.
I think this is the proof by contrapositive that you were getting at.
Suppose that $E$ has no limit points at all. Pick an arbitrary point $x \in E$. Then $x$ cannot be a limit point, so there must be some $\delta>0$ such that the ball of radius $\delta$ around $x$ contains no other points of $E$ :
$$
B_\delta(x) \cap E=\{x\}
$$
Call this "point 1 ". For the next point, take the closest element to $x$ and on its left; that is, choose the point
$$
\max [E \cap(-\infty, x)]
$$
if it exists (that is important - if not, skip to the next step). Note that by the argument above, this supremum, should it exist, cannot equal $x$ and is therefore a new point in $E$.

Call this "point 2 ". Now take the first point to the right of $x$ for "point 3 ". Take the first point to the left of point 2 for "point 4 ". And so on, ad infinitum.

This gives a countable list of unique points; we must show that it exhausts the entire set $E$. Suppose not. Suppose there is some element $a<x$ which is never included in the list (picking $a$ on the negative side of $x$ is arbitrary, and the same argument would work for the second case). Then the element closest and to the right of $a$ in $E$ (which exists, by the no-limit-points argument at the beginning) is also not in the list; if it was, $a$ would have been in one of the next two spots. And same with that point (call it $a_1$ ); there is a closest $a_2>a_1 \in E$ such that $a_2$ is not in the list. Repeating, we generate an infinite monotone-increasing sequence $\left\{a_i\right\}$ of elements in $E$ and not in the list, which is clearly bounded above by $x$. By the Monotone
Convergence Theorem this sequence has a limit. But that means the sequence $\left\{a_i\right\} \subset E$ converges to a limit, and hence $E$ has a limit point, contradicting the assumption. Therefore our list exhausts $E$, and we have enumerated all its elements.
Qed.