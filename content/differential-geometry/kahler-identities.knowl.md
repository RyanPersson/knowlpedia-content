+++
id = "differential-geometry/kahler-identities"
title = "Kähler identities"
kind = "theorem"
summary = "Commutator formulas relating the Dolbeault operators, their formal adjoints, and the Lefschetz operators of a Kähler metric."
aliases = ["commutator identities in Kähler geometry"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/kahler-manifold", "differential-geometry/formal-adjoint-differential-operator", "differential-geometry/dolbeault-operators"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \((X,\omega)\) be a [[differential-geometry/kahler-manifold|Kähler manifold]]. Define \(L\alpha=\omega\wedge\alpha\), let \(\Lambda=L^*\), and let \(\partial^*,\bar\partial^*\) be the [[differential-geometry/formal-adjoint-differential-operator|formal adjoints]] of the [[differential-geometry/dolbeault-operators|Dolbeault operators]]. With the Hermitian and commutator conventions used here, the **Kähler identities** are
\[
[\bar\partial^*,L]=i\partial,\qquad
[\partial^*,L]=-i\bar\partial,
\]
\[
[\Lambda,\bar\partial]=-i\partial^*,\qquad
[\Lambda,\partial]=i\bar\partial^*.
\]
Here \([A,B]=AB-BA\), since \(L\) and \(\Lambda\) have even total degree. The identities depend on the normalization of \(\omega\) and the adjoint conventions.

## Structure and consequences

The identities imply that the Dolbeault Laplacians agree:
\[
\Delta_\partial=\Delta_{\bar\partial},
\]
and that the de Rham [[differential-geometry/hodge-laplacian|Hodge Laplacian]] satisfies
\[
\Delta_d=2\Delta_\partial=2\Delta_{\bar\partial}.
\]
They also force the mixed commutators \([\partial,\bar\partial^*]\) and \([\bar\partial,\partial^*]\) to vanish.

## Geometric role

Because \(\Delta_d\) preserves bidegree, a harmonic complex-valued \(k\)-form splits into harmonic \((p,q)\)-components. On compact Kähler manifolds, Hodge theory then yields the Hodge decomposition of de Rham cohomology and Hodge symmetry. The identities are therefore the analytic mechanism connecting de Rham, Dolbeault, and Lefschetz theory.

## Conventions and scope

**Warning.** On a general [[differential-geometry/hermitian-manifold|Hermitian manifold]], torsion terms appear in these commutators; the four displayed formulas use the Kähler condition \(d\omega=0\). Signs can also reverse if the [[differential-geometry/fundamental-form-almost-hermitian|fundamental form]] or commutator is defined oppositely.

## References

1. Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, 2012. [Author-hosted text](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf). Relevant: Chapter VI, §6.1, especially Theorem 6.4 and Corollary 6.5; §6.2 for the non-Kähler correction terms.
2. Raymond O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [Publisher record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter V, §1, differential operators on a Kähler manifold.
