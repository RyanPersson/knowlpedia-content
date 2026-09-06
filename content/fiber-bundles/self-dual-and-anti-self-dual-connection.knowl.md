+++
id = "fiber-bundles/self-dual-and-anti-self-dual-connection"
title = "Self-dual and anti-self-dual connection"
kind = "definition"
summary = "A connection on an oriented Riemannian four-manifold whose curvature lies entirely in the self-dual or anti-self-dual summand of two-forms."
aliases = ["self-dual connection", "anti-self-dual connection", "SD connection", "ASD connection"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection", "fiber-bundles/curvature-2-form-of-a-principal-connection", "differential-geometry/hodge-star-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] over an oriented Riemannian four-manifold, and let \(A\) be a [[fiber-bundles/principal-connection|connection]] with [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature]] \(F_A\in\Omega^2(M;\operatorname{ad}P)\). The metric and orientation define a [[differential-geometry/hodge-star-operator|Hodge star]] with \(*^2=1\) on two-forms. The connection is **self-dual** if
\[
*F_A=F_A,
\]
and **anti-self-dual** if
\[
*F_A=-F_A.
\]
Equivalently, \(F_A\) lies in the \(+1\) or \(-1\) eigenbundle of the Hodge star. Reversing the orientation interchanges the two conditions.

## Why these connections are Yang–Mills

The [[fiber-bundles/bianchi-identity|Bianchi identity]] gives \(d_AF_A=0\). If \(*F_A=\pm F_A\), it follows that \(d_A(*F_A)=0\), which is the [[fiber-bundles/yangmills-equation|Yang–Mills equation]] in the convention \(d_A(*F_A)=0\). Thus every self-dual or anti-self-dual connection is a [[fiber-bundles/yangmills-connection|Yang–Mills connection]]. The converse is false: the Yang–Mills equation is second order in the connection, whereas the self-duality equations impose the stronger first-order curvature condition.

## Curvature splitting and examples

The Hodge star splits bundle-valued two-forms orthogonally as
\[
\Omega^2(M;\operatorname{ad}P)
=\Omega^2_+(M;\operatorname{ad}P)\oplus
\Omega^2_-(M;\operatorname{ad}P).
\]
Writing \(F_A=F_A^++F_A^-\), self-duality means \(F_A^-=0\), while anti-self-duality means \(F_A^+=0\). Every [[fiber-bundles/flat-principal-connection|flat connection]] satisfies both equations because \(F_A=0\); a nonflat connection cannot satisfy both.

The basic \(SU(2)\) BPST instanton on \(\mathbb R^4\) gives a nonflat solution of one of the two equations. Whether it is labeled self-dual or anti-self-dual depends on the orientation and curvature conventions.

## Conventions and scope

The four-dimensional hypothesis is essential to this formulation: only in dimension four does the Hodge star carry two-forms to two-forms and square to \(+1\) in Riemannian signature. The equations themselves do not require compactness of \(M\), but finite-action moduli theory normally imposes compactness or decay conditions and uses an \(\operatorname{Ad}\)-invariant [[linear-algebra/inner-product|inner product]] on the [[lie-groups/lie-algebra|Lie algebra]].

## References

1. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [Publisher record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §2.1, self-duality, curvature splitting, and the Yang–Mills functional.
2. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [Publisher record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 2, the self-dual Yang–Mills equations.
