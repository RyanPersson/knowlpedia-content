+++
id = "proofs/grh/upper-divisibility/hecke-cosets-as-edges"
title = "Cosets of a Hecke operator at a split prime as edges"
kind = "proposition"
summary = "The left cosets (modulo right multiplication by the maximal compact subgroup) in the double coset of the Hecke operator of index r at a split prime are parametrised by cosets of a parahoric subgroup; each edge has an origin class, a rational part and a change of basis."
aliases = ["Hecke edges", "edge step", "edge of a Hecke operator"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Columns.HeckeEdges", "New.Columns.nonempty_heckeEdges", "New.Columns.edgeStep", "New.Columns.ClassEdges", "New.Columns.blockScaling", "New.Columns.latticeGL", "New.Columns.localGL", "New.Columns.exists_edgeStep_eq", "New.Columns.edgeStep_mem_basicDoubleCoset", "New.Columns.edgeStep_inv_mul_mem_localIntGL_iff", "New.Columns.conj_blockScaling_mem_localIntGL_iff", "New.Columns.blockScaling_mem_basicDoubleCoset", "New.Columns.mem_parahoric_twoBlock_iff", "New.Columns.HeckeEdges.rationalPart_eq", "New.Columns.HeckeEdges.localGL_rationalPart_mem_localIntGL"]
lean_files = ["src/New/UpperBound/Divisibility/HeckeEdges.lean"]
proof_status = "outline"
+++

Let \(E\) be a [[?c:CM field|CM field]] with a CM type, \(n\) an index set with a numbering \(q\colon n\simeq\{0,\dots,k-1\}\), \(G_f\) the finite adelic unitary group of the standard hermitian space \(E^{n}\), \(\Gamma\) its rational points, and \(K\subset G_f\) a [[?lean:New.IsLevel|level]]. Let \(\mathfrak l\) be a finite place of \(E\) with \(\bar{\mathfrak l}\ne\mathfrak l\), so that the component of \(G_f\) at \(\{\mathfrak l,\bar{\mathfrak l}\}\) is \(\mathrm{GL}_n(E_{\mathfrak l})\); let \(W=\mathcal O_{E,(\mathfrak l)}\subset E\) be the valuation ring of \(\mathfrak l\), and let \(p\) be a prime number that is a uniformiser at \(\mathfrak l\). Let \(0\le r<k\) and
\[
d=\operatorname{diag}(\underbrace{p,\dots,p}_{r},1,\dots,1)\in\mathrm{GL}_n(E)
\]
(with \(p\) at the coordinates numbered below \(r\)). The Hecke operator \(T_{\mathfrak l,r}\) is the operator of the double coset \(K_{\mathfrak l}\,d\,K_{\mathfrak l}\), where \(K_{\mathfrak l}=\mathrm{GL}_n(\mathcal O_{\mathfrak l})\); a form fixed by \(K_{\mathfrak l}\) is sent to the sum of its right translates by representatives \(\delta\) of the left cosets \(\delta K_{\mathfrak l}\subset K_{\mathfrak l}dK_{\mathfrak l}\). Let \(\mathcal P_r\subset\mathrm{GL}_k(W)\) be the [[?c:Parahoric subgroup|parahoric subgroup]] for the blocks of sizes \(r\) and \(k-r\): the matrices whose entries \((i,j)\) with \(i<r\le j\) lie in the maximal ideal.

For \(g\in G_f\) and \(\beta\in\mathrm{GL}_k(W)\) the **edge step** is \(\delta_g(\beta)=g_{\mathfrak l}^{-1}\beta d\in\mathrm{GL}_n(E_{\mathfrak l})\). An **edge** is a pair \(e=(x,b)\) of a class \(x\in\Gamma\backslash G_f/K\) (its terminus) and a coset \(b\in\mathrm{GL}_k(W)/\mathcal P_r\).

**Proposition.**

1. For \(\beta\in\mathrm{GL}_k(W)\): \(d^{-1}\beta d\in\mathrm{GL}_n(\mathcal O_{\mathfrak l})\) if and only if \(\beta\in\mathcal P_r\).
2. If \(g_{\mathfrak l}\) is integral, then \(\delta_g(\beta)\) lies in the double coset of \(T_{\mathfrak l,r}\); the left cosets \(\delta_g(\beta)K_{\mathfrak l}\) and \(\delta_g(\beta')K_{\mathfrak l}\) are equal if and only if \(\beta^{-1}\beta'\in\mathcal P_r\); and if \(g\) is integral at all places above \(p\), every left coset \(zK_{\mathfrak l}\) in the double coset is \(\delta_g(\beta)K_{\mathfrak l}\) for some \(\beta\).
3. (**Edge data.**) There exist: for each class \(x\) a representative \(\rho_x\in G_f\) integral at all places above \(p\); and for each edge \(e=(x,b)\), with \(\beta\) a fixed representative of \(b\), a class \(o(e)\) (the **origin**), a rational point \(\gamma_e\in\Gamma\) (the **rational part**), an element \(u_e\in K\) and a matrix \(g_e\in\mathrm{GL}_k(W)\) (the **change of basis at the origin**) such that
\[
\rho_x\cdot\delta_{\rho_x}(\beta)=\gamma_e\,\rho_{o(e)}\,u_e,\qquad\gamma_e=\beta\,d\,g_e^{-1},
\]
where \(\delta_{\rho_x}(\beta)\) is placed at \(\mathfrak l\) (and correspondingly at \(\bar{\mathfrak l}\)) and is \(1\) elsewhere.
4. For such data, \(\gamma_e\) is integral at every place \(v\mid p\) with \(v\notin\{\mathfrak l,\bar{\mathfrak l}\}\).

## Proof

(1) \((d^{-1}\beta d)_{ij}=d_i^{-1}\beta_{ij}d_j\): the entries with \(i<r\le j\) are divided by \(p\), those with \(j<r\le i\) multiplied by \(p\), the others unchanged. So \(d^{-1}\beta d\) is integral iff \(\beta_{ij}\in pW\) for \(i<r\le j\); the same applies to \(\beta^{-1}\), and \(\mathcal P_r\) is a group.

(2) \(g_{\mathfrak l}^{-1}\beta\) is integral, so \(\delta_g(\beta)\) lies in the double coset of \(d\). \(\delta_g(\beta)K_{\mathfrak l}=\delta_g(\beta')K_{\mathfrak l}\) means \(\delta_g(\beta)^{-1}\delta_g(\beta')=d^{-1}\beta^{-1}\beta'd\in K_{\mathfrak l}\), and (1) applies. (The side matters: for \(g=1\) all \(\beta d\) lie in the single coset \(K_{\mathfrak l}d\) on the other side.) For the last claim let \(z=u_1du_2\) with \(u_i\) integral. By weak approximation above \(p\) ([[?lean:New.exists_mul_mem_integralAbove|`exists_mul_mem_integralAbove`]], quoted) there is a rational point \(\eta\in\Gamma\) such that \(\eta g u_1\) and \(d^{-1}(\eta gu_1)d\) are integral at the places above \(p\). Then \(\eta\) is integral at \(\mathfrak l\), so \(\eta=\beta_0\in\mathrm{GL}_k(W)\), and with \(\beta=\beta_0^{-1}\): \(\delta_g(\beta)^{-1}z=d^{-1}\eta g_{\mathfrak l}u_1d\,u_2\) is integral, that is \(zK_{\mathfrak l}=\delta_g(\beta)K_{\mathfrak l}\).

(3) Representatives integral above \(p\) exist ([[?lean:New.exists_reps_integralAbove|`exists_reps_integralAbove`]], quoted). The element \(\rho_x\delta_{\rho_x}(\beta)\) lies in some class \(o(e)\), which gives \(\gamma_e\) and \(u_e\). At \(\mathfrak l\) the left side is \(\beta d\), so \(\gamma_e^{-1}\beta d=(\rho_{o(e)})_{\mathfrak l}(u_e)_{\mathfrak l}\) is integral and invertible at \(\mathfrak l\); being rational, it is a matrix \(g_e\in\mathrm{GL}_k(W)\).

(4) At such \(v\) the edge step is trivial, so \(\gamma_e=(\rho_x)_v(u_e)_v^{-1}(\rho_{o(e)})_v^{-1}\) is a product of integral matrices. \(\blacksquare\)

*Status.* Weak approximation above \(p\) and the existence of representatives integral above \(p\) are quoted from other files.

## References

1. Lean: `New.Columns.nonempty_heckeEdges` and the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/HeckeEdges.lean`.
