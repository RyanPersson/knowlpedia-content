+++
id = "differential-geometry/hamiltonian-function"
title = "Hamiltonian function"
kind = "definition"
summary = "A Hamiltonian function is a smooth real-valued function on a symplectic manifold that determines a Hamiltonian vector field."
aliases = ["Hamiltonian"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-manifold", "fiber-bundles/vector-field"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]]. A **Hamiltonian function** is a smooth function \(H:M\to\mathbb{R}\). With the convention
\[
\iota_{X_H}\omega=dH,
\]
the nondegeneracy of \(\omega\) determines a unique [[fiber-bundles/vector-field|vector field]] \(X_H\), called the [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] of \(H\). The corresponding [[differential-geometry/hamiltonian-system|Hamiltonian system]] is the differential equation \(\dot{\gamma}(t)=X_H(\gamma(t))\). Thus \(H\) is the scalar function, not the vector field or its flow. Two Hamiltonians differing by a locally constant function generate the same vector field; the converse also holds.

## Generated dynamics

Cartan's formula gives \(\mathcal{L}_{X_H}\omega=0\), so every local flow map of \(X_H\) preserves the symplectic form. Moreover,
\[
\frac{d}{dt}H(\gamma(t))=dH(X_H)=\omega(X_H,X_H)=0,
\]
and hence \(H\) is constant along its own trajectories. These conclusions use only the defining equation and the closedness and skew-symmetry of \(\omega\).

## Examples and scope

On \(\mathbb{R}^{2n}\) with coordinates \((q_i,p_i)\) and \(\omega=\sum_i dq_i\wedge dp_i\), the defining equation yields
\[
X_H=\sum_i\left(\frac{\partial H}{\partial p_i}\frac{\partial}{\partial q_i}
-\frac{\partial H}{\partial q_i}\frac{\partial}{\partial p_i}\right).
\]
A constant Hamiltonian generates the zero vector field. A vector field preserving \(\omega\) need not be globally Hamiltonian: \(\iota_X\omega\) must be exact, not merely closed.

## Conventions

**Warning.** Some authors define \(X_H\) by \(\iota_{X_H}\omega=-dH\). That choice reverses the displayed coordinate formula and changes related Poisson-bracket signs. The convention must therefore be fixed before comparing formulas.

## References

1. V. I. Arnol'd, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: Chapter 8.
2. R. Abraham and J. E. Marsden, *Foundations of Mechanics*, 2nd ed., AMS Chelsea, 2008. [DOI record](https://doi.org/10.1090/chel/364). Relevant: §3.3.
