+++
id = "langlands/ramification-of-g-local-system"
title = "Ramification of a G-local system"
kind = "definition"
summary = "The obstruction to extending a G-local system across a puncture as an unramified object in a fixed Betti, de Rham, or etale category."
aliases = ["ramified G-local system"]
domains = ["langlands", "fiber-bundles"]
prerequisites = ["fiber-bundles/local-system", "langlands/g-local-system", "langlands/regular-singular-connection", "langlands/irregular-singular-connection", "langlands/stokes-data", "langlands/tame-ramification", "langlands/wild-ramification"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Fix a Betti, de Rham, or étale category of [[fiber-bundles/local-system|local systems]], and let
\(U=X\setminus D\) be a punctured smooth curve. A
[[langlands/g-local-system|\(G\)-local system]] on \(U\) is **ramified at a
marked point \(x\in D\)** when it does not extend across \(x\) as an
unramified object in that category.

In the Betti category over \(\mathbb C\), extension across \(x\) is
equivalent to trivial local monodromy. For an algebraic flat connection,
extension means extension with no pole. A
[[langlands/regular-singular-connection|regular-singular connection]] may
still have nontrivial monodromy, while an
[[langlands/irregular-singular-connection|irregular-singular connection]]
requires formal type and [[langlands/stokes-data|Stokes data]] in addition to
ordinary monodromy.

In the étale category, ramification is the nontrivial action of inertia.
[[langlands/tame-ramification|Tame ramification]] is trivial on wild inertia;
[[langlands/wild-ramification|wild ramification]] is not.

## Automorphic counterpart

Prescribing a particular ramification condition on the spectral side
corresponds to choosing
[[langlands/level-structure-on-g-bundle|level structure]] together with
equivariance or character conditions on automorphic sheaves.

## References

1. Pierre Deligne, *Équations différentielles à points singuliers réguliers*,
   Lecture Notes in Mathematics 163, Springer, 1970.
   [DOI](https://doi.org/10.1007/BFb0061194).
2. Philip Boalch, “Geometry and braiding of Stokes data; fission and wild
   character varieties,” *Annals of Mathematics* 179 (2014), 301–365.
   [arXiv](https://arxiv.org/abs/1111.6228).
