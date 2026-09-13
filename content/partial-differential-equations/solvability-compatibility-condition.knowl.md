+++
id = "partial-differential-equations/solvability-compatibility-condition"
title = "Solvability compatibility condition"
kind = "definition"
summary = "A necessary condition on equation data imposed by the requested solution class and boundary conditions."
aliases = ["compatibility condition for solvability", "integral compatibility condition"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "shared-foundations/image", "linear-algebra/linear-map", "convex-analysis/bounded-linear-functional-norm-of-a-functional"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For an equation \(Lu=f\) in a specified solution class, a **compatibility condition** is a condition on \(f\) that is necessary for a solution to exist. In the linear setting, the complete abstract condition is \(f\in\operatorname{im}L\), the [[shared-foundations/image|image]] of the operator with its chosen domain and boundary conditions.

## Integral obstructions

If a linear functional \(\ell\) vanishes on every \(Lu\) in the chosen class, then \(\ell(f)=0\) is necessary. For example, a compactly supported primitive \(u\) on the real line satisfies \(\int u'=0\), so \(u'=f\) requires \(\int f=0\). A list of necessary conditions is not automatically sufficient; sufficiency needs an inverse construction or a range theorem. Changing the support or boundary requirements can change the compatibility conditions.
