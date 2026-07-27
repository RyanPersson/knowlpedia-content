+++
id = "differential-geometry/darboux-theorem-symplectic"
title = "Darboux theorem for symplectic manifolds"
kind = "theorem"
summary = "Every symplectic form is locally equivalent to the standard constant symplectic form."
aliases = ["symplectic Darboux theorem", "Darboux local normal-form theorem"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,\omega)\) be a \(2n\)-dimensional [[differential-geometry/symplectic-manifold|symplectic manifold]] and \(x\in M\). The **Darboux theorem** states that there are [[fiber-bundles/smooth-chart-coordinate-chart|local coordinates]]
\[
(q^1,\ldots,q^n,p_1,\ldots,p_n)
\]
centered at \(x\) in which
\[
\omega=\sum_{i=1}^n dq^i\wedge dp_i.
\]
Equivalently, every point has a neighborhood [[differential-geometry/symplectomorphism|symplectomorphic]] to an open subset of the standard [[differential-geometry/symplectic-vector-space|symplectic vector space]] \(\mathbb R^{2n}\). Hence a symplectic form has no local invariants beyond dimension, although global symplectic manifolds can differ substantially.

## Proof idea

Moser's path method interpolates between \(\omega\) and its constant value at \(x\), after arranging equality along the chosen point. One solves a time-dependent contraction equation for a [[fiber-bundles/vector-field|vector field]] and integrates its local flow. The resulting isotopy pulls the interpolating forms back to the initial one; see [Cannas da Silva, §1.3](https://doi.org/10.1007/978-3-540-45330-7).

## Consequences

Every symplectic manifold is locally indistinguishable from [[differential-geometry/classical-phase-space|classical phase space]]. In particular, quantities resembling curvature cannot be extracted from a symplectic form alone. Lagrangian and Hamiltonian questions can therefore be studied in standard coordinates locally, while their global gluing and topology retain substantive information.

## Conventions and scope

The theorem concerns closed, nondegenerate \(2\)-forms. Nondegeneracy alone does not give this normal form on a neighborhood, because the Moser argument uses closedness. This result is unrelated to [[real-analysis/darboux-theorem|Darboux's theorem]] about derivatives from real analysis.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: §1.3, the Darboux theorem and Moser method.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [Publisher record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 3, local normal forms.
