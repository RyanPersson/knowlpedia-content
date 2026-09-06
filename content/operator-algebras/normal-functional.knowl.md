+++
id = "operator-algebras/normal-functional"
title = "Normal functional"
kind = "definition"
summary = "A bounded linear functional on a von Neumann algebra that is continuous for the ultraweak topology."
aliases = ["ultraweakly continuous functional"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/ultraweak-topology", "operator-algebras/predual", "operator-algebras/normal-linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]]. A
**normal functional** on \(M\) is a bounded linear functional
\(\varphi:M\to\mathbb C\) that is continuous for the
[[operator-algebras/ultraweak-topology|ultraweak topology]]. Equivalently,
\(\varphi\) belongs to the canonical [[operator-algebras/predual|predual]]
\(M_*\), under the isometric identification \(M=(M_*)^*\). Thus a normal
functional is precisely a scalar-valued
[[operator-algebras/normal-linear-map|normal linear map]]. Normality is an
additional continuity property specific to von Neumann algebras; an arbitrary
bounded functional on the underlying \(C^*\)-algebra need not be normal.

## Order characterization

If \(\varphi\) is positive, normality is equivalent to preservation of suprema
of bounded increasing nets:
\[
\varphi\!\left(\sup_i x_i\right)=\sup_i\varphi(x_i)
\]
for every bounded increasing net \((x_i)\) in \(M_+\). It is also enough to
test this condition on increasing nets of projections. Replacing nets by
sequences is generally insufficient unless suitable countability hypotheses
are imposed.

## Positive decomposition and states

Every normal functional is a [[convex-analysis/linear-combination|linear combination]] of four positive normal
functionals. Its adjoint \(\varphi^*(x)=\overline{\varphi(x^*)}\), real and
imaginary parts, and polar decomposition all remain within \(M_*\). A positive
normal functional of norm one is a
[[operator-algebras/normal-state|normal state]]. Positivity and normalization
are therefore extra properties; they are not part of the definition of a
normal functional.

## Concrete model

For \(M=B(H)\), each normal functional has the form
\[
\varphi(x)=\operatorname{Tr}(Tx)
\]
for a unique trace-class operator \(T\), and \(\|\varphi\|=\|T\|_1\). It is
positive exactly when \(T\) is positive. Singular bounded functionals on
\(B(H)\) lie outside the trace-class predual and show why norm continuity alone
does not imply normality.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §2 on the predual and normal functionals.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, American Mathematical Society, 1997. [AMS record](https://bookstore.ams.org/GSM/15). Relevant: ultraweak continuity and normal positive functionals.
