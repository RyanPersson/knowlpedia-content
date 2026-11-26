+++
id = "proofs/grh/upper-divisibility/hecke-operator-as-a-sum-over-edges"
title = "The Hecke operator as a sum over edges; an edge is determined by its origin"
kind = "proposition"
summary = "At a representative of a class the Hecke operator sums the rational parts of the edges into it applied to the values at their origins, and at a free level an edge is determined by its origin and the parahoric coset of its transposed change of basis."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Columns.HeckeEdges.heckeSplit_apply_rep", "New.Columns.HeckeEdges.eq_of_origin_eq_of_mem_parahoric", "New.Columns.conj_mem_localIntGL_of_transposeGL_mem_parahoric", "New.Columns.HeckeEdges.embFin_rationalPart"]
lean_files = ["src/New/UpperBound/Divisibility/HeckeEdges.lean"]
proof_status = "outline"
+++

Notation and [[proofs/grh/upper-divisibility/hecke-cosets-as-edges|edge data]] \((\rho_x,o(e),\gamma_e,u_e,g_e)\) as in the knowl on Hecke cosets as edges; assume in addition that \(K\) contains every integral element of \(G_f\) that is trivial away from \(\mathfrak l,\bar{\mathfrak l}\) (\(K\) is maximal at \(\mathfrak l\)).

**Proposition.**

1. Let \(\varphi\) be an [[?lean:New.AlgForm|algebraic form]] of weight \((\kappa,c)\) fixed by \(K\), and \(\varrho\) the weight representation of \(\Gamma\). For every class \(x\),
\[
\bigl(T_{\mathfrak l,r}\varphi\bigr)(\rho_x)=\sum_{b\in\mathrm{GL}_k(W)/\mathcal P_r}\varrho(\gamma_{(x,b)})\,\varphi\bigl(\rho_{o(x,b)}\bigr).
\]
2. Suppose moreover that \(K\) is free (\(\Gamma\cap gKg^{-1}=1\) for all \(g\)). If two edges \(e,e'\) have \(o(e)=o(e')\) and \(g_e^{T}(g_{e'}^{T})^{-1}\in\mathcal P_r\), then \(e=e'\).

## Proof

(1) \(\varphi\) is spherical at \(\mathfrak l\), and by definition \(T_{\mathfrak l,r}\varphi\) is the sum of the right translates of \(\varphi\) by representatives of the right cosets in the double coset ([[?lean:New.heckeFun_eq_sum_pullback|`heckeFun_eq_sum_pullback`]], quoted); by part 2 of the knowl on edges these are the \(\delta_{\rho_x}(\beta_b)\), one for each \(b\), when evaluating at \(\rho_x\). Hence \((T\varphi)(\rho_x)=\sum_b\varphi(\rho_x\delta_{\rho_x}(\beta_b))=\sum_b\varphi(\gamma_e\rho_{o(e)}u_e)=\sum_b\varrho(\gamma_e)\varphi(\rho_{o(e)})\), using the equivariance of \(\varphi\) under \(\Gamma\) and its invariance under \(K\).

(2) Write \(e=(x,b)\), \(e'=(x',b')\) with representatives \(\beta,\beta'\). Put \(\eta=\gamma_e\gamma_{e'}^{-1}=\beta\,\bigl(d\,g_e^{-1}g_{e'}\,d^{-1}\bigr)\beta'^{-1}\in\Gamma\). The inverse transpose preserves integrality and exchanges \(d\) and \(d^{-1}\), and the inverse transpose of \(d\,g_e^{-1}g_{e'}\,d^{-1}\) is \(d^{-1}g_e^{T}(g_{e'}^{T})^{-1}d\), which is integral at \(\mathfrak l\) by the hypothesis and part 1 of the knowl on edges. So \(\eta\) is integral at \(\mathfrak l\). Let \(y=\rho_x^{-1}\eta\rho_{x'}\) and \(u=u_{e'}^{-1}u_e\in K\). Using \(o(e)=o(e')\), the representatives of the origin cancel:
\[
yu=\delta_{\rho_x}(\beta)\cdot u^{-1}\,\delta_{\rho_{x'}}(\beta')^{-1}u ,
\]
so \(yu\) is trivial away from \(\{\mathfrak l,\bar{\mathfrak l}\}\): there the two edge steps are \(1\) and \(u^{-1}u=1\) remains. At \(\mathfrak l\) it is integral, because \(\rho_x,\rho_{x'}\) are integral above \(p\), \(\eta\) is integral at \(\mathfrak l\) and \(u\in K\). Hence \(yu\in K\) by maximality at \(\mathfrak l\), and \(y\in K\). Thus \(\eta\rho_{x'}\in\rho_xK\): the classes agree, \(x=x'\), and then \(\rho_x^{-1}\eta\rho_x\in K\) forces \(\eta=1\) by freeness. From \(\eta=1\): \(\beta^{-1}\beta'=d\,g_e^{-1}g_{e'}\,d^{-1}\), so \(d^{-1}(\beta^{-1}\beta')d=g_e^{-1}g_{e'}\) is integral, \(\beta^{-1}\beta'\in\mathcal P_r\), and \(b=b'\). \(\blacksquare\)

*Status.* In (1) the expression of a Hecke operator as a sum of translates over coset representatives is quoted.

## References

1. Lean: `New.Columns.HeckeEdges.heckeSplit_apply_rep`, `New.Columns.HeckeEdges.eq_of_origin_eq_of_mem_parahoric` in `src/New/UpperBound/Divisibility/HeckeEdges.lean`.
