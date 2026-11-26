# derivatives-vacuum

This area contains 95 individual knowls and a chapter page. The review records 41 comments. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports/derivatives-vacuum.md)

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Chapter page

<a name="page-derivatives-vacuum"></a>

### The integral vacuum and the sharpness of the valuation bound

Correction recorded · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum.knowl.md) · [BoundAttained.lean:381](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L381)

The final sharpness estimate has one t per multidegree and permits the indicator and coefficient to depend on the prime and embedding. The factor c_vac¹²∏lτ!/t and the bound exp(fmb/k) agree.

<a name="derivatives-vacuum-finding-1"></a>

**High · Both six-copy conclusions are upper bounds of zero.** The spanning statement at line 49 and the inert-frame statement at line 57 each assert an equality. Both prove val₆(ν) ≤ 0. For the first, take μ(z)=z/p and multiplicity zero. The integral multiple pμ spans the coordinate, but the permissible series y(z/p) has linear coefficient 1/p. The inert specialization also concludes only an upper bound in Cases.lean:220. Change the link texts at lines 49 and 57 to “least valuation at most zero” and carry the wording into both linked leaf titles. [Knowl line 49](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum.knowl.md#L49) · [LeastValuation.lean:548](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L548)

<a name="derivatives-vacuum-finding-2"></a>

**Medium · Standard data give an integrality statement at the chosen prime.** The standard-data module at p is generated over the ring of numbers integral at that embedding. It allows multiplication by 1/ℓ for any other prime ℓ. A vector standard at p therefore does not acquire integral derivatives at every other prime from this theorem. Line 42 repeats the ambiguous global quantifier. Say that for each p and embedding, data standard there have integral scaled derivatives there. Global integrality of one datum needs the corresponding standardness at every place. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum.knowl.md#L15) · [Divisibility.lean:57](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Divisibility.lean#L57)

## Knowls with comments

<a name="page-cm-curve-and-period"></a>

### The CM curve and the period of K

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/cm-curve-and-period.knowl.md) · [TightFrames.lean:83](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L83)

The curve and Ω₀ are chosen together from the unit ideal, so the displayed lattice identity and Ω₀∈Λ follow. The underlying existence result requires a choice of scale.

<a name="cm-curve-and-period-finding-1"></a>

**Medium · The CM-lattice existence theorem chooses the scale.** The link describes every scaled ideal as a CM lattice. The cited theorem gives, for each nonzero fractional ideal 𝔞, some u∈ℂˣ and a CM datum with lattice u𝔞. The proof chooses a fourth root to impose ℘″(t)=2, which a prescribed scale need not satisfy. Say that each nonzero fractional ideal has a complex multiple supporting a CM datum. Applying this to the unit ideal gives the chosen Ω₀. [Knowl line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/cm-curve-and-period.knowl.md#L19) · [GoodReduction.lean:164](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/GoodReduction.lean#L164)

<a name="page-existence-of-resolution-product-along-tight-frame"></a>

### A product of monomial sections along a tight frame is the theta function of an integral vector

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/existence-of-resolution-product-along-tight-frame.knowl.md) · [TightFrames.lean:860](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L860)

With b=a/conj(δ), the frame form and shifted lattice give the signed theta law. Fourier inversion applies to δ integral of nonzero norm, and the rational-translation law gives the indicated negative shift.

<a name="existence-of-resolution-product-along-tight-frame-finding-1"></a>

**Medium · Fix the dependency for rational finite translates.** The outline directs the reader to New.Space.entireTheta_translate_finiteImage for the sign and shift of every factor. The declaration is in New, so this placeholder cannot resolve to the cited theorem. Link New.entireTheta_translate_finiteImage. Its standard-space hypothesis and its shift by −realImage(γ) are exactly the ones used here. [Knowl line 40](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/existence-of-resolution-product-along-tight-frame.knowl.md#L40) · [ThetaJets.lean:208](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaJets.lean#L208)

<a name="existence-of-resolution-product-along-tight-frame-finding-2"></a>

**Low · Two declarations indexed here are absent from the proof.** The declaration list assigns both cmPeriod_mem_cmCurve_lattice and norm_map_selfDualAddChar to this knowl. The proof concerns a general a∈Λ and uses neither the chosen period nor the finite additive character. Readers following these two entries find no account of the claims. Associate the period-membership lemma with the CM curve and period page, where its proof is given. Associate the character norm with a proof that uses the finite-order argument or state that argument on its own. [Knowl line 10](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/existence-of-resolution-product-along-tight-frame.knowl.md#L10) · [TightFrames.lean:640](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L640)

<a name="page-jet-ring-is-stable-under-derivatives"></a>

### The jet ring has integral constant terms and is stable under derivatives

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/jet-ring-is-stable-under-derivatives.knowl.md) · [JetIntegrality.lean:161](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/JetIntegrality.lean#L161)

The coefficient identity g″ = 2g₂ + x and the bound for √(−d)·2g₂ give d g″ in the integral y-series ring. The constant-term result itself holds for arbitrary d in Lean, and the derivative result uses d prime and congruent to 7 modulo 8.

<a name="jet-ring-is-stable-under-derivatives-finding-1"></a>

**Medium · The Leibniz induction must retain membership of the factors.** The set of ambient series whose first derivatives lie in the jet ring need not be closed under products. In one variable p⁻¹ and z have derivatives 0 and 1, yet (p⁻¹z)′ = p⁻¹ has nonintegral constant term. Lean carries membership of both undifferentiated factors into its product step. Use the subset of F in the jet ring for which every ∂ₓF is in the jet ring. For two such elements F and G, both terms of ∂ₓ(FG) = F∂ₓG + (∂ₓF)G belong to the jet ring. This proves closure under products and permits induction on the generators. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/jet-ring-is-stable-under-derivatives.knowl.md#L29) · [JetIntegrality.lean:192](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/JetIntegrality.lean#L192)

<a name="page-least-valuation-along-couplings"></a>

### Least valuations along couplings at an inert prime

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-along-couplings.knowl.md) · [Couplings.lean:581](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Couplings.lean#L581)

The precise factorial bound, the estimate |ν| ≥ (p+1)|j| and the Legendre deduction agree. The index of the unit scale changes just before the coefficient lemma is used.

<a name="least-valuation-along-couplings-finding-1"></a>

**Medium · The distinguished theta factor changes index.** The preparation specifies δ₁ = 1. The next line singles out c = 0 in G and needs δ₀ = 1 to identify G(z′,0) with the integral product U. The six-copy witness in Lean specifies δ₀ = 1. Index the six scales by 0 through 5 and set δ₀ = 1 throughout, or explicitly relabel the one-based witness before applying the coefficient lemma. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-along-couplings.knowl.md#L27) · [Couplings.lean:533](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Couplings.lean#L533)

<a name="page-least-valuation-rules"></a>

### Rules for least valuations

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-rules.knowl.md) · [LeastValuation.lean:296](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L296)

Concatenation, the ultrametric selection of a coefficient in the copy substitution, and the monomial degree bound agree with the Lean arguments. The one-copy rescaling rule needs the same integrality assumption as the preceding rule.

<a name="least-valuation-rules-finding-1"></a>

**Medium · Make the parameter-series hypothesis explicit in the rescaling rule.** Item 3 reuses H_c from item 2 without saying it must lie in the parameter ring. Without that hypothesis, n=1, Θ=1, H₁=1/p, δ₁=1 and ν=0 would give val₁(0) ≤ −1, although every allowed witness has integral constant term. Move H_c ∈ 𝒪\[\[y(μz)\]\] into shared hypotheses for items 2–3 or repeat it at the start of item 3. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-rules.knowl.md#L21) · [LeastValuation.lean:345](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L345)

<a name="page-least-valuation-zero-when-forms-span"></a>

### Least valuation zero when the forms span the coordinates

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-zero-when-forms-span.knowl.md) · [LeastValuation.lean:548](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L548)

The unit lowest term yields one coefficient of valuation zero, and five constant-term witnesses give the stated upper bound for six copies. Other allowed witnesses can have negative valuation.

<a name="least-valuation-zero-when-forms-span-finding-1"></a>

