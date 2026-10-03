+++
id = "algebra-fields-galois/minkowski-embedding"
title = "Minkowski embedding of a number field"
kind = "construction"
summary = "The simultaneous Archimedean embedding takes the ring of integers to a full Euclidean lattice."
aliases = []
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/archimedean-algebra", "algebra-fields-galois/integral-basis", "linear-algebra/euclidean-lattice"]
+++

For a number field \(K\) with real embeddings \(\sigma_j\) and one representative \(\tau_j\) from each complex-conjugate pair, the **Minkowski embedding** into its [[algebra-fields-galois/archimedean-algebra|Archimedean algebra]] is
\[
\iota:K\longrightarrow K_\infty=\mathbb R^{r_1}\times\mathbb C^{r_2},\qquad
\iota(a)=(\sigma_1(a),\ldots,\sigma_{r_1}(a),\tau_1(a),\ldots,\tau_{r_2}(a)).
\]
It is an injective \(\mathbb Q\)-algebra map. The image \(\iota(\mathcal O_K)\) is a full lattice of real rank \([K:\mathbb Q]\).

## Integral lattice and convention

An integral basis of \(\mathcal O_K\) maps to a real basis of \(K_\infty\), so its integer span is a full lattice. For \(K=\mathbb Q(i)\) it is \(\mathbb Z[i]\subseteq\mathbb C\).

Some metric conventions rescale the two real coordinates of each complex place by \(\sqrt2\). The algebra embedding here uses the complex coordinates without that rescaling, so multiplication remains coordinatewise.

## References

1. J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, 2020. Chapter 4, lattices and the Archimedean embedding.
