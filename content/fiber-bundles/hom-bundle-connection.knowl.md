+++
id = "fiber-bundles/hom-bundle-connection"
title = "Connection on a Hom bundle"
kind = "definition"
summary = "The connection on a homomorphism bundle induced by connections on its source and target bundles."
aliases = ["induced connection on Hom(E,F)", "endomorphism-bundle connection"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/vector-field", "fiber-bundles/tensor-product-connection", "fiber-bundles/dual-connection"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(E,F\to M\) be smooth real or complex [[fiber-bundles/vector-bundle|vector bundles]] with [[fiber-bundles/connection-on-a-vector-bundle|connections]] \(\nabla^E\) and \(\nabla^F\). The **induced connection on \(\operatorname{Hom}(E,F)\)** is the unique connection satisfying
\[
(\nabla^{\operatorname{Hom}}_X T)(s)
=
\nabla^F_X(Ts)-T(\nabla^E_Xs)
\]
for every [[fiber-bundles/vector-field|vector field]] \(X\), section \(T\) of \(\operatorname{Hom}(E,F)\), and section \(s\) of \(E\). Under the canonical identification \(\operatorname{Hom}(E,F)\cong E^*\otimes F\), it is the [[fiber-bundles/tensor-product-connection|tensor product connection]] formed from the [[fiber-bundles/dual-connection|dual connection]] on \(E^*\) and \(\nabla^F\).

## Curvature formula

The [[fiber-bundles/curvature-of-a-vector-bundle-connection|curvature]] of the induced connection obeys the following formula. With the convention
\[
R^\nabla(X,Y)
=
[\nabla_X,\nabla_Y]-\nabla_{[X,Y]},
\]
the induced curvature is
\[
R^{\operatorname{Hom}}(X,Y)T
=
R^F(X,Y)\circ T-T\circ R^E(X,Y).
\]
In particular, on \(\operatorname{End}(E)\) one has \(R^{\operatorname{End}}(X,Y)T=[R^E(X,Y),T]\). This commutator formula is the reason curvature naturally acts on endomorphism-valued tensors.

## Local expression and parallel maps

Choose local frames in which \(\nabla^E=d+A^E\) and \(\nabla^F=d+A^F\). A homomorphism field is then a matrix-valued function \(T\), and
\[
\nabla^{\operatorname{Hom}}T
=
dT+A^F T-TA^E.
\]
Consequently \(T\) is parallel exactly when it intertwines the two covariant derivatives. A parallel [[fiber-bundles/bundle-isomorphism|bundle isomorphism]] identifies both connections and conjugates their curvatures. If \(F\) is the trivial [[fiber-bundles/line-bundle|line bundle]] with its trivial connection, the construction recovers the dual connection on \(E^*\).

## Conventions and scope

The notation \(\operatorname{End}(E)\) means \(\operatorname{Hom}(E,E)\); no metric is needed. A [[fiber-bundles/hermitian-metric|Hermitian metric]] can identify \(E^*\) with a conjugate-dual bundle, but that identification is additional data and does not alter the defining formula.

**Warning.** Switching to the opposite curvature convention reverses every displayed curvature operator but leaves the difference \(R^F\circ T-T\circ R^E\) in the corresponding convention. The commutator is an ordinary, not graded, commutator because \(T\) has degree zero.

## References

1. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume I, Wiley Classics, 1996. [Publisher record](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/mathematics-16ma/geometry-topology-16ma6/foundations-of-differential-geometry-volume-1-978-0-471-15733-5). Relevant: Chapter II, induced connections on associated tensor bundles.
2. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [DOI record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: Appendix A, connections and curvature on tensor bundles.