**Medium · The spanning argument proves an upper bound of zero.** The title, also used in the chapter overview, asserts that the least valuation equals zero. In one variable take μ(z)=z/p, multiplicity zero, and a=p so that aμ=z. The allowed series y(z/p) has linear coefficient 1/p, of valuation −1. The other five witnesses can be constant. Retitle the knowl and its overview link “Least valuation at most zero when the forms span the coordinates.” Keep the ≤0 statement and its existing proof. [Knowl line 3](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-zero-when-forms-span.knowl.md#L3) · [LeastValuation.lean:550](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L550)

<a name="page-resolution-product-integral-values"></a>

### Values of a resolution product of monomial sections are p-integral

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/resolution-product-integral-values.knowl.md) · [TightFrames.lean:755](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L755)

Clearing denominators gives N·L times the shift in Λ because δ·conj(δ)=N and b·conj(δ) lies in Λ. This permits the independent torsion-value integrality theorem at every p.

<a name="resolution-product-integral-values-finding-1"></a>

**Medium · Point rational approximation to its actual declaration.** The proof depends on matching a finite adelic translate with a rational one, but its linked name New.Space.exists_finiteImage_approx is absent. The theorem lies in New and obtains equality from local constancy on the finite part and density. Use New.exists_finiteImage_approx as the target of the rational-approximation link. [Knowl line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/resolution-product-integral-values.knowl.md#L23) · [ThetaJets.lean:184](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaJets.lean#L184)

<a name="page-scaled-linear-forms-are-p-integral"></a>

### Scaled linear forms of vectors integral above p are p-integral

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/scaled-linear-forms-are-p-integral.knowl.md) · [Scale.lean:113](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Scale.lean#L113)

Integrality of the coordinate α⁻¹yᵢ at the place of ιₚ∘conj∘Φᵥ is enough. The period factor has precisely the inverse norm of α at that place.

<a name="scaled-linear-forms-are-p-integral-finding-1"></a>

**Medium · The extension preserves integrality through equivalent valuations.** The proof calls the map from the completion isometric. The source proves that its target norm is a positive power of the completion norm, with no assertion that the exponent is one. The threshold at one is preserved independently of normalization. Describe the extension as continuous and valuation-equivalent. If its norm is the c-th power of the local norm for c&gt;0, the inequalities against one are equivalent. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/scaled-linear-forms-are-p-integral.knowl.md#L21) · [ValuationSubrings.lean:497](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/Places/ValuationSubrings.lean#L497)

<a name="page-stability-of-standard-data"></a>

### Standard data are stable under integral Heisenberg and Weil operators

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/stability-of-standard-data.knowl.md) · [JetIntegrality.lean:307](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/JetIntegrality.lean#L307)

The quotient in the generator formula is L/(L∩g⁻¹L). The norm-one property applies to the inverse multiplier at all places above p, and both gy and gx satisfy the required δ-integrality condition.

<a name="stability-of-standard-data-finding-1"></a>

**Medium · State the lattice coordinates for integral unitary points.** For a general pointed space V = (J,a), Lean takes g in the standard finite unitary group with gᴴg = 1. The corresponding element u of U(J) is a_f g a_f⁻¹. If the entries tested in the prose are read in the original J coordinates, the condition on u and u⁻¹ can pick out a different subgroup. Specify the coordinates of the chosen finite adelic point of V. In those coordinates g and g⁻¹ have integral entries above p. In the J coordinates the element u stabilizes a_w 𝒪_wⁿ there. [Knowl line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/stability-of-standard-data.knowl.md#L20) · [Defs.lean:510](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L510)

<a name="stability-of-standard-data-finding-2"></a>

**Low · Cite the translated-vacuum formula for the displayed identity.** The named omega_vacElem_sum treats the untranslated vacuum and gives m(g)/|m(g)|². The displayed formula also moves h(x) across the Weil operator and writes the scalar as m(g⁻¹)⁻¹. Both additional identities are present in the source. Cite omega_finHeisenbergOp_intVacuum for this exact formula, or cite the covariance identity and m(g⁻¹) = conjugate(m(g)) alongside the vacuum sum. [Knowl line 28](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/stability-of-standard-data.knowl.md#L28) · [JetIntegrality.lean:300](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/JetIntegrality.lean#L300)

<a name="page-standard-data"></a>

### Standard data at a prime

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/standard-data.knowl.md) · [IntegralVacuum.lean:338](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L338)

The translates use the signed finite Heisenberg operator, and the scalars are complex numbers whose images under the fixed ιₚ are integral. The local condition on δx needs its valuation convention made explicit.

<a name="standard-data-finding-1"></a>

**Medium · Specify multiplicative absolute value in the integrality test.** Lean uses a multiplicative valuation ≤ 1. The unqualified phrase “valuation ≤ 1” gives a different set under the additive convention used in the corpus’s valuation-ring and p-adic-valuation definitions. At δ = 1 it would accept π_w⁻¹ of order −1 and reject π_w² of order 2, for a uniformizer π_w. Require δxᵢ,w to lie in the local ring of integers for every i and w in S. Equivalently require |δxᵢ,w|_w ≤ 1 or ord_w(δxᵢ,w) ≥ 0. [Knowl line 16](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/standard-data.knowl.md#L16) · [IntegralVacuum.lean:328](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L328)

<a name="page-standard-data-as-theta-products"></a>

### Standard data are theta products along a resolution times integral series

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/standard-data-as-theta-products.knowl.md) · [StandardDataProducts.lean:485](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean#L485)

The division-point computation gives exponent k²N, and the theorem correctly gives a resolution whose finite images are integral above p. The common denominator for a sum of translates needs one more factor.

<a name="standard-data-as-theta-products-finding-1"></a>

**Medium · The summary strengthens finite-image integrality.** The summary promises a resolution integral above p. The Lean result and item 2 give integrality of α⁻¹uⱼ there. The idele α can have denominators at primes dividing q₁, and the separate conversion to integrality of uⱼ in Divisibility.lean assumes p does not divide q₁. Describe the resolution as having finite images integral above p. Reserve integrality of the vectors themselves for the stated coprimality hypothesis. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/standard-data-as-theta-products.knowl.md#L5) · [StandardDataProducts.lean:489](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean#L489)

<a name="standard-data-as-theta-products-finding-2"></a>

**Medium · The common multiple omits the frame denominator b.** Step 1 proves membership for multiples of bmⱼ. Step 2 then takes m = ∏ⱼmⱼ and assumes m divides k, which does not imply bmⱼ divides k. In particular the implication fails for b &gt; 1, all mⱼ = 1 and k = 1. This leaves the stated membership for all multiples, and hence the choice k = m, unjustified. Choose m = b∏ⱼmⱼ, still prime to p, or return bmⱼ as the witness in Step 1 before taking the product in Step 2. [Knowl line 34](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/standard-data-as-theta-products.knowl.md#L34) · [StandardDataProducts.lean:515](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean#L515)

<a name="standard-data-as-theta-products-finding-3"></a>

**Low · The approximation lemma has a different namespace.** The point-approximation assertion is correct, but the link targets New.Space.exists_finiteImage_approx. The declaration is in namespace New, with Space opened locally. Point the approximation reference to New.exists_finiteImage_approx. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/standard-data-as-theta-products.knowl.md#L30) · [ThetaJets.lean:184](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaJets.lean#L184)

<a name="page-taylor-series-on-a-line-from-jet-series"></a>

### The jet series restricts to the Taylor series of the theta function on every line

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/taylor-series-on-a-line-from-jet-series.knowl.md) · [TightFrames.lean:480](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L480)

The equality of Taylor coefficients follows by integrating the exponential expansion against the Gaussian and comparing k! times the line coefficient. The reproducing and jet identities apply with the finite-part hypothesis.

<a name="taylor-series-on-a-line-from-jet-series-finding-1"></a>

**Medium · Identify the Weil model and its theta evaluations.** The text introduces 𝒮(V) simply as its Schwartz space and later uses f(realVec w) as though it were ordinary pointwise evaluation. The source uses a Banach model with an L¹ norm and defines the adelic evaluation of a vector f by θ(ρ(x)f), the identity behind the bound in step 2. Introduce 𝒮(V) as the source’s Banach model of the Weil representation and define f(x)=θ(ρ(x)f). Then the bound follows from the norm of θ and the isometry of ρ(x). [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/taylor-series-on-a-line-from-jet-series.knowl.md#L15) · [AdelicRepresentation.lean:244](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/AdelicRepresentation.lean#L244)

<a name="taylor-series-on-a-line-from-jet-series-finding-2"></a>

**Medium · Qualify entireness by the real vacuum condition.** The setup calls Θf entire for every f in 𝒮(V). The source proves holomorphy when the real vacuum projection fixes f. In one positive-sign coordinate, translating a nonzero finite-part vector g by a real Heisenberg vector u gives Θρ(u)g(z)=exp(−u·conj(z)−|u|²/2)Θg(z+u), which need not be holomorphic. Define Θf for arbitrary f and call it entire under the all-positive-sign and real-vacuum hypotheses. State here that the latter holds for f in the finite part. [Knowl line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/taylor-series-on-a-line-from-jet-series.knowl.md#L17) · [RealTheta.lean:191](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/RealTheta.lean#L191)

<a name="page-theta-product-times-monomials-as-a-vector"></a>

### Theta products times monomials in y are Taylor series of integral vectors

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/theta-product-times-monomials-as-a-vector.knowl.md) · [BoundAttained.lean:169](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L169)

The choices (cᵢ−3e,0,e), δ = π̄_M and the cancellation of the period and area scales give the claimed twelve factors. The last displayed identification needs the coefficient map between the two fields.

<a name="theta-product-times-monomials-as-a-vector-finding-1"></a>

**Medium · Distinguish the complex linear form from its p-adic image.** The linked definition makes μᵢ a form over ℂₚ. The proof substitutes that same μᵢ into an equality for the complex series 𝒯(F), then says to apply ιₚ. This mixes coefficient fields. Lean first substitutes a complex form with coefficients ϖ times the conjugate embeddings and then sends that identity to ℂₚ. Write μ̃ᵢ for the complex form in the product for 𝒯(F). After applying ιₚ to its coefficients, use μᵢ = ιₚ(μ̃ᵢ) and the corresponding p-adic Taylor series of y and θ. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/theta-product-times-monomials-as-a-vector.knowl.md#L29) · [BoundAttained.lean:205](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L205)

<a name="page-vector-determined-by-jet-series"></a>

### A vector of the finite part is determined by its jet series

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/vector-determined-by-jet-series.knowl.md) · [TightFrames.lean:511](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L511)

Since a≠0, evaluating the identically zero line function at a⁻¹ reaches the prescribed point. The last implication uses the model’s adelic theta evaluations and their rational quasi-periodicity.

<a name="vector-determined-by-jet-series-finding-1"></a>

**Medium · Specify the theta evaluation in the uniqueness step.** An ordinary adelic Schwartz function can vanish whenever the finite coordinates are zero and still be nonzero, for example one with finite support in a compact open set away from zero. Here f(realVec y)=θ(ρ(realVec y)f) exactly. Only Θf has the Gaussian factor. It is rational quasi-periodicity of these theta evaluations and density that make the restriction injective. State the exact evaluation identity, then invoke injectivity specifically for the Weil model’s theta evaluations. A sentence on rational translation removing a rational finite part and density explains the cited lemma. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/vector-determined-by-jet-series.knowl.md#L21) · [RealTheta.lean:137](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/RealTheta.lean#L137)

<a name="page-bound-for-the-partner-minimum-sum"></a>

### A bound for the partner minimum sum

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/bound-for-the-partner-minimum-sum.knowl.md) · [NearPairs.lean:421](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L421)

The cutoff at ⌈l₀/2⌉ gives at most one exceptional term below it. The geometric tail is at most 2b/pⁿ, and the remaining comparison needs k ≤ 2ˢ.

<a name="bound-for-the-partner-minimum-sum-finding-1"></a>

**Low · Supply the data comparison used in the geometric tail.** The proof marked full points only to a generic comparison tactic for k ≤ 2ˢ. Its exponent bounds are straightforward from the admissible data but are omitted, leaving the last denominator kp unjustified for a reader following the paper proof. Insert k ≤ r ≤ 3x⁵ ≤ x¹¹ ≤ m²² = 2ˢ, using x ≥ 2, m ≥ √x, and the prescribed bounds on r. Then n−1 ≥ s and p ≥ 2 give k ≤ pⁿ⁻¹. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/bound-for-the-partner-minimum-sum.knowl.md#L26) · [NearPairs.lean:390](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L390)

<a name="page-conjugates-of-jets-of-translates"></a>

### Conjugates of the jets of the translates of a generating vector

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/conjugates-of-jets-of-translates.knowl.md) · [IntegralVacuum.lean:595](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L595)

The same family B is chosen before the standard space, and one pair t,F′ works for every translation x for a fixed automorphism. The inverse place permutation and the squared scale Ω⁻¹ agree with the definitions and the CM calculation.

<a name="conjugates-of-jets-of-translates-finding-1"></a>

**Low · Supply the phase in the local constancy argument.** The open stabilizer invoked here gives constancy near zero. At a general x, composing the finite translation operators introduces the central character ψ(½ h\*·x). A shrinking of the stabilizer kills this phase, as reflected in the source proof of local constancy. Cite the local constancy theorem for finite translates directly, or explain that for fixed x the additive character of h is locally constant and equals one near h = 0. [Knowl line 39](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/conjugates-of-jets-of-translates.knowl.md#L39) · [VacuumProjections.lean:866](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/VacuumProjections.lean#L866)

<a name="page-copy-substitution"></a>

### Substitution of a linear combination of copies of the variables

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/copy-substitution.knowl.md) · [LeastValuation.lean:106](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L106)

The coordinate sum of the copy exponents, the product of multinomial coefficients, and the p-adic norm inequality agree with the coefficient calculation. The formal chain rule listed in the metadata is more general than the evaluation at zero reproduced here.

<a name="copy-substitution-finding-1"></a>

**Low · State the chain rule as an identity of series.** The proof gives the iterated derivative at zero under the characteristic-zero domain hypothesis. A later coupling argument uses the first derivative identity before evaluating at zero, over any commutative ring. For the stated substitution S, add ∂₍ₓ,ₖ₎ S(F) = aₖ S(∂ₓF) as an identity of formal series. Its iteration gives the factorial-weighted coefficient identity in every commutative ring, with cancellation available over a characteristic-zero domain. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/copy-substitution.knowl.md#L22) · [LeastValuation.lean:124](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L124)

<a name="page-integral-series-in-parameters-after-scaling"></a>

### Integral series in the parameters have integral coefficients after scaling

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/integral-series-in-parameters-after-scaling.knowl.md) · [LeastValuation.lean:586](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L586)

