+++
id = "operator-algebras/predual"
title = "Predual of a von Neumann algebra"
kind = "definition"
summary = "The canonical Banach space whose continuous dual is a von Neumann algebra."
aliases = ["normal functional space", "von Neumann algebra predual"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

For a [[operator-algebras/von-neumann-algebra|von Neumann algebra]] \(M\), its
**predual** \(M_*\) is the [[linear-algebra/banach-space|Banach space]] of
ultraweakly continuous linear functionals on \(M\), with the norm inherited
from the Banach dual \(M^*\). Evaluation gives an isometric identification
\[
M=(M_*)^*.
\]
Under this identification, the
[[functional-analysis/weak-star-topology|weak-star topology]]
\(\sigma(M,M_*)\) is precisely the
[[operator-algebras/ultraweak-topology|ultraweak topology]] on \(M\).
Consequently, elements of \(M_*\) are also called
[[operator-algebras/normal-functional|normal functionals]]. A fundamental
uniqueness theorem says that \(M_*\) is the unique Banach predual of \(M\) up
to the canonical isometric isomorphism compatible with the duality.

## Concrete realization

If \(M\subseteq B(H)\) is represented concretely, every element of \(M_*\)
has the form
\[
x\longmapsto \operatorname{Tr}(ax),
\]
after restricting a
[[shale-paper/trace-class-operator|trace-class operator]] \(a\) on \(H\) to
\(M\). Different trace-class operators can induce the same functional. More
precisely, \(M_*\) is isometrically the quotient of the trace-class operators
by the annihilator of \(M\), rather than generally a distinguished subspace
of the trace class.

## Positive and normal functionals

Positive elements of \(M_*\) are exactly the normal [[operator-algebras/positive-linear-functional|positive functionals]] on
\(M\). Every element of \(M_*\) is a [[convex-analysis/linear-combination|linear combination]] of normal positive
functionals, and [[operator-algebras/normal-state|normal states]] are the
positive elements of norm one. This order structure makes monotone
convergence inside \(M\) visible to its predual.

## Why the distinction matters

The full Banach dual \(M^*\) usually contains singular functionals that are
not ultraweakly continuous. Thus \(M_*\) must not be confused with \(M^*\).
Weak-star compactness, [[operator-algebras/normal-representation|normal representations]], and integration theory for
von Neumann algebras use the dual pair \((M,M_*)\), not the larger pairing
\((M,M^*)\).

## References

- [Masamichi Takesaki, *Theory of Operator Algebras I*, Chapter III, §2 (Springer, 1979)](https://doi.org/10.1007/978-1-4612-6188-9)
- [Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, Chapter 7 (American Mathematical Society, 1997)](https://bookstore.ams.org/gsm-16/)
