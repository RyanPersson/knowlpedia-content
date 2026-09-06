+++
id = "lie-groups/exceptional-lie-algebra-g2"
title = "Exceptional Lie algebra g2"
kind = "knowl"
summary = "The 14-dimensional simple complex Lie algebra of rank 2 and exceptional Dynkin type G2."
aliases = ["exceptional-lie-algebra-g2", "g2", "complex Lie algebra g2", "exceptional Lie algebra G2"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/simple-lie-algebra", "lie-groups/root-system", "algebra-representation-theory/irreducible-representation"]
dependency_review_count = 1
section_mode = "progressive"
+++

The **exceptional complex Lie algebra** \(\mathfrak g_2\) is the unique [[lie-groups/simple-lie-algebra|simple complex Lie algebra]] whose [[lie-groups/root-system|root system]] has Dynkin type \(G_2\). It has complex dimension \(14\), rank \(2\), and \(12\) roots, with squared-length ratio \(3\) between long and short roots.

Its smallest nontrivial [[algebra-representation-theory/irreducible-representation|irreducible representation]] is the \(7\)-dimensional fundamental module \(\mathbf7\). Its adjoint representation is \(\mathbf{14}\), and
\[
\Lambda^2\mathbf7\cong\mathbf7\oplus\mathbf{14}.
\]

## Octonionic realization

For the complexified [[nonassociative-algebra/octonion-algebra|octonion algebra]] \(\mathbb O_{\mathbb C}\),
\[
\mathfrak g_2\cong\operatorname{Der}(\mathbb O_{\mathbb C}).
\]
Derivations kill the identity and act irreducibly on the seven-dimensional imaginary, or trace-zero, subspace. This is the module \(\mathbf7\). Equivalently, \(G_2\) is characterized inside \(GL(7,\mathbb C)\) as the stabilizer of the generic alternating three-form induced by octonion multiplication.

## Groups and real forms

The [[lie-groups/simply-connected-lie-group|simply connected]] and adjoint complex groups of type \(G_2\) coincide and have trivial center. The [[algebra-groups/automorphism-group|automorphism group]] of the real division octonions is the [[lie-groups/compact-exceptional-lie-group-g2|compact exceptional group \(G_2\)]]. The split octonions instead yield the split real form \(G_{2(2)}\).

## Paper context

Compact \(G_2=\operatorname{Aut}(\mathbb O)\) acts on the choices of complex subalgebra \(\mathbb C\subset\mathbb O\). The stabilizer of a chosen imaginary unit is isomorphic to \(SU(3)\), and under it
\[
\mathbb O\cong\mathbb C\oplus\mathbb C^3
\]
as real vector spaces equipped with compatible complex structure. This supplies the \(SU(3)\)-invariant [[linear-algebra/inner-product|inner product]] and conjugated cross product used in the exceptional-Jordan-algebra construction of octonion multiplication.

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4--6*, Springer, 2002, Plate IX. [Publisher record](https://doi.org/10.1007/978-3-540-89394-3).
2. John C. Baez, "The Octonions," *Bulletin of the American Mathematical Society* 39 (2002), 145--205. [DOI](https://doi.org/10.1090/S0273-0979-01-00934-X).
3. John Frank Adams, *Lectures on Exceptional Lie Groups*, University of Chicago Press, 1996, Chapters 3--5. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/L/bo3683975.html).
4. John C. Baez and Paul Schwahn, *The Standard Model Gauge Group from the Exceptional Jordan Algebra*, 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
