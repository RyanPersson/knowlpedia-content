+++
id = "noncommutative-geometry/even-spectral-triple"
title = "Even spectral triple"
kind = "definition"
summary = "A spectral triple with a grading that commutes with the represented algebra and anticommutes with its self-adjoint operator."
aliases = ["graded spectral triple", "even K-cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/spectral-triple", "functional-analysis/z2-graded-hilbert-space", "operator-algebras/graded-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

An **even spectral triple** is a [[noncommutative-geometry/spectral-triple|spectral triple]] \((\mathcal A,H,D)\) together with a [[functional-analysis/z2-graded-hilbert-space|grading]] operator \(\Gamma\) on \(H\) such that
\[
\Gamma=\Gamma^*,\qquad \Gamma^2=1,\qquad
\Gamma a=a\Gamma,\qquad
\Gamma D=-D\Gamma
\]
for every \(a\in\mathcal A\), with \(\Gamma\operatorname{Dom}(D)=\operatorname{Dom}(D)\). Thus the algebra representation is even and \(D\) is an [[operator-algebras/graded-operator|odd operator]] in the unbounded, domain-sensitive sense. Equivalently, \(H=H^+\oplus H^-\), every \(a\) preserves the two summands, and \(D\) interchanges them.

## Block form

Relative to \(H^+\oplus H^-\), the data have the form
\[
a=
\begin{pmatrix}
a^+&0\\
0&a^-
\end{pmatrix},
\qquad
D=
\begin{pmatrix}
0&D^-\\
D^+&0
\end{pmatrix},
\]
where self-adjointness gives \(D^-=(D^+)^*\), with the corresponding domains understood. The off-diagonal form is precisely the anticommutation relation \(\Gamma D=-D\Gamma\).

## Geometric example

On a closed even-dimensional Riemannian spin manifold, the complex [[differential-geometry/spinor-bundle|spinor bundle]] splits as
\[
S=S^+\oplus S^-.
\]
The chirality operator supplies \(\Gamma\), functions preserve the splitting, and the spin [[noncommutative-geometry/dirac-operator|Dirac operator]] exchanges positive and negative spinors. The canonical spectral triple is therefore even.

## Index pairing

For a projection \(p\) over the algebra, the represented projection preserves the graded subspaces. Under the usual compactness hypotheses, the compression of the positive part,
\[
pD^+p:pH^+\longrightarrow pH^-,
\]
has a Fredholm realization, and its integer index gives the even pairing with K-theory. Precise domain and matrix-amplification conventions are part of the pairing construction, not extra axioms in the definition above.

## Graded-algebra variant

The standard definition assumes that \(\mathcal A\) is trivially graded, which is why every represented \(a\) commutes with \(\Gamma\). If \(\mathcal A\) itself is graded, a graded representation and graded commutators replace these ordinary parity relations. That convention is broader and should be stated explicitly.

## References

- [Alain Connes, *Noncommutative Geometry*, Parts IV and VI (Academic Press, 1994)](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf)
- [José M. Gracia-Bondía, Joseph C. Várilly, and Héctor Figueroa, *Elements of Noncommutative Geometry*, Section 10.1 (Birkhäuser, 2001)](https://doi.org/10.1007/978-1-4612-0005-5)
