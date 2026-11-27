# spanning-unfolding-a

[Incremental audit](README.md) · [Findings table](findings.tsv)

<a name="page-spanning-unfolding-a"></a>

## Spanning: unfolding, part A (cutoffs, block sums, Poincaré series and the Bessel period)

Added · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md) · [PoincareSeries.lean:734](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L734)

All 81 child knowls are linked and their 62 full and five outline labels agree with the chapter count. The Petersson identity has vol(J_M) and the stated order of its two arguments, the class count includes |H̄|(Nᵏ−1)ᶠ, and the final period map agrees with the Poincaré map in source coordinates.

<a name="finding-spanning-unfolding-a-1"></a>

**High · The second moment sums squared absolute values of Petersson products.** The chapter describes the second moment as a sum of Petersson products. In Lean it is the sum over s of ‖P\* s P‖²_HS. In coordinates this sums the squared moduli of the pairings. The pairings themselves may be complex and cancel, so summing them would not give this nonnegative moment. Say that each pairing unfolds to a block entry and that the second moment sums the squared absolute values of those entries, with the scale of the chosen P. [Translation, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L14) · [SpanningTheorem.lean:270](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L270)

<a name="finding-spanning-unfolding-a-2"></a>

**High · Theorem B bounds the dimension of the span.** Theorem B gives a finite collection of translates of the normalized map on ramified source forms whose images span at least (1−4/b²) times the target dimension. Its conclusion permits a complement of positive dimension. Saying the translates fill the space states a stronger result. Give the proportion 1−4/b², or say that the chosen translates span all but a proportion at most 4/b² of the target. [Translation, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L14) · [ShortAndEnough.lean:448](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L448)

<a name="finding-spanning-unfolding-a-3"></a>

**High · Bound frame vectors on each Bessel-length layer.** A nonzero class cutoff gives the box bound at scale R when the local Bessel length is at most b^(6n+2)R. Its entire support has no uniform frame bound. The unipotent action fixes the first frame vector, so a split diagonal dilation can make ‖y⁻¹e₁‖ arbitrarily large on a whole orbit. The cutoff partition of unity still gives a nonzero value somewhere on that orbit. Say that on the local Bessel-length layer ℓ(yᵥ) ≤ b^(6n+2)R the support lies in the frame box of radius b^(37n)R. [Translation, line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L38) · [Packing.lean:115](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L115)

<a name="finding-spanning-unfolding-a-4"></a>

**High · The Poincaré series have uniformly bounded absolute sums.** Lean proves that ∑γ |Bₐ(γg)| is bounded by a constant independent of g. This gives absolute convergence at each g. Uniform convergence of the partial sums on the whole adelic group would force the individual summands to tend uniformly to zero. For a nonzero seed, every translate has the same positive supremum norm as Bₐ, which rules this out for infinite Γ. Replace “converge uniformly” with “converge absolutely at every g, with the absolute sums bounded uniformly in g”. [Translation, line 68](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L68) · [PoincareSeries.lean:349](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L349)

<a name="finding-spanning-unfolding-a-5"></a>

**High · Normalize the generic character before identifying the Bessel period.** For a general fitting space, the Bessel character restricts to the generic unipotent character under the additional condition ȷ c_Y = −(Mϖ)⁻¹. The grading permits other choices of the nonzero real scalar c_Y with the same underlying groups. The period identity in SeriesPeriod.lean:620 needs the same condition. The data D satisfy it separately at lines 699–704. State the normalization of the Weil scalar and generic constant in Section 8. Point out that the grading of D satisfies it in Section 9. [Translation, line 76](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L76) · [SeriesPeriod.lean:143](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L143)

<a name="finding-spanning-unfolding-a-6"></a>

**Medium · State the field and admissibility hypotheses used in the unfolding steps.** The setting begins with filling data over a CM field. The partition of unity and the analytic block estimates assume that E contains a primitive 5040th root of unity and that S is admissible. The latter has structural conditions beyond the inequalities mentioned on line 30: reduction is onto and the source level is the inverse image of K(M), as specified in Setup.lean:501–505. State these standing assumptions once for the results that use them, then explain that Section 9 supplies admissibility for the data D. [Translation, line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L20) · [ReducedPoints.lean:637](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L637)

<a name="finding-spanning-unfolding-a-7"></a>

**Medium · Moving a block requires the translating pair to preserve the term set.** Stability of T is invariance under left and right unipotent multiplication. For rational elements σ,σ′ of the larger Bessel subgroup, the transport lemma separately requires γ∈T exactly when σγσ′⁻¹∈T and requires a continuous linear map implementing the kernel transformation. Arbitrary Bessel translations can change the term set. Qualify the first consequence with preservation of T by the translating pair and the corresponding linear transformation of the kernel. [Translation, line 56](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L56) · [AmplitudeSums.lean:806](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L806)

<a name="finding-spanning-unfolding-a-8"></a>

**Medium · Fitting the data also constrains the type, point and grading.** The chapter defines a fit by identifying the groups. The group identifications are consequences of a fit. The definition also asks for the local discrete-series Bessel types, the standard grading indices, an idempotent type kernel, the prescribed finite-point congruence and a central η. The same groups may be paired with incompatible types. Describe the fit as compatibility of the local types, grading and adelic point with the filling data, and present the group identifications as a consequence. [Translation, line 68](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L68) · [PoincareSeries.lean:69](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L69)

<a name="finding-spanning-unfolding-a-9"></a>

**Medium · Keep the Weyl-vector factor in the formula for the Bessel function.** The tensor product is vector-valued. For each test vector ζ, Lean expresses its scalar pairing with ζ as an integral with three factors: the conjugate type kernel, the inverse Bessel character, and t(a·ζ) for the Levi part a and a chosen linear functional t. Integrating the two scalar character and kernel factors alone loses the dependence on ζ. Say that after pairing the tensor product with ζ, one integrates the conjugate type kernel times χ_R(s)⁻¹ t(a·ζ) at a suitable real base point. [Translation, line 76](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L76) · [BesselFormula.lean:375](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselFormula.lean#L375)

<a name="finding-spanning-unfolding-a-10"></a>

**Low · Direct readers to the area that defines Bessel systems.** The companion unfolding chapter owns the filling-data notation. Bessel systems are defined in the Bessel portion of spanning-core, and the real group G₁ is defined in Lib/DiscreteSeries/Bessel/Basic.lean:235. The assertion that all objects in the setting are defined in the companion chapter sends readers to the wrong place for both. Refer to the companion chapter for the filling data and to the spanning-core Bessel-system knowl for the local analytic input. [Translation, line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L18) · [Basic.lean:1018](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L1018)

<a name="finding-spanning-unfolding-a-11"></a>

**Low · Specify the type and orbit action of replacement weights.** The weight in this change of cutoff is a nonnegative function of (γ,y), measurable in y for each γ. Its translates must sum to one under the joint action (u,u′)·(γ,y) = (uγu′⁻¹,uy). A sum-one statement on the real translates alone does not state the input to the lemma. Describe the replacement as a measurable nonnegative cutoff of the indicated joint action. [Translation, line 54](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L54) · [AmplitudeSums.lean:717](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L717)

<a name="finding-spanning-unfolding-a-12"></a>

**Low · Name the group in which the source level has index |H̄|.** The source level has this index in the inverse image of the chosen lattice stabilizer under the inclusion of H. The standard maximal level can be larger. In the application its relative index supplies the separate factor (Nᵏ−1)ᶠ in the class count. Write the index as \[ι_H⁻¹(K) : source level\] = |H̄|. [Translation, line 64](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a.knowl.md#L64) · [ReducedGroups.lean:566](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedGroups.lean#L566)

<a name="page-additivity-of-unipotent-row-entries"></a>

## Additivity of a row entry under right multiplication in the unipotent group

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/additivity-of-unipotent-row-entries.knowl.md) · [CutoffIntegral.lean:123](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L123)

The expansion of (x−1)(u−1) and the three cases c&lt;d, c=d and c&gt;d reproduce the unitary matrix identity. The last case on the diagonal uses both skewness from that identity and the zero imaginary part from the hypothesis.

<a name="finding-additivity-of-unipotent-row-entries-1"></a>

**High · The displayed levels identify the last hyperbolic pair with the middle block.** The page numbers e₁ through eϱ and assigns eϱ, eϱ\* and the middle block the same level ϱ. Its block-unitriangular condition then excludes I+iE_{eϱ,eϱ\*}, an isometry of the last hyperbolic plane that belongs to Lean’s unipotent group. The case split in the proof also uses the strict separation of these levels. Use e₀,…,e_{ϱ−1} throughout with the stated levels, or keep one-based labels and give eₐ and eₐ\* levels a−1 and 2ϱ−a+1. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/additivity-of-unipotent-row-entries.knowl.md#L15) · [BesselGroups.lean:121](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/BesselGroups.lean#L121)

<a name="page-bessel-character-extends-generic-character"></a>

## The Bessel character is a character of R(A) extending the generic character

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-character-extends-generic-character.knowl.md) · [SeriesPeriod.lean:143](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L143)

The library definition at Equivariant.lean 220 uses +ȷ/2. Conjugation fixes c_Y and negates ȷ, so the self-adjoint part of ȷc_Yσ gives exactly the Bessel character at −(Mϖ)⁻¹σ. Right translation by c_out η⁻¹ then cancels η in the evaluation of the source form.

<a name="finding-bessel-character-extends-generic-character-1"></a>

