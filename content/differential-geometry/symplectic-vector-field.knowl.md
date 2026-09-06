+++
id = "differential-geometry/symplectic-vector-field"
title = "Symplectic vector field"
kind = "definition"
summary = "A vector field whose local flow preserves the symplectic form."
aliases = ["locally Hamiltonian vector field"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/symplectic-manifold", "fiber-bundles/vector-field", "fiber-bundles/lie-derivative-of-a-differential-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]]. A **symplectic vector field** is a [[fiber-bundles/vector-field|smooth vector field]] \(X\) satisfying
\[
\mathcal L_X\omega=0,
\]
where \(\mathcal L_X\omega\) is the [[fiber-bundles/lie-derivative-of-a-differential-form|Lie derivative of the differential form]]. Since \(d\omega=0\), Cartan’s formula gives \(\mathcal L_X\omega=d(\iota_X\omega)\). Thus \(X\) is symplectic exactly when the one-form \(\iota_X\omega\) is closed. It is **Hamiltonian** under the convention \(\iota_X\omega=dH\) when that one-form is globally exact, a strictly stronger condition in general.

## Flow characterization

A vector field is symplectic exactly when each map in its local flow preserves \(\omega\) wherever defined. If \(X\) is complete, this yields a one-parameter group of [[differential-geometry/symplectomorphism|symplectomorphisms]].

## Closed versus exact

Every symplectic vector field is locally Hamiltonian by the [[differential-geometry/poincare-lemma|Poincaré lemma]]. It is globally Hamiltonian precisely when the de Rham cohomology class \([\iota_X\omega]\) vanishes. In particular, if the first [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology group]] of \(M\) vanishes, every symplectic vector field is Hamiltonian.

On the standard symplectic two-torus, a translation field gives a closed contraction one-form that need not be exact, hence a symplectic but non-Hamiltonian field.

## Conventions and scope

**Warning.** The sign in the Hamiltonian equation varies. This knowl uses \(\iota_{X_H}\omega=dH\), matching the convention in the existing symplectic-manifold knowl. Sources using \(\iota_{X_H}\omega=-dH\) define the same class of [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector fields]] but associate \(H\) to the opposite vector field.

## References

1. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [Publisher record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: Chapter 10, symplectic and Hamiltonian vector fields.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Hamiltonian vector fields and flows.
