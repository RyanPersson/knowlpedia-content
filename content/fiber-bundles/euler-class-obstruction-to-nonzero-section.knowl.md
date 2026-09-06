+++
id = "fiber-bundles/euler-class-obstruction-to-nonzero-section"
title = "Euler class obstruction to a nowhere-zero section"
kind = "theorem"
summary = "A nowhere-zero section forces the Euler class to vanish, and in base dimension equal to the bundle rank this is the complete obstruction."
aliases = ["Euler obstruction", "nonvanishing-section obstruction"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/section-of-a-vector-bundle", "fiber-bundles/bundle-metric", "fiber-bundles/sphere-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\to X\) be an oriented real rank-\(n\) [[fiber-bundles/vector-bundle|vector bundle]] over a CW complex. If \(E\) admits a nowhere-zero [[fiber-bundles/section-of-a-fiber-bundle|section]], then
\[
e(E)=0\in H^n(X;\mathbb Z).
\]
More precisely, \(e(E)\) is the primary obstruction to a section of the unit sphere bundle \(S(E)\to X\). Consequently, when \(\dim X\leq n\), the Euler class is the complete obstruction: such a section exists if and only if \(e(E)=0\). For bases of dimension greater than \(n\), higher obstruction classes may remain after \(e(E)\) vanishes.

## Obstruction-theoretic mechanism

A [[fiber-bundles/bundle-metric|bundle metric]] turns a [[fiber-bundles/nowhere-vanishing-section|nowhere-zero section]]
into a section of the
[[fiber-bundles/sphere-bundle|sphere bundle]] \(S(E)\), whose fiber is
\(S^{n-1}\). Since \(S^{n-1}\) is \((n-2)\)-connected, a section extends
through the \((n-1)\)-skeleton. The first possible obstruction lies in degree
\(n\), with coefficients \(\pi_{n-1}(S^{n-1})\cong\mathbb Z\). The orientation
trivializes this local coefficient system, and the resulting class is \(e(E)\).
There are no cells on which a higher obstruction could live when
\(\dim X\le n\).

## Geometric interpretation

For a smooth section transverse to the [[fiber-bundles/zero-section|zero section]], its zero set represents the Poincaré dual of \(e(E)\). When the base and bundle both have dimension \(n\), the signed count of isolated zeros equals
\[
\langle e(E),[X]\rangle.
\]
Applied to \(E=TM\) on a closed oriented manifold, this is the Poincaré–Hopf
theorem: the total index of a [[fiber-bundles/vector-field|vector field]] is
\(\chi(M)\). Thus the even sphere has no nowhere-zero tangent vector field.

## Scope and near-misses

**Warning.** Vanishing of \(e(E)\) alone need not produce a section when \(\dim X>n\); the Euler class is only the first obstruction in that range.

For a nonorientable bundle, the primary obstruction lives in cohomology with the orientation local system rather than ordinary integral cohomology. A section that vanishes somewhere is not a counterexample: the required condition is nowhere-zero, not merely nonzero as an element of the [[fiber-bundles/module-of-smooth-sections|section module]].

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: Euler classes, zero sections, and the obstruction interpretation.
2. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-4008-0). Relevant: sphere bundles, cross-sections, and obstruction theory for vector bundles.
