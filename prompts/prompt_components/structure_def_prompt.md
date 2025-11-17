## Definition of Structure

### Node Types

The basic units of the structure of mathematical natural language are 11 different types of nodes:

#### 'Show' Node

- Semantics: "We will now prove proposition P, with hint Q".
- JSON:
```json
{
	"type": "Show",
	"proposition": [...],
	"method": [...]
}
```
- Explanation: The Show node corresponds to the overall proof goal, or subgoals in a proof text or in a problem solving text. Here, the hint Q is an indication for the proof method, for example 'induction'.

Example 1:
"Below we prove that the set $S$ is not empty and the set $T$ is not empty"

```json
{
	"type": "Show",
	"proposition": ["the set $S$ is not empty", "the set $T$ is not empty"],
	"method": null
}
```

Example 2:
"We use induction to prove $\forall n\in \N,f(n)\geq g(n)$ using theorem 3.1"

```json
{
	"type": "Show",
	"proposition": ["$\\forall n \\in \\N,f(n) \\geq g(n)$"],
	"method": ["induction", "theorem 3.1"]
}
```

Example 3:
"We show that $k\neq 0$. We prove by contradiction, ..."

```json
{
	"type": "Show",
	"proposition": ["$k \neq 0$"],
	"method": ["contradiction"]
}
```

#### 'Assume' Node

- Semantics: "Assume proposition P holds."
- JSON:
  ```json
  {
      "type": "Assume",
      "assumption": [...]
  }
  ```
- Explanation: 'Assume' nodes are used in the premises of the overall proof goal, or temporary assumptions introduced in the middle of the text, e.g. the conditions for each case in a "case analysis". (For situations that introduces new variables, although natural language might use the words "assume" or "let" or "suppose", it generally needs to be identified as a 'Fix' node, which will be introduced later(see Example 3). 'Assume' nodes only applies to situations that a assumption has been made, but NO NEW VARIABLES HAVE BEEN INTRODUCED in the text environment. Care must be taken to distinguish between Assume and Fix nodes!!!)

Example 1:
"Assume $a > 0$ and $a \in \mathbb{Q}$" (when $a$ has already been introduced above)

```json
{
    "type": "Assume",
    "assumption": ["$a > 0$", "$a \\in \\mathbb{Q}$"]
}
```

Example 2:
"Case 1: $n$ is even"

```json
{
    "type": "Assume",
    "assumption": ["$n$ is even"]
}
```

Example 3:
"Let $\varepsilon > 0$" ($\varepsilon$ is a newly introduced variable - This should be a Fix node.)

```json
{
    "type": "Fix",
    "variable": ["$\\varepsilon$"],
    "condition": ["$\\varepsilon > 0$"]
}
```

#### 'Fix' Node

- Semantics: "Fix a variable list `variables`, these variables satisfy proposition P."
- JSON:
  ```json
  {
      "type": "Fix",
      "variable": [...],
      "condition": [...]
  }
  ```
- Explanation: The Fix node introduces one or a list of new variables satisfying specific conditions. It corresponds to expressions in natural language like "for any ...", "for all ...", "given ...", "let ...", etc. Logically, it is equivalent to the universal quantifier (`∀`). Again, note the distinction between Fix and Assume nodes!

Example 1:
"For any $\varepsilon > 0$" ($\varepsilon$ is a newly introduced variable)

```json
{
    "type": "Fix",
    "variable": ["$\\varepsilon$"],
    "condition": ["$\\varepsilon > 0$"]
}
```

Example 2:
"Let $x, y$ be arbitrary real numbers"

```json
{
    "type": "Fix",
    "variable": ["$x$", "$y$"],
    "condition": ["$x, y$ are real numbers"]
}
```
(always use LaTeX expression to write variables)

Example 3:
"Let $x_1, ..., x_n$, $y_1, ..., y_n$ be arbitrary real numbers"

```json
{
    "type": "Fix",
    "variable": ["$x_1, ..., x_n$","$y_1, ..., y_n$"],
    "condition": ["$x_1, ..., x_n$, $y_1, ..., y_n$ are real numbers"]
}
```
(remark: when variables are written with '...', we put them in one string)

#### 'Have' Node

- Semantics: "claim P, the reasons for this assertion is Q."
- JSON:
  ```json
  {
      "type": "Have",
      "claim": [...],
      "reason": [...]
  }
  ```
- Explanation: A reason can be a theorem name, a previously proven conclusion(in natural language), or a natural language hint. If the original claim in the given text did not state a reason, then the "reason" should be empty.

Example 1:
"Therefore, $x>0$"

```json
{
    "type": "Have",
    "claim": ["$x>0$"],
    "reason": null
}
```

Example 2:
"By Lemma 1.2 and Lemma 1.3, $A$ is a closed set"

```json
{
    "type": "Have",
    "claim": ["$A$ is a closed set"],
    "reason": ["Lemma 1.2", "Lemma 1.3"]
}
```

#### 'Obtain' Node

- Semantics: "Claim the existence of the variable list `obtained_variable`, these variables satisfy the "condition", by "reason"."
- JSON:
  ```json
  {
      "type": "Obtain",
      "obtained_variable": [...],
      "condition": [...],
      "reason": [...]
  }
  ```
