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
  -- [4] [Show] {Any union of elements of $\mathcal{B}$ is in $\mathcal{T}$}
  have h_forward : ∀ (C : Set (Set X)), (∀ s ∈ C, s ∈ B) → IsOpen (⋃₀ C) := by
    -- [5] [Fix] {$\mathcal{C}$} such that {$\mathcal{C}$ is a collection of elements of $\mathcal{B}$}
    intro C hC
    -- [6] [Have] {The elements of $\mathcal{C}$ are also elements of $\mathcal{T}$}
    have h_C_in_T : ∀ s ∈ C, IsOpen s := by
      sorry
    -- [7] [Have] {The union of the elements of $\mathcal{C}$ is in $\mathcal{T}$} by {$\mathcal{T}$ is a topology}
    have h_union_in_T : IsOpen (⋃₀ C) := by
      sorry
    sorry
  -- [8] [Show] {Any element of $\mathcal{T}$ is a union of elements of $\mathcal{B}$}
  have h_backward : ∀ U : Set X, IsOpen U → ∃ (C : Set (Set X)), (∀ s ∈ C, s ∈ B) ∧ U = ⋃₀ C := by
    sorry
  sorry