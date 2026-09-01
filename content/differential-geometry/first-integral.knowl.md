+++
id = "differential-geometry/first-integral"
title = "First integral"
kind = "definition"
summary = "A smooth function that is constant along every trajectory of a dynamical system."
aliases = ["constant of motion", "conserved quantity"]
domains = ["differential-geometry", "classical-mechanics"]
prerequisites = ["differential-geometry/hamiltonian-system", "differential-geometry/hamiltonian-vector-field", "differential-geometry/hamiltonian-flow"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,\omega,H)\) be a [[differential-geometry/hamiltonian-system|Hamiltonian system]] with [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] \(X_H\). A smooth function \(F:M\to\mathbb R\) is a **first integral** if
\[
dF(X_H)=0
\]
at every point of \(M\). Equivalently, \(F\) is constant along each integral curve of \(X_H\), or \(F\circ\varphi_t=F\) wherever the [[differential-geometry/hamiltonian-flow|Hamiltonian flow]] \(\varphi_t\) is defined. With the Poisson-bracket convention \(\dot F=\{F,H\}\), the defining condition is \(\{F,H\}=0\). The zero condition is independent of the opposite sign convention for the bracket.

## Equivalent formulations and use

The flow formulation follows from
\[
\frac{d}{dt}F(\varphi_t(x))=dF_{\varphi_t(x)}(X_H)=\{F,H\}(\varphi_t(x)).
\]
Thus a first integral confines every trajectory to a level set of \(F\). Several independent first integrals can reduce the effective dimension of the motion; when half the phase-space dimension is supplied by pairwise commuting integrals, one obtains a [[differential-geometry/completely-integrable-hamiltonian-system|completely integrable Hamiltonian system]].

## Examples and non-examples

The Hamiltonian \(H\) itself is a first integral because \(\{H,H\}=0\). If a Lie-group symmetry preserves \(H\), the corresponding component of a [[fiber-bundles/moment-map|moment map]] is another standard example. A function that is constant on one selected trajectory but not on all trajectories is not a first integral on \(M\); the defining identity must hold everywhere in its stated domain.

## Conventions and scope

For a general [[fiber-bundles/vector-field|vector field]] \(X\), the same term means a function satisfying \(dF(X)=0\). For a time-dependent Hamiltonian \(H_t\), a time-dependent conserved quantity \(F_t\) instead satisfies \(\partial_tF_t+\{F_t,H_t\}=0\). “First integral” does not mean an antiderivative, despite that usage of “integral” in elementary calculus.

## References

1. V. I. Arnol'd, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: Chapters 9–10, first integrals, Poisson brackets, and complete integrability.
2. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., AMS Chelsea Publishing 364, 2008 reprint. [DOI record](https://doi.org/10.1090/chel/364). Relevant: Chapters 3–4, Hamiltonian systems, conserved quantities, and symmetry.
