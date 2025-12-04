import Mathlib
set_option linter.style.longLine false

open Real

-- [1] [Find] {$\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$}
noncomputable def integrand (x : ℝ) := (4*x^3 - 13*x^2 + 3*x + 8) / ((x+1)*(x-2)*(x-1)^2)
noncomputable def antiderivative (x : ℝ) := log (abs (x+1)) - 2 * log (abs (x-2)) + 5 * log (abs (x-1)) + 1/(x-1)
theorem find_integral :
  ∀ x ∈ {y | y ≠ -1 ∧ y ≠ 2 ∧ y ≠ 1}, HasDerivAt antiderivative (integrand x) x
:= by
  -- [2] [Hint] {First, decompose the integrand into a sum of simple fractions.}
  -- [3] [Find] {$A$; $B$; $C$; $D$} such that {$\forall x, \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}$}
  have h_decomp : ∀ x : ℝ, x ≠ -1 → x ≠ 2 → x ≠ 1 →
    (4*x^3 - 13*x^2 + 3*x + 8) / ((x+1)*(x-2)*(x-1)^2) = 1/(x+1) - 2/(x-2) + 5/(x-1) - 1/((x-1)^2) := by
    -- [4] [Have] {$\forall x, 4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 + C(x+1)(x-2)(x-1) + D(x+1)(x-2)$}
    have h_num_eq : ∀ x : ℝ, 4*x^3 - 13*x^2 + 3*x + 8 = 1*(x-2)*(x-1)^2 - 2*(x+1)*(x-1)^2 + 5*(x+1)*(x-2)*(x-1) - 1*(x+1)*(x-2) := by
      sorry
    -- [5] [Have] {$A = 1$}
    have hA : (let x := -1; 4*x^3 - 13*x^2 + 3*x + 8) = (let x := -1; 1*(x-2)*(x-1)^2) := by
      sorry
    -- [6] [Have] {$B = -2$}
    have hB : (let x := 2; 4*x^3 - 13*x^2 + 3*x + 8) = (let x := 2; -2*(x+1)*(x-1)^2) := by
      sorry
    -- [7] [Have] {$D = -1$}
    have hD : (let x := 1; 4*x^3 - 13*x^2 + 3*x + 8) = (let x := 1; -1*(x+1)*(x-2)) := by
      sorry
    -- [8] [Have] {$C = 5$}
    have hC : deriv (fun x ↦ 4*x^3 - 13*x^2 + 3*x + 8) 1 = deriv (fun x ↦ 5*(x+1)*(x-2)*(x-1) - 1*(x+1)*(x-2)) 1 := by
      sorry
    sorry
  -- [9] [CalculationChain] {$\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$}
  --                    = {$\int \left[ \frac{1}{x+1} - \frac{2}{x-2} + \frac{5}{x-1} - \frac{1}{(x-1)^2} \right]  dx$}
  --                    = {function family $\ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C$}
  intro x hx
  unfold integrand
  rw [h_decomp x hx.1 hx.2.1 hx.2.2]
  sorry