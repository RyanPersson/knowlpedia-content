+++
id = "topology/compact-exhaustion"
title = "Compact exhaustion of an open Euclidean set"
kind = "definition"
summary = "An increasing sequence of compact subsets whose interiors cover the open domain."
aliases = []
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/compact-set", "topology/interior", "convex-analysis/distance-function-to-a-set", "topology/heine-borel-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **compact exhaustion** of an open set \(U\subseteq\mathbb R^n\) is a sequence of compact sets \(K_j\subset U\) with
\[
K_j\subseteq\operatorname{int}K_{j+1},\qquad
U=\bigcup_j\operatorname{int}K_j.
\]
Every compact subset of \(U\) is then contained in some \(K_j\): take a finite subcover from the increasing cover by interiors.

## Explicit construction

If \(U\ne\mathbb R^n\), one may take
\[
K_j=\{x\in\mathbb R^n:|x|\le j,\quad
\operatorname{dist}(x,\mathbb R^n\setminus U)\ge1/j\},\qquad j\ge1.
\]
These are compact by the [[topology/heine-borel-theorem|Heine–Borel theorem]] and lie inside \(U\). The strict improvement of both inequalities at the next index gives the interior inclusion. For \(U=\mathbb R^n\), closed balls of radius \(j\) suffice. Some initial sets can be empty.

## Use

An exhaustion turns local requirements into a countable sequence of estimates. In [[real-analysis/borel-jet-extension|smooth jet realization]], the \(j\)-th cutoff is chosen to control finitely many derivatives on \(K_j\).