The one-variable integrality theorem applies to the generator y, and substitution of the integral linear forms preserves both integrality and the zero constant term. The theorem allows every scale whose norm satisfies the inequality.

<a name="integral-series-in-parameters-after-scaling-finding-1"></a>

**Low · Distinguish the fixed threshold from the chosen scale.** Calling ρₚ the valuation of ϖ identifies two quantities that may differ in the very next sentence. For example ϖ = 0 is permitted, while ρₚ is the finite number v(πₚ)/(qₚ−1). Introduce ρₚ as the valuation threshold v(πₚ)/(qₚ−1), then quantify the scale ϖ independently with |ϖ|ₚ ≤ p^(−ρₚ). [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/integral-series-in-parameters-after-scaling.knowl.md#L15) · [PrimeNotation.lean:100](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/PrimeNotation.lean#L100)

<a name="page-jets-along-homogeneous-polynomials"></a>

### Jets of the jet series along homogeneous polynomials

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/jets-along-homogeneous-polynomials.knowl.md) · [Scale.lean:62](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Scale.lean#L62)

The monomial calculation contributes α! times the coefficient, so rescaling multiplies every degree-l term by aˡ. I checked that the Fock polynomial at scale one is Q itself.

<a name="jets-along-homogeneous-polynomials-finding-1"></a>

**Low · Define the infinite-place index of the Fock signs.** The formula introduces Σ without defining it and then refers to signs “at the real places.” A CM field E has no real embeddings. The index in the source is (v,i) with v an infinite place of E, carrying sign εᵢ. Define Σ as the infinite places of E, equivalently the real places of its maximal totally real subfield, and assign sign εᵢ to (v,i). [Knowl line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/jets-along-homogeneous-polynomials.knowl.md#L20) · [AdelicRepresentation.lean:80](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/AdelicRepresentation.lean#L80)

<a name="page-lattice-a0-is-galois-stable"></a>

### The lattice a0 is Galois stable and its vectors have integral norms

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/lattice-a0-is-galois-stable.knowl.md) · [ShortVectors.lean:192](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L192)

Pulling the finite place back by the automorphism transports the valuation of y, while the condition on β and the valuation of the different are preserved. The integral Hermitian self-pairing is real and nonnegative, hence a natural number.

<a name="lattice-a0-is-galois-stable-finding-1"></a>

**Low · Name the polynomial differentiated to obtain the different generator.** In “P be parameters … g=P′(ζ)” the symbol P already denotes the parameter tuple. No polynomial P has been introduced, so the derivative used in the lattice criterion cannot be read literally. Write g=Φ′_{q₁}(ζ), with Φ_{q₁} the q₁-th cyclotomic polynomial. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/lattice-a0-is-galois-stable.knowl.md#L15) · [PrimeDecomposition.lean:255](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L255)

<a name="page-least-valuation-zero-at-inert-primes"></a>

### Least valuation zero along a tight frame at an inert prime

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-zero-at-inert-primes.knowl.md) · [Cases.lean:220](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean#L220)

The proof constructs integral coefficients cᵢ ιₚ(Φτ(uᵢ)) expressing a unit times each coordinate in the resolution forms. This gives the advertised inequality in the body.

<a name="least-valuation-zero-at-inert-primes-finding-1"></a>

**Low · The title turns an upper bound into equality.** The result is val₆(ν) ≤ 0. Strict inequality occurs under these hypotheses: at an inert p &gt; 2 use a singleton coupling family with exponent 1 and multiplicity 1. The normal form along the frame and the six-copy coupling bound give val₆(p\[τ\] + \[τ⁺\]) ≤ −1. Title the result “Nonpositive least valuation along a tight frame at an inert prime” and use the same wording for the area-page link. [Knowl line 3](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-zero-at-inert-primes.knowl.md#L3) · [Couplings.lean:588](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Couplings.lean#L588)

<a name="page-legendre-bounds-for-the-data"></a>

### Legendre bounds up to O(log b)

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/legendre-bounds-for-the-data.knowl.md) · [NearPairs.lean:263](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L263)

The digit bound for n&lt;pᴰ gives the lower error D, and applying it to three separate factorials gives the factor 3(log b+2). The proof is valid with a correction to the source attribution.

<a name="legendre-bounds-for-the-data-finding-1"></a>

**Low · Attribute the factorial interval estimate to the project library.** The parenthetical “Mathlib” identifies the wrong source. New.padicValNat_factorial_mem_Icc is a lemma proved in this development from Legendre’s digit-sum formula. Cite New.padicValNat_factorial_mem_Icc in Lib/General/Algebra/IntegralPowerSeries.lean in References, or omit the parenthetical and retain the self-contained digit-sum proof. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/legendre-bounds-for-the-data.knowl.md#L22) · [IntegralPowerSeries.lean:230](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/IntegralPowerSeries.lean#L230)

<a name="page-modulus-of-jet-scale"></a>

### The modulus of the jet scale

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/modulus-of-jet-scale.knowl.md) · [Scale.lean:140](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Scale.lean#L140)

Matching a₁ under the identity conjugation gives equal areas via mutual lattice inclusions. Substitution into the conjugated period identity yields |λ|²=Ω⁻¹.

<a name="modulus-of-jet-scale-finding-1"></a>

**Low · Correct the isogeny citation for the area equality.** The principal bridge left to the source is cited as New.CMLattice.exists_isIsogeny_of_mul_mem_lattice. That qualified name does not exist. The result for period pairs lies in New, as does its companion in ConjugateCurve. Cite New.exists_isIsogeny_of_mul_mem_lattice and New.conj_isogeny_mul_mem_lattice. The latter applies to the identity isogeny and gives inclusion of the corresponding period lattices. [Knowl line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/modulus-of-jet-scale.knowl.md#L23) · [Basic.lean:170](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean#L170)

<a name="page-norm-bounded-by-values-at-finite-points"></a>

### A bound at finite points bounds the norm

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/norm-bounded-by-values-at-finite-points.knowl.md) · [IntegralVacuum.lean:408](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L408)

Weak approximation is used at the archimedean coordinates while the finite part varies freely. Translating the dense set by rational vectors changes the values by unit-modulus scalars, so the pointwise estimate passes to the quotient mean.

<a name="norm-bounded-by-values-at-finite-points-finding-1"></a>

**Low · Identify the space carrying the inner product.** The introduction calls the pairing the inner product of V. Its arguments are vectors of the complex function space 𝒮(V), whereas V itself carries a Hermitian form over E. Call it the inner product on 𝒮(V) and retain the quotient-mean formula for its value on (f,f). [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/norm-bounded-by-values-at-finite-points.knowl.md#L15) · [AdelicRepresentation.lean:261](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/AdelicRepresentation.lean#L261)

<a name="page-reduction-to-the-curve"></a>

### Reduction of the sharpness bound to the curve

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/reduction-to-the-curve.knowl.md) · [BoundAttained.lean:288](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L288)

The monomial witnesses give 3e_{b,i} ≤ cᵢ and a product of twelve separate coefficients of norm at least p^(−r). Multiplying by the vacuum value, which may vanish, yields the same weak inequality as Lean.

<a name="reduction-to-the-curve-finding-1"></a>

**Low · The integer-product valuation lemma is assigned to the wrong knowl.** The metadata and References assign norm_natCast_prod_eq_rpow_neg_sum to this page. Its proof uses the product of coefficients on disjoint variables. The separate identity for p-adic norms of natural-number products is used for the loss products and factorials in the final sharpness theorem, and is absent from the reduction page. Move that secondary Lean declaration and its reference to sharpness-of-the-valuation-bound, whose last step presents both applications. [Knowl line 10](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/reduction-to-the-curve.knowl.md#L10) · [BoundAttained.lean:426](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L426)

<a name="page-resolution-from-tight-frame"></a>

### A tight frame of square length gives a resolution of the identity

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/resolution-from-tight-frame.knowl.md) · [StandardDataProducts.lean:75](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean#L75)

At positive b and k the coordinatewise Gram computation cancels k²/(bk)² and the frame bound b². Repeating each root of unity q₁ times gives the final specialization.

<a name="resolution-from-tight-frame-finding-1"></a>

**Low · The displayed definition divides by an allowed zero.** The knowl defines wᵢ/ν for every ν in ℕ. At ν = 0 this is undefined in ordinary field notation, while Lean uses total division and returns the zero vector. The theorem immediately below only uses positive denominators. Specify ν &gt; 0 and b,k positive integers in the textbook formulation, or state the zero-vector convention when ν = 0. [Knowl line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/resolution-from-tight-frame.knowl.md#L17) · [StandardDataProducts.lean:62](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean#L62)

<a name="page-sharpness-of-the-valuation-bound"></a>

### Sharpness of the valuation bound

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/sharpness-of-the-valuation-bound.knowl.md) · [BoundAttained.lean:381](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L381)

The witness t is independent of the modulus, prime and p-adic place. The final multiplication by the product of factorial norms and division by the two loss-product norms cancels the two corresponding valuation sums with the stated signs.

<a name="sharpness-of-the-valuation-bound-finding-1"></a>

**Low · Specify the weight at which the local prime sum is evaluated.** The text calls Sₚ the predicted valuation while the theorem varies the order l. The local prime sum takes an order as an argument. Lean uses Sₚ = ∑τ sₚ(κ(τ),τ), which is independent of l throughout the interval. Put the formula for Sₚ after the inequality and identify sₚ as the local prime sum. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/sharpness-of-the-valuation-bound.knowl.md#L22) · [ShortColumns.lean:78](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L78)

<a name="page-six-scaled-copies-are-a-unit"></a>

### Six scaled copies of a theta product multiply to a unit

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/six-scaled-copies-are-a-unit.knowl.md) · [LeastValuation.lean:488](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L488)

The two exponential expressions agree by the square-sum condition. Four squares representing −1, together with 1 and 0, give a distinguished scale and an inverse in the parameter ring.

<a name="six-scaled-copies-are-a-unit-finding-1"></a>

**Low · Use the same index for the distinguished copy across the six-copy arguments.** The summary calls the distinguished scale δ₀, while the one-based text calls it δ₁. Either indexing proves this theorem, but the linked coupling argument later singles out factor 0 while quoting the δ₁ convention. Index this six-tuple as δ₀,…,δ₅ with δ₀=1 in both the summary and body, or explicitly state the relabelling wherever it is used. [Knowl line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/six-scaled-copies-are-a-unit.knowl.md#L20) · [LeastValuation.lean:489](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L489)

<a name="six-scaled-copies-are-a-unit-finding-2"></a>

**Low · Identify the norm-pair closure in the cited integrality theorem.** The source assumes membership in the closure of (ιₚα, ιₚ(α times its conjugate)) for all integers α of K. The page attributes to it the smaller closure of the natural-integer pairs (k,k²). This specialization suffices here, but it omits the domain of the cited result. Give the norm-pair closure from the source, then note that it contains (a,a²) for a ∈ ℤₚ by density of the natural integers. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/six-scaled-copies-are-a-unit.knowl.md#L26) · [LogTheta.lean:318](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/LogTheta.lean#L318)

<a name="page-size-of-the-sharpness-constant"></a>

### Conjugates of the constant in the sharpness bound

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/size-of-the-sharpness-constant.knowl.md) · [BoundAttained.lean:332](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L332)

The exponent has terms 12f log M, 2f n♯ log(2b+n♯), and 12 C q₁². The final magnitude comparison is identified as an asserted step, and its two sides agree with Lean.

<a name="size-of-the-sharpness-constant-finding-1"></a>

**Low · Handle a zero vacuum value before taking its logarithm.** The estimate is quantified over every y. Positivity of the integer factor gives no positivity of the vacuum value at that particular y, so the real logarithm in the proof requires a case distinction. Lean multiplies the separate exponential bounds directly. When the vacuum value vanishes, the inequality is immediate. Take logarithms in the remaining case, or multiply the exponential bounds for both factors. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/size-of-the-sharpness-constant.knowl.md#L21) · [BoundAttained.lean:367](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L367)

<a name="page-sparseness-along-powers-of-minus-p"></a>

### Sparseness of the b-places along the powers of -p

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/sparseness-along-powers-of-minus-p.knowl.md) · [NearPairs.lean:92](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L92)