**Low · Identify the matrix used in the character trace.** The expression tr(𝔢u) assumes a particular matrix for the adelic point u. The shift is expressed in the rational basis of V, and Lean pairs it with V.ratCoordMatrix(u). In the orthonormal adelic bases the matrix of u differs by conjugation by the point of V. Specify once that u inside both traces means its rational-coordinate matrix α(u). This also places the trace and the simple-root sum in the same coordinates. [Translation, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-character-extends-generic-character.knowl.md#L31) · [Equivariant.lean:220](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Equivariant.lean#L220)

<a name="page-bessel-character-of-fitting-space"></a>

## The Bessel character of a fitting space

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-character-of-fitting-space.knowl.md) · [BesselFormula.lean:259](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselFormula.lean#L259)

The negative sign in the wave and the factor 2 Re(zᵥ) agree with the source. The standard additive character has the negative archimedean exponent, so taking its inverse gives precisely the displayed product.

<a name="finding-bessel-character-of-fitting-space-1"></a>

**Medium · Restrict the character in the summary to the Bessel group.** Lean defines the formula on the full adelic group G but proves multiplicativity for r and r′ in R(𝔸). The simple-root sum is additive on that subgroup. For example, multiplying an arbitrary matrix g by the central −I negates its simple-root sum, although χ(−I)=1. This reverses any nonreal value of χ(g). Describe the function on G and identify its restriction to R(𝔸) as the Bessel character. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-character-of-fitting-space.knowl.md#L5) · [SeriesPeriod.lean:82](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L82)

<a name="finding-bessel-character-of-fitting-space-2"></a>

**Medium · State the Weil scalar in the generic-character identity.** The remark leaves “matched” unspecified. The hypothesis is ȷ c_Y = −(Mϖ)⁻¹, where c_Y is fixed by conjugation and ȷ is the purely imaginary element of the Weil data. Equating c_Y alone with the right side would lose this factor. The newly translated SeriesPeriod theorem proves the extension under the displayed condition. Give the equality with ȷ and link to the companion knowl bessel-character-extends-generic-character. [Translation, line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-character-of-fitting-space.knowl.md#L30) · [SeriesPeriod.lean:143](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L143)

<a name="page-bessel-function-as-one-integral"></a>

## The Bessel function as an integral over the real Bessel group

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-function-as-one-integral.knowl.md) · [BesselFormula.lean:375](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselFormula.lean#L375)

The local integrand uses the coefficient at x⁻¹ry, the negative wave and the inverse Levi action. Combining the integral of their tensor product with the bilinear coordinate pairing gives the stated linear form, whose scalar divides by the nonzero product of formal degrees.

<a name="finding-bessel-function-as-one-integral-1"></a>

**Low · Separate the real constants from the Levi integration variables.** The same aᵥ denotes the real local normalization factor outside the product integral and the U(κ) component inside repᵥ(aᵥ⁻¹). Lean keeps the real constants a v distinct from the second components of the integration points. Write λᵥ for the real constants and (rᵥ,hᵥ) for the integration variables. The product outside the integral is ∏ᵥλᵥ and the Levi action is repᵥ(hᵥ⁻¹). [Translation, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-function-as-one-integral.knowl.md#L31) · [BesselFormula.lean:397](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselFormula.lean#L397)

<a name="finding-bessel-function-as-one-integral-2"></a>

**Low · Link to the analytic idempotent-kernel definition.** Here the proof needs e(1) ≠ 0 to divide by the product of the formal degrees. The concept placeholder denotes an idempotent element of a ring and only specifies e² = e. Point “idempotent kernel” to the analytic definition New.IsIdempotentKernel or to a knowl stating its fields. [Translation, line 37](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-function-as-one-integral.knowl.md#L37) · [IdempotentKernel.lean:205](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/IdempotentKernel.lean#L205)

<a name="page-bessel-quotient-as-union-of-class-quotients"></a>

## The quotient \[R\] modulo the level is the disjoint union of the quotients U_c backslash R(F_infinity)

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-quotient-as-union-of-class-quotients.knowl.md) · [SeriesPeriod.lean:546](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L546)

The class decomposition gives A = δ c_out k for A = a_f η. After the Levi embedding, k A⁻¹ = c_out⁻¹δ⁻¹ gives the claimed product of k with the inverse approximation error. The weighted decomposition of the quotient gives precisely one nonzero Haar factor for every class.

<a name="finding-bessel-quotient-as-union-of-class-quotients-1"></a>

**Medium · Restrict conjugation into the principal level to the indicated Levi subgroup.** The proof says the finite unipotent character is trivial on elements conjugate into K(M). The cited lemma permits conjugation by the image of the finite unitary group H, which preserves the simple-root character. Conjugation by an arbitrary ambient torus element can rescale a simple-root coordinate. Say that ι(η)⁻¹ v ι(η) belongs to K(M) for v = α(u)_f. Apply the cited lemma with its first argument equal to 1 and its Levi variable equal to η to obtain χ(v) = 1. [Translation, line 34](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-quotient-as-union-of-class-quotients.knowl.md#L34) · [BesselLevelStructure.lean:775](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L775)

<a name="page-class-cutoff-translates-sum-to-one"></a>

## The class cutoffs: translates sum to one, support in boxes

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one.knowl.md) · [Packing.lean:134](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L134)

The partition sum runs over the full congruence group after the initial cutoff is averaged over the frame fixer. I checked the reduction of the Gram–Schmidt matrices and the Bessel-length invariance used to place a translate in the cut.

<a name="finding-class-cutoff-translates-sum-to-one-1"></a>

**Low · Qualify the frame-box support assertion in the summary.** Item 3 puts the frame in a box of radius b^(37n)R only under the length bound b^(6n+2)R. Without such a bound, a nonzero cutoff controls the frame by b^27 times the variable Bessel length. The summary can read as support in fixed boxes on the whole real group. Say that on each Bessel-length sublevel the cutoff is supported in the corresponding frame box. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/class-cutoff-translates-sum-to-one.knowl.md#L5) · [Packing.lean:115](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L115)

<a name="page-class-sections-and-class-weights"></a>

## Class sections and class weights on the Bessel group

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/class-sections-and-class-weights.knowl.md) · [SeriesPeriod.lean:483](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L483)

The class point is j_Y(c_out η⁻¹), and the correcting level element is x_c⁻¹u_f x_c. The normalization of the class cutoff uses the field hypothesis in the translated partition theorem.

<a name="finding-class-sections-and-class-weights-1"></a>

**Medium · State the field hypothesis for the cutoff partition.** Item 4 assumes admissibility of S over a CM field. The cited partition also assumes E contains a primitive 5040th root of unity. The specialization at SeriesPeriod.lean 222 obtains this separate hypothesis from fixed Weil data, and the definition of admissibility supplies only level, reduction, and size conditions. Add the primitive 5040th-root hypothesis to item 4, or place this property in the setting of a CM field with the fixed Weil data of SeriesPeriod.lean. [Translation, line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/class-sections-and-class-weights.knowl.md#L29) · [Packing.lean:134](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L134)

<a name="page-climbing-common-vectors-modulo-a-place"></a>

## Climbing modulo a place above M

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/climbing-common-vectors-modulo-a-place.knowl.md) · [Climbing.lean:1044](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L1044)

At the chosen sign the reduced Eichler map has the rank-one correction r(fx)m. The same-sign components away from the selected place are identity, and those components suffice to test equality in the residue group.

<a name="finding-climbing-common-vectors-modulo-a-place-1"></a>

**Medium · Lift the coordinates of the covector before extending it linearly.** The text calls m a linear form on the residue space, then sets the integral linear form to ℓ composed with m. The section ℓ is a set map. For nonzero m this composite on the residue space cannot even be additive into the torsion-free integral adeles. Lean applies ℓ to each entry of the row m, and separately to each entry of the row m g. On each lattice basis vector eᵢ prescribe the values ℓ(m(eᵢ)) and ℓ(m(g eᵢ)), respectively. Extend these rows linearly over the integral adeles. [Translation, line 41](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/climbing-common-vectors-modulo-a-place.knowl.md#L41) · [Climbing.lean:991](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L991)

<a name="finding-climbing-common-vectors-modulo-a-place-2"></a>

**Low · Specify the scalar in the integral Eichler map.** The formula introduces ς and a trace-one τ without defining ς. Unitarity uses ς + conjugate(ς) = h(v,v). Also, the vanishing after reduction comes from the conjugate-linear factor h(X,y). The product with v + ςX need not itself be conjugate-linear in X. Set ς = τ h(v,v) and say that the reduction of h(X,y) is zero because every conjugate coordinate of X vanishes there. [Translation, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/climbing-common-vectors-modulo-a-place.knowl.md#L35) · [BesselLevelStructure.lean:419](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselLevelStructure.lean#L419)

<a name="page-common-vectors-of-two-flags"></a>

## Common vectors of two flags and their top index

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/common-vectors-of-two-flags.knowl.md) · [Climbing.lean:647](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L647)

The annihilator criterion fixes the entries at and above j while varying those strictly below it. The least-index convention also gives index zero for two zero coordinate vectors.

<a name="finding-common-vectors-of-two-flags-1"></a>

**Low · Give the range of the shift identity.** The page indexes both vectors from 0 through n, but wᵢ₊₁ has no entry for i = n and the unrestricted sum also appears to include wₙ₊₁. Lean takes i in Fin n and truncates x by one entry before shifting. State 0 ≤ i &lt. N and write the sum over b = 0,…,n−1. Only the term with b = i can contribute. [Translation, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/common-vectors-of-two-flags.knowl.md#L25) · [Climbing.lean:706](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L706)

<a name="page-convergence-of-poincare-series"></a>

## Uniform convergence of the Poincaré series and integrability of the cut-off Bessel functions

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/convergence-of-poincare-series.knowl.md) · [PoincareSeries.lean:349](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L349)

Fixing a rational element δ that satisfies the finite level condition and reindexing by γ⁻¹δ gives a uniform bound for the absolute sum at each g. Integrating this bound over the finite-volume quotient proves L¹ integrability on G.

<a name="finding-convergence-of-poincare-series-1"></a>

**High · A uniform bound for the absolute sums does not give uniform convergence on G.** The theorem proves pointwise absolute convergence with one bound C for all g. Its terms do not tend uniformly to zero on the full adelic group. If Bₐ(g₀) is nonzero, every translate takes this same value at g = γ⁻¹g₀. Such a point exists by orthonormality of the full Bessel coordinates and their recovery from the class-unipotent sum. The rational subgroup contains infinitely many scalar elements of norm one. Retitle the page “Uniform bound for the absolute Poincaré sums and integrability of the cut-off Bessel functions”. Keep the two numbered claims as written. [Translation, line 3](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/convergence-of-poincare-series.knowl.md#L3) · [PoincareSeries.lean:349](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L349)

<a name="page-cut-changes-kernel-little"></a>

## Pointwise bounds for the Bessel kernel and for the effect of the cut

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/cut-changes-kernel-little.knowl.md) · [AmplitudeSums.lean:380](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L380)

The cutoff support gives P(y)P(γ⁻¹y) ≥ b wherever the kernel changes. Of the three powers of i₀ in the pointwise majorant, two give the b^(−2i₀) gain and one gives decay in γ⁻¹y.

<a name="finding-cut-changes-kernel-little-1"></a>

**Low · State which part of a decay majorant is being recalled.** The description following “decay majorant” lists the pointwise properties. The definition also requires aᵥ times the quotient integral of wᵥ to be at most b^(400r²) times the local dimension. The convergence knowl refers back here for its hypotheses. Arbitrary rescaling of both wᵥ and aᵥ preserves everything listed here and can violate the integral bound. Add the integral budget, or label the display as the pointwise part of the definition and refer to the integral budget when passing to block sums. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/cut-changes-kernel-little.knowl.md#L15) · [Basic.lean:981](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L981)

<a name="page-degree-of-bessel-systems-of-the-data"></a>

## The degree of the Bessel systems of admissible data

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/degree-of-bessel-systems-of-the-data.knowl.md) · [FillingAdmissible.lean:278](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L278)

The doubled parameter contributes one difference σᵢ−σₗ per pair. The initial factors have product l!, and summing the remaining m columns gives the two logarithmic bounds. In the upper bound the lift index l+2−k is at most m, within the cited lemma’s range.

<a name="finding-degree-of-bessel-systems-of-the-data-1"></a>

**Low · The entry-difference bound also holds beyond the rank.** The opening restricts the parameter entries to indices below r. The translated auxiliary theorem bounds σᵢ−σₗ for every pair of natural numbers i&lt;l. The restriction l&lt;r is used for the finite degree product and its logarithmic bounds. Define the sequence for all nonnegative indices and restrict the degree product to its first r entries. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/degree-of-bessel-systems-of-the-data.knowl.md#L15) · [FillingAdmissible.lean:226](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L226)

<a name="page-eichler-element-with-prescribed-row"></a>

## A unipotent element of level M with one prescribed row

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/eichler-element-with-prescribed-row.knowl.md) · [ReducedPoints.lean:209](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L209)

The unimodular lattice identifies the column u from the integral linear form. The expansion correctly leaves the exceptional column free for a nonzero form and gives precisely the Ms entry in that column when the form vanishes.

<a name="finding-eichler-element-with-prescribed-row-1"></a>

**Medium · Identify the prescribed rows as rows of γ−1.** The summary says that the row of the group element γ itself is Mℓ. Its diagonal entry is actually 1, whereas ℓ vanishes there. Already for ℓ=s=0 the stated rows of γ agree with the identity. The displayed theorem adds the Kronecker delta correctly. Say that γ−1 has row Mℓ at eₐ and zero rows at the other isotropic vectors outside the exceptional column. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/eichler-element-with-prescribed-row.knowl.md#L5) · [ReducedPoints.lean:216](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L216)

<a name="page-eichler-elements-of-unipotent-congruence-subgroup"></a>

## Eichler elements of the unipotent congruence subgroups

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/eichler-elements-of-unipotent-congruence-subgroup.knowl.md) · [ReducedPoints.lean:134](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L134)

