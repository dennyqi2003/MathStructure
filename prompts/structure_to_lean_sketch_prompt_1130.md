You need to help me write a lean sketch base on the proof-structure I give you.

## Example 1

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

```Lean
import Mathlib

open Set

theorem product_distributes_over_sUnion {α β : Type*} (A : Set α) (B : Set (Set β)):
  prod A (⋃₀ B) = ⋃ X ∈ B, prod A X
:= by
  have h_show_forward: prod A (⋃₀ B) ⊆
   ⋃ X ∈ B, prod A X := by
    intro ⟨a, x⟩ h_fix1
    have h_x_in_U_B : x ∈ ⋃₀ B := by
      sorry
      -- hint: by "definition"
    have h_exists_X : ∃ X, X ∈ B ∧ x ∈ X := by sorry
    rcases h_exists_X with ⟨X, h_X_in_B, h_x_in_X⟩
    have h_ax_in_prod : (a, x) ∈ prod A X := by
      sorry
    have h_concl : (a, x) ∈ ⋃ X ∈ B, A.prod X := by
      sorry
      --hint: by "$A \\times X$ is part of the union $\\bigcup \\{A \\times X \\mid X \\in B\\}$"
    sorry
  have h_show_backward: ⋃ X ∈ B, prod A X ⊆ prod A (⋃₀ B) := by
    intro ⟨a, x⟩ h_fix1
    have h_exists_X : ∃ X, X ∈ B ∧ (a, x) ∈ prod A X := by
      sorry
    rcases h_exists_X with ⟨X, hX_in_B, h_ax_in_prod_AX⟩
    have h_prod_mem : a ∈ A ∧ x ∈ X := by
      sorry
      -- hint: by "definition of Cartesian product"
    have h_x_in_sUnion : x ∈ ⋃₀ B := by
      sorry
      -- hint: by "$X \\in B$"
    have h_concl : (a, x) ∈ A.prod (⋃₀ B) := by
      sorry
    sorry
  have h_backward: ⋃ X ∈ B, prod A X = prod A (⋃₀ B) := by
    sorry
  sorry
```

## Example 2

**Structure:**
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

```Lean
import Mathlib
set_option linter.style.longLine false

open Set Filter Topology Real

theorem limit_root_n_one (a : ℝ) (h_a_pos : a > 0) :
  Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1)
:= by
  have h_case_a_eq_1 : (a = 1) -> Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1) := by
    sorry
  have h_case_a_gt_1 : (a > 1) -> Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1) := by
    intro h_a_gt_1
    rw [Metric.tendsto_atTop]
    intro ε h_ε_pos
    let N := ⌈(a - 1) / ε⌉
    use N
    intro n h_n_geq_N
    have h_ineq : |a ^ (1 / n) - 1| < ε := by
      sorry
    sorry
  have h_case_a_lt_1 : (a < 1) -> Tendsto (fun n ↦ a ^ (1 / (n : ℝ))) atTop (nhds 1) := by
    intro h_a_lt_1
    let a' := 1 / a
    have h_ap_gt_1 : a' > 1 := by
      sorry
    have h_sub : Tendsto (fun n ↦ 1 / (a' ^ (1 / (n : ℝ)))) atTop (nhds 1) := by
      sorry
    have h_iff : Tendsto (fun n ↦ (a ^ (1 / (n : ℝ)))) atTop (nhds 1) ↔ Tendsto (fun n ↦ 1 / (a' ^ (1 / (n : ℝ)))) atTop (nhds 1) := by
      sorry
    sorry
  sorry
```

## Example 3

**Structure:**

```json
[
    {
        "type": "Define",
        "term": "$x$",
        "definition": "$\\forall n\\in \\N^*, {x}_{n} = \\frac{n}{n + 1}$"
    },
    {
        "type": "Show",
        "proposition": ["$\\lim_{n \\to \\infty} {x}_{n} = 1$"],
        "method": null,
        "scope": [
            {
                "type": "Have",
                "claim": ["$\\forall n \\in \\N^*, |{x}_{n} - 1| = \\frac{1}{n + 1}$"],
                "reason": null
            },
            {
                "type": "Fix",
                "variable": ["$\\varepsilon$"],
                "condition": ["$\\varepsilon>0$"],
                "scope": [
                    {
                        "type": "Fix",
                        "variable": ["$n$"],
                        "condition": ["$n \\in \\N^*$"],
                        "scope": [
                            {
                                "type": "LogicChain",
                                "initial_proposition": ["$|{x}_{n} - 1| < \\varepsilon$"],
                                "steps": [
                                    {
                                        "operator": "⇐",
                                        "proposition": ["$\\frac{1}{n + 1} < \\varepsilon$"],
                                        "reason": null
                                    },
                                    {
                                        "operator": "⇔",
                                        "proposition": ["$n > \\frac{1}{\\varepsilon} - 1$"],
                                        "reason": null
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "Define",
                        "term": "$N$",
                        "definition": "$N=\\lfloor \\frac{1}{\\varepsilon} \\rfloor$"
                    },
                    {
                        "type": "Have",
                        "claim": ["$\\forall n > N, |{x}_{n} - 1| < \\varepsilon$"],
                        "reason": null
                    }
                ]
            },
            {
                "type": "Have",
                "claim": ["$\\lim_{n \\to \\infty} {x}_{n} = 1$"],
                "reason": null
            }
        ]
    }
]
```

**Lean Sketch**

