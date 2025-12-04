import Mathlib
set_option linter.style.longLine false

open Finset

theorem sum_of_first_n_integers :
  -- [1] [Show] {$\forall n \in \N^*, 1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$} by {mathematical induction}
  ∀ n : ℕ, ∑ i ∈ Finset.Icc 1 n, i = n * (n + 1) / 2
:= by
  intro n
  induction n
  -- [2] [Have] {When $n = 1$, $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds}
  case zero =>
    sorry
  -- [3] [Fix] {$k$} such that {$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds for n=k}
  case succ k ih =>
    -- [4] [Have] {$1 + 2 + \cdots + k + (k + 1) = \frac{k(k + 1)}{2} + k + 1 = \frac{(k + 1)[(k + 1) + 1]}{2}$}
    have h_calc : ∑ i ∈ Icc 1 (k + 1), i = (k + 1) * (k + 1 + 1) / 2 := by
      sorry
    -- [5] [Have] {$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds for n = k + 1}
    exact h_calc
-- [6] [Have] {for any positive integer $n$, $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$}