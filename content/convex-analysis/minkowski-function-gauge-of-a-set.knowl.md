+++
id = "convex-analysis/minkowski-function-gauge-of-a-set"
title = "Minkowski Function (Gauge)"
kind = "knowl"
summary = "An extended-real-valued functional measuring the dilation needed for a set to contain a vector."
aliases = ["minkowski-function-gauge-of-a-set", "Minkowski Function (Gauge)"]
domains = ["convex-analysis"]
prerequisites = ["linear-algebra/vector-space", "shared-foundations/set", "real-analysis/infimum"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
legacy_source_path = "convex-analysis/minkowski-function-gauge-of-a-set.md"
+++

Let \(X\) be a [[linear-algebra/vector-space|vector space]] and let \(\Omega\subset X\) be nonempty.

The **Minkowski function** (or **Minkowski gauge**) of \(\Omega\) is the function \(p_\Omega:X\to[0,\infty]\) defined by
\[
p_\Omega(x):=\inf\{t\ge 0 \mid x\in t\Omega\}, \qquad x\in X,
\]

with the convention \(\inf(\emptyset)=\infty\).

When \(\Omega\) is [[convex-analysis/balanced-and-absorbing-sets|absorbing]] and [[convex-analysis/convex-set|convex]], the gauge is real-valued and [[convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions|sublinear]]; its strict and non-strict sublevel sets recover [[convex-analysis/algebraic-interior-core|core(Ω) and lin(Ω)]] via [[convex-analysis/properties-of-the-minkowski-functional-of-a-convex-set|the main Minkowski gauge theorem]].

## Examples

- If \(\Omega\) is the closed unit ball of a [[convex-analysis/norm-normed-vector-space|norm]], then \(p_\Omega(x)=\|x\|\).
- If \(\Omega\) is a cone (e.g., \(\mathbb{R}^n_+\)), then \(p_\Omega\) can take the value \(\infty\) outside the cone unless \(\Omega\) is absorbing.
