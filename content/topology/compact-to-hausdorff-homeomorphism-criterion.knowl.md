+++
id = "topology/compact-to-hausdorff-homeomorphism-criterion"
title = "Compact-to-Hausdorff homeomorphism criterion"
kind = "knowl"
summary = "A continuous bijection from a compact space to a Hausdorff space is a homeomorphism."
aliases = ["compact-to-hausdorff-homeomorphism-criterion", "Compact-to-Hausdorff homeomorphism criterion"]
domains = ["topology"]
legacy_source_path = "topology/compact-to-hausdorff-homeomorphism-criterion.md"
prerequisites = ["topology/compact-set", "topology/hausdorff-space", "topology/homeomorphism", "topology/closed-subset-of-compact-set-is-compact", "topology/continuous-image-of-compact-set-is-compact", "topology/compact-subset-of-hausdorff-is-closed"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

**Compact-to-Hausdorff homeomorphism criterion.** Let \(f:X\to Y\) be a [[topology/continuous-map|continuous]] [[shared-foundations/bijective-function|bijection]]. If \(X\) is [[topology/compact-set|compact]] and \(Y\) is [[topology/hausdorff-space|Hausdorff]], then \(f\) is a [[topology/homeomorphism|homeomorphism]].

## Proof

Indeed, every [[topology/closed-subset-of-compact-set-is-compact|closed subset of \(X\) is compact]], its [[topology/continuous-image-of-compact-set-is-compact|image under \(f\) is compact]], and [[topology/compact-subset-of-hausdorff-is-closed|compact subsets of \(Y\) are closed]]. Thus \(f\) is a closed map, so \(f^{-1}\) is continuous.

## Metric spaces

In particular, the criterion applies to a continuous bijection from a compact metric space to any metric space.
