+++
id = "operator-algebras/singular-state"
title = "Singular state on a von Neumann algebra"
kind = "definition"
summary = "A state on a von Neumann algebra that dominates no nonzero normal positive functional."
aliases = ["singular von Neumann algebra state", "purely singular state"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/state-cstar-algebra", "operator-algebras/normal-functional", "operator-algebras/normal-state"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]].
A [[operator-algebras/state-cstar-algebra|state]]
\(\varphi:M\to\mathbb C\) is **singular** if every
[[operator-algebras/normal-functional|normal positive functional]]
\(\psi\) satisfying \(0\leq\psi\leq\varphi\) is zero. Thus a singular state
has no nonzero normal positive part hidden beneath it in the order on
functionals. This is stronger than merely being non-normal: a convex
combination of a [[operator-algebras/normal-state|normal state]] and a singular
state is non-normal but not singular. The convention is the noncommutative
analogue of a purely finitely additive measure in the Yosida–Hewitt
decomposition.

## Equivalent projection criterion

Takesaki's projection criterion says that a
[[operator-algebras/positive-linear-functional|positive functional]]
\(\varphi\) on \(M\) is singular exactly when every nonzero projection
\(e\in M\) dominates a nonzero projection \(f\leq e\) with \(\varphi(f)=0\).
This formulation shows that singularity is distributed throughout the
projection lattice; it is not simply failure of ultraweak continuity at one
particular increasing net.

## Normal-singular decomposition

Every positive functional \(\omega\in M^*\) decomposes uniquely as
\[
\omega=\omega_{\mathrm n}+\omega_{\mathrm s},
\]
where \(\omega_{\mathrm n}\) is normal and \(\omega_{\mathrm s}\) is
singular. For a state, the two summands are positive but need not themselves
be states: their values at \(1\) add to \(1\). The state is normal precisely
when \(\omega_{\mathrm s}=0\), and singular precisely when
\(\omega_{\mathrm n}=0\). This is the operator-algebraic
normal-singular decomposition.

## Examples and non-examples

On \(\ell^\infty(\mathbb N)\), evaluation along a free ultrafilter is a
singular state. It vanishes on every finitely supported sequence even though
the corresponding finite-coordinate projections increase strongly to \(1\).
On \(B(H)\) for infinite-dimensional \(H\), any state that factors through
the quotient by \(K(H)\) is singular.

Finite-dimensional von Neumann algebras have no singular states because every
linear functional on them is normal. A nonnormal state with a nonzero normal
summand is the decisive near-miss: nonnormality alone does not imply
singularity.

## References

1. Masamichi Takesaki, “On the Singularity of a Positive Linear Functional on Operator Algebra,” *Proceedings of the Japan Academy* 35 (1959), 365–366. [DOI record](https://doi.org/10.3792/pja/1195524290). Relevant: the opening definition, normal-singular decomposition, and Theorem 1.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, AMS, 1997. [Publisher record](https://doi.org/10.1090/gsm/016). Relevant: §7.1 on normal and singular functionals.
