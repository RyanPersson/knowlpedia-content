+++
id = "linear-algebra/dual-basis"
title = "Dual basis"
kind = "definition"
summary = "The coordinate linear functionals associated with a basis of a finite-dimensional vector space."
aliases = ["dual coordinates", "coordinate functionals"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["convex-analysis/basis-hamel-basis-and-dimension", "convex-analysis/dual-space-and-duality-pairing"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \((e_1,\ldots,e_n)\) be a [[convex-analysis/basis-hamel-basis-and-dimension|basis]] of a finite-dimensional vector space \(V\). Its **dual basis** is the family \((e^1,\ldots,e^n)\) of [[convex-analysis/dual-space-and-duality-pairing|linear functionals]] satisfying
\[
e^i(e_j)=\delta_{ij},
\]
where \(\delta_{ij}\) is one if \(i=j\) and zero otherwise. For \(v=\sum_j v_j e_j\), the functional \(e^i\) returns the coordinate \(v_i\), so
\[
v=\sum_i e^i(v)e_i.
\]

## Basis of the dual

Every linear functional \(\ell\) equals \(\sum_i\ell(e_i)e^i\). Evaluating a proposed linear relation among the \(e^i\) on each \(e_j\) shows independence. Hence the family is a basis of the [[convex-analysis/dual-space-and-duality-pairing|dual space]]. No inner product or orthogonality is required.

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
