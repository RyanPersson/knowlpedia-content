+++
id = "proofs/grh/upper-elementary-divisors/hecke-operator-factors-through-edges"
title = "The edge Hecke operator factors through functions on edges"
kind = "proposition"
summary = "On vectors multiplied by the edge pairing weights, the edge Hecke operator is restriction to edges followed by the pairing with the restrictions to the dual edges."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.IsEdgePairing.edgeHeckeOperator_regroup", "New.FrobeniusCycle.IsEdgePairing.transpose_mul_diagonal_mul"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean"]
proof_status = "full"
+++

**Proposition.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\), \(\mathfrak{E}\) [[proofs/grh/upper-elementary-divisors/edge-hecke-operator|edge coordinates]] with \(X\) finite, \(\mathbb{A}\) the edge Hecke operator, and \((b,b')\) an [[proofs/grh/upper-elementary-divisors/edge-pairing|edge pairing]]. Let \(V=H\times X\) (origins) and \(\mathrm{Ed}'=H\times X\times\mathcal{B}\) (edges, with a label in \(H\)), and consider the two [[proofs/grh/upper-elementary-divisors/origin-functions|restrictions to edges]] \(O^{V\times\mathcal{E}}\to O^{\mathrm{Ed}'\times\mathcal{E}}\):

- \(\mathrm{Res}\): source \((h,x,\mathsf{b})\mapsto(h,\operatorname{or}(x,\mathsf{b}))\), matrices \(g_{(h,x,\mathsf{b})}={}^{t}o(x,\mathsf{b})\);
- \(\mathrm{Res}'\) (dual edges): source \((h,x,\mathsf{b})\mapsto(h,x)\), matrices \(g'_{(h,x,\mathsf{b})}=t(\mathsf{b})\).

Let \(\mathrm{Add}={}^{t}\mathrm{Res}'\cdot(u\boxtimes\operatorname{diag}b)\) be the [[proofs/grh/upper-elementary-divisors/pairing-map-and-near-inverse|pairing map]] for the transition matrices \(u\) and \(Q'=\mathrm{Res}'\). Then for every \(F\colon V\times\mathcal{E}\to O\), after regrouping,
\[
\mathbb{A}\bigl(b\cdot F\bigr)=\mathrm{Add}\cdot\mathrm{Res}\cdot F,
\]
where \((b\cdot F)((h,x),\beta)=b_\beta F((h,x),\beta)\).

## Proof

*Key identity.* For \(g,\gamma\in\mathrm{GL}_k(W)\), with \(\Delta=\Delta_r\) and \(\Pi=\Delta^{2}\):
\[
{}^{t}(\Delta\rho_n(\gamma))\,\operatorname{diag}(b)\,\Delta\,\rho_n({}^{t}g)={}^{t}\bigl(\rho_n(g)\,\Pi\,\rho_n(\gamma)\bigr)\operatorname{diag}(b).
\]
Indeed diagonal matrices commute, so the left side is \({}^t\rho_n(\gamma)\,\Pi\operatorname{diag}(b)\,\rho_n({}^tg)\), and the adjointness axiom of an edge pairing reads \(\operatorname{diag}(b)\rho_n({}^tg)={}^t\rho_n(g)\operatorname{diag}(b)\).

*Comparison.* Fix \(x\) and \(h\). By definition of \(\mathrm{Res}\), \((\mathrm{Res}F)((h,x,\mathsf{b}),\cdot)=\Delta\rho_n({}^to(x,\mathsf{b}))F((h,\operatorname{or}(x,\mathsf{b})),\cdot)\). Applying \(u\boxtimes\operatorname{diag}b\) gives at \((h,x,\mathsf{b})\) the vector \(\operatorname{diag}(b)\sum_{h'}u(x,\mathsf{b})_{hh'}(\mathrm{Res}F)((h',x,\mathsf{b}),\cdot)\). The edges of \(\mathrm{Res}'\) with source \((h,x)\) are the \((h,x,\mathsf{b})\), so
\[
({}^t\mathrm{Res}'\cdots)((h,x),\cdot)=\sum_{\mathsf{b}}{}^{t}\bigl(\Delta\rho_n(t(\mathsf{b}))\bigr)\operatorname{diag}(b)\sum_{h'}u(x,\mathsf{b})_{hh'}\,\Delta\rho_n({}^to(x,\mathsf{b}))F((h',\operatorname{or}(x,\mathsf{b})),\cdot).
\]
By the key identity with \(\gamma=t(\mathsf{b})\), \(g=o(x,\mathsf{b})\), this is \(\sum_{\mathsf{b}}\sum_{h'}u(x,\mathsf{b})_{hh'}\,{}^{t}[\rho_n(o(x,\mathsf{b}))\Pi\rho_n(t(\mathsf{b}))]\,(b\cdot F)((h',\operatorname{or}(x,\mathsf{b})),\cdot)\), which is the definition of \(\mathbb{A}(b\cdot F)\) at \((x,(\cdot,h))\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.IsEdgePairing.edgeHeckeOperator_regroup`, `New.FrobeniusCycle.IsEdgePairing.transpose_mul_diagonal_mul` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
