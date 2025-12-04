import Mathlib
set_option linter.style.longLine false

open Set TopologicalSpace

-- [1] [Hint] {Lemma 13.1.}
lemma basis_unions_eq_topology
  -- [2] [Fix] {$X$; $\mathcal{B}$; $\mathcal{T}$} such that {$X$ is a set; $\mathcal{B}$ is a basis for a topology $\mathcal{T}$ on $X$}
  {X : Type*} (B : Set (Set X)) (T : TopologicalSpace X)
  (hB : IsTopologicalBasis B) (hT : T = generateFrom B) :
  -- [3] [Show] {$\mathcal{T}$ equals the collection of all unions of elements of $\mathcal{B}$}
  ∀ U : Set X, IsOpen U ↔ ∃ (C : Set (Set X)), (∀ s ∈ C, s ∈ B) ∧ U = ⋃₀ C
:= by
  sorry