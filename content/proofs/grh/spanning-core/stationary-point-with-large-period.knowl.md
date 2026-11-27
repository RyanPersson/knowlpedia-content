+++
id = "proofs/grh/spanning-core/stationary-point-with-large-period"
title = "A point of bounded length at which the Bessel period is large"
kind = "theorem"
summary = "For a steep discrete series parameter there is a point x of Bessel length at most b^(5n) at which the period of the coefficient over R is at least beta^(-20(r+k)^2) times the volume of a unit ball of R."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DiscreteSeries.IsSteep.exists_stationary_point", "New.DiscreteSeries.IsPosition.exists_mul_eq_frameCols_and_besselLength_le", "New.DiscreteSeries.besselPairHom", "New.DiscreteSeries.isProperMap_besselPairHom_fst", "New.DiscreteSeries.lowersFlag_besselPairHom", "New.DiscreteSeries.inducesOn_besselPairHom", "New.DiscreteSeries.exists_besselPairHom_fst_eq", "New.DiscreteSeries.exists_sub_one_mul_frameCols_eq", "New.DiscreteSeries.exists_sub_one_mul_definiteCols_eq", "New.DiscreteSeries.exists_besselGraph_fst_eq", "New.DiscreteSeries.mul_sqrt_mul_pow_le_pow", "New.DiscreteSeries.norm_frame_mulVec_le", "New.DiscreteSeries.initCols_eq_of_frame"]
lean_files = ["src/New/Spanning/Bessel/LargeFunction.lean"]
proof_status = "outline"
+++

**Theorem (stationary point).** Fix a shape with \(n=\varrho+1\), rank \(r\), \(k=\lvert\kappa\rvert\), a unitary sign frame \(p\) for signs \(\varepsilon\) ([[proofs/grh/spanning-core/bessel-system-of-discrete-series-type|discrete series type]]), and the group \(R\) with its measure ([[proofs/grh/spanning-core/bessel-period-group-and-average|Bessel period group]]). Split the basis indices as \(X\sqcup\{1,\dots,2n\}\) and \(\kappa\) as \(X\sqcup\{\ast\}\). Let \(l\) be a doubled parameter for \(\varepsilon\) that is [[?lean:New.DiscreteSeries.IsSteep|steep]] with bound \(B\ge1\) for this splitting (its lowest \(K\)-type has weight \(0\) on \(X\) and decreasing weights in \([-3B,-B]\) on the other coordinates, where the signs alternate), and let \(u\) be a doubled parameter for the compact group \(U(\kappa)\) whose lowest \(K\)-type has weight \(a\in\mathbb{N}\) at \(\ast\) and \(0\) on \(X\). Let both have entries of modulus \(\le L\) and [[?lean:New.HCParam.HasLargeGap|large gap with excess]] \(\mathrm{exc}\). Assume \(\beta\ge10^{12}\), \(r+k+L\le\beta\), \(10^{30}((r+k)^2\log\beta)^3\le\mathrm{exc}\), \(3B+a\le b^2\), \(8nr\le b\). Then there is \(x\in G_1\) with [[proofs/grh/spanning-core/bessel-length|Bessel length]] \(\ell(x)\le b^{5n}\) and
\[
\operatorname{vol}\{s=(g,h)\in R:\ \lVert p^{-1}x^{-1}gx\,p-1\rVert\le1\}\ \le\ \beta^{20(r+k)^2}\,\Bigl\lvert\int_Rc_l(x^{-1}gx)\,\overline{c_u(h)}\,e^{\bar\sigma(g)-\sigma(g)}\,ds\Bigr\rvert ,
\]
where \(c_l,c_u\) are the [[?lean:New.HCParam.dsCoeff|discrete series coefficients]] (read in the frame) and \(\sigma(g)\) is the sum of the entries of \(g\) just above the diagonal on the frame.

## Proof

*Outline.* The analytic content is in the appendix on discrete series (other area); this file transports it to \(G_1\).

1. (Appendix, `New.DiscreteSeries.IsSteep.exists_isStationary`.) There is a **stationary position** of \(U(X_0)\) in \(U(\varepsilon)\): independent vectors \(v_1,\dots,v_n\) whose products for \(\operatorname{diag}(\varepsilon)\) vanish except \(\langle v_n,v_n\rangle=-1\), and an isometry \(i_0\) of \(X_0\) into their orthogonal complement; moreover, with \(\mu\) the diagonal matrix of the lowest \(K\)-type weights, the vectors \(w_c=\mu^cv_1\) continue \(v_1,\dots,v_n\), have entries bounded by \(M=(3B+a)^{2n}\) for \(c\le2n-2\), and satisfy \(\langle w_c,w_{c'}\rangle=-1\) if \(c+c'=2n-2\) and \(0\) if \(c+c'<2n-2\).
2. (Witt.) The families \(p(i_0\mid v)\) and (basis of \(X_0\mid\) frame) have the same Gram matrix for \(J\) and are independent, so by [[?c:Witt's extension theorem|Witt's theorem]] (`New.witt`) some \(x\in G_1\) has \(xp\,i_0=\) inclusion of \(X_0\) and \(xp\,v=\) frame. Then the moved frame at \(x\) is \(x^{-1}f_a=p\,v_a=p\,w_{a-1}\), and the vectors \(V_c=p\,w_c\) have length \(\le\sqrt r\,M\) (as \(p\) is unitary) and the triangular duality for \(h\). By [[proofs/grh/spanning-core/bessel-length-versus-orthogonal-frame|part 3 of the comparison theorem]], \(\ell(x)\le8n\sqrt rM\le b^{5n}\) (using \(3B+a\le b^2\), \(8nr\le b\)).
3. (Transport.) The map \(s=(g,h)\mapsto(p^{-1}x^{-1}gx\,p,\ h)\) is a homomorphism \(R\to U(\varepsilon)\times U(\kappa)\) whose first component is proper (\(R\) is closed in \(G_1\times U(\kappa)\) and \(U(\kappa)\) is compact). Since \(g-1\) maps the frame into the span of \(e_1,\dots,e_\varrho\) by a strictly triangular matrix whose superdiagonal sum is \(\sigma(g)\), and acts on \(X_0\) by \(h\) modulo that span, the conjugate \(x^{-1}gx\) lowers the flag of the \(v_j\) and induces \(h\) on the image of \(i_0\); conversely every element of the position group of \(v\) arises from some \(s\in R\).
4. (Appendix, `New.DiscreteSeries.IsPosition.period_lower_bound_of_surjective`.) Under exactly these properties and the numerical hypotheses, the volume of \(\{s:\lVert p^{-1}x^{-1}gxp\rVert\le\beta+1,\ \lVert h\rVert\le\beta+1\}\) is at most \(\beta^{20(r+k)^2}\) times the modulus of the period. This set contains the unit ball of the statement (\(\lVert h\rVert=1\)).

Steps 1 and 4 are quoted from the appendix and not reproved; their statements were read only at the call sites. \(\blacksquare\)

## References

1. Lean: `New.DiscreteSeries.IsSteep.exists_stationary_point`, `New.DiscreteSeries.IsPosition.exists_mul_eq_frameCols_and_besselLength_le` in `src/New/Spanning/Bessel/LargeFunction.lean`.
