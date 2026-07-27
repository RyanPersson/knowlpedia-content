+++
id = "differential-geometry/completely-integrable-hamiltonian-system"
title = "Completely integrable Hamiltonian system"
kind = "definition"
summary = "A Hamiltonian system in dimension two n with n independent first integrals in pairwise involution."
aliases = ["Liouville integrable system"]
domains = ["differential-geometry", "classical-mechanics"]
section_mode = "progressive"
+++

Let \((M,\omega,H)\) be a [[differential-geometry/hamiltonian-system|Hamiltonian system]] with \(\dim M=2n\). It is **completely integrable in the Liouville sense** if there are smooth functions \(F_1=H,F_2,\ldots,F_n\) that are [[differential-geometry/functions-in-involution|in involution]],
\[
\{F_i,F_j\}=0\quad\text{for all }i,j,
\]
and are functionally independent on an open dense subset of \(M\), meaning \(dF_1\wedge\cdots\wedge dF_n\neq0\) there. The map \(F=(F_1,\ldots,F_n):M\to\mathbb R^n\) is the integral map. Some authors require independence only near a specified regular level, so the intended global or local convention must be stated.

## Liouville–Arnold theorem

If \(c\) is a [[fiber-bundles/regular-value|regular value]] of \(F\) and a [[topology/connected-component|connected component]] \(L\) of \(F^{-1}(c)\) is compact, then \(L\) is an \(n\)-torus. A neighborhood of \(L\) admits [[differential-geometry/action-angle-coordinates|action-angle coordinates]] \((I_1,\ldots,I_n,\theta_1,\ldots,\theta_n)\) in which
\[
\omega=\sum_i dI_i\wedge d\theta_i
\]
and \(H\) depends only on the actions. Consequently, the Hamiltonian motion is linear on each nearby invariant torus [Arnol'd, Chapter 10](https://doi.org/10.1007/978-1-4757-1693-1).

## Regular and singular fibers

At a regular point of \(F\), the commuting [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector fields]] \(X_{F_i}\) are linearly independent and span a Lagrangian distribution tangent to the common level set. Critical points of \(F\) produce singular fibers, to which the regular Liouville–Arnold normal form does not directly apply. Global action-angle coordinates may also fail even when all fibers under consideration are regular; monodromy is one obstruction [Duistermaat, §§1–3](https://doi.org/10.1002/cpa.3160330602).

## Examples and non-examples

The harmonic oscillator on \(\mathbb R^{2n}\), with the \(n\) one-dimensional oscillator energies as integrals, is completely integrable away from their singular locus. A family of \(n\) conserved quantities that satisfies a nontrivial functional relation is not enough: its differentials are dependent. Likewise, independent [[differential-geometry/first-integral|first integrals]] whose Poisson brackets do not vanish do not establish Liouville integrability.

## Conventions and scope

“Completely integrable” can refer to other notions, including noncommutative integrability or integrability by quadratures. This knowl uses Liouville integrability. The requirement \(F_1=H\) may be replaced by asking that \(H\) be a function of a complete involutive family; locally at regular points these formulations agree in the usual setup.

## References

1. V. I. Arnol'd, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: Chapter 10, complete integrability and action-angle variables.
2. J. J. Duistermaat, “On global action-angle coordinates,” *Communications on Pure and Applied Mathematics* 33 (1980), 687–706. [DOI record](https://doi.org/10.1002/cpa.3160330602). Relevant: global obstructions to action-angle coordinates.
