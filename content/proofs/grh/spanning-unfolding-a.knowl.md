+++
id = "proofs/grh/spanning-unfolding-a"
title = "Spanning: unfolding, part A (cutoffs, block sums, Poincaré series and the Bessel period)"
kind = "page"
summary = "First half of the unfolding step of the spanning theorem: covolumes of arithmetic unipotent groups, convergence and symmetry of the block sums of amplitudes, the Poincaré series of Bessel functions with their Petersson products, and the identification of the Poincaré map with a Bessel period."
aliases = []
domains = ["proofs"]
section_mode = "continuous"
prerequisites = []
lean = []
lean_files = ["src/New/Spanning/Unfolding/FrameMass.lean", "src/New/Spanning/Unfolding/ReducedPoints.lean", "src/New/Spanning/Unfolding/Packing.lean", "src/New/Spanning/Unfolding/CutoffIntegral.lean", "src/New/Spanning/Unfolding/AmplitudeSums.lean", "src/New/Spanning/Unfolding/Climbing.lean", "src/New/Spanning/Unfolding/PoincareSeries.lean", "src/New/Spanning/Unfolding/BesselFormula.lean", "src/New/Spanning/Unfolding/ReducedGroups.lean", "src/New/Spanning/Unfolding/FillingAdmissible.lean", "src/New/Spanning/Unfolding/SeriesPeriod.lean"]
+++

This chapter covers eleven files of the folder "Unfolding, and the proof of the moments" of the spanning part of the argument. The spanning theorem (Theorem B, "enough forms") is proved by a second moment: one shows that the translates of Poincaré series fill the space of target forms on \(Y_0\). The second moment is a sum of Petersson products of translated Poincaré series, and by unfolding each product becomes a sum, over rational isometries \(\gamma\) of the hermitian space, of integrals of Bessel functions — the *amplitudes*. This chapter prepares everything that is needed before the terms are sorted and estimated: the measure theory of the cutoffs, the convergence and the symmetries of the sums of amplitudes, the Poincaré series themselves, and the verification that the abstract "filling data" attached to the admissible data \(D\) satisfy the standing hypotheses of the filling theorem. The sorting of the terms and the proof of the moments belong to the second half of the folder (another chapter), as do the definitions of the filling data themselves.

## Setting and notation

All objects below are defined in the companion chapter; here they are only named, with links.

[[?lean:New.Filling|Filling data]] \(S\) over a [[?c:CM field|CM field]] \(E\) with \(f\) infinite places consist of a prime \(N=\pi\bar\pi\), two level primes \(p_0,p_1\) with product \(M\) and chosen places above them, a generator \(\varpi\) of the different, a real parameter \(b\) measuring all sizes, a level in \(U(X_0)\) and a [[?lean:New.BesselSystem|Bessel system]] \((W_v,W_v^{\flat})\) (a Bessel function and its cut) at each infinite place \(v\). The hermitian space is
\[
V=\bigoplus_{a=1}^{\varrho}(Ee_a\oplus Ee_a^{*})\ \oplus\ X_0\ \oplus\ Ez,\qquad h(e_a,e_a^{*})=1,\quad h(z,z)=-N,
\]
with \(X_0\) definite of rank \(k\); its rank is \(r=k+2\varrho+1\), and \(n=\varrho+1\). The *frame* is \(f=(e_1,\dots,e_\varrho,z)\). The [[?lean:New.Shape.Form.besselU|unipotent group \(\mathsf U\)]] consists of the isometries that are block upper unitriangular for the flag of the frame, \(H=U(X_0)\), and the [[?lean:New.Shape.Form.besselS|Bessel subgroup]] is \(\mathsf S=\mathsf UH\). At the infinite places one works in \(G_\infty=\prod_vG_1\), with [[?lean:New.Shape.G₁|\(G_1\)]] the real unitary group in a rescaled basis; at the finite places in the lattice basis, with the integral subgroup \(K\) ([[?lean:New.Filling.latticeStabilizer|lattice stabiliser]]), its reduction to the finite [[?lean:New.Filling.ResidueGL|residue group]] \(\prod_wGL_r(k_w)\), and the kernel \(K(M)\) ([[?lean:New.Filling.principalLevel|principal level]]).

