+++
id = "proofs/grh/spanning-unfolding-a/space-fitting-filling-data"
title = "Hermitian space fitting the filling data"
kind = "definition"
summary = "A hermitian space with a point and a grading fits filling data S if its Gram matrix, real types and finite point match those of S; this identifies its adelic unitary group with the groups of S."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.Fits", "New.Filling.stdPrincipalLevel", "New.Filling.Fits.J_eq_ratGram", "New.Filling.Fits.ratEquiv", "New.Filling.Fits.adelicEquiv", "New.Filling.Fits.realHomeomorph", "New.Filling.Fits.finiteEquiv", "New.Filling.Fits.classPoint", "New.Filling.Fits.adelicEquiv_ratEquiv", "New.Filling.Fits.realHomeomorph_mul", "New.Filling.Fits.finiteEquiv_eq_conj_adelicToFin", "New.Filling.Fits.exists_coe_finiteEquiv_eq_conj", "New.Filling.Fits.finiteEquiv_mem_latticeStabilizer_iff", "New.Filling.Fits.reduction_finiteEquiv_iff", "New.Filling.Fits.mem_stdPrincipalLevel_iff", "New.Filling.Fits.measurePreserving_realHomeomorph", "New.Filling.Fits.gram_map_evalInf_point"]
lean_files = ["src/New/Spanning/Unfolding/PoincareSeries.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]], \(S\) [[?lean:New.Filling|filling data]] over \(E\) of shape \((\varrho,\kappa)\), and \(\varepsilon\) a family of signs on the basis indices of \(V\), with a fixed unitary matrix \(p\) such that \(p^{*}J_1p=\operatorname{diag}(\varepsilon)\) for the form \(J_1\) of \(G_1\) ([[?lean:New.DiscreteSeries.UnitarySignFrame|unitary sign frame]]). Let \(V=(J,x)\) be a [[?lean:New.Space|hermitian space with a point]]: a matrix \(J\) over \(E\) and an invertible adelic matrix \(x\) with \(x^{*}Jx=\operatorname{diag}(\varepsilon)\) at the [[?c:Infinite place of a number field|infinite places]] and \(=1\) at the finite places; its adelic group is \(G=G_\infty\times G_f\) ([[?lean:New.G|adelic unitary group in orthonormal local bases]]) with \(G_\infty=\prod_vU(\operatorname{diag}\varepsilon)\) and \(G_f\) the finite adelic unitary group of the standard form. Let \(Y\) be a [[?lean:New.Grading|grading]] of \(V\) (splitting the basis into \(\kappa\) and a string of \(2\varrho+1\) vectors), let \(l=(l_v)_v\) be doubled [[?c:Harish-Chandra parameter|Harish-Chandra parameters]], \(kw=(kw_v)_v\) weights, and \(\eta\) a finite adelic point of \(U(X_0)\).

The space \(V\) with \(Y\) **fits** \(S\) (with data \(l,kw,\eta\)) if:

1. at every infinite place \(v\) the Bessel system of \(S\) has type \((l_v,kw_v)\): its full function is the Bessel function of the [[?c:Discrete series representation|discrete series]] of parameter \(l_v\) with values in the representation of \(U(X_0)\) of weight \(kw_v\) ([[?lean:New.Filling.IsDiscreteSeriesBessel|discrete series Bessel system]]);
2. \(Y\) labels the basis in the standard way ([[?lean:New.Shape.besselIndexEquiv|standard labelling]]);
3. the kernel \(e_l=\prod_ve_{l_v}\) on \(G_\infty\) ([[?lean:New.typeKernel|type kernel]]) is an [[?lean:New.IsIdempotentKernel|idempotent kernel]];
4. the finite part of the point is \(x_f=u\cdot\iota_0(\eta)\cdot B\cdot k\) with \(u\) a [[?c:Idele group|finite idele]], \(\iota_0(\eta)\) the image of \(\eta\) acting on \(X_0\) ([[?lean:New.toBesselH|embedding of \(U(X_0)\)]]), \(B\) the [[?lean:New.Filling.latticeBasis|lattice basis]], and \(k\) an integral invertible matrix that reduces to \(1\) at the chosen places;
5. \(\eta\) commutes with every finite adelic point of \(U(X_0)\).

The **principal level** \(J_M\subseteq G_f\) is the open subgroup of integral matrices that reduce to \(1\) at all chosen places (in the orthonormal local bases of \(V\)).

## Identifications

If \(V\) fits \(S\), then \(J\) equals the rational [[?c:Gram matrix|Gram matrix]] of \(S\) (\(\varrho\) hyperbolic pairs around \(\operatorname{diag}(1,\dots,1,-N)\)), and there are:

- \(\rho:G_S(E)\xrightarrow{\ \sim\ }\Gamma\), from the rational [[?c:Isometry of a hermitian space|isometries]] of \(S\) to the group \(\Gamma\subseteq G\) of rational points of \(V\);
- \(\alpha:G\xrightarrow{\ \sim\ }G_S(\mathbb A)\), conjugation by the point \(x\); \(\alpha(\rho(\gamma))\) is the diagonal image of \(\gamma\);
- a homeomorphism \(\theta:G_\infty\to\prod_vG_1\), \(g_v\mapsto(d_v^{-1}x_vp^{-1})\cdot(p\,g_v\,p^{-1})\) with \(d_v\) the diagonal matrix of [[?lean:New.Filling.basisScale|basis scales]]; it preserves [[harmonic-analysis/haar-measure|Haar measures]] and satisfies \(\theta((gg')_\infty)=\alpha(g)_\infty\cdot\theta(g'_\infty)\), where \(\alpha(g)_\infty\) is the rescaled infinite part ([[?lean:New.Filling.adelicToInf|map to the infinite places]]);
- an isomorphism \(\psi:G_f\xrightarrow{\ \sim\ }G_{S,f}\) onto the finite adelic group of \(S\) in the lattice basis, with \(\psi(g_f)=\iota(\eta)^{-1}\,\alpha(g)_f\,\iota(\eta)\) (\(\iota\) the [[?lean:New.Filling.inclHFin|inclusion of \(U(X_0)\)]]);
- for a class \(c\), the **class point** \(x_c=\psi^{-1}\bigl(\iota(\eta)^{-1}h_c\bigr)\in G_f\).

## Properties

1. \(\psi\) is conjugation by an integral invertible matrix that reduces to \(1\) at the chosen places (the matrix \(k\) of condition 4; the idele \(u\) is central).
2. Hence \(\psi(k)\in K\) (the [[?lean:New.Filling.latticeStabilizer|lattice stabiliser]]) iff \(k\) is integral, and then both have the same reductions at the chosen places; and \(k\in J_M\) iff \(\psi(k)\in K(M)\) ([[?lean:New.Filling.principalLevel|principal level of \(S\)]]).

## References

1. Lean: `New.Filling.Fits`, `New.Filling.stdPrincipalLevel`, `New.Filling.Fits.ratEquiv`, `New.Filling.Fits.adelicEquiv`, `New.Filling.Fits.realHomeomorph`, `New.Filling.Fits.finiteEquiv`, `New.Filling.Fits.classPoint`, and the lemmas `J_eq_ratGram`, `adelicEquiv_ratEquiv`, `realHomeomorph_mul`, `finiteEquiv_eq_conj_adelicToFin`, `exists_coe_finiteEquiv_eq_conj`, `reduction_finiteEquiv_iff`, `mem_stdPrincipalLevel_iff`, `measurePreserving_realHomeomorph` of the namespace `New.Filling.Fits`, in `src/New/Spanning/Unfolding/PoincareSeries.lean`.
