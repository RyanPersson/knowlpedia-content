+++
id = "lie-groups/complex-lie-algebra-sl3"
title = "Complex Lie algebra sl3(C)"
kind = "knowl"
summary = "The eight-dimensional simple complex Lie algebra of rank 2 and Dynkin type A2."
aliases = ["complex-lie-algebra-sl3", "sl3(C)", "sl(3,C)", "complex Lie algebra sl3"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

The **complex Lie algebra** \(\mathfrak{sl}_3(\mathbb C)\) is the algebra of trace-zero \(3\times3\) complex matrices with commutator bracket. It is [[lie-groups/simple-lie-algebra|simple]], has complex dimension \(8\), rank \(2\), and [[lie-groups/dynkin-diagram|Dynkin type]] \(A_2\).

Its defining module is \(\mathbf 3=\mathbb C^3\). The other nontrivial [[lie-groups/fundamental-representation|fundamental representation]] is the dual \(\mathbf{\bar 3}=(\mathbb C^3)^*\), and the adjoint representation is the eight-dimensional summand in
\[
\mathbf 3\otimes\mathbf{\bar 3}\cong \mathbf 1\oplus\mathbf 8.
\]

## Roots and weights

For the [[lie-groups/cartan-subalgebra|Cartan subalgebra]] of diagonal trace-zero matrices, write \(\varepsilon_i\) for the \(i\)-th diagonal coordinate. The roots are
\[
\varepsilon_i-\varepsilon_j\qquad(i\ne j),
\]
and one may take \(\varepsilon_1-\varepsilon_2\) and \(\varepsilon_2-\varepsilon_3\) as [[lie-groups/simple-root|simple roots]]. The corresponding Dynkin diagram has two nodes joined by one edge.

The tensor products \(\mathbf3\otimes\mathbf3\cong\mathbf6\oplus\mathbf{\bar3}\) and \(\mathbf3\otimes\mathbf{\bar3}\cong\mathbf1\oplus\mathbf8\) are frequently used to recognize \(A_2\)-modules.

## Groups and real forms

The [[lie-groups/simply-connected-lie-group|simply connected]] complex group is \(SL(3,\mathbb C)\), with center \(\mu_3\); its adjoint form is \(PSL(3,\mathbb C)\). The [[lie-groups/compact-real-form|compact real form]] integrates to \(SU(3)\), while \(SL(3,\mathbb R)\) is the split real form. Thus a paper that writes \(\mathfrak{sl}_3\) over \(\mathbb C\) is not automatically referring to the compact group \(SU(3)\), even though their representation theories are closely related by complexification.

## Paper context

In the three-generation construction, one copy is the color factor in the complexified Standard Model algebra \(\mathbb C\oplus\mathfrak{sl}_2\oplus\mathfrak{sl}_3\), while a commuting copy \(\mathfrak{sl}_3^{\mathrm{gen}}\) relates the three generation subspaces. In the exceptional-Jordan-algebra construction, the compact group \(SU(3)\) is the [[algebra-groups/automorphism-group|automorphism group]] of the octonions that fixes a chosen complex subalgebra; its defining \(\mathbb C^3\) module appears in \(\mathbb O\cong\mathbb C\oplus\mathbb C^3\).

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, Sections 8--13. [Publisher record](https://doi.org/10.1007/978-1-4612-6398-2).
2. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, Sections 12--13. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
3. John C. Baez and Paul Schwahn, *The Standard Model Gauge Group from the Exceptional Jordan Algebra*, 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
4. John C. Baez, *Three Generations in E7*, 2026. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
