+++
id = "fiber-bundles/irreducible-connection"
title = "Irreducible connection"
kind = "definition"
summary = "A connection whose stabilizer under the full gauge group is exactly the unavoidable central subgroup."
aliases = ["irreducible gauge field", "connection with central stabilizer"]
domains = ["fiber-bundles"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection", "fiber-bundles/gauge-group", "fiber-bundles/stabilizer-of-a-connection", "fiber-bundles/gauge-transformation", "algebra-groups/center-of-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] over a connected manifold, with compact structure group \(G\), and let \(A\) be a [[fiber-bundles/principal-connection|connection]]. Relative to the full [[fiber-bundles/gauge-group|gauge group]], \(A\) is **irreducible** if its [[fiber-bundles/stabilizer-of-a-connection|stabilizer]] consists exactly of the constant [[fiber-bundles/gauge-transformation|gauge transformations]] induced by the center:
\[
\operatorname{Stab}(A)=Z(G).
\]
Thus \(A\) has no stabilizing gauge transformations beyond this central subgroup. ## Reducibility

If the stabilizer strictly contains \(Z(G)\), the connection is [[fiber-bundles/reducible-connection|reducible]]. This convention is designed for nonabelian [[fiber-bundles/gauge-theory|gauge theory]] and depends on the chosen gauge group.

## Holonomy characterization

Evaluation at a point identifies \(\operatorname{Stab}(A)\) with the [[algebra-groups/centralizer|centralizer]] of the [[fiber-bundles/holonomy-group|holonomy group]] of \(A\). Consequently,
\[
A\text{ is irreducible}
\quad\Longleftrightarrow\quad
C_G(\operatorname{Hol}(A))=Z(G).
\]
For a [[fiber-bundles/hermitian-connection|unitary connection]] on a Hermitian [[fiber-bundles/vector-bundle|vector bundle]], a nontrivial parallel orthogonal splitting produces noncentral stabilizing endomorphisms and hence reducibility. Under the standard compactness hypotheses, absence of such a parallel splitting is the corresponding irreducibility criterion.

## Role in moduli spaces

Irreducible connections form the locus of minimal isotropy for the gauge action. After dividing out the central subgroup, the action is free there; combined with an analytic gauge slice, this makes gauge quotients locally manifold-like. [[fiber-bundles/reducible-connection|Reducible connections]] retain additional isotropy and can produce singular strata; isotropy alone does not force the coarse quotient to be singular.

## Examples and conventions

For an \(SU(2)\)-connection, the unavoidable stabilizer is \(\{\pm I\}\); a connection with exactly this stabilizer is irreducible. For nonabelian \(G\), a flat connection with trivial holonomy is reducible: parallel trivialization identifies its stabilizer with \(G\), which strictly contains \(Z(G)\).

The quotient group \(\mathcal G(P)/Z(G)\) has trivial stabilizer exactly at irreducible connections. By contrast, a [[fiber-bundles/based-gauge-group|based gauge group]] has trivial stabilizer at every connection on a connected base: a parallel gauge transformation equal to the identity at one point is the identity everywhere. Based freeness therefore does not detect irreducibility. For abelian \(G\), one has \(Z(G)=G\), and the full-gauge-group convention labels every connection irreducible; the terminology is therefore usually reserved for nonabelian settings.

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [Publisher record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 3, stabilizers and irreducible connections.
2. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [Publisher record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §4.2, gauge-group actions and irreducibility.

3. Ralph L. Cohen, *The Topology of Fiber Bundles*, Chapter 2, §3, Theorem 2.18 and its proof, pp. 61–62. [Author-hosted notes](https://math.stanford.edu/~ralph/fiber.pdf).