The [[?lean:New.Filling.Classes|classes]] \(c\) are the double cosets of \(U(X_0)\) for the source level, with representatives \(h_c\). For a class \(c\), \(\mathsf U_c(M)\) is the [[?lean:New.Filling.classUnipotent|group of rational unipotent elements]] \(u\) with \(h_c^{-1}uh_c\in K(M)\), and \(\beta_c\) is the [[?lean:New.Filling.classCutoff|class cutoff]], a function on \(G_\infty\) used to write integrals over \(\mathsf U_c(M)\backslash G_\infty\). A rational isometry \(\gamma\) is a [[?lean:New.Filling.termsOver|term]] over the *block* \((c,s,c')\) if \(h_c^{-1}\gamma h_{c'}\in K\) with reduction \(s\). Its [[?lean:New.Filling.amplitude|amplitude]] is
\[
\mathcal A(c,c';\gamma)=\int_{G_\infty}\beta_c(y)\,\beta_{c'}(\gamma^{-1}y)\;W(y)\otimes W(\gamma^{-1}y)^{*}\,dy,
\]
and the [[?lean:New.Filling.amplitudeSum|block sum]] \(A_T(c,s,c')\) of a set \(T\) is the sum of the amplitudes of the terms of \(T\) over \((c,s,c')\). The [[?lean:New.Filling.IsAdmissible|standing hypotheses]] collect the size inequalities between \(b\), \(M\), \(N\), \(\varpi\) and the second moments.

## 1. Masses of spheres and frames

For admissible data \(D\), the [[proofs/grh/spanning-unfolding-a/unit-sphere-mass|sphere masses]] \(\operatorname{sph}_l(v)\) and the [[proofs/grh/spanning-unfolding-a/frame-mass|frame masses]] \(\operatorname{fr}_v=N^k\operatorname{sph}_{k+1}(v)\cdots\operatorname{sph}_r(v)\) are explicit numbers built from the [[proofs/grh/spanning-unfolding-a/size-of-different-generator-at-infinite-places|absolute values of \(\varpi\)]]. By the approximate mass formula for consecutive ranks, [[proofs/grh/spanning-unfolding-a/product-of-frame-masses-upper-bound|their product is at most \(N^{kf}\operatorname{mass}_k/\operatorname{mass}_r\)]] up to a factor \(1+b^{-9}\); and it is [[proofs/grh/spanning-unfolding-a/product-of-frame-masses-and-open-cell-constant|expressed exactly]] through the Siegel constant and the open cell constant. These two facts are used in section 9.

## 2. Unipotent elements, reduced points, cutoffs

