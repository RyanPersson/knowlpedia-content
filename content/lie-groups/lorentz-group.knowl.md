+++
id = "lie-groups/lorentz-group"
title = "Lorentz group"
kind = "knowl"
summary = "The group of linear transformations preserving the Minkowski bilinear form."
aliases = ["lorentz-group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lorentz-group.md"
+++

Fix the Minkowski bilinear form on \(\mathbb R^n\) with one negative and \(n-1\) positive directions, represented by
\[
\eta=\mathrm{diag}(-1,1,\dots,1).
\]
Thus the [[linear-algebra/signature-of-symmetric-bilinear-form|signature]] notation \((1,n-1)\) here lists negative directions first. This is the convention used in [[linear-algebra/minkowski-vector-space|Minkowski vector space]] and the Hermitian determinant model.

The **Lorentz group** in dimension \(n\) is the subgroup
\[
O(1,n-1)=\{A\in \mathrm{GL}(n,\mathbb R)\mid A^{\mathsf T}\eta A=\eta\}.
\]

It is an instance of the [[lie-groups/orthogonal-group|orthogonal group in an indefinite signature]]. The case \(n=4\) is the classical Lorentz group of special relativity.

Two commonly used subgroups are:
- \(SO(1,n-1)=\{A\in O(1,n-1)\mid \det A=1\}\) (the “special” Lorentz group),
- the identity component \(SO^{+}(1,n-1)\), consisting of matrices preserving both orientation and a chosen [[differential-geometry/time-orientation|time orientation]].

The identity component is also called the
[[lie-groups/proper-orthochronous-lorentz-group|proper orthochronous Lorentz
group]] (with the linked page treating the four-dimensional case).

## Lie algebra
Its Lie algebra is the indefinite orthogonal Lie algebra
\[
\mathfrak{so}(1,n-1)=\{X\in \mathfrak{gl}(n,\Bbb R)\mid X^{T}\eta+\eta X=0\},
\]
an instance of [[lie-groups/orthogonal-lie-algebra|orthogonal Lie algebras]].

## Remarks
The Lorentz group acts linearly on Minkowski space, and adjoining translations yields the [[lie-groups/poincare-group|Poincaré group]], the full isometry group of Minkowski spacetime. In four dimensions, the identity component has the spin covering
\[
SL(2,\mathbb C)_{\mathbb R}\longrightarrow SO^+(1,3)
\]
and the induced real-Lie-group isomorphism \(PSL(2,\mathbb C)_{\mathbb R}\cong SO^+(1,3)\). The full group \(O(1,3)\) has four connected components; the spin cover above does not include parity or time reversal.

## References

1. Barrett O'Neill, *Semi-Riemannian Geometry With Applications to Relativity*, Academic Press, 1983, Chapter 5. [Publisher record](https://doi.org/10.1016/C2009-0-11874-8).
2. Gregory L. Naber, *The Geometry of Minkowski Spacetime*, 2nd ed., Springer, 2012, Chapters 1–2. [Publisher record](https://doi.org/10.1007/978-1-4419-7838-7).
