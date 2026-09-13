+++
id = "convex-analysis/planar-quadratic-cone"
title = "Planar cone defined by a quadratic inequality"
kind = "definition"
summary = "A positive longitudinal component and a quadratic transverse bound describe an open planar wedge."
aliases = ["quadratic wedge criterion"]
domains = ["convex-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/inner-product", "linear-algebra/orthogonality", "convex-analysis/convex-cone", "real-analysis/nonnegative-square-root"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(n,k\) be nonzero orthogonal vectors in \(\mathbb R^2\), and let \(a,b>0\). The inequalities
\[
n\cdot T>0,\qquad a(k\cdot T)^2<b(n\cdot T)^2
\]
are equivalent to
\[
n\cdot T>\sqrt{a/b}\,|k\cdot T|.
\]
They define an open convex wedge invariant under positive scaling. Its closure is a [[convex-analysis/convex-cone|convex cone]] containing zero.

## Why the sign matters

The quadratic inequality without \(n\cdot T>0\) also allows the opposite wedge. The positive longitudinal condition chooses one component. Replacing the strict inequalities by a uniform gap on \(T/|T|\) supplies a directional margin that remains meaningful as \(|T|\) tends to zero.
