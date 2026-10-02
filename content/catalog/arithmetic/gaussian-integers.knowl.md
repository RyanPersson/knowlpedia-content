+++
id = "catalog/arithmetic/gaussian-integers"
title = "Gaussian integers"
kind = "definition"
summary = "Gaussian integers with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["catalog/arithmetic/qi"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **gaussian integers** form the subring \(\mathbb Z[i]=\{a+bi:a,b\in\mathbb Z\}\) of [[catalog/arithmetic/qi|its quadratic rational field]], with multiplication determined by \(i^2=-1\).

## Arithmetic

Its units are \(1,-1,i,-i\). The norm \(a+bi\mapsto a^2+b^2\) is integral and multiplicative.

## Category distinction

Its additive group is a free abelian group of rank two. It is a ring and an integral lattice, but it is not a rational vector space: division by every nonzero integer does not stay in the ring. Tensoring with \(\mathbb Q\) gives the associated quadratic field.

## References

1. [J. S. Milne, Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 2, Example 2.41, p. 39: integral bases in quadratic fields.
