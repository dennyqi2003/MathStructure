-- 导入我们需要的基础定义
import Mathlib.GroupTheory.Subgroup.Basic -- 定义 Subgroup 和 Subgroup.is_abelian
import Mathlib.GroupTheory.CommutingElements -- 定义 Commute 和相关引理

-- Exercise 2.2.9
theorem generated_subgroup_of_commuting_elements_is_abelian
  {G : Type*} [Group G] (a b : G) (H : Subgroup G)
  (hH : H = Subgroup.closure {a, b})
  (h_comm : a * b = b * a) : -- 假设 a 和 b 交换
  Subgroup.is_abelian H :=    -- 结论：H 是一个阿贝尔子群
by
  -- 1. 将 'H' 替换为其定义
  rw [hH]

  -- 现在的目标是证明: Subgroup.is_abelian (Subgroup.closure {a, b})
  -- 即：由 {a, b} 生成的子群是阿贝尔群

  -- 2. 展开 "is_abelian" 的定义
  rw [Subgroup.is_abelian_def]

  -- 现在的目标是证明:
  -- ∀ (x y : ↥(Subgroup.closure {a, b})), x * y = y * x
  -- 即：对于 closure 中的任意两个元素 x 和 y，它们都交换。

  -- 3. Mathlib 有一个完美的引理：Commute.closure_commute
  -- 它指出：如果 x 和 y 交换，那么由 {x, y} 生成的子群中的任何两个元素也都交换。
  apply Commute.closure_commute

  -- 4. 证明 'Commute.closure_commute' 的前提条件，
  -- 即 a 和 b 交换，这正是我们的假设 h_comm。
  exact h_comm