The trace-one integral parameter, the lattice-coordinate formula for M⁻¹(γ′−1), and the criterion for fixing the frame agree with Lean. The hand computation of the matrix entries mixes indexing conventions and omits a sum.

<a name="finding-eichler-elements-of-unipotent-congruence-subgroup-1"></a>

**High · Separate the last isotropic, middle and first dual levels.** The page numbers e₁ through eρ starting at 1, then uses Lean’s zero-based formula. It assigns eρ, the entire middle block and eρ\* the same level ρ. Take x=eρ, u=0 and a nonzero integral skew scalar s in the page’s own construction. The resulting γ has entry Ms at (eρ,eρ\*), which the stated equal-level rule forbids. This example works at every rank allowed by the filling data. With 1≤a≤ρ use levels a−1, ρ and 2ρ−a+1 for eₐ, the middle block and eₐ\* respectively. These put the two sides of each hyperbolic plane strictly across the middle. [Translation, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/eichler-elements-of-unipotent-congruence-subgroup.knowl.md#L35) · [BesselGroups.lean:121](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/BesselGroups.lean#L121)

<a name="finding-eichler-elements-of-unipotent-congruence-subgroup-2"></a>

**Medium · Sum the contributions when p repeats an index.** The lemma allows an arbitrary map p. Row eₐ of xu\*J is the sum of rows b of u\*J over all b with p(b)=a. The proof identifies that row with a single summand. The same multiplicity occurs when multiplying on the right by x\*J. With two equal p-values and equal nonzero contributions, the entry is twice the single contribution. Write each matrix product as a sum over the fibre of p and apply the stated vanishing hypothesis to every summand. [Translation, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/eichler-elements-of-unipotent-congruence-subgroup.knowl.md#L35) · [ReducedPoints.lean:83](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L83)

<a name="finding-eichler-elements-of-unipotent-congruence-subgroup-3"></a>

**Low · Place the conjugation on the correct matrix entry.** In x\*Ju the (b,b′) entry is the coordinate of u_{b′} at e\*_{p(b)}, with no conjugation. Its conjugate occurs in the reversed product u\*Jx. Both vanish under the hypothesis, so the conclusion survives. Identify the entry of x\*Ju directly with u_{e\*_{p(b)},b′}. Reserve the conjugate for u\*Jx. [Translation, line 33](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/eichler-elements-of-unipotent-congruence-subgroup.knowl.md#L33) · [ReducedPoints.lean:157](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L157)

<a name="page-eichler-map-is-isometry"></a>

## Eichler maps are isometries

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/eichler-map-is-isometry.knowl.md) · [ReducedPoints.lean:60](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L60)

The linear term reduces to −g Jxu\*Jux\*J and the quadratic term to Jxu\*Jux\*J, so the claimed cancellation also works over the commutative involutive ring used in the page.

<a name="finding-eichler-map-is-isometry-1"></a>

**Medium · Include the scalar and skew conditions in the summary.** The short statement claims preservation of J under the conditions on x and u alone. With the standard hyperbolic J, x=e₁, u=0, s=g=1 and τ=1/2, the resulting matrix sends e₂ to e₂+e₁, changing its norm from 0 to 2. The detailed statement imposes the missing condition on s. State that J is Hermitian, s is skew-Hermitian and g=τ+τ̄, along with the orthogonality assumptions on x and u. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/eichler-map-is-isometry.knowl.md#L5) · [ReducedPoints.lean:62](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L62)

<a name="page-existence-of-cell-rank"></a>

## A term with agreeing characters and vanishing discriminant has a cell rank

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/existence-of-cell-rank.knowl.md) · [Climbing.lean:1269](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L1269)

The three cited operations in step (c) agree with the source. Inversion swaps the coefficient pair and rescales by conjugate(ζ). For γ⁻¹ the free upper coordinates are those of X, and the pairing with y reduces to −N conjugate(Yρ)yρ. Its vanishing forces the remaining rows to kill y.

<a name="finding-existence-of-cell-rank-1"></a>

**Low · Keep the translated-frame hypothesis in the lemma’s link label.** The application correctly takes a vector γ f y. The label “vectors orthogonal to the frame” suggests that orthogonality alone puts an arbitrary vector in the frame span. A nonzero vector in the positive middle space X₀ is a counterexample to that reading. Lean uses the link isometry to kill this component of γ f y. Label the link “a translated frame vector orthogonal to the frame” and retain γ f y in the displayed step. [Translation, line 41](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/existence-of-cell-rank.knowl.md#L41) · [Link.lean:862](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Link.lean#L862)

<a name="page-filling-data-fit-the-space-y0"></a>

## The filling data of admissible data fit the space Y_0

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/filling-data-fit-the-space-y0.knowl.md) · [FillingAdmissible.lean:58](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L58)

In the block identity, multiplying the filling basis by u on all rows and by u⁻¹ on X₀ fixes its X₀ components and scales the string. In particular the exceptional column becomes eₖ₀/π̄+u z/(ππ̄), which is exactly the graded basis entry. Both level consequences use the distinguished last row.

<a name="finding-filling-data-fit-the-space-y0-1"></a>

**Low · Identify the doubled Harish-Chandra parameter.** The page calls lᵥ the Harish-Chandra parameter. In the fitting data paramW is the doubled integral parameter, with entry 2σ at the index selected by basisNumber. The linked fitting definition observes that convention, and the distinction affects the Weyl degree formula. Call lᵥ the doubled Harish-Chandra parameter. Entry i is twice entry β(i) of the target parameter at v, for the chosen basis numbering β. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/filling-data-fit-the-space-y0.knowl.md#L15) · [LabelsAndIndexTypes.lean:297](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L297)

<a name="finding-filling-data-fit-the-space-y0-2"></a>

**Low · Link to the analytic idempotent-kernel definition.** The fitting structure records all the analytic kernel conditions derived from the cusp kernel. The concept placeholder denotes an idempotent element of a ring and only specifies e² = e. Point “idempotent kernel” to the analytic definition New.IsIdempotentKernel or to a knowl stating its fields. [Translation, line 28](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/filling-data-fit-the-space-y0.knowl.md#L28) · [IdempotentKernel.lean:205](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/IdempotentKernel.lean#L205)

<a name="page-filling-data-of-admissible-data-are-admissible"></a>

## The filling data of admissible data satisfy the standing hypotheses

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/filling-data-of-admissible-data-are-admissible.knowl.md) · [FillingAdmissible.lean:743](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L743)

All eleven fields of the standing hypotheses are represented in the eight numbered items. The real-place exponent 23 follows from M≤b²² and |ϖ|ᵥ≤b, the level exponent is 30(2ϱ+2)=60n, and Nᵏ/b≤Nᵏ−1 gives the relative index bound.

<a name="finding-filling-data-of-admissible-data-are-admissible-1"></a>

**Low · The front matter assigns a conjectural name to an anonymous instance.** The authors mark New.Data.instIsAdmissibleFilling as a guess in their reference. The pinned file declares an anonymous instance whose type is D.filling.IsAdmissible. Its location and the three explicitly named supporting lemmas are verifiable from the text. The resolver relies on recorded declaration names. Use a verified generated name if available. Otherwise cite the instance by type and source line 743, and use the three explicitly named lemmas for declaration lookups. [Translation, line 10](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/filling-data-of-admissible-data-are-admissible.knowl.md#L10) · [FillingAdmissible.lean:743](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L743)

<a name="page-frame-matrices-of-unipotent-congruence-subgroup"></a>

## Frame matrices of the unipotent congruence subgroups

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/frame-matrices-of-unipotent-congruence-subgroup.knowl.md) · [ReducedPoints.lean:355](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L355)

The proof obtains integrality from the class level and uses density of the rational field in the finite adeles to build a rational dual form. Its elementary shear has the asserted orientation.

<a name="finding-frame-matrices-of-unipotent-congruence-subgroup-1"></a>

**Medium · Use the same frame indices in the proof and statement.** Line 15 defines (f₀,…,fρ)=(e₁,…,eρ,z), so fₐ=eₐ₊₁ for 0≤a&lt;ρ. The proof sets fₐ=eₐ and later takes a∈{1,…,ρ}, which omits the first allowable row and makes e₀ undefined when a=0. Use one-based frame indices f₁,…,fρ₊₁ throughout, or retain f₀,…,fρ and consistently replace the associated e-index and row conditions by a+1. [Translation, line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/frame-matrices-of-unipotent-congruence-subgroup.knowl.md#L26) · [BesselGroups.lean:137](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/BesselGroups.lean#L137)

<a name="finding-frame-matrices-of-unipotent-congruence-subgroup-2"></a>

**Low · Qualify the realization of elementary frame matrices.** The header places the divisibility claim and realization of every elementary matrix under the same hypotheses. The second part of the cited proposition assumes that E contains a primitive 5040th root of unity, as the body correctly specifies. Mention the root-of-unity hypothesis when summarizing the realization direction and identify the integer x as an algebraic integer of E. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/frame-matrices-of-unipotent-congruence-subgroup.knowl.md#L5) · [ReducedPoints.lean:308](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L308)

<a name="page-fundamental-box-for-arithmetic-unipotent-group"></a>

## A fundamental box for the arithmetic unipotent group in row coordinates

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/fundamental-box-for-arithmetic-unipotent-group.knowl.md) · [CutoffIntegral.lean:646](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L646)

I checked right multiplication, the free-before-imaginary triangular order and the row-volume exponents. The last frame factor in Λ is N^(−k) at each place, giving the displayed N^(−kf) numerator factor when the shorter row product is expressed using Λ.

<a name="finding-fundamental-box-for-arithmetic-unipotent-group-1"></a>

**Low · Specify the finite-adelic volume in the explicit covolume.** The archimedean Lebesgue covolume is fixed, but the displayed formula uses vol(Ô) without choosing a finite-adelic normalization. In this CM field Lean defines the constant as 2^f/√|disc E|. Normalizing Ô to have volume one generally changes the displayed answer. Give vol(Ô)=2^f/√|disc E| beside the formula, or specify that the adelic quotient by E has mass one for the indicated archimedean Lebesgue measures. [Translation, line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/fundamental-box-for-arithmetic-unipotent-group.knowl.md#L20) · [AdditiveCharacter.lean:128](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/AdditiveCharacter.lean#L128)

<a name="page-identity-block-of-the-bessel-subgroup"></a>

## The identity block of the Bessel subgroup

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/identity-block-of-the-bessel-subgroup.knowl.md) · [AmplitudeSums.lean:891](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L891)

For equal classes the weight supported at γ = 1 has orbit sum one because u′ = uγ. The local products of coordinates descend and their integrals give the Kronecker factors, hence precisely one unipotent covolume.

<a name="finding-identity-block-of-the-bessel-subgroup-1"></a>

**Low · Identify the character in the quotient L² space.** A coordinate transforms under left U by wave(simpleRootSum u). The invariant quantities on the ordinary quotient are Wᵢ times the conjugate of Wⱼ. The scalar-orthonormality wording suggests each coordinate separately descends as a function on U∖G₁. The displayed inner products are correct. Describe orthonormality for the U-character-equivariant functions, or state the integral identity with besselQuotMeasure on G₁. [Translation, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/identity-block-of-the-bessel-subgroup.knowl.md#L35) · [Basic.lean:665](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L665)

<a name="page-lattices-of-unipotent-row-coordinates"></a>

## The lattices of row coordinates of the arithmetic unipotent group

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/lattices-of-unipotent-row-coordinates.knowl.md) · [CutoffIntegral.lean:525](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L525)

The transposed free block gives the stated row integrality, its determinant has inverse Haar modulus N^(−f), and the pair of scales from e_b and e_b\* cancels. I checked both strict fundamental-domain volume formulas at the defining library lemmas and the separate hypotheses for the imaginary coordinate.

<a name="finding-lattices-of-unipotent-row-coordinates-1"></a>

**Medium · The imaginary-coordinate lattice requires the additivity hypothesis.** Item (iii) correctly restricts membership to elements for which right multiplication adds the chosen entry. The summary claims it for all elements. On two hyperbolic pairs take A=I+ME₁₂ and a skew matrix H with H₂₁=Mζ, H₁₂=−Mζ̄ for a primitive cube root ζ. The product of diag(A,A^{−\*}) with the upper block shear of parameter H is a level-M unipotent and has (e₁,e₁\*) entry M²ζ. Its scaled imaginary part would require the skew integer M(ζ−ζ̄)/2, whose norm in ℚ(ζ) is 3M²/4. The level M is odd. Say that every skew-lattice value is attained and that membership is proved for elements translating that coordinate additively, in particular after the required earlier coordinates vanish. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/lattices-of-unipotent-row-coordinates.knowl.md#L5) · [CutoffIntegral.lean:595](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L595)

<a name="finding-lattices-of-unipotent-row-coordinates-2"></a>

**Low · Use one row index in the frame scale and free-column count.** The same sentence fixes a in {1,…,ϱ} and then uses it as a zero-based index in λᵥ(a) and nₐ. The final isotropic row has k+1 free columns and scale κᵥ/√N. Substituting a=ϱ into the printed formulas does not give these values. The parenthetical warning calls attention to the change without specifying the conversion. Fix a in {0,…,ϱ−1} throughout this proposition, or insert a−1 in the formulas with the existing one-based basis labels. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/lattices-of-unipotent-row-coordinates.knowl.md#L15) · [Setup.lean:227](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L227)

<a name="finding-lattices-of-unipotent-row-coordinates-3"></a>

**Low · Name the Haar normalization in the lattice-volume formula.** The denominator vol(Ô) first appears as an unspecified finite-adelic volume. The real free-entry coordinates carry Lebesgue measure, so their numerical covolume is fixed. The class-lattice theorem uses 2^f/√|disc E| for vol(Ô). Define vol(Ô)=2^f/√|disc E| at its first occurrence. [Translation, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/lattices-of-unipotent-row-coordinates.knowl.md#L25) · [AdditiveCharacter.lean:128](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/AdditiveCharacter.lean#L128)

<a name="page-meet-norm-bounded-by-index-of-determinant"></a>

## The meet norm is bounded by the index of a two-by-two determinant

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/meet-norm-bounded-by-index-of-determinant.knowl.md) · [Climbing.lean:1145](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L1145)

Choosing the two terminal frame indices in their written order is legitimate. Reduction gives a nonzero kernel vector (xρ,−yρ) for the terminal two-column matrix. The quotient by its integral determinant then surjects onto the product of the meeting residue fields.

<a name="finding-meet-norm-bounded-by-index-of-determinant-1"></a>

**Medium · Include the two determinant hypotheses in the summary.** The summary asserts the bound for two integral vectors. Lean requires all earlier rows of the product matrix to vanish and the terminal determinant to be a unit in the finite adeles. The first condition is what allows the kernel relation to descend to two columns. With two zero test vectors the determinant is zero and its generalized index is zero, even though every meet norm is at least one. Qualify the summary with the preceding-row vanishing condition and the assumption that the final two-by-two determinant is a finite idele. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/meet-norm-bounded-by-index-of-determinant.knowl.md#L5) · [Climbing.lean:1147](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L1147)

<a name="finding-meet-norm-bounded-by-index-of-determinant-2"></a>

**Medium · Distinguish the coordinate pairing from the unitary form.** The prose calls the entries h-pairings. The displayed formula and Lean both use the ordinary coordinate conjugate transpose of F = (f | kf), giving Fᴴt. The actual unitary pairing is FᴴJt with the lattice Gram matrix J. For an isotropic frame vector e, its coordinate self-pairing is 1 while h(e,e) is 0. Describe Fᴴt as the matrix of standard coordinate pairings. To present a statement with the unitary form, explicitly replace the test matrix by Jt and use unimodularity. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/meet-norm-bounded-by-index-of-determinant.knowl.md#L15) · [Climbing.lean:1147](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L1147)

<a name="finding-meet-norm-bounded-by-index-of-determinant-3"></a>

**Medium · Reduce the global conjugate transpose before multiplying.** Writing the multiplier as the adjoint of the reduced t uses the wrong residue component. At a split level place p, reduction of tᴴ is the transpose of t reduced at the conjugate place. A place idempotent already distinguishes the two operations. Lean sets T = tᴴ over the integral adeles and reduces T entrywise. Write redₚ(tᴴ)(f x − redₚ(k) f y) = 0. Equivalently, its first factor is red at the opposite sign of t, transposed. [Translation, line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/meet-norm-bounded-by-index-of-determinant.knowl.md#L30) · [Climbing.lean:1124](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L1124)

<a name="finding-meet-norm-bounded-by-index-of-determinant-4"></a>

**Low · Account for conjugation in the last index equality.** The stated genIndex_eq_card applied to δ gives the index of δ. The determinant on the right is its conjugate Δ. The simplification in Lean also uses invariance of the generalized index under conjugation. Mention genIndex_star, or say that conjugation identifies the quotients by δ and by Δ. [Translation, line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/meet-norm-bounded-by-index-of-determinant.knowl.md#L32) · [HaarModulus.lean:432](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/HaarModulus.lean#L432)

<a name="page-moving-a-block-by-the-bessel-subgroup"></a>

## Moving a block by elements of the Bessel subgroup

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/moving-a-block-by-the-bessel-subgroup.knowl.md) · [AmplitudeSums.lean:806](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L806)

The bijection of index sets uses both the residual terms condition and preservation of T. The translated cutoff has orbit sums one by conjugating the class unipotent groups, and left Haar invariance then gives the transformed amplitude.

<a name="finding-moving-a-block-by-the-bessel-subgroup-1"></a>

**Medium · Include the preservation of the summation set in the summary.** The summary says that the hypotheses on the two Bessel elements and on L suffice to carry one block to the other. Blocks sum only over T. The source requires γ in T if and only if σγσ′⁻¹ is in T as a separate condition, even when T is stable under the unipotent groups. Without it the change of variables can relate different summation sets. The main statement includes it. Begin the summary with a stable set T preserved by γ ↦ σγσ′⁻¹. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/moving-a-block-by-the-bessel-subgroup.knowl.md#L5) · [AmplitudeSums.lean:810](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L810)

<a name="page-poincare-series-are-forms"></a>

## The Poincaré series are forms of the discrete series type and principal level

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/poincare-series-are-forms.knowl.md) · [PoincareSeries.lean:514](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L514)

The product of the local kernel identities fixes the full Bessel coordinate. Applying that identity to each grouped sum requires the unipotent factor to act on the left of the rational representative.

<a name="finding-poincare-series-are-forms-1"></a>

**High · Group the summands with the unipotent factor on the left.** The displayed group sums have arguments q̃u g. The cutoff identity used in the next sentence sums Bₐ(uδg), so it cannot collapse the displayed sum unless extra normalization by q̃ is proved. Lean indexes by q in G_S(E)/U but its bijection sends (q,u) to u q.out⁻¹. The kernel-fixing step at PoincareSeries.lean lines 529–532 uses δ = ρ(q.out⁻¹). For each representative q̃ take the right coset U q̃⁻¹ and set F_q(g) = ∑ᵤ Bₐ(ρ(u q̃⁻¹)g). Property 3 now applies at δg with δ = ρ(q̃⁻¹). [Translation, line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/poincare-series-are-forms.knowl.md#L30) · [Basic.lean:399](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/Basic.lean#L399)

<a name="finding-poincare-series-are-forms-2"></a>

**Low · Link to the analytic idempotent-kernel definition.** The form-construction theorem takes the continuous, integrable type kernel satisfying the normalized convolution identity. The concept placeholder denotes an idempotent element of a ring and only specifies e² = e. Point “idempotent kernel” to the analytic definition New.IsIdempotentKernel or to a knowl stating its fields. [Translation, line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/poincare-series-are-forms.knowl.md#L32) · [IdempotentKernel.lean:205](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/IdempotentKernel.lean#L205)

<a name="finding-poincare-series-are-forms-3"></a>

**Low · Supply measurability and countability in the quoted summation theorem.** The general theorem also assumes countably many measurable functions Wᵢ. The proof mentions measurability of Bₐ alone, while the theorem is applied to the grouped functions F_q. Say that Γ and its coset space are countable and that each F_q is a countable pointwise convergent sum of measurable translates of Bₐ. Include these assumptions in the statement of the cited theorem. [Translation, line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/poincare-series-are-forms.knowl.md#L32) · [RealConvolution.lean:595](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/RealConvolution.lean#L595)

<a name="page-poincare-series-of-bessel-functions"></a>

## Poincaré series of cut-off Bessel functions

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/poincare-series-of-bessel-functions.knowl.md) · [PoincareSeries.lean:255](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L255)

The support, the η conjugation in the rational translate, and the principal-level invariance all agree. The partition of unity recovers the full Bessel coordinate on the finite class coset, as in the source.

<a name="finding-poincare-series-of-bessel-functions-1"></a>

**Medium · State the hypotheses for measurability of the cutoff.** The page restricts the standing hypotheses to item 3, leaving measurability in item 2 unconditional. The cited measurability lemma uses admissibility and the primitive-root hypothesis through the class cutoff. Its reduced indicator uses a chosen residue domain, whose existence is proved for admissible data. Apply the stated assumptions also to the measurability clause of item 2. Keep the norm bound and right level invariance unconditional. Refer to the convergence proposition for the hypotheses guaranteeing that the displayed Poincaré sum converges absolutely. [Translation, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/poincare-series-of-bessel-functions.knowl.md#L25) · [PoincareSeries.lean:315](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L315)

<a name="page-poincare-series-represents-the-bessel-period"></a>

## The Poincaré series represents the Bessel period

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/poincare-series-represents-the-bessel-period.knowl.md) · [SeriesPeriod.lean:620](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L620)

The source function is equivariant because the string length 2ϱ + 1 is odd. Folding supplies vol(J), decomposition over the Bessel quotient supplies vol(J′), and their ratio rescales the linear form t in precisely this order.

<a name="finding-poincare-series-represents-the-bessel-period-1"></a>

**Low · Link the analytic idempotent-kernel hypothesis.** The proof needs continuity and integrability of e_l. The linked ring-idempotent concept only describes the equation e² = e. The fitting-space hypothesis gives IsIdempotentKernel, whose first two fields are exactly the analytic inputs used here. Link “idempotent kernel” to New.IsIdempotentKernel or to the fitting-space definition, and identify continuity and integrability as its hypotheses. [Translation, line 33](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/poincare-series-represents-the-bessel-period.knowl.md#L33) · [IdempotentKernel.lean:205](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Measure/IdempotentKernel.lean#L205)

<a name="page-ratio-of-main-and-identity-second-moments"></a>

## The ratio of the main second moment to the identity second moment

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/ratio-of-main-and-identity-second-moments.knowl.md) · [FillingAdmissible.lean:692](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L692)

The exact ratio and both final exponents agree. The logarithmic errors in the degree and masses cancel all factorial terms except f log((k−1)!). The lower coefficient is 19−15/2−1/4=45/4≥11, and the upper correction is −15/2+5/4+1/4=−6.

<a name="finding-ratio-of-main-and-identity-second-moments-1"></a>

**Medium · Keep the level and mass errors in the logarithmic estimate.** The outline describes the remainder as linear in log b and the other listed quantities. The range for log N contributes fk√(log b). Lean explicitly reserves that term in the final error estimate. It also uses the finer summed mass error log(1+b⁻⁹)−4f/N to absorb the loss from replacing Nᵏ−1 by Nᵏ. State the level error fk√(log b) and the sharper mass error from the linked remark. Distinguish those errors from the linear calculation of the main term and keep the final appeal to the size estimate. [Translation, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/ratio-of-main-and-identity-second-moments.knowl.md#L31) · [FillingAdmissible.lean:671](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L671)

<a name="finding-ratio-of-main-and-identity-second-moments-2"></a>

**Low · Distinguish the two levels in the exact ratio.** The theorem defines M=p₀p₁ but introduces a separate N in its first displayed formula without identifying it. The exact ratio uses the prime level N, whereas the two final estimates use the principal level M. The quantities d and deg in that formula are the coordinate count and the degree of the tensor product of local Bessel systems. Introduce N as the prime level, distinct from p₀ and p₁, and define d and deg before the three displays. [Translation, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/ratio-of-main-and-identity-second-moments.knowl.md#L15) · [FillingAdmissible.lean:599](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L599)

<a name="page-real-bessel-group-is-product-of-local-groups"></a>

## The real points of the Bessel group are the product of the local Bessel groups

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/real-bessel-group-is-product-of-local-groups.knowl.md) · [BesselFormula.lean:218](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselFormula.lean#L218)

Right translation by θ(1)⁻¹ gives c, its first components yield the embedding, and lifting the real Levi and unipotent parts gives surjectivity. The Haar measure on the local graph is the pushforward of du dh, so the product measure and the transported Haar measure are proportional.

<a name="finding-real-bessel-group-is-product-of-local-groups-1"></a>

**Medium · Give the integral convention for arbitrary test functions.** Item 3 asserts the equality for every function. The Lean statement quantifies over complex-valued functions using the totalized Bochner integral. For example, the constant 1 on this noncompact group with a real unipotent factor has no finite complex Haar integral, although the two Haar measures are proportional. State the identity for Haar-integrable complex functions, or retain all functions and specify that the Bochner integral is zero for a nonintegrable test. [Translation, line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/real-bessel-group-is-product-of-local-groups.knowl.md#L23) · [BesselFormula.lean:233](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/BesselFormula.lean#L233)

<a name="page-reduced-levi-group"></a>

## The reduction of U(X_0) and the index of the source level

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reduced-levi-group.knowl.md) · [ReducedGroups.lean:526](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedGroups.lean#L526)

The supported lift of every family of residue matrices lies in the lattice stabilizer because its N-adic components are trivial. The two surjective reductions have equal kernels, and admissibility identifies the pulled-back principal level with the source level.

<a name="finding-reduced-levi-group-1"></a>

**Medium · Qualify the source-level index in the summary.** The product description of H̄ holds for every filling. The separate index formula for the source level requires admissibility, which identifies that level with the preimage of K(M). The ambient group in the index is the preimage of the lattice stabilizer in H(𝔸_f). Item 3 of the body states both qualifications. State that for admissible data the order of H̄ is the index of the source level in ι⁻¹(K). [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reduced-levi-group.knowl.md#L5) · [ReducedGroups.lean:566](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedGroups.lean#L566)

<a name="page-reduced-points-give-box-partition-of-unity"></a>

## The indicator of the reduced points is a partition of unity in boxes

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reduced-points-give-box-partition-of-unity.knowl.md) · [ReducedPoints.lean:637](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L637)

The proof uses precisely the b²⁷ times Bessel-length frame box and pointwise fixer invariance. The reindexing u↦uγ₀ in the weighted sum is legitimate over extended nonnegative reals.

<a name="finding-reduced-points-give-box-partition-of-unity-1"></a>

**Medium · State the coset normalization in the partition-of-unity summary.** The summary says the translates over the entire unipotent congruence subgroup sum to one. For fixed y the indicator is one on a whole right coset of the frame fixer, so the unweighted sum counts the elements of that fixer. The source instead assumes the weight has mass one on each right coset, exactly as in item 4. Say that the indicators sum to one over representatives for the right cosets, or that their weighted sum is one for weights normalized on every such coset. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reduced-points-give-box-partition-of-unity.knowl.md#L5) · [Setup.lean:444](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L444)

<a name="page-reduced-unipotent-group"></a>

## The reduction of the Bessel unipotent group

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reduced-unipotent-group.knowl.md) · [ReducedGroups.lean:295](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedGroups.lean#L295)

The inverse adjoint uses J⁻¹(u⁻¹)ᴴJ, which preserves strict block upper triangularity. The free-entry count is (2ρ choose 2) + 2ρ(k+1) and gives the stated order over the two families of residue fields.

<a name="finding-reduced-unipotent-group-1"></a>

**Medium · Use one indexing convention for the hyperbolic levels.** The area chapter labels the vectors e₁,…,eρ. The displayed levels a and 2ρ−a use Lean’s a ∈ Fin ρ, starting at zero. With the chapter labels the formula puts eρ and z at the same level and incorrectly forces the free entry in row eρ, column z to vanish. For 1 ≤ a ≤ ρ give eₐ level a−1 and eₐ\* level 2ρ−a+1. Alternatively, explicitly relabel the vectors e₀,…,eρ₋₁ before using the current levels. [Translation, line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reduced-unipotent-group.knowl.md#L17) · [BesselGroups.lean:121](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/BesselGroups.lean#L121)

<a name="page-reduction-of-unitriangular-matrices"></a>

## Reduction of unitriangular matrices modulo a triangular discrete group

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reduction-of-unitriangular-matrices.knowl.md) · [ReducedPoints.lean:470](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L470)

The degree b−a ensures that all lower-diagonal cross terms vanish when a new entry is set. The uniqueness proof applies the unique additive translate successively to the coordinates of the quotient of two group elements.

<a name="finding-reduction-of-unitriangular-matrices-1"></a>

**Low · Drop the discreteness requirement from the title.** The algebraic reduction lemma assumes no topology on R or Γ. It applies even to the full real unitriangular group with L=ℝ and D={0}, which is nondiscrete in its usual topology for n≥2. Use “Reduction of unitriangular matrices to entrywise representatives” or refer simply to a triangular subgroup. [Translation, line 3](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reduction-of-unitriangular-matrices.knowl.md#L3) · [ReducedPoints.lean:470](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L470)

<a name="page-rigidity-of-frames"></a>

## Rigidity of frames

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/rigidity-of-frames.knowl.md) · [Packing.lean:286](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L286)

The rational frame product pairs f_b with γf_a and picks up κᵥ^(ϱ−b)κᵥ^(ϱ−a)/N in normalized coordinates. The anisotropy argument and downward induction yield the stated threshold. The two label systems need reconciling in the scale ratio.

<a name="finding-rigidity-of-frames-1"></a>

**Medium · The scale quotient is off by a power of κ for the stated row labels.** Step 3 indexes eₐ from 1 to ϱ, while f_b is zero-based. Its stated denominator |κᵥ|^(ϱ−a) is the zero-based one. For a=ϱ and f_b=z the quotient should be 1/|κᵥ|, whereas the displayed equality gives 1. The coarse lower bound used by the rigidity argument still holds. Use |κᵥ|^(ϱ−a+1) for a one-based eₐ, or reindex that induction from 0 through ϱ−1. Give the frame column a different letter from the size parameter b. [Translation, line 46](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/rigidity-of-frames.knowl.md#L46) · [Setup.lean:227](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L227)

<a name="page-scaled-siegel-constant-bound"></a>

## The scaled Siegel constant is bounded by the main second moment

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/scaled-siegel-constant-bound.knowl.md) · [FillingAdmissible.lean:539](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L539)

Squaring the covolume identity contributes |disc E|^(ϱ/2), N^(−2kf) and vol(Ô)^(−2δ), where δ=ϱ(ϱ+k). The frame-mass identity cancels these factors and the remaining volume power n=ϱ+1. This reproduces the scaled constant with |Ū|².

<a name="finding-scaled-siegel-constant-bound-1"></a>

**Low · Name the main second moment in the summary.** The summary writes the multiplier as plain M. In these filling data M denotes the principal level p₀p₁. The body and Lean inequality use the main second moment, written ℳ in the display, as the multiplier. Spell out “the main second moment” in the summary or use the same distinct symbol ℳ as the body. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/scaled-siegel-constant-bound.knowl.md#L5) · [FillingAdmissible.lean:539](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L539)

<a name="page-source-form-coordinates-of-the-data"></a>

## Source form coordinates and the good projection of a translate

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/source-form-coordinates-of-the-data.knowl.md) · [FillingAdmissible.lean:125](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L125)

The coordinate map applies the central action by u before class evaluation. For the other map, translation by s precedes the action of e₀, the codomain is the image of that action, and the multiplier is the order of the whole chosen finite group.

<a name="finding-source-form-coordinates-of-the-data-1"></a>

**Low · Specify the archimedean type of the principal forms.** The source of the displayed map is described only by its finite principal level. The linked definition of principalForms also fixes the archimedean type kernel of the data’s parameter. Omitting it makes the domain appear to include principal-level forms of arbitrary type. Say that these are the forms on Y₀ of parameter σ and principal level M, with integral doubled parameter 2σ=paramW. [Translation, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/source-form-coordinates-of-the-data.knowl.md#L22) · [Rows.lean:281](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean#L281)

<a name="page-source-forms-in-bessel-coordinates"></a>

## Source forms in Bessel coordinates and their dimension

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/source-forms-in-bessel-coordinates.knowl.md) · [PoincareSeries.lean:1013](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L1013)

The two transposes, the right action on row vectors, and the Kronecker-product change of coordinates agree. Trivial rational stabilizers give arbitrary values at the class representatives, and local nonempty indices give positive dimension.

<a name="finding-source-forms-in-bessel-coordinates-1"></a>

**Low · State the listed Kronecker product identity for product vectors.** The references and front matter assign kroneckerPi_mulVec_prod to this page. The proof uses multiplicativity of Kronecker products of matrices. The listed lemma instead describes the action on a decomposable vector and is used for the local Bessel integrands in BesselFormula.lean line 360. Add the identity (⊗ᵥ Mᵥ)(⊗ᵥ zᵥ) = ⊗ᵥ(Mᵥ zᵥ) when recording this lemma, or move its declaration to the knowl that uses that identity. [Translation, line 44](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/source-forms-in-bessel-coordinates.knowl.md#L44) · [PoincareSeries.lean:821](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L821)

<a name="page-space-fitting-filling-data"></a>

## Hermitian space fitting the filling data

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/space-fitting-filling-data.knowl.md) · [PoincareSeries.lean:69](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L69)

The rational and adelic identifications, the real homeomorphism dᵥ⁻¹xᵥgᵥp⁻¹, and the conjugation by the finite integral matrix k agree. Matching the rational Gram matrix also uses the coefficient built into the grading.

<a name="finding-space-fitting-filling-data-1"></a>

**Medium · Specify the coefficient of the grading.** The setup describes Y through the length of its string and the κ-block. Lean takes a grading with coefficient S.N, the integer N of these filling data. The Gram comparison in lines 111–115 uses the grading’s Gram identity, including the central string vector’s norm −N. The standard labelling alone fixes only the positions of the blocks. Specify that Y is a grading of V with coefficient S.N, in which the middle string vector has norm −S.N. [Translation, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/space-fitting-filling-data.knowl.md#L14) · [PoincareSeries.lean:71](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L71)

<a name="page-summation-by-layers"></a>

## Summation by layers

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/summation-by-layers.knowl.md) · [AmplitudeSums.lean:178](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L178)

The hand integration is correct for u ≥ 1 and yields the sharper factor i/(i−ed). The library result at IntegralOperators.lean:92 specializes to A = i, c = 2 and V = 1.

<a name="finding-summation-by-layers-1"></a>

**Medium · Keep the lower bound on u in the layer bound summary.** The summary only bounds the mass of sublevels with R ≥ 1. On one point take w = K = e = d = 1, u = 1/4 and i = 3. Every displayed sublevel bound in the summary holds, yet the weighted sum is 64 and the claimed upper bound is 2. The body supplies u ≥ 1. Add “for u ≥ 1” to the summary before the sublevel bound. [Translation, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/summation-by-layers.knowl.md#L5) · [AmplitudeSums.lean:179](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L179)

<a name="page-terms-with-disagreeing-characters-contribute-zero"></a>

## A stable set of terms whose characters do not agree contributes zero

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/terms-with-disagreeing-characters-contribute-zero.knowl.md) · [Climbing.lean:584](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L584)

The twist is ψ(u)⁻¹ψ(u′). In the orbit sum the class cutoff is evaluated at u′γ⁻¹u⁻¹, while the translated stabilizer cutoff is evaluated at uy. Summing over u′ first leaves exactly one translated stabilizer sum.

<a name="finding-terms-with-disagreeing-characters-contribute-zero-1"></a>

**Medium · Qualify the twist criterion for ordinary integrals.** The last sentence asserts vanishing of the quotient integral of any continuous invariant function with a nontrivial unitary twist. For Γ trivial in the additive real line, F(y)=exp(iy) changes sign under translation by π, but its ordinary Lebesgue integral does not exist. The source uses Lean’s Bochner integral, which takes value zero on nonintegrable functions. State the ordinary criterion for functions integrable on the quotient, or specify Lean’s integral convention. For the actual weighted block terms, integrability is part (b) of the cited change-of-weight theorem. [Translation, line 28](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/terms-with-disagreeing-characters-contribute-zero.knowl.md#L28) · [UnfoldingInStages.lean:365](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/UnfoldingInStages.lean#L365)

<a name="page-unfolding-class-cutoff-against-invariant-weights"></a>

## Unfolding a class cutoff against unipotent-invariant weights

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/unfolding-class-cutoff-against-invariant-weights.knowl.md) · [AmplitudeSums.lean:155](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L155)

With the chosen cutoff on G₁, the action map preserves the product measure. The inner integral of βc gives the class-independent unipotent covolume. Tonelli then separates the product of invariant nonnegative local weights.

<a name="finding-unfolding-class-cutoff-against-invariant-weights-1"></a>

**Low · Give the domain of the unfolding map.** Line 19 identifies the cutoff-weighted Haar model correctly. In the general unfolding sentence the map (x,u) ↦ ux is presented using the quotient measure. If x denotes an actual coset in A∖G₁, the displayed product is undefined without a representative. The source uses G₁ × A and a measure on G₁. Specify x ∈ G₁ with the cutoff-weighted Haar measure in this map, or introduce a measurable section before using literal cosets. [Translation, line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/unfolding-class-cutoff-against-invariant-weights.knowl.md#L23) · [Basic.lean:259](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/QuotientMeasure/Basic.lean#L259)

<a name="page-unitary-group-of-x0-in-lattice-basis"></a>

## Integrality and reduction of U(X_0) in the lattice basis

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/unitary-group-of-x0-in-lattice-basis.knowl.md) · [Climbing.lean:453](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L453)

The distinguished row is divided by π and the distinguished column by its conjugate. The local unit alternative handles the entry divided twice. At chosen level places both factors are units and the reduction criterion is preserved.

<a name="finding-unitary-group-of-x0-in-lattice-basis-1"></a>

**Low · Evaluate the class sum at the chosen representatives.** The statement says to sum a function over the classes. Lean accepts any real-valued function on the finite adelic group, which need not descend to the double-coset set. Triviality of the stabilizers makes every weight one and leaves the choice of c.out in the evaluation. Write the sum as the sum of f(c.out) over classes c. For a function already defined on classes the shorter formula follows. [Translation, line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/unitary-group-of-x0-in-lattice-basis.knowl.md#L21) · [Climbing.lean:503](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L503)

<a name="page-amplitude-bounded-by-majorant"></a>

## The Bessel kernel is continuous and the amplitude is bounded by its majorant

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/amplitude-bounded-by-majorant.knowl.md) · [CutoffIntegral.lean:85](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L85)

The Euclidean tensor norm factors across both index tuples and places. The amplitude uses the real value of the product of cutoffs, and the majorant is the extended nonnegative integral of their product times the kernel norm.

<a name="page-bessel-function-paired-with-a-form-value"></a>

## The integral formula of the Bessel function paired with the value of a form

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/bessel-function-paired-with-a-form-value.knowl.md) · [SeriesPeriod.lean:281](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L281)

The left side is the bilinear coordinate pairing. Inversion in the unimodular real Bessel group changes s to s⁻¹ in the conjugate kernel, cancels the inverse character and sends the Levi action to its inverse, giving the translated class-section integrand for every form ψ.

<a name="page-block-sums-under-unipotent-reductions"></a>

## Blocks transform by the unipotent character and vanish unless s agrees

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/block-sums-under-unipotent-reductions.knowl.md) · [AmplitudeSums.lean:847](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L847)

The two rational approximations preserve the finite characters. Complex conjugation in the second tensor factor gives ψ(u)⁻¹ψ(u′), and a nonzero fixed block forces agreement. The definition in Setup also gives the displayed minus sign and Mϖ denominator.

<a name="page-change-of-weight-in-block-sums"></a>

## Change of weight in a block sum

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/change-of-weight-in-block-sums.knowl.md) · [AmplitudeSums.lean:717](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L717)

The translated orbit action preserves counting measure times Haar measure. Both weights have orbit sum one, and the orbit-measure lemma applies to the invariant kernel. Countability makes integrability in each individual term follow from product integrability.

<a name="page-climbing-common-vectors-over-the-field"></a>

## Climbing: common vectors of the frame and its image move up the flags

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/climbing-common-vectors-over-the-field.knowl.md) · [Climbing.lean:793](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L793)

The formula for the rational Eichler transformation gives uγ = γw because the two displacements agree and γ preserves h(v,v). Multiplying the simple-root sums by −1/(Mϖ) gives t times the shifted pairings. At the top the only remaining norm term is −N times the squared coefficient.

<a name="page-colouring-bound-for-weighted-sums"></a>

## Colouring bounds for weighted sums

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/colouring-bound-for-weighted-sums.knowl.md) · [ReducedPoints.lean:396](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L396)