```
import Mathlib
set_option linter.style.longLine false

open Set Filter Topology Real

noncomputable def x_seq (n : ℕ) : ℝ := n / (n + 1)

theorem x_seq_tensto_1 :
  Tendsto x_seq atTop (nhds 1)
:= by
  have h_abs_eq : ∀ n : ℕ, |x_seq n - 1| = 1 / (n + 1) := by
    sorry
  rw [Metric.tendsto_atTop]
  intro ε h_ε_pos
  have h_logic_chain : ∀ n : ℕ, n > 1 / ε - 1 → |x_seq n - 1| < ε := by
    intro n h_condition
    have h_step1 : 1 / (n + 1) < ε → |x_seq n - 1| < ε := by
      sorry
    have h_step2 : 1 / (n + 1) < ε ↔ n > 1 / ε - 1 := by
      sorry
    sorry
  let N := ⌊1 / ε⌋.toNat
  use N
  have h_abs_lt : ∀ n ≥ N, |x_seq n - 1| < ε := by
    sorry
  sorry

```

## Example 5

**Natural language text:**
"""
Theorem 2.4.7 (Cauchy Convergence): A sequence $\{x_n\}$ converges if and only if $\{x_n\}$ is a Cauchy sequence.

Proof: First, we prove the necessity.
Assume $\{x_n\}$ converges to $a$.
By definition, for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - a| < \frac{\varepsilon}{2}, \quad |x_m - a| < \frac{\varepsilon}{2}$.
Thus, $|x_n - x_m| \leq |x_n - a| + |x_m - a| < \varepsilon$.

Next, we prove the sufficiency.
First, we show that a Cauchy sequence must be bounded.
Take $\varepsilon_0 = 1$. Since $\{x_n\}$ is a Cauchy sequence, there exists $N_0$ such that for all $n > N_0$: $|x_n - x_{N_0 + 1}| < 1$.
Let $M = \max \{|x_1|, |x_2|, \ldots, |x_{N_0}|, |x_{N_0 + 1}| + 1\}$.
Then for all $n$, we have $|x_n| \leq M$.
By the Bolzano-Weierstrass theorem, there exists a convergent subsequence in $\{x_n\}$: $\lim_{k \to \infty} x_{n_k} = \xi$.
Since $\{x_n\}$ is a Cauchy sequence, for any $\varepsilon > 0$, there exists $N$ such that for all $n, m > N$: $|x_n - x_m| < \frac{\varepsilon}{2}$.
In the above inequality, take $x_m = x_{n_k}$, where $k$ is sufficiently large such that $n_k > N$, and let $k \to \infty$. Then we obtain $|x_n - \xi| \leq \frac{\varepsilon}{2}$.
Thus, $|x_n - \xi| < \varepsilon$.
This shows that the sequence $\{x_n\}$ converges.
The proof is complete.
"""

**Structure:**
```json
[
    {
        "type": "Hint",
        "text": "Theorem 2.4.7 (Cauchy Convergence)"
    },
    {
        "type": "Fix",
        "variable": ["$x$"],
        "condition": ["$\\{x_n\\}$ is a real sequence"],
        "scope": [
            {
                "type": "Show",
                "proposition": ["sequence $\\{x_n\\}$ converges if and only if $\\{x_n\\}$ is a Cauchy sequence."],
                "method": null,
                "scope": [
                    {
                        "type": "Show",
                        "proposition": ["sequence $\\{x_n\\}$ converges implies $\\{x_n\\}$ is a Cauchy sequence."],
                        "method": null,
                        "scope": [
                            {
                                "type": "Fix",
                                "variable": ["$a$"],
                                "condition": ["$\\{x_n\\}$ converges to $a$"],
                                "scope": [
                                    {
                                        "type": "Fix",
                                        "variable": ["$\\varepsilon$"],
                                        "condition": ["$\\varepsilon>0$"],
                                        "scope": [
                                            {
                                                "type": "Obtain",
                                                "obtained_variable": ["$N$"],
                                                "condition": ["$\\forall n, m > N, |x_n - a| < \\frac{\\varepsilon}{2} \\text{ and } |x_m - a| < \\frac{\\varepsilon}{2}$"],
                                                "reason": ["definition"]
                                            },
                                            {
                                                "type": "Fix",
                                                "variable": ["$n$", "$m$"],
                                                "condition": ["$n>N$", "$m>N$"],
                                                "scope": [
                                                    {
                                                        "type": "Have",
                                                        "claim": ["$|x_n - x_m| \\leq |x_n - a| + |x_m - a| < \\varepsilon$"],
                                                        "reason": null
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "Show",
                        "proposition": ["$\\{x_n\\}$ is a Cauchy sequence implies sequence $\\{x_n\\}$ converges"],
                        "method": null,
                        "scope": [
                            {
                                "type": "Show",
                                "proposition": ["Cauchy sequence $\\{x_n\\}$ is bounded"],
                                "method": null,
                                "scope": [
                                    {
                                        "type": "Obtain",
                                        "obtained_variable": ["$N_0$"],
                                        "condition": ["$\\forall n > N_0, |x_n - x_{N_0 + 1}| < 1$"],
                                        "reason": ["take $\\varepsilon_0 = 1$", "$\\{x_n\\}$ is a cauchy sequence"]
                                    },
                                    {
                                        "type": "Define",
                                        "term": "$M$",
                                        "definition": "$M = \\max \\{|x_1|, |x_2|, \\ldots, |x_{N_0}|, |x_{N_0 + 1}| + 1\\}$"
                                    },
                                    {
                                        "type": "Have",
                                        "claim": ["$\\forall n, |x_n| \\leq M$"],
                                        "reason": null
                                    }
                                ]
                            },
                            {
                                "type": "Obtain",
                                "obtained_variable": ["$\\{x_{n_k}\\}$", "$\\xi$"],
                                "condition": ["$\\{x_{n_k}\\}$ is a subsequence of $\\{x_n\\}$", "$\\lim_{k \\to \\infty} x_{n_k} = \\xi$"],
                                "reason": ["Bolzano-Weierstrass theorem"]
                            },
                            {
                                "type": "Fix",
                                "variable": ["$\\varepsilon$"],
                                "condition": ["$\\varepsilon>0$"],
                                "scope": [
                                    {
                                        "type": "Obtain",
                                        "obtained_variable": ["$N$"],
                                        "condition": ["$\\forall n, m > N, |x_n - x_m| < \\frac{\\varepsilon}{2}$"],
                                        "reason": ["$\\{x_n\\}$ is a Cauchy sequence"]
                                    },
                                    {
                                        "type": "Fix",
                                        "variable": ["$n$"],
                                        "condition": ["$n>N$"],
                                        "scope": [
                                            {
                                                "type": "Have",
                                                "claim": ["$|x_n - \\xi| \\leq \\frac{\\varepsilon}{2}$"],
                                                "reason": ["take $x_m = x_{n_k}$ in the inequality $|x_n - x_m| < \\frac{\\varepsilon}{2}$, where $k$ is sufficiently large such that $n_k > N$, and let $k \\to \\infty$"]
                                            },
                                            {
                                                "type": "Have",
                                                "claim": ["$|x_n - \\xi| < \\varepsilon$"],
                                                "reason": null
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "Have",
                                "claim": ["$\\{x_n\\}$ converges"],
                                "reason": null
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
```

