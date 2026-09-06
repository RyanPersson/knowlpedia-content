+++
id = "real-analysis/uniform-limit-theorem"
title = "Uniform limit theorem"
kind = "knowl"
summary = "The uniform limit of continuous functions is continuous."
aliases = ["uniform-limit-theorem", "Uniform limit theorem"]
domains = ["real-analysis"]
prerequisites = ["topology/continuous-map", "real-analysis/uniform-convergence"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
legacy_source_path = "real-analysis/uniform-limit-theorem.md"
+++

**Uniform limit theorem.** Let \(X\) be a topological space and \(Y\) a [[topology/metric-space|metric space]]. If \(f_n:X\to Y\) are [[topology/continuous-map|continuous functions]] and \(f_n\to f\) [[real-analysis/uniform-convergence|uniformly]], then \(f:X\to Y\) is continuous. Uniform convergence means that for every \(\varepsilon>0\) there exists \(N\) such that
\[
n\ge N\quad\Longrightarrow\quad
d_Y\bigl(f_n(x),f(x)\bigr)<\varepsilon
\quad\text{for every }x\in X.
\]

## Counterexample for pointwise convergence
\(f_n(x) = x^n\) on \([0, 1]\) converges pointwise to a discontinuous limit:
\[
f(x) = \begin{cases} 0 & x \in [0,1) \\ 1 & x = 1 \end{cases}.
\]
The convergence is not uniform.
