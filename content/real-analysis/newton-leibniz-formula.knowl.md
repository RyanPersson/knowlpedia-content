+++
id = "real-analysis/newton-leibniz-formula"
title = "Newton–Leibniz formula"
kind = "knowl"
summary = "For continuous f and an antiderivative F, the integral of f over [a,b] equals F(b)-F(a)."
aliases = ["newton-leibniz-formula", "Newton–Leibniz formula"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/continuity-on-a-set", "real-analysis/riemann-integral", "real-analysis/derivative"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "real-analysis/newton-leibniz-formula.md"
+++

Let \(f:[a,b]\to\mathbb{R}\) be [[real-analysis/continuity-on-a-set|continuous]]. If \(F:[a,b]\to\mathbb{R}\) is continuous on \([a,b]\), differentiable on \((a,b)\), and satisfies \(F'(x)=f(x)\) for every \(x\in(a,b)\), then

\[
\int_a^b f(x)\,dx = F(b)-F(a).
\]

## Remarks

This is the evaluation form of the [[real-analysis/fundamental-theorem-of-calculus-i|fundamental theorem of calculus]].
