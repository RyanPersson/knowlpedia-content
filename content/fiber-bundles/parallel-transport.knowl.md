+++
id = "fiber-bundles/parallel-transport"
title = "Parallel transport for an Ehresmann connection"
kind = "knowl"
summary = "Transport along a base curve defined by taking the endpoint of its horizontal lift in the total space."
aliases = ["parallel-transport", "Parallel transport for an Ehresmann connection"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/ehresmann-connection", "fiber-bundles/horizontal-lift-of-a-curve"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
legacy_source_path = "fiber-bundles/parallel-transport.md"
+++

Let \(\pi:E\to M\) be a surjective submersion equipped with an [[fiber-bundles/ehresmann-connection|Ehresmann connection]]. For a smooth curve \(\gamma:[0,1]\to M\) and an initial point \(e_0\in E_{\gamma(0)}\), let \(\widetilde\gamma\) denote the [[fiber-bundles/horizontal-lift-of-a-curve|horizontal lift of the curve]] with \(\widetilde\gamma(0)=e_0\), defined (at least) on \([0,1]\) whenever the lift exists globally.

Let \(D_\gamma\subset E_{\gamma(0)}\) be the open set of initial points whose horizontal lifts exist throughout \([0,1]\). **Definition.** The parallel transport along \(\gamma\) is the map
\[
P_\gamma: D_\gamma \longrightarrow E_{\gamma(1)},\qquad
P_\gamma(e_0):=\widetilde\gamma(1),
\]
where \(\widetilde\gamma\) is the horizontal lift starting at \(e_0\).

For the reversed curve \(\bar\gamma(t)=\gamma(1-t)\), uniqueness of horizontal lifts gives a diffeomorphism \(P_\gamma:D_\gamma\to D_{\bar\gamma}\) with inverse \(P_{\bar\gamma}\). It is a diffeomorphism between the entire fibers when lifts exist throughout \([0,1]\) for every initial point in both directions. This holds for a complete connection. Forward existence alone need not give surjectivity. If the connection comes from a vector bundle connection, \(P_\gamma\) is linear on each fiber; if it comes from a [[fiber-bundles/principal-connection|principal connection]], it is \(G\)-equivariant.

## Examples
1. **Product bundle.** For \(E=M\times F\) with the product connection, \(P_\gamma\) is the identity map on the fiber \(F\): it sends \((\gamma(0),f)\) to \((\gamma(1),f)\).
2. **Levi-Civita transport on tangent vectors.** For the Levi-Civita connection on the tangent bundle, \(P_\gamma\) transports tangent vectors along \(\gamma\) by keeping them covariantly constant; on a sphere this produces the classical “rotation” effect around a loop.
3. **[[fiber-bundles/line-bundle|Line bundle]] with a local 1-form.** In a trivialization along \(\gamma\) where a complex line-bundle connection is \(\nabla=d+A\), parallel transport multiplies the fiber coordinate by \(\exp(-\int_\gamma A)\). For a Hermitian connection in a unitary frame, \(A\) is imaginary-valued and this multiplier is a phase. A general complex connection can also change its magnitude.

## Remarks
For a complete connection, parallel transport along loops based at \(x\in M\) generates the [[fiber-bundles/holonomy-group|holonomy group]] at \(x\), and its failure to be path-independent is governed by [[fiber-bundles/curvature|curvature]].
