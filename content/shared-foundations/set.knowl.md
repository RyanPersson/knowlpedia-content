+++
id = "shared-foundations/set"
title = "Set"
kind = "knowl"
summary = "A fundamental object determined entirely by which elements it contains."
aliases = ["set"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/set.md"
prerequisites = []
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

In axiomatic set theory, **set** and the membership relation \(\in\) are primitive notions. The axiom of **extensionality** determines equality by membership: for sets \(A,B\),
\[
A=B \iff \forall x\,\bigl(x\in A \Leftrightarrow x\in B\bigr).
\]

## Axiomatic role

Extensionality is not a complete axiomatization of set theory. Other axioms specify which sets exist and how sets may be formed.

## Remarks

Many basic constructions in set theory are specified by describing their elements, such as [[shared-foundations/union|union]], [[shared-foundations/intersection|intersection]], and the [[shared-foundations/power-set|power set]].

## Examples

- The set of natural numbers \(\mathbb{N}\) (see [[shared-foundations/natural-numbers|natural numbers]]).
- For a real number \(a\), the singleton \(\{a\}=\{x : x=a\}\) is the set containing exactly the element \(a\).
