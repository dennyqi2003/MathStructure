import Mathlib.Topology.MetricSpace.Basic

open Set Filter Topology

-- [1] [Hint] {Exercise 2.26}
theorem exercise_2_26
  -- [2] [Fix] {$M$; $U$} such that {$M$ is a metric space; $U \subset M$}
  {M : Type*} [MetricSpace M] (U : Set M)
  :
  -- [3] [Show] {$U$ is open if and only if none of its points are limits of its complement}
  IsOpen U ↔ ∀ p ∈ U, p ∉ closure (Uᶜ)
:= by
  constructor
  -- [13] [Show] {If $U$ is open, then none of its points are limits of its complement}
  · -- [14] [Assume] {$U$ is open}
    intro h_U_open
    -- [15] [Show] {none of its points are limits of its complement} using {contradiction}
    by_contra h_contra
    sorry
  -- [4] [Show] {If none of the points of $U$ are limits of its complement, then $U$ is open}
  · -- [5] [Assume] {none of the points of $U$ are limits of its complement}
    intro h_no_limits
    -- [6] [Show] {$U$ is open} using {contradiction}
    by_contra h_not_open
    -- [7] [Assume] {$U$ is not open}
    -- [8] [Obtain] {$p$} such that {$p \in M$; for every $r>0$, there exists $q \in M$ with $d(p, q)<r$ but $q \notin U$}
    obtain ⟨p, hp_in_U, hp_prop⟩ : ∃ p ∈ U, ∀ r > 0, ∃ q, dist q p < r ∧ q ∉ U := by
      sorry
    -- [9] [Obtain] {$\{q_n\}$} such that {$\forall n \in \mathbb{N}, q_n \in U^c$; $\forall n \in \mathbb{N}, d(q_n, p) < 1/n$} by {Applying the property that for every $r>0$, there exists $q \in M$ with $d(p, q)<r$ but $q \notin U$, with $r=1/n$}
    choose q hq using fun n : ℕ ↦ hp_prop (1 / (n + 1)) (by sorry)
    -- [10] [Have] {$q_n \rightarrow p$}
    have h_tendsto : Tendsto q atTop (𝓝 p) := by
      sorry
    -- [11] [Have] {$p$ is a limit of a sequence of points in $U^c$}
    have h_p_is_limit : p ∈ closure (Uᶜ) := by
      sorry
    -- [12] [Have] {a contradiction}
    have h_contra : False := by
      sorry
    sorry