Grouping an extended nonnegative sum by the image of the colouring gives nonempty fibres. Colouring by a tuple in K′/(K∩K′) gives the stated power of the relative index, including when the coordinate set is empty.

<a name="page-convergence-of-block-sums"></a>

## Absolute convergence of the block sums

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/convergence-of-block-sums.knowl.md) · [AmplitudeSums.lean:578](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L578)

The uniform bound is 2b^(12n³rf) times the finite product of the local aᵥ. Unfolding the remaining majorants and multiplying their local integral bounds yields b^(400r²f) times the number of coordinate tuples, giving absolute summability in each class.

<a name="page-fixers-of-frame-vectors"></a>

## Fixers of frame vectors in the residue group

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/fixers-of-frame-vectors.knowl.md) · [Climbing.lean:145](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L145)

At a conjugate place the inverse transpose fixes J f v exactly when the inverse adjoint fixes f v. The intersection defining the joint fixer uses only the selected places over the first level prime.

<a name="page-folding-of-poincare-series"></a>

## Folding: pairing a form of principal level with a Poincaré series

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/folding-of-poincare-series.knowl.md) · [PoincareSeries.lean:619](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L619)

The support is the coset x_c J_M. Right level invariance makes z(x,k) constant there, and left invariance of the finite Haar measure gives exactly vol(J_M). The finite-sum interchange uses integrability of each zB₍c,i₎.

