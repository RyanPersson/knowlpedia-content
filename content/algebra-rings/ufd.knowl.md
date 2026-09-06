+++
id = "algebra-rings/ufd"
title = "Unique factorization domain"
kind = "knowl"
summary = "An integral domain where every element factors uniquely into irreducibles up to associates and order."
aliases = ["ufd", "Unique factorization domain"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ufd.md"
prerequisites = ["algebra-rings/integral-domain", "algebra-rings/irreducible-element", "algebra-rings/associated-elements"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **unique factorization domain (UFD)** is an [[algebra-rings/integral-domain|integral domain]] \(R\) such that:

1. every nonzero nonunit is a finite product of [[algebra-rings/irreducible-element|irreducible elements]]; and
2. any two such factorizations differ only by reordering the factors and replacing factors by [[algebra-rings/associated-elements|associates]].

## Remarks

In a UFD, every irreducible element is [[algebra-rings/prime-element|prime]]. If \(R\) is a UFD, then \(R[x]\) is a UFD; by iteration, so is \(R[x_1,\dots,x_n]\).

## Examples

- \(\mathbb{Z}\) is a UFD.
- If \(k\) is a field, then \(k[x,y]\) is a UFD.
- \(\mathbb{Z}[\sqrt{-5}]\) is not a UFD (e.g. \(6\) has essentially different factorizations).
