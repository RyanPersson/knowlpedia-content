+++
id = "fiber-bundles/gauge-fixing-condition"
title = "Gauge-fixing condition"
kind = "definition"
summary = "A supplementary condition used to choose local representatives of gauge-equivalence classes of fields."
aliases = ["gauge fixing", "choice of gauge", "local gauge condition"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/bundle-of-connections", "fiber-bundles/principal-g-bundle", "fiber-bundles/gauge-group", "fiber-bundles/corollary-conn-gauge-is-a-well-defined-orbit-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\mathcal A(P)\) be the [[fiber-bundles/bundle-of-connections|space of connections]] on a fixed [[fiber-bundles/principal-g-bundle|principal bundle]] and let the [[fiber-bundles/gauge-group|gauge group]] \(\mathcal G(P)\) act on it. A **gauge-fixing condition** on a region \(U\subseteq\mathcal A(P)\) is an auxiliary equation
\[
\chi(A)=0
\]
whose solution set is meant to provide representatives for the [[fiber-bundles/corollary-conn-gauge-is-a-well-defined-orbit-space|gauge-orbit space]]. It is effective on \(U\) when every relevant orbit has a solution. A local gauge fixing near \(A_0\) should additionally cut nearby orbits transversely and uniquely up to the stabilizer of \(A_0\). These requirements are local analytical properties; the equation alone does not assert that a global representative exists on every orbit.

## Local slices and analytical role

After completing the configuration and gauge spaces in suitable Sobolev norms, a successful gauge condition often defines a local slice for the gauge action. Near a reference connection \(A_0\), the Coulomb condition has the form
\[
d_{A_0}^{*}(A-A_0)=0.
\]
For compact structure group and the regularity hypotheses used in [[fiber-bundles/gauge-theory|gauge theory]], slice theorems identify a neighborhood of an orbit with [[fiber-bundles/gauge-transformation|gauge transformations]] applied to such a slice. Stabilizers must still be retained, so the local quotient can have orbifold-like or more singular behavior.

Gauge fixing is therefore an analytical device for studying equations and quotients, not an additional physical field equation. It can make an underdetermined gauge-invariant system elliptic or otherwise suitable for local analysis.

## Examples

The Coulomb condition \(d^{*}A=0\) for an abelian connection removes the exact part of \(A\) locally, while harmonic forms and constant gauge transformations can remain as residual data.

Temporal gauge sets the component of a connection along a chosen time direction to zero. It can often be imposed along an interval by solving an ordinary differential equation, but global topology or periodic time may obstruct a single global choice.

## Residual symmetry and global obstructions

Even when every nearby orbit meets a local slice, an orbit can meet the same condition more than once. Such multiple representatives are often called Gribov copies. Conversely, some orbits may fail to meet a proposed global condition. Thus local slice results do not produce a global section of the orbit projection in general.

**Warning.** A gauge condition, a local slice, and a global gauge choice are different strengths of assertion. Uniqueness should always be stated modulo the stabilizer or other residual gauge transformations.

## References

1. D. S. Freed and K. K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: chapter 3, gauge-group actions and local slices.
2. M. J. D. Hamilton, *Mathematical Gauge Theory: With Applications to the Standard Model of Particle Physics*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-68439-0). Relevant: gauge transformations, gauge conditions, and Yang–Mills equations.
