+++
id = "differential-geometry/hamiltonian-vector-field"
title = "Hamiltonian vector field"
kind = "definition"
summary = "The vector field obtained from the differential of a Hamiltonian function through a symplectic form."
aliases = ["Hamiltonian field"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/hamiltonian-function", "fiber-bundles/vector-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]] and let \(H:M\to\mathbb R\) be a [[differential-geometry/hamiltonian-function|Hamiltonian function]]. The **Hamiltonian vector field** of \(H\) is the unique smooth [[fiber-bundles/vector-field|vector field]] \(X_H\) satisfying
\[
\iota_{X_H}\omega=dH.
\]
Existence and uniqueness follow pointwise from the nondegeneracy of \(\omega\), which identifies tangent vectors with covectors. This knowl fixes the plus-sign convention in the displayed equation. The vector field \(X_H\), rather than the scalar function \(H\), supplies the first-order differential equation for the associated dynamics.

## Basic properties

Cartan's formula and \(d\omega=0\) give
\[
\mathcal L_{X_H}\omega=d(\iota_{X_H}\omega)=d^2H=0,
\]
so \(X_H\) is a [[differential-geometry/symplectic-vector-field|symplectic vector field]]. Also \(dH(X_H)=\omega(X_H,X_H)=0\), and hence \(H\) is constant along integral curves of \(X_H\). The assignment \(H\mapsto X_H\) is real-linear, and its kernel consists of functions that are locally constant.

## Coordinate form and a near miss

In Darboux coordinates with \(\omega=\sum_i dq_i\wedge dp_i\),
\[
X_H=\sum_i\left(
\frac{\partial H}{\partial p_i}\frac{\partial}{\partial q_i}
-\frac{\partial H}{\partial q_i}\frac{\partial}{\partial p_i}
\right).
\]
Every Hamiltonian vector field preserves \(\omega\), but the converse can fail globally. On the symplectic torus, contraction of a constant translation field with \(\omega\) can be a closed nonexact \(1\)-form, so no globally defined \(H\) produces that field.

## Conventions

**Warning.** Some authors define \(\iota_{X_H}\omega=-dH\). Changing that sign reverses \(X_H\) and changes the related coordinate and Poisson-bracket formulas. The plus-sign convention here agrees with  and with Cannas da Silva.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Springer, 2008. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Lecture 18.1, Definition 18.1 and the preservation calculation.
2. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., AMS Chelsea, 2008. [DOI record](https://doi.org/10.1090/chel/364). Relevant: §3.3.