The nonsplit prime lies away from q₁, so the independent signs in the sparseness condition give the prohibited triple of powers. The argument for p=d uses dᵉ≠−1 mod q₀ and is independent of the bound p≤k.

<a name="sparseness-along-powers-of-minus-p-finding-1"></a>

**Low · Define the place of a nonunit for the unrestricted second assertion.** The page introduces \[ν\] only when ν is coprime to q₁. Item 2 as a separate implication also allows primes dividing q₁, so \[−pᵉ\] is undefined there for e&gt;0 under the page’s notation. Lean sets the place to the identity in this case. Define \[ν\] for every integer ν, using its residue-class place if ν is a unit modulo q₁ and the identity place otherwise. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/sparseness-along-powers-of-minus-p.knowl.md#L15) · [AdmissibleData.lean:222](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L222)

<a name="page-tight-frames-of-all-large-lengths"></a>

### Tight frames of every large length with large multiplicities

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/tight-frames-of-all-large-lengths.knowl.md) · [ShortVectors.lean:584](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L584)

The numerical threshold allows the Frobenius bound to be applied after subtracting R(q₁+h). Taking constant multiplicities a+R and b+R on the two indexed families produces exactly m.

<a name="tight-frames-of-all-large-lengths-finding-1"></a>

**Low · State the root-of-unity frame assumed by the large-length construction.** The inline lemma introduces neither ζ nor its relation to q₁ and the ambient field. Its proof requires that the q₁ powers of ζ themselves give a tight frame of length q₁ in the same lattice as v. Fix the parameters P and exponent s, introduce E=K(ζ) with ζ the chosen primitive q₁-th root, and link the root-of-unity frame lemma there. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/tight-frames-of-all-large-lengths.knowl.md#L15) · [ShortVectors.lean:584](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L584)

