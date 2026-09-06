+++
id = "complex-analysis/riemann-mapping-theorem"
title = "Riemann mapping theorem"
kind = "theorem"
summary = "Every nonempty proper simply connected plane domain is biholomorphic to the unit disc."
aliases = ["Riemann mapping theorem for plane domains"]
domains = ["complex-analysis", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["topology/simply-connected-space", "complex-analysis/complex-domain", "differential-geometry/biholomorphism", "complex-analysis/normal-family"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

If \(D\subsetneq\mathbb C\) is a nonempty [[topology/simply-connected-space|simply connected]] [[complex-analysis/complex-domain|domain]], then there is a [[differential-geometry/biholomorphism|biholomorphism]]
\[
f:D\longrightarrow\mathbb D,
\qquad
\mathbb D=\{z\in\mathbb C:|z|<1\}.
\]

## Normalization and uniqueness

Given \(a\in D\), there is a unique such map satisfying
\[
f(a)=0,\qquad f'(a)>0.
\]
Without normalization, two Riemann maps differ by a holomorphic automorphism of the disc.

## Excluded cases and scope

The properness hypothesis excludes \(D=\mathbb C\), which cannot be biholomorphic to the disc by [[complex-analysis/liouville-theorem|Liouville's theorem]]. Simple connectivity is essential: an annulus is not biholomorphic to a disc. The theorem classifies domains as [[differential-geometry/riemann-surface|Riemann surfaces]], not their boundary regularity; extending \(f\) continuously or smoothly to the boundary needs additional hypotheses.

## Proof architecture

Standard proofs use a [[complex-analysis/normal-family|normal family]] of injective holomorphic maps and an extremal derivative argument. The result is a striking bridge from topology to [[differential-geometry/conformal-map|conformal geometry]].

## References

1. John B. Conway, *Functions of One Complex Variable I*, 2nd ed., Springer, 1978. [Publisher record](https://doi.org/10.1007/978-1-4612-6313-5). Relevant: Chapter VI, §3.
