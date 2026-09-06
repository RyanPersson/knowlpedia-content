+++
id = "convex-analysis/convexity-of-the-marginal-optimal-value-function"
title = "Convexity of the Marginal (Optimal Value) Function"
kind = "knowl"
summary = "A jointly convex objective minimized over a convex feasible graph has a convex marginal value function."
aliases = ["convexity-of-the-marginal-optimal-value-function", "Convexity of the Marginal (Optimal Value) Function"]
domains = ["convex-analysis"]
prerequisites = ["linear-algebra/vector-space", "convex-analysis/convex-function-via-epigraph", "convex-analysis/marginal-optimal-value-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "convex-analysis/convexity-of-the-marginal-optimal-value-function.md"
+++

**Convexity of the marginal function.** Let \(X\) and \(Y\) be real [[linear-algebra/vector-space|vector spaces]]. Suppose \(\varphi:X\times Y\to(-\infty,+\infty]\) is [[convex-analysis/convex-function-via-epigraph|convex]] and the graph of \(F:X\rightrightarrows Y\) is convex. Define the [[convex-analysis/marginal-optimal-value-function|marginal function]]
\[
\mu(x)=\inf\{\varphi(x,y):y\in F(x)\},
\]
with \(\inf\varnothing=+\infty\). Then \(\mu\) is convex on \(X\).

## Interpretation

The theorem explains why optimal values in convex optimization vary convexly with parameters: joint convexity of the objective and convexity of the feasible graph survive partial minimization.

## Proof idea

For \(0<\lambda<1\), choose feasible points \(y_i\in F(x_i)\) with nearly minimal objective values. Convexity of the graph makes \(\lambda y_1+(1-\lambda)y_2\) feasible at \(\lambda x_1+(1-\lambda)x_2\), and convexity of \(\varphi\) gives the required inequality after the approximation error tends to zero.
