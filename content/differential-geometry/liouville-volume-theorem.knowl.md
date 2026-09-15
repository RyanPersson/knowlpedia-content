+++
id = "differential-geometry/liouville-volume-theorem"
title = "Liouville theorem for Hamiltonian volume"
kind = "theorem"
summary = "A Hamiltonian flow preserves the top exterior power of the symplectic form."
aliases = ["Liouville measure in Hamiltonian mechanics"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/hamiltonian-flow", "fiber-bundles/wedge-product-of-differential-forms"]
+++

On a \(2n\)-dimensional [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\), the **Liouville volume form** is \(\omega^n/n!\), using the symplectic orientation. A Hamiltonian flow preserves this form wherever the flow is defined:
\[
(\Phi^t)^*(\omega^n/n!)=\omega^n/n!.
\]
If the flow is complete and the total volume is finite and nonzero, normalization gives an invariant probability measure.

## Reason

Hamiltonian flow preserves \(\omega\). Pullback respects wedge products, so it preserves its top exterior power. In canonical coordinates the form is the usual phase-space volume \(dq_1\,dp_1\cdots dq_n\,dp_n\).

## Energy levels

Restricting dynamics to an energy surface requires the appropriate invariant surface measure; simply restricting the ambient volume as a set measure usually gives zero. Volume preservation by itself does not imply ergodicity.
