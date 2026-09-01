+++
id = "operator-algebras/kasparov-stabilization-theorem"
title = "Kasparov stabilization theorem"
kind = "theorem"
summary = "A countably generated Hilbert C-star module is absorbed by the standard Hilbert module."
aliases = ["stabilization theorem for Hilbert C*-modules"]
domains = ["operator-algebras", "noncommutative-geometry"]
prerequisites = ["operator-algebras/countably-generated-hilbert-cstar-module", "operator-algebras/standard-hilbert-cstar-module", "operator-algebras/adjointable-operator-hilbert-module"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be a \(C^*\)-algebra, let \(E\) be a
[[operator-algebras/countably-generated-hilbert-cstar-module|countably
generated Hilbert \(A\)-module]], and let
\(H_A=\ell^2(A)\) be the
[[operator-algebras/standard-hilbert-cstar-module|standard Hilbert
\(A\)-module]]. The **Kasparov stabilization theorem** states that there is a
unitary Hilbert-module isomorphism
\[
E\oplus H_A\cong H_A.
\]
Here unitary means an adjointable \(A\)-linear map whose adjoint is its
inverse, in the sense of an
[[operator-algebras/adjointable-operator-hilbert-module|adjointable
operator]]. In particular, \(E\) is isomorphic to an orthogonally complemented
submodule of \(H_A\). No unitality assumption on \(A\) is required; the
countable-generation hypothesis on \(E\) is essential.

## Equivalent complemented form

From a unitary \(U:E\oplus H_A\to H_A\), the image \(U(E\oplus0)\) is the
range of an adjointable projection \(P\) on \(H_A\), while
\((1-P)H_A\cong H_A\). Conversely, any adjointable projection with
\(PH_A\cong E\) and \((1-P)H_A\cong H_A\) yields the displayed absorption
isomorphism. In particular, the theorem implies the frequently used weaker
form that every countably generated Hilbert \(A\)-module embeds as an
orthogonally complemented submodule of \(H_A\).

## Proof mechanism

One chooses a countable generating sequence for \(E\), rescales it so that
the associated coordinate operators are bounded, and constructs an
adjointable operator from \(H_A\) with dense range in \(E\). A sequence of
operator rotations then turns this approximate spanning data into a unitary
between \(E\oplus H_A\) and \(H_A\). The construction replaces the
orthonormal-basis argument unavailable for general Hilbert \(C^*\)-modules.

## Consequences

Stabilization lets one represent [[operator-algebras/countably-generated-hilbert-cstar-module|countably generated Hilbert modules]] by
adjointable projections on a single standard module. It is therefore a basic
tool for [[operator-algebras/compact-operator-hilbert-module|compact module
operators]], Morita equivalence, and Kasparov's \(KK\)-theory. The theorem
does not extend to arbitrary, possibly uncountably generated [[operator-algebras/hilbert-cstar-module|Hilbert modules]]
without additional hypotheses.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [Publisher record](https://doi.org/10.1017/CBO9780511526206). Relevant: Theorem 6.2 and its proof.
2. G. G. Kasparov, “Hilbert \(C^*\)-modules: Theorems of Stinespring and Voiculescu,” *Journal of Operator Theory* **4** (1980), 133–150. [Journal record](https://jot.theta.ro/jot/archive/1980-004-001/1980-004-001-007.html). Relevant: the stabilization theorem for countably generated modules.
