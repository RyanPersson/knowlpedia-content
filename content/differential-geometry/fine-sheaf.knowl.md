+++
id = "differential-geometry/fine-sheaf"
title = "Fine sheaf"
kind = "definition"
summary = "A sheaf admitting endomorphism-valued partitions of unity subordinate to locally finite open covers."
aliases = ["fine module sheaf"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/sheaf", "algebra-groups/abelian-group", "topology/topological-space", "topology/open-cover", "algebraic-geometry-foundations/stalk"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathcal F\) be a [[algebraic-geometry-foundations/sheaf|sheaf]] of [[algebra-groups/abelian-group|abelian groups]] on a [[topology/topological-space|topological space]] \(X\). It is **fine** if, for every locally finite [[topology/open-cover|open cover]] \((U_i)_{i\in I}\), there are sheaf endomorphisms \(h_i:\mathcal F\to\mathcal F\) such that the family \((h_i)\) is locally finite,
\[
\sum_{i\in I}h_i=\operatorname{id}_{\mathcal F},
\]
and the support of \(h_i\) is contained in \(U_i\). Here the support is the closure of the set of points where the induced map on the [[algebraic-geometry-foundations/stalk|stalk]] of \(\mathcal F\) is nonzero. Thus fineness internalizes a partition of unity at the level of sheaf sections.

## Module-sheaf criterion

Let \(\mathcal A\) be a sheaf of rings that admits partitions of unity subordinate to locally finite covers. Every sheaf of \(\mathcal A\)-modules is fine: if \((\varphi_i)\) is such a partition, multiplication by \(\varphi_i\) defines the required endomorphism \(h_i\).

In particular, the [[differential-geometry/sheaf-of-smooth-functions|sheaf of smooth functions]] is fine, and every sheaf of modules over it is fine. The endomorphisms arise from multiplication by a [[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|smooth partition of unity]].

## Cohomological consequence

On a [[fiber-bundles/paracompact-topological-space|paracompact]] [[topology/hausdorff-space|Hausdorff space]], every fine sheaf is acyclic for the global-section functor: its higher sheaf cohomology groups vanish. This theorem is the sheaf-theoretic reason partitions of unity make many smooth resolutions compute cohomology. Bott and Tu use this mechanism in their treatment of de Rham theory and fine resolutions.

## Conventions and scope

**Warning.** Some references define fineness only for locally finite covers and others quantify over arbitrary covers after assuming paracompactness; the formulations then agree by refinement. Fine, soft, and flabby are distinct sheaf conditions, even though each yields acyclicity under appropriate hypotheses. Fineness depends on the topology of \(X\) and on the available endomorphisms, not only on the abstract groups of sections.

## References

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Graduate Texts in Mathematics 82, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter I, partitions of unity, fine sheaves, and the de Rham resolution.