## Example 6

**Natural language text**
"""
If $A \subseteq B$, then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$:

Pf: Let $X \in \mathcal{P}(A)$. By definition of power set, $X \subseteq A$. We have $A \subseteq B$. It follows that $X \subseteq B$. Therefore, $X \in \mathcal{P}(B)$. Hence, every element of $\mathcal{P}(A)$ is also in $\mathcal{P}(B)$, so $\mathcal{P}(A) \subseteq \mathcal{P}(B)$. Qed.
"""

**Structure**
```json
{
  "structure": [
    {
      "type": "Fix",
      "variable": ["$A$", "$B$"],
      "condition": ["$A, B$ are sets", "$A \\subseteq B$"],
      "scope": [
        {
          "type": "Show",
          "proposition": ["$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"],
          "method": null,
          "scope": [
            {
              "type": "Fix",
              "variable": ["$X$"],
              "condition": ["$X \\in \\mathcal{P}(A)$"],
              "scope": [
                {
                  "type": "Have",
                  "claim": ["$X \\subseteq A$"],
                  "reason": ["definition of power set"]
                },
                {
                  "type": "Have",
                  "claim": ["$A \\subseteq B$"],
                  "reason": null
                },
                {
                  "type": "Have",
                  "claim": ["$X \\subseteq B$"],
                  "reason": null
                },
                {
                  "type": "Have",
                  "claim": ["$X \\in \\mathcal{P}(B)$"],
                  "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["every element of $\\mathcal{P}(A)$ is also in $\\mathcal{P}(B)$"],
                    "reason": null
                },
              ]
            },
            {
              "type": "Have",
              "claim": ["$\\mathcal{P}(A) \\subseteq \\mathcal{P}(B)$"],
              "reason": null
            }
          ]
        }
      ]
    }
  ]
}
```

## Example 7

**Natural language text:**
"""
We need to find all functions $ f: \mathbb{R} \rightarrow \mathbb{R} $ such that for all $ x, y \in \mathbb{R} $, $ f(x + y) - f(x - y) = f(x)f(y). $
Solution
First, interchange $ x $ and $ y $ in the original equation: 
$ f(y + x) - f(y - x) = f(y)f(x). $ 
Thus, we have: 
$ f(y + x) - f(y - x) = f(x + y) - f(x - y). $ 
This implies: 
$ f(y - x) = f(x - y). $ 
Let $ y = 0 $, then: 
$ f(-x) = f(x). $ 
So $ f $ is an even function. 
Now, in the original equation, replace $ y $ with $ -y $: 
$ f(x + (-y)) - f(x - (-y)) = f(x)f(-y), $ 
which simplifies to: 
$ f(x - y) - f(x + y) = f(x)f(-y). $ 
Since $ f $ is even, $ f(-y) = f(y) $, so: 
$ f(x - y) - f(x + y) = f(x)f(y). $ 
But from the original equation, 
$ f(x + y) - f(x - y) = f(x)f(y). $
Adding these two equations: 
$ [f(x + y) - f(x - y)] + [f(x - y) - f(x + y)] = f(x)f(y) + f(x)f(y), $ 
which gives: 
$ 0 = 2f(x)f(y). $ 
Therefore, for all $ x, y \in \mathbb{R} $, 
$ f(x)f(y) = 0. $ 
In particular, let $ y = x $: 
$ f(x)^2 = 0 \quad \Rightarrow \quad f(x) = 0. $ 
Thus, the only function satisfying the condition is the zero function. 
In conclusion, the only solution is: 
$ \boxed{f(x) = 0} $
"""