<a name="page-gluing-integral-isometries-at-chosen-places"></a>

## Gluing integral isometries at the chosen places

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/gluing-integral-isometries-at-chosen-places.knowl.md) · [ReducedGroups.lean:257](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedGroups.lean#L257)

The idempotent and its conjugate have disjoint support. Expanding mᴴJm gives the two cross-adjoint identities, and unimodularity of the lattice Gram matrix promotes m to an integral isometry. The fixed-entry and separate-place reduction assertions both follow.

<a name="page-groups-of-a-graded-fitting-space"></a>

## The Bessel groups and the embedding of U(X_0) for a fitting space

Added · outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/groups-of-a-graded-fitting-space.knowl.md) · [PoincareSeries.lean:858](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L858)

Checking the columns in the asserted block comparison gives precisely eₐ and the middle string vector z. The κ-columns fail the string condition and the eₐ\* columns have negative grade. Centrality of η gives the claimed finite embedding, and the basis scaling is one on κ.

<a name="page-index-of-scaled-integral-lattice"></a>

## Index of a scaled lattice of integral adelic vectors

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/index-of-scaled-integral-lattice.knowl.md) · [ReducedPoints.lean:434](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L434)

The column-lattice index is the generalized index of det(cI)=c^|ι|. For an integral finite idele this is the positive ordinary index and the reciprocal Haar scaling factor used in the text.

