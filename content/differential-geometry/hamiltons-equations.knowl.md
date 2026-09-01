+++
id = "differential-geometry/hamiltons-equations"
title = "Hamilton's equations"
kind = "theorem"
summary = "The canonical-coordinate differential equations determined by a Hamiltonian function and the standard symplectic form."
aliases = ["canonical Hamilton equations"]
domains = ["differential-geometry", "classical-mechanics"]
prerequisites = ["differential-geometry/hamiltonian-system", "differential-geometry/darboux-theorem-symplectic"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,\omega,H)\) be an [[differential-geometry/hamiltonian-system|autonomous Hamiltonian system]]. In [[differential-geometry/darboux-theorem-symplectic|Darboux coordinates]] \((q^1,\ldots,q^n,p_1,\ldots,p_n)\), where
\[
\omega=\sum_{i=1}^n dq^i\wedge dp_i,
\]
a curve \(t\mapsto(q(t),p(t))\) is a Hamiltonian trajectory if and only if it satisfies **Hamilton's equations**
\[
\dot q^i=\frac{\partial H}{\partial p_i},
\qquad
\dot p_i=-\frac{\partial H}{\partial q^i}
\]
for every \(i\). These signs correspond to the convention \(\iota_{X_H}\omega=dH\).
The equations give the local coordinate form of the intrinsic vector-field equation \(\dot\gamma=X_H\).

## Derivation

Write
\[
X_H=\sum_i\left(a^i\frac{\partial}{\partial q^i}
+b_i\frac{\partial}{\partial p_i}\right).
\]
Contracting with the Darboux form gives
\[
\iota_{X_H}\omega=\sum_i(a^i\,dp_i-b_i\,dq^i).
\]
Comparison with \(dH=\sum_i(H_{q^i}\,dq^i+H_{p_i}\,dp_i)\) yields \(a^i=H_{p_i}\) and \(b_i=-H_{q^i}\). Since trajectories satisfy \(\dot\gamma=X_H\), the coordinate equations follow.

## Examples and time dependence

For \(H(q,p)=p^2/(2m)+m\Omega^2q^2/2\), Hamilton's equations are
\[
\dot q=p/m,\qquad \dot p=-m\Omega^2q,
\]
and hence \(\ddot q+\Omega^2q=0\).

For a [[differential-geometry/time-dependent-hamiltonian-system|time-dependent Hamiltonian]] \(H(t,q,p)\), the same formulas hold with the [[real-analysis/partial-derivative|partial derivatives]] evaluated at time \(t\). The resulting evolution is nonautonomous, and \(H\) need not be conserved.

## Conventions and scope

**Warning.** Authors using \(\iota_{X_H}\omega=-dH\), or using \(\sum_i dp_i\wedge dq^i\) as the displayed standard form, obtain different intermediate signs. Hamilton's equations should be compared together with both the symplectic-form convention and the definition of \(X_H\).

## References

1. V. I. Arnol'd, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: Chapters 8–9, Hamilton's equations and time-dependent systems.
2. Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics*, 2nd ed., AMS Chelsea Publishing, 2008. [DOI record](https://doi.org/10.1090/chel/364). Relevant: §3.3, Hamiltonian systems in canonical coordinates.
