+++
id = "differential-geometry/action-angle-coordinates"
title = "Action-angle coordinates"
kind = "definition"
summary = "Canonical coordinates adapted to invariant tori in which an integrable Hamiltonian depends only on action variables."
aliases = ["angle-action variables"]
domains = ["differential-geometry", "classical-mechanics"]
section_mode = "progressive"
+++

On an open set \(U\) of a \(2n\)-dimensional [[differential-geometry/symplectic-manifold|symplectic manifold]], **action-angle coordinates** are a diffeomorphism \(U\cong B\times\mathbb T^n\), where \(B\subset\mathbb R^n\) is open, providing variables
\[
(I_1,\ldots,I_n,\theta_1,\ldots,\theta_n)\in B\times\mathbb T^n
\]
such that \(\omega=\sum_{j=1}^n dI_j\wedge d\theta_j\) and the functions of a specified [[differential-geometry/completely-integrable-hamiltonian-system|completely integrable system]] depend only on \(I=(I_1,\ldots,I_n)\). The \(I_j\) are action variables and the circle-valued \(\theta_j\) are angle variables. In particular, if \(H=H(I)\), [[differential-geometry/hamiltons-equations|Hamilton's equations]] give \(\dot I_j=0\) and \(\dot\theta_j=\partial H/\partial I_j\), so the motion on each torus \(I=\mathrm{constant}\) is linear.

## Geometric meaning

The projection \(B\times\mathbb T^n\to B\) describes a local fibration by invariant [[differential-geometry/lagrangian-submanifold|Lagrangian]] tori. Actions may be obtained by integrating a local primitive of the symplectic form around a basis of one-cycles on each torus; changing that integral basis transforms the actions by an integral affine change. Angles then parametrize the commuting flows around the torus. [Arnol'd, Chapter 10](https://doi.org/10.1007/978-1-4757-1693-1) gives the classical construction.

## Existence and limitations

The [[differential-geometry/liouville-arnold-theorem|Liouville–Arnold theorem]] supplies action-angle coordinates near a compact connected [[differential-geometry/regular-level-set|regular fiber]] of the integral map. It is a local statement around a torus, not a guarantee of one coordinate system over the entire regular locus. Monodromy of the period lattice and the topology of the torus fibration can obstruct global action-angle coordinates [Duistermaat, §§1–3](https://doi.org/10.1002/cpa.3160330602).

## Examples and conventions

The one-dimensional harmonic oscillator admits an action proportional to its energy and an angle equal to the phase of its periodic orbit away from the equilibrium. The equilibrium itself is a singular fiber, so these angle coordinates do not extend through it. Some authors write \(\omega=\sum_j d\theta_j\wedge dI_j\); the corresponding Hamilton-equation signs change with that convention.

## References

1. V. I. Arnol'd, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: Chapter 10, action-angle variables and complete integrability.
2. J. J. Duistermaat, “On global action-angle coordinates,” *Communications on Pure and Applied Mathematics* 33 (1980), 687–706. [DOI record](https://doi.org/10.1002/cpa.3160330602). Relevant: §§1–3, local coordinates and global obstructions.
