+++
id = "fiber-bundles/g-bundle"
title = "G-bundle"
kind = "definition"
summary = "A fiber bundle with specified group-valued transition data acting on its model fiber."
aliases = ["G-bundle", "bundle with structure group", "fiber bundle with structure group"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/fiber-bundle", "topology/topological-group", "topology/continuous-group-action"]
+++

Let \(G\) be a [[topology/topological-group|topological group]] with a [[topology/continuous-group-action|continuous left action]] on a nonempty space \(F\). A **\(G\)-bundle with fiber \(F\)** is a [[fiber-bundles/fiber-bundle|fiber bundle]] \(\pi:E\to B\) equipped with local trivializations \(\Phi_i\) over an open cover \(\{U_i\}\) and continuous maps \(g_{ij}:U_i\cap U_j\to G\) such that
\[
\Phi_i\Phi_j^{-1}(b,f)=(b,g_{ij}(b)\cdot f),
\qquad g_{ii}=e,\qquad g_{ij}g_{jk}=g_{ik}
\]
on the respective overlaps. The last identity is required on every triple overlap. Here \(G\) is the [[fiber-bundles/structure-group|structure group]]. The chosen data are considered up to refinement of the cover and changes of trivializations by continuous maps \(h_i:U_i\to G\); replacing \(\Phi_i\) by \(h_i\Phi_i\) replaces \(g_{ij}\) by \(h_i g_{ij}h_j^{-1}\).

## Smooth version and examples

For a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]], a Lie group acting smoothly on \(F\), and smooth maps \(g_{ij}\) and \(h_i\), this defines a smooth \(G\)-bundle. A rank-\(n\) [[fiber-bundles/vector-bundle|vector bundle]] has structure group \(\mathrm{GL}(n,\mathbb K)\) acting on \(\mathbb K^n\).

## Principal bundles and conventions

Taking \(F=G\) with left multiplication gives a [[fiber-bundles/topological-principal-bundle|principal bundle]]: right multiplication on each local copy of \(G\) commutes with the transition maps and therefore defines a global right action. Its smooth version is a [[fiber-bundles/principal-g-bundle|principal G-bundle]]. For general \(F\), a \(G\)-bundle need not carry a global \(G\)-action on its total space.

**Terminology.** In gauge theory and algebraic geometry, “\(G\)-bundle” often abbreviates “principal \(G\)-bundle.” This knowl uses the broader structure-group meaning; principal-bundle statements link to their explicit definition.

If the action on \(F\) is not faithful, the maps \(g_{ij}\) and their cocycle identities are extra data: the underlying changes of fiber coordinates do not determine them uniquely.

## References

1. [Fiber Bundles lecture notes](https://people.math.osu.edu/carr.520/files/Lecture_Notes_P1.pdf), §1.2, pp. 6–7: fiber bundles, G-atlases, equivalent atlases, and the non-effective-action convention.