- Explanation: Logically, the Obtain node corresponds to the existential quantifier (`∃`); it asserts that variables satisfying specific properties exist. The `reason` part indicates the reason for the claim, similar to the 'Have' node.

Example 1:
"By the Mean Value Theorem, there exists $\xi \in (a,b)$ such that $f'(\xi)=0$"

```json
{
    "type": "Obtain",
    "obtained_variable": ["$\\xi$"],
    "condition": ["$\\xi \\in (a,b)$", "$f'(\\xi)=0$"],
    "reason": ["the Mean Value Theorem"]
}
```

Example 2:
"So there exists an integer $k$ such that $n=2k$"

```json
{
    "type": "Obtain",
    "obtained_variable": ["$k$"],
    "condition": ["$k$ is an integer", "$n=2k$"],
    "reason": null
}
```

Example 3:
"By the Bolzano-Weierstrass theorem, there exists a convergent subsequence in $\{x_n\}$: $\lim_{k \to \infty} x_{n_k} = \xi$."

```json
{
    "type": "Obtain",
    "obtained_variable": ["$\\{x_{n_k}\\}$", "$\\xi$"],
    "condition": ["$\\{x_{n_k}\\}$ is a subsequence of $\\{x_n\\}$", "$\\lim_{k \to \\infty} x_{n_k} = \\xi$"],
    "reason": ["Bolzano-Weierstrass theorem"]
}
```
In fact, "obtaining a subsequence" essentially means "obtaining a mapping $n:\mathbb{N}$ to $\mathbb{N}$". But sometimes it is difficult to extract the exact new variable we have newly obtained. Instead, we allow putting the full expression in "obtained_variable", and the introduction of this expression implicitly entails the introduction of a certain variable.

#### 'SufficesToProve' Node

- Semantics: "claim that to prove the current proof goal, it suffices to prove "sufficient_proposition", with the reason being "reason"."
- JSON:
  ```json
  {
      "type": "SufficesToProve",
      "sufficient_proposition": [...],
      "reason": [...]
  }
  ```
- Explanation: SufficesToProve is a transformation of the current proof goal during the proof process. The current proof goal could be the overall goal of the proof text or some subgoal, depending on the current context. It corresponds to natural language expressions like "it suffices to prove", "we only need to prove"...

Example 1:
"It suffices to prove $x \in A$ and $x \in B$"

```json
{
    "type": "SufficesToProve",
    "sufficient_proposition": ["$x \\in A$", "$x \\in B$"],
    "reason": null
}
```

Example 2:
"Since $A\subseteq B$, it suffices to prove $\forall x \in B, f(x)=0$"

```json
{
    "type": "SufficesToProve",
    "sufficient_proposition": ["$\\forall x \\in B, f(x)=0$"],
    "reason": ["$A \\subseteq B$"]
}
```

#### 'LogicChain' Node

- Semantics: "A logical derivation chain. The chain consists of an initial proposition and a sequence of steps, each with an operator, a resulting proposition, and an optional reason."
- JSON:
  ```json
  {
      "type": "LogicChain",
      "initial_proposition": [...],
      "step": [
          {
              "operator": "...",
              "proposition": [...],
              "reason": [...]
          },
          ...
      ]
  }
  ```
- Explanation: Used to represent long strings of logical derivations in natural language. If all symbols are forward implications (left implies right), then LogicChain is equivalent to a series of Have nodes. However, if the derivation involves backward implications, or a mix of forward, backward, and bidirectional implications, it is generally represented by a LogicChain node.

Example 1:
"$\begin{aligned}P_1&\iff P_2&(reason1) \\ &\implies P_3&(reason2)\\&\implies P_4\end{aligned}$"

```json
{
    "type": "LogicChain",
    "initial_proposition": ["$P_1$"],
    "step": [
        {
            "operator": "<=>",
            "proposition": ["$P_2$"],
            "reason": ["reason1"]
        },
        {
            "operator": "=>",
            "proposition": ["$P_3$"],
            "reason": ["reason2"]
        },
        {
            "operator": "=>",
            "proposition": ["$P_4$"],
            "reason": null
        }
    ]
}
```

Example 2:
"to have $|{x}_{n} - 1| < \varepsilon$, it suffices to have $\frac{1}{n + 1} < \varepsilon$, i.e., $n > \frac{1}{\varepsilon} - 1$."

```json
{
    "type": "LogicChain",
    "initial_proposition": ["$|{x}_{n} - 1| < \\varepsilon$"],
    "step": [
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
```

#### 'CalculationChain' Node

- Semantics: "Represents a calculation chain. The chain consists of an initial expression and a sequence of steps, each with an operator, a resulting expression, and an optional reason."
- JSON:
  ```json
  {
      "type": "CalculationChain",
      "initial_expression": [...],
      "step": [
          {
              "operator": "...",
              "expression": [...],
              "reason": [...]
          },
          ...
      ]
  }
  ```
- Explanation: Similar to LogicChain, CalculationChain is used to represent consecutive calculation steps, such as long chains of equalities or estimation processes.

