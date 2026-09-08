+++
id = "fiber-bundles/euler-class-obstruction-to-nonzero-section"
title = "Euler class obstruction to a nowhere-zero section"
kind = "theorem"
summary = "A nowhere-zero section forces the Euler class to vanish, and in base dimension equal to the bundle rank this is the complete obstruction."
aliases = ["Euler obstruction", "nonvanishing-section obstruction"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/topological-real-vector-bundle", "topology/cw-complex", "fiber-bundles/euler-class-as-zero-section"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\to X\) be an oriented real rank-\(n\) [[fiber-bundles/topological-real-vector-bundle|topological vector bundle]] with \(n\ge2\) over a [[topology/cw-complex|CW complex]]. If \(E\) admits a continuous section \(s:X\to E\) satisfying \(\pi s=\operatorname{id}_X\) and \(s(x)\ne0_x\) for all \(x\), then
\[
e(E)=0\in H^n(X;\mathbb Z).
\]
Here \(e(E)\) is the [[fiber-bundles/euler-class-as-zero-section|integral Euler class]]. More precisely, \(e(E)\) is the primary obstruction to a section of the unit sphere bundle \(S(E)=\{v:\|v\|=1\}\to X\) for any continuous positive-definite fiber metric (the topological unit sphere is defined by the displayed norm equation). Consequently, when \(\dim X\leq n\), the Euler class is the complete obstruction: such a section exists if and only if \(e(E)=0\). For bases of dimension greater than \(n\), higher obstruction classes may remain after \(e(E)\) vanishes.

## Obstruction-theoretic mechanism

A continuous positive-definite fiber metric turns a nowhere-zero section
into a section of the
unit sphere bundle \(S(E)\), whose fiber is
\(S^{n-1}\). Since \(S^{n-1}\) is \((n-2)\)-connected, a section extends
through the \((n-1)\)-skeleton. The first possible obstruction lies in degree
\(n\), with coefficients \(\pi_{n-1}(S^{n-1})\cong\mathbb Z\). The orientation
trivializes this local coefficient system, and the resulting class is \(e(E)\).
There are no cells on which a higher obstruction could live when
\(\dim X\le n\).

## Geometric interpretation

For a smooth bundle over a closed oriented smooth base, a smooth section transverse to the [[fiber-bundles/zero-section|zero section]] has a zero set representing the Poincaré dual of \(e(E)\). When the base and bundle both have dimension \(n\), the signed count of isolated zeros equals
\[
\langle e(E),[X]\rangle.
\]
Applied to \(E=TM\) on a closed oriented manifold, this is the Poincaré–Hopf
theorem: the total index of a [[fiber-bundles/vector-field|vector field]] is
\(\chi(M)\). Thus \(S^{2m}\), for \(m\ge1\), has no nowhere-zero tangent vector field.

## Rank zero and rank one

An oriented real line bundle over a CW complex is trivial, so it has a nowhere-zero section and Euler class zero in every base dimension. The displayed obstruction argument using \(\pi_{n-1}(S^{n-1})\cong\mathbb Z\) is for \(n\ge2\). A rank-zero bundle over a nonempty base has no nowhere-zero section and has Euler class \(1\in H^0(X;\mathbb Z)\).

## Scope and near-misses

**Warning.** Vanishing of \(e(E)\) alone need not produce a section when \(\dim X>n\); the Euler class is only the first obstruction in that range.

For a nonorientable bundle, the primary obstruction lives in cohomology with the orientation local system rather than ordinary integral cohomology. A section that vanishes somewhere is not a counterexample: the required condition is nowhere-zero, not merely nonzero as an element of the [[fiber-bundles/module-of-smooth-sections|section module]].

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: Euler classes, zero sections, and the obstruction interpretation.
2. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-4008-0). Relevant: sphere bundles, cross-sections, and obstruction theory for vector bundles.
