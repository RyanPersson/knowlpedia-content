# spanning-core

[Incremental audit](README.md) · [Findings table](findings.tsv)

<a name="page-spanning-core"></a>

## Spanning: the second moment, equal multiplicities, and Bessel systems

Revised · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core.knowl.md) · [FillingData.lean:339](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/FillingData.lean#L339)

All 66 child knowls and all 17 listed Lean files are present. The new local construction feeds the normalized Bessel average and its cut into the real-place existence theorem. The earlier comments on lines 26, 32 and 41 concern untouched text.

<a name="finding-spanning-core-1"></a>

**High · Normalize the test function in the quantitative pairing bound.** The chapter gives the square root of the product of the local bounds for a bounded frame-invariant test function. Lean assumes a measurable function of modulus at most 1 and requires its product with the cut kernel to vanish outside the frame boxes. The integral and the cut error scale with the test function. For a general bounded test, its supremum norm also multiplies the square-root term. State the unit bound and support condition. For the displayed radii ρᵥ, require ρᵥ ≥ b^(6n+2) and a common y′ with y′ᵥ and γᵥ⁻¹y′ᵥ in the radius-ρᵥ box at each place. The quantity bounded is the Hilbert–Schmidt norm of the integral. [Translation, line 59](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core.knowl.md#L59) · [OpenCellPairing.lean:240](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellPairing.lean#L240)

<a name="finding-spanning-core-2"></a>

**Medium · Include the formal degree and the square in the period identity.** The period at x is ⟨v,W(x)⟩ = deg(λ)·‖W‖₂² for the unnormalized average of a unit vector v. Calling the period its L² norm loses both the square and the formal degree. The stationary-point step uses the size of this period compared with the volume of the unit ball in the period group. Give the identity for the unnormalized average before describing its normalization. Mention that the quantitative lower bound comes from the steep parameter and matching compact type in the linked stationary-point theorem. [Translation, line 63](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core.knowl.md#L63) · [LargeFunction.lean:685](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean#L685)

<a name="page-bessel-average-properties"></a>

## The Bessel average is a Bessel function reproduced by the discrete series kernel

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-average-properties.knowl.md) · [LargeFunction.lean:685](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean#L685)

Right invariance gives left Bessel equivariance. The inverse in the reproducing kernel, the covering exponent 9r² and factor 16^(9r²), and the identity equating the period to the formal degree times the squared norm all agree with the declarations.

<a name="finding-bessel-average-properties-1"></a>

**Medium · Specify that rep is a continuous unitary representation.** The displayed input is a continuous map into a unitary group. The proof of equivariance uses its multiplication and inverse laws to factor the operator π(s) out of the translated integral. Continuity and unitary values alone do not supply those laws. Introduce rep as a continuous group homomorphism U(κ) → U(I), as required in the linked definition of the Bessel average. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-average-properties.knowl.md#L15) · [LargeFunction.lean:473](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean#L473)

<a name="finding-bessel-average-properties-2"></a>

**Low · Give the squared norm and its formal-degree factor in the summary.** The period equals the formal degree times the square of the L² norm. A reader of the summary alone gets the unscaled norm. Item 4 already has the exact identity. Say that the period is degλ‖W‖₂². [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-average-properties.knowl.md#L5) · [LargeFunction.lean:685](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean#L685)

<a name="finding-bessel-average-properties-3"></a>

**Low · Specify how W is integrated over the unipotent quotient.** The vector W can change by the character ψ under a change of coset representative. Its norm descends to the quotient. Lean integrates W on G₁ with besselQuotMeasure, a cutoff-weighted Haar measure on G₁ that computes quotient integrals. Define μ on G₁ as besselQuotMeasure, or state that W is an integrable equivariant section and its norm is integrable on the quotient. [Translation, line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-average-properties.knowl.md#L20) · [Basic.lean:630](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L630)

<a name="finding-bessel-average-properties-4"></a>

**Low · Correct the two library names for the decay estimates.** Both coefficient decay and the covering inequality live under New.DiscreteSeries. The generic coefficient result allows c ≤ h and is specialized at c = j + 9r². The covering theorem at TotalMass.lean line 466 takes a right-invariant measure finite on compact sets and c &gt; 8r². The chosen Haar measure and exponent satisfy these conditions. Cite New.DiscreteSeries.norm_dsCoeff_le_pow and New.DiscreteSeries.lintegral_decay_le. Keep New.isIdempotentKernel_dsCoeffInFrame as written. [Translation, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-average-properties.knowl.md#L25) · [SquareIntegrability.lean:297](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/SquareIntegrability.lean#L297)

<a name="page-bessel-period-group-and-average"></a>

## The group of the Bessel period and the Bessel average

Added · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-period-group-and-average.knowl.md) · [Average.lean:154](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Average.lean#L154)

The coordinates (u,h) ↦ (hu,h) give the stated left and right translations. The coefficient at x⁻¹gy, the negative phase and rep(h⁻¹) all agree with the integrand.

<a name="finding-bessel-period-group-and-average-1"></a>

**Low · The period group is a semidirect product.** The summary writes R = U × H as a group. The product is a coordinate description of the underlying space. In the group law H acts on U by conjugation, as the proof on this page shows. Write R = U ⋊ H in the summary and reserve U × H for the Haar coordinates. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-period-group-and-average.knowl.md#L5) · [Average.lean:42](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Average.lean#L42)

<a name="finding-bessel-period-group-and-average-2"></a>

**Low · Specify the unipotent Haar normalization.** The page names the compact Haar measure but only calls du a Haar measure. The value of the displayed Bessel average scales with du. Lean fixes besselHaar by pushing forward the product of Lebesgue measure on the upper entries and besselHaar₀. Identify du as New.Shape.besselHaar and dh as Haar probability, so the average has its source normalization. [Translation, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-period-group-and-average.knowl.md#L14) · [Basic.lean:624](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L624)

<a name="finding-bessel-period-group-and-average-3"></a>

**Low · Point the sign-frame reference to its declared namespace.** The placeholder names New.SignFrame. The class that supplies the matrix taking the Hermitian form to the sign diagonal is New.DiscreteSeries.SignFrame. Replace the target with New.DiscreteSeries.SignFrame. [Translation, line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-period-group-and-average.knowl.md#L19) · [Grading.lean:744](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L744)

<a name="page-bessel-system-of-discrete-series-type"></a>

## Bessel system of discrete series type

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-system-of-discrete-series-type.knowl.md) · [LargeFunction.lean:60](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean#L60)

The two inverse changes of basis yield exactly the transposed Schur action. The conjugated coefficient is the kernel applied at x, and the four defining fields allow a real scalar and an unnormalized vector in the average.

<a name="finding-bessel-system-of-discrete-series-type-1"></a>

**Low · Point the sign-frame reference to its declaring namespace.** The link expects New.SignFrame. New.DiscreteSeries.UnitarySignFrame extends New.DiscreteSeries.SignFrame, the class whose Gram identity supplies the conjugation into U(ε). Change the placeholder to New.DiscreteSeries.SignFrame. [Translation, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-system-of-discrete-series-type.knowl.md#L14) · [Grading.lean:744](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L744)

<a name="page-bessel-systems-exist-at-the-real-places"></a>

## Bessel systems exist at the real places

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-systems-exist-at-the-real-places.knowl.md) · [FillingData.lean:339](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/FillingData.lean#L339)

The construction uses the common unitary frame, a Schur highest-weight vector of norm one, the stationary-period estimate with exponent 60(r+k)², and a cut pair of squared mass |I|. The degree and reproduction clauses of the resulting discrete-series type agree. The numerical size estimates are cited in this outline.

<a name="finding-bessel-systems-exist-at-the-real-places-1"></a>

**High · Use the global size parameter for the stationary-point entry bound.** The substitution sets a = ccᵥ(1) and then L = 3a. The stationary-point theorem needs L to bound every entry of both Harish-Chandra parameters. Lean supplies these bounds with L = 3·D.a (FillingData.lean lines 235–236, 350 and 375). At places outside D.aPlaces the local column count is zero by Weights.lean lines 53–55. Then the proposed L is zero, which is incompatible with the large-gap parameter on the indefinite group. Write aᵥ = ccᵥ(1) for the distinguished lowest K-type weight and L = 3·D.a for the common bound. Keep 3·D.a as the bound in steps 2 and 6. [Translation, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-systems-exist-at-the-real-places.knowl.md#L24) · [FillingData.lean:375](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/FillingData.lean#L375)

<a name="finding-bessel-systems-exist-at-the-real-places-2"></a>

**Medium · Include the degree hypothesis in the local-bounds application.** The quoted local-bounds theorem has a separate hypothesis 4000n ≤ f. The listed RealPlaceSizes controls the box radius, ranks, exponent and base, and has no f parameter. FillingData.lean lines 407–409 supplies this final inequality from admissibility. Add 4000n ≤ f to step 7 and cite the data’s size estimates. The volume-of-balls premise in the same sentence is for T ≥ 1. [Translation, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-systems-exist-at-the-real-places.knowl.md#L27) · [RealBandLimits.lean:703](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealBandLimits.lean#L703)

<a name="finding-bessel-systems-exist-at-the-real-places-3"></a>

**Medium · Use the radial majorant in the volume-of-balls argument.** The outline attributes the ball-volume estimate to Chebyshev applied to the coefficient tail. An upper bound on a coefficient permits it to vanish on the ball. The source integrates the positive radial function φ(g) = deg·(2/‖g‖)ᵐ, with m = 9r², whose lower bound on the ball controls its volume. Cite the integral bound for φ and integrate deg ≤ (T/2)ᵐφ(g) over ‖g‖ ≤ T for T ≥ 1. [Translation, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/bessel-systems-exist-at-the-real-places.knowl.md#L27) · [CutTailBound.lean:108](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/CutTailBound.lean#L108)

<a name="page-cut-of-a-bessel-function"></a>

## Cut of a Bessel function

Added · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/cut-of-a-bessel-function.knowl.md) · [CutTailBound.lean:289](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/CutTailBound.lean#L289)

The support and change thresholds follow from the two ends of the linear cutoff. On the change set the scaled length is at least b, and the two majorant bounds give b^(6r³f)‖F♭−F‖² ≤ aw, yielding the stated loss after integration.

<a name="finding-cut-of-a-bessel-function-1"></a>

**Low · Define the dimension in the cutoff error exponent.** The first use of r is the condition r ≥ 100. Its cube sets the decay rate. Lean takes r to be the size of the matrices in G₁, while the preceding text defines only n. Introduce r = 2ϱ + |κ| + 1 as the matrix size and f as a positive integer before stating the estimate. [Translation, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/cut-of-a-bessel-function.knowl.md#L25) · [CutTailBound.lean:283](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/CutTailBound.lean#L283)

<a name="page-cut-pair-from-the-bessel-average"></a>

## The normalised Bessel average and its cut form a cut pair

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/cut-pair-from-the-bessel-average.knowl.md) · [CutTailBound.lean:411](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/CutTailBound.lean#L411)

The normalization uses the positive ball volume and a finite, nonzero squared norm, and the majorant construction gives the exponent m+99r² ≤ 400r². The two cases of the scaled-length estimate agree with the proof.

<a name="finding-cut-pair-from-the-bessel-average-1"></a>

**Medium · Distinguish the library tail estimate from its specialization in b.** The number called the “exact form” of integral_tail_le contains b. The library theorem uses 8·(2000·(r+L+1)⁶)^(2r²)·2ᴹ and has no b parameter. CutTailBound.lean lines 69–78 replaces 8 and 2000 by b and r+L+1 by b⁴. The resulting estimate used in the integral is valid. Give the library constant and then state the substitutions using b ≥ 2000 and r+L+1 ≤ b⁴. [Translation, line 33](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/cut-pair-from-the-bessel-average.knowl.md#L33) · [SquareIntegrability.lean:945](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/FlenstedJensen/SquareIntegrability.lean#L945)

<a name="finding-cut-pair-from-the-bessel-average-2"></a>

**Low · State that rep is a continuous unitary representation.** The theorem introduces a continuous map from U(κ) to U(I). The construction also needs its homomorphism property, which appears in the Lean type →\* and gives the transformation law for the normalized Bessel function. The linked definition of the average uses this structure. Call rep a continuous unitary representation of U(κ) on ℂᴵ. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/cut-pair-from-the-bessel-average.knowl.md#L15) · [CutTailBound.lean:47](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/CutTailBound.lean#L47)

<a name="page-open-cell-bound"></a>

## Open cell bound for a Bessel system

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/open-cell-bound.knowl.md) · [OpenCellBound.lean:547](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellBound.lean#L547)

The bound uses both kernel coordinates, Haar restricted to A, probability in the shift, and almost-sure capture of every qualifying z. The unrestricted definition and its intermediate version need the qualifications below.

<a name="finding-open-cell-bound-1"></a>

**Medium · The displayed mass bound can divide by zero outside the open cell.** The page defines the predicate for arbitrary γ and divides by g(Z(γ)). For example, at ϱ = 0 and γ = 1 the frame Gram matrix is \[−1\] and the discriminant is zero. Lean uses total real division, making pairingBoundSq zero there. The existence theorem separately assumes positive discriminant. Give the explicit fraction on the open cell and state how pairingBoundSq is defined when the discriminant vanishes, or state the source convention 0⁻¹ = 0. [Translation, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/open-cell-bound.knowl.md#L22) · [Basic.lean:881](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L881)

<a name="finding-open-cell-bound-2"></a>

**Medium · The intermediate kernel bound carries fewer conditions on the shifts.** IsKernelBound does more than replace γt by an arbitrary g and change the radius and mass bound. It imposes neither measurability of t nor frame fixing. Lines 719–721 of the source add those conditions explicitly to pass from the kernel bound to the open-cell bound. State that the compactness, probability, contraction, mass and capture fields are retained. List measurability of t and its values in the frame fixer as extra requirements of IsOpenCellBound. [Translation, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/open-cell-bound.knowl.md#L25) · [OpenCellBound.lean:576](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellBound.lean#L576)

<a name="page-open-cell-bound-exists"></a>

## The open cell bound holds for every Bessel system

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/open-cell-bound-exists.knowl.md) · [OpenCellBound.lean:695](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellBound.lean#L695)

The two frame-box conditions, radius P⁻⁶, choice M₀ = M⁹ⁿ, tube, tensor-kernel estimate and final exponent 93600 n⁴ + 2 n² + 45 n agree with the source. The density chosen in the proof needs one correction.

<a name="finding-open-cell-bound-exists-1"></a>

**High · The proof applies the fixer-measure density twice.** The linked definition uses μ_d = c_G d^(k−1) dh du. Step 3 sets c = c_G (g(Z)/2)^(k−1) and then uses μ_c, which has density c_G c^(k−1). Step 5 instead uses mass c · vol(Ω₀). Conditioning cancels a constant in m, but ν also contains the inverse of this mass, so the claimed bound for the proposed ν does not follow. Set d = g(Z)/2 and c = c_G d^(k−1). Take μ = μ_d = c · dh du throughout. This gives the step-5 mass and the Sobolev measure used in step 4. [Translation, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/open-cell-bound-exists.knowl.md#L25) · [OpenCellBound.lean:648](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellBound.lean#L648)

<a name="page-schur-bound-holds-for-functions-fixed-by-the-kernel"></a>

## Schur's bound for a Bessel function fixed by the discrete series kernel

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/schur-bound-holds-for-functions-fixed-by-the-kernel.knowl.md) · [SchurBound.lean:290](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/SchurBound.lean#L290)

The coefficient is cλ(g) times the squared quotient norm of F. For an integrable test function and an order s ≤ 2n², the two inverse formal-degree factors in the convolution estimate give B^(2s)D. The differentiated bumps supply derivatives for all orders.

<a name="finding-schur-bound-holds-for-functions-fixed-by-the-kernel-1"></a>

**Medium · Limit the fixed-constant Schur estimate to the stated derivative orders.** The summary attributes Schur’s L² bound to derivatives of all orders. The chain rule does hold for every word, but the uniform estimate B^(2s)D in the theorem requires s ≤ 2n². The unrestricted estimate for X_w uses a base growing with the word length. The body gives the correct cutoff at line 27. State that right derivatives exist at every order and that the displayed Schur constants apply through order 2n². [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/schur-bound-holds-for-functions-fixed-by-the-kernel.knowl.md#L5) · [Basic.lean:918](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L918)

<a name="finding-schur-bound-holds-for-functions-fixed-by-the-kernel-2"></a>

**Low · Correct the namespaces for the two abstract Schur estimates.** The abstract convolution and coefficient estimates are declared as New.IsBoundedMeasurable.lintegral_sq_convolve_convolve_le and New.IsBoundedMeasurable.integral_inner_translate (the latter at line 262 of the same file). The cited New.IsBesselFunction names do not identify those declarations. Dot notation at their applications uses the bounded measurable structure carried by a Bessel function. Give the two New.IsBoundedMeasurable qualified names in the list of library inputs. [Translation, line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/schur-bound-holds-for-functions-fixed-by-the-kernel.knowl.md#L23) · [SchurBound.lean:570](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/SchurBound.lean#L570)

<a name="page-sizes-near-a-point-of-the-open-cell"></a>

## Sizes at and near a point of the open cell

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/sizes-near-a-point-of-the-open-cell.knowl.md) · [OpenCellBound.lean:110](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellBound.lean#L110)

The operator-norm estimate is the stated l²M² entrywise estimate. Cramer’s rule gives M^(3+4ϱ), the square-root defect gives M^(4n+1), and applying the perturbation result at P/2 gives the claimed ball and discriminant range.

<a name="finding-sizes-near-a-point-of-the-open-cell-1"></a>

**Low · Include the inverse-scale inequality assigned to this page.** The front matter claims inv_pow_div_gramDiscReal_le. The three listed conclusions stop after the lower bound for ρ⁹ⁿ/g. The separate assigned estimate is used when the existence proof verifies its lower bound on the discriminant. Add that for g &gt; 0, ρ ≥ 1 and each natural N, (ρᴺ/g)⁻¹ = g/ρᴺ ≤ g. This estimate needs no entry bound. [Translation, line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/sizes-near-a-point-of-the-open-cell.knowl.md#L19) · [OpenCellBound.lean:332](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellBound.lean#L332)

<a name="page-sobolev-bound-at-the-gram-section"></a>

## The L2 bound at the Gram section via Sobolev's inequality

Revised · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/sobolev-bound-at-the-gram-section.knowl.md) · [SobolevBound.lean:592](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/SobolevBound.lean#L592)

The edit resolves the previous medium finding about 0 &lt; ε ≤ 1, distinguishes integrals from means, and preserves the correct corner constant and exponent 550n². The previous low finding at line 15 about the matrix size r is still open.

<a name="finding-sobolev-bound-at-the-gram-section-1"></a>

**Low · Specify the measure and measurability in the rewritten cube lemma.** The standalone paraphrase lists the derivative and integral bounds. The library also assumes an s-finite parameter measure and joint measurability of each f_w in (x,ω). These hypotheses hold here for the restricted fixer measure and the displayed compositions, as used at SobolevBound.lean lines 450–455. Introduce the cube inequality for jointly measurable f_w and an s-finite parameter measure. The application and its constants are already correct. [Translation, line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/sobolev-bound-at-the-gram-section.knowl.md#L32) · [PackingAndSobolev.lean:188](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/PackingAndSobolev.lean#L188)

<a name="page-stationary-point-with-large-period"></a>

## A point of bounded length at which the Bessel period is large

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/stationary-point-with-large-period.knowl.md) · [LargeFunction.lean:388](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean#L388)

The appendix specializes at L′ = 1 and d = n−1. The Gram sign, the bound (3B+a)^(2n), the passage from 8n√r M to b^(5n), the phase exp(conj σ−σ) and the exponent 20(r+k)² agree with the sources.

<a name="finding-stationary-point-with-large-period-1"></a>

**Medium · Subtract the identity in the flag-lowering assertion.** Writing A = p⁻¹x⁻¹gxp, it is A−I that sends the first j vectors into the span of the first j−1. A itself preserves their flag. At the identity, A cannot send the nonzero first vector to zero. Similarly g−I induces h−I on the definite coordinates modulo the isotropic span. State the flag condition for A−I in the sign frame. State either that A acts by h modulo the preceding vectors, or that A−I acts by h−I there. [Translation, line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/stationary-point-with-large-period.knowl.md#L27) · [LargeFunction.lean:308](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean#L308)

<a name="finding-stationary-point-with-large-period-2"></a>

**Medium · Use the period estimate for a stationary position.** The cited IsPosition.period_lower_bound_of_surjective does not exist. The appendix requires IsStationary, including i₀† μ i₀ = μ′ and the identity on the common X-coordinates. The Gram and flag properties listed in the outline do not provide those two identities. Step 1 actually obtains them from IsSteep.exists_isStationary. Cite New.DiscreteSeries.IsStationary.period_lower_bound_of_surjective and carry the two defining identities of its stationary-position input forward from step 1. [Translation, line 28](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/stationary-point-with-large-period.knowl.md#L28) · [PositionGroup.lean:426](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/PositionGroup.lean#L426)

<a name="finding-stationary-point-with-large-period-3"></a>

**Low · Include the signs on X in the description of steepness.** Steepness requires sign +1 on X as well as zero weight there. On the remaining coordinates the signs start with +1 and alternate, and the weights decrease strictly. The parenthetical description omits the first two sign conditions. Specify +1 on X and signs +, −, +, … with strictly decreasing weights on the other coordinates. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/stationary-point-with-large-period.knowl.md#L15) · [SteepParameters.lean:74](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Appendix/DiscreteSeries/SteepParameters.lean#L74)

<a name="page-filling-data-of-admissible-data"></a>

## Filling data of admissible data

Added · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/filling-data-of-admissible-data.knowl.md) · [FillingData.lean:461](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/FillingData.lean#L461)

The criterion for M-divisibility uses both conjugate places above each level prime and coprimality of the two primes. The level comparison takes the preimage along inclHFin, with integrality already contained in the level congruence. The archimedean systems are chosen with their asserted discrete-series type.

<a name="page-norm-bound-from-the-length-at-the-section"></a>

## A norm bound from the Bessel length at the Gram section

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/norm-bound-from-the-length-at-the-section.knowl.md) · [OpenCellBound.lean:230](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellBound.lean#L230)

The coefficient of the moved-frame term is (Z′\*)⁻¹ and the correction has the positive factor 1/2. The bounds on both families of columns give R⁴, then 8nR⁴ ≤ R⁵. Left multiplication by the fixer preserves the frame box in part 2.

<a name="page-one-pairing-on-the-open-cell"></a>

## One pairing on the open cell, at all places together

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-core/one-pairing-on-the-open-cell.knowl.md) · [OpenCellPairing.lean:240](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/OpenCellPairing.lean#L240)

The real-linear adjoint conjugates the scalar weight and replaces γ by γ⁻¹ with witness γ⁻¹y′. The product L² contraction, the almost-everywhere box property and the cutoff support then give the square root of the product of the local squared bounds and the nonnegative integral error.
