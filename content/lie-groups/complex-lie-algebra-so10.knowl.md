+++
id = "lie-groups/complex-lie-algebra-so10"
title = "Complex Lie algebra so10(C)"
kind = "knowl"
summary = "The 45-dimensional simple complex orthogonal Lie algebra of rank 5 and Dynkin type D5."
aliases = ["complex-lie-algebra-so10", "so10(C)", "so(10,C)", "complex Lie algebra so10"]
domains = ["lie-groups"]
prerequisites = ["linear-algebra/bilinear-form", "lie-groups/lie-algebra", "lie-groups/simple-lie-algebra", "lie-groups/dynkin-diagram", "lie-groups/half-spin-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

The **complex Lie algebra** \(\mathfrak{so}_{10}(\mathbb C)\) consists of endomorphisms preserving a nondegenerate symmetric [[linear-algebra/bilinear-form|bilinear form]] infinitesimally:
\[
\mathfrak{so}_{10}(\mathbb C)=\{X\in M_{10}(\mathbb C):X^{\mathsf T}+X=0\}
\]
after choosing the standard form. It is [[lie-groups/simple-lie-algebra|simple]], of complex dimension \(45\), rank \(5\), and [[lie-groups/dynkin-diagram|Dynkin type]] \(D_5\).

Its distinguished irreducible modules include the vector module \(\mathbf{10}\), the two inequivalent [[lie-groups/half-spin-representation|half-spin modules]] \(\mathbf{16}_+\) and \(\mathbf{16}_-\), and the adjoint module \(\mathbf{45}\cong\Lambda^2\mathbf{10}\).

## Spin representations and global groups

The half-spin modules are representations of the [[lie-groups/spin-group|spin group]] \(\operatorname{Spin}(10,\mathbb C)\), the [[lie-groups/simply-connected-lie-group|simply connected]] complex group with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak{so}_{10}(\mathbb C)\). They do not descend to the ordinary matrix group \(SO(10,\mathbb C)\). Thus the notation “\(SO(10)\) grand unified theory” commonly refers globally to \(\operatorname{Spin}(10)\) when a \(\mathbf{16}\) of fermions is present.

The [[lie-groups/compact-real-form|compact real form]] integrates to compact \(\operatorname{Spin}(10)\); the split real form is \(\mathfrak{so}(5,5)\). Other real forms, such as \(\mathfrak{so}(p,10-p)\), have the same complexification but different real-group representation theory.

## Role in the E-series chain

The regular inclusion
\[
\mathfrak{sl}_5\subset\mathfrak{so}_{10}
\]
is followed by the inclusion of \(\mathfrak{so}_{10}\) in the [[lie-groups/exceptional-lie-algebra-e6|exceptional Lie algebra \(\mathfrak e_6\)]]. Under \(\mathfrak{so}_{10}\oplus\mathbb C\), the adjoint representation of \(\mathfrak e_6\) branches, up to a choice of charge sign, as
\[
\mathbf{78}\cong\mathbf{45}_0\oplus\mathbf1_0
\oplus\mathbf{16}_{3}\oplus\mathbf{16}^{*}_{-3}.
\]
This places \(\mathfrak{so}_{10}\) at the \(E_5\) stage of the [[lie-groups/en-series-of-lie-algebras|\(E_n\) series]] used in the three-generation construction.

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4--6*, Springer, 2002, Plate IV. [Publisher record](https://doi.org/10.1007/978-3-540-89394-3).
2. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, Sections 19--20. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
3. John C. Baez and John Huerta, *The Algebra of Grand Unified Theories*, *Bulletin of the American Mathematical Society* 47 (2010), 483--552. [DOI](https://doi.org/10.1090/S0273-0979-10-01294-2).
4. John C. Baez, *Three Generations in E7*, 2026. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