Example 1:
"
$|a_n b_n + \cdots + a_{n+k} b_{n+k}| = |B_n a_n + B_{n+1} (a_{n+1} - a_n) + \cdots + B_{n+k} (a_{n+k} - a_{n+k-1}) + B_{n+k+1} a_{n+k}|$ (Lemma)
$\leq |B_n a_n| + |B_{n+1} (a_{n+1} - a_n)| + \cdots + |B_{n+k} (a_{n+k} - a_{n+k-1})| + |B_{n+k+1} a_{n+k}|$ (Triangle Inequality for Complex Numbers)
$\leq M \epsilon + M \epsilon$
$= 3M \epsilon$
"

```json
{
    "type": "CalculationChain",
    "initial_expression": ["$|a_n b_n + \\cdots + a_{n+k} b_{n+k}|$"],
    "step": [
        {
            "operator": "=",
            "expression": ["$|B_n a_n + B_{n+1} (a_{n+1} - a_n) + \\cdots + B_{n+k} (a_{n+k} - a_{n+k-1}) + B_{n+k+1} a_{n+k}|$"],
            "reason": ["Lemma"]
        },
        {
            "operator": "<=",
            "expression": ["$|B_n a_n| + |B_{n+1} (a_{n+1} - a_n)| + \\cdots + |B_{n+k} (a_{n+k} - a_{n+k-1})| + |B_{n+k+1} a_{n+k}|$"],
            "reason": ["Triangle Inequality for Complex Numbers"]
        },
        {
            "operator": "<=",
            "expression": ["$M \\epsilon + M \\epsilon$"],
            "reason": null
        },
        {
            "operator": "=",
            "expression": ["$3M \\epsilon$"],
            "reason": null
        }
    ]
}
```

#### 'Find' Node

- Semantics: "To find out(solve) the target, which satisfies certain condition(optional)"
- JSON:
  ```json
  {
      "type": "Find",
      "target": [...],
      "condition": [...]
  }
  ```
- Explanation: The Find node is used to represent a "problem-solving" task. For example, tasks like "compute the value of ...", "simplify the expression", "solve the equation ...", or "find all sets satisfying ...". Its purpose is not to "prove" a proposition, but to "find" an object satisfying specific conditions. **The target can be variables or expressions. For tasks like simplification or evaluating an expression, "condition" should be empty.** 

Example 1:
"Find the solutions to the equation $x^2 -3x+ 4 = 0$"

```json
{
    "type": "Find",
    "target": ["$x$"],
    "condition": ["$x^2 - 3x + 4 = 0$"]
}
```

Example 2:
"Now we compute the integral $\int_0^1 x dx$"

```json
{
    "type": "Find",
    "target": ["$\\int_0^1 x dx$"],
    "condition": null
}
```

#### 'Define' Node

- Semantics: "Define a 'variable/symbol/concept' "term", whose meaning is "definition"."
- JSON:
  ```json
  {
      "type": "Define",
      "term": "...",
      "definition": "..."
  }
  ```
- Explanation: Used to define new variables, symbols, or concepts.

Example 1:
"Let $M = \sup_{x \in S} f(x)$"

```json
{
    "type": "Define",
    "term": "$M$",
    "definition": "$M = \\sup_{x \\in S} f(x)$"
}
```

Example 2:
"We call $G$ an Abelian group if $G$ is a group and its operation is commutative"

```json
{
    "type": "Define",
    "term": "Abelian group",
    "definition": "$G$ is an Abelian group if $G$ is a group and its operation is commutative"
}
```

#### 'Hint' Node

- Semantics: "a natural language annotation."
- JSON:
  ```json
  {
      "type": "Hint",
      "text": "..."
  }
  ```
- Explanation: Natural language texts often contain explanatory, annotative text that **does not have specific mathematical meaning**. For example, transitional text, author's comments, emphasis on the importance of a conclusion, or an intuitive overview of the upcoming proof steps or calculation steps.

Example 1:
"Thus we can obtain the answer"

```json
{
    "type": "Hint",
    "text": "Thus we can obtain the answer"
}
```

Example 2:
"The idea of this proof is very clever"

```json
{
    "type": "Hint",
    "text": "The idea of this proof is very clever"
}
```

Example 3:
"Next we use a skillful technique to prove this conclusion; a more natural proof method will be introduced in Chapter 4"

```json
{
    "type": "Hint",
    "text": "Next we use a skillful technique to prove this conclusion; a more natural proof method will be introduced in Chapter 4"
}
```

### Scope

Now we define the scope of a node.

Only four types of node have a scope: 'Show', 'Assume', 'Fix', and 'Find'. Other types of nodes do not.

In the scope of a node is another structure defined exactly the same as the outer structure. Hnece, a structure is a nested multi-level node sequences.

The content within the scope of these four nodes is generally:

- Show: The scope of a Show node contains the proof for that proof goal;
- Assume: The scope of an Assume node corresponds to the text content that acknowledges the assumption holds;
- Fix: The scope of a Fix node contains text content about the newly introduced variables;
- Find: The scope of a Find node is the specific process of finding or solving;