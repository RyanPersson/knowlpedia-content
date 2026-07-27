+++
id = "fiber-bundles/irreducible-connection"
title = "Irreducible connection"
kind = "definition"
summary = "A connection whose stabilizer under the full gauge group is exactly the unavoidable central subgroup."
aliases = ["irreducible gauge field", "connection with central stabilizer"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] over a connected manifold, with compact structure group \(G\), and let \(A\) be a [[fiber-bundles/principal-connection|connection]]. Relative to the full [[fiber-bundles/gauge-group|gauge group]], \(A\) is **irreducible** if its [[fiber-bundles/stabilizer-of-a-connection|stabilizer]] consists exactly of the constant gauge transformations induced by the center:
\[
\operatorname{Stab}(A)=Z(G).
\]
Thus \(A\) has no gauge symmetries beyond those that fix every connection. If the stabilizer strictly contains \(Z(G)\), the connection is [[fiber-bundles/reducible-connection|reducible]]. This convention is designed for nonabelian [[fiber-bundles/gauge-theory|gauge theory]] and depends on the chosen gauge group.

## Holonomy characterization

Evaluation at a point identifies \(\operatorname{Stab}(A)\) with the [[algebra-groups/centralizer|centralizer]] of the [[fiber-bundles/holonomy-group|holonomy group]] of \(A\). Consequently,
\[
A\text{ is irreducible}
\quad\Longleftrightarrow\quad
C_G(\operatorname{Hol}(A))=Z(G).
\]
For a [[fiber-bundles/hermitian-connection|unitary connection]] on a Hermitian vector bundle, a nontrivial parallel orthogonal splitting produces noncentral stabilizing endomorphisms and hence reducibility. Under the standard compactness hypotheses, absence of such a parallel splitting is the corresponding irreducibility criterion.

## Role in moduli spaces

Irreducible connections form the locus of minimal isotropy for the gauge action. After dividing out the central subgroup, the action is free there; combined with an analytic gauge slice, this makes gauge quotients locally manifold-like. Reducible connections instead produce singular or stratified points. This role is treated in [Freed–Uhlenbeck, Chapter 3](https://doi.org/10.1007/978-1-4613-9703-8) and [Donaldson–Kronheimer, §4.2](https://doi.org/10.1093/oso/9780198535539.001.0001).

## Examples and conventions

For an \(SU(2)\)-connection, the unavoidable stabilizer is \(\{\pm I\}\); a connection with exactly this stabilizer is irreducible. A flat connection with trivial holonomy is reducible because every constant \(G\)-transformation stabilizes it.

A [[fiber-bundles/based-gauge-group|based gauge group]] removes constant central transformations, so the equivalent condition becomes trivial stabilizer. For abelian \(G\), one has \(Z(G)=G\), and the full-gauge-group convention labels every connection irreducible; the terminology is therefore usually reserved for nonabelian settings.

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [Publisher record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 3, stabilizers and irreducible connections.
2. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [Publisher record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §4.2, gauge-group actions and irreducibility.
