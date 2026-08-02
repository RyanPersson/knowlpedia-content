+++
id = "lie-groups/special-linear-lie-algebra"
title = "Special linear Lie algebra"
kind = "knowl"
summary = "The Lie algebra sl(n,F) of trace-zero matrices with bracket [X,Y]=XY−YX."
aliases = ["special-linear-lie-algebra", "Special linear Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/special-linear-lie-algebra.md"
+++

For \(\mathbb F\in\{\mathbb R,\mathbb C\}\), the **special linear Lie algebra** is
\[
\mathfrak{sl}_n(\mathbb F)=\{X\in M_n(\mathbb F): \mathrm{tr}(X)=0\},
\]
equipped with the commutator bracket
\[
[X,Y]=XY-YX
\]
(see [[fiber-bundles/lie-bracket|Lie bracket]] and compare [[lie-groups/general-linear-lie-algebra|general linear Lie algebra]]).

This Lie algebra is the Lie algebra of the [[lie-groups/special-linear-group|special linear group]] \(SL(n,\mathbb F)\): under the identification \(T_I SL(n,\mathbb F)\cong \mathfrak{sl}_n(\mathbb F)\), tangent vectors at the identity are exactly the trace-zero directions. Equivalently, \(\mathfrak{sl}_n(\mathbb F)\) is the kernel of the differential of \(\det:GL(n,\mathbb F)\to\mathbb F^\times\) at the identity.

Over \(\mathbb C\), \(\mathfrak{sl}_n(\mathbb C)\) is a fundamental example of a complex simple Lie algebra for \(n\ge 2\) (see [[lie-groups/simple-lie-algebra|simple Lie algebra]] and [[lie-groups/classification-simple-lie-algebras|classification of simple Lie algebras]]). The case \(n=2\) is the standard testbed for root computations (see [[lie-groups/example-sl2c|standard sl2 example]]).

## Dimensions and scalar restriction

One has
\[
\dim_{\mathbb R}\mathfrak{sl}_n(\mathbb R)=n^2-1,\qquad
\dim_{\mathbb C}\mathfrak{sl}_n(\mathbb C)=n^2-1.
\]
The [[lie-groups/underlying-real-lie-algebra|underlying real Lie algebra]]
\(\mathfrak{sl}_n(\mathbb C)_{\mathbb R}\) therefore has real dimension
\(2(n^2-1)\). In particular,
\[
\dim_{\mathbb C}\mathfrak{sl}_2(\mathbb C)=3,\qquad
\dim_{\mathbb R}\mathfrak{sl}_2(\mathbb C)_{\mathbb R}=6.
\]
The latter is the Lie algebra of both \(SL(2,\mathbb C)_{\mathbb R}\) and, after quotienting by the discrete center, \(PSL(2,\mathbb C)_{\mathbb R}\). It is isomorphic as a **real** Lie algebra to \(\mathfrak{so}(1,3)\).

## References

1. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer, 2015, Chapters 2–3. [Publisher record](https://doi.org/10.1007/978-3-319-13467-3).
2. Jean-Pierre Serre, *Complex Semisimple Lie Algebras*, Springer, 1987, Chapter I. [Publisher record](https://doi.org/10.1007/978-1-4757-3910-7).
