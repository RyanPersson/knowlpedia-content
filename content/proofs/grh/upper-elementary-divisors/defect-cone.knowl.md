+++
id = "proofs/grh/upper-elementary-divisors/defect-cone"
title = "Defect cone"
kind = "definition"
summary = "The real vectors whose defects along all simple roots at all letters are at most 0, except along one simple root where they are at most h."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.defectCone", "New.FrobeniusCycle.convex_defectCone_inter_degreeSlab"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/DefectCount.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(N\ge1\), \(a\) an index below \(k\) and \(h\in\mathbb{R}\). Extend the [[proofs/grh/upper-elementary-divisors/defect-of-monomial|defect]] to real vectors \(\beta\in\mathbb{R}^{k\times\mathbb{Z}/N}\) by \(\operatorname{def}_{i,b,b'}(\beta)=\sum_{x}\omega_{i,b,b'}(x)\beta(x)\). The **defect cone** \(\mathcal{K}(a,h)\) is the set of \(\beta\) such that for every letter \(i\) and every simple root \((b,b+1)\), \(b+1<k\),
\[
\operatorname{def}_{i,b,b+1}(\beta)\le\begin{cases}h&b=a,\\0&b\ne a.\end{cases}
\]
The condition \(\beta\ge0\) is not part of the definition; it comes with the [[proofs/grh/upper-elementary-divisors/step-map-pieri-cone-slab|degree slab]]. For every \(D\), \(\mathcal{K}(a,h)\cap\mathrm{Slab}_k(D)\) is convex (it is cut out by linear inequalities) and bounded.

For \(h=0\) these are Pieri's inequalities in other coordinates: see [[proofs/grh/upper-elementary-divisors/defect-of-steps|the defect of a vector of steps]].

## References

1. Lean: `New.FrobeniusCycle.defectCone`, `New.FrobeniusCycle.convex_defectCone_inter_degreeSlab` in `src/New/UpperBound/ElementaryDivisors/DefectCount.lean`.
