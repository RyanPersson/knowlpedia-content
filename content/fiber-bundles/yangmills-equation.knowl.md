+++
id = "fiber-bundles/yangmills-equation"
title = "Yang–Mills equation"
kind = "knowl"
summary = "The Euler–Lagrange equation for the Yang–Mills functional, expressed as a covariant divergence-free condition on curvature."
aliases = ["yangmills-equation", "Yang–Mills equation"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/yangmills-equation.md"
+++

Let $P\to M$ be a principal $G$-bundle over an oriented Riemannian
manifold, where the Lie algebra of $G$ carries an
$\operatorname{Ad}$-invariant inner product. Let $A$ be a
[[fiber-bundles/principal-connection|principal connection]] with curvature
$F_A$.

The Euler–Lagrange equation for the
[[fiber-bundles/yangmills-functional|Yang–Mills functional]] is
$$
d_A(*F_A)=0.
$$
Here $d_A$ is the covariant exterior derivative on
$\operatorname{ad}(P)$-valued forms and $*$ is the Hodge star. A
connection satisfying this equation is a **Yang–Mills connection**.

## Examples
1. **Flat connections.** If $F_A=0$, the equation holds automatically.
2. **Abelian reduction.** For $G=U(1)$, it becomes $d(*F)=0$, the
   source-free Maxwell equation.
3. **Instantons in dimension four.** If $*F_A=\pm F_A$, the Bianchi
   identity $d_AF_A=0$ implies the Yang–Mills equation.
