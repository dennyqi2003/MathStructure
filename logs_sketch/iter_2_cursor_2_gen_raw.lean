import Mathlib
set_option linter.style.longLine false

open Finset BigOperators

theorem sum_of_first_n_integers :
  -- [1] [Show] {$\forall n \in \N^*, 1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$} by {mathematical induction}
  ∀ (n : ℕ), n ≥ 1 → ∑ i ∈ Icc 1 n, i = n * (n + 1) / 2
:= by
  intro n hn
  induction n, hn using Nat.le_induction with
  | base =>
    -- [2] [Have] {When $n = 1$, $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$ holds}
    sorry
  | succ k hk ih =>
    -- [3] [Fix] {$n$} such that {$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$}
    -- [4] [Have] {$1 + 2 + \cdots + n + (n + 1) = \frac{n(n + 1)}{2} + n + 1 = \frac{(n + 1)[(n + 1) + 1]}{2}$}
    have h_calc : ∑ i in Icc 1 (k + 1), i = (k + 1) * ((k + 1) + 1) / 2 := by
      sorry
    -- [5] [Have] {$1 + 2 + \cdots + n+(n+1) = \frac{(n+1)((n+1) + 1)}{2}$}
    sorry
-- [6] [Have] {for any positive integer $n$, $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$}