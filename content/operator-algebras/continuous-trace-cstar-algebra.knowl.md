+++
id = "operator-algebras/continuous-trace-cstar-algebra"
title = "Continuous-trace C*-algebra"
kind = "definition"
summary = "A C*-algebra whose irreducible-representation traces vary continuously and densely detect its positive elements."
aliases = ["continuous trace algebra", "CT C*-algebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] with
Hausdorff spectrum \(\widehat A\) of unitary-equivalence classes of
[[operator-algebras/irreducible-cstar-representation|irreducible
representations]]. For \(a\in A_+\), define
\[
\widehat a([\pi])=\operatorname{Tr}(\pi(a)).
\]
The element \(a\) has **continuous trace** when this function is finite and
continuous on \(\widehat A\). The algebra \(A\) is a **continuous-trace
\(C^*\)-algebra** when its continuous-trace positive elements are dense in
\(A_+\). Continuity uses the
[[operator-algebras/operator-trace|canonical operator trace]] in each
[[algebra-representation-theory/irreducible-representation|irreducible representation]], while density makes such elements detect the
whole algebra. This is a property of \(A\), not one representation.

## Local compact-operator structure

Continuous-trace algebras are [[operator-algebras/type-i-cstar-algebra|type I]] and, locally over their spectrum, are strongly Morita equivalent to commutative algebras \(C_0(U)\). Under the usual separability and paracompactness hypotheses, their stabilizations are section algebras of locally trivial bundles of [[operator-algebras/compact-operator-cstar-algebra|compact-operator algebras]]. This is the geometric form developed in [Raeburn–Williams, Chapters 4–5].

Consequently a continuous-trace algebra is a particularly regular [[operator-algebras/continuous-field-cstar-algebra|continuous field of \(C^*\)-algebras]]. Its fibers in irreducible representations are [[linear-algebra/compact-operator|compact operators]] rather than arbitrary type I algebras.

## Morita invariance

The continuous-trace property is preserved by [[operator-algebras/strong-morita-equivalence|strong Morita equivalence]]. The spectrum is carried along by the Rieffel correspondence, while the local compact-operator models are unchanged up to stabilization [Raeburn–Williams, Chapters 3–5]. This makes continuous-trace algebras natural noncommutative analogues of spaces equipped with a twisting class.

## Examples and non-examples

For a locally compact [[topology/hausdorff-space|Hausdorff space]] \(X\), both \(C_0(X)\) and \(C_0(X,\mathcal K(H))\) have continuous trace. The latter has spectrum \(X\), and positive finite-rank sections supply a dense family of continuous-trace elements.

If \(H\) is infinite-dimensional, \(B(H)\) does not have continuous trace. Its positive trace-class operators are not norm-dense in \(B(H)_+\); equivalently, its identity has infinite trace and cannot be approximated in norm by compact finite-trace elements.

## References

1. I. Raeburn and D. P. Williams, *Morita Equivalence and Continuous-Trace \(C^*\)-Algebras*, Mathematical Surveys and Monographs 60, American Mathematical Society, 1998. [DOI record](https://doi.org/10.1090/surv/060). Relevant: Chapters 4–5 on continuous trace, local compact-operator models, and Morita invariance.
2. J. Dixmier, *\(C^*\)-Algebras*, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapter 10 on continuous fields and continuous-trace algebras.
