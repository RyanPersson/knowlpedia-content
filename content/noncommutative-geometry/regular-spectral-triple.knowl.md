+++
id = "noncommutative-geometry/regular-spectral-triple"
title = "Regular spectral triple"
kind = "definition"
summary = "A spectral triple whose algebra and Dirac commutators are smooth for every iterated commutator with the absolute Dirac operator."
aliases = ["QC-infinity spectral triple", "smooth spectral triple"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["noncommutative-geometry/spectral-triple", "functional-analysis/bounded-commutator", "noncommutative-geometry/smooth-domain-delta"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A [[noncommutative-geometry/spectral-triple|spectral triple]] \((\mathcal A,H,D)\) is **regular** if
\[
\mathcal A+[D,\mathcal A]\subseteq
\operatorname{Dom}\delta^\infty,
\qquad
\delta(T)=[|D|,T].
\]
Here \(\mathcal A+[D,\mathcal A]\) denotes the linear span of represented
operators \(a\) and [[functional-analysis/bounded-commutator|bounded commutators]] \([D,b]\), and
\(\operatorname{Dom}\delta^\infty\) is the
[[noncommutative-geometry/smooth-domain-delta|smooth domain of the Dirac derivation]].
Equivalently, for every \(a\in\mathcal A\), all iterated commutators
\(\delta^k(a)\) and \(\delta^k([D,a])\) extend to bounded operators for every
integer \(k\geq1\). Regularity is an additional differentiability axiom; it
does not follow from the bounded first-commutator axiom of a spectral triple.

## Analytic consequences

Regularity supports a filtered algebra of abstract differential and
pseudodifferential operators. In that calculus, repeated commutators with
\(|D|\) behave like derivatives, while operators in
\(\operatorname{Dom}\delta^\infty\) behave like order-zero coefficients. With
separate summability and meromorphic-continuation hypotheses, this machinery
leads to residues of zeta functions and the local index formula.

## Standard example

For the canonical spin spectral triple of a closed Riemannian spin manifold,
smooth functions and their commutators with the [[noncommutative-geometry/dirac-operator|Dirac operator]] remain bounded
under all iterated commutators with \(|D|\). This follows from the classical
pseudodifferential calculus. By contrast, merely completing the smooth
function algebra in the [[linear-algebra/operator-norm|operator norm]] generally introduces nonsmooth
functions and destroys this all-orders condition.

## Conventions and scope

**Warning.** “Regular” here means \(QC^\infty\), not regularity of an
unbounded operator in the Hilbert-module sense. Some sources use
\(\langle D\rangle=(1+D^2)^{1/2}\) in place of \(|D|\). Those formulations
agree in standard compact settings under appropriate estimates, but the
equivalence should not be assumed in every generalized spectral-triple
framework.

## References

1. A. Connes and H. Moscovici, “The Local Index Formula in Noncommutative Geometry,” *Geometric and Functional Analysis* 5 (1995), 174–243. [DOI record](https://doi.org/10.1007/BF01895667). Relevant: §II, regularity and the pseudodifferential calculus.
2. N. Higson, “The Local Index Formula in Noncommutative Geometry,” in *Contemporary Developments in Algebraic K-Theory*, ICTP Lecture Notes 15, 2004. [Author-hosted manuscript](https://nigel.higson.ca/uploads/1/2/1/4/121496570/higson_-_2004_-_the_local_index_formula_in_noncommutative_geometry.pdf). Relevant: smoothness hypotheses and the differential-operator approach.
