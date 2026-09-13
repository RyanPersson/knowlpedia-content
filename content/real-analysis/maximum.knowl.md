+++
id = "real-analysis/maximum"
title = "Maximum"
kind = "knowl"
summary = "The largest element of a set of real numbers, when it exists."
aliases = ["maximum"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/maximum.md"
prerequisites = ["shared-foundations/subset", "shared-foundations/real-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

A **maximum** of a [[shared-foundations/subset|subset]] \(A\subseteq\mathbb R\) is an element \(m\in A\) such that \(x\le m\) for every \(x\in A\).

## Remarks

If a maximum exists, it is unique and equals the [[real-analysis/supremum|supremum]] of \(A\). Many sets have a supremum but no maximum (for instance, open intervals).

## Examples

- For \(A=[0,1]\), the maximum is \(1\).
- For \(A=\{2,5,3\}\), the maximum is \(5\).

## Finite sets

Every nonempty finite set of real numbers has a maximum, by induction using the larger of two numbers. The empty set has no maximum under this definition.
