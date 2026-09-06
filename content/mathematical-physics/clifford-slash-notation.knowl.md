+++
id = "mathematical-physics/clifford-slash-notation"
title = "Clifford slash notation"
kind = "definition"
summary = "Notation for Clifford multiplication by a vector or metric-dual covector."
aliases = ["Feynman slash notation", "Dirac slash notation", "slash notation"]
domains = ["mathematical-physics", "differential-geometry"]
prerequisites = ["differential-geometry/clifford-module", "mathematical-physics/gamma-matrices", "noncommutative-geometry/dirac-operator", "differential-geometry/clifford-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(c:\operatorname{Cl}(V,g)\to\operatorname{End}(\Delta)\) be a
[[differential-geometry/clifford-module|Clifford module]]. For \(v\in V\), its
**Clifford slash** is
\[
\slashed v=c(v).
\]
For a covector \(\xi\in V^*\), the metric is used to raise its index:
\[
\slashed\xi=c(\xi^\sharp).
\]
In a basis with [[mathematical-physics/gamma-matrices|gamma matrices]]
\(\gamma^a\), this is
\[
\slashed\xi=\gamma^a\xi_a.
\]

Under the convention \(c(v)^2=-g(v,v)\), slash notation satisfies
\[
\slashed\xi^{\,2}
=-g^{-1}(\xi,\xi)\operatorname{id}_\Delta.
\]
This identity is the principal-symbol calculation behind the fact that the
square of a [[noncommutative-geometry/dirac-operator|Dirac operator]] has metric quadratic principal symbol.

The musical isomorphism in the covector formula is essential: Clifford
multiplication is defined on vectors unless the [[differential-geometry/clifford-algebra|Clifford algebra]] has instead
been constructed directly from the cotangent quadratic form.

## References

1. H. Blaine Lawson Jr. and Marie-Louise Michelsohn, *Spin Geometry*,
   Princeton University Press, 1989. [DOI
   record](https://doi.org/10.1515/9781400883912). Relevant: Chapter I.
2. Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum
   Field Theory*, Addison–Wesley, 1995. Relevant: §3.1.
