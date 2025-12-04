import Mathlib
set_option linter.style.longLine false

open Set Function Classical

-- [Hint] {Theorem 4 (Schröder-Bernstein's Theorem)}
theorem schroder_bernstein
  -- [Fix] {$A$; $B$} such that {$A$, $B$ are sets}
  {α β : Type*}
  (A : Set α)
  (B : Set β)
  -- [Fix] {$f$; $g$} such that {$f: A \to B$ is an injection; $g: B \to A$ is an injection}
  (f : α → β)
  (hf : InjOn f A)
  (g : β → α)
  (hg : InjOn g B)
  :
  -- [Show] {there is a bijection $h$ from $A$ into $B$}
  ∃ h : α → β, BijOn h A B
:= by
  -- [Define] {$C_0$} as {$C_0=\{ a \in A \mid \forall b \in B, g(b) \neq a \}$}
  let C₀ : Set α := { a ∈ A | ∀ b ∈ B, g b ≠ a }
  -- [Define] {$D_0$} as {$D_0=\{ f(a) \mid a \in C_0 \}$}
  let D₀ : Set β := f '' C₀
  -- [Define] {$C_1$} as {$C_1=\{ a \in A \setminus C_0 \mid \forall b \in B \setminus D_0, g(b) \neq a \}$}
  let C₁ : Set α := { a ∈ A \ C₀ | ∀ b ∈ B \ D₀, g b ≠ a }
  -- [Have] {$C_1 = \{ g(b) \mid b \in D_0 \}$}
  have h_C₁_eq : C₁ = { g b | b ∈ D₀ } := by
    sorry
  -- [Define] {$D_1$} as {$D_1=\{ f(a) \mid a \in C_1 \}$}
  let D₁ : Set β := f '' C₁
  -- [Define] {set sequence $\{C_{n}\}$} as {$\forall n>1,C_{n+1}=\{ a \in A \setminus \bigcup_{i=0}^{n} C_i \mid \forall b \in B \setminus \bigcup_{i=0}^{n} D_i, g(b) \neq a \}$}
  let C : ℕ → Set α :=
    sorry
  -- [Define] {set sequence $\{D_{n}\}$} as {$\forall n>1,D_{n+1}=\{ f(a) \mid a \in C_{n+1} \}$}
  let D : ℕ → Set β :=
    sorry
  -- [Have] {$\forall n \in \N, C_{n+1} = \{ g(b) \mid b \in D_n \}$} by {similarly}
  have h_Cn_succ : ∀ n, C (n + 1) = { g b | b ∈ D n } := by
    sorry
  -- [Define] {$h$} as {function $h: A \to B$ such that for any $a \in A$, $h(a) := \begin{cases} f(a), & \text{if } a \in \bigcup_{i=0}^{\infty} C_i \\ b, \text{ such that } g(b) = a, & \text{if } a \in A \setminus \bigcup_{i=0}^{\infty} C_i \end{cases}$}
  let h : α → β := fun a ↦
    if a ∈ (⋃ i, C i)
    then f a
    else
      have h_exists : ∃ b, g b = a :=
        sorry
      Classical.choose h_exists
  -- [Have] {$\forall n$, the restriction of $f$ to $C_n$ is a bijection onto $D_n$}
  have h_restrict_bij : ∀ n, BijOn f (C n) (D n) := by
    sorry
  -- [Define] {$C$} as {$A \setminus \bigcup_{i=0}^{\infty} C_i$}
  let C_limit : Set α := A \ (⋃ i, C i)
  -- [Define] {$D$} as {$B \setminus \bigcup_{i=0}^{\infty} D_i$}
  let D_limit : Set β := B \ (⋃ i, D i)
  -- [SufficesToProve] {$\forall d \in D, \exists c \in C, g(d) = c$; $\forall c \in C, \exists d \in D, g(d) = c$}
  suffices (∀ d ∈ D_limit, ∃ c ∈ C_limit, g d = c) ∧ (∀ c ∈ C_limit, ∃ d ∈ D_limit, g d = c) by
    sorry
  -- [Show] {$\forall d \in D, \exists c \in C, g(d) = c$}
  have h_surj_on_D : ∀ d ∈ D_limit, ∃ c ∈ C_limit, g d = c := by
    -- [Fix] {$d$} such that {$d \in D$}
    intro d hd
    -- [Obtain] {$c$} such that {$c \in A$; $g(d) = c$} by {$g$ is a function from $B$ into $A$}
    obtain ⟨c, hc⟩ : ∃ c ∈ A, g d = c := by
      sorry
    -- [Show] {$\forall n, c \notin C_n$} using {contradiction}
    have h_c_not_Cn : ∀ n, c ∉ C n := by
      -- [Fix] {$n$} such that {$n \in \N$}
      intro n
      -- [Assume] {$c \in C_n$}
      by_contra h_c_in_Cn

      cases n with
      -- [Assume] {$n=0$}
      | zero =>
        -- [Have] {contradiction}
        have h_contra : False := by
          sorry
        tauto
      -- [Assume] {$n=m+1$ for some $m \in \N$}
      | succ m =>
        -- [Have] {$c \in C_{m+1} \implies d \in D_m$}
        have h_imply : c ∈ C (m + 1) → d ∈ D m := by
          sorry
        -- [Have] {contradiction}
        have h_contra : False := by
          sorry
        tauto
    -- [Have] {$c \in C$}
    have h_c_in_C : c ∈ C_limit := by
      sorry
    sorry
  -- [Show] {$\forall c \in C, \exists d \in D, g(d) = c$}
  have h_surj_on_C : ∀ c ∈ C_limit, ∃ d ∈ D_limit, g d = c := by
    -- [Fix] {$c$} such that {$c \in C$}
    intro c hc
    -- [Obtain] {$d$} such that {$d \in B$; $g(d) = c$} by {otherwise $c \in C_0$, contradiction}
    obtain ⟨d, hd⟩ : ∃ d ∈ B, g d = c := by
      sorry
    -- [Show] {$\forall n, d \notin D_n$} using {contradiction}
    have h_d_not_Dn : ∀ n, d ∉ D n := by
      -- [Fix] {$n$} such that {$n \in \N$}
      intro n
      -- [Assume] {$d \in D_n$}
      by_contra h_d_in_Dn
      -- [Have] {$c \in C_{n+1}$}
      have h_c_in_next : c ∈ C (n + 1) := by
        sorry
      -- [Have] {contradiction}
      have h_contra : False := by
        sorry
      tauto
    -- [Have] {$d \in D$}
    have h_d_in_D : d ∈ D_limit := by
      sorry
    sorry
  sorry