<a name="page-unit-coefficient-at-the-power-degree"></a>

### The derivatives of the coupling sum have a unit coefficient at the power degree

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/unit-coefficient-at-the-power-degree.knowl.md) · [Couplings.lean:242](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Couplings.lean#L242)

The proof restricts to the selected variables only after taking the indicated derivatives. The product’s unique surviving lowest monomial has coefficient equal to a product of nonzero residues, and multiplying by U preserves it.

<a name="unit-coefficient-at-the-power-degree-finding-1"></a>

**Low · The residue calculations are attributed to the wrong source.** The two results called Lib lemmas are proved in the derivatives-divisibility chapter, in NormalForm.lean at lines 394 and 411. Both already have a translated proof under coupling-sum-derivatives. Cite the derivatives-divisibility knowl coupling-sum-derivatives for the two residue computations. [Knowl line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/unit-coefficient-at-the-power-degree.knowl.md#L25) · [NormalForm.lean:394](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L394)

<a name="page-vacuum-expansion"></a>

### Expansion of the integral vacuum along a tight frame

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/vacuum-expansion.knowl.md) · [StandardDataProducts.lean:292](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean#L292)

I checked the six conditions, including the negative shift −(Ω₀/b)∑Φτ(γₖ)conj(Φτ(wᵢ)). The two sorts of translation in the definition use different finite coordinates, which the page leaves implicit.

<a name="vacuum-expansion-finding-1"></a>

**Low · The translation notation hides an idele factor.** Conditions 5 and 6 both use a subscript f without specifying how to embed the two inputs. For a finite adelic coordinate y, the argument is finVec(y) with finite part αy. For a rational vector γ, it is finVec(finiteImage(γ)) with finite part γ. Treating y as its own finite part changes the expansion at the components where α differs from 1. Define both subscripts before the conditions: (y)f is the adelic vector (0,αy), while γf is (0,γ), obtained from finite coordinate α⁻¹γ. [Knowl line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/vacuum-expansion.knowl.md#L20) · [AdelicRepresentation.lean:287](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/AdelicRepresentation.lean#L287)

## Other knowls checked

<a name="page-chowla-selberg-unit"></a>

### The Chowla-Selberg unit of the CM curve

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/chowla-selberg-unit.knowl.md) · [TightFrames.lean:100](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L100)

The same chosen unit has norm one for every p and p-adic embedding. The conjugate-area identity retains both π and the separate 2π/√d factor, with c=γ−Re(L′/L)(1,χK).

<a name="page-coefficient-of-a-product-of-couplings"></a>

### The coefficient of a product of couplings in a product of copies

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/coefficient-of-a-product-of-couplings.knowl.md) · [Couplings.lean:358](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Couplings.lean#L358)

With δ₀ = 1, restricting G to its first block gives U. The two differential operators contribute ν′! and ν″!, and cancellation of the common ν′! gives the stated coefficient norm, including the sign of the ν″! term in its valuation.

<a name="page-coupling-family"></a>

### Coupling families and the degrees of a product of couplings

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/coupling-family.knowl.md) · [Couplings.lean:52](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Couplings.lean#L52)

The exclusion tests every odd exponent up to eτ for every selected start. The multi-indices sum the pᵉ-weighted multiplicities at the starts and the ordinary multiplicities at the ends, and only copy zero receives z″.

<a name="page-degree-near-the-weights"></a>

### Degrees near the weights

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/degree-near-the-weights.knowl.md) · [Cases.lean:300](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean#L300)

Both endpoints of the interval are included. Composing its upper bound with κ(τ) + x⁴² ≤ 2b gives the coordinate bound even when lτ equals the upper endpoint.

<a name="page-derivatives-of-exponential-factorizations"></a>

### Derivatives of a series W exp(kappa Xi) with kappa of negative valuation

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/derivatives-of-exponential-factorizations.knowl.md) · [Couplings.lean:328](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Couplings.lean#L328)

The logarithmic derivative in z″ acts on the distinguished factor alone. At each differentiation κ⁻¹ multiplies both the derivative of the previous integral factor and its product with the logarithmic derivative of W, so both contributions vanish in the residue field.

<a name="page-derivatives-of-the-formal-parameter"></a>

### Derivatives of the formal parameter at powers of the prime norm

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/derivatives-of-the-formal-parameter.knowl.md) · [OneCurve.lean:293](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/OneCurve.lean#L293)

At n+1=qₚʲ the scaled coefficient is 1 modulo πₚ. Cancelling the single factor of ϖ leaves |ϖ|⁻ⁿ, and Legendre’s bound on (n+1)! gives the displayed derivative inequality.

<a name="page-divisibility-of-derivatives-along-minors"></a>

### Divisibility of derivatives of standard data along products of minors and Schur entries

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/divisibility-of-derivatives-along-minors.knowl.md) · [Divisibility.lean:215](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Divisibility.lean#L215)

B counts boxes strictly below the output rank. The Schur estimate uses the charge on the output filling, γₚ times the erased box count, and the logarithmic loss computed from the original B. I checked both cited minor-product bounds and the comparison of a Schur entry to one such jet.

<a name="page-dual-vectors"></a>

### The dual vectors of the powers of zeta

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/dual-vectors.knowl.md) · [ShortVectors.lean:272](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L272)

The factor multiplying the trace-dual coefficient is the j-th power of the conjugate of β, and the denominator is Φ′_{q₁}(ζ). The monic quotient has degree φ(q₁)−1, giving the stated zero coefficients beyond that degree.

<a name="page-dual-vectors-properties"></a>

### Properties of the dual vectors

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/dual-vectors-properties.knowl.md) · [ShortVectors.lean:321](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L321)

