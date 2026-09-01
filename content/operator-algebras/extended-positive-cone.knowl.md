+++
id = "operator-algebras/extended-positive-cone"
title = "Extended positive cone of a von Neumann algebra"
kind = "definition"
summary = "A cone of possibly unbounded positive objects evaluated on normal positive functionals."
aliases = ["extended positive part"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/normal-functional"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]
and \(M_*^+\) its cone of
[[operator-algebras/normal-functional|normal positive functionals]]. The
**extended positive cone** \(\widehat M_+\) consists of the maps
\[
m:M_*^+\longrightarrow[0,\infty]
\]
that are additive, positively homogeneous, and lower semicontinuous for the
norm topology on \(M_*^+\). Thus
\(m(\omega_1+\omega_2)=m(\omega_1)+m(\omega_2)\) and
\(m(t\omega)=t\,m(\omega)\) for \(t\geq0\), with
\(0\cdot\infty=0\). It is ordered pointwise. Every \(x\in M_+\) defines an
extended positive element by \(m_x(\omega)=\omega(x)\), but elements of
\(\widehat M_+\) may take the value \(\infty\).

## Operator realization

Extended positive elements admit a spectral realization by positive
self-adjoint [[operator-algebras/affiliated-operator|operators affiliated with \(M\)]], together with an allowed infinite part supported on a projection.
This realizes \(\widehat M_+\) as a completion of \(M_+\) that is closed under
increasing suprema.
The functional description is intrinsic and does not require choosing a
particular representation of \(M\).

## Operations and examples

Addition, multiplication by nonnegative scalars, and increasing suprema are
computed pointwise on \(M_*^+\). If \(a\in M\) and \(m\in\widehat M_+\), then
\(a^*ma\) is defined by
\[
(a^*ma)(\omega)=m(a\omega a^*),
\qquad (a\omega a^*)(x)=\omega(a^*xa).
\]
An ordinary positive element gives a finite-valued example. At the opposite
extreme, the formal value \(+\infty\) on a nonzero projection produces an
extended element that cannot belong to \(M_+\).

## Role in integration

The extended cone is the natural codomain for an
[[operator-algebras/operator-valued-weight|operator-valued weight]]:
integrating a positive element over one part of a noncommutative space can
produce an unbounded positive object over another part. Ordinary
\(N_+\)-valued maps cannot express this behavior without an artificial
boundedness assumption.

## References

1. Uffe Haagerup, “Operator-Valued Weights in von Neumann Algebras I,” *Journal of Functional Analysis* 32 (1979), 175–206. [DOI record](https://doi.org/10.1016/0022-1236%2879%2990053-3). Relevant: §1 on the extended positive part and its operations.
2. Masamichi Takesaki, *Theory of Operator Algebras II*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-662-10451-4). Relevant: Chapter IX, §4 on conditional expectations and operator-valued weights.
