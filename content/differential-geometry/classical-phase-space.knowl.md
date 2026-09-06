+++
id = "differential-geometry/classical-phase-space"
title = "Classical phase space"
kind = "definition"
summary = "A symplectic manifold whose points represent the instantaneous states of a finite-dimensional classical system."
aliases = ["phase space", "Hamiltonian phase space"]
domains = ["differential-geometry", "classical-mechanics"]
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/hamiltonian-function", "fiber-bundles/vector-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

In finite-dimensional Hamiltonian mechanics, a **classical phase space** is a [[differential-geometry/symplectic-manifold|symplectic manifold]] \((P,\omega)\) whose points represent the complete instantaneous states of a classical system. A real-valued [[differential-geometry/hamiltonian-function|smooth function \(H\in C^\infty(P)\), called a Hamiltonian]], specifies a particular dynamics through the unique [[fiber-bundles/vector-field|vector field]] \(X_H\) determined by
\[
\iota_{X_H}\omega=dH.
\]
Thus the symplectic form belongs to the kinematic structure of phase space, whereas the choice of \(H\) supplies the evolution law. Sign conventions may instead use \(\iota_{X_H}\omega=-dH\).

## Cotangent-bundle model

For a configuration manifold \(Q\), the standard phase space is the [[fiber-bundles/cotangent-bundle|cotangent bundle]] \(T^*Q\). Its points \((q,p)\) record position and momentum, and its canonical symplectic form is obtained from the tautological \(1\)-form. This construction is intrinsic and does not require a metric on \(Q\).

## Observables and evolution

Smooth functions on \(P\) are classical observables. The symplectic form defines their Poisson bracket, and [[differential-geometry/hamiltonian-flow|Hamiltonian flow]] preserves \(\omega\) and the Hamiltonian \(H\). A [[differential-geometry/hamiltonian-system|Hamiltonian system]] is therefore more data than a phase space: it is usually a triple \((P,\omega,H)\).

## Scope and generalizations

The definition describes unconstrained finite-dimensional Hamiltonian mechanics. Systems with constraints may first produce a degenerate presymplectic form and require reduction. Infinite-dimensional field theories need functional-analytic hypotheses, and statistical or quantum state spaces use different structures. In Poisson mechanics, a [[differential-geometry/poisson-manifold|Poisson manifold]] is sometimes also called a phase space even when its Poisson tensor is degenerate.

## References

1. V. I. Arnol'd, *Mathematical Methods of Classical Mechanics*, Springer, 1978. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: Hamiltonian mechanics, differential forms, and symplectic manifolds.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Springer, 2008. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: canonical symplectic form on a cotangent bundle and Hamiltonian mechanics.
