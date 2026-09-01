+++
id = "operator-algebras/breuer-fredholm-operator"
title = "Breuer–Fredholm operator"
kind = "definition"
summary = "An operator in a semifinite von Neumann algebra that is invertible modulo the ideal of trace-compact operators."
aliases = ["tau-Fredholm operator", "semifinite Fredholm operator"]
domains = ["operator-algebras", "functional-analysis"]
prerequisites = ["operator-algebras/semifinite-von-neumann-algebra", "operator-algebras/faithful-normal-semifinite-trace", "operator-algebras/tau-compact-operator", "functional-analysis/fredholm-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\mathcal M\subseteq B(H)\) be a
[[operator-algebras/semifinite-von-neumann-algebra|semifinite von Neumann
algebra]] equipped with a
[[operator-algebras/faithful-normal-semifinite-trace|faithful normal
semifinite trace]], and let
\(\mathcal K(\mathcal M,\tau)\) be its
[[operator-algebras/tau-compact-operator|tau-compact ideal]]. A bounded
operator \(T\in\mathcal M\) is **Breuer–Fredholm** if its image in the quotient
\(C^*\)-algebra
\[
\mathcal M/\mathcal K(\mathcal M,\tau)
\]
is invertible. Equivalently, there is \(S\in\mathcal M\) such that
\(1-ST\) and \(1-TS\) are tau-compact. This is the semifinite analogue of a
[[functional-analysis/fredholm-operator|Fredholm operator]], with
tau-compactness replacing ordinary compactness.

## Kernel criterion and index

A bounded \(T\in\mathcal M\) is Breuer–Fredholm exactly when
\(\tau(P_{\ker T})<\infty\) and there is a projection \(p\in\mathcal M\) such
that \(\tau(1-p)<\infty\) and \(pH\subseteq\operatorname{Ran}(T)\). In that
case the cokernel projection \(P_{\ker T^*}\) also has finite trace, and the
Breuer index is
\[
\operatorname{Ind}_\tau(T)
=\tau(P_{\ker T})-\tau(P_{\ker T^*}).
\]
Unlike the classical Fredholm index, this value may be any real number because
the trace of a projection in a semifinite algebra need not be integral.

## Stability and examples

The Breuer–Fredholm operators form an open subset of \(\mathcal M\), and their
index is locally constant. Adding an element of
\(\mathcal K(\mathcal M,\tau)\) preserves Breuer–Fredholmness and the index.
For \(\mathcal M=B(H)\) with the ordinary trace, tau-compact operators are the
usual [[linear-algebra/compact-operator|compact operators]], so the definition
and index reduce to classical Fredholm theory.

If \(\tau(1)<\infty\), then
\(\mathcal K(\mathcal M,\tau)=\mathcal M\), the quotient is zero, and the
notion becomes degenerate: every operator is Breuer–Fredholm under the standard
zero-quotient convention. Applications generally concern traces for which the
relative compact ideal is proper.

## Unbounded version

A closed densely defined self-adjoint
[[operator-algebras/affiliated-operator|operator affiliated with \(\mathcal M\)]] is called Breuer–Fredholm when an appropriate bounded
transform, such as
\[
T(1+T^2)^{-1/2},
\]
is Breuer–Fredholm. Equivalent formulations use invertibility modulo
tau-compact operators for the resolvent or spectral projections near zero.
This unbounded form is the one used in
[[noncommutative-geometry/semifinite-spectral-triple|semifinite spectral
triples]] and [[noncommutative-geometry/spectral-flow|spectral flow]].

## References

1. M. Breuer, “Fredholm theories in von Neumann algebras. I,” *Mathematische Annalen* 178 (1968), 243–254. [DOI record](https://doi.org/10.1007/BF01350663). Relevant: §§1–3 on relative compactness, Fredholm operators, and the trace index.
2. A. L. Carey, J. Phillips, A. Rennie, and F. A. Sukochev, “The local index formula in semifinite von Neumann algebras I: Spectral flow,” *Advances in Mathematics* 202 (2006), 451–516. [Preprint record](https://arxiv.org/abs/math/0411019). Relevant: §2 on semifinite Fredholm theory and spectral flow.