The trace-dual formula gives AB=I and the equal sizes give BA=I, with the two conjugate factors in the displayed order. The placewise integrality proof uses g∣q₁∣(β times its conjugate)ʲ and cancels β locally exactly when β is a unit.

<a name="page-errors-covered-by-the-loss-product"></a>

### The errors at one place are covered by the loss product

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/errors-covered-by-the-loss-product.knowl.md) · [NearPairs.lean:449](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L449)

The three displayed scale inequalities are the ones the Lean proof supplies. With T=b/(kp) they give a total error ≤3T and 1≤T, while n♯/p≥6T makes 3T≤n♯/p−1≤vₚ(B(l)).

<a name="page-existence-of-theta-products"></a>

### Existence of theta products

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/existence-of-theta-products.knowl.md) · [IntegralVacuum.lean:165](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L165)

Repeating each ζᵏ exactly q₁ times gives the frame of length q₁². The scale Ωe/(q₁e), the negative trace coordinate, the area condition and the q₁-th powers of the grouped factors all agree with the construction.

<a name="page-existence-of-vacuum-expansion"></a>

### Existence of vacuum expansions

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/existence-of-vacuum-expansion.knowl.md) · [StandardDataProducts.lean:367](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean#L367)

The Fourier inversion factor is (b²) raised to the number of place-coordinate pairs. Its inverse is p-integral, and the resulting points are α⁻¹(period − point), whose multiples by b are integral. The asserted Fourier theorem has both inversion identities used here.

<a name="page-existence-of-vector-with-unit-linear-form"></a>

### One of two explicit vectors has a unit linear form at each prime

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/existence-of-vector-with-unit-linear-form.knowl.md) · [ShortVectors.lean:557](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L557)

For each fixed p-adic embedding the condition |ιₚ(conj β)|ₚ&lt;1 is independent of τ, so one choice of y works for every τ. In that case the period norm |φτ(g)|ₚ cancels the norm of the last dual vector times ζ.

<a name="page-expansion-in-indicator-data"></a>

### A vector with integral values is bounded by indicator data

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/expansion-in-indicator-data.knowl.md) · [BoundAttained.lean:224](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L224)

Fourier inversion gives M^(12f)F and bounds cᵢ vac(y_f) by one. The indicator expansion uses the integrality of π̄_M α⁻¹uᵢ, and its character factors have p-adic norm one, so the finite maximum gives the stated direction.

<a name="page-frame-forms-sum-to-standard-hermitian-form"></a>

### The forms of a tight frame sum to the standard hermitian form

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/frame-forms-sum-to-standard-hermitian-form.knowl.md) · [TightFrames.lean:795](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L795)

The area assumption gives (π/A)|b/cA|²=1/M. The order of conjugation in the frame identity then contracts the two place indices, leaving the standard form ∑conj(uₚ)vₚ.

<a name="page-greatest-norm-of-derivatives"></a>

### The greatest norm of the n-th derivatives of integral series in y

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/greatest-norm-of-derivatives.knowl.md) · [OneCurve.lean:160](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/OneCurve.lean#L160)

The supremum is taken over n! times the zⁿ coefficient. Applying the finite monomial maximum to the single parameter y proves attainment, and stability under differentiation gives the bound by one for the stated d.

<a name="page-greatest-norm-of-derivatives-is-submultiplicative"></a>

### The greatest norm of derivatives is submultiplicative

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/greatest-norm-of-derivatives-is-submultiplicative.knowl.md) · [OneCurve.lean:258](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/OneCurve.lean#L258)

The binomial coefficient in y(z₀+z₁)ʲ converts (m+n)! to m!n!. The integral addition formula and the two-variable maximum then bound the mixed coefficient by separate coefficients of powers of y.

<a name="page-hermitian-product-of-lattice-vectors-is-integral"></a>

### Hermitian products of vectors of the lattice a0 are integers of K

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/hermitian-product-of-lattice-vectors-is-integral.knowl.md) · [TightFrames.lean:223](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L223)

Factoring x·conj(y)·g adelically puts x·conj(y) in the inverse different. Its relative trace is the displayed CM-type sum, and its integrality gives stability of any CM lattice under that multiplier.

<a name="page-integral-vacuum"></a>

### The integral vacuum

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/integral-vacuum.knowl.md) · [IntegralVacuum.lean:323](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L323)

A single bound C is chosen for all tower levels, then a nonzero scalar c(s) for each level. The Hermitian space of any finite rank uses c(s) to the power of its rank, with no standard-space assumption on this definition.

<a name="page-integral-vacuum-in-rank-one"></a>

### The integral vacuum in rank one

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/integral-vacuum-in-rank-one.knowl.md) · [IntegralVacuum.lean:228](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L228)

The CM theorem compares constant Taylor coefficients near a finite adele, and the uniform bound holds for all translations of all the conjugate lattices. The Fourier sum has (q₁²)^f terms and each term contributes q₁² torsion factors, which gives C = ⌈M⌉ + 2 independent of s.

<a name="page-integral-vacuum-values"></a>

### Values of the integral vacuum are integral, bounded and not all zero

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/integral-vacuum-values.knowl.md) · [IntegralVacuum.lean:370](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L370)

The rank-one factors supply the exponent |n| in the archimedean estimate. Composing an arbitrary automorphism with conjugation when needed makes it fix K while preserving all absolute values, and the unit vacuum norm rules out simultaneous vanishing at the finite points.

<a name="page-integrality-of-derivatives-of-standard-data"></a>

