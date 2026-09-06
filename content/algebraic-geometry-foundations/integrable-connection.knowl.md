+++
id = "algebraic-geometry-foundations/integrable-connection"
title = "Integrable algebraic connection"
kind = "definition"
summary = "An algebraic connection whose curvature vanishes."
aliases = ["flat algebraic connection", "integrable connection"]
domains = ["algebraic-geometry-foundations", "fiber-bundles"]
prerequisites = ["linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a smooth scheme over a field \(k\), and let \(\mathcal E\) be an
\(\mathcal O_X\)-module. An **algebraic connection** on \(\mathcal E\) is a
\(k\)-linear map
\[
\nabla:\mathcal E\longrightarrow
\mathcal E\otimes_{\mathcal O_X}\Omega^1_{X/k}
\]
satisfying the Leibniz rule
\[
\nabla(f s)=f\nabla(s)+s\otimes df.
\]

The connection extends to
\(\mathcal E\otimes\Omega^\bullet_{X/k}\). It is **integrable**, or **flat**,
if its curvature vanishes:
\[
\nabla^2:
\mathcal E\longrightarrow
\mathcal E\otimes\Omega^2_{X/k},
\qquad \nabla^2=0.
\]

## Relation to D-modules

In characteristic \(0\), a [[algebraic-geometry-foundations/locally-free-sheaf|finite-rank locally free sheaf]] with an integrable
connection is equivalently an \(\mathcal O_X\)-coherent
[[algebraic-geometry-foundations/d-module|\(D\)-module]].

## References

1. Nicholas M. Katz, “Nilpotent connections and the monodromy theorem:
   Applications of a result of Turrittin,” *Publications Mathématiques de
   l’IHÉS* 39 (1970), 175–232.
   [DOI](https://doi.org/10.1007/BF02684688).
