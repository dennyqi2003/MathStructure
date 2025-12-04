 1 | import Mathlib
 2 | set_option linter.style.longLine false
 3 | 
 4 | open Set Filter Topology Real
 5 | 
 6 | -- [1] [Define] {$x$} as {$\forall n\in \N^*, {x}_{n} = \frac{n}{n + 1}$}
 7 | noncomputable def x_seq (n : ℕ) : ℝ := n / (n + 1)
 8 | 
 9 | theorem x_seq_tensto_1 :
10 |   -- [2] [Show] {$\lim_{n \to \infty} {x}_{n} = 1$}
11 |   Tendsto x_seq atTop (nhds 1)
12 | := by
13 |   -- [3] [Have] {$\forall n \in \N^*, |{x}_{n} - 1| = \frac{1}{n + 1}$}
14 |   have h_abs_eq : ∀ n : ℕ, |x_seq n - 1| = 1 / (n + 1) := by
15 |     sorry
16 |   -- [4] [Fix] {$\varepsilon$} such that {$\varepsilon>0$}
17 |   rw [Metric.tendsto_atTop]
18 |   intro ε h_ε_pos
19 |   -- [5] [Fix] {$n$} such that {$n \in \N^*$}
20 |   -- [6] [LogicChain] {$|{x}_{n} - 1| < \varepsilon$}
21 |   --           <= {$\frac{1}{n + 1} < \varepsilon$}
22 |   --          <=> {$n > \\frac{1}{\\varepsilon} - 1$}
23 |   have h_logic_chain : ∀ n : ℕ, n > 1 / ε - 1 → |x_seq n - 1| < ε := by
24 |     intro n h_condition
25 |     have h_step1 : 1 / (n + 1) < ε → |x_seq n - 1| < ε := by
26 |       sorry
27 |     have h_step2 : 1 / (n + 1) < ε ↔ n > 1 / ε - 1 := by
28 |       sorry
29 |     sorry
30 |   -- [7] [Define] {$N$} as {$N=\lfloor \frac{1}{\varepsilon} \rfloor$}
31 |   let N := ⌊1 / ε⌋
32 |   use N
33 |   sorry
