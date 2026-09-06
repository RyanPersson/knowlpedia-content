+++
id = "operator-algebras/conditional-expectation-reduced-crossed-product"
title = "Canonical conditional expectation on a reduced crossed product"
kind = "definition"
summary = "For a discrete-group action, the faithful conditional expectation that extracts the identity Fourier coefficient from the reduced crossed product."
aliases = ["Fourier coefficient expectation", "crossed-product expectation"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/reduced-crossed-product", "operator-algebras/conditional-expectation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let a discrete group \(G\) act by automorphisms \(\alpha\) on a
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\). The **canonical
conditional expectation on the [[operator-algebras/reduced-crossed-product|reduced crossed product]]** is the map
\[
E_A:A\rtimes_{\alpha,r}G\longrightarrow A,\qquad
E_A\!\left(\sum_{s\in F}a_su_s\right)=a_e
\]
on finite Fourier sums, extended continuously. It is a contractive positive
\(A\)-bimodule projection fixing \(A\), hence a
[[operator-algebras/conditional-expectation|conditional expectation]].
Moreover, it is faithful: \(E_A(x^*x)=0\) implies \(x=0\). The discreteness
hypothesis ensures that \(A\) is the degree-\(e\) coefficient algebra inside
the crossed product.

## Fourier coefficients

For \(x\in A\rtimes_{\alpha,r}G\), its \(s\)-th Fourier coefficient is
\[
\widehat{x}(s)=E_A(xu_s^*).
\]
These coefficients recover the expected values on finite sums and are
compatible with left and right multiplication by \(A\). Faithfulness makes
\(E_A\) particularly useful: positivity questions can often be tested after
forming \(x^*x\) and extracting its identity coefficient. The construction is
canonical, so it does not depend on a choice of faithful representation used
to realize the [[operator-algebras/reduced-crossed-product|reduced crossed
product]].

## Example

For the trivial action on \(A=\mathbb C\), the map is the canonical trace on
the [[operator-algebras/reduced-group-cstar-algebra|reduced group
\(C^*\)-algebra]]:
\[
E_{\mathbb C}\!\left(\sum_{s\in F}c_s\lambda_s\right)=c_e.
\]
For a nontrivial action it is usually not tracial, because the coefficient
algebra need not commute with the implementing unitaries. It remains an
\(A\)-bimodule map, which is the relevant replacement for scalar traciality.

## Beyond discrete groups

**Warning.** For a general nondiscrete
[[topology/locally-compact-group|locally compact group]], evaluation at the
identity is not a bounded coefficient-extraction map on the reduced crossed
product. The coefficient algebra also sits naturally in the multiplier
algebra rather than necessarily inside the crossed product. The appropriate
general constructions use [[operator-algebras/operator-valued-weight|operator-valued weights]] or special additional
hypotheses; they should not be called the conditional expectation defined
above without qualification.

## References

1. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/gsm/088). Relevant: §4.1 on reduced crossed products by discrete groups and the canonical expectation.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Chapter 2 on reduced crossed-product constructions.
