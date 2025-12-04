Given a json structure of a math proof, you need to write a corresponding LEAN sketch. The sketch should preserve the exact information that the json structure provided, you shouldn't add or delete claims. Most importantly, for the "gaps" between the claims, you should fill with "sorry", don't try to prove it! 

Always use `import Mathlib`.

## Examples

### Example 1

**Structure**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": ["$A$","$B$"],
      "condition": ["$A$,$B$ are sets"],
      "scope": [
        {
          "type": "Show",
          "proposition": ["$A \\times \\bigcup B = \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
          "method": null,
          "scope": [
            {
              "type": "Show",
              "proposition": ["$A \\times \\bigcup B \\subseteq \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
              "method": null,
              "scope": [
                {
                  "type": "Fix",
                  "variable": ["$a$","$x$"],
                  "condition": ["$(a, x) \\in A \\times \\bigcup B$"],
                  "scope": [
                    {
                      "type": "Have",
                      "claim": ["$x \\in \\bigcup B$"],
                      "reason": ["definition"]
                    },
                    {
                      "type": "Obtain",
                      "obtained_variable": ["$X$"],
                      "condition": ["$X \\in B$", "$x \\in X$"],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": ["$(a, x) \\in A \\times X$"],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": ["$(a, x) \\in \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
                      "reason": ["$A \\times X$ is part of the union $\\bigcup \\{A \\times X \\mid X \\in B\\}$"]
                    }
                  ]
                }
              ]
            },
            {
              "type": "Show",
              "proposition": ["$\\bigcup \\{A \\times X \\mid X \\in B\\} \\subseteq A \\times \\bigcup B$"],
              "method": null,
              "scope": [
                {
                  "type": "Fix",
                  "variable": ["$a$", "$x$"],
                  "condition": ["$(a, x) \\in \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
                  "scope": [
                    {
                      "type": "Obtain",
                      "obtained_variable": ["$X$"],
                      "condition": ["$X \\in B$", "$(a, x) \\in A \\times X$"],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": ["$a \\in A$", "$x \\in X$"],
                      "reason": ["definition of Cartesian product"]
                    },
                    {
                      "type": "Have",
                      "claim": ["$x \\in \\bigcup B$"],
                      "reason": ["$X \\in B$"]
                    },
                    {
                      "type": "Have",
                      "claim": ["$(a, x) \\in A \\times \\bigcup B$"],
                      "reason": null
                    }
                  ]
                }
              ]
            },
            {
              "type": "Have",
              "claim": ["$A \\times \\bigcup B = \\bigcup \\{A \\times X \\mid X \\in B\\}$"],
              "reason": null
            }
          ]
        }
      ]
    }
  ]
}
```

**Lean Sketch**
```lean
import Mathlib

open Set

theorem product_distributes_over_sUnion {α β : Type*} (A : Set α) (B : Set (Set β)) :
Set.prod A (⋃₀ B) = ⋃ X ∈ B, Set.prod A X :=
by
  apply Set.Subset.antisymm
  · intro ⟨a, x⟩ hp
    have h_x_in_U_B : x ∈ ⋃₀ B := by sorry
    have h_exists_X : ∃ X, X ∈ B ∧ x ∈ X := by sorry
    rcases h_exists_X with ⟨X, hX_in_B, hx_in_X⟩
    have h_ax_in_prod : (a, x) ∈ Set.prod A X := by sorry
    have h_concl : (a, x) ∈ ⋃ X ∈ B, A.prod X := by sorry
    exact h_concl

  · intro ⟨a, x⟩ hp
    have h_exists_X : ∃ X, X ∈ B ∧ (a, x) ∈ Set.prod A X := by sorry
    rcases h_exists_X with ⟨X, hX_in_B, h_ax_in_prod_AX⟩
    have h_prod_mem : a ∈ A ∧ x ∈ X := by sorry
    have h_x_in_sUnion : x ∈ ⋃₀ B := by sorry
    have h_concl : (a, x) ∈ A.prod (⋃₀ B) := by sorry
    exact h_concl
```

### Example 2

**Structure**
```json
{
    "type": "Fix",
    "variable": ["$a$"],
    "condition": ["$a > 0$"],
    "scope": [
        {
            "type": "Show",
            "proposition": ["$\\lim_{n \\to \\infty} \\sqrt[n]{a} = 1$"],
            "method": null,
            "scope": [
                {
                    "type": "Assume",
                    "assumption": ["$a = 1$"],
                    "scope": [
                        {
                            "type": "Have",
                            "claim": ["$\\lim_{n \\to \\infty} \\sqrt[n]{a} = 1$"],
                            "reason": null
                        }
                    ]
                },
                {
                    "type": "Assume",
                    "assumption": ["$a > 1$"],
                    "scope": [
                        {
                            "type": "Fix",
                            "variable": ["$\\varepsilon$"],
                            "condition": ["$\\varepsilon > 0$"],
                            "scope": [
                                {
                                    "type": "Define",
                                    "term": "$N$",
                                    "definition": "$N = \\lceil \\frac{a - 1}{\\varepsilon} \\rceil$"
                                },
                                {
                                    "type": "Fix",
                                    "variable": ["$n$"],
                                    "condition": ["$n > N$"],
                                    "scope": [
                                        {
                                            "type": "Have",
                                            "claim": ["$|\\sqrt[n]{a} - 1| < \\varepsilon$"],
                                            "reason": null
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "Have",
                            "claim": ["$\\lim_{n \\to \\infty} \\sqrt[n]{a} = 1$"],
                            "reason": null
                        }
                    ]
                },
                {
                    "type": "Assume",
                    "assumption": ["$0 < a < 1$"],
                    "scope": [
                        {
                            "type": "Define",
                            "term": "$a'$",
                            "definition": "$a' = \\frac{1}{a}$"
                        },
                        {
                            "type": "Have",
                            "claim": ["$a' > 1$"],
                            "reason": null
                        },
                        {
                            "type": "Have",
                            "claim": ["as $n \\to \\infty$, $\\sqrt[n]{a} = \\frac{1}{\\sqrt[n]{a'}} \\to 1$"],
                            "reason": null
                        }
                    ]
                }
            ]
        }
    ]
}
```

**Lean Sketch**
```lean
import Mathlib
open Real Topology Filter

theorem limit_nth_root_of_a (a : ℝ) (ha : 0 < a) :
  Tendsto (fun n : ℕ ↦ a ^ (1 / (n : ℝ))) atTop (𝓝 1) :=
by
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
```

## Your Task

**Structure**
```json
{Json_structure}
```

**Lean Sketch**