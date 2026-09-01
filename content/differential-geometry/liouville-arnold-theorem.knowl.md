+++
id = "differential-geometry/liouville-arnold-theorem"
title = "Liouville–Arnold theorem"
kind = "theorem"
summary = "A compact connected regular fiber of a completely integrable Hamiltonian system is a torus with local action-angle coordinates."
aliases = ["action-angle theorem"]
domains = ["differential-geometry", "classical-mechanics"]
prerequisites = ["differential-geometry/symplectic-manifold", "topology/connected-component", "differential-geometry/regular-level-set", "differential-geometry/action-angle-coordinates"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,\omega)\) be a \(2n\)-dimensional [[differential-geometry/symplectic-manifold|symplectic manifold]], and let \(F=(F_1,\ldots,F_n):M\to\mathbb R^n\) have pairwise commuting components whose differentials are independent along \(F^{-1}(c)\). If \(\Lambda\) is a compact [[topology/connected-component|connected component]] of this [[differential-geometry/regular-level-set|regular fiber]], the **Liouville–Arnold theorem** states that \(\Lambda\) is diffeomorphic to \(\mathbb T^n\) and has a saturated neighborhood carrying [[differential-geometry/action-angle-coordinates|action-angle coordinates]]. In those coordinates the fibers of \(F\) are the tori \(I=\mathrm{constant}\), and every Hamiltonian commuting with all \(F_j\) depends only on the actions. Consequently, its flow is linear on each such torus.

## Why a torus appears

The [[differential-geometry/functions-in-involution|involution]] relations make the [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector fields]] \(X_{F_1},\ldots,X_{F_n}\) commute. Regularity makes them linearly independent and tangent to \(\Lambda\), so their flows define a locally free \(\mathbb R^n\)-action on the fiber. Compactness forces the stabilizer to be a full lattice; hence \(\Lambda\cong\mathbb R^n/\mathbb Z^n\). Period integrals then produce action variables, while the commuting flows provide angles.

## Consequences

Each regular compact fiber is a [[differential-geometry/lagrangian-submanifold|Lagrangian submanifold]]. For \(H=H(I)\), [[differential-geometry/hamiltons-equations|Hamilton's equations]] reduce to
\[
\dot I=0,\qquad \dot\theta=\nabla_IH,
\]
so the dynamics is periodic when the frequency vector has rationally related components and quasiperiodic otherwise. The theorem therefore converts the local dynamics near a regular invariant torus into constant-velocity motion.

## Hypotheses and global scope

Independence of the differentials and pairwise Poisson commutation are both essential. Compactness cannot simply be omitted: a regular invariant level may instead be a cylinder or another quotient of \(\mathbb R^n\). The resulting coordinates are local around one regular fiber. A family of such local charts need not glue globally; period-lattice monodromy is a standard obstruction.

## References

1. V. I. Arnol'd, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. [DOI record](https://doi.org/10.1007/978-1-4757-1693-1). Relevant: Chapter 10, the Liouville theorem and action-angle variables.
2. J. J. Duistermaat, “On global action-angle coordinates,” *Communications on Pure and Applied Mathematics* 33 (1980), 687–706. [DOI record](https://doi.org/10.1002/cpa.3160330602). Relevant: §§1–3, local theorem and global obstructions.
