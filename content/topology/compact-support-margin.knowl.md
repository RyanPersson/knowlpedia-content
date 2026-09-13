+++
id = "topology/compact-support-margin"
title = "Positive margin around a compact subset of an open set"
kind = "theorem"
summary = "A compact subset of a Euclidean open set has a uniform positive distance from the complement."
aliases = ["support margin"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/compact-set", "topology/open-set", "convex-analysis/distance-function-to-a-set", "topology/continuous-attains-max-min-compact"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If \(K\subset U\subseteq\mathbb R^n\), with \(K\) nonempty and compact and \(U\) open, then some \(\delta>0\) satisfies
\[
\{x:\operatorname{dist}(x,K)<\delta\}\subset U.
\]
If \(U\ne\mathbb R^n\), equivalently
\[
\inf_{x\in K}\operatorname{dist}(x,\mathbb R^n\setminus U)>0.
\]
This is a **positive support margin**.

## Proof

The [[convex-analysis/distance-function-to-a-set|distance to the closed complement]] is continuous and strictly positive on \(K\). It attains a positive minimum by compactness. Any smaller positive number is a suitable \(\delta\). If \(U=\mathbb R^n\), every \(\delta>0\) works. Empty \(K\) causes no constraint.

## Use in localization

Margins leave room for a cutoff to transition from one to zero before reaching a boundary. They also allow small translations or mollifications of compactly supported functions while keeping their supports in \(U\).
