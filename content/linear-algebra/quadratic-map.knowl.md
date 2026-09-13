+++
id = "linear-algebra/quadratic-map"
title = "Quadratic map over the real numbers"
kind = "definition"
summary = "A map Q(v)=B(v,v) obtained from a symmetric bilinear map."
aliases = ["quadratic map", "quadratic nonlinearity"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["algebra-modules/bilinear-map", "linear-algebra/vector-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **quadratic map** between real [[linear-algebra/vector-space|vector spaces]] \(V,W\) is a map \(Q:V\to W\) of the form \(Q(v)=B(v,v)\), where \(B:V\times V\to W\) is symmetric and bilinear. Then
\[
Q(v+h)=Q(v)+2B(v,h)+Q(h),\qquad Q(tv)=t^2Q(v).
\]
Conversely, the associated bilinear map is recovered by polarization:
\[
B(v,w)=\tfrac12[Q(v+w)-Q(v)-Q(w)].
\]

## Linearization

For finite-dimensional spaces, or for a bounded bilinear map between normed spaces, the derivative is \(DQ(v)[h]=2B(v,h)\), and the exact remainder is \(Q(h)\). Mere degree-two homogeneity without the bilinear/polarization property is not the definition used here.

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
