# upper-divisibility

This area contains 60 individual knowls and a chapter page. The review records 40 comments. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports/upper-divisibility.md)

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Chapter page

<a name="page-upper-divisibility"></a>

### Upper bound: divisibility and size of the composite lift

Correction recorded · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility.knowl.md) · [LocalDivisibility.lean:494](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/LocalDivisibility.lean#L494)

The main local estimate uses a small-colength submodule and twists prime to p. The factor 2∑gain(p)log p, its positive sign in the archimedean bound and its cancellation on normalization all agree with the source.

<a name="upper-divisibility-finding-1"></a>

**Medium · Only a selected sparse subset of class −1 receives weight b.** The parallel descriptions of the a- and b-places suggest that both are entire residue classes. All class-1 places are a-places, whereas the b-places are selected inside class −1 and satisfy a sparseness condition. Other class-−1 places receive a/x₁. This distinction changes the total F(p) used without definition at line 27. Name Φ_b as the chosen sparse subset of class −1 and define F(p)=∑σ sₚ(w(σ),σ) when displaying the gain. [Knowl line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility.knowl.md#L23) · [AdmissibleData.lean:128](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L128)

<a name="upper-divisibility-finding-2"></a>

**Medium · Full marks cover the conjugate pairs arising from a-places.** The quantified requirement is that for each a-place τ, either its induced prime or its conjugate lies in Λ. The phrase “every conjugate pair” extends this to unrelated primes above p. Marked sets in this argument also have p&lt;x₁. State that for each a-place its induced prime or its conjugate is marked, at a small exceptional nonsplit prime. [Knowl line 41](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility.knowl.md#L41) · [MarkedPrimes.lean:69](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkedPrimes.lean#L69)

<a name="upper-divisibility-finding-3"></a>

**Low · The chapter contains seven items carrying a full proof label.** The statement that all proofs are outlines conflicts with the actual item metadata: three lemmas, three propositions and a construction are marked full. One is the identity summing the gains cited in this very chapter. Describe the principal divisibility and size theorems as outlines relative to named inputs and leave the individual proof labels in force. [Knowl line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility.knowl.md#L19) · [ArchimedeanSize.lean:146](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean#L146)

## Knowls with comments

<a name="page-divisibility-bound"></a>

### Divisibility bound of a stage at a prime

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/divisibility-bound.knowl.md) · [JetExponent.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/JetExponent.lean#L56)

The three terms in the partner contribution and the half-weight correction at d agree with predictedDivisibility. The remark describes a stronger lift estimate than the one obtained from that formula.

<a name="divisibility-bound-finding-1"></a>

**High · Erasing long rows does not give the stated lift valuation by itself.** The remark says the stage lift is divisible to db for the chosen set of erased places. The charged-jet theorem actually bounds the norm by p^(fillingCharge−db), under a condition on the charges for all partners. The neighbor lift also pays the Hecke and low-column costs. The direct p^(−db) bound in ValuationAtNonSplitPrimes.lean:66 is for the empty set and standard data at a non-split prime. Describe db as the contribution to the exponent before charges. State the direct estimate for the empty set, and give either the fillingCharge−db jet exponent or the full marked-neighbor exponent when explaining nonempty sets. [Knowl line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/divisibility-bound.knowl.md#L35) · [Divisibility.lean:256](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Divisibility.lean#L256)

<a name="divisibility-bound-finding-2"></a>

**Low · The base-p logarithm is undefined at two admitted inputs.** The page quantifies over natural p, including 0 and 1. Its displayed ordinary logarithm to base p is undefined there, whereas the source uses the total real logb. Restrict the mathematical presentation to p prime, or supply the total logarithm convention at p=0 and p=1 for the extension to natural indices. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/divisibility-bound.knowl.md#L30) · [JetExponent.lean:61](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/JetExponent.lean#L61)

<a name="page-hecke-cosets-as-edges"></a>

### Cosets of a Hecke operator at a split prime as edges

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/hecke-cosets-as-edges.knowl.md) · [HeckeEdges.lean:335](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/HeckeEdges.lean#L335)

The parahoric condition comes from the upper-right block of d⁻¹βd. The factorization γₑ=βd gₑ⁻¹ and integrality away from the marked pair follow from the chosen representatives.

<a name="hecke-cosets-as-edges-finding-1"></a>

**High · The edge steps parametrize δKₗ, not Kₗδ.** Part 2 calls the cosets right cosets, but δ⁻¹δ′ ∈ Kₗ tests equality of the left cosets δKₗ. At g=1, k=2, r=1 all steps βd give the same right coset Kₗβd=Kₗd; β=1 and an upper unipotent with upper-right entry 1 give distinct left cosets because the latter matrix is outside Pᵣ. Put Kₗ=GLₙ(Oₗ), write δ_g(β)Kₗ throughout part 2, and call these left cosets, or cosets modulo right multiplication by Kₗ. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/hecke-cosets-as-edges.knowl.md#L26) · [HeckeEdges.lean:240](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/HeckeEdges.lean#L240)

<a name="page-all-lifts-become-direct"></a>

### At N all lifts become direct lifts after a power of U

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/all-lifts-become-direct.knowl.md) · [ValuationAtLevel.lean:410](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtLevel.lean#L410)

The scalar is uniform in the input data and the ramified vector. Its product includes all commutation factors with l&lt;2i+2, and each pair contributes at most N^(2fb), yielding N^(mfb).

<a name="all-lifts-become-direct-finding-1"></a>

**Medium · The quoted chain identity has a different source.** The proof and its status paragraph attribute the three principal inputs to CharactersAtLevel.lean. The gluing-to-direct-chain induction is in LiftLawsModuloN.lean, while the local Weil-action and double-gluing formulas are in Columns.lean. The norm-comparison citation in step 1 also omits the IsSplitLevel namespace. Cite LiftLawsModuloN.lean:895 for step 5, Columns.lean:292 and :522 for steps 2 and 4, and New.IsSplitLevel.norm_detCharAt_diagN_anti at Columns.lean:341 for step 1. [Knowl line 47](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/all-lifts-become-direct.knowl.md#L47) · [LiftLawsModuloN.lean:895](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L895)

<a name="page-allowed-loss"></a>

### Allowed loss at a prime and its total

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/allowed-loss.knowl.md) · [Estimates.lean:342](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean#L342)

The four candidate values for a fixed denominator and the factor 4 in T reproduce the source’s bound for the nonzero summands. The admissibility scales also make the final harmonic estimate valid.

<a name="allowed-loss-finding-1"></a>

**Medium · Assign denominators only to the nonzero losses.** The proof says every term in every finite U can be assigned to one of four slots per c≤x₁. An arbitrarily large U can have more than 4⌊x₁⌋ elements. The source bounds every unserved value by zero instead. With U allowed to contain zero, the ordinary-real expression 0·log 0 also needs a convention. Define the weighted term to be zero whenever the allowed loss vanishes and discard those terms, including p=0, before assigning the remaining primes and N to slots. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/allowed-loss.knowl.md#L29) · [Estimates.lean:357](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean#L357)

<a name="allowed-loss-finding-2"></a>

**Low · The last numerical inequality also uses a lower bound on log x₁.** The single relation L⁶≤log b with L=log x₁ does not by itself imply 16L(1+L)≤log b. For example L=log b=1 satisfies the former inequality and violates the latter. Use the available scale bound L≥3 to give 16L(1+L)≤L⁶≤log b, or cite the full size comparison as done in Estimates.lean:393. [Knowl line 41](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/allowed-loss.knowl.md#L41) · [Magnitudes.lean:77](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Magnitudes.lean#L77)

<a name="page-chain-of-lifts-as-a-sum-over-classes"></a>

### A chain of lifts is a plain sum over classes

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/chain-of-lifts-as-a-sum-over-classes.knowl.md) · [ChainValuation.lean:156](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainValuation.lean#L156)

The double classes and the order of the kernel factors match. Freeness removes each stabilizer weight once the combined integrand is constant on its double classes.

<a name="chain-of-lifts-as-a-sum-over-classes-finding-1"></a>

**Medium · The class sum is taken after the integrands are combined.** The proof starts by treating each single lift as a sum over the stated level classes. For a fixed x the integrand can vary on a K_j-coset. Joint invariance proves right K_j-invariance of the sum over x, with the last kernel included, before its integral is evaluated as a class sum (lines 253–267). Start with the class integral. Sum the integrands over x, apply joint invariance to that sum, and then use trivial stabilizers to replace its integral by the unweighted sum. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/chain-of-lifts-as-a-sum-over-classes.knowl.md#L27) · [LiftChains.lean:253](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L253)

<a name="page-data-of-a-weak-chain-datum-are-standard"></a>

### The data of a weak chain datum are standard above a prime

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/data-of-a-weak-chain-datum-are-standard.knowl.md) · [ChainValuation.lean:174](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainValuation.lean#L174)

The four displayed conclusions agree with the source. In particular the split into conjugation-stable supports kills the Heisenberg phase, and the standard-data argument uses admissibility for the twist norm times N.

<a name="data-of-a-weak-chain-datum-are-standard-finding-1"></a>

**Medium · The advertised projection lemma is missing.** The declaration list includes projOn_translateDatum. The page ends its four claims without stating that projection onto the vacuum at S fixes a translated datum whenever its translation is integral on S and its conjugate. The Hecke-transfer proof invokes exactly this property (ValuationAtNonSplitPrimes.lean, lines 402–412). Add the implication that integrality of x_j at S ∪ conjugate(S) gives projOn(S) Φ⁰_{x,j} = Φ⁰_{x,j}, and identify the integral translations in the projector that fix the local vacuum. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/data-of-a-weak-chain-datum-are-standard.knowl.md#L22) · [ChainValuation.lean:103](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainValuation.lean#L103)

<a name="page-direct-lifts-lose-little"></a>

### Direct lifts at N lose little

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/direct-lifts-lose-little.knowl.md) · [ValuationAtLevel.lean:491](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtLevel.lean#L491)

The element β=(1+√(−d))/2 is the integral generator used in the source. Clearing the denominator N^(2f nⱼ nⱼ₊₁) and transporting the base points yields the claimed N^(fb) bound.

<a name="direct-lifts-lose-little-finding-1"></a>

**Medium · The local insertion depends on the vacuum projection of the input.** For general v, “replace its component” does not define the linear operator in the theorem. The Schrödinger operator is a sum of Heisenberg translates of the local vacuum projection of v. In particular its value is zero if that projection vanishes, a case that occurs in the translated-vacuum argument on this page. Define Dirⱼ(v) by applying the local Schrödinger operator of the direct datum to v and then applying the Weil action of (δⱼ,δⱼ₊₁). Explain that the local operator factors through the projection onto the vacuum. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/direct-lifts-lose-little.knowl.md#L15) · [NamedData.lean:70](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/NamedData.lean#L70)

<a name="direct-lifts-lose-little-finding-2"></a>

**Medium · The two estimates used to prove the gauge bound have incorrect qualified names.** The Fourier expansion is New.Seesaw.isAdmissibleCombination_schrodingerOp_of_reduction, and the standard-data bound is New.Parameters.mem_raises_of_standardData in UpperBound/Kernels/ThetaLiftGauge.lean:298. The direct-datum definition in line 15 also belongs to New.IsSplitLevel. All three have matching translated pages. Link the existing schrodinger-operator-admissible, gauge-bounds-for-one-lift and data-modulo-n knowls, or use their correct qualified names. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/direct-lifts-lose-little.knowl.md#L27) · [AdmissibleCombinations.lean:842](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L842)

<a name="page-elementary-divisors-of-the-scaled-hecke-operator-given-a-frobenius-cycle"></a>

### Elementary divisor bound for the scaled Hecke operator, given a Frobenius cycle

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/elementary-divisors-of-the-scaled-hecke-operator-given-a-frobenius-cycle.knowl.md) · [HeckeEdges.lean:769](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/HeckeEdges.lean#L769)

The factor p raised to a times the number of even letters, the transition matrix on the complementary factor, and the determinant-divisibility formulation give the displayed colength bound after evaluating at the class representatives.

<a name="elementary-divisors-of-the-scaled-hecke-operator-given-a-frobenius-cycle-finding-1"></a>

**Medium · Specify the inverse transpose in the origin’s quotient coordinate.** In the stated quotient GLₖ(W)/Pᵣ, the origin coordinate is gₑ⁻ᵀPᵣ. The criterion gₑᵀ(gₑ′ᵀ)⁻¹ ∈ Pᵣ compares those cosets or equivalently the opposite cosets Pᵣgₑᵀ. It does not compare gₑᵀPᵣ and gₑ′ᵀPᵣ, as the unqualified “coset of gₑᵀ” can suggest in this quotient. Write the coordinate as (o(e), gₑ⁻ᵀPᵣ), or explicitly say that Pᵣgₑᵀ is a coset on the opposite side. [Knowl line 33](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/elementary-divisors-of-the-scaled-hecke-operator-given-a-frobenius-cycle.knowl.md#L33) · [ElementaryDivisorTheorem.lean:1152](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L1152)

<a name="page-gain"></a>

### Gain at a prime

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/gain.knowl.md) · [ShortColumns.lean:83](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L83)

The factor m multiplies both the long-row sum and k times the weighted total over all infinite places. The later divisibility interpretation needs the domain condition from the cited theorem.

<a name="gain-finding-1"></a>

**Medium · The divisibility interpretation omits the restricted source module.** The cited theorem guarantees gain minus error on a submodule of controlled colength in the integral ramified source forms. Its quantified valuation conclusion at lines 508–509 assumes membership in that submodule. The remark describes it as a conclusion about an integral source form without this condition. Say that the divisibility holds for forms in the submodule supplied for the chosen prime and embedding, and for twists of modulus prime to p. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/gain.knowl.md#L22) · [LocalDivisibility.lean:503](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/LocalDivisibility.lean#L503)

<a name="page-gauge-and-size-of-the-restriction-to-y-m"></a>

### Gauge and size of the restriction to Y_m

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/gauge-and-size-of-the-restriction-to-y-m.knowl.md) · [ChainValuation.lean:361](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainValuation.lean#L361)

The conjugate induced place determines the last diagonal entry. Its inverse supplies the same p-adic absolute value as the restriction scalar, and the squared complex absolute value contributes N raised to minus the sum of the branch exponents.

<a name="gauge-and-size-of-the-restriction-to-y-m-finding-1"></a>

**Medium · The archimedean norm in the bound is unspecified.** The bare squared norm in part 3 is specifically the Weyl Gram norm Re(ξ\*Gξ), with the Gram matrix for the corresponding module on each side. The branching estimate invoked in the proof controls that norm. An ordinary coordinate norm does not inherit the stated constant from it. Specify the Weyl Gram norms in part 3 and link the branching-map knowl. Its defining properties are New.Data.IsBranchingMap.mul_weylRep and New.Data.IsBranchingMap.weylNormSq_le in Objects/Columns.lean, lines 681 and 690. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/gauge-and-size-of-the-restriction-to-y-m.knowl.md#L27) · [GramMatrix.lean:380](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/GramMatrix.lean#L380)

<a name="page-hecke-operator-as-a-sum-over-edges"></a>

### The Hecke operator as a sum over edges. An edge is determined by its origin

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/hecke-operator-as-a-sum-over-edges.knowl.md) · [HeckeEdges.lean:459](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/HeckeEdges.lean#L459)

Equivariance at γₑρₒuₑ gives the displayed operator formula. For origin uniqueness, conjugation of gₑ⁻¹gₑ′ by d gives the claimed integrality, and freeness then forces γₑγₑ′⁻¹=1.

<a name="hecke-operator-as-a-sum-over-edges-finding-1"></a>

**Medium · Right translation is summed over left cosets.** The proof asks for representatives of right cosets. Its action on a Kₗ-fixed form factors through δKₗ because changing δ to δk fixes the summand. Choosing representatives modulo multiplication on the left does not have this invariance. Write the sum over the left cosets δKₗ in KₗdKₗ and retain the right translation of the form by each representative. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/hecke-operator-as-a-sum-over-edges.knowl.md#L27) · [Basic.lean:307](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Hecke/Basic.lean#L307)

<a name="page-hecke-transfer-through-the-chain"></a>

### Hecke transfer through the lifts at a marked prime

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/hecke-transfer-through-the-chain.knowl.md) · [ValuationAtNonSplitPrimes.lean:770](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean#L770)

The range i′ ≤ i, coefficient sign, scaling by z^{t+1} and final factor p^{ν_p} check out. The coefficients for p^{ν_p} are guaranteed integral only through the m-th lift.

<a name="hecke-transfer-through-the-chain-finding-1"></a>

**Medium · Identify the character whose value enters the transfer polynomial.** Part 1 names a rank-twisted base change, and part 3 calls χ the unit value of “the lift character.” Lean takes χ from the unrank-twisted base change of ν_{e+1} at the uniformizer. The two rank-twisted base changes supply the unramifiedness hypotheses, while their space characters both reduce to ν_{e+1}’s base change by evenness of the ranks (lines 495–515). Confusing these values changes the factors of R. Define χ = ν_{e+1}^{BC}(ϖ_l). Explain the even-rank space-character cancellation giving the Frobenius values z^{n_e}χ and z^{n_{e+1}}χ. In the quoted pairing theorem use its actual name New.SiegelWeil.hecke_transfer_of_pairing. [Knowl line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/hecke-transfer-through-the-chain.knowl.md#L38) · [ValuationAtNonSplitPrimes.lean:490](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean#L490)

<a name="page-local-prime-sum"></a>

### Local prime sum

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/local-prime-sum.knowl.md) · [ShortColumns.lean:72](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L72)

I checked the odd and ramified exponent sets, their valuation factors, and the order argument w(σ) used for the total. The global regrouping in the remark needs a bound on y.

<a name="local-prime-sum-finding-1"></a>

**Medium · The global regrouping fails for arbitrary derivative order.** The local definition allows any real y. The global prime sum stops at ν=a, whereas the local sums include all prime powers. Choose e with d^e&gt;a and then y&gt;d^e max(w). The ramified prime-power term is positive in the local sum and omitted from the global sum. All terms are nonnegative. Qualify the identity with y≤a, as in primeSum_eq_sum_localPrimeSum. Under this hypothesis all terms with p^e≥x₁ vanish and one may sum over primes below any integer U≥ceil(x₁). [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/local-prime-sum.knowl.md#L27) · [Estimates.lean:107](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean#L107)

<a name="page-one-lift-evaluated-at-a-neighbor"></a>

### One lift, evaluated at a neighbour

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/one-lift-evaluated-at-a-neighbor.knowl.md) · [ValuationAtNonSplitPrimes.lean:304](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean#L304)

The positive sign in the diagonal contribution is correct because |p^{-ε}|ₚ = p^ε. The determinant weights cancel by balance and distinct entries in a column give at most |J| marked boxes there.

<a name="one-lift-evaluated-at-a-neighbor-finding-1"></a>

**Medium · The jet criterion ranges over the whole standard-data module.** The text says it suffices to check every vacuum translate in the given datum. The criterion quantifies over every standard f. In its proof the original datum is moved by integral group elements before testing its jets (lines 215–228), so checking only its original summands is insufficient. The charged-jet theorem actually provides the requisite uniformity. Quantify over all standard f, or use all standard vacuum-translate generators and extend by integral linearity and the ultrametric inequality. Specify the kernel's jet scale and use the New.Parameters namespace for omega_mem_raises_of_schurJet_le, norm_schurJet_jetSeries_le_of_charges and mem_raises_predictedDivisibility. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/one-lift-evaluated-at-a-neighbor.knowl.md#L27) · [ThetaLiftGauge.lean:198](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L198)

<a name="page-row-lengths-and-jet-sizes"></a>

### Row lengths of the lift diagrams and growth of the jet size

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/row-lengths-and-jet-sizes.knowl.md) · [Estimates.lean:192](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean#L192)

The row slack and its three cases agree with the truncated diagram. The actual jet estimate has a logarithmic factor per added box, and the identity for the absolute value of the conjugate uses π̄_M times its conjugate equal to M.

<a name="row-lengths-and-jet-sizes-finding-1"></a>

**Medium · The jet size does not have global linear growth.** The summary says the jet size grows at most linearly. For fixed data s∞(l)=log(l!)+l log(M/Ω), so s∞(l)/l is unbounded. Part 2 in the body correctly retains log(r′+e+1) in the increment per added box. Describe the estimate as an upper bound on the cost of e added boxes, at most e\[log(r′+e+1)+log(M/Ω)\]. A linear bound with a fixed slope requires a specified bound on row length. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/row-lengths-and-jet-sizes.knowl.md#L5) · [Estimates.lean:225](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean#L225)

<a name="page-scaled-hecke-operator"></a>

### Scaled Hecke operator at a marked prime

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/scaled-hecke-operator.knowl.md) · [MarkedPrimes.lean:472](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkedPrimes.lean#L472)

The definition has the correct scalar p^{A_l}, Hecke index and restriction of scalars. The cited elementary-divisor result controls reductions of the image at each finite p-adic precision.

<a name="scaled-hecke-operator-finding-1"></a>

**Medium · The cokernel estimate requires reduction modulo p^j.** The remark attributes a controlled length to the full cokernel on the integral module M. The cited theorem bounds the colength of T̃M + p^j M in M for each j, with a bound that grows with j. This permits a free part in the full cokernel and does not supply a finite length bound for it. Say that the scaling preserves M and bounds the colength of T̃M + p^j M in M at every specified j. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/scaled-hecke-operator.knowl.md#L22) · [MarkOperator.lean:345](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkOperator.lean#L345)

<a name="page-short-forms-span-at-a-free-level"></a>

### Short forms span at a free level

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/short-forms-span-at-a-free-level.knowl.md) · [ShortColumns.lean:369](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L369)

The delta-form reduction, degree count and C^(6M) bound agree. The proof of p-adic integrality depends on using the conjugate weight embeddings consistently in both factors of its test matrices.

<a name="short-forms-span-at-a-free-level-finding-1"></a>

**Medium · The short test vectors use conjugate weight embeddings.** The displayed A is described as using the embeddings of the CM type. Lean forms both its determinant factors and its Weyl matrix with weightEmbedding, x ↦ Φ_τ(conj x) over ℂ and x ↦ ι(Φ_τ(conj x)) over ℂ_p (ShortColumns.lean:386–389). Replacing this by Φ_τ(x) can read the other prime above p, so the claimed integral matrix after multiplying by c⁻¹ need not follow. Define the embedding used for each τ as Φ_τ composed with complex conjugation on E, and use its adelic extension in the integral determinant and Schur calculation. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/short-forms-span-at-a-free-level.knowl.md#L29) · [ValuationSubrings.lean:580](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/ValuationSubrings.lean#L580)

<a name="short-forms-span-at-a-free-level-finding-2"></a>

**Low · Several quoted estimates omit parts of their declaration names.** The two delta-form estimates are New.Rows.weylGauge_deltaForm_le and New.Rows.weylNormSq_deltaForm_le. The short-basis theorem on line 23 belongs to New.Space, and the p-adic Schur bound on line 31 belongs to New.Rows. The named declarations are the external inputs the outline asks the reader to consult. Use New.Rows for the two delta-form estimates and norm_schur_mulVec_le, and New.Space for exists_short_basis_stdSpace. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/short-forms-span-at-a-free-level.knowl.md#L21) · [PAdicGauge.lean:252](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean#L252)

<a name="page-valuation-of-a-chain-at-a-non-split-prime"></a>

### Valuation of the restricted chain on the image of the scaled Hecke operators

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/valuation-of-a-chain-at-a-non-split-prime.knowl.md) · [ValuationAtNonSplitPrimes.lean:984](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean#L984)

The local induction cancels each A_l when L reaches Λ, leaving |Λ|ν_p plus the lift loss at a stage. Iterating the data operators really does put Y^j on the input after j lifts.

<a name="valuation-of-a-chain-at-a-non-split-prime-finding-1"></a>

**Medium · The auxiliary translate must be supported on the marked pairs.** Condition (c) specifies g only at primes of Λ and leaves its other components unrestricted. Lean quantifies over a tuple of matrices at Λ and applies its unitary embedding, which is identity outside Λ and its conjugate. The cited base case for one neighbor has exactly this support hypothesis. With Λ empty the printed condition would allow every adelic g while the source tests only 1. Define g in (c) as the unitary adelic extension of a tuple at Λ, or require it to be identity outside Λ ∪ conjugate(Λ). The induction then changes just the component at the newly added prime and its conjugate. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/valuation-of-a-chain-at-a-non-split-prime.knowl.md#L29) · [ValuationAtNonSplitPrimes.lean:903](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean#L903)

<a name="page-valuation-of-chains-at-unmarked-primes"></a>

### Valuation of the restricted chain without Hecke operators

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/valuation-of-chains-at-unmarked-primes.knowl.md) · [LocalDivisibility.lean:190](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/LocalDivisibility.lean#L190)

I checked the coprimality conditions in each case and the sign in the rescaling by p^j_p. The ratio in the standard-datum argument gives 1 once the jet period normalization is included.

<a name="valuation-of-chains-at-unmarked-primes-finding-1"></a>

**Medium · Identify the normalization of the jets in the integrality argument.** The proof describes the jets as scaled by the conjugate of π̄_M. The cited estimate takes a kernel at c·jetScale, and c alone occurs in its norm ratio. The actual lift kernel in Columns.lean:859 uses this full product. Applying the displayed ratio to jets with only the stated scale omits the period normalization used for integrality. Write that the already period-normalized jets are multiplied by c=conj(π̄_M), or display the full kernel scale c·jetScale. Keep c alone in the numerator of the estimate. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/valuation-of-chains-at-unmarked-primes.knowl.md#L30) · [ThetaLiftGauge.lean:305](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L305)

<a name="page-action-of-an-edge-on-the-variables"></a>

### Action of the rational part of an edge on the weight space

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/action-of-an-edge-on-the-variables.knowl.md) · [HeckeEdges.lean:568](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/HeckeEdges.lean#L568)

The even-letter factor is p times the inverse block scaling and the odd-letter factor is the block scaling itself. The transposed monomial indices in the Schur factorization and integrality at the conjugate induced prime agree with the source.

<a name="action-of-an-edge-on-the-variables-finding-1"></a>

**Low · The diagram away from the a-places is empty at rank k.** The phrase “no column of height below k except of height k” suggests that a height-k column might contribute. The diagram sums only over h&lt;k. At a non-a-place even the height-one count is zero, so the factor is the degree-zero symmetric power. State that the diagram used by the Schur matrix on X₀ is empty at a non-a-place. Cite the height cutoff in diagramWeight and the degree-zero calculation at HeckeEdges.lean lines 675–683 in place of the uncertainty in the status note. [Knowl line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/action-of-an-edge-on-the-variables.knowl.md#L25) · [Basic.lean:69](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/Basic.lean#L69)

<a name="page-chain-datum-as-a-weak-chain-datum"></a>

### Two weak chain data attached to a chain datum

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum.knowl.md) · [ChainDatumExpansion.lean:357](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainDatumExpansion.lean#L357)

The regrouped coefficients give one weak datum working for every source form. Projecting the original glued tensor to the vacuum at the places over N separately proves the original datum is weak.

<a name="chain-datum-as-a-weak-chain-datum-finding-1"></a>

**Low · Two quoted proof inputs have incorrect declaration names.** The coefficient substitution uses New.Seesaw.IsAdmissibleCombination and its bind lemma. The commutation cited on line 26 is New.Space.omega_projOn in VacuumProjections.lean, line 587. Both links omit their intermediate namespace. Link to the existing upper-seesaw/admissible-combination-substitution page for regrouping and use New.Space.omega_projOn for the commutation. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum.knowl.md#L24) · [AdmissibleCombinations.lean:501](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L501)

<a name="page-class-number-bound-for-the-standard-lattice"></a>

### Explicit bound for the number of classes in the genus of the standard lattice

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/class-number-bound-for-the-standard-lattice.knowl.md) · [ClassCount.lean:122](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ClassCount.lean#L122)

The two matrices Y\*Y and Y\*Y X distinguish the double cosets because equality gives the integral unitary matrix A′A⁻¹. Counting their 2r² entries gives the exponent 4fr².

<a name="class-number-bound-for-the-standard-lattice-finding-1"></a>

**Low · The short-basis theorem is cited under the wrong namespace.** The quoted input supplying integral g⁻¹Y and the bound at every complex embedding is New.Space.exists_short_basis_stdSpace. The current link targets New.exists_short_basis_stdSpace. Point the citation to New.Space.exists_short_basis_stdSpace. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/class-number-bound-for-the-standard-lattice.knowl.md#L24) · [FirstMinimumShortBases.lean:892](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Reduction/FirstMinimumShortBases.lean#L892)

<a name="page-classes-of-primes"></a>

### Small non-split primes, primes congruent to plus or minus one modulo m, and exceptional primes

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/classes-of-primes.knowl.md) · [ShortColumns.lean:118](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L118)

I checked that exceptionality requires an inert character value, exclusion of both congruences, and an odd order at most the ceiling logarithm. The definition of exceptionality alone has no size cutoff.

<a name="classes-of-primes-finding-1"></a>

**Low · The natural-number domain includes undefined loss and exponent formulas.** The page explicitly includes p=0 in the preceding clause, then uses a/p and ceil(2mfa/p). The ceiling logarithm is described only for p&gt;1, leaving the transfer exponent unspecified at 0 and 1. The source defines all these functions on natural numbers. Either present the formulas only for primes or explicitly state the source conventions for division by zero and the degenerate bases of the ceiling logarithm. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/classes-of-primes.knowl.md#L18) · [ShortColumns.lean:96](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L96)

<a name="page-expanding-the-gluing"></a>

### Expanding the gluing of a chain datum

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/expanding-the-gluing.knowl.md) · [ChainDatumExpansion.lean:338](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainDatumExpansion.lean#L338)

Disjoint support above N kills the Heisenberg phase. I checked the double sum and the product of the N^(f n_{2i+1}) choices that gives the stated exponent f m n_m/2.

<a name="expanding-the-gluing-finding-1"></a>

**Low · The pole entries require a representative of each residue class.** At this point y is a residue modulo N. Writing −y/N does not specify an element of the local field. Replacing a representative by y+N changes the adelic translation tuple by an integral vector. The source takes the integer representative in \[0,N) before dividing. Specify this lift in the definition and form the conjugate of its adelic column for the last row. Link the pole column and row to New.Seesaw.poleColumn and New.Seesaw.poleRow, both already on the upper-objects chain-datum-and-composite-lift page. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/expanding-the-gluing.knowl.md#L18) · [LiftLawsModuloN.lean:62](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L62)

<a name="expanding-the-gluing-finding-2"></a>

**Low · The quoted Heisenberg composition law has the wrong namespace.** The phase law used to combine the disjoint translates is New.Space.finHeisenbergOp_finHeisenbergOp. The current reference, New.finHeisenbergOp_finHeisenbergOp, does not identify that declaration. Use the fully qualified name New.Space.finHeisenbergOp_finHeisenbergOp. [Knowl line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/expanding-the-gluing.knowl.md#L38) · [VacuumProjections.lean:102](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/VacuumProjections.lean#L102)

<a name="page-gauge-bound-for-a-chain-of-lifts"></a>

### Gauge bound for a chain of lifts with modified data

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/gauge-bound-for-a-chain-of-lifts.knowl.md) · [ChainValuation.lean:248](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainValuation.lean#L248)

I checked the support-wise commutation assumption at all stages, the raising bounds only at j &lt; m, and the use of integrality of the coefficients to preserve the ultrametric bound.

<a name="gauge-bound-for-a-chain-of-lifts-finding-1"></a>

**Low · State the domain or the positive part of the gauge factor.** The definition given for raising by C omits the source's factor max(C,0). For C &lt; 0 even the zero kernel fails the displayed prose definition on a nonzero input, whereas it belongs to the source's additive submonoid for every C. The proposition uses positive factors p^{r_j}. Restrict the explanatory definition to C ≥ 0 or use max(C,0) for arbitrary real C. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/gauge-bound-for-a-chain-of-lifts.knowl.md#L15) · [ThetaLiftGauge.lean:73](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L73)

<a name="page-level-at-n-as-a-mirabolic-group"></a>

### The level at N as a mirabolic group in a basis of L_j

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/level-at-n-as-a-mirabolic-group.knowl.md) · [SetupAtLevel.lean:199](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/SetupAtLevel.lean#L199)

Conjugation divides the last row and multiplies the last column by N precisely at w dividing π_N. At conjugate primes unitarity supplies the inverse-row condition, and applying it to k and k⁻¹ recovers integral invertibility.

<a name="level-at-n-as-a-mirabolic-group-finding-1"></a>

**Low · The mirabolic references name the wrong namespace.** The links for the group in the statement and for the two ingredients in the status paragraph use New.mirabolic, New.directDatum and New.exists_inclGL_eq. All three belong to New.IsSplitLevel, and their existing knowls use that qualified namespace. Use New.IsSplitLevel.mirabolic, New.IsSplitLevel.directDatum and New.IsSplitLevel.exists_inclGL_eq, or link the existing mirabolic-subgroup-at-split-level and data-modulo-n knowls. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/level-at-n-as-a-mirabolic-group.knowl.md#L15) · [LiftLawsModuloN.lean:206](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L206)

<a name="page-only-collisions-lose"></a>

### Only collisions lose: the divisibility bound is at least the gain

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/only-collisions-lose.knowl.md) · [JetExponent.lean:504](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/JetExponent.lean#L504)

The comparison retains the surplus at e=1 for an erased a-place, charges the ramified correction at most 2fa/(pm), and yields the stated final coefficient after the counting error.

<a name="only-collisions-lose-finding-1"></a>

**Low · The displayed gain terms need the partner-exponent restriction.** The text extends the preceding inequality outside I_p by saying its left side then vanishes. For example e=0 is excluded, but at an a-place the displayed positive part (a−w(u(−1)τ)) is positive. Lean explicitly sets each gain summand to zero outside I_p and likewise restricts the full geometric summand. Sum the displayed inequality only over e in I_p, or insert the indicator of I_p on all gain and full geometric terms before extending it to all natural exponents. [Knowl line 46](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/only-collisions-lose.knowl.md#L46) · [JetExponent.lean:442](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/JetExponent.lean#L442)

<a name="page-properties-of-marked-sets"></a>

### Properties of marked sets

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/properties-of-marked-sets.knowl.md) · [MarkedPrimes.lean:401](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkedPrimes.lean#L401)

Translation by u(−p) identifies the two fibers, which carry the same lift weight. I also checked the principal-level containment and the arithmetic input for the uniformizer assertion.

<a name="properties-of-marked-sets-finding-1"></a>

**Low · Supply the parameter-specific reason that p avoids q₁.** Inertness gives p ∤ q₁ here because every prime divisor of this particular q₁ splits in K. The proof asserts this implication immediately and its link for unramifiedness names New.intValuation_natCast_eq_exp_neg_one, whose actual namespace is New.Parameters. Cite New.Parameters.not_dvd_q₁_mul_d_of_inert for the coprimality and New.Parameters.intValuation_natCast_eq_exp_neg_one for v_l(p), or link the existing decomposition-of-primes-in-e knowl. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/properties-of-marked-sets.knowl.md#L27) · [PrimeDecomposition.lean:727](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L727)

<a name="page-ramified-source-forms-are-the-image-of-the-ramifying-operator"></a>

### Ramified source forms are the image of the ramifying operator

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/ramified-source-forms-are-the-image-of-the-ramifying-operator.knowl.md) · [ShortColumns.lean:758](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L758)

The fixed-space bound comes from the index of the overlevel containing one scalar. Rank–nullity then gives the asserted codimension upper bound for all f places.

<a name="ramified-source-forms-are-the-image-of-the-ramifying-operator-finding-1"></a>

**Low · The summary reads as an exact codimension.** “All but a proportion f/(N−1)” gives the impression of equality. The source bounds the dimension from below by (1−f/(N−1)) times the full dimension, as part 4 of the page correctly states. Say that the codimension is at most a proportion f/(N−1) of the source dimension. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/ramified-source-forms-are-the-image-of-the-ramifying-operator.knowl.md#L5) · [ShortColumns.lean:944](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L944)

<a name="page-setup-at-the-level-prime"></a>

### The places Sigma_N, the lattices L_j and the module A' at the prime N

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/setup-at-the-level-prime.knowl.md) · [SetupAtLevel.lean:34](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/SetupAtLevel.lean#L34)

The definition selects the conjugates of the induced places, with δ_j^∨ = δ_j δ_j(Σ_N)⁻¹. The power used in the preimage defining A′ is exactly ϱ+1, with no requirement that the original form already be a source form.

<a name="setup-at-the-level-prime-finding-1"></a>

**Low · The operator defining A′ links to a nonexistent declaration.** U is introduced only by reference to New.upOperator. Its definition and the existing operator knowl use New.IsSplitLevel.upOperator, so the reference cannot resolve to the operator needed to interpret the preimage. Link proofs/grh/upper-objects/up-operator or use the fully qualified declaration New.IsSplitLevel.upOperator. [Knowl line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/setup-at-the-level-prime.knowl.md#L20) · [LiftLawsModuloN.lean:200](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L200)

<a name="page-size-of-one-kernel"></a>

### Size of one kernel and of the rows of the chain

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/size-of-one-kernel.knowl.md) · [ArchimedeanSize.lean:226](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean#L226)

The one-kernel estimate uses growth rate a+1, tower factor q₁/q₀ in the constant, and the first nⱼ rows of the nⱼ₊₁ diagram. The slack term contributes once per row before the sum over places and stages.

<a name="size-of-one-kernel-finding-1"></a>

**Low · The cited row bound does not include the comparison with 2a.** The row-lengths page bounds the diagram row by main+slack. The additional inequality main+slack≤2a, used both for the analytic exponent and for the per-box cost 25 log b, comes from a separate size estimate in ArchimedeanSize.lean. Supply the one-line argument that slack≤b+offWeight+halfGap²≤a by the data scales and main≤a, or cite rowMainLength_add_rowSlack_le explicitly. [Knowl line 34](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/size-of-one-kernel.knowl.md#L34) · [ArchimedeanSize.lean:191](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean#L191)

<a name="page-up-operator-preserves-source-forms"></a>

### The operator U at N preserves the source forms. Ramified source forms are ramified vectors

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/up-operator-preserves-source-forms.knowl.md) · [SetupAtLevel.lean:290](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/SetupAtLevel.lean#L290)

The proof factors a level element into its component at N and its component away from N. The scaling generator really is supported on one conjugate pair, so it yields the stronger local representative described for these source forms.

<a name="up-operator-preserves-source-forms-finding-1"></a>

**Low · Distinguish a ramified vector from this stronger witness.** The gloss on “ramified vector” requires the scalar to equal 1 at the other places. The definition requires only that its reduction modulo N equal 1 there. Exact equality holds for the scaling chosen in this proof, as the support argument shows. The link New.ramified also omits IsSplitLevel. State the residue condition as the definition, then observe that this proof chooses a scalar equal to 1 away from w. Link the ramified-vector-at-split-level knowl, and qualify the related upOperator and mirabolic_fix_upOperator links with New.IsSplitLevel. [Knowl line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/up-operator-preserves-source-forms.knowl.md#L20) · [LiftLawsModuloN.lean:222](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L222)

## Other knowls checked

<a name="page-class-count-at-levels-containing-a-principal-level"></a>

### Class count at levels containing a principal level

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/class-count-at-levels-containing-a-principal-level.knowl.md) · [Estimates.lean:248](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean#L248)

The class count uses q₁d as an element of the different, and the level index is bounded by G^(2f|n|²). Since π_Mπ_N divides MN, the subgroup contains the level-MN kernel, allowing the second estimate.

<a name="page-colength-of-the-up-integral-forms"></a>

### The prime N: colength of the up-integral forms

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/colength-of-the-up-integral-forms.knowl.md) · [ColengthAtLevel.lean:273](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ColengthAtLevel.lean#L273)

The determinant of the coordinate scaling is N^l. Pullback at the adapted class representatives and iteration under U give N^{l(i+1)}, hence e = l(ϱ+2) at i = ϱ+1, with the advertised dimension bound.

<a name="page-collision-sum-bound"></a>

### The collision sum is within the loss at non-exceptional primes

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/collision-sum-bound.knowl.md) · [JetExponent.lean:167](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/JetExponent.lean#L167)

A collision forces an odd multiple of the order of the class of the place named by −p. The excluded ramified case follows from the congruence for d, and summing the geometric tail beyond the first allowable exponent gives the factor 2.

<a name="page-collisions"></a>

### Collisions of a-places at a prime

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/collisions.knowl.md) · [ShortColumns.lean:123](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L123)

Both the starting place and its translated partner must lie in the a-places outside ev, and e must be positive. The sum counts the ordered pairs with weight a/p^e and no factor v(π_p).

<a name="page-cost-of-low-columns-at-marked-places"></a>

### Cost of the transfer and of the low columns at marked places

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/cost-of-low-columns-at-marked-places.knowl.md) · [MarkedPrimes.lean:523](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkedPrimes.lean#L523)

The bound splits at p = m. Above m the order modulo q₀ is one, so every place inducing a marked prime is an a-place. The final inequality after multiplication by p agrees with the quoted size comparison at lines 549–554.

<a name="page-divisibility-at-one-prime"></a>

### Divisibility of the composite lift at one prime

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/divisibility-at-one-prime.knowl.md) · [LocalDivisibility.lean:407](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/LocalDivisibility.lean#L407)

I checked the choices of S in all four cases, the factor 2 in the exceptional and level bounds, and the determinant condition without assuming S lies in the integral forms. Ramification enters the valuation argument at N.

<a name="page-frobenius-cycle-of-a-marked-prime"></a>

### The Frobenius cycle of a marked prime

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/frobenius-cycle-of-a-marked-prime.knowl.md) · [MarkOperator.lean:301](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkOperator.lean#L301)

The orbit test needs only inertness and odd o₀ in part 1. The integer congruence ρ(ā) ≡ a^(pᵉ) extends through localization after the alternating conjugations, and the residue degree o₀N supplies the last Frobenius-cycle axiom.

<a name="page-full-mark-exists"></a>

### Existence of full marks, and vanishing of collisions outside a full mark

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/full-mark-exists.knowl.md) · [MarkedPrimes.lean:230](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkedPrimes.lean#L230)

The smaller member of each conjugate pair is available because multiplication by the odd power indexed by o₀ preserves the a-places and exchanges their induced primes. An odd collision partner of an unmarked a-place must then induce a marked prime.

<a name="page-gains-add-up-to-the-prime-sums"></a>

### The gains add up to the prime sums

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/gains-add-up-to-the-prime-sums.knowl.md) · [ArchimedeanSize.lean:146](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean#L146)

The definition of gain supplies one sum over a-places and a k-weighted sum over all places. Substituting the grouped prime sums into the definitions of mainAmount and totalRemainder cancels both with the signs printed here.

<a name="page-integral-source-forms-as-families-of-integral-vectors"></a>

### Integral source forms as families of integral vectors

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/integral-source-forms-as-families-of-integral-vectors.knowl.md) · [HeckeEdges.lean:729](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/HeckeEdges.lean#L729)

Freeness permits arbitrary complex vectors at the representatives. Because the representatives are integral above p, their coordinatewise-integral vectors are exactly the gauge-one unit balls, and equivariance propagates the bound to every point.

<a name="page-integral-values-of-source-forms-as-polynomials"></a>

### Integral values of source forms as polynomials

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/integral-values-of-source-forms-as-polynomials.knowl.md) · [ChainValuation.lean:416](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ChainValuation.lean#L416)

Unitarity turns the transpose of the conjugate of g⁻¹ into g. The one-row Gram-model identity then gives exactly the multinomial-scaled monomials with coefficient ring O_{C_p} and degree zero outside the a-places.

<a name="page-level-compensates-the-excess"></a>

### The level compensates the archimedean excess

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/level-compensates-the-excess.knowl.md) · [ArchimedeanSize.lean:105](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean#L105)

The lower endpoint of the level window gives m(log κ̄+G)−G−(15/2)log b. The period formula cancels the logarithmic-derivative constant, after which the bounds 1, 23 and 8 sum to the coefficient 32.

<a name="page-local-divisibility-of-the-composite-lift"></a>

### Divisibility of the composite lift

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/local-divisibility-of-the-composite-lift.knowl.md) · [LocalDivisibility.lean:494](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/LocalDivisibility.lean#L494)

Taking err equal to allowedLoss works simultaneously for all finite sums. For each prime and embedding, intersecting the one-prime module with the integral ramified forms preserves the determinant bound and gives one submodule for every admissible twist and chain datum.

<a name="page-mark-operator"></a>

### Elementary divisors of the scaled Hecke operator at a marked prime

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/mark-operator.knowl.md) · [MarkOperator.lean:345](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkOperator.lean#L345)

The parity shift gives N=2ℓ, where aℓ is the scaling exponent. The inequalities mp≤P^(2r) and mr²≤k bound both terms of the divisor constant by 1/(mp), giving 12Aₗ/(mp) after the factor 3.

<a name="page-marked-set-of-primes"></a>

### Induced primes, marked sets and full marks

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/marked-set-of-primes.knowl.md) · [MarkedPrimes.lean:57](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkedPrimes.lean#L57)

The four marking conditions, the disjunction required of every a-place for fullness and the scaling exponent agree. The summation formula counts the fibers of the induced-prime map on the a-places.

<a name="page-mean-degree-in-one-variable"></a>

### Mean degree of the weight basis in one variable

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/mean-degree-in-one-variable.knowl.md) · [ColengthAtLevel.lean:102](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ColengthAtLevel.lean#L102)

I checked the transposition of the two diagonal weight operators and the sum over all variables. Freeness identifies the number of class–tableau pairs with the dimension, giving the factor fa on the right.

<a name="page-mean-zero-vectors-are-the-image-of-one-minus-translation"></a>

### Vectors of mean zero under commuting operators of finite order

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/mean-zero-vectors-are-the-image-of-one-minus-translation.knowl.md) · [ShortColumns.lean:472](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L472)

The product of r−Σz_w^i acts by r^|I| on the joint kernel, while the matching factor 1−z_w kills each geometric sum after applying the representation. The proof only requires finite order of the represented operators.

<a name="page-neighbor-exponents-and-lift-loss"></a>

### Neighbours at a marked set: exponents, charges and the lift loss

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/neighbor-exponents-and-lift-loss.knowl.md) · [ValuationAtNonSplitPrimes.lean:87](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean#L87)

The selected local diagonal is p on J at a marked prime and p⁻¹ at its conjugate. Reading the component at the conjugate induced prime gives p^{-ε}, and the charge rule and subtraction of the divisibility bound agree with the definitions.

<a name="page-orbits-at-an-exceptional-prime"></a>

### Orbits of the place named by -p at an exceptional prime

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/orbits-at-an-exceptional-prime.knowl.md) · [MarkedPrimes.lean:299](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkedPrimes.lean#L299)

The inert-prime decomposition gives even powers of u(−p) as the stabilizer, odd powers as transport to the conjugate and residue degree lcm(o,2). The divisibility m ∣ o reduces this to o and rules out a conjugation-fixed prime.

<a name="page-passage-to-the-good-part"></a>

### Passage to target forms by the good projection

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/passage-to-the-good-part.knowl.md) · [ArchimedeanSize.lean:526](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean#L526)

The first-block lift acts on the right by the product ts. The scaled coefficients are character values and hence algebraic integers, and the pointwise bound contributes |G|⁴ before the class count.

<a name="page-prime-sum-grouped-by-primes"></a>

### The von Mangoldt sum grouped prime by prime

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/prime-sum-grouped-by-primes.knowl.md) · [Estimates.lean:107](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean#L107)

The factor (1−χ(pᵉ))/2 is 1/2 for the ramified prime, 1 for odd inert powers and zero for split powers or even inert powers. The support cutoff and nonnegativity justify both the reindexing and enlargement of a finite prime set.

<a name="page-ramified-source-forms"></a>

### Ramified source forms

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/ramified-source-forms.knowl.md) · [ShortColumns.lean:741](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L741)

The central action is right translation by a scalar matrix. Each kernel sums the N−1 powers starting with the identity, and the independent product over a set of places agrees with ramifyingOp.

<a name="page-scaling-generator"></a>

### Scaling generator at a prime dividing pi_N

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/scaling-generator.knowl.md) · [ShortColumns.lean:606](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L606)

The norm-one idele built from a lift of a residue-field generator has the required component because w and its conjugate are distinct. At the level, the only remaining congruence is its scalar last-row entry at w.

<a name="page-short-form"></a>

### Short algebraic form

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/short-form.knowl.md) · [ShortColumns.lean:155](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L155)

The p-adic condition uses the gauge at g of the value at g. The size takes all field automorphisms of ℂ and the integer Weyl Gram form, and the parallelogram identity gives the exact factor 4 for a difference of translates.

<a name="page-short-ramified-source-forms-span"></a>

### Short ramified source forms span

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/short-ramified-source-forms-span.knowl.md) · [ShortColumns.lean:1002](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L1002)

At the source rank k at most fa boxes contribute, giving the initial bound exp(errorUnit)/4^f. Applying the f scaling differences incurs 4^f and their image spans the ramified source forms.

<a name="page-size-of-the-composite-lift"></a>

### Archimedean size of the composite lift

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/size-of-the-composite-lift.knowl.md) · [ArchimedeanSize.lean:436](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ArchimedeanSize.lean#L436)

The restriction exponent actually uses the exact identity Στ nτ=|Φₐ|a−fmΔ/2 (Weights.lean:649). The weaker inequality in step 4 is sufficient because log N&gt;0 and the term is subtracted. The class and coefficient counts are squared as in the source.

<a name="page-valuation-and-colength-at-a-full-mark"></a>

### Exceptional primes: valuation and colength at a full mark

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/valuation-and-colength-at-a-full-mark.knowl.md) · [LocalDivisibility.lean:255](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/LocalDivisibility.lean#L255)

Fullness removes all residual collisions in the valuation bound, while the colength estimate applies to any marked set. The costs add over m copies of the list of places, with truncation exponent ceil(2mfa/p).

<a name="page-valuation-of-the-composite-lift-at-n"></a>

### The prime N: valuation of the composite lift

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-divisibility/valuation-of-the-composite-lift-at-n.knowl.md) · [ValuationAtLevel.lean:516](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/ValuationAtLevel.lean#L516)

Up-integrality bounds U^(m/2)φ at δ₀, and the same scalar works for each support term of Ψ. The m direct lifts and the scalar each cost mfb powers, while the restriction from δₘ to 1 preserves the resulting bound.
