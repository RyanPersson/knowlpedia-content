+++
id = "real-analysis/moment-matching"
title = "Matching prescribed integral moments"
kind = "definition"
summary = "Choosing a function so a specified finite family of integral functionals takes prescribed values."
aliases = ["integral moment matching", "integral moment map"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/weighted-radial-moment", "shared-foundations/function", "shared-foundations/finite-set", "measure-theory/lebesgue-integral"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Given integral functionals \(\Phi_1,\ldots,\Phi_m\) on a class of functions, **moment matching** asks for \(u\) such that
\[
\Phi_j(u)=d_j,\qquad 1\le j\le m.
\]
The **moment map** in this sense is \(\Phi(u)=(\Phi_1(u),\ldots,\Phi_m(u))\). The functionals may be linear [[real-analysis/weighted-radial-moment|weighted integrals]] or integrals of nonlinear expressions such as \(u^2\).

## Function-valued targets

For profiles \(u(r,\eta)\), one may prescribe \(\Phi_j(u)(\eta)=d_j(\eta)\) for every \(\eta\). There are finitely many rows, but each row is a function. Solving at finitely many sample values does not establish this identity. Corrections built from fixed radial bumps and parameter-dependent coefficients reduce the problem to a parameterized finite system. This integral moment map is distinct from a Hamiltonian moment map in symplectic geometry.
