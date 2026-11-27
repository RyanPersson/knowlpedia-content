+++
id = "proofs/grh/spanning-unfolding-a/source-forms-in-bessel-coordinates"
title = "Source forms in Bessel coordinates and their dimension"
kind = "theorem"
summary = "Algebraic forms on U(X_0) of weight kw and the source level are identified with vectors indexed by classes and Bessel coordinates; their space has dimension sourceDim > 0."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.finrank_levelSpace_eq_sourceDim", "New.Filling.Fits.sourceFormCoords", "New.Filling.Fits.weylBesselEquiv", "New.Filling.Fits.exists_weylBesselEquiv", "New.Filling.Fits.weylBesselEquiv_vecMul", "New.Filling.Fits.sourceDim_eq_card_mul_finrank", "New.kroneckerPi_mulVec_prod"]
lean_files = ["src/New/Spanning/Unfolding/PoincareSeries.lean"]
proof_status = "full"
+++

**Theorem.** Let \(V\) with grading \(Y\) [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fit]] the [[?lean:New.Filling|filling data]] \(S\) over a [[?c:CM field|CM field]] \(E\), with weights \(kw=(kw_v)_v\). Let \(\mathcal W_{kw}\) be the space of the representation of \(\prod_vGL(X_0)\) of weight \(kw\), with its basis indexed by [[?lean:New.WeylIndex|Weyl indices]], on which a tuple of matrices acts by the [[?lean:New.schur|Schur matrices]]; and let \(I=\prod_vI_v\) be the set of tuples of [[?lean:New.Filling.BesselCoord|Bessel coordinates]].

1. There is a linear isomorphism \(A:\mathcal W_{kw}\to\mathbb C^{I}\) such that for all tuples \(g=(g_v)_v\) of unitary matrices on \(X_0\otimes\mathbb C\) and all \(x\in\mathcal W_{kw}\)
\[
A(x)\cdot\bigotimes_v\operatorname{rep}_v(g_v)=A\bigl(\operatorname{schur}_{kw}(g^{\top})\,x\bigr),
\]
where \(\operatorname{rep}_v\) is the unitary representation of \(U(X_0)\) carried by the [[?lean:New.BesselSystem|Bessel system]] at \(v\), acting on row vectors from the right, and \(g^{\top}=(g_v^{\top})_v\).
2. Evaluation at the class representatives followed by \(A\) in each class is a linear isomorphism (the **source form coordinates**)
\[
\{\text{algebraic forms on }U(X_0)\text{ of weight }(kw,0)\text{ and level the source level}\}\ \xrightarrow{\ \sim\ }\ \mathbb C^{\{\text{classes}\}\times I}.
\]
3. The dimension of this space of [[?c:Algebraic modular form|algebraic forms]] is the [[?lean:New.Filling.sourceDim|source dimension]] \(\#\{\text{classes}\}\cdot\lvert I\rvert\), which equals \(\#\{\text{classes}\}\cdot\dim\mathcal W_{kw}\) and is positive.

## Proof

1. At each place \(v\), the hypothesis that the Bessel system has type \((l_v,kw_v)\) provides an invertible matrix \(A_v\) intertwining \(\operatorname{rep}_v(g)\) with the transpose of the Schur matrix of \(g^{\top}\) for the weight \(kw_v\): \(A_v\operatorname{rep}_v(g)=\operatorname{schur}_{kw_v}(g^{\top})^{\top}A_v\) ([[?lean:New.Filling.IsDiscreteSeriesBessel.exists_conj_rep_eq_schur|the Bessel representation is the Schur representation]]). The Schur matrix of weight \(kw\) for a tuple is the [[?c:Kronecker product|Kronecker product]] of the local ones, after identifying a global Weyl index with a tuple of local ones, and Kronecker products are multiplicative. So the Kronecker product \(M\) of the \(A_v\) satisfies \(M\cdot\bigotimes_v\operatorname{rep}_v(g_v)=\operatorname{schur}_{kw}(g^{\top})^{\top}M\) and is invertible (with inverse the Kronecker product of the inverses); \(A(x)=x\cdot M\) has the stated property.

2. The source level is free: the rational points of \(U(X_0)\) meet each of its conjugates trivially (part of the data). Hence an algebraic form of that level is determined by its values at the class representatives, which are arbitrary vectors of \(\mathcal W_{kw}\) ([[?lean:New.freeLevelEquiv|forms of a free level]]). Composing with \(A\) in each class gives the isomorphism.

3. By 1, \(\dim\mathcal W_{kw}=\lvert I\rvert\), so the source dimension \(\#\{\text{classes}\}\cdot\lvert I\rvert\) equals \(\#\{\text{classes}\}\dim\mathcal W_{kw}\); the dimension of the space of forms is this number by the freeness of the level ([[?lean:New.finrank_levelSpace_smoothFormRep|dimension of forms of a free level]]). It is positive because there is at least one class and each \(I_v\) is nonempty.

## References

1. Lean: `New.Filling.Fits.finrank_levelSpace_eq_sourceDim` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
2. Lean: `New.Filling.Fits.sourceFormCoords` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
3. Lean: `New.Filling.Fits.weylBesselEquiv` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
4. Lean: `New.Filling.Fits.exists_weylBesselEquiv` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
5. Lean: `New.Filling.Fits.weylBesselEquiv_vecMul` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
6. Lean: `New.Filling.Fits.sourceDim_eq_card_mul_finrank` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
7. Lean: `New.kroneckerPi_mulVec_prod` in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
