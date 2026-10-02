+++
id = "catalog/arithmetic/eisenstein-integers"
title = "Eisenstein integers"
kind = "definition"
summary = "Eisenstein integers with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-rings"]
section_mode = "progressive"
prerequisites = ["catalog/arithmetic/qsqrt-minus3"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **eisenstein integers** form the subring \(\mathbb Z[\omega]=\{a+b\omega:a,b\in\mathbb Z\}\) of [[catalog/arithmetic/qsqrt-minus3|its quadratic rational field]], with multiplication determined by \(\omega^2+\omega+1=0\).

## Arithmetic

Take \(\omega=(-1+\sqrt{-3})/2\). The norm \(a+b\omega\mapsto a^2-ab+b^2\) is integral and multiplicative. Its six units are \(\pm1,\pm\omega,\pm\omega^2\).

## Category distinction

Its additive group is a free abelian group of rank two. It is a ring and an integral lattice, but it is not a rational vector space: division by every nonzero integer does not stay in the ring. Tensoring with \(\mathbb Q\) gives the associated quadratic field.

## References

1. [J. S. Milne, Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 2, Example 2.41, p. 39: integral bases in quadratic fields.
