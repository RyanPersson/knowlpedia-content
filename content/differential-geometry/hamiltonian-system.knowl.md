+++
id = "differential-geometry/hamiltonian-system"
title = "Hamiltonian system"
kind = "definition"
summary = "A symplectic phase space together with a Hamiltonian function specifying its autonomous dynamics."
aliases = ["autonomous Hamiltonian system"]
domains = ["differential-geometry", "classical-mechanics"]
prerequisites = ["differential-geometry/classical-phase-space", "differential-geometry/hamiltonian-function", "differential-geometry/hamiltonian-vector-field"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

An **autonomous Hamiltonian system** is a triple \((M,\omega,H)\), where \((M,\omega)\) is a [[differential-geometry/classical-phase-space|classical phase space]] and \(H:M\to\mathbb R\) is a smooth [[differential-geometry/hamiltonian-function|Hamiltonian function]]. With the convention
\[
\iota_{X_H}\omega=dH,
\]
the system's trajectories are the maximal curves \(\gamma\) satisfying
\[
\dot\gamma(t)=X_H(\gamma(t)).
\]
Thus \(M\) is the state space, \(\omega\) converts the differential of \(H\) into the [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]], and \(H\) specifies the dynamics. The system is more data than any one of these ingredients separately.

## Evolution and observables

The [[differential-geometry/hamiltonian-flow|Hamiltonian flow]] preserves both \(\omega\) and \(H\). For an observable \(f\in C^\infty(M)\),
\[
\frac{d}{dt}f(\gamma(t))=\{f,H\},
\]
using the Poisson-bracket convention associated with \(\iota_{X_H}\omega=dH\). In particular, \(f\) is a [[differential-geometry/first-integral|first integral]] exactly when \(\{f,H\}=0\).

## Example

The harmonic oscillator on \(\mathbb R^2\) has
\[
\omega=dq\wedge dp,\qquad H(q,p)=\frac{p^2}{2m}+\frac{m\Omega^2q^2}{2}.
\]
Its Hamilton equations are \(\dot q=p/m\) and \(\dot p=-m\Omega^2q\), and its trajectories lie on the ellipses \(H=\text{constant}\). The symplectic plane without the choice of \(H\) is only a phase space, not this Hamiltonian system.

## Scope

**Warning.** If \(H\) depends explicitly on time, the resulting dynamics is a [[differential-geometry/time-dependent-hamiltonian-system|time-dependent Hamiltonian system]] and is not literally a triple of the form in the core. Constrained systems may begin with a degenerate presymplectic form, and infinite-dimensional field theories require additional analytic hypotheses.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Springer, 2008. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Lecture 18.4, Definition 18.8 and the discussion of integrals of motion.
2. V. I. Arnol'd, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: Chapter 8.
