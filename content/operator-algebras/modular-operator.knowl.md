+++
id = "operator-algebras/modular-operator"
title = "Modular operator"
kind = "definition"
summary = "The modular operator is the positive self-adjoint part of the polar decomposition of a Tomita operator."
aliases = ["Delta operator", "Tomita modular operator"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/cyclic-vector", "operator-algebras/separating-vector", "operator-algebras/tomita-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] with
[[operator-algebras/cyclic-vector|cyclic]]
[[operator-algebras/separating-vector|separating vector]] \(\Omega\), and let
\(S\) be its
[[operator-algebras/tomita-operator|Tomita operator]]. The
**modular operator** of \((M,\Omega)\) is
\[
\Delta=S^*S.
\]
It is a positive self-adjoint operator with trivial kernel and generally is
unbounded. Its positive square root occurs in the polar decomposition
\[
S=J\Delta^{1/2},
\]
where \(J\) is the
[[operator-algebras/modular-conjugation|modular conjugation]]. The spectral
calculus defines a strongly continuous unitary group
\(t\mapsto\Delta^{it}\), even when \(\Delta\) or \(\Delta^{-1}\) is
unbounded. The operator depends on the chosen pair \((M,\Omega)\).

## Modular dynamics

The [[operator-algebras/tomita-takesaki-theorem|Tomita–Takesaki theorem]]
states that
\[
\Delta^{it}M\Delta^{-it}=M,\qquad t\in\mathbb R.
\]
Hence
\(\sigma_t^\Omega(x)=\Delta^{it}x\Delta^{-it}\) defines a one-parameter group
of \(*\)-automorphisms of \(M\). The invariance of \(M\) is the deep modular
theorem; it does not follow from spectral calculus alone.

## Spectral relations

Modular conjugation reverses the positive generator:
\[
J\Delta J=\Delta^{-1}.
\]
The vector \(\Omega\) lies in the kernel of \(\Delta-1\), because
\(S\Omega=\Omega=S^*\Omega\). If the vector functional
\(\langle\,\cdot\,\Omega,\Omega\rangle\) is tracial, then \(\Delta=1\).
Conversely, in the cyclic separating setting, \(\Delta=1\) implies that this
vector functional is a trace.

## Finite-dimensional model

Let \(M=M_n(\mathbb C)\) act by left multiplication on Hilbert–Schmidt
matrices, and represent a faithful state by an invertible density matrix
\(\rho\). Under the standard identification, the modular operator acts as
\[
\Delta(x)=\rho x\rho^{-1}.
\]
Thus \(\Delta^{it}(x)=\rho^{it}x\rho^{-it}\). It equals the identity exactly
when \(\rho\) is scalar, illustrating how modular data measure the failure of
a faithful state to be tracial.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter VI, §1 on the modular operator and its unitary group.
