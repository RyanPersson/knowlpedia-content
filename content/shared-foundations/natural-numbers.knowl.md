+++
id = "shared-foundations/natural-numbers"
title = "Natural numbers"
kind = "knowl"
summary = "The set of nonnegative integers used for counting and indexing."
aliases = ["natural-numbers", "Natural numbers"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/natural-numbers.md"
prerequisites = ["shared-foundations/set", "shared-foundations/function", "shared-foundations/subset"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

The **natural numbers** form a [[shared-foundations/set|set]] \(\mathbb N\) with an element \(0\) and a successor [[shared-foundations/function|function]] \(S:\mathbb N\to\mathbb N\) satisfying:

1. **Injectivity:** \(S(m)=S(n)\) implies \(m=n\).
2. **Zero is not a successor:** \(S(n)\ne0\) for every \(n\in\mathbb N\).
3. **Induction:** every [[shared-foundations/subset|subset]] \(A\subseteq\mathbb N\) containing \(0\) and satisfying \(S(A)\subseteq A\) equals \(\mathbb N\).

## Notation and convention

Write \(1=S(0)\), \(2=S(1)\), and so on, so that \(\mathbb N=\{0,1,2,\ldots\}\). Some authors exclude zero; in this corpus, a positive index is written explicitly as \(n\ge1\). These Peano axioms with induction over all subsets characterize the system up to isomorphism.

## Remarks


Natural numbers are used to index a [[shared-foundations/sequence|sequence]] and to formulate principles such as [[shared-foundations/mathematical-induction|mathematical induction]] and the [[shared-foundations/well-ordering-principle|well-ordering principle]]. They embed naturally into the [[shared-foundations/integers|integers]].

## Examples

- The numbers \(0,1,2,3\) belong to \(\mathbb N\).
- The set \(\{n\in\mathbb N:n\text{ is even}\}\) is an infinite subset of \(\mathbb N\).
