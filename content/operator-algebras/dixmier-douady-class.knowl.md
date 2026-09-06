+++
id = "operator-algebras/dixmier-douady-class"
title = "Dixmier–Douady class"
kind = "definition"
summary = "The degree-three integral cohomology class measuring the twisting of a continuous-trace C*-algebra over its spectrum."
aliases = ["Dixmier-Douady invariant", "DD class", "Dixmier-Douady class"]
domains = ["operator-algebras", "topology"]
section_mode = "progressive"
prerequisites = ["operator-algebras/continuous-trace-cstar-algebra", "linear-algebra/hilbert-space", "topology/singular-cohomology-group", "functional-analysis/unitary-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\) be a separable
[[operator-algebras/continuous-trace-cstar-algebra|continuous-trace \(C^*\)-algebra]] with spectrum \(X=\widehat A\), and assume \(X\) is
paracompact. For a fixed separable infinite-dimensional [[linear-algebra/hilbert-space|Hilbert space]] \(H\),
the stabilization of \(A\) is locally a field of compact-operator algebras.
Its transition automorphisms define a principal \(PU(H)\)-bundle over
\(X\), whose obstruction class
\[
\delta(A)\in H^3(X;\mathbb Z)
\]
is the **Dixmier–Douady class** of \(A\). Equivalently, it is the image in
[[topology/singular-cohomology-group|degree-three integral cohomology]] of
the Čech cocycle obtained by lifting the projective-unitary transition
functions locally to [[functional-analysis/unitary-operator|unitary operators]].
The class depends on the identification of the spectrum with \(X\).

## Classification and vanishing

Over a fixed second-countable
[[topology/locally-compact-space|locally compact]] [[topology/hausdorff-space|Hausdorff space]] \(X\),
the assignment
\(A\mapsto\delta(A)\) classifies continuous-trace \(C^*\)-algebras up to
[[operator-algebras/strong-morita-equivalence|strong Morita equivalence]]:
two such algebras are Morita equivalent over \(X\) exactly when their
Dixmier–Douady classes agree. Every class in \(H^3(X;\mathbb Z)\) occurs.

The class vanishes exactly when \(A\) is Morita equivalent over \(X\) to
\(C_0(X)\). In the separable stable setting, vanishing says that the
compact-operator bundle is trivial, so the algebra is isomorphic to
\(C_0(X,\mathcal K)\). Thus \(\delta(A)\) measures twisting rather than the
local fiber type, which is already fixed.

## Cocycles and examples

Choose [[fiber-bundles/local-trivialization|local trivializations]] with transition maps
\(g_{ij}:U_i\cap U_j\to PU(H)\), and choose local unitary lifts
\(\widetilde g_{ij}\). On triple overlaps,
\[
\widetilde g_{ij}\widetilde g_{jk}\widetilde g_{ki}
=c_{ijk}1
\]
for circle-valued functions \(c_{ijk}\). Their Čech class in
\(H^2(X;\mathbb T)\), transported by the exponential-sequence connecting
map, is \(\delta(A)\in H^3(X;\mathbb Z)\). Changing lifts changes the
cocycle by a coboundary.

The trivial field \(C_0(X,\mathcal K)\) has class zero. More generally, a
principal \(PU(H)\)-bundle with nonzero class produces a section algebra
that is locally indistinguishable from the trivial compact-operator field
but is not Morita equivalent to \(C_0(X)\) over \(X\). This global
obstruction is the phenomenon isolated in the original
Dixmier–Douady theory.

## Conventions and scope

Some formulations classify stable continuous-trace algebras up to
\(*\)-isomorphism, while others classify arbitrary continuous-trace
algebras up to Morita equivalence. Stability, separability, and
paracompactness determine which version applies. The unqualified class
\(\delta(A)\) should therefore be read together with its spectrum and the
chosen classification setting.

## References

1. Jacques Dixmier and Adrien Douady, “Champs continus d'espaces hilbertiens et de \(C^*\)-algèbres,” *Bulletin de la Société Mathématique de France* 91 (1963), 227–284. [Numdam DOI record and full text](https://doi.org/10.24033/bsmf.1596). Relevant: the obstruction and classification of locally trivial fields of elementary \(C^*\)-algebras.
2. Iain Raeburn and Dana P. Williams, *Morita Equivalence and Continuous-Trace \(C^*\)-Algebras*, Mathematical Surveys and Monographs 60, American Mathematical Society, 1998. [AMS DOI record](https://doi.org/10.1090/surv/060). Relevant: Chapter 5 on the Dixmier–Douady class, Morita classification, and stable classification.