**Correct Structure:**
```json
{
    "type": "Find",
    "target": ["$f$"],
    "condition": [
        "$f: \\mathbb{R} \\rightarrow \\mathbb{R}$",
        "$\\forall x, y \\in \\mathbb{R}, f(x + y) - f(x - y) = f(x)f(y)$"
    ],
    "scope": [
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, f(y + x) - f(y - x) = f(y)f(x)$"],
            "reason": ["interchanging $x$ and $y$ in $f(x + y) - f(x - y) = f(x)f(y)$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R,f(y + x) - f(y - x) = f(x + y) - f(x - y)$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, f(y - x) = f(x - y)$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x \\in \\mathbb{R}, f(-x) = f(x)$"],
            "reason": ["Letting y = 0 in $\\forall x, y \\in \\mathbb{R}, f(y - x) = f(x - y)$"]
        },
        {
            "type": "Have",
            "claim": ["$f$ is an even function"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R, f(x + (-y)) - f(x - (-y)) = f(x)f(-y)$"],
            "reason": ["replacing $y$ with $-y$ in $f(x + y) - f(x - y) = f(x)f(y)$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, f(x - y) - f(x + y) = f(x)f(-y)$"],
            "reason": ["simplify"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R, f(x - y) - f(x + y) = f(x)f(y)$"],
            "reason": ["$f$ is even", "$f(-y) = f(y)$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R, f(x + y) - f(x - y) = f(x)f(y)$"],
            "reason": ["this is the original equation"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, [f(x + y) - f(x - y)] + [f(x - y) - f(x + y)] = f(x)f(y) + f(x)f(y)$"],
            "reason": ["Adding the equation $f(x + y) - f(x - y) = f(x)f(y)$ and the equation $f(x - y) - f(x + y) = f(x)f(y)$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x,y \\in \\R, 0 = 2f(x)f(y)$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x, y \\in \\mathbb{R}, f(x)f(y) = 0$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["$\\forall x \\in \\mathbb{R}, f(x)^2 = 0$"],
            "reason": ["Letting $y = x$"]
        },
        {
            "type": "Have",
            "claim": ["$\\forall x \\in \\mathbb{R}, f(x) = 0$"],
            "reason": null
        },
        {
            "type": "Have",
            "claim": ["The only solution is the function $f(x) = 0$ for all $x \\in \\mathbb{R}$"],
            "reason": null
        }
    ]
}
```

## Example 8

**Natural language text:**
"""
Find the integral $\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$.
First, decompose the integrand into a sum of simple fractions. Let: 
$\displaystyle\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \frac{A}{x+1} + \frac{B}{x-2} + \frac{C}{x-1} + \frac{D}{(x-1)^2}.$ 
After combining the right-hand side over a common denominator, the numerators on both sides must be equal, so: 
$4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 +$ 
$C(x+1)(x-2)(x-1) + D(x+1)(x-2).$ 
Let $x = -1$, we get $A = 1$; 
Let $x = 2$, we get $B = -2$; 
Let $x = 1$, we get $D = -1$; 
Differentiate both sides, then let $x = 1$, we get $C = 5$; 
Thus: 
$\displaystyle\int \frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx = \int \left[ \frac{1}{x+1} - \frac{2}{x-2} + \frac{5}{x-1} - \frac{1}{(x-1)^2} \right]  dx$ 
$= \ln |(x+1)(x-1)^5| - \ln |(x-2)^2| + \frac{1}{x-1} + C.$
"""

**Structure:**
```json
{
    "type": "Find",
    "target": ["$\\int \\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$"],
    "condition": null,
    "scope": [
        {
            "type": "Hint",
            "text": "First, decompose the integrand into a sum of simple fractions."
        },
        {
            "type": "Find",
            "target": ["$A$", "$B$", "$C$", "$D$"],
            "condition": ["$\\forall x, \\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2} = \\frac{A}{x+1} + \\frac{B}{x-2} + \\frac{C}{x-1} + \\frac{D}{(x-1)^2}$"],
            "scope": [
                {
                    "type": "Have",
                    "claim": ["$\\forall x, 4x^3 - 13x^2 + 3x + 8 = A(x-2)(x-1)^2 + B(x+1)(x-1)^2 + C(x+1)(x-2)(x-1) + D(x+1)(x-2)$"],
                    "reason": ["combining the right-hand side over a common denominator, the numerators on both sides must be equal"]
                },
                {
                    "type": "Have",
                    "claim": ["$A = 1$"],
                    "reason": ["Let $x = -1$"]
                },
                {
                    "type": "Have",
                    "claim": ["$B = -2$"],
                    "reason": ["Let $x = 2$"]
                },
                {
                    "type": "Have",
                    "claim": ["$D = -1$"],
                    "reason": ["Let $x = 1$"]
                },
                {
                    "type": "Have",
                    "claim": ["$C = 5$"],
                    "reason": ["Differentiate both sides then let $x = 1$"]
                }
            ]
        },
        {
            "type": "CalculationChain",
            "initial_expression": ["$\\int \\frac{4x^3 - 13x^2 + 3x + 8}{(x+1)(x-2)(x-1)^2}  dx$"],
            "steps": [
                {
                    "operator": "=",
                    "expression": ["$\\int \\left[ \\frac{1}{x+1} - \\frac{2}{x-2} + \\frac{5}{x-1} - \\frac{1}{(x-1)^2} \\right]  dx$"],
                    "reason": null
                },
                {
                    "operator": "=",
                    "expression": ["function family $\\ln |(x+1)(x-1)^5| - \\ln |(x-2)^2| + \\frac{1}{x-1} + C$"],
                    "reason": null
                }
            ]
        }
    ]
}
```

