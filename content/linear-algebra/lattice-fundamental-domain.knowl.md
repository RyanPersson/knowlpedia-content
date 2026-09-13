+++
id = "linear-algebra/lattice-fundamental-domain"
title = "Fundamental domain of a Euclidean lattice"
kind = "definition"
summary = "A measurable set containing one representative of each lattice translation class."
aliases = ["lattice fundamental domain", "lattice covolume"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-lattice", "shared-foundations/quotient-set", "measure-theory/lebesgue-measure", "linear-algebra/determinant", "shared-foundations/floor-function", "real-analysis/change-of-variables-formula"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

A **fundamental domain** for a [[linear-algebra/euclidean-lattice|lattice]] \(\Lambda\subset\mathbb R^n\) is a measurable set \(F\) whose translates \(F+\lambda\), \(\lambda\in\Lambda\), partition \(\mathbb R^n\). A frequently used variant allows overlaps or omissions of measure zero; the convention must be specified.

## A half-open domain

For \(\Lambda=B\mathbb Z^n\), the half-open parallelepiped \(F=B[0,1)^n\) is an exact fundamental domain. Write each component of \(B^{-1}x\) uniquely as an integer plus a number in \([0,1)\). Its volume is \(|\det B|\), called the **covolume** of \(\Lambda\). Lattice translations give a concrete realization of the quotient \(\mathbb R^n/\Lambda\).
