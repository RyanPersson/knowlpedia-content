+++
id = "fiber-bundles/construction-holonomy-element-from-parallel-transport-around-a-loop"
title = "Holonomy element from parallel transport around a loop"
kind = "knowl"
summary = "Definition of the holonomy element in G obtained by transporting a point around a based loop."
aliases = ["construction-holonomy-element-from-parallel-transport-around-a-loop", "Holonomy element from parallel transport around a loop"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection", "fiber-bundles/construction-parallel-transport-map-along-a-curve", "fiber-bundles/holonomy-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "fiber-bundles/construction-holonomy-element-from-parallel-transport-around-a-loop.md"
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] with [[fiber-bundles/principal-connection|principal connection]] \(\omega\). Fix \(x\in M\), \(p\in P_x\), and a piecewise smooth loop \(\gamma:[0,1]\to M\) with \(\gamma(0)=\gamma(1)=x\).

Using [[fiber-bundles/construction-parallel-transport-map-along-a-curve|parallel transport]], \(p\) is carried to another point in the same fiber:
\[
\mathrm{PT}^\omega_\gamma(p)\in P_x.
\]
Because \(P_x\) is a right \(G\)-torsor, there is a unique element \(h_\gamma(p)\in G\) such that
\[
\mathrm{PT}^\omega_\gamma(p)=p\cdot h_\gamma(p).
\]
This element is the **holonomy element** of \(\omega\) along \(\gamma\) based at \(p\).

Changing the point in the fiber conjugates the element: if \(p'=p\cdot g\), then
\[
h_\gamma(p') = g^{-1}\,h_\gamma(p)\,g.
\]
As \(\gamma\) varies over based loops, the elements \(h_\gamma(p)\) form the [[fiber-bundles/holonomy-group|holonomy group]] at \(p\). Changing \(p\) conjugates this subgroup, so its conjugacy class depends only on \(x\).

## Examples
1. If \(\omega\) is flat and \(M\) is simply connected, then \(h_\gamma(p)=e\) for all loops.
2. On the Levi-Civita connection of the round 2-sphere, transporting a tangent frame around a latitude circle yields a nontrivial rotation, giving a nontrivial holonomy element.
3. For an abelian structure group \(G\), the conjugation ambiguity disappears, so \(h_\gamma(p)\) is independent of \(p\in P_x\).
