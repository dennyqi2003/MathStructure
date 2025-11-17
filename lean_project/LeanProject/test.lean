import Mathlib
open Real Topology Filter

theorem limit_nth_root_of_a (a : ℝ) (ha : 0 < a) :
  Tendsto (fun n : ℕ ↦ a ^ (1 / (n : ℝ))) atTop (𝓝 1) :=
by
  have h_lt : a > 1 ∨ a = 1 ∨ a < 1 := by sorry
  by_cases h_eq : a = 1
  · sorry
  by_cases h_gt : 1 < a
  · rw [Metric.tendsto_atTop]
    intro ε hε_pos
    let N := Nat.ceil ((a - 1) / ε)
    use N
    intro n hn_ge_N
    have h_abs_lt_eps : |a ^ (1 / (n : ℝ)) - 1| < ε := by sorry
    sorry
  by_cases h_gt : 1 > a
  · let a' := 1 / a
    have ha'_gt_1 : 1 < a' := by sorry
    have h_lim_a : Tendsto (fun n : ℕ ↦ a ^ (1 / (n : ℝ))) atTop (𝓝 1) := by sorry
    exact h_lim_a
  sorry
