+++
id = "fiber-bundles/gauge-theory"
title = "Gauge theory"
kind = "definition"
summary = "A field theory whose configurations carry local symmetries represented geometrically by gauge transformations."
aliases = ["classical gauge theory", "geometric gauge theory"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

A **classical geometric gauge theory** on a manifold \(M\) specifies a [[fiber-bundles/principal-g-bundle|principal bundle]] \(P\to M\), a configuration space containing [[fiber-bundles/principal-connection|principal connections]] on \(P\) and possibly additional matter fields, and an action of the [[fiber-bundles/gauge-group|gauge group]] \(\mathcal G(P)\). Its equations, action functional, and observables are required to be invariant under this action. Configurations related by a [[fiber-bundles/gauge-transformation|gauge transformation]] represent the same physical or geometric state, so solutions are studied through their gauge-equivalence classes. This definition describes the classical bundle-theoretic framework; a particular gauge theory also fixes the structure group, field content, functional, boundary conditions, and regularity class.

## Geometric structure

A connection is the gauge potential, while its [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature]] is the corresponding field strength. Matter fields are commonly sections of bundles associated to \(P\), and a connection on \(P\) induces covariant derivatives on those bundles. Gauge transformations act simultaneously on the connection and matter fields, preserving the theory's geometric constructions.

The quotient of the solution set by \(\mathcal G(P)\) is a moduli space. It need not be a smooth manifold: reducible configurations have nontrivial stabilizers, and nonlinear equations can produce singularities.

## Yang–Mills example

Given a Riemannian metric on \(M\) and an invariant inner product on the Lie algebra of a compact structure group, the Yang–Mills functional is
\[
\operatorname{YM}(A)=\frac12\int_M \langle F_A,F_A\rangle\,\mathrm{vol}_M.
\]
Its critical points are [[fiber-bundles/yangmills-connection|Yang–Mills connections]]. The functional is gauge invariant because curvature transforms by the adjoint action and the inner product is invariant. Coupling sections of associated bundles to \(A\) produces standard gauge–matter systems.

## Conventions and scope

The word “gauge theory” covers more than Yang–Mills theory. Topological gauge theories, theories with higher-form gauge fields, and discrete gauge theories can require different geometric models.

**Warning.** Choosing a [[fiber-bundles/gauge-fixing-condition|gauge-fixing condition]] is an analytical technique for representing gauge orbits; it is not part of the invariant definition of the classical theory. Quantization introduces additional structures and is not implied by the classical definition above.

## References

1. M. J. D. Hamilton, *Mathematical Gauge Theory: With Applications to the Standard Model of Particle Physics*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-68439-0). Relevant: principal bundles, connections, gauge transformations, and Yang–Mills theory.
2. J. C. Baez and J. P. Muniain, *Gauge Fields, Knots and Gravity*, World Scientific, 1994. [DOI record](https://doi.org/10.1142/2324). Relevant: chapter 2, the bundle-theoretic formulation of gauge fields.