### Integrality and divisibility of the derivatives of standard data at all primes

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/integrality-of-derivatives-of-standard-data.knowl.md) · [Divisibility.lean:100](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Divisibility.lean#L100)

Scaling by d times the period factor makes the forms dνⱼ with νⱼ integral, as required by the jet-ring lemma. Homogeneity then contributes the lth power of the p-adic norm of c/(δ̄d).

<a name="page-integrality-of-jets-of-theta-products"></a>

### Integrality of the jets of theta products

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/integrality-of-jets-of-theta-products.knowl.md) · [JetIntegrality.lean:202](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/JetIntegrality.lean#L202)

The integral multiplier H belongs to the substituted y-series ring, each θ factor belongs to the jet ring, and natural powers preserve membership. Stability under differentiation gives the stated bound for all polynomials whose coefficients have integral images under φ.

<a name="page-jet-ring"></a>

### The jet ring of a CM lattice for a family of linear forms

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/jet-ring.knowl.md) · [JetIntegrality.lean:104](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/JetIntegrality.lean#L104)

The first generator is the image of all integral-coefficient formal series under substitution by the y(μᵢz). The other generators are θ(μᵢz) and the derivative of the one-variable negative logarithm evaluated at μᵢz, with no extra factor of μᵢ.

<a name="page-jet-scale"></a>

### The scale of theta Taylor series

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/jet-scale.knowl.md) · [TightFrames.lean:126](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L126)

The principal root is taken after inverting χfin(α). The jet scale divides by both the chosen Chowla–Selberg unit and the CM period, and the Fock coordinate calculation supplies the factor √(2π/√d).

<a name="page-jet-series-of-product-of-linear-forms"></a>

### Jet series of a theta function that is a product of functions of linear forms

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/jet-series-of-product-of-linear-forms.knowl.md) · [TightFrames.lean:573](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L573)

Evaluation at zero requires neither entireness of the factors nor a sign condition. For the jet statement, restriction of formal series to vX evaluates each degree component at v, which detects equality over ℂ.

<a name="page-jets-integral-in-derivative-stable-ring"></a>

### Jets are integral on a ring of series stable under derivatives

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/jets-integral-in-derivative-stable-ring.knowl.md) · [JetIntegrality.lean:51](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/JetIntegrality.lean#L51)

Polynomial induction works for arbitrary variable sets because each polynomial uses finitely many monomials. Quantifying over F at each stage permits the multiplication-by-Xₓ step to pass to ∂ₓF, while the ultrametric inequality handles addition.

<a name="page-katz-divisibility-limit"></a>

### The limit of Katz divisibility of derivatives

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/katz-divisibility-limit.knowl.md) · [OneCurve.lean:330](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/OneCurve.lean#L330)

For b=p^(−γₚ)≤1, the formal-parameter estimate at q=qₚᴹ gives c(q)≥b^(q−1)≥b^q. Submultiplicativity extends the inequality to every n, and the maximum is attained.

<a name="page-largest-coefficient-among-integral-series"></a>

### A monomial has the largest coefficient among integral series

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/largest-coefficient-among-integral-series.knowl.md) · [OneCurve.lean:45](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/OneCurve.lean#L45)

The same exponent m works for every integral G because it maximizes the norm of the coefficient of fᵈs over the finite set |d|≤|α|. The ultrametric estimate still applies when every such coefficient vanishes.

<a name="page-least-valuation-relation"></a>

### The least valuation of coefficients of products of theta products

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-relation.knowl.md) · [LeastValuation.lean:259](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L259)

The definition asks for actual witnesses whose multiindices sum to ν and whose coefficient norms have product at least p^(−r). Taking each parameter series equal to one verifies the degree-zero case, including the empty product.

<a name="page-least-valuation-with-a-unit-form"></a>

### Least valuation over six copies when one form has unit coefficients

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/least-valuation-with-a-unit-form.knowl.md) · [LeastValuation.lean:509](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L509)

Inserting G times the inverse of the six-copy theta product into the distinguished factor leaves G after rescaling. The multinomial coefficient and unit coefficients of the selected form give exactly the subtraction of vₚ(ν!) in the valuation bound.

<a name="page-loss-product"></a>

### The loss product of consecutive integers

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/loss-product.knowl.md) · [NearPairs.lean:234](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L234)

The product starts after max(l−n♯,0), so it is exactly n♯! when l&lt;n♯. Factorial divisibility then yields both valuation inequalities, and the first Legendre term gives the real lower bound n♯/p−1.

<a name="page-lowest-term-of-a-power-series"></a>

### Lowest term of a power series for a weight

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/lowest-term-of-a-power-series.knowl.md) · [LeastValuation.lean:59](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/LeastValuation.lean#L59)

The definition includes ties in weight and permits a zero coefficient. In the multiplication proof a summand with one exponent above its cutoff forces the other strictly below its cutoff, where the coefficient vanishes.

<a name="page-near-pair"></a>

### Near pairs of b-places

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/near-pair.knowl.md) · [NearPairs.lean:113](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L113)

Both endpoints must be b-places and 2e&lt;l₀ is strict. The common residue class of b-places excludes p=d, and the remaining positive exponent is odd, allowing the end to be written \[−p\]ᵉτ.

<a name="page-near-pairs-are-disjoint"></a>

### No place occurs twice among the starts and ends of near pairs

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/near-pairs-are-disjoint.knowl.md) · [NearPairs.lean:158](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L158)

For equal ends with e&lt;e′ the forbidden intermediate exponent is e′−e. For one end equal to the next start the last exponent is e+e′&lt;l₀, which gives the third sparseness contradiction even if some places coincide.

<a name="page-normal-form-along-a-tight-frame"></a>

### Normal form of the theta product along a tight frame at an inert prime

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/normal-form-along-a-tight-frame.knowl.md) · [Cases.lean:245](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean#L245)

The resolution theorem applies with the integral factor H = 1. The unit rescaling multiplies λₑⱼ by the Taylor scale to the power (pᵉ + 1)pʲ, which preserves the odd leading units and leaves v(ϖₚ) unchanged.

<a name="page-normal-form-of-standard-data"></a>

### Normal form of standard data at a non-split prime

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/normal-form-of-standard-data.knowl.md) · [Divisibility.lean:170](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/Divisibility.lean#L170)

The normal form uses all nonnegative e at p = d, including 0, and odd e at an inert prime. Its exponential factor has coefficient ϖₚ^(p+1)/p in both cases. The argument only needs the period factor to be a local unit and the final rescaling to be integral.

<a name="page-orbit-tight-frame"></a>

### The orbit of a lattice vector is a tight frame

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/orbit-tight-frame.knowl.md) · [ShortVectors.lean:237](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L237)

Factoring the sum over powers of ζ and Galois conjugates gives zero off the diagonal by root-of-unity orthogonality. On the diagonal multiplication of the place index by τ permutes the norm terms and gives the factor ν.

<a name="page-p-adic-size-of-period-factor"></a>

### The p-adic size of the period factor

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/p-adic-size-of-period-factor.knowl.md) · [TightFrames.lean:324](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L324)

Dividing by the Chowla–Selberg unit preserves the p-adic norm. In the proof away from q₁, all generators of the span of s₀ are integral and q₁ itself belongs to the span and has norm one.

<a name="page-p-adic-size-of-vacuum-root"></a>

### The p-adic size of the vacuum root

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/p-adic-size-of-vacuum-root.knowl.md) · [TightFrames.lean:265](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L265)

The weight embedding includes conjugation. Galois invariance of the relative different gives equal norms for all CM-type embeddings, while density of E in its finite adeles supplies a local unit for the reverse span inclusion.

<a name="page-partner-minimum-sum"></a>

### The partner minimum sum of a place

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/partner-minimum-sum.knowl.md) · [NearPairs.lean:310](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L310)

The second weight is evaluated at \[−pᵉ\]τ, and summing only over Iₚ agrees with setting all remaining terms to zero. Nonnegativity and κ(τ)≤b make b/2ᵉ a convergent majorant.

<a name="page-product-of-translated-thetas-as-theta-power"></a>