<a name="page-integral-of-class-cutoff-is-unipotent-covolume"></a>

## The integral of a class cutoff over the real unipotent group

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/integral-of-class-cutoff-is-unipotent-covolume.knowl.md) · [CutoffIntegral.lean:728](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L728)

Taking the preimage of the row box under the product measure-preserving map computes its measure. The positive prescribed real volume rules out an infinite extended volume before recovering the integral.

<a name="page-integral-of-class-cutoff-over-fundamental-set"></a>

## The integral of a class cutoff is the measure of a set of coset representatives

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/integral-of-class-cutoff-over-fundamental-set.knowl.md) · [CutoffIntegral.lean:324](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L324)

The right-coset representative condition on B gives a left fundamental domain B⁻¹. Injectivity identifies the sum over the image with the arithmetic cutoff sum, and unimodularity gives equal measures for B and B⁻¹.

<a name="page-mean-value-bounds-for-the-main-second-moment"></a>

## Mean value bounds by the main second moment

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/mean-value-bounds-for-the-main-second-moment.knowl.md) · [FillingAdmissible.lean:517](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L517)

Cancelling the sphere masses gives NᵏᶠQ. Substitution of the class count then gives the exponent 2f on Nᵏ/(Nᵏ−1) in the second estimate. Replacing (Nᵏ−1)ᶠ by Nᵏᶠ in the first is valid because the remaining factors are nonnegative.

