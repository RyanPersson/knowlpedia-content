+++
id = "noncommutative-geometry/spectral-flow"
title = "Spectral flow"
kind = "definition"
summary = "The signed count of eigenvalues crossing zero along a continuous path of self-adjoint Fredholm operators."
aliases = ["net eigenvalue crossing", "spectral-flow index"]
domains = ["noncommutative-geometry", "functional-analysis", "operator-algebras"]
section_mode = "progressive"
+++

Let \(H\) be a separable complex [[linear-algebra/hilbert-space|Hilbert space]] and let \(B:[0,1]\to\mathcal B(H)\) be a norm-continuous path of self-adjoint [[functional-analysis/fredholm-operator|Fredholm operators]]. Choose \(0=t_0<\cdots<t_m=1\) and \(a_i>0\) so that \(E_i(t)=1_{[-a_i,a_i]}(B_t)\) is finite-rank and norm-continuous on \([t_{i-1},t_i]\). Let \(E_i^+(t)H\) be its spectral subspace for eigenvalues in \([0,a_i]\). The **spectral flow** is
\[
\operatorname{sf}(B)=\sum_{i=1}^m
\bigl(\dim E_i^+(t_i)H-\dim E_i^+(t_{i-1})H\bigr).
\]
It is independent of these choices; a crossing from negative to positive contributes \(+1\).

## Meaning of the local formula

Fredholmness isolates \(0\) from the essential spectrum, so only finitely many eigenvalues lie in a sufficiently small interval around \(0\). The subdivision allows that interval to vary along the path without letting eigenvalues escape through its endpoints. Comparing the nonnegative parts at the ends of each subinterval counts the signed crossings, including multiplicity.

No differentiability or generic-crossing assumption is required. For paths with simple transverse crossings, however, the formula reduces to the intuitive count of upward crossings minus downward crossings.

## Structure and consequences

Spectral flow is invariant under fixed-endpoint homotopy, additive under concatenation, and additive under direct sums. On loops in the indefinite component of bounded self-adjoint Fredholm operators, it realizes the fundamental-group isomorphism with \(\mathbb Z\).

When a path joins invertible endpoints, spectral flow is stable under sufficiently small endpoint-preserving perturbations. Endpoint conventions require care when a path begins or ends with a nontrivial kernel.

## Examples and non-examples

On the one-dimensional Hilbert space \(\mathbb C\), the path
\[
B_t=2t-1
\]
has one eigenvalue crossing \(0\) upward, so \(\operatorname{sf}(B)=1\). Reversing the path gives \(-1\).

A path of self-adjoint operators that reaches an operator with \(0\) in its essential spectrum is not a path in the self-adjoint Fredholm space. The finite-rank local spectral projection may then fail to exist, so the defining Fredholm hypothesis has been lost.

## Unbounded and semifinite extensions

For paths of [[functional-analysis/self-adjoint-unbounded-operator|self-adjoint unbounded Fredholm operators]], continuity must be specified. Gap-continuous paths admit a spectral-flow theory through graph projections or the Cayley transform; Riesz-continuous paths can be treated through bounded transforms. These topologies are not interchangeable without hypotheses.

In a [[operator-algebras/semifinite-von-neumann-algebra|semifinite von Neumann algebra]], self-adjoint Breuer-Fredholm paths have a trace-valued analogue. In type \(\mathrm{II}_\infty\), it can be real-valued rather than integer-valued and is expressed using the trace dimension of spectral projections.

## References

1. [John Phillips, “Self-Adjoint Fredholm Operators and Spectral Flow,” *Canadian Mathematical Bulletin* 39 (1996), 460–467](https://doi.org/10.4153/CMB-1996-054-4).
2. [Bernhelm Booss-Bavnbek, Matthias Lesch, and John Phillips, “Unbounded Fredholm Operators and Spectral Flow,” *Canadian Journal of Mathematics* 57 (2005), 225–250](https://arxiv.org/abs/math/0108014).
3. [Alan L. Carey and John Phillips, “Spectral Flow in Fredholm Modules, Eta Invariants and the JLO Cocycle,” *K-Theory* 31 (2004), 135–194](https://arxiv.org/abs/math/0308161).