## Example 9

**Natural language text:**
"""
Suppose $f(x)$ is continuous on $[0,1]$ , prove that: $\lim_{h \to 0^+} \int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \frac{\pi}{2} f(0)$

Pf:
$\int_0^1 \frac{h}{h^2 + x^2} f(x) dx = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx + \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
令$I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx$, $I_2 = \int_{h^{1/4}}^1 \frac{hf(x)}{h^2 + x^2} dx$
where $I_1 = \int_0^{h^{1/4}} \frac{hf(x)}{h^2 + x^2} dx = f(\xi) \int_0^{h^{1/4}} \frac{h}{h^2 + x^2} dx \quad (0 \leq \xi \leq h^{1/4})$
$= f(\xi) \arctan \frac{x}{h} \Big|_0^{h^{1/4}} = f(\xi) \arctan \frac{1}{h^{3/4}} \to f(0)\dfrac{\pi}{2} \quad (h \to 0^+)$
$|I_2| = \left| \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} f(x) dx \right| \leq M \int_{h^{1/4}}^1 \frac{h}{h^2 + x^2} dx(\quad |f(x)|\leq M\quad)$
$= M \left( \arctan \frac{1}{h} - \arctan \frac{1}{h^{3/4}} \right) \to 0 \quad (h \to 0^+)$
Hence $h\to 0^+$时$I_1+I_2\to f(0)\dfrac{\pi}{2}$
Qed.
"""

```json
{
    "type": "Fix",
    "variable": ["$f$"],
    "condition": ["$f:\\R \\to \\R$", "$f(x)$ is continuous on $[0,1]$"],
    "scope": [
        {
            "type": "Show",
            "proposition": ["$\\lim_{h \\to 0^+} \\int_0^1 \\frac{h}{h^2 + x^2} f(x) dx = \\frac{\\pi}{2} f(0)$"],
            "method": null,
            "scope": [
                {
                    "type": "Have",
                    "claim": ["$\\forall h \\in (0,1/2), \\int_0^1 \\frac{h}{h^2 + x^2} f(x) dx = \\int_0^{h^{1/4}} \\frac{hf(x)}{h^2 + x^2} dx + \\int_{h^{1/4}}^1 \\frac{hf(x)}{h^2 + x^2} dx$"],
                    "reason": null
                },
                {
                    "type": "Define",
                    "term": "$I_1$",
                    "definition": "$\\forall h \\in (0,1/2), I_1(h)=\\int_0^{h^{1/4}} \\frac{hf(x)}{h^2 + x^2} dx$"
                },
                {
                    "type": "Define",
                    "term": "$I_2$",
                    "definition": "$\\forall h \\in (0,1/2), I_2(h)=\\int_{h^{1/4}}^1 \\frac{hf(x)}{h^2 + x^2} dx$"
                },
                {
                    "type": "Obtain",
                    "obtained_variable": ["$\\xi$"],
                    "condition": [
                        "$\\xi:\\R\\to \\R \\land \\forall h\\in (0,1/2),\\xi(h)\\in [0, h^{1/4}]$",
                        "$\\forall h\\in (0,1/2),I_1(h) = \\int_0^{h^{1/4}} \\frac{hf(x)}{h^2 + x^2} dx = f(\\xi(h)) \\int_0^{h^{1/4}} \\frac{h}{h^2 + x^2} dx$"
                    ],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\forall h \\in (0,1/2),f(\\xi(h)) \\int_0^{h^{1/4}} \\frac{h}{h^2 + x^2} dx = f(\\xi(h)) \\arctan \\frac{x}{h} \\Big|_0^{h^{1/4}} = f(\\xi(h)) \\arctan \\frac{1}{h^{3/4}}$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\lim_{h \\to 0^+} f(\\xi(h)) \\arctan \\frac{1}{h^{3/4}} = f(0)\\dfrac{\\pi}{2}$"],
                    "reason": null
                },
                {
                    "type": "Obtain",
                    "obtained_variable": ["$M$"],
                    "condition": ["$M \\in \\R$", "$\\forall x \\in [0,1],|f(x)|\\leq M$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\forall h \\in (0,1/2),|I_2(h)| = \\left| \\int_{h^{1/4}}^1 \\frac{h}{h^2 + x^2} f(x) dx \\right| \\leq M \\int_{h^{1/4}}^1 \\frac{h}{h^2 + x^2} dx$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\forall h \\in (0,1/2),M \\int_{h^{1/4}}^1 \\frac{h}{h^2 + x^2} dx = M \\left( \\arctan \\frac{1}{h} - \\arctan \\frac{1}{h^{3/4}} \\right)$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\lim_{h \\to 0^+} M \\left( \\arctan \\frac{1}{h} - \\arctan \\frac{1}{h^{3/4}} \\right) = 0$"],
                    "reason": null
                },
                {
                    "type": "Have",
                    "claim": ["$\\lim_{h \\to 0^+} (I_1(h) + I_2(h)) = f(0)\\dfrac{\\pi}{2}$"],
                    "reason": null
                }
            ]
        }
    ]
}
```

