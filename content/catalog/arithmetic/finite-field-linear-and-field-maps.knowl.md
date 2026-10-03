+++
id = "catalog/arithmetic/finite-field-linear-and-field-maps"
title = "Linear maps and field maps between finite fields"
kind = "theorem"
summary = "Fixed-prime matrix Hom-sets compared with the far smaller field Hom-sets."
aliases = ["finite-field linear versus field homomorphisms"]
domains = ["catalog", "algebra-fields-galois", "linear-algebra"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/finite-field", "linear-algebra/linear-map", "catalog/categories/fields"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

Fix a prime \(p\) and positive integers \(a,b\). Choosing bases of the [[algebra-fields-galois/finite-field|finite fields]] over \(\mathbb F_p\) identifies their [[linear-algebra/linear-map|linear maps]] with rectangular matrices:
\[
\operatorname{Hom}_{\mathbb F_p\text{-Vect}}(\mathbb F_{p^a},\mathbb F_{p^b})
\cong M_{b\times a}(\mathbb F_p).
\]
In the [[catalog/categories/fields|category of fields]], maps preserve addition, multiplication and \(1\): the same pair instead has \(a\) homomorphisms if \(a\mid b\), and none otherwise. The two comparisons use different morphism axioms on the same finite carriers.

## Linear endomorphisms and automorphisms

For \(a=b\), the matrix identification respects addition and composition, so the linear endomorphism ring is \(M_a(\mathbb F_p)\), with \(p^{a^2}\) elements. Its units are \(\mathrm{GL}_a(\mathbb F_p)\), whose cardinality is
\[
\left|\mathrm{GL}_a(\mathbb F_p)\right|
=\prod_{j=0}^{a-1}(p^a-p^j).
\]
Indeed, the first column can be any nonzero vector, and each subsequent column must avoid the span of its predecessors. For a \(b\times a\) matrix there are \(ab\) independent entries, giving \(p^{ab}\) linear maps. The matrix identification depends on the chosen bases.

## Concrete comparisons

| Object | Scalar field | Linear endomorphisms | Linear automorphisms | Field endomorphisms = field automorphisms |
| --- | --- | --- | --- | --- |
| [[catalog/arithmetic/f4|\(\mathbb F_4\)]] | \(\mathbb F_2\) | \(M_2(\mathbb F_2)\), 16 maps | \(\mathrm{GL}_2(\mathbb F_2)\), 6 maps | 2 Frobenius powers |
| [[catalog/arithmetic/f8|\(\mathbb F_8\)]] | \(\mathbb F_2\) | \(M_3(\mathbb F_2)\), 512 maps | \(\mathrm{GL}_3(\mathbb F_2)\), 168 maps | 3 Frobenius powers |
| [[catalog/arithmetic/f9|\(\mathbb F_9\)]] | \(\mathbb F_3\) | \(M_2(\mathbb F_3)\), 81 maps | \(\mathrm{GL}_2(\mathbb F_3)\), 48 maps | 2 Frobenius powers |

For example there are \(2^{3\cdot2}=64\) linear maps from \(\mathbb F_4\) to \(\mathbb F_8\), but no field homomorphisms, since \(2\nmid3\). The zero linear map is one of those 64 maps and never a field homomorphism.

## Why the field-map count is different

A field homomorphism is injective and fixes the prime field. Its image would make \(\mathbb F_{p^b}\) an extension of \(\mathbb F_{p^a}\), forcing \(a\mid b\) by the tower formula. When \(a\mid b\), the target contains a unique subfield of size \(p^a\), and the isomorphisms onto it differ by the \(a\) powers of Frobenius \(x\mapsto x^p\). Thus every endomorphism of a finite field is an automorphism, although most linear endomorphisms are not even injective.

## Fixed scalar categories

The catalogue uses distinct categories \(\mathbb F_2\text{-Vect}\) and \(\mathbb F_3\text{-Vect}\). A symbolic \(\mathbb F_p\text{-Vect}\) comparison requires the same fixed prime \(p\) and the specified prime-field scalar actions at both endpoints. A shared letter standing for an unspecified prime does not create a linear Hom-set across different characteristics.

## References

1. [J. S. Milne, Fields and Galois Theory](https://www.jmilne.org/math/CourseNotes/FT.pdf), Chapter 4, Proposition 4.20, Corollary 4.21 and Proposition 4.23, pp. 53–54.