<a name="page-meeting-places-and-meet-norm"></a>

## Meeting places and the meet norm of a residue element

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/meeting-places-and-meet-norm.knowl.md) · [Climbing.lean:209](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L209)

The two signs give s at the chosen place and J⁻¹s⁻ᵀJ at the conjugate place. Each meeting sign supplies its own norm factor. The inverse-adjoint automorphism explains why one fixed sign over all chosen places already determines s.

<a name="page-moving-the-quotient-to-the-bessel-group"></a>

## Moving the quotient by U_c from G(F_infinity) to R(F_infinity)

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/moving-the-quotient-to-the-bessel-group.knowl.md) · [SeriesPeriod.lean:309](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L309)

The diagonal action preserves the integrand. Left invariance in x bounds its weighted absolute integral by the product of the L¹ norms of e and β_c W and a bound for y. After the cutoff swap, the substitution x = s g₀ z reproduces y at (s g₀,x_c).

<a name="page-number-of-bessel-coordinates"></a>

## The number of Bessel coordinates of admissible data

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/number-of-bessel-coordinates.knowl.md) · [FillingAdmissible.lean:157](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L157)

The Schur basis in rank k uses column heights below k. Only height one contributes, with a′=a or 0 according to the place. Its monomial count is binomial(k+a′−1,a′). Multiplying over the places and using (k+a)k≤b^(5/4) gives the stated factorial bound.

