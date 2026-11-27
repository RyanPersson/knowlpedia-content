+++
id = "proofs/grh/upper-elementary-divisors/origin-functions"
title = "Restriction to edges and functions depending only on the origin"
kind = "definition"
summary = "The matrix sending integral functions on origins to functions on edges with values in halfway lattices, and the saturated module of functions on edges that come from the origins."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.edgeRestriction", "New.FrobeniusCycle.originFunctions", "New.FrobeniusCycle.edgeRestriction_mulVec_apply", "New.FrobeniusCycle.transpose_edgeRestriction_mulVec"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Edges.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\). Let \(X\) be a finite set of **origins**, \(E\) a set of **edges**, \(\operatorname{src}\colon E\to X\) a map and \(g\colon E\to\mathrm{GL}_k(W)\) a family of matrices (\(g_e\) passes to a basis adapted to the edge \(e\)). Write \(\mathcal{E}=\mathcal{E}(N,k,n)\).

- The **restriction to edges** is the \(O\)-linear map \(\mathrm{Res}\colon O^{X\times\mathcal{E}}\to O^{E\times\mathcal{E}}\),
\[
(\mathrm{Res}\,\varphi)(e,\cdot)=\Delta_r\,\rho_n(g_e)\,\varphi(\operatorname{src}e,\cdot),
\]
with \(\Delta_r\) the [[proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices|depth scaling]]: the vector of normalised coefficients of the translate by \(g_e\) of the value of \(\varphi\) at the origin of \(e\).
- The module of **origin functions** is the \(w\)-power saturation of the image of \(\mathrm{Res}\): \(\mathcal{O}=\{\psi\in O^{E\times\mathcal{E}}:\ w^{m}\psi\in\operatorname{im}\mathrm{Res}\text{ for some }m\ge0\}\), an \(O\)-submodule. When \(w\) is not a zero divisor of \(O\) (the geometric case) these are the functions on edges, with values in the halfway lattices, that become restrictions of functions on origins after inverting \(w\), i.e. that depend only on the origin. For \(w=0\) the definition gives all of \(O^{E\times\mathcal{E}}\) and has no such interpretation.

## Remarks

For finite \(E\), the transpose is \(({}^t\mathrm{Res}\,\psi)(x,\cdot)=\sum_{e:\operatorname{src}e=x}{}^t(\Delta_r\rho_n(g_e))\,\psi(e,\cdot)\).

## References

1. Lean: `New.FrobeniusCycle.edgeRestriction`, `New.FrobeniusCycle.originFunctions`, `New.FrobeniusCycle.edgeRestriction_mulVec_apply`, `New.FrobeniusCycle.transpose_edgeRestriction_mulVec` in `src/New/UpperBound/ElementaryDivisors/Edges.lean`.
