+++
id = "fiber-bundles/corollary-conn-gauge-is-a-well-defined-orbit-space"
title = "Gauge equivalence classes of connections form an orbit space"
kind = "knowl"
summary = "The space of connections modulo gauge transformations is the set of orbits for the gauge group action"
aliases = ["corollary-conn-gauge-is-a-well-defined-orbit-space", "Gauge equivalence classes of connections form an orbit space"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/corollary-conn-gauge-is-a-well-defined-orbit-space.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal $G$-bundle]], let $\operatorname{Conn}(P)$ be its set of [[fiber-bundles/principal-connection|principal connections]], and let $\mathcal G(P)$ be its [[fiber-bundles/gauge-group|gauge group]]. Pullback defines the [[fiber-bundles/proposition-gauge-group-acts-on-conn-by-pullback|right action]]
$$
\operatorname{Conn}(P)\times\mathcal G(P)\longrightarrow\operatorname{Conn}(P),
\qquad (\omega,u)\longmapsto\omega\cdot u:=u^*\omega.
$$
Its orbit relation is
$$
\omega_0 \sim \omega_1
\quad\Longleftrightarrow\quad
\exists\,u\in\mathcal G(P)\ \text{such that}\ \omega_1=u^*\omega_0.
$$
Thus the quotient
$$
\mathrm{Conn}(P)/\mathcal G(P)
$$
is the set of gauge-equivalence classes of connections.

## Local form

In a trivialization, a [[fiber-bundles/local-gauge-transformation|local gauge transformation]] $g:U\to G$ sends a [[fiber-bundles/local-connection-1-form|local connection form]] $A$ to
$$
A^g=\operatorname{Ad}_{g^{-1}}A+g^{-1}dg.
$$

## Examples
1. **Trivial bundle: gauge action on Lie algebra valued 1-forms.**
   If $P=M\times G$ is the [[fiber-bundles/trivial-principal-bundle-mgm|trivial principal bundle]], then a connection is represented by a $\mathfrak g$-valued $1$-form $A$, and the gauge group identifies with $C^\infty(M,G)$.
   $$
       A \longmapsto \operatorname{Ad}_{g^{-1}}A+g^{-1}dg.
   $$
2. **Abelian case.**
   For $G=U(1)$ on a trivial bundle, the adjoint term is $A$, so
   $$
   A \longmapsto A + g^{-1}dg.
   $$
   Locally writing $g=e^{i\theta}$ gives $g^{-1}dg=i\,d\theta$.

3. **Flat connections.**
   Gauge equivalence preserves the [[fiber-bundles/holonomy-group|holonomy]] of a flat connection up to conjugation. If $G$ is connected, gauge classes of flat connections on the trivial bundle over $S^1$ correspond to conjugacy classes in $G$.
