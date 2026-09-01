+++
id = "operator-algebras/brown-green-rieffel-stabilization-theorem"
title = "Brown–Green–Rieffel stabilization theorem"
kind = "theorem"
summary = "For sigma-unital C-star algebras, strong Morita equivalence is equivalent to stable isomorphism."
aliases = ["stable isomorphism and strong Morita equivalence"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/approximate-identity", "operator-algebras/compact-operator-cstar-algebra", "linear-algebra/hilbert-space", "operator-algebras/strong-morita-equivalence", "linear-algebra/compact-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) and \(B\) be \(\sigma\)-unital \(C^*\)-algebras, equivalently \(C^*\)-algebras admitting countable [[operator-algebras/approximate-identity|approximate identities]], and let \(\mathcal K\) be the [[operator-algebras/compact-operator-cstar-algebra|\(C^*\)-algebra of compact operators]] on a separable infinite-dimensional [[linear-algebra/hilbert-space|Hilbert space]]. The **Brown–Green–Rieffel stabilization theorem** states that \(A\) and \(B\) are [[operator-algebras/strong-morita-equivalence|strongly Morita equivalent]] if and only if
\[
A\otimes_{\min}\mathcal K\cong B\otimes_{\min}\mathcal K
\]
as \(C^*\)-algebras. Thus, under the countability hypothesis, Morita equivalence becomes ordinary \(*\)-isomorphism after stabilization by [[linear-algebra/compact-operator|compact operators]].

## Mechanism of the theorem

An [[operator-algebras/imprimitivity-bimodule|imprimitivity bimodule]] places
\(A\) and \(B\) as complementary full corners of its
[[operator-algebras/linking-algebra|linking algebra]]. After tensoring with
\(\mathcal K\), the
\(\sigma\)-unitality hypothesis supplies enough countable matrix units to
identify these full corners with the stabilized linking algebra. Conversely,
isomorphic stabilizations are Morita equivalent, and each algebra is Morita
equivalent to its stabilization.

## Consequences and examples

The theorem turns many Morita-invariant questions into isomorphism questions
for stable algebras. For example, \(M_n(A)\) and \(A\) have isomorphic
stabilizations and are strongly Morita equivalent. Likewise,
\(\mathcal K(H)\) is strongly Morita equivalent to \(\mathbb C\) for
separable infinite-dimensional \(H\), since
\(\mathcal K(H)\otimes\mathcal K\cong\mathcal K\).

## Hypotheses and limitations

**Warning.** The theorem requires [[operator-algebras/sigma-unital-cstar-algebra|countable approximate identities]] for both
algebras. Brown, Green, and Rieffel exhibit failure without this hypothesis,
so stable isomorphism and strong Morita equivalence are not unconditionally
interchangeable. The tensor product here is the
[[operator-algebras/minimal-cstar-tensor-product|minimal \(C^*\)-tensor product]]; because \(\mathcal K\) is nuclear, no tensor-norm ambiguity remains.

## References

1. Lawrence G. Brown, Philip Green, and Marc A. Rieffel, “Stable Isomorphism and Strong Morita Equivalence of \(C^*\)-Algebras,” *Pacific Journal of Mathematics* 71 (1977), 349–363. [DOI record](https://doi.org/10.2140/pjm.1977.71.349). Relevant: the main stabilization theorem and the counterexamples without countable approximate identities.
2. Iain Raeburn and Dana P. Williams, *Morita Equivalence and Continuous-Trace \(C^*\)-Algebras*, Mathematical Surveys and Monographs 60, American Mathematical Society, 1998. [DOI record](https://doi.org/10.1090/surv/060). Relevant: Chapter 3 on imprimitivity bimodules, linking algebras, and stabilization.
