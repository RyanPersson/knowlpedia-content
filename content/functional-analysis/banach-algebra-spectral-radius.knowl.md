+++
id = "functional-analysis/banach-algebra-spectral-radius"
title = "Spectral radius in a Banach algebra"
kind = "definition"
summary = "The largest modulus of a spectral value of a Banach-algebra element."
aliases = ["spectral radius of an element"]
domains = ["functional-analysis", "operator-algebras"]
prerequisites = ["functional-analysis/banach-algebra", "functional-analysis/banach-algebra-spectrum"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be a complex unital
[[functional-analysis/banach-algebra|Banach algebra]] and let \(a\in A\). The
**spectral radius** of \(a\) is
\[
r_A(a)=\sup\{|\lambda|:\lambda\in\sigma_A(a)\},
\]
where \(\sigma_A(a)\) is the
[[functional-analysis/banach-algebra-spectrum|spectrum of \(a\) in \(A\)]].
Because that spectrum is nonempty and compact, the supremum is a maximum.
The spectral-radius formula states that
\[
r_A(a)=\lim_{n\to\infty}\lVert a^n\rVert^{1/n}
      =\inf_{n\geq1}\lVert a^n\rVert^{1/n}.
\]
For a nonunital Banach algebra, the spectral radius is computed in its
unitization. It always satisfies \(0\leq r_A(a)\leq\lVert a\rVert\).

## Basic properties

One has \(r(a^n)=r(a)^n\) for positive integers \(n\), and more generally
polynomial spectral mapping gives \(r(p(a))=\max_{\lambda\in\sigma(a)}
|p(\lambda)|\). The spectral radius need not be a norm: nonzero nilpotent
elements have radius zero, and subadditivity can fail in noncommutative
Banach algebras. The limit formula, including existence of the limit, is a
central result of Banach-algebra spectral theory.

## The C-star-algebra case

If \(a\) is normal in a \(C^*\)-algebra, then
\(r(a)=\lVert a\rVert\). In particular, this holds for self-adjoint, positive,
and unitary elements. For an arbitrary \(C^*\)-algebra element, the sharper
identity is
\[
\lVert a\rVert^2=r(a^*a).
\]
Thus the norm is spectrally determined on normal elements even though the
spectral radius can be strictly smaller than the norm for nonnormal ones.

## Examples

For a matrix, the spectral radius is the maximum modulus of its eigenvalues.
The matrix
\(\begin{pmatrix}0&1\\0&0\end{pmatrix}\) has spectral radius zero but
positive [[linear-algebra/operator-norm|operator norm]]. For multiplication by a continuous function \(f\)
on \(C(X)\), the spectral radius is \(\max_{x\in X}|f(x)|\).

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §§1.2 and 2.2 on spectra, the spectral-radius formula, and normal elements.
