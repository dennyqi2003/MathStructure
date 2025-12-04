import Mathlib
set_option linter.style.longLine false

open Set Filter Topology Real

theorem limit_root_n_one
  -- [1] [Fix] {$a$} such that {$a > 0$}
  (a : ℝ)
  (h_a_pos : a > 0) :
  -- [2] [Show] {$\lim_{n \to \infty} \sqrt[n]{a} = 1$}
  Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1)
:= by
  -- [3] [Assume] {$a = 1$}
  have h_case_a_eq_1 : (a = 1) -> Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1) := by
    intro h_a_eq_1
    -- [4] [Have] {$\lim_{n \to \infty} \sqrt[n]{a} = 1$}
    have h_concl : Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1) := by
      sorry
    sorry
  -- [5] [Assume] {$a > 1$}
  have h_case_a_gt_1 : (a > 1) -> Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1) := by
    intro h_a_gt_1
    -- [6] [Fix] {$\varepsilon$} such that {$\varepsilon > 0$}
    rw [Metric.tendsto_atTop]
    intro ε h_ε_pos
    -- [7] [Define] {$N$} by {$N = \lceil \frac{a - 1}{\varepsilon} \rceil$}
    let N := ⌈(a - 1) / ε⌉
    use N
    -- [8] [Fix] {$n$} such that {$n > N$}
    intro n h_n_geq_N
    -- [9] [Have] {$|\sqrt[n]{a} - 1| < \varepsilon$}
    have h_ineq : |a ^ (1 / n) - 1| < ε := by
      sorry
    -- [10] [Have] {$\lim_{n \to \infty} \sqrt[n]{a} = 1$}
    have h_concl : Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1) := by
      sorry
    sorry
  -- [11] [Assume] {$0 < a < 1$}
  have h_case_a_lt_1 : (a < 1) -> Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1) := by
    intro h_a_lt_1
    -- [12] [Define] {$a'$} by {$a' = \frac{1}{a}$}
    let a' := 1 / a
    -- [13] [Have] {$a' > 1$}
    have h_ap_gt_1 : a' > 1 := by
      sorry
    -- [14] [Have] {as $n \to \infty$, $\sqrt[n]{a} = \frac{1}{\sqrt[n]{a'}} \to 1$}
    have h_sub : Tendsto (fun n ↦ 1 / (a' ^ (1 / (n : ℝ)))) atTop (nhds 1) ∧ Tendsto (fun n ↦ (a ^ (1 / (n : ℝ)))) atTop (nhds 1) := by
      sorry
    sorry
  sorry
