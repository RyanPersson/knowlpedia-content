+++
id = "fiber-bundles/instanton"
title = "Yang–Mills instanton"
kind = "definition"
summary = "A finite-action self-dual or anti-self-dual connection on an oriented Riemannian four-manifold."
aliases = ["instanton", "gauge instanton", "ASD instanton"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/principal-g-bundle", "linear-algebra/inner-product", "lie-groups/lie-algebra", "fiber-bundles/principal-connection", "fiber-bundles/curvature-2-form-of-a-principal-connection", "fiber-bundles/self-dual-and-anti-self-dual-connection", "differential-geometry/riemannian-manifold", "differential-geometry/hodge-star-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal bundle]] with compact structure group over an oriented Riemannian four-manifold, and choose an invariant [[linear-algebra/inner-product|inner product]] on its [[lie-groups/lie-algebra|Lie algebra]]. A **Yang–Mills instanton** is a [[fiber-bundles/principal-connection|connection]] \(A\) whose [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature]] has finite action
\[
\int_M |F_A|^2\,d\operatorname{vol}<\infty
\]
and satisfies one of the first-order equations
\[
*F_A=F_A
\qquad\text{or}\qquad
*F_A=-F_A.
\]
Equivalently, \(A\) is a [[fiber-bundles/self-dual-and-anti-self-dual-connection|self-dual or anti-self-dual connection]] of finite energy. On compact \(M\), finiteness is automatic. A common orientation convention reserves “instanton” for the anti-self-dual equation.

## Relation to the Yang–Mills equation

The [[fiber-bundles/bianchi-identity|Bianchi identity]] gives \(d_AF_A=0\). If \(*F_A=\pm F_A\), then \(d_A(*F_A)=0\), so every instanton is a [[fiber-bundles/yangmills-connection|Yang–Mills connection]]. The converse fails: a Yang–Mills connection can have both self-dual and anti-self-dual curvature components.

On a compact four-manifold, the orthogonal decomposition \(F_A=F_A^++F_A^-\) rewrites the Yang–Mills action as a topological Chern–Weil term plus a nonnegative multiple of either \(\|F_A^+\|_{L^2}^2\) or \(\|F_A^-\|_{L^2}^2\). Hence instantons attain the absolute energy bound in their fixed topological class.

## Canonical example

The BPST connection on the charge-one \(SU(2)\)-bundle over \(S^4\) is the basic nonflat instanton. Removing one point and using stereographic coordinates gives a finite-action instanton on \(\mathbb R^4\); its curvature decay makes the noncompact action finite. Its self-dual versus anti-self-dual label changes when the orientation is reversed.

A general finite-action Yang–Mills connection with neither \(F_A^+=0\) nor \(F_A^-=0\) is a near miss: finite action and the second-order [[fiber-bundles/yangmills-equation|Yang–Mills equation]] do not imply the instanton equation.

## Conventions and scope

Some authors exclude flat connections or require nonzero [[fiber-bundles/instanton-number|topological charge]], while the stated definition includes the zero-curvature solution. In higher-dimensional [[fiber-bundles/gauge-theory|gauge theory]], “instanton” can mean a connection solving a different first-order equation determined by special holonomy or a calibration. Such generalized instantons are not covered by this four-dimensional definition.

## References

1. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [DOI record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §2.1, self-duality, the energy identity, and instanton number.
2. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Mathematical Sciences Research Institute Publications 1, Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: “The Yang–Mills Equations,” pp. 28–43, finite-action self-dual connections and their moduli.
