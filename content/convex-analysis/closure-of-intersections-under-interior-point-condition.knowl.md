+++
id = "convex-analysis/closure-of-intersections-under-interior-point-condition"
title = "Closure of intersections under an interior-point condition"
kind = "knowl"
summary = "If convex sets have intersecting interiors, closure distributes over their intersection"
aliases = ["closure-of-intersections-under-interior-point-condition", "Closure of intersections under an interior-point condition"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/metric-metric-space", "convex-analysis/norm-normed-vector-space", "convex-analysis/convex-set", "convex-analysis/interior-of-a-set", "convex-analysis/closure-of-a-set", "convex-analysis/segments-from-interior-points-stay-in-the-interior"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "convex-analysis/closure-of-intersections-under-interior-point-condition.md"
+++

**Theorem.**
Let \(X\) be a normed vector space, and let \(\Omega_1,\Omega_2\subset X\) be [[convex-analysis/convex-set|convex]] sets such that
\[
\mathrm{int}(\Omega_1)\cap \mathrm{int}(\Omega_2)\neq\emptyset.
\]
Then
\[
\overline{\Omega_1\cap\Omega_2}=\overline{\Omega_1}\cap\overline{\Omega_2}.
\]

## Remarks

**Context.** In general, \(\overline{A\cap B}\subset \overline{A}\cap\overline{B}\) can be strict. Convexity plus an interior qualification condition forces equality, which is important in convex analysis and duality.

**Proof idea.** Use the existence of an interior point common to both sets to "stabilize" approximations and apply [[convex-analysis/segments-from-interior-points-stay-in-the-interior|interior-segment geometry]] to build sequences in \(\Omega_1\cap\Omega_2\) approximating any point in \(\overline{\Omega_1}\cap\overline{\Omega_2}\).

**Remark.** The conclusion remains valid under the weaker condition \(\mathrm{int}(\Omega_1)\cap \Omega_2\neq\emptyset\).
