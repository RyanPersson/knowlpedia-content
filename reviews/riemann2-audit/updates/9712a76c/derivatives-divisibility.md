# derivatives-divisibility

28 page records. Of 20 earlier findings, 20 are resolved. This review adds 8 findings. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/12cc7330341b6b4fb72c78b91a659e67e82a4b18/docs/riemann2/reports/derivatives-divisibility.md)

[Review overview](README.md) · [Status of earlier findings](response-ledger.tsv) · [New findings](findings.tsv)

<a name="page-derivatives-divisibility"></a>

## Derivatives of theta functions: divisibility at non-split primes

Revised · page · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility.knowl.md) · [NormalForm.lean:262](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L262)

The normal-form criterion now states the analytic scale and the two substitution hypotheses. The theta equality, weighted determinant bound, and treatment of the ramified Frobenius congruence agree with the source.

<a name="prior-derivatives-divisibility-1"></a>

**Resolved · high · Coupling divisibility needs a bound on the exponential scale.** The criterion now assumes |(ϖ^(p+1)/p)π| ≤ p^(−1/(p−1)) and that the substituted series are integral with zero constant term. For theta products the equality at v(ϖ)=ρₚ follows from the non-split scale identity. [Knowl, line 26](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility.knowl.md#L26) · [NormalForm.lean:262](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L262)

<a name="prior-derivatives-divisibility-2"></a>

**Resolved · medium · The determinant norm has a lower bound and the cost is additive in valuations.** The page bounds the sum of the determinant valuations, weighted by κ(τ,h), above by v(πₚ) times the deduction sum. The equivalent lower norm bound and restriction to nonexempt pairs agree with the two conclusions in the lemma. [Knowl, line 36](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility.knowl.md#L36) · [NullFrames.lean:361](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean#L361)

<a name="prior-derivatives-divisibility-3"></a>

**Resolved · medium · The Frobenius description of the decomposition group is unramified.** The Frobenius generator is now restricted to p ∤ q₁d. The partner congruence at p=d uses the separate residue-ring criterion, where the image of √−d modulo πₚ vanishes. [Knowl, line 44](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility.knowl.md#L44) · [PrimeDecomposition.lean:618](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L618)

<a name="new-derivatives-divisibility-1"></a>

**New finding · low · Restore the dependency link for the absolute ideal norm.** The retired field-setting page linked Nw to the definition of an ideal’s absolute norm. Its replacement notation says “absolute norm” without the link. The concept table already identifies the exact existing target and the Lean declaration defines w.q as w.asIdeal.absNorm. Link “absolute norm” beside Nw to algebra-fields-galois/ideal-norm. [Knowl, line 18](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility.knowl.md#L18) · [Basic.lean:131](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/Basic.lean#L131)

<a name="new-derivatives-divisibility-2"></a>

**New finding · low · The degree cutoff in the chapter is undefined for the empty diagram.** The restated criterion writes e ≤ logₚ B. For B=0 the real logarithm is undefined, while Lean uses the natural-number logarithm and sets its value to zero. The linked integrality proposition and the revised charged count both specify this convention. Write e ≤ floor(logₚ(max(B,1))) or specify that the integer logarithm of zero is zero. [Knowl, line 26](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility.knowl.md#L26) · [NormalForm.lean:265](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L265)

<a name="new-derivatives-divisibility-3"></a>

**New finding · low · The dependency summary still reverses the Schur expansion.** The library identity used in the chapter expands a row-substituted product of minors. The entries of the Schur row are its coefficients. Calling it an expansion of the Schur matrix in products of minors suggests the inverse identity that the revised definition explicitly rejects over general rings. Describe the library input as the expansion of a product of minors in a Schur row. Name the subsequent comparison of jet norms separately if needed. [Knowl, line 50](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility.knowl.md#L50) · [Count.lean:772](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L772)

<a name="page-frobenius-congruence-for-theta"></a>

## Frobenius congruence for the theta function

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta.knowl.md) · [FrobeniusCongruence.lean:158](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean#L158)

Step 1 uses the normalized degree-n torsion value and preserves integrality under isogeny pullback, with n multiplied by the isogeny degree. The same paragraph contains an independent clash between its complex and p-adic notation.

<a name="prior-frobenius-congruence-for-theta-1"></a>

**Resolved · medium · The integrality input concerns twisted torsion values.** The proof gives G\[u\] with the exponential twist in degree n and tests its image under the p-adic embedding for integrality. It then applies preservation under pullback in degree q. [Knowl, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta.knowl.md#L24) · [TorsionValues.lean:129](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/TorsionValues.lean#L129)

<a name="prior-frobenius-congruence-for-theta-2"></a>

**Resolved · low · Correct the isogeny reference.** The reference now names PeriodPair.IsIsogeny and states the lattice inclusion and the factor q relating areas. These are precisely the two conditions used to form the self-isogeny. [Knowl, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta.knowl.md#L24) · [Basic.lean:86](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean#L86)

<a name="new-frobenius-congruence-for-theta-1"></a>

**New finding · low · Distinguish the real π in the Gaussian from the p-adic uniformizer.** Line 15 defines π as the p-adic image of πₚ. The new formula for G\[u\] on line 24 uses the same π in a complex exponential before the p-adic embedding is applied. The twist uses the real circle constant and does not depend on the chosen p-adic uniformizer. Write πℝ for the circle constant in the Gaussian and define that notation there, or use the complex Hermitian form in the formula. [Knowl, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta.knowl.md#L24) · [TorsionValues.lean:129](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/TorsionValues.lean#L129)

<a name="page-frobenius-on-generators"></a>

## Galois elements as powers of Frobenius: a criterion on generators

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/frobenius-on-generators.knowl.md) · [PrimeDecomposition.lean:495](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L495)

The body now handles the prime d in rings with nilpotents: it is the coefficient of φ(√−d) that vanishes. Iteration includes n = 0.

<a name="prior-frobenius-on-generators-1"></a>

**Resolved · medium · Euler’s criterion alone does not identify the two residue symbols.** For p ≠ d the proof combines Euler’s criterion with quadratic reciprocity and d ≡ 3 modulo 4. At p = d both coefficients vanish, so the same Frobenius formula applies. [Knowl, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/frobenius-on-generators.knowl.md#L31) · [ImaginaryQuadraticField.lean:376](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean#L376)

<a name="new-frobenius-on-generators-1"></a>

**New finding · medium · Qualify the Frobenius-element equivalence in the summary.** The summary claims that a domain alone identifies the Frobenius pair. Take p = d, n = 1, the residue field at a prime over d, the identity sign and v = ν_d. The two generator tests hold because σ_v sends ζ to ζ^d and √−d reduces to zero. But the pair (v, 1) cannot equal Frob_d, whose second coordinate is χ_K(d) = 0. State p ∤ q₁ for the two-generator test and p ∤ q₁d for the domain equivalence, as in lines 21 and 27. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/frobenius-on-generators.knowl.md#L5) · [PrimeDecomposition.lean:562](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L562)

<a name="new-frobenius-on-generators-2"></a>

**New finding · low · Use the qualified name of the Frobenius lemma on β_K.** The new citation names New.eq_map_betaK_pow_iff. The actual declaration lives in the New.QuadField namespace, so the placeholder names a different, nonexistent declaration. Change the link target to New.QuadField.eq_map_betaK_pow_iff. [Knowl, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/frobenius-on-generators.knowl.md#L31) · [ImaginaryQuadraticField.lean:395](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean#L395)

<a name="page-partner-of-a-place"></a>

## Partner of an infinite place

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/partner-of-a-place.knowl.md) · [ThetaProducts.lean:138](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean#L138)

The integer naming the partner is tested for invertibility even when e = 0. The lemma in the body gives the required exponent and integrality hypotheses, which the summary still omits.

<a name="prior-partner-of-a-place-1"></a>

**Resolved · medium · Use the unit test on −pᵉ even at e=0.** The definition tests the class of −pᵉ itself and correctly treats e = 0 as a unit for every modulus. The identity fallback is now restricted to nonunits. [Knowl, line 19](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/partner-of-a-place.knowl.md#L19) · [FieldsAndPlaces.lean:287](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L287)

<a name="new-partner-of-a-place-1"></a>

**New finding · medium · Restrict the partner congruence in the summary to admissible exponents.** The unchanged summary asserts the congruence for any prime and exponent. For an odd inert p, take e = 0 and α = √−d. All the chosen places restrict to the same embedding of K, so the two sides are √−d and −√−d. Their difference is a p-adic unit because p is odd and p does not divide d. The lemma below requires e ∈ Iₚ° and α integral. Qualify the summary by “for e ∈ Iₚ° and integral α” and describe the partner as ν_{−pᵉ}τ, as in the definition. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/partner-of-a-place.knowl.md#L5) · [ThetaProducts.lean:138](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean#L138)

<a name="page-product-of-minors"></a>

## Product of minors attached to a filling

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/product-of-minors.knowl.md) · [Count.lean:772](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L772)

The diagram and minor formula use only heights strictly below the output rank. The revised remark places the Schur row on the correct side of the expansion, but it gives that expansion over a larger range of ranks than the source.

<a name="prior-product-of-minors-1"></a>

**Resolved · medium · The Schur expansion runs in the opposite direction over a general ring.** The revised remark expands the evaluated minor product in entries of its Schur row. It correctly distinguishes this from the subsequent p-adic comparison of individual jet norms. [Knowl, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/product-of-minors.knowl.md#L22) · [Count.lean:772](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L772)

<a name="new-product-of-minors-1"></a>

**New finding · medium · The Schur expansion and jet comparison require compatible ranks.** The revised remark states the expansion for the arbitrary input and output ranks of the definition. With one place, input rank 2, output rank 1, and one height-one column, output truncation gives P_y=1. At y=0 every proposed input coefficient is a degree-one minor and vanishes, so the expansion would read 1=0. Both the expansion and the subsequent jet lemma assume FitsRanks. Require |n| ≤ |n′| and κ(τ,h)=0 whenever |n| &lt. H &lt; |n′| for both Schur conclusions. The definition of P_y itself allows arbitrary ranks. [Knowl, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/product-of-minors.knowl.md#L22) · [Count.lean:772](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L772)

<a name="page-chosen-places-and-characters"></a>

## Chosen places, their residue characters, and characters of given weight

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/chosen-places-and-characters.knowl.md) · [ChosenPlaces.lean:230](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L230)

The cited field page supplies the root-of-unity and product facts used to construct the global characters. The proof restricts the local components to the chosen finite places.

<a name="prior-chosen-places-and-characters-1"></a>

**Resolved · medium · Justify why every root of unity here is a power of ζ.** After Kronecker gives finite order, part 6 of the linked field-properties page identifies the element as a power of ζ. Part 7 supplies the product of embeddings used in the character calculation. [Knowl, line 40](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/chosen-places-and-characters.knowl.md#L40) · [FieldsAndPlaces.lean:482](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L482)

<a name="page-cm-curve-setting"></a>

## The CM lattice, its theta function and the ring of integral series in y

Revised · notation · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/cm-curve-setting.knowl.md) · [Basic.lean:477](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean#L477)

The revised sigma transformation law gives the correct sign on lattice points, the correct Hermitian exponent and the derivative-one normalization. The definition of θ uses the twisted translation by the 2-torsion point and divides by its nonzero value at the origin.

<a name="prior-cm-curve-setting-1"></a>

**Resolved · high · Use the normalized sigma function that defines θ.** The page gives H(ℓ,z) = πz conj(ℓ)/A, sign +1 if ℓ/2 belongs to the lattice and −1 otherwise, and the exact multiplier exp(H(ℓ,z)+H(ℓ,ℓ)/2). It distinguishes the normalization from the classical Weierstrass sigma before defining θ. [Knowl, line 16](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/cm-curve-setting.knowl.md#L16) · [Basic.lean:477](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean#L477)

<a name="page-count-with-charges"></a>

## The count with charges

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/count-with-charges.knowl.md) · [Count.lean:585](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L585)

The integral logarithm convention includes the empty diagram. The chain-rule factor is p raised to the negative filling charge in norm, and the deduction enters the lower valuation bound with a minus sign.

<a name="prior-count-with-charges-1"></a>

**Resolved · low · The truncated bound needs the zero-box logarithm convention.** The truncated statement explicitly sets the integer logarithm at zero to zero, matching Nat.log. The same convention gives the proper cutoff for the e=0 term when p=d. [Knowl, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/count-with-charges.knowl.md#L25) · [Count.lean:595](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L595)

<a name="page-coupling"></a>

## Coupling of places with their partners

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/coupling.knowl.md) · [NormalForm.lean:38](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L38)

The partner can be any map, and it changes only the place coordinate. The displayed sum and its behavior under rescaling and substitution give the stated homogeneous degree.

<a name="page-coupling-sum"></a>

## Sum of powers of couplings

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/coupling-sum.knowl.md) · [NormalForm.lean:90](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L90)

The terms have order at least (p^e+1)p^j, so coefficientwise local finiteness survives substitutions with zero constants. Scaling all variables by α multiplies the (e,j) term by α raised to that same degree.

<a name="page-decomposition-of-primes-in-e"></a>

## Decomposition of primes in E = K(zeta)

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/decomposition-of-primes-in-e.knowl.md) · [PrimeDecomposition.lean:618](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L618)

The Frobenius subgroup and residue-degree arguments use p ∤ q₁d. For a self-conjugate place above d, the separate generator calculation and reduction modulo q₀ exclude dⁿ ≡ −1 without applying the unramified theorem at d.

<a name="page-deduction-term"></a>

## Deduction term and exempt pairs of heights

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/deduction-term.knowl.md) · [NullFrames.lean:116](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean#L116)

The displayed cost follows the source convention on short columns, including formal columns of height zero. The covering choice is constructed with exactly that cost.

<a name="prior-deduction-term-1"></a>

**Resolved · medium · The deduction is an attainable cost, not a minimum.** The revised text asserts existence of a covering choice with the stated cost and explains its role as a determinant-loss bound. The source gives this equality and coverage without minimizing over choices. [Knowl, line 29](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/deduction-term.knowl.md#L29) · [NullFrames.lean:224](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean#L224)

<a name="page-different-of-e"></a>

## The different of E = K(zeta) and its imaginary generator

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/different-of-e.knowl.md) · [PrimeDecomposition.lean:271](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L271)

The replacement field link supplies E and ζ. The different in the tower is generated by P′(ζ)√−d, and the order-5040 root used for Weil data follows from 5040 dividing q₁.

<a name="page-exponent-on-one-curve"></a>

## The exponent on one curve

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/exponent-on-one-curve.knowl.md) · [Exponent.lean:702](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean#L702)

The revised summary includes e = 0 when p = d. The body restricts the unit leading coefficients to odd e at inert primes and treats the special ramified coefficient at (e,j) = (0,0) separately.

<a name="prior-exponent-on-one-curve-1"></a>

**Resolved · low · The summary drops the zeroth ramified exponent.** The summary ranges over all nonnegative e at p = d, including the exponent-zero contribution. It retains the odd-exponent condition in the inert case. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/exponent-on-one-curve.knowl.md#L5) · [Exponent.lean:702](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean#L702)

<a name="page-exponent-series"></a>

## The exponent series of the theta function

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/exponent-series.knowl.md) · [Exponent.lean:240](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean#L240)

The page distinguishes the valuation identities for nonsplit primes from the unconditional root-of-unity filtering and scaled factorization. The filtering identity also exists at its cited declaration in the formal parameter library.

<a name="prior-exponent-series-1"></a>

**Resolved · low · The scaling factorization also holds at split primes.** Property 3 now requires a nonzero scale and the stated lower bound on its valuation. Those are the two scale hypotheses in the source, including at split primes. [Knowl, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/exponent-series.knowl.md#L24) · [Exponent.lean:240](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean#L240)

<a name="page-field-setting"></a>

## The field E = K(zeta) and its group of infinite places

Removed · notation · [Previous page](https://github.com/RyanPersson/knowlpedia-content/blob/8835566df7e272d301d0a0b1d3782a50cdf3eb22/content/proofs/grh/derivatives-divisibility/field-setting.knowl.md) · [FieldsAndPlaces.lean:195](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L195)

The reduction-main owner declares E, Φ, ζ, galOfPlace, placeMulEquiv and placeOfInt and gives the identity fallback. All twelve referring pages have been redirected, and the Frobenius page now defines the pullback action on finite places at its use.

<a name="page-normal-form"></a>

## Normal form of a power series

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/normal-form.knowl.md) · [NormalForm.lean:50](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L50)

The multiplier W is integral and the exponential uses ϖ^(p+1)/p after rescaling each variable by ϖ. The inert and ramified application scales both give cϖ negative valuation.

<a name="page-normal-form-modulo-pi"></a>

## The exponent of a normal form need only be known modulo pi

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/normal-form-modulo-pi.knowl.md) · [NormalForm.lean:144](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L144)

Both exponents have zero constant term. Their difference is divisible coefficientwise by π, and the stated norm condition on cϖπ makes the correction exponential integral by the factorial bound.

<a name="page-normal-form-of-theta-products"></a>

## Normal form of theta products at non-split primes

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/normal-form-of-theta-products.knowl.md) · [ThetaProducts.lean:54](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean#L54)

The added coefficient identity has the total-degree factorial in the numerator and the product of component factorials in the denominator. It also gives the correct constant coefficient for the zero multi-index.

<a name="prior-normal-form-of-theta-products-1"></a>

**Resolved · low · One indexed coefficient identity is absent.** The displayed formula now computes the coefficient for every multi-index, including D = 0, before the proof uses rescaling and multiplication. [Knowl, line 33](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/normal-form-of-theta-products.knowl.md#L33) · [ThetaProducts.lean:54](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean#L54)

<a name="page-p-adic-setting"></a>

## The p-adic setting for derivatives of theta functions

Revised · notation · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/p-adic-setting.knowl.md) · [PrimeNotation.lean:98](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/PrimeNotation.lean#L98)

With d congruent to 7 modulo 8, the table matches the symbol-defined split, inert, and ramified cases, including the factor 1/2 at the ramified prime. The jet pairing uses a product of component factorials.

<a name="page-place-permutation"></a>

## Automorphisms of C over K permute the embeddings of the CM type

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/place-permutation.knowl.md) · [PrimeDecomposition.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L56)

The linked field owner defines the action on ζ and the embeddings Φ_v. Composition with an automorphism fixing K permutes them by multiplication by the place determined at the identity.

<a name="page-places-above-split-primes"></a>

## Places of E above a prime congruent to 1 modulo q1 d

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/places-above-split-primes.knowl.md) · [WeilData.lean:126](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/WeilData.lean#L126)

For p ≡ 1 modulo q₁d the trivial Frobenius gives a trivial stabilizer. The complementary valuations of a and its conjugate in aā = pc choose one prime in each conjugate pair, as required for the bijection.

<a name="page-predicted-divisibility"></a>

## Predicted divisibility of a family of diagrams

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/predicted-divisibility.knowl.md) · [Count.lean:422](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L422)

The half-weighted correction at p=d is exactly the e=0 term omitted by the positive-exponent sum. The symbol determines the geometric-series cases in the more general algebraic statement.

<a name="prior-predicted-divisibility-1"></a>

**Resolved · low · The splitting terminology needs the congruence assumption on d.** The statement requires d ≡ 7 mod 8 for the splitting interpretation, and the proof distinguishes this interpretation from the symbol-defined exponent sets used for arbitrary primes d. [Knowl, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/predicted-divisibility.knowl.md#L15) · [PrimeNotation.lean:163](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/PrimeNotation.lean#L163)

<a name="page-schur-entry-to-minor-product"></a>

## From entries of the Schur matrix to products of minors

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/schur-entry-to-minor-product.knowl.md) · [Count.lean:800](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L800)

The dedicated lemma states the rank conditions and includes the full-height determinant factor. Linear independence over the infinite residue field of the valuation ring supplies the integral evaluation needed to compare jet norms.

<a name="page-supersingular-coefficient-unit"></a>

## The coefficient of z^(p-1) in x at an inert prime

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/supersingular-coefficient-unit.knowl.md) · [FrobeniusCongruence.lean:322](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean#L322)

The proof now obtains the n = 0 differential identity directly from x″ and uses the differentiated power only for n ≥ 1. This supplies the base case needed to run the coefficient recurrence.

<a name="prior-supersingular-coefficient-unit-1"></a>

**Resolved · low · Handle n=0 in the differentiated power formula.** The new split gives the second derivative formula for n = 0 without a negative power of x. The positive cases follow from the product rule, as in the source. [Knowl, line 23](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/supersingular-coefficient-unit.knowl.md#L23) · [FrobeniusCongruence.lean:330](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean#L330)

<a name="page-the-count"></a>

## The count: divisibility of jets along products of minors

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/the-count.knowl.md) · [Count.lean:707](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L707)

Taking no marked places and zero charge exponents gives the stated norm inequality. In the theta corollary the new condition on H is exactly the multiSeriesRing condition on the chosen linear forms.

<a name="prior-the-count-1"></a>

**Resolved · high · The theta-product application omits the integrality hypothesis on H.** The multiplier H must now be an integral series in the particular parameters y(uⱼ†z). The new empty-diagram example also shows why a constant H=p^(−M) with M greater than fN³ would disprove the unrestricted claim. [Knowl, line 29](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/the-count.knowl.md#L29) · [ThetaProducts.lean:449](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean#L449)

<a name="page-theta-product"></a>

## Product of theta functions along linear forms

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/theta-product.knowl.md) · [Resolution.lean:155](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Resolution.lean#L155)

The edited power-series notation preserves the definition by substitution of linear forms. The partial-derivative argument keeps the required integrality of every matrix entry and of the series for y′ in y.

<a name="page-weil-data-of-e"></a>

## The idele alpha and the Weil data of E

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/weil-data-of-e.knowl.md) · [WeilData.lean:420](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/WeilData.lean#L420)

The unit η = ζ^(q₁/4)(ζ−1) has norm one and satisfies ζ·conj(η) = η. The primitive 5040-th root assumed by the existence theorem is supplied by the linked page on the different.

<a name="prior-weil-data-of-e-1"></a>

**Resolved · medium · The splitting-character construction assumes the full group of roots of unity.** Part 6 of the linked field-properties page proves that every finite-order element of E is a power of ζ. The constructed powers of η consequently cover every y required by the existence theorem. [Knowl, line 34](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/weil-data-of-e.knowl.md#L34) · [FieldsAndPlaces.lean:482](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L482)

<a name="prior-weil-data-of-e-2"></a>

**Resolved · low · Specify the integral finite ideles in the character normalization.** The normalization now requires every finite component to be a unit in its local ring of integers, precisely the integral finite idele subgroup in υ_unit. [Knowl, line 19](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/derivatives-divisibility/weil-data-of-e.knowl.md#L19) · [WeilData.lean:63](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/WeilData.lean#L63)
