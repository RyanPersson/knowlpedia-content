+++
id = "convex-analysis/holder-inequality-integrals"
title = "Hölder inequality (integrals)"
kind = "knowl"
summary = "The integral of |fg| is bounded by the product of the conjugate L^p and L^q norms."
aliases = ["holder-inequality-integrals", "Hölder inequality (integrals)"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/holder-inequality-integrals.md"
prerequisites = ["measure-theory/lp-space", "measure-theory/measurable-function", "convex-analysis/youngs-inequality"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++


Let \((X,\Sigma,\mu)\) be a measure space and let \(1\le p,q\le\infty\) satisfy \(1/p+1/q=1\), with \(1/\infty=0\). For real or complex \(f\in L^p\) and \(g\in L^q\), **Hölder's inequality** is
\[
\int_X|fg|\,d\mu\le\|f\|_p\|g\|_q.
\]

## Proof and endpoints

For \(1<p,q<\infty\) and nonzero norms, normalize both functions to norm one, apply [[convex-analysis/youngs-inequality|Young's product inequality]] pointwise, and integrate. If a norm is zero, the corresponding function vanishes almost everywhere. At the endpoint \(p=1,q=\infty\), use \(|fg|\le|f|\|g\|_\infty\) almost everywhere; the other endpoint is symmetric.

## Special cases

Counting measure gives the finite-sum and sequence versions. For \(p=q=2\), this is the integral [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]]. On a measurable set \(E\) of finite measure, applying it to \(|f|\) and \(\mathbf1_E\) gives \(\|f\|_{L^1(E)}\le\mu(E)^{1-1/p}\|f\|_{L^p(E)}\).

## References

- [John K. Hunter, Measure Theory, Theorem 7.7](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf).
