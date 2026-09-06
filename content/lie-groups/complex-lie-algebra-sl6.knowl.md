+++
id = "lie-groups/complex-lie-algebra-sl6"
title = "Complex Lie algebra sl6(C)"
kind = "knowl"
summary = "The 35-dimensional simple complex Lie algebra of rank 5 and Dynkin type A5."
aliases = ["complex-lie-algebra-sl6", "sl6(C)", "sl(6,C)", "complex Lie algebra sl6"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/simple-lie-algebra", "lie-groups/dynkin-diagram", "lie-groups/fundamental-representation"]
dependency_review_count = 1
section_mode = "progressive"
+++

The **complex Lie algebra** \(\mathfrak{sl}_6(\mathbb C)\) is the algebra of trace-zero \(6\times6\) complex matrices with commutator bracket. It is [[lie-groups/simple-lie-algebra|simple]], has complex dimension \(35\), rank \(5\), and [[lie-groups/dynkin-diagram|Dynkin type]] \(A_5\).

Its defining module is \(\mathbf6=\mathbb C^6\). The [[lie-groups/fundamental-representation|fundamental modules]] are \(\Lambda^k\mathbb C^6\) for \(1\leq k\leq5\), of dimensions \(6,15,20,15,6\). In particular \(\Lambda^3\mathbb C^6\) is a self-dual \(20\)-dimensional module, while the adjoint module has dimension \(35\).

## Root data and groups

The roots are \(\varepsilon_i-\varepsilon_j\), and the five consecutive differences form a simple system of type \(A_5\). The [[lie-groups/simply-connected-lie-group|simply connected]] complex group is \(SL(6,\mathbb C)\), with center \(\mu_6\), and its [[lie-groups/compact-real-form|compact real form]] is \(SU(6)\). Neither should be identified with the adjoint group \(PSL(6,\mathbb C)\), even though all have the expected closely related [[lie-groups/lie-algebra|Lie algebras]].

## Paper context

In the three-generation construction, a distinguished \(\mathfrak{sl}_6^{\mathrm{SM}}\) is the centralizer of the generation-symmetry \(\mathfrak{sl}_3^{\mathrm{gen}}\) inside [[lie-groups/exceptional-lie-algebra-e7|\(\mathfrak e_7\)]]. Together they form a maximal-rank regular subalgebra. The corresponding branching of the adjoint module is
\[
\mathbf{133}
\cong(\mathbf{35},\mathbf1)\oplus(\mathbf1,\mathbf8)
\oplus(\mathbf{15},\mathbf3)\oplus(\mathbf{15}^*,\mathbf{\bar3})
\]
under \(\mathfrak{sl}_6\oplus\mathfrak{sl}_3\), where
\(\mathbf{15}=\Lambda^2\mathbb C^6\) and
\(\mathbf{15}^*=\Lambda^4\mathbb C^6\).

The paper also uses the common intersection \(\mathfrak{sl}_6\oplus\mathbb C^2\) of three \(\mathfrak{sl}_2\oplus\mathfrak{so}_{12}\) subalgebras and a chain through the [[lie-groups/complex-lie-algebra-sl5|complex Lie algebra \(\mathfrak{sl}_5\)]]:
\[
\mathfrak g_{\mathrm{SM}}\subset\mathfrak{sl}_5
\subset\mathfrak{sl}_6\subset\mathfrak{sl}_6\oplus\mathbb C^2
\subset\mathfrak e_7.
\]

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4--6*, Springer, 2002, Plates I and VI. [Publisher record](https://doi.org/10.1007/978-3-540-89394-3).
2. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, Section 15. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
3. John C. Baez, *Three Generations in E7*, 2026. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
