+++
id = "large-deviations/rate-function"
title = "Rate function"
kind = "knowl"
summary = "A lower semicontinuous function that governs exponential decay rates in large deviations."
aliases = ["rate-function", "Rate function"]
domains = ["large-deviations"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "large-deviations/rate-function.md"
+++

A **rate function** on a topological space \(E\) is a lower semicontinuous function \(I:E\to[0,\infty]\) that is not identically \(+\infty\). Equivalently, for every \(\alpha\in\mathbb R\), its sublevel set
\[
\{x\in E:I(x)\le \alpha\}
\]
is closed in \(E\).

## Interpretation

In a [[large-deviations/large-deviation-principle|large deviation principle]], \(I\) governs exponential decay: values of \(I\) closer to zero correspond to less strongly suppressed outcomes. A [[large-deviations/good-rate-function|good rate function]] additionally has compact sublevel sets.

## Examples

- On \(E=\mathbb R\), the function \(I(x)=x^2/2\) is a rate function.
- For a nonempty closed set \(C\subseteq E\), the function
  \[
  I(x)=\begin{cases}
  0,&x\in C,\\
  +\infty,&x\notin C
  \end{cases}
  \]
  is a rate function.