<a name="page-number-of-classes-of-the-source-level"></a>

## The number of classes of the source level

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/number-of-classes-of-the-source-level.knowl.md) · [FillingAdmissible.lean:384](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L384)

At each of the f places dividing π the inverse transpose fixes the distinguished unit vector. Its orbit has Nᵏ−1 elements. The lifted stabilizer therefore has index (Nᵏ−1)ᶠ, and the remaining index |H̄| times the standard mass gives the class count because all class stabilizers are trivial.

<a name="page-open-element-of-residue-group"></a>

## Open element of the residue group

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/open-element-of-residue-group.knowl.md) · [Climbing.lean:273](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L273)

The same single chosen place above p₀ must work for every proper leading minor. Reducing the Gram matrix gives the indicated frame submatrix of J₍w₎s₍w₎, and the full determinant of order ϱ+1 is outside the test.

<a name="page-packing-of-frames"></a>

## Packing of frames

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/packing-of-frames.knowl.md) · [Packing.lean:359](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L359)

The composition rule makes p⁻¹q a term with the required middle class. Separation in the sup norm gives 1+4Nρ² in the volume count, and the stated bounds on N, b and n give the printed power b^(6n²).

<a name="page-packing-of-weights"></a>

## Packing of weights bounded by class cutoffs

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/packing-of-weights.knowl.md) · [Packing.lean:448](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L448)

I checked the support restriction, fixed residue and class, and injection q↦γ_q⁻¹γ_p. The sum over each colour is bounded by x via the cutoff partition in the full congruence group, including extended nonnegative x.

<a name="page-petersson-products-of-poincare-series"></a>

## Petersson products of translated Poincaré series are amplitude sums

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/petersson-products-of-poincare-series.knowl.md) · [PoincareSeries.lean:734](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L734)

The source conjugates the first slot, translates Pₐ′ on the right by k, and retains Wᵢ(y) times the conjugate of Wᵢ′(γ⁻¹y). The class-coset computation selects reduction s and the finite integration contributes vol(J_M).

<a name="page-poincare-map-of-admissible-data"></a>

## The Poincaré map of admissible data is a Poincaré series of the Bessel function

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/poincare-map-of-admissible-data.knowl.md) · [SeriesPeriod.lean:695](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/SeriesPeriod.lean#L695)

The constant in gradingY is −(ȷ Mϖ)⁻¹, which gives the required equality after multiplication by ȷ. Equality against every test form uses the conjugate of that test form in the first Petersson argument and translation by the inverse lattice scale to cancel the translate in the source coordinates.

<a name="page-prescribing-residues-above-the-level"></a>

## Prescribing residues at the places above M

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/prescribing-residues-above-the-level.knowl.md) · [Climbing.lean:119](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L119)

The chosen idempotents are supported at mutually distinct places disjoint from their conjugates. Taking a + conjugate(b) sets the two signs independently, and subtracting the lift of zero produces the point-supported section with ℓ(0)=0.

<a name="page-product-of-frame-masses-and-open-cell-constant"></a>

## The product of the frame masses in terms of the Siegel constant and the open cell constant

Revised · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/product-of-frame-masses-and-open-cell-constant.knowl.md) · [FrameMass.lean:329](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FrameMass.lean#L329)

The edit links “infinite places.” The logarithmic coefficients agree: with e = ϱ + 1 + 2ϱ(ϱ+k), the coefficient of log 2 is k+e and that of log rd is ½−k−e, after division by f.

<a name="page-product-of-frame-masses-upper-bound"></a>

## Upper bound for the product of the frame masses

Revised · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/product-of-frame-masses-upper-bound.knowl.md) · [FrameMass.lean:248](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FrameMass.lean#L248)

The edit only links “infinite places.” The N-level factor, the telescoping direction and the exponent 2f agree with Lean. The previous medium finding on the unexplained numerical error budget at line 34 remains open.

<a name="page-reduced-bessel-group"></a>

## The structure of the reduced Bessel group

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reduced-bessel-group.knowl.md) · [ReducedGroups.lean:614](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedGroups.lean#L614)

The integral-level lemma passes both integrality and the congruence from uh to h. Applying it at levels 1 and M yields factorization and trivial intersection after reduction. Multiplication is therefore bijective, giving the stated product of orders.

<a name="page-reductions-are-products-over-places"></a>

## Reductions of subgroups defined by fixed entries are products over the chosen places

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/reductions-are-products-over-places.knowl.md) · [ReducedGroups.lean:362](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedGroups.lean#L362)

The given relation may prescribe any set of identity entries for a subgroup B. Gluing an integral representative, used as its own inverse adjoint, isolates its component at one chosen place and preserves every prescribed entry. The product over all places recovers the target tuple, including the Bessel specialization.

<a name="page-row-coordinates-of-real-unipotent-group"></a>

## Row coordinates on the real unipotent group

Added · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/row-coordinates-of-real-unipotent-group.knowl.md) · [CutoffIntegral.lean:295](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L295)

One-based row a has two copies of each later isotropic index and k+1 middle columns, giving 2(ϱ−a)+k+1 complex coordinates per place, plus one real imaginary coordinate. The local free-entry measures push forward to Lebesgue measure and regrouping by rows preserves the product.

<a name="page-scalar-coset-of-bessel-subgroup"></a>

## Scalar coset of the reduced Bessel subgroup

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/scalar-coset-of-bessel-subgroup.knowl.md) · [Climbing.lean:280](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Climbing.lean#L280)

A single element of the reduced Bessel subgroup supplies all components before multiplication by the residues of ζ. The input ζ can be any integral finite adele. Existence of the required invertible components forces the relevant residues to be units.

<a name="page-scaled-bessel-length-product"></a>

## Product of the scaled Bessel lengths

Added · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/scaled-bessel-length-product.knowl.md) · [AmplitudeSums.lean:206](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L206)

The Lean length uses the L² operator norm and an infimum over the Bessel subgroup. The finite product has local factors at least one, so bounding the product by R bounds every local length by b^(6n)R.

<a name="page-sum-of-cutoffs-with-inverse-length-powers"></a>

## Sums of class cutoffs over terms, weighted by inverse powers of the length

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/sum-of-cutoffs-with-inverse-length-powers.knowl.md) · [AmplitudeSums.lean:227](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L227)

The sublevel packing bound uses real dimension 2nrf and e = 2. Its exponent condition simplifies to 8n &lt. R², and raising b^(6n²) to 2nrf gives the stated power 12n³rf.

<a name="page-tail-bound-for-the-cut"></a>

## Cutting the Bessel function changes the block sums little

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/tail-bound-for-the-cut.knowl.md) · [AmplitudeSums.lean:606](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/AmplitudeSums.lean#L606)

The two factors of 2 in the preliminary integral bound and the final ½ require absorbing 8 ≤ b. With |I| ≤ b^(2kf), the remaining exponents are bounded by (402r²+k³)f ≤ 2r³f, as in the source.

<a name="page-unfolding-of-poincare-series"></a>

## Unfolding of the Poincaré series

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/unfolding-of-poincare-series.knowl.md) · [PoincareSeries.lean:461](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/PoincareSeries.lean#L461)

Left Γ-invariance moves y inside each rational sum. The quotient integration formula applies to the integrable function yBₐ, and the finite sum has coefficients φₐ with no conjugation.

<a name="page-unique-coset-moving-a-point-to-a-reduced-point"></a>

## Exactly one coset of unipotent elements moves a point to a reduced point

Added · full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b4aa180eb8c6458b06da8af94de844de0e5e2d91/content/proofs/grh/spanning-unfolding-a/unique-coset-moving-a-point-to-a-reduced-point.knowl.md) · [ReducedPoints.lean:557](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/ReducedPoints.lean#L557)

The basis-scale factors in T(y)=T(uy)θ(u) cancel at the summation index. Right multiplication by θ(u⁻¹) and the frame-fixing kernel consequently give the right coset U⁰_c(M)u₀ in the displayed order.
