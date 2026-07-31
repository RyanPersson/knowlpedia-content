+++
id = "fiber-bundles/reducible-connection"
title = "Reducible connection"
kind = "definition"
summary = "A connection whose gauge stabilizer is larger than the unavoidable central subgroup."
aliases = ["reducible gauge field", "connection with noncentral stabilizer"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] over a connected manifold with compact structure group \(G\), and let \(A\) be a [[fiber-bundles/principal-connection|principal connection]]. Using the full [[fiber-bundles/gauge-group|gauge group]], \(A\) is **reducible** when its [[fiber-bundles/stabilizer-of-a-connection|stabilizer]] strictly contains the subgroup of constant gauge transformations arising from the center \(Z(G)\):
\[
\operatorname{Stab}(A)\supsetneq Z(G).
\]
Equivalently, there is a [[fiber-bundles/gauge-transformation|gauge transformation]] fixed by \(A\) whose value is not central. A connection is **irreducible** in this convention when \(\operatorname{Stab}(A)=Z(G)\). The definition records extra continuous or discrete symmetry of the connection, not merely nontriviality of the center.

## Holonomy and preserved reductions

Evaluation at a point identifies the stabilizer with the [[algebra-groups/centralizer|centralizer]] of the [[fiber-bundles/holonomy-group|holonomy group]]. Thus \(A\) is reducible exactly when the holonomy has centralizer larger than \(Z(G)\); see [Freed and Uhlenbeck, Chapter 3]. For matrix groups this often means that the [[fiber-bundles/holonomy-representation|holonomy representation]] preserves a proper decomposition, so \(A\) is [[fiber-bundles/connection-compatible-with-a-reduction|compatible with a reduction]] to the corresponding [[algebra-groups/proper-subgroup|proper subgroup]].

For a [[fiber-bundles/hermitian-connection|unitary connection]] on a Hermitian [[fiber-bundles/vector-bundle|vector bundle]], a parallel orthogonal splitting into nonzero subbundles makes the connection reducible. The converse takes this form when the stabilizing element has suitable eigenspace decomposition.

## Role in gauge quotients

Reducible connections are points with nonminimal isotropy for the gauge action. Their orbits therefore produce singular or lower-dimensional strata in the quotient of the space of connections. Gauge-theoretic moduli problems often impose hypotheses excluding reducibles so that a gauge slice has a manifold-like quotient near a solution; this role is developed in [Freed and Uhlenbeck, Chapter 3].

For a nonabelian \(G\), the flat product connection with trivial holonomy is reducible because its stabilizer contains all constant \(G\)-valued transformations.

## Conventions and examples

For an \(SU(2)\)-connection on a rank-two Hermitian bundle, a preserved splitting \(E=L\oplus L^{-1}\) is the standard reducible situation. By contrast, the central transformations \(\{\pm I\}\) stabilize every \(SU(2)\)-connection and do not by themselves make it reducible.

**Warning.** Terminology changes with the chosen gauge group. A [[fiber-bundles/based-gauge-group|based gauge group]] removes constant central symmetries, and some authors call a connection reducible when the based action has nontrivial stabilizer. In abelian [[fiber-bundles/gauge-theory|gauge theory]] \(Z(G)=G\), so the nonabelian definition above does not provide a useful reducible/irreducible distinction.

## References

1. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [DOI record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §4.2, reducible connections and gauge-theoretic moduli spaces.
2. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 3, gauge actions, stabilizers, and irreducibility.
