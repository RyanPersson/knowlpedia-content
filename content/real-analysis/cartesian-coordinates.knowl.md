+++
id = "real-analysis/cartesian-coordinates"
title = "Cartesian coordinates"
kind = "definition"
summary = "Coordinates relative to a fixed orthonormal basis and an origin in Euclidean space."
aliases = ["Cartesian", "rectangular coordinates"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-space", "linear-algebra/orthonormal-basis"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Choose an origin \(o\) and an [[linear-algebra/orthonormal-basis|orthonormal basis]] \((e_1,\ldots,e_n)\) in Euclidean space. The **Cartesian coordinates** of a point are the unique real numbers satisfying
\[
x=o+\sum_{i=1}^n x_i e_i.
\]
The basis vectors are constant as the point varies. Hence differentiating a vector-valued function in these coordinates differentiates only its component functions.

## Comparison with a moving basis

For \(u(q)=\sum_i u_i(q)e_i(q)\) in a moving basis, the product rule instead gives
\(\partial_j u=\sum_i(\partial_j u_i)e_i+u_i\partial_j e_i\).
Those extra terms are essential in [[real-analysis/cylindrical-coordinates|cylindrical coordinates]]. Cartesian components also provide a direct way to check smoothness at points where another coordinate system degenerates.