[[proofs/grh/spanning-unfolding-a/eichler-map-is-isometry|Eichler's formula]] gives [[proofs/grh/spanning-unfolding-a/eichler-elements-of-unipotent-congruence-subgroup|explicit elements of \(\mathsf U_c(M)\)]], in particular [[proofs/grh/spanning-unfolding-a/eichler-element-with-prescribed-row|elements with one prescribed row]]; hence the [[proofs/grh/spanning-unfolding-a/frame-matrices-of-unipotent-congruence-subgroup|action of \(\mathsf U_c(M)\) on the frame]] is by all unitriangular matrices with entries in \(M\mathcal O_E\) above the diagonal. By a general [[proofs/grh/spanning-unfolding-a/reduction-of-unitriangular-matrices|reduction of unitriangular matrices]], [[proofs/grh/spanning-unfolding-a/unique-coset-moving-a-point-to-a-reduced-point|exactly one coset]] of the subgroup fixing the frame moves a given point of \(G_\infty\) to a *reduced* point, so that [[proofs/grh/spanning-unfolding-a/reduced-points-give-box-partition-of-unity|the indicator of the reduced points is a partition of unity in boxes]]. Consequently [[proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one|the translates of \(\beta_c\) under \(\mathsf U_c(M)\) sum to one]], and \(\beta_c\) is supported where the frame vectors are bounded.

Two counting tools follow. A term that moves the frame vectors of a point in a box very little must fix the frame ([[proofs/grh/spanning-unfolding-a/rigidity-of-frames|rigidity of frames]]: the relevant coordinates are algebraic integers of absolute value \(<1\) at all places). Hence [[proofs/grh/spanning-unfolding-a/packing-of-frames|few frames fit in a box]], and [[proofs/grh/spanning-unfolding-a/packing-of-weights|weights dominated by class cutoffs]] have a bounded sum; the bookkeeping uses [[proofs/grh/spanning-unfolding-a/colouring-bound-for-weighted-sums|colouring bounds]] and the [[proofs/grh/spanning-unfolding-a/index-of-scaled-integral-lattice|index of scaled lattices]].

## 3. The covolume of the arithmetic unipotent group

In [[proofs/grh/spanning-unfolding-a/row-coordinates-of-real-unipotent-group|row coordinates]] the real unipotent group \(\mathsf U_\infty\) has Lebesgue measure as Haar measure, right multiplication is [[proofs/grh/spanning-unfolding-a/additivity-of-unipotent-row-entries|additive coordinate by coordinate]] in a triangular order, and the coordinates of \(\mathsf U_c(M)\) [[proofs/grh/spanning-unfolding-a/lattices-of-unipotent-row-coordinates|fill explicit lattices]]. So there is a [[proofs/grh/spanning-unfolding-a/fundamental-box-for-arithmetic-unipotent-group|fundamental box]], and with the [[proofs/grh/spanning-unfolding-a/integral-of-class-cutoff-over-fundamental-set|unfolding lemma for cutoffs]]:

> [[proofs/grh/spanning-unfolding-a/integral-of-class-cutoff-is-unipotent-covolume|\(\int_{\mathsf U_\infty}\beta_c(uy)\,du=\operatorname{cov}_{\mathsf U}\)]], the same explicit number for every class \(c\) and point \(y\).

## 4. Block sums of amplitudes

[[proofs/grh/spanning-unfolding-a/amplitude-bounded-by-majorant|The amplitude is bounded by its majorant]]. Unfolding \(\beta_c\) [[proofs/grh/spanning-unfolding-a/unfolding-class-cutoff-against-invariant-weights|against \(\mathsf U\)-invariant weights]] and counting terms in layers of the [[proofs/grh/spanning-unfolding-a/scaled-bessel-length-product|scaled Bessel length]] ([[proofs/grh/spanning-unfolding-a/summation-by-layers|summation by layers]], [[proofs/grh/spanning-unfolding-a/sum-of-cutoffs-with-inverse-length-powers|sums of cutoffs]]), the decay of the Bessel functions ([[proofs/grh/spanning-unfolding-a/cut-changes-kernel-little|pointwise bounds]]) gives:

- [[proofs/grh/spanning-unfolding-a/convergence-of-block-sums|absolute convergence of all block sums]];
- [[proofs/grh/spanning-unfolding-a/tail-bound-for-the-cut|replacing \(W\) by its cut \(W^{\flat}\) changes a block by at most \(\tfrac12\operatorname{cov}_{\mathsf U}b^{-k^3f}\)]];
- [[proofs/grh/spanning-unfolding-a/change-of-weight-in-block-sums|for a stable set \(T\), the product \(\beta_c(y)\beta_{c'}(\gamma^{-1}y)\) may be replaced by any weight with orbit sums one]].

The change of weight has three consequences: blocks can be [[proofs/grh/spanning-unfolding-a/moving-a-block-by-the-bessel-subgroup|moved by rational elements of the Bessel subgroup]]; they [[proofs/grh/spanning-unfolding-a/block-sums-under-unipotent-reductions|transform by the unipotent character and vanish unless \(s\) agrees]]; and [[proofs/grh/spanning-unfolding-a/identity-block-of-the-bessel-subgroup|the identity block of the Bessel subgroup is \(\operatorname{cov}_{\mathsf U}\) times the identity]] (orthonormality of the Bessel coordinates).

## 5. Which terms contribute

[[proofs/grh/spanning-unfolding-a/terms-with-disagreeing-characters-contribute-zero|A stable set of terms whose characters do not agree contributes zero]]. For a term whose characters do agree, common vectors of the flags of \(f\) and \(\gamma f\) ([[proofs/grh/spanning-unfolding-a/common-vectors-of-two-flags|definition]]) can be [[proofs/grh/spanning-unfolding-a/climbing-common-vectors-over-the-field|moved up the flags]] by Eichler maps, with leading coefficients of equal norm; hence [[proofs/grh/spanning-unfolding-a/existence-of-cell-rank|a term with vanishing discriminant has a cell rank]]. The same climbing works [[proofs/grh/spanning-unfolding-a/climbing-common-vectors-modulo-a-place|modulo each place above \(M\)]] (using [[proofs/grh/spanning-unfolding-a/prescribing-residues-above-the-level|lifts of residues]]), and bounds the [[proofs/grh/spanning-unfolding-a/meeting-places-and-meet-norm|meet norm]] of the reduction of an integral element [[proofs/grh/spanning-unfolding-a/meet-norm-bounded-by-index-of-determinant|by the index of a two-by-two determinant]]. The subsets of the residue group used later are defined here: [[proofs/grh/spanning-unfolding-a/fixers-of-frame-vectors|fixers of frame vectors]], [[proofs/grh/spanning-unfolding-a/open-element-of-residue-group|open elements]], [[proofs/grh/spanning-unfolding-a/scalar-coset-of-bessel-subgroup|scalar cosets]]; and [[proofs/grh/spanning-unfolding-a/unitary-group-of-x0-in-lattice-basis|the integrality of \(U(X_0)\) in the lattice basis]] is described.

## 6. The finite groups

The reductions at the chosen places are computed: [[proofs/grh/spanning-unfolding-a/reduced-unipotent-group|\(\bar{\mathsf U}\) is the group of all block unitriangular tuples, of order \(M^{f\varrho(2k+2\varrho+1)}\)]] (by [[proofs/grh/spanning-unfolding-a/gluing-integral-isometries-at-chosen-places|gluing integral isometries]]); [[proofs/grh/spanning-unfolding-a/reduced-levi-group|\(\bar H\cong\prod_wGL_k(k_w)\), and \(\lvert\bar H\rvert\) is the index of the source level]]; [[proofs/grh/spanning-unfolding-a/reduced-bessel-group|\(\bar{\mathsf S}=\bar{\mathsf U}\bar H\) with trivial intersection]]; and [[proofs/grh/spanning-unfolding-a/reductions-are-products-over-places|these reductions are products over the places]].

## 7. Poincaré series

A hermitian space \(V\) with a point and a grading [[proofs/grh/spanning-unfolding-a/space-fitting-filling-data|fits]] the filling data when its groups can be identified with those of \(S\); then the [[proofs/grh/spanning-unfolding-a/groups-of-a-graded-fitting-space|Bessel groups and the embeddings of \(U(X_0)\) correspond]]. The [[proofs/grh/spanning-unfolding-a/poincare-series-of-bessel-functions|Poincaré series]] \(\mathcal P_\varphi=\sum_a\varphi_a\sum_{\gamma}B_a(\gamma g)\) of the cut-off Bessel functions [[proofs/grh/spanning-unfolding-a/convergence-of-poincare-series|converge uniformly]], [[proofs/grh/spanning-unfolding-a/poincare-series-are-forms|are forms of the discrete series type and of principal level]], [[proofs/grh/spanning-unfolding-a/unfolding-of-poincare-series|unfold]] and [[proofs/grh/spanning-unfolding-a/folding-of-poincare-series|fold]], and

> [[proofs/grh/spanning-unfolding-a/petersson-products-of-poincare-series|\(\langle k\,\mathcal P_{(c',i')},\mathcal P_{(c,i)}\rangle=\operatorname{vol}(J_M)\cdot A^{\mathrm{full}}_{\mathrm{all}}(c,s,c')_{(i,i')}\)]] for integral \(k\) with reduction \(s\).

This is the bridge between the second moment of the Poincaré series and the block sums of section 4. The coefficient vectors \(\varphi\) are [[proofs/grh/spanning-unfolding-a/source-forms-in-bessel-coordinates|source forms in Bessel coordinates]].

## 8. The Bessel function and the Bessel period

The [[proofs/grh/spanning-unfolding-a/real-bessel-group-is-product-of-local-groups|real Bessel group is the product of the local ones]], so the tensor product of the local Bessel functions is [[proofs/grh/spanning-unfolding-a/bessel-function-as-one-integral|one integral over \(R(F_\infty)\)]] of the conjugate type kernel against the [[proofs/grh/spanning-unfolding-a/bessel-character-of-fitting-space|Bessel character]], which [[proofs/grh/spanning-unfolding-a/bessel-character-extends-generic-character|extends the generic character]]. Pairing with the value of a source form ([[proofs/grh/spanning-unfolding-a/bessel-function-paired-with-a-form-value|integral formula]]), [[proofs/grh/spanning-unfolding-a/moving-the-quotient-to-the-bessel-group|moving the quotient by \(\mathsf U_c(M)\) to the Bessel group]] along the [[proofs/grh/spanning-unfolding-a/class-sections-and-class-weights|class sections]], and using that [[proofs/grh/spanning-unfolding-a/bessel-quotient-as-union-of-class-quotients|\([R]/J'\) is the disjoint union of the \(\mathsf U_c(M)\backslash R(F_\infty)\)]], one obtains:

> [[proofs/grh/spanning-unfolding-a/poincare-series-represents-the-bessel-period|the Poincaré series represents the Bessel period]].

## 9. The filling data of the admissible data

For admissible data \(D\), [[proofs/grh/spanning-unfolding-a/filling-data-fit-the-space-y0|the filling data fit \(Y_0\)]]. The numerical inputs are the [[proofs/grh/spanning-unfolding-a/number-of-bessel-coordinates|number of Bessel coordinates]], the [[proofs/grh/spanning-unfolding-a/degree-of-bessel-systems-of-the-data|degree of the Bessel systems]], the [[proofs/grh/spanning-unfolding-a/number-of-classes-of-the-source-level|number of classes]] \(n_X=\lvert\bar H\rvert(N^k-1)^f\operatorname{mass}_k\), the [[proofs/grh/spanning-unfolding-a/mean-value-bounds-for-the-main-second-moment|mean value bounds]], the [[proofs/grh/spanning-unfolding-a/scaled-siegel-constant-bound|bound for the scaled Siegel constant]] and the [[proofs/grh/spanning-unfolding-a/ratio-of-main-and-identity-second-moments|range of the ratio of the main to the identity second moment]]. Together:

> [[proofs/grh/spanning-unfolding-a/filling-data-of-admissible-data-are-admissible|the filling data of \(D\) satisfy the standing hypotheses]],

so that all results above apply to \(D\). Finally, with the [[proofs/grh/spanning-unfolding-a/source-form-coordinates-of-the-data|source form coordinates of the data]], the [[proofs/grh/spanning-unfolding-a/poincare-map-of-admissible-data|Poincaré map \(\mathcal P_D\) of the data]] — the map \(\mathcal P\) of the main argument, defined by a Bessel period — is the Poincaré series of the Bessel function.

## Status

Of the 67 results of this chapter, 62 carry complete proofs and 5 are outlines in which one computational step is asserted with a pointer to the Lean declaration (fit to \(Y_0\); the degree formula; the Bessel groups of a graded space; the generic character; the logarithmic estimate of the ratio of second moments). All numerical comparisons "by the size calculus of the data" are cited from [[?lean:New.Data.le_of_hasLogBound|the comparison of logarithmic bounds]].

## References

1. Lean: the files `FrameMass`, `ReducedPoints`, `Packing`, `CutoffIntegral`, `AmplitudeSums`, `Climbing`, `PoincareSeries`, `BesselFormula`, `ReducedGroups`, `FillingAdmissible`, `SeriesPeriod` of `src/New/Spanning/Unfolding/`.
2. The heads of these files name as related work: H. Petersson (1932) on Poincaré series; S. Friedberg, Poincaré series for GL(n) (1987); Y. Liu, Relative trace formulae toward Bessel and Fourier–Jacobi periods (2014); M. Furusawa and J. Shalika, Mem. AMS 782 (2003); G. Shimura (1997) for the mass formula. These are pointers of the source, not checked here.
