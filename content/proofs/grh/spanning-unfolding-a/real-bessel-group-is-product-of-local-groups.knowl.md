+++
id = "proofs/grh/spanning-unfolding-a/real-bessel-group-is-product-of-local-groups"
title = "The real points of the Bessel group are the product of the local Bessel groups"
kind = "proposition"
summary = "For a fitting space, R(F_infinity) is isomorphic as a topological group to the product over the infinite places of the local Bessel group R, and Haar measures correspond up to a constant."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits.besselRealEquiv", "New.Filling.Fits.besselRealToPi", "New.Filling.Fits.realCoords", "New.Filling.Fits.realCoordsHomeomorph", "New.Filling.Fits.exists_integral_pi_eq", "New.Filling.Fits.besselRealToPi_surjective", "New.Filling.Fits.mem_unipotent_of_snd_eq_one", "New.Filling.Fits.adelicToInf_mem_besselU", "New.Filling.Fits.adelicToInf_mul_inv_inclX", "New.Filling.Fits.realCoords_mul_realHomeomorph", "New.unitSignEquiv"]
lean_files = ["src/New/Spanning/Unfolding/BesselFormula.lean"]
proof_status = "full"
+++

**Proposition.** Let \(V\) with grading \(Y\) [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fit]] the [[?lean:New.Filling|filling data]] \(S\) over a [[?c:CM field|CM field]] \(E\). Let \(R=U\rtimes H\) be the [[?lean:New.Grading.besselGroup|Bessel group of the grading]] (\(U\) its unipotent group, \(H=U(X_0)\) embedded by the grading), \(R(F_\infty)\) the group of its real points ([[?lean:New.Grading.besselReal|real Bessel group]]: the \(s\in G_\infty\) with \((s,1)\in R\)), and \(a(s)\in H(F_\infty)\) the [[?lean:New.Grading.leviPart|Levi part]] of \(s\). Let \(R_{\mathrm{loc}}\) be the [[?lean:New.Shape.besselGraph|local Bessel group]]: the pairs \((g,a)\in G_1\times U(\kappa)\) with \(g\,a^{-1}\in\mathsf U\) (the Bessel unipotent group of \(G_1\), \(a\) embedded in the block of \(X_0\)).

1. The map \(c:G_\infty\to\prod_vG_1\), \(s\mapsto\alpha(s,1)_\infty\) (the rescaled infinite components of the image in the adelic group of \(S\)) is a homomorphism and a homeomorphism, with \(c(s)\,\theta(y)=\theta(sy)\) for the identification \(\theta\).
2. The map
\[
R(F_\infty)\longrightarrow\prod_vR_{\mathrm{loc}},\qquad s\longmapsto\bigl(c(s)_v,\ a(s)_v\bigr)_v
\]
is an isomorphism of topological groups.
3. There is a real constant \(c_0\) such that for every function \(F\) on \(\prod_vR_{\mathrm{loc}}\), \(\int F\,d\bigl(\prod_v\mu_R\bigr)=c_0\int_{R(F_\infty)}F\bigl((c(s)_v,a(s)_v)_v\bigr)\,ds\), where \(\mu_R\) is the Haar measure \(du\,dh\) on \(R_{\mathrm{loc}}\) ([[?lean:New.Shape.besselGraphMeasure|measure of the local Bessel group]]) and \(ds\) a fixed [[harmonic-analysis/haar-measure|Haar measure]] of \(R(F_\infty)\).

## Proof

1. \(c\) is a composite of homomorphisms. From \(\theta((gg')_\infty)=\alpha(g)_\infty\theta(g'_\infty)\) we get \(c(s)\theta(y)=\theta(sy)\), hence \(c(s)=\theta(s)\theta(1)^{-1}\): \(c\) is \(\theta\) followed by a right translation, a homeomorphism.

2. *Well defined.* For \(s\in R(F_\infty)\), \((s,1)\,j_Y(a(s))^{-1}\in U\) by the definition of the Levi part; its component at \(v\) in \(G_1\) is \(c(s)_v\cdot a(s)_v^{-1}\) (block embedding of \(a(s)_v\); see the proposition on [[proofs/grh/spanning-unfolding-a/groups-of-a-graded-fitting-space|groups of a graded fitting space]]), and components of elements of \(U\) lie in \(\mathsf U\), because the diagonal rescaling keeps [[?c:Unitriangular matrix|unitriangular]] matrices unitriangular. It is a homomorphism since \(c\) and the Levi part are. *Continuity* is componentwise; it is a topological embedding because its first components are given by the embedding \(c\). *Surjectivity.* Given \((q_v)=(g_v,a_v)\), take \(s\) with \(c(s)_v=g_v\) and the real point \(a=(a_v)\) of \(H\). The finite part of \(j_Y(a,1)\) is trivial. The point \((s,1)j_Y(a,1)^{-1}\) has trivial finite part and components \(g_va_v^{-1}\in\mathsf U\) at the [[?c:Infinite place of a number field|infinite places]]; a point with trivial finite part whose infinite components lie in \(\mathsf U\) lies in \(U\) (compare entries, the rescaling factors being nonzero). Hence \((s,1)\in R\) with Levi part \(a\), and \(s\) maps to \((q_v)\).

3. The product of the Haar measures \(\mu_R\) and the image of \(ds\) under the isomorphism of 2 are two Haar measures on the same locally compact group, hence proportional ([[?c:Uniqueness of Haar measure|uniqueness of Haar measure]]).

## References

1. Lean: `New.Filling.Fits.besselRealEquiv` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
2. Lean: `New.Filling.Fits.besselRealToPi` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
3. Lean: `New.Filling.Fits.realCoords` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
4. Lean: `New.Filling.Fits.realCoordsHomeomorph` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
5. Lean: `New.Filling.Fits.exists_integral_pi_eq` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
6. Lean: `New.Filling.Fits.besselRealToPi_surjective` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
7. Lean: `New.Filling.Fits.mem_unipotent_of_snd_eq_one` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
8. Lean: `New.Filling.Fits.adelicToInf_mem_besselU` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
9. Lean: `New.Filling.Fits.adelicToInf_mul_inv_inclX` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
10. Lean: `New.Filling.Fits.realCoords_mul_realHomeomorph` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
11. Lean: `New.unitSignEquiv` in `src/New/Spanning/Unfolding/BesselFormula.lean`.
