+++
id = "functional-analysis/spectrum-closed-operator"
title = "Spectrum of a closed operator"
kind = "definition"
summary = "The complement of the resolvent set for a closed, possibly unbounded operator."
aliases = ["operator spectrum for an unbounded operator", "spectrum of an unbounded operator"]
domains = ["functional-analysis", "operator-theory", "spectral-theory"]
prerequisites = ["functional-analysis/closed-linear-operator", "linear-algebra/banach-space", "functional-analysis/resolvent-set-closed-operator", "functional-analysis/closed-graph-theorem"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(T:\mathcal D(T)\subseteq X\to X\) be a densely defined
[[functional-analysis/closed-linear-operator|closed operator]] on a complex
[[linear-algebra/banach-space|Banach space]]. Its **spectrum** is
\[
\sigma(T)=\mathbb C\setminus\rho(T),
\]
where \(\rho(T)\) is the
[[functional-analysis/resolvent-set-closed-operator|resolvent set]]: the set
of \(\lambda\in\mathbb C\) for which
\[
T-\lambda I:\mathcal D(T)\longrightarrow X
\]
is bijective and its inverse is bounded on \(X\). Because \(T\) is closed,
boundedness of this everywhere-defined inverse follows from bijectivity and
the [[functional-analysis/closed-graph-theorem|closed graph theorem]]. The domain is part of the definition; replacing
\(\mathcal D(T)\) can change the spectrum even when the differential formula
for \(T\) is unchanged.

## Basic topology

The resolvent set is open, the resolvent depends analytically on
\(\lambda\), and \(\sigma(T)\) is closed. Unlike the spectrum of a bounded
operator, the spectrum of a closed unbounded operator need not be bounded,
compact, or even nonempty. For a
[[functional-analysis/self-adjoint-unbounded-operator|self-adjoint operator]]
on a [[linear-algebra/hilbert-space|Hilbert space]], however, the spectrum is a nonempty closed subset of
\(\mathbb R\), and every nonreal number lies in the resolvent set.

## Spectral parts

If \(T-\lambda I\) is not injective, then \(\lambda\) is an eigenvalue and
belongs to the point spectrum. When it is injective with dense but non-surjective
range, \(\lambda\) lies in the continuous spectrum under the standard Hilbert
space convention. When the range is not dense, \(\lambda\) lies in the
residual spectrum. These parts can behave very differently for
non-self-adjoint operators.

## Dependence on closed realizations

An unbounded expression such as a differential operator does not determine a
spectrum until its domain, including any boundary conditions, has been fixed.
Distinct closed realizations of the same expression can have different
eigenvalues and resolvents. Spectral assertions should therefore name the
closed operator rather than only its formal formula.

## References

- [Tosio Kato, *Perturbation Theory for Linear Operators*, Chapter III (Springer, 1995)](https://doi.org/10.1007/978-3-642-66282-9)
- [Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Chapter 2 (Springer, 2012)](https://doi.org/10.1007/978-94-007-4753-1)
