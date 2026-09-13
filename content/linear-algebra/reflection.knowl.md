+++
id = "linear-algebra/reflection"
title = "Orthogonal reflection across a hyperplane"
kind = "definition"
summary = "The orthogonal map x -> x - 2(n dot x)n for a unit normal n."
aliases = ["reflection symmetry", "spatial reflection"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/unit-vector", "linear-algebra/inner-product", "linear-algebra/linear-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[linear-algebra/unit-vector|unit vector]] \(n\in\mathbb R^d\), the **orthogonal reflection** across the hyperplane perpendicular to \(n\) is
\[
Sx=x-2(n\cdot x)n.
\]
It fixes vectors perpendicular to \(n\), sends \(n\) to \(-n\), and satisfies \(S^2=I\) and \(|Sx|=|x|\).

## Symmetry of fields

A scalar field is reflection-invariant if \(f(Sx)=f(x)\). For a vector field the natural equivariance condition is \(u(Sx)=Su(x)\), so different components can have different parities. For reflection in \(z=0\), tangential components are even in \(z\) and the normal component is odd under this vector symmetry.

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
