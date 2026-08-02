+++
id = "topology/one-point-compactification"
title = "One-point compactification"
kind = "construction"
summary = "A compact space obtained by adjoining one point whose neighborhoods have compact complements."
aliases = ["Alexandroff compactification", "point at infinity"]
domains = ["topology"]
section_mode = "progressive"
+++

Let \(X\) be a noncompact, [[topology/locally-compact-space|locally compact]] [[topology/hausdorff-space|Hausdorff space]]. Its **one-point compactification** is the set
\[
X^+=X\sqcup\{\infty\}
\]
with the original open subsets of \(X\), together with neighborhoods of \(\infty\) of the form
\[
\{\infty\}\cup(X\setminus K),
\]
where \(K\subseteq X\) is compact. This topology makes \(X^+\) a compact Hausdorff space containing \(X\) as an open dense subspace.

## Characterization

Up to a homeomorphism fixing \(X\), \(X^+\) is the unique compact Hausdorff space obtained from \(X\) by adjoining exactly one point. Local compactness supplies enough neighborhoods to separate \(\infty\) from points of \(X\).

## Examples

- The one-point compactification of \(\mathbb R\) is a circle.
- The one-point compactification of \(\mathbb R^n\) is the sphere \(S^n\).
- The one-point compactification of \(\mathbb C\) is the [[complex-analysis/riemann-sphere|Riemann sphere]] \(\mathbb C\cup\{\infty\}\).

## Convention

Some authors also apply the construction to compact \(X\), in which case the adjoined point is isolated. Restricting to noncompact \(X\) gives the dense-embedding characterization above.

## References

1. John M. Lee, *Introduction to Topological Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7940-7). Relevant: compactifications and locally compact Hausdorff spaces.
