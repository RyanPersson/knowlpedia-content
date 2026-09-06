+++
id = "fiber-bundles/euler-class-as-zero-section"
title = "Euler class as pullback of the Thom class"
kind = "definition"
summary = "The topological Euler class obtained by pulling a vector bundle's Thom class back along its zero section."
aliases = ["zero-section definition of Euler class", "Euler class via Thom class"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/orientation-of-a-real-vector-bundle", "fiber-bundles/thom-class", "fiber-bundles/zero-section"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi:E\to B\) be an [[fiber-bundles/orientation-of-a-real-vector-bundle|oriented real vector bundle]] of rank \(r\), let \(u_E\in H^r(E,E^\times;\mathbb Z)\) be its [[fiber-bundles/thom-class|Thom class]], and let \(0_E:B\to E\) be the [[fiber-bundles/zero-section|zero section]]. The **Euler class of \(E\)** is
\[
e(E):=0_E^*u_E\in H^r(B;\mathbb Z),
\]
where \(0_E\) is regarded as a map of pairs \((B,\varnothing)\to(E,E^\times)\). This definition applies in every rank and uses only the orientation and topology of \(E\); it is natural under orientation-preserving pullback.

## Zeros of sections

If a [[fiber-bundles/section-of-a-vector-bundle|smooth section]] \(s:B\to E\) is transverse to the zero section, its zero set is a codimension-\(r\) submanifold whose cohomological dual is \(e(E)\), with the induced orientation. This geometric interpretation follows from the Thom construction.

In particular, a [[fiber-bundles/nowhere-vanishing-section|nowhere-zero section]] has empty zero locus and forces \(e(E)=0\). The converse is false in general: vanishing of the primary [[fiber-bundles/euler-class-obstruction-to-nonzero-section|Euler obstruction]] need not produce a nowhere-zero section without additional dimension or obstruction-theoretic hypotheses.

## Relation to other definitions

For an oriented even-rank smooth bundle with a metric connection, the image of this integral class in real cohomology agrees with the [[fiber-bundles/euler-class|Chern–Weil Euler class]] represented by the normalized Pfaffian of the curvature. Thus the zero-section construction supplies the integral topological class, while Chern–Weil theory supplies a differential-form representative of its real image.

For a closed oriented manifold \(B\), the [[fiber-bundles/tangent-bundle|tangent-bundle]] Euler class satisfies
\[
\langle e(TB),[B]\rangle=\chi(B),
\]
the cohomological form of the Poincaré–Hopf theorem.

## Examples and conventions

For the trivial oriented bundle \(B\times\mathbb R^r\) with \(r>0\), a constant nonzero section shows that \(e(E)=0\). For the tangent bundle of the oriented sphere \(S^{2m}\), evaluation on the [[topology/fundamental-class|fundamental class]] gives \(2\), so the Euler class is nonzero. Reversing the orientation of \(E\) changes the sign of \(e(E)\).

**Warning.** A nonorientable bundle requires local coefficients; with \(\mathbb Z/2\)-coefficients the analogous construction yields its top [[fiber-bundles/stiefel-whitney-class|Stiefel–Whitney class]].

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: Chapter 9, Euler classes, Thom classes, and zeros of sections.
2. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter 6, Thom isomorphism and Euler class.