### Products of theta functions translated by division points

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/product-of-translated-thetas-as-theta-power.knowl.md) · [StandardDataProducts.lean:109](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean#L109)

The cited isogeny result takes a shift t with δt in the lattice and rescales the argument by δ̄. It gives the Nth power of θ with N = δδ̄, and substitution into arbitrary finite linear forms gives the stated integral series in the translated parameters.

<a name="page-properties-of-resolution-forms"></a>

### Properties of the resolution forms of a tight frame of length M

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/properties-of-resolution-forms.knowl.md) · [Cases.lean:129](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean#L129)

The division by π̄M cancels the length M in the Gram matrix. The level congruence is precisely 1 modulo q₁d, and q₁M uᵢ = (q₁wᵢ)πM clears the denominator in the local integrality argument.

<a name="page-rate-minus-predicted-valuation"></a>

### The rate times the total weight minus the predicted valuation

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/rate-minus-predicted-valuation.knowl.md) · [NearPairs.lean:334](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/NearPairs.lean#L334)

After removing the positive part termwise, the geometric identity leaves v(πₚ) times the partner minimum sum at each place. The positive parts have an absolutely summable majorant, so the subtraction of the sums is valid.

<a name="page-resolution-forms-of-a-frame"></a>

### The resolution forms and the Taylor scale of a tight frame of length M

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/resolution-forms-of-a-frame.knowl.md) · [Cases.lean:81](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean#L81)

The form uses the conjugate of the CM embedding of wᵢ. Dividing the vector by π̄M divides its dagger by πM, which is canceled by the πM in the Taylor scale.

<a name="page-resolution-product"></a>

### Resolution product of entire functions along a family of vectors

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/resolution-product.knowl.md) · [TightFrames.lean:697](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L697)

The shift is −b⟨γₖ,wⱼ⟩ and the form has scale b/cA. I checked the twisted exponential against the definition of thetaShift and verified that finVec(finiteImage γ) has actual finite part γ.

<a name="page-resolution-product-theta-values-and-jets"></a>

### Theta values and jet series of the translates of a resolution product

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/resolution-product-theta-values-and-jets.knowl.md) · [TightFrames.lean:728](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L728)

The theta-value formula evaluates the resolution identity at zero for all signs. For jets, standardness gives positive signs, finite translation preserves the finite part, and c multiplies the form coefficient b/cA.

<a name="page-roots-of-unity-tight-frame"></a>

### The powers of a primitive root of unity form a tight frame

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/roots-of-unity-tight-frame.knowl.md) · [TightFrames.lean:388](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/TightFrames.lean#L388)

A primitive root generates E over K, so distinct CM embeddings have different images of it. Their quotient yields a vanishing geometric sum off the diagonal and q₁ on it, and repeating multiplicities multiplies the bound by k.

<a name="page-short-coprime-tight-frame"></a>

### A short tight frame of length prime to q1 for admissible data

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/short-coprime-tight-frame.knowl.md) · [ShortVectors.lean:754](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L754)

The proof keeps the p-adic unit vector in the union of the root powers and the coprime frame, and preserves the order of the universal and existential quantifiers. The cyclotomic coefficient bound, dual-vector estimate and polynomial bound for h agree, with the final logarithmic comparison explicitly left to the source.

<a name="page-submultiplicative-sequences"></a>

### A lower bound along a sparse set extends to a submultiplicative sequence

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/submultiplicative-sequences.knowl.md) · [OneCurve.lean:83](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/OneCurve.lean#L83)

Writing q=n⌊q/n⌋+r gives c(q)≤c(n)^⌊q/n⌋ because c(r)≤1. The contradiction uses b&gt;0 for division and 0≤c(n)/bⁿ&lt;1 for the decay of its powers.

<a name="page-theta-product"></a>

### Theta product along the resolution of powers of zeta

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/theta-product.knowl.md) · [IntegralVacuum.lean:135](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L135)

The negative trace divided by q₁ gives the rational shift and the exponent on each Taylor factor is q₁. I checked the difference between (0,γ) for rational translations and (0,αx) for finite-adelic evaluation, together with all five defining requirements.

<a name="page-tight-frame-of-length-m"></a>

### A tight frame of length M with large multiplicities

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/tight-frame-of-length-m.knowl.md) · [ShortVectors.lean:787](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L787)

Taking R=⌈6fb⌉ in the large-length construction gives the required natural multiplicities, and both possible sources of the unit vector remain in the union. The proof identifies the threshold comparison with M as the scale estimate it leaves to Lean.

<a name="page-tight-frame-of-length-prime-to-q1"></a>

### A tight frame of length prime to q1

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/tight-frame-of-length-prime-to-q1.knowl.md) · [ShortVectors.lean:508](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L508)

Pairing ζ⁻ⁱ with the (0,1) element of each orbit adds the trace βʲ plus its conjugate and leaves the (1,1) element of the last orbit. Reducing at a prime above each divisor of q₁ makes that trace 1, which proves the length is coprime to q₁.

<a name="page-tight-frame-of-square-length-prime-to-p"></a>

### A tight frame whose length is a square prime to p

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/tight-frame-of-square-length-prime-to-p.knowl.md) · [StandardDataProducts.lean:217](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/StandardDataProducts.lean#L217)

When p divides q₁ the separate coprime-length frame works, and otherwise roots of unity give length q₁. Repeating every vector b times multiplies its initial frame bound b by b while retaining multiplicity one on the enlarged index set.

<a name="page-tight-frame-operations"></a>

### Unions of tight frames and replacing pairs by their sums

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/tight-frame-operations.knowl.md) · [ShortVectors.lean:93](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L93)

Disjoint union adds the frame bounds, and the injective selection of pairs makes every old diagonal term occur once in the replacement family. A diagonal entry of the new matrix is a sum of squares, proving that the adjusted integer length is nonnegative.

<a name="page-twelve-space-and-indicator-data"></a>

### The space of twelve copies, its Taylor series and indicator data

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/twelve-space-and-indicator-data.knowl.md) · [BoundAttained.lean:131](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/BoundAttained.lean#L131)

The finite index is a row of twelve coordinates and one column, all signs are positive, and the complex jet scale is π_M λ. The modulus datum inserts the residue-class indicator at its supporting places, while disjoint copy variables force a product of twelve individual coefficients.

<a name="page-unit-linear-form"></a>

### Vectors with a unit linear form at p

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/unit-linear-form.knowl.md) · [ShortVectors.lean:549](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/ShortVectors.lean#L549)

For a fixed p and embedding ιₚ the unit condition is imposed simultaneously at every infinite place. The conjugation acts on Φτ(y) before multiplication by the complex period factor and application of ιₚ.

<a name="page-vacuum-as-sum-of-translates"></a>

### A multiple of the vacuum is a sum of translates of a theta-function vector

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/vacuum-as-sum-of-translates.knowl.md) · [IntegralVacuum.lean:85](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L85)

Applying the theta functional to the inverse Fourier identity forces some coefficient to be nonzero. The averaging set has N^(f|n|) elements, and composing finite operators gives a unit scalar times a single translate, which proves the claimed spanning inclusion.

<a name="page-valuation-bound-at-large-inert-primes"></a>

### The valuation bound on twelve copies at an inert prime above k

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/valuation-bound-at-large-inert-primes.knowl.md) · [Cases.lean:544](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean#L544)

For jτ = min(iτ,lτ⁺), the bijection of partners gives p jₜ + jτ at t = τ⁺. The factorial estimate costs two copies of v(B(lτ)), and the e = 1 term of the local sum covers the remaining positive part.

<a name="page-valuation-bound-at-small-non-split-primes"></a>

### The valuation bound on twelve copies at a non-split prime at most k

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/valuation-bound-at-small-non-split-primes.knowl.md) · [Cases.lean:619](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean#L619)

Near pairs are disjoint at their starts and ends, so the unused degree η is nonnegative. The empty family also covers the ramified case. The three factorial errors cost 3f(log b + 2) and the loss product absorbs this together with the partner-minimum error.

<a name="page-valuation-bound-at-split-primes"></a>

### The valuation bound on twelve copies at a split prime

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/valuation-bound-at-split-primes.knowl.md) · [Cases.lean:526](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean#L526)

The positive partner-exponent set is empty and γₚ = 0. The unit-form bound works for an arbitrary family of vectors in this case, and six factors of constant coefficient one extend its six-copy bound to twelve.

<a name="page-valuation-bound-on-twelve-copies"></a>

### The valuation bound on twelve copies at every prime

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-vacuum/valuation-bound-on-twelve-copies.knowl.md) · [Cases.lean:672](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Sharpness/Cases.lean#L672)

The proof uses d ≤ k to exclude the ramified prime from the large-prime branch. The nonnegative sum of loss valuations permits the split bound and the one-loss small-prime bound to imply the common two-loss conclusion.