## Example 10

**Induction using an explicit variable `k`:**
"""
$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
Proof: 
We prove by mathematical induction. 
When $n = 1$, the equality holds. 
Assume the equality holds for $n = k$. 
Then for $n = k + 1$, we have 
$1 + 2 + \cdots + k + (k + 1) = \frac{k(k + 1)}{2} + k + 1 = \frac{(k + 1)[(k + 1) + 1]}{2}$. 
Thus, the equality also holds for $n = k + 1$. 
Therefore, for any positive integer $n$, we have $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
"""

```json
[
    {
        "type": "Show",
        "proposition": ["$\\forall n \\in \\N^*, 1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
        "method": ["mathematical induction"],
        "scope": [
            {
                "type": "Have",
                "claim": ["When $n = 1$, $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds"],
                "reason": null
            },
            {
                "type": "Fix",
                "variable": ["$k$"],
                "condition": ["$1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds for n=k"],
                "scope": [
                    {
                        "type": "Have",
                        "claim": ["$1 + 2 + \\cdots + k + (k + 1) = \\frac{k(k + 1)}{2} + k + 1 = \\frac{(k + 1)[(k + 1) + 1]}{2}$"],
                        "reason": null
                    },
                    {
                        "type": "Have",
                        "claim": ["$1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds for n = k + 1"],
                        "reason": null
                    }
                ]
            }
        ]
    },
    {
        "type": "Have",
        "claim": ["for any positive integer $n$, $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
        "reason": null
    }
]
```

**Induction reusing the variable `n`:**
"""
$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
Proof: 
We prove by mathematical induction. 
When $n = 1$, the equality holds. 
Assume the equality holds for $n$. 
Then 
$1 + 2 + \cdots + n + (n + 1) = \frac{n(n + 1)}{2} + n + 1 = \frac{(n + 1)[(n + 1) + 1]}{2}$. 
Thus, the equality also holds for $n + 1$. 
Therefore, for any positive integer $n$, we have $1 + 2 + \cdots + n = \frac{n(n + 1)}{2}$.
"""

```json
[
    {
        "type": "Show",
        "proposition": ["$\\forall n \\in \\N^*, 1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
        "method": ["mathematical induction"],
        "scope": [
            {
                "type": "Have",
                "claim": ["When $n = 1$, $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$ holds"],
                "reason": null
            },
            {
                "type": "Fix",
                "variable": ["$n$"],
                "condition": ["$1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
                "scope": [
                    {
                        "type": "Have",
                        "claim": ["$1 + 2 + \\cdots + n + (n + 1) = \\frac{n(n + 1)}{2} + n + 1 = \\frac{(n + 1)[(n + 1) + 1]}{2}$"],
                        "reason": null
                    },
                    {
                        "type": "Have",
                        "claim": ["$1 + 2 + \\cdots + n+(n+1) = \\frac{(n+1)((n+1) + 1)}{2}$"],
                        "reason": null
                    }
                ]
            }
        ]
    },
    {
        "type": "Have",
        "claim": ["for any positive integer $n$, $1 + 2 + \\cdots + n = \\frac{n(n + 1)}{2}$"],
        "reason": null
    }
]
```

## Example 11

**Natural language text:**
"""
**Lemma 13.1.**  *Let $X$ be a set; let $\mathcal{B}$ be a basis for a topology $\mathcal{T}$ on $X$. Then $\mathcal{T}$ equals the collection of all unions of elements of $\mathcal{B}$.*

*Proof.* Given a collection of elements of $\mathcal{B}$, they are also elements of $\mathcal{T}$. Because $\mathcal{T}$ is a topology, their union is in $\mathcal{T}$. Conversely, given $U \in \mathcal{T}$, choose for each $x \in U$ an element $B_x$ of $\mathcal{B}$ such that $x \in B_x \subset U$. Then $U = \bigcup_{x \in U} B_x$, so $U$ equals a union of elements of $\mathcal{B}$. ■
"""

