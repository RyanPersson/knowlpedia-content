+++
id = "proofs/grh/upper-elementary-divisors/edge-hecke-operator"
title = "Edge coordinates and the edge Hecke operator"
kind = "definition"
summary = "Coordinates for the edges into a finite set of representatives, and the operator on vector-valued functions that sums, over the edges into a point, the values at their origins transported along the edge and scaled by p to the depth."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.EdgeCoordinates", "New.FrobeniusCycle.edgeHeckeOperator", "New.FrobeniusCycle.depthPower", "New.FrobeniusCycle.edgeHeckeOperator_apply", "New.regroup", "New.regroup_surjective", "New.EdgeCoordinates.surjective_origin_originBasisChange"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean"]
+++

Let \(W\) be a [[algebra-commutative/local-ring|local ring]], \(O\) a commutative ring, \(k,r\ge0\), and let \(\mathcal{B}=\mathrm{GL}_k(W)/\mathrm{Par}_r(W)\) be the set of [[proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices|parahoric cosets]], assumed finite. Let \(X\) be a set (of **representatives**) and \(H\) a finite set. **Edge coordinates** \(\mathfrak{E}\) for \((W,O,k,r,X,H)\) consist of maps

- \(\operatorname{or}\colon X\times\mathcal{B}\to X\) (the representative of the origin of the edge \(e=(x,\mathsf{b})\) into \(x\)),
- \(o\colon X\times\mathcal{B}\to\mathrm{GL}_k(W)\) (basis change at the origin), \(t\colon\mathcal{B}\to\mathrm{GL}_k(W)\) (basis change at the terminus),
- \(u\colon X\times\mathcal{B}\to\mathrm{GL}_H(O)\) (the **transition** matrices),

such that (i) \(t(\mathsf{b})^{-1}\) represents the coset \(\mathsf{b}\) for every \(\mathsf{b}\); (ii) if \(\operatorname{or}(e)=\operatorname{or}(e')\) and \({}^{t}o(e)\cdot({}^{t}o(e'))^{-1}\in\mathrm{Par}_r(W)\), then \(e=e'\).

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(\mathcal{E}=\mathcal{E}(N,k,n)\), and \(I\) a finite set with a bijection \(J\colon I\to\mathcal{E}\times H\). Let \(\Pi_r=\operatorname{diag}(p^{\operatorname{depth}_r\beta})_\beta=\Delta_r^{2}\). The **edge Hecke operator** is the \(O\)-linear endomorphism \(\mathbb{A}\) of the module of functions \(F\colon X\to O^{I}=O^{\mathcal{E}}\otimes O^{H}\),
\[
(\mathbb{A}F)(x)=\sum_{\mathsf{b}\in\mathcal{B}}\Bigl({}^{t}\bigl[\rho_n(o(x,\mathsf{b}))\,\Pi_r\,\rho_n(t(\mathsf{b}))\bigr]\otimes u(x,\mathsf{b})\Bigr)\,F\bigl(\operatorname{or}(x,\mathsf{b})\bigr).
\]

## Remarks

- The situation in mind (a comment in the formal source, not part of the structure): \(p\) is a uniformizer of \(W\), matrices are read over the fraction field of \(W\), and a group \(\Gamma\) acts freely with finitely many orbits on pairs of a \(W\)-lattice of rank \(k\) and a free \(O\)-module with basis \(H\); \(X\) is a set of orbit representatives with chosen bases; the origin of \(e\) is \(\delta\cdot\operatorname{or}(e)\) for one \(\delta\in\Gamma\), with \(\delta^{-1}=o(e)\operatorname{diag}(p^{-1},\dots,p^{-1},1,\dots,1)\,t(\mathsf{b})\) (\(r\) entries \(p^{-1}\)), and \(u(e)\) is the matrix of \(\delta\). The values of \(F\) are coefficients in the divided powers \(\frac{(n!)^{N}}{\beta!}x^{\beta}\), in which the substitution by \(g\) has the matrix \({}^t\rho_n(g)\).
- If \(X\) is finite, axiom (ii) implies that \(e\mapsto(\operatorname{or}(e),\ ({}^{t}o(e))^{-1}\mathrm{Par}_r)\) is injective, hence bijective, on \(X\times\mathcal{B}\): every edge from every representative occurs exactly once.
- A function \(G\colon(H\times X)\times\mathcal{E}\to O\) is regarded as a function \(X\to O^{I}\) via \(J\) ("regrouping"); this is a surjection (indeed a bijection) of modules.

## References

1. Lean: `New.EdgeCoordinates`, `New.FrobeniusCycle.edgeHeckeOperator`, `New.FrobeniusCycle.depthPower`, `New.FrobeniusCycle.edgeHeckeOperator_apply`, `New.regroup`, `New.regroup_surjective`, `New.EdgeCoordinates.surjective_origin_originBasisChange` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
