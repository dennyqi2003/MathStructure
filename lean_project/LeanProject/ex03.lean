import Mathlib
set_option linter.style.longLine false

open Set Filter Topology Real

-- [1] [Define] {$x$} as {$\forall n\in \N^*, {x}_{n} = \frac{n}{n + 1}$}
noncomputable def x_seq (n : ℕ) : ℝ := (n : ℝ) / (n + 1 : ℝ)

theorem x_seq_tensto_1 :
  -- [2] [Show] {$\lim_{n \to \infty} {x}_{n} = 1$}
  Tendsto x_seq atTop (nhds 1)
:= by
  -- [3] [Have] {$\forall n \in \N^*, |{x}_{n} - 1| = \frac{1}{n + 1}$}
  have h_abs_eq : ∀ n : ℕ, |x_seq n - 1| = 1 / ((n : ℝ) + 1) := by
    sorry
  -- [4] [Fix] {$\varepsilon$} such that {$\varepsilon>0$}
  rw [Metric.tendsto_atTop]
  intro ε h_ε_pos
  -- [5] [Fix] {$n$} such that {$n \in \N^*$}
  -- [6] [LogicChain] {$|{x}_{n} - 1| < \varepsilon$}
  --           <= {$\frac{1}{n + 1} < \varepsilon$}
  --          <=> {$n > \\frac{1}{\\varepsilon} - 1$}
  have h_logic_chain : ∀ n : ℕ, (n : ℝ) > 1 / ε - 1 → |x_seq n - 1| < ε := by
    intro n h_condition
    have h_step1 : 1 / ((n : ℝ) + 1) < ε → |x_seq n - 1| < ε := by
      sorry
    have h_step2 : 1 / ((n : ℝ) + 1) < ε ↔ (n : ℝ) > 1 / ε - 1 := by
      sorry
    sorry
  -- [7] [Define] {$N$} as {$N=\lfloor \frac{1}{\varepsilon} \rfloor$}
  let N := ⌊1 / ε⌋.toNat
  use N
  -- [8] [Have] {$\forall n > N, |{x}_{n} - 1| < \varepsilon$}
  have h_abs_lt : ∀ n ≥ N, |x_seq n - 1| < ε := by
    sorry
  -- [9] [Have] {$\lim_{n \to \infty} {x}_{n} = 1$}
  have h_concl : Tendsto x_seq atTop (nhds 1) := by
    sorry
  sorry