**Correct Structure**
```json
{
  "structure": [
    {
      "type": "Hint",
      "text": "Lemma 13.1."
    },
    {
      "type": "Fix",
      "variable": [
        "$X$",
        "$\\mathcal{B}$",
        "$\\mathcal{T}$"
      ],
      "condition": [
        "$X$ is a set",
        "$\\mathcal{B}$ is a basis for a topology $\\mathcal{T}$ on $X$"
      ],
      "scope": [
        {
          "type": "Show",
          "proposition": [
            "$\\mathcal{T}$ equals the collection of all unions of elements of $\\mathcal{B}$"
          ],
          "method": null,
          "scope": [
            {
              "type": "Show",
              "proposition": [
                "Any union of elements of $\\mathcal{B}$ is in $\\mathcal{T}$"
              ],
              "method": null,
              "scope": [
                {
                  "type": "Fix",
                  "variable": [
                    "$\\mathcal{C}$"
                  ],
                  "condition": [
                    "$\\mathcal{C}$ is a collection of elements of $\\mathcal{B}$"
                  ],
                  "scope": [
                    {
                      "type": "Have",
                      "claim": [
                        "The elements of $\\mathcal{C}$ are also elements of $\\mathcal{T}$"
                      ],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": [
                        "The union of the elements of $\\mathcal{C}$ is in $\\mathcal{T}$"
                      ],
                      "reason": [
                        "$\\mathcal{T}$ is a topology"
                      ]
                    }
                  ]
                }
              ]
            },
            {
              "type": "Show",
              "proposition": [
                "Any element of $\\mathcal{T}$ is a union of elements of $\\mathcal{B}$"
              ],
              "method": null,
              "scope": [
                {
                  "type": "Fix",
                  "variable": [
                    "$U$"
                  ],
                  "condition": [
                    "$U \\in \\mathcal{T}$"
                  ],
                  "scope": [
                    {
                      "type": "Obtain",
                      "obtained_variable": [
                        "collection $\\{B_x\\}_{x \\in U}$"
                      ],
                      "condition": [
                        "$\\forall x \\in U, B_x \\in \\mathcal{B}$",
                        "$\\forall x \\in U, x \\in B_x \\subset U$"
                      ],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": [
                        "$U = \\bigcup_{x \\in U} B_x$"
                      ],
                      "reason": null
                    },
                    {
                      "type": "Have",
                      "claim": [
                        "$U$ equals a union of elements of $\\mathcal{B}$"
                      ],
                      "reason": null
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

## Example 12

**Natural language text:**
"""
**Theorem 4** (Schröder-Bernstein's Theorem). If $f: A \to B$ and $g: B \to A$ are both injections, then there is a bijection from $A$ into $B$.
**Proof.**
Suppose $f: A \to B, g: B \to A$ are injections. Let’s construct the bijection $h$ from $A$ into $B$.
$$C_0 = \{ a \in A \mid \forall b \in B. \, g(b) \neq a \}$$
$$D_0 = \{ f(a) \mid a \in C_0 \}$$
$$C_1 = \{ a \in A \setminus C_0 \mid \forall b \in B \setminus D_0. \, g(b) \neq a \}$$
We can prove that $C_1 = \{ g(b) \mid b \in D_0 \}$ also.
$$D_1 = \{ f(a) \mid a \in C_1 \}$$
So that we can define
$$C_{n+1} = \{ a \in A \setminus \bigcup_{i=0}^{n} C_i \mid \forall b \in B \setminus \bigcup_{i=0}^{n} D_i. \, g(b) \neq a \}$$
$$D_{n+1} = \{ f(a) \mid a \in C_{n+1} \}$$
And similarly, we can prove that $C_{n+1} = \{ g(b) \mid b \in D_n \}$.
In the end, we can define
$$h(a) := \begin{cases} 
f(a), & \text{if} \, a \in \bigcup_{i=0}^{\infty} C_i \\
b, \, \text{such that} \, g(b) = a, & \text{if} \, a \in A \setminus \bigcup_{i=0}^{\infty} C_i 
\end{cases}$$
Obviously, the $f$ part is a bijection from $C_n$ into $D_n$.
So we just need to prove that the $g$ part is a bijection from $D := B \setminus \bigcup_{i=0}^{\infty} D_i$ into $C := A \setminus \bigcup_{i=0}^{\infty} C_i$.
Thus, it is suffice to prove: (1) $\forall d \in D. \, \exists c \in C. \, g(d) = c$ and (2) $\forall c \in C. \, \exists d \in D. \, g(d) = c$.

- $\forall d \in D. \exists c \in C. g(d) = c$.
  As $g$ is an injection from $B$ into $A$, $\exists c \in A, g(d) = c$.
  Let prove $c \notin C_n$.
  Suppose $c \in C_n$.
  - $n = 0$, Obviously contradiction.
  - $n = m + 1$, $c \in C_{m+1} \Rightarrow d \in D_m$, contradiction.
    Therefore, $c \in C$.
- $\forall c \in C. \exists d \in D. g(d) = c$.
  $\exists d \in B. g(d) = c$. Otherwise, $c \in C_0$, contradiction.
  Let’s prove $d \notin D_n$.
  Suppose $d \in D_n$, so that $c \in C_{n+1}$, contradiction.
  Therefore, $d \in D$.
  Qed.
  """

```json
[
    {
        "type": "Hint",
        "text": "Theorem 4 (Schröder-Bernstein's Theorem)"
    },
    {
        "type": "Fix",
        "variable": ["$A$", "$B$"],
        "condition": ["$A$, $B$ are sets"],
        "scope": [
            {
                "type": "Fix",
                "variable": ["$f$", "$g$"],
                "condition": ["$f: A \\to B$ is an injection", "$g: B \\to A$ is an injection"],
                "scope": [
                    {
                        "type": "Show",
                        "proposition": ["there is a bijection from $A$ into $B$"],
                        "method": null,
                        "scope": [
                            {
                                "type": "Define",
                                "term": "$C_0$",
                                "definition": "$C_0=\\{ a \\in A \\mid \\forall b \\in B, g(b) \\neq a \\}$"
                            },
                            {
                                "type": "Define",
                                "term": "$D_0$",
                                "definition": "$D_0=\\{ f(a) \\mid a \\in C_0 \\}$"
                            },
                            {
                                "type": "Define",
                                "term": "$C_1$",
                                "definition": "$C_1=\\{ a \\in A \\setminus C_0 \\mid \\forall b \\in B \\setminus D_0, g(b) \\neq a \\}$"
                            },
                            {
                                "type": "Have",
                                "claim": ["$C_1 = \\{ g(b) \\mid b \\in D_0 \\}$"],
                                "reason": null
                            },
                            {
                                "type": "Define",
                                "term": "$D_1$",
                                "definition": "$D_1=\\{ f(a) \\mid a \\in C_1 \\}$"
                            },
                            {
                                "type": "Define",
                                "term": "set sequence $\\{C_{n}\\}$",
                                "definition": "$\\forall n>1,C_{n+1}=\\{ a \\in A \\setminus \\bigcup_{i=0}^{n} C_i \\mid \\forall b \\in B \\setminus \\bigcup_{i=0}^{n} D_i, g(b) \\neq a \\}$"
                            },
                            {
                                "type": "Define",
                                "term": "set sequence $\\{D_{n}\\}$",
                                "definition": "$\\forall n>1,D_{n+1}=\\{ f(a) \\mid a \\in C_{n+1} \\}$"
                            },
                            {
                                "type": "Have",
                                "claim": ["$\\forall n \\in \\N, C_{n+1} = \\{ g(b) \\mid b \\in D_n \\}$"],
                                "reason": ["similarly"]
                            },
                            {
                                "type": "Define",
                                "term": "$h$",
                                "definition": "function $h: A \\to B$ such that for any $a \\in A$, $h(a) := \\begin{cases} f(a), & \\text{if } a \\in \\bigcup_{i=0}^{\\infty} C_i \\\\ b, \\text{ such that } g(b) = a, & \\text{if } a \\in A \\setminus \\bigcup_{i=0}^{\\infty} C_i \\end{cases}$"
                            },
                            {
                                "type": "Have",
                                "claim": ["$\\forall n$, the restriction of $f$ to $C_n$ is a bijection onto $D_n$"],
                                "reason": null
                            },
                            {
                                "type": "Define",
                                "term": "$C$",
                                "definition": "$A \\setminus \\bigcup_{i=0}^{\\infty} C_i$"
                            },
                            {
                                "type": "Define",
                                "term": "$D$",
                                "definition": "$B \\setminus \\bigcup_{i=0}^{\\infty} D_i$"
                            },
                            {
                                "type": "SufficesToProve",
                                "sufficient_proposition": [
                                    "$\\forall d \\in D, \\exists c \\in C, g(d) = c$",
                                    "$\\forall c \\in C, \\exists d \\in D, g(d) = c$"
                                ],
                                "reason": null
                            },
                            {
                                "type": "Show",
                                "proposition": ["$\\forall d \\in D, \\exists c \\in C, g(d) = c$"],
                                "method": null,
                                "scope": [
                                    {
                                        "type": "Fix",
                                        "variable": ["$d$"],
                                        "condition": ["$d \\in D$"],
                                        "scope": [
                                            {
                                                "type": "Obtain",
                                                "obtained_variable": ["$c$"],
                                                "condition": ["$c \\in A$", "$g(d) = c$"],
                                                "reason": ["$g$ is a function from $B$ into $A$"]
                                            },
                                            {
                                                "type": "Show",
                                                "proposition": ["$\\forall n, c \\notin C_n$"],
                                                "method": ["contradiction"],
                                                "scope": [
                                                    {
                                                        "type": "Fix",
                                                        "variable": ["$n$"],
                                                        "condition": ["$n \\in \\N$"],
                                                        "scope": [
                                                            {
                                                                "type": "Assume",
                                                                "assumption": ["$c \\in C_n$"],
                                                                "scope": [
                                                                    {
                                                                        "type": "Assume",
                                                                        "assumption": ["$n=0$"],
                                                                        "scope": [
                                                                            {
                                                                                "type": "Have",
                                                                                "claim": ["contradiction"],
                                                                                "reason": null
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "Assume",
                                                                        "assumption": ["$n=m+1$ for some $m \\in \\N$"],
                                                                        "scope": [
                                                                            {
                                                                                "type": "Have",
                                                                                "claim": ["$c \\in C_{m+1} \\implies d \\in D_m$"],
                                                                                "reason": null
                                                                            },
                                                                            {
                                                                                "type": "Have",
                                                                                "claim": ["contradiction"],
                                                                                "reason": null
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "Have",
                                                "claim": ["$c \\in C$"],
                                                "reason": null
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "Show",
                                "proposition": ["$\\forall c \\in C, \\exists d \\in D, g(d) = c$"],
                                "method": null,
                                "scope": [
                                    {
                                        "type": "Fix",
                                        "variable": ["$c$"],
                                        "condition": ["$c \\in C$"],
                                        "scope": [
                                            {
                                                "type": "Obtain",
                                                "obtained_variable": ["$d$"],
                                                "condition": ["$d \\in B$", "$g(d) = c$"],
                                                "reason": ["otherwise $c \\in C_0$, contradiction"]
                                            },
                                            {
                                                "type": "Show",
                                                "proposition": ["$\\forall n, d \\notin D_n$"],
                                                "method": ["contradiction"],
                                                "scope": [
                                                    {
                                                        "type": "Fix",
                                                        "variable": ["$n$"],
                                                        "condition": ["$n \\in \\N$"],
                                                        "scope": [
                                                            {
                                                                "type": "Assume",
                                                                "assumption": ["$d \\in D_n$"],
                                                                "scope": [
                                                                    {
                                                                        "type": "Have",
                                                                        "claim": ["$c \\in C_{n+1}$"],
                                                                        "reason": null
                                                                    },
                                                                    {
                                                                        "type": "Have",
                                                                        "claim": ["contradiction"],
                                                                        "reason": null
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "Have",
                                                "claim": ["$d \\in D$"],
                                                "reason": null
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
```