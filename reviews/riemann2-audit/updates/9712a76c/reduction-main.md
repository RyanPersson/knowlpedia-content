# reduction-main

18 page records. Of 22 earlier findings, 22 are resolved. This review adds 2 findings. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/12cc7330341b6b4fb72c78b91a659e67e82a4b18/docs/riemann2/reports/reduction-main.md)

[Review overview](README.md) · [Status of earlier findings](response-ledger.tsv) · [New findings](findings.tsv)

<a name="page-reduction-main"></a>

## The reduction: data, heights, twisted lattices, three theorems and the main inequality

Revised · page · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main.knowl.md) · [MainInequality.lean:104](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L104)

The chapter now carries the near-full dimension from selection through Theorem C and uses the half-dimension bound only for division. The displayed error bound uses two undefined symbols.

<a name="prior-reduction-main-1"></a>

**Resolved · medium · Identify the ramified source of the normalized Poincaré maps.** The chapter explicitly distinguishes the ramified source from the space of all forms on U(X₀). The signature of normalizedPoincare uses the ramified subspace, including in the dimension factor for the index bound. [Knowl, line 55](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main.knowl.md#L55) · [ShortAndEnough.lean:185](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L185)

<a name="prior-reduction-main-2"></a>

**Resolved · medium · Retain the near-full dimension bound when invoking Theorem C.** The chosen independent family satisfies (1 − 4/b²)d_T ≤ n ≤ d_T. Theorem C uses the stronger lower bound, cancellation uses the upper bound with h_main + F ≥ 0, and only the final division uses n ≥ d_T/2. [Knowl, line 64](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main.knowl.md#L64) · [MainInequality.lean:134](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L134)

<a name="new-reduction-main-1"></a>

**New finding · low · Define the two errors in the chapter’s cancellation inequality.** The newly displayed n m rem ≤ d_T(4F + 2I) introduces I and uses F, but neither symbol is defined on the chapter page. The index estimate immediately before it is d_T times I, so treating I as the whole index changes the scale by d_T. Define F = f a (log b)⁴ and I = 10 log(1 + 2b²) f a (log b)³, and identify c + 2δ as the quantity Theorem C bounds below. [Knowl, line 64](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main.knowl.md#L64) · [MainInequality.lean:97](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L97)

<a name="page-covolume-bound"></a>

## Covolume bound for a family in a twisted lattice

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/covolume-bound.knowl.md) · [TwistedLattice.lean:275](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L275)

The exterior-power interpretation and the example (1, i) distinguish the complex Gram determinant from real lattice area. The logarithmic restatement still needs to handle zero.

<a name="prior-covolume-bound-1"></a>

**Resolved · medium · A complex Gram determinant need not be a squared lattice covolume.** The text now describes the squared Hermitian norm of the wedge. The complex Gram determinant for (1, i) vanishes, although its real lattice is the square lattice of area one. [Knowl, line 26](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/covolume-bound.knowl.md#L26) · [TwistedLattice.lean:275](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L275)

<a name="new-covolume-bound-1"></a>

**New finding · low · Qualify the logarithmic interpretation at a vanishing Gram determinant.** CovolumeLe asks for |det| ≤ exp(c) and admits dependent families. For the page’s own family (1, i) the determinant vanishes at every conjugate, so c = −1 is a valid bound. The ordinary logarithm of zero is undefined, and Lean’s real convention log 0 = 0 would make the stated logarithmic inequality false. State that c bounds the ordinary logarithm when the determinant is nonzero, or explicitly give the extended logarithm the value −∞ at zero. [Knowl, line 26](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/covolume-bound.knowl.md#L26) · [TwistedLattice.lean:275](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L275)

<a name="page-colength-bounds-length"></a>

## Over a discrete valuation ring, a colength bound bounds a length

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/colength-bounds-length.knowl.md) · [Colength.lean:216](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Colength.lean#L216)

The Smith normal form bounds the length of the image of M in V/N. This image is isomorphic to M/(M ∩ N), including when N is not contained in M.

<a name="prior-colength-bounds-length-1"></a>

**Resolved · low · relLength denotes the length of the quotient.** The concluding sentence identifies relLength M N as the length of the quotient. Its defining Lean expression is length A (S ⧸ T.submoduleOf S), with values in ℕ∞. [Knowl, line 44](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/colength-bounds-length.knowl.md#L44) · [FittingIdealsAndLengths.lean:95](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/FittingIdealsAndLengths.lean#L95)

<a name="page-colength-divides"></a>

## Colength dividing an element

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/colength-divides.knowl.md) · [Colength.lean:34](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Colength.lean#L34)

The determinant-divisibility predicate quantifies over all finite families in arbitrary M. The separate length estimate chooses a finite generating family for M.

<a name="prior-colength-divides-1"></a>

**Resolved · low · The linked length proof assumes finitely generated M.** The link to the length bound now explicitly assumes M is finitely generated, matching hM : M.FG in ColengthDvd.relLength_le. [Knowl, line 28](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/colength-divides.knowl.md#L28) · [Colength.lean:217](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Colength.lean#L217)

<a name="page-data-derived-quantities"></a>

## Derived quantities of the data

Revised · notation · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/data-derived-quantities.knowl.md) · [AdmissibleData.lean:246](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L246)

The defined positive shifted quantity is κ+(j+½)Δ. Specializing the lift-character weight instance at an infinite place gives its negative. Both the revised summary and the table preserve this distinction.

<a name="prior-data-derived-quantities-1"></a>

**Resolved · high · The character of lift j has weight −κⱼ.** The table and summary distinguish κⱼ from the character’s weight −κⱼ. The tame twist has weight zero in the cited instance. [Knowl, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/data-derived-quantities.knowl.md#L31) · [LevelAndTwists.lean:342](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L342)

<a name="page-data-exist"></a>

## Existence of the data at every large integer x

Revised · outline · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/data-exist.knowl.md) · [Existence.lean:898](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L898)

The logarithmic window and both ingredients of the conductor comparison agree with their declarations. The construction uses a positive modulus q₀d and the two rank choices remain the least powers satisfying their stated lower bounds.

<a name="prior-data-exist-1"></a>

**Resolved · medium · The different bound and the size of b give separate inequalities.** The norm of the different gives rd_E ≤ q₁d, as in AdmissibleData.lean:284. The revised sentence separately invokes the large-scale lemma with s ≤ 32 log x and W⁶ ≤ log b, giving q₁d ≤ b. [Knowl, line 35](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/data-exist.knowl.md#L35) · [Existence.lean:705](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L705)

<a name="prior-data-exist-2"></a>

**Resolved · low · State the positive modulus in the prime-window input.** The modulus is now a positive integer divisible by four and A a fixed natural. The bounds on U, k and M′ᵏ are those of the prime-window theorem. [Knowl, line 33](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/data-exist.knowl.md#L33) · [Primes.lean:389](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L389)

<a name="page-data-sizes"></a>

## Sizes of the data

Revised · outline · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/data-sizes.knowl.md) · [Sizes.lean:87](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Sizes.lean#L87)

The added tower argument proves the square-root bound: with h = log x₁, the scale estimates give h³ ≥ 6·81² and (log x₁)⁶ ≤ log b. The generator argument uses exactly f positive factors and their geometric mean.

<a name="prior-data-sizes-1"></a>

**Resolved · medium · The last estimate in the scale row needs the tower bound.** The proof includes l₀ ≤ 81s and s ≤ 32 log x ≤ log x₁. The resulting 3·81²(log x₁)³ ≤ (log b)/2 exponentiates to the asserted fifth estimate. [Knowl, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/data-sizes.knowl.md#L31) · [Sizes.lean:87](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Sizes.lean#L87)

<a name="prior-data-sizes-2"></a>

**Resolved · low · The root-discriminant estimate has a direct proof and knowl.** The new link and declaration identify the product rd_Eᶠ = ∏ᵥ |δ_E|ᵥ. All f factors lie between x¹⁰ and x¹², and f is positive. [Knowl, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/data-sizes.knowl.md#L31) · [ChosenPlaces.lean:433](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L433)

<a name="page-gain-normalisation"></a>

## Divisibility errors, gain exponents and the factor c_B

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/gain-normalisation.knowl.md) · [ShortAndEnough.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L56)

The error estimate quantifies over every finite set of natural numbers. Deleting 0 has no effect on the weighted sum under the convention now stated.

<a name="prior-gain-normalisation-1"></a>

**Resolved · low · Give the logarithm convention for sums over all natural numbers.** The knowl specifies log 0 = 0 for the natural-number indices, so the expression err₀ log 0 is defined even when U contains 0. [Knowl, line 16](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/gain-normalisation.knowl.md#L16) · [ShortAndEnough.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L56)

<a name="page-grh"></a>

## Main theorem in half-plane form: Dirichlet L-functions do not vanish to the right of the critical line

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/grh.knowl.md) · [OneSidedBound.lean:239](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L239)

The theorem refers to the half-plane proposition with the principal-character pole exception. The corpus has a single front-matter owner for the proposition, and this theorem page links to it.

<a name="prior-grh-1"></a>

**Resolved · low · The proposition name has two resolver destinations.** The theorem now claims only New.grh. Its statement refers to the unique DirichletLNonvanishingRightOfHalf owner in reduction-zeros, and the duplicate alias has also been removed. [Knowl, line 10](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/grh.knowl.md#L10) · [Statements.lean:6](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L6)

<a name="page-height-bound"></a>

## Height bound for a family of complex numbers indexed by the finite places

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/height-bound.knowl.md) · [Heights.lean:41](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L41)

For a rational z ≠ 0, multiplying by 1/z makes each finite-place value one. All complex automorphisms fix z, so the product formula with c′ = log|z| supplies the opposite inequality and the minimum is attained.

<a name="prior-height-bound-1"></a>

**Resolved · medium · The Weil-height comparison fails already for a rational constant.** For z=2 the displayed witness H=1/2, α=−log 2 and zero prime exponents satisfies each clause of HeightLe. The cited second product-formula clause gives c ≥ −log|z| for every nonzero rational constant. [Knowl, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/height-bound.knowl.md#L31) · [Heights.lean:225](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L225)

<a name="page-inverse-ratio-height"></a>

## The height of Z(1)/Z(xi) for a regular family of twists

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/inverse-ratio-height.knowl.md) · [LongForms.lean:139](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L139)

The determinant on the good source matches the chain factorisation. The inverse scalar has exponent −d_T and the sum of the m single-lift estimates supplies −mk h_dir.

<a name="prior-inverse-ratio-height-1"></a>

**Resolved · medium · Identify the restricted map in the single-lift determinant.** At both the trivial twist and the j-th power of the chosen twist, the text now restricts the single lift to the good forms on W_j before forming det(u\* u), exactly as liftDeterminant uses goodLift. [Knowl, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/inverse-ratio-height.knowl.md#L15) · [NormOfChain.lean:73](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/NormOfChain.lean#L73)

<a name="page-log-bound-calculus"></a>

## Calculus of logarithmic bounds for the sizes of the data

Revised · notation · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/log-bound-calculus.knowl.md) · [Magnitudes.lean:238](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Magnitudes.lean#L238)

The revised propagation rules distinguish the lower and upper exponent estimates for inverses. Over a positive real F one may choose log F as a lower exponent, providing the additional hypothesis of the inverse rule.

<a name="prior-log-bound-calculus-1"></a>

**Resolved · medium · Give the hypotheses on powers and reciprocal bounds.** The page restricts the power exponent A to natural numbers, as at Magnitudes.lean:238. A lower exponent gives the reciprocal upper bound unconditionally, and the reversed implication now requires F &gt; 0. [Knowl, line 16](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/log-bound-calculus.knowl.md#L16) · [Magnitudes.lean:304](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Magnitudes.lean#L304)

<a name="page-log-product-formula"></a>

## Product formula for the rational numbers, in logarithms

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/log-product-formula.knowl.md) · [Heights.lean:53](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L53)

The product-formula proof uses prime factorizations for nonzero numerator and denominator. At zero both the infinite-place and prime terms vanish under the stated logarithm convention.

<a name="prior-log-product-formula-1"></a>

**Resolved · low · Qualify the finite-support explanation at zero.** The finite-support interpretation is now restricted to q ≠ 0. The text handles the allowed exceptional value q=0 separately using log 0=0. [Knowl, line 21](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/log-product-formula.knowl.md#L21) · [Heights.lean:53](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L53)

<a name="page-regular-family-of-twists"></a>

## Ratios of Hecke L-values, main pairs, families with small ratios and regular families of twists

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/regular-family-of-twists.knowl.md) · [FitTwists.lean:164](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/FitTwists.lean#L164)

The fixed index has 20 elements up to z=10 and then 2z elements. In clearing denominators the correct subspace is the orthogonal complement of the image of the lift from the good forms, with false lifts tested at every split place outside the level.

<a name="prior-regular-family-of-twists-1"></a>

**Resolved · medium · Specify which false lifts enter the projection bound.** The translated projection bound specifies D.e₀ and Zϑ,j⊥. Being orthogonal to all forms in that intersection killed at some split place off the level is equivalent to TestedForms.lean:380, which quantifies over every such place. [Knowl, line 30](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/regular-family-of-twists.knowl.md#L30) · [FitTwists.lean:169](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/FitTwists.lean#L169)

<a name="prior-regular-family-of-twists-2"></a>

**Resolved · low · Give the actual size of the four-block index set.** The fourth block has size max(2z−20,0). The stated criterion z≥10 for total size 2z follows, and m&lt;z implies it because m≥10⁴. [Knowl, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/regular-family-of-twists.knowl.md#L22) · [FitTwists.lean:100](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/FitTwists.lean#L100)

<a name="page-sparse-places-exist"></a>

## Existence of a large sparse set of places (Behrend's construction)

Revised · outline · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/sparse-places-exist.knowl.md) · [Existence.lean:80](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L80)

The degenerate Behrend lower bound is zero at nH=0, so an empty set suffices. For n,H≥1 the possible squared radii are at most n(H−1)²+1 ≤ nH², including the singleton case n=H=1.

<a name="prior-sparse-places-exist-1"></a>

**Resolved · medium · State the zero-denominator convention in the Behrend bound.** The convention now covers both displayed real quotients, and line 25 uses the non-strict count of radii. This agrees with the real division used for both the digit set and the sparse places. [Knowl, line 17](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/sparse-places-exist.knowl.md#L17) · [Existence.lean:83](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L83)

<a name="page-target-lattice"></a>

## The target forms as a twisted lattice

Revised · outline · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/target-lattice.knowl.md) · [IntegralTargetForms.lean:65](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/IntegralTargetForms.lean#L65)

The specified level, character and fixed Weyl weight match the LevelForm parameters defining the target lattice. The proof uses trivial stabilizers at this level for control of the Petersson pairing.

<a name="prior-target-lattice-1"></a>

**Resolved · medium · Specify the level and weight of the lifted forms.** The text gives the weight (columnsY, lastEntry m), the integral level with identity reductions at chosen places and block upper triangular reductions at Q, and the character on the diagonal blocks. [Knowl, line 18](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/target-lattice.knowl.md#L18) · [IntegralTargetForms.lean:65](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/IntegralTargetForms.lean#L65)

<a name="page-theorem-a-short-forms"></a>

## Theorem A (a): the source is spanned by integral forms with short lifts

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/theorem-a-short-forms.knowl.md) · [ShortAndEnough.lean:254](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L254)

The squared-norm estimate follows by multiplying by the positive scalar c_B² and comparing exponentials. This also applies when the image has squared norm zero.

<a name="prior-theorem-a-short-forms-1"></a>

**Resolved · low · Keep the norm inequality valid for a zero image.** The revised proof uses the scaling by exp(2 log c_B) in normSqAt_normalizedPoincare and bounds the exponent. It no longer takes the logarithm of an image norm. [Knowl, line 34](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/theorem-a-short-forms.knowl.md#L34) · [ShortAndEnough.lean:285](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L285)

<a name="page-theorem-b-enough-forms"></a>

## Theorem B: few translates span almost all of the target

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/theorem-b-enough-forms.knowl.md) · [ShortAndEnough.lean:410](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L410)

The few-maps theorem first produces translates for the full source. The dimension bound for the ramified restriction is obtained after this application.

<a name="prior-theorem-b-enough-forms-1"></a>

**Resolved · medium · Verify the full source is nonzero before applying the few-maps theorem.** The proof now invokes the source coordinate isometry for nontriviality of the full source before the few-maps theorem, matching D.sourceFormCoords.nontrivial. [Knowl, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-main/theorem-b-enough-forms.knowl.md#L24) · [ShortAndEnough.lean:414](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L414)
