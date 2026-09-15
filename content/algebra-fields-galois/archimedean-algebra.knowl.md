+++
id = "algebra-fields-galois/archimedean-algebra"
title = "Archimedean algebra of a number field"
kind = "construction"
summary = "The real algebra formed from all real embeddings and one embedding from each complex-conjugate pair."
aliases = ["K infinity"]
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/number-field", "algebra-fields-galois/field-embedding"]
+++

Let \(K/\mathbb Q\) be a [[algebra-fields-galois/number-field|number field]] of degree \(m=r_1+2r_2\), with real embeddings \(\sigma_1,\ldots,\sigma_{r_1}\) and representatives \(\tau_1,\ldots,\tau_{r_2}\) of the complex-conjugate pairs. Its **Archimedean algebra** is
\[
K_\infty=\mathbb R^{r_1}\times\mathbb C^{r_2}\cong K\otimes_{\mathbb Q}\mathbb R.
\]
The [[algebra-fields-galois/minkowski-embedding|Minkowski embedding]] is \(\iota(a)=(\sigma_1(a),\ldots,\sigma_{r_1}(a),\tau_1(a),\ldots,\tau_{r_2}(a))\), with coordinatewise algebra operations.

## Integral lattice

An integral basis of \(\mathcal O_K\) maps to a real basis of \(K_\infty\). Consequently \(\iota(\mathcal O_K)\) is a full lattice of real rank \(m\). Some metric conventions rescale complex coordinates by \(\sqrt2\); that rescaling is not used in this algebra embedding.

## Examples

For \(K=\mathbb Q\), this is \(\mathbb R\) with lattice \(\mathbb Z\). For \(K=\mathbb Q(i)\), it is \(\mathbb C\) with lattice \(\mathbb Z[i]\). For a real quadratic field, it is \(\mathbb R^2\), using both real embeddings.

## References

1. J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, 2020. Chapter 4, lattices and the embedding used in the finiteness theorem.
