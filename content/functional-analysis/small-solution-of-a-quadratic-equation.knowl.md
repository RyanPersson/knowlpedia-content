+++
id = "functional-analysis/small-solution-of-a-quadratic-equation"
title = "Small solution of an invertible linear equation with quadratic error"
kind = "theorem"
summary = "A contraction estimate solves an invertible linear equation perturbed by a bounded quadratic term."
aliases = ["quadratic moment correction by contraction"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/banach-space", "functional-analysis/bounded-linear-operator", "functional-analysis/bounded-bilinear-map", "functional-analysis/contraction-on-a-closed-ball", "real-analysis/neumann-series-lemma", "linear-algebra/quadratic-map", "real-analysis/implicit-function-theorem"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(X\) be a [[linear-algebra/banach-space|Banach space]], \(B:X\to X\) a bounded invertible linear map with \(\|B^{-1}\|\le\beta\), and \(Q:X\times X\to X\) a bounded bilinear map with norm at most \(\kappa\). If
\[
8\beta^2\kappa\|d\|\le1,
\]
then \(Bc+Q(c,c)=d\) has a unique solution in the closed ball \(\|c\|\le2\beta\|d\|\).

## Contraction proof

Set \(r=2\beta\|d\|\) and \(T(c)=B^{-1}(d-Q(c,c))\). For \(\|c\|\le r\),
\[
\|T(c)\|\le\beta\|d\|+\beta\kappa r^2\le\tfrac34r.
\]
On this ball \(\|T(c)-T(c')\|\le2\beta\kappa r\|c-c'\|\le\tfrac12\|c-c'\|\). The contraction theorem applies; if \(d=0\), the radius-zero case is immediate. When \(Q=0\), no smallness restriction is needed.

## Smooth parameter families

In finite dimensions, if \(B,Q,d\) vary smoothly over compact parameters with these uniform zeroth-order bounds, the selected solution is smooth. Its Jacobian is \(B+Q(c,\cdot)+Q(\cdot,c)\), and after multiplication by \(B^{-1}\) the perturbation of the identity has norm at most \(1/2\). The implicit function theorem applies. Higher derivatives follow from implicit differentiation; smoothness does not require simultaneous smallness at every derivative order.
