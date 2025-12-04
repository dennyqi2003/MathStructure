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
    sorry