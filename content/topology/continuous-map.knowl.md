+++
id = "topology/continuous-map"
title = "Continuous map"
kind = "knowl"
summary = "A function whose preimage of every open set is open."
aliases = ["continuous-map", "Continuous map"]
domains = ["topology"]
prerequisites = ["topology/topological-space", "shared-foundations/function", "topology/open-set", "shared-foundations/preimage"]
dependency_heuristic = "semantic-foundations-review-v1"
dependency_review_count = 1
legacy_source_path = "topology/continuous-map.md"
+++

A **continuous map** between [[topology/topological-space|topological spaces]] \((X,\mathcal{T}_X)\) and \((Y,\mathcal{T}_Y)\) is a [[shared-foundations/function|function]] \(f:X\to Y\) such that for every [[topology/open-set|open set]] \(V\in\mathcal{T}_Y\), the [[shared-foundations/preimage|preimage]] \(f^{-1}(V)\) is open in \(X\).

## Equivalent characterizations

Equivalently, \(f\) is continuous if the preimage of every [[topology/closed-set|closed set]] in \(Y\) is closed in \(X\).

## Remarks

In practice, continuity is often checked using a [[topology/basis-of-topology|basis]] or [[topology/subbasis-of-topology|subbasis]] of the topology on \(Y\).

## Examples

- The identity map \(\mathrm{id}_X:X\to X\) is continuous for any topological space \(X\).
- Any constant map \(f:X\to Y\) (sending all of \(X\) to a single point of \(Y\)) is continuous.
- If \(Y\subseteq X\) has the [[topology/subspace-topology|subspace topology]], the inclusion map \(i:Y\to X\) is continuous.
