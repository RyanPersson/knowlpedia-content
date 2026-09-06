+++
id = "noncommutative-geometry/semifinite-spectral-triple"
title = "Semifinite spectral triple"
kind = "definition"
summary = "A spectral triple represented in a semifinite von Neumann algebra with compactness measured by a semifinite trace."
aliases = ["semifinite unbounded Fredholm module", "spectral triple relative to (M,tau)"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/involutive-algebra", "operator-algebras/semifinite-von-neumann-algebra", "operator-algebras/faithful-normal-semifinite-trace", "operator-algebras/affiliated-operator", "operator-algebras/tau-compact-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **semifinite spectral triple** \((\mathcal A,\mathcal H,D;\mathcal M,\tau)\)
consists of a unital
[[operator-algebras/involutive-algebra|involutive algebra]] \(\mathcal A\)
represented in a
[[operator-algebras/semifinite-von-neumann-algebra|semifinite von Neumann
algebra]] \(\mathcal M\subseteq B(\mathcal H)\), a
[[operator-algebras/faithful-normal-semifinite-trace|faithful normal
semifinite trace]] \(\tau\) on
\(\mathcal M\), and a densely defined self-adjoint operator
\(D\) [[operator-algebras/affiliated-operator|affiliated with \(\mathcal M\)]]. Each \(a\in\mathcal A\) preserves
\(\operatorname{Dom}(D)\), the commutator \([D,a]\) extends boundedly, and
the resolvent scale belongs to the
[[operator-algebras/tau-compact-operator|tau-compact ideal]]:
\[
(1+D^2)^{-1/2}\in\mathcal K(\mathcal M,\tau).
\]
Thus both measurability and compactness are internal to the traced algebra
\((\mathcal M,\tau)\).

## Relation to ordinary spectral triples

Taking \(\mathcal M=B(\mathcal H)\) with its canonical trace makes
\(\mathcal K(\mathcal M,\tau)\) the ordinary
[[linear-algebra/compact-operator|compact operators]]. The definition
then becomes the usual compact
[[noncommutative-geometry/spectral-triple|spectral triple]]. For a general
semifinite algebra, tau-compactness can be weaker than Hilbert-space
compactness, and the trace provides real-valued dimensions of spectral
projections. This replacement is the basis of the semifinite local index
formula.

## Fredholm and summability data

The [[noncommutative-geometry/bounded-transform-spectral-triple|bounded
transform]]
\[
F=D(1+D^2)^{-1/2}
\]
is a [[operator-algebras/breuer-fredholm-operator|Breuer–Fredholm operator]]
modulo the tau-compact ideal, and its trace index replaces the integer-valued
Fredholm index. Summability is also measured by \(\tau\): for example,
\(p\)-summability may require
\((1+D^2)^{-p/2}\) to be tau-integrable.
Regularity, dimension spectrum,
grading, and real structure are additional axioms rather than consequences of
semifiniteness.

## Examples and variants

An ordinary spectral triple is the basic example via
\(\mathcal M=B(\mathcal H)\). Geometric operators on a regular covering can
instead be placed in the [[operator-algebras/von-neumann-algebra|von Neumann algebra]] of equivariant operators and
measured using its canonical semifinite trace, producing \(L^2\)-type indices.

For nonunital \(\mathcal A\), global tau-compact resolvent is usually replaced
by local compactness
\[
a(1+D^2)^{-1/2}\in\mathcal K(\mathcal M,\tau)
\qquad(a\in\mathcal A).
\]
Authors also vary between \((1+D^2)^{-1/2}\) and resolvent formulations; for
self-adjoint \(D\), functional calculus relates these conventions.

## References

1. A. L. Carey, J. Phillips, A. Rennie, and F. A. Sukochev, “The local index formula in semifinite von Neumann algebras I: Spectral flow,” *Advances in Mathematics* 202 (2006), 451–516. [Preprint record](https://arxiv.org/abs/math/0411019). Relevant: §2 on semifinite spectral triples, tau-compactness, and Breuer–Fredholm operators.
2. A. L. Carey, J. Phillips, A. Rennie, and F. A. Sukochev, “The local index formula in semifinite von Neumann algebras II: The even case,” *Advances in Mathematics* 202 (2006), 517–554. [DOI record](https://doi.org/10.1016/j.aim.2005.03.010). Relevant: the even semifinite framework and generalized McKean–Singer formula.
