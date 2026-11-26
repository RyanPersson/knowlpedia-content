# derivatives-divisibility

This area contains 39 individual knowls and a chapter page. The review records 20 comments. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports/derivatives-divisibility.md)

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Chapter page

<a name="page-derivatives-divisibility"></a>

### Derivatives of theta functions: divisibility at non-split primes

Correction recorded · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility.knowl.md) · [Count.lean:707](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L707)

The count has the stated error fN³(1+logₚ max(B,1)) for a nonsplit prime and a scale of valuation ρₚ. The substitution criterion and determinant inequality used to obtain it need their local hypotheses.

<a name="derivatives-divisibility-finding-1"></a>

**High · Coupling divisibility needs a bound on the exponential scale.** The passage from divisibility of the substituted couplings to integral coefficients also uses |(ϖ^(p+1)/p)π|ₚ ≤ p^(−1/(p−1)). A normal form allows arbitrary ϖ. Without the bound, the factorial denominators of the exponential can survive. The substitution must consist of integral series with zero constant term. Include the norm condition and the two conditions on Z where the chapter states the integrality criterion. For the theta application one may instead specify the scale v(ϖ)=ρₚ and record that it supplies the norm bound. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility.knowl.md#L26) · [NormalForm.lean:262](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L262)

<a name="derivatives-divisibility-finding-2"></a>

**Medium · The determinant norm has a lower bound and the cost is additive in valuations.** The argument bounds the weighted sum of the determinant valuations above by v(π) times the sum of the deductions. Equivalently the product of the determinant norms, each with its column multiplicity κ(τ,h), is bounded below by |π| raised to that sum. Bounding this product above by the sum itself can already give 1 ≤ 0 when no congruences are imposed. Pairing divisibility is required only for nonexempt pairs. State the bound on the weighted sum of valuations and restrict the pairing conclusion to nonexempt pairs. [Knowl line 36](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility.knowl.md#L36) · [NullFrames.lean:361](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean#L361)

<a name="derivatives-divisibility-finding-3"></a>

**Medium · The Frobenius description of the decomposition group is unramified.** The pair (χ_K(p)p,χ_K(p)) generates the decomposition group in the cited result when p does not divide q₁d. At p=d its second component is zero and does not represent either Galois sign. This matters in a chapter that also treats p=d. Specify p ∤ q₁d before using the Frobenius element for the decomposition group, and distinguish the separate residue congruence at the ramified prime. [Knowl line 44](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility.knowl.md#L44) · [PrimeDecomposition.lean:612](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L612)

## Knowls with comments

<a name="page-cm-curve-setting"></a>

### The CM lattice, its theta function and the ring of integral series in y

Correction recorded · notation · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/cm-curve-setting.knowl.md) · [Basic.lean:694](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean#L694)

The lattice’s two-torsion conditions, its normalization ℘″(t)=2, and the stated low-degree, scaled-parameter and closure lemmas check out. The sigma function in the definition of θ requires a different normalization from the linked classical function.

<a name="cm-curve-setting-finding-1"></a>

**High · Use the normalized sigma function that defines θ.** The link identifies σ with the classical Weierstrass sigma. The source defines the odd theta section with derivative 1 at zero and multiplier χ(ℓ)exp(H(ℓ,z)+H(ℓ,ℓ)/2). It explicitly records an exp(cz²) factor relative to classical sigma. Translating by t and dividing by the value at zero leaves the nonconstant factor exp(c(z²+2tz)), changing θ and g. Define σ through its normalized transformation law with H(ℓ,z)=πℓ̄z/area Λ and χ=+1 on 2Λ, −1 elsewhere. Link that definition where θ is introduced and distinguish its relationship to classical sigma. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/cm-curve-setting.knowl.md#L14) · [Basic.lean:469](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean#L469)

<a name="page-the-count"></a>

### The count: divisibility of jets along products of minors

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/the-count.knowl.md) · [Count.lean:707](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L707)

The uncharged inequality follows by using no marked places and zero exponents. The application in the remarks loses a necessary assumption on the multiplier.

<a name="the-count-finding-1"></a>

**High · The theta-product application omits the integrality hypothesis on H.** The cited normal-form theorem requires H to be an integral series in the coordinates y(u_j†z). The remark leaves H unrestricted. For the empty diagram the jet is F(0), and θ(0) = 1. Taking H = p^(−M) gives |F(0)| = p^M, exceeding the stated p^(f N³) bound for M &gt; f N³. In the remark require H ∈ O\[\[y(u_j†z) : j ∈ J\]\], as in the normal-form theorem. Keep the main bound for F already known to have the normal form. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/the-count.knowl.md#L29) · [ThetaProducts.lean:449](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean#L449)

<a name="page-chosen-places-and-characters"></a>

### Chosen places, their residue characters, and characters of given weight

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/chosen-places-and-characters.knowl.md) · [ChosenPlaces.lean:230](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L230)

The character orders, the two chosen global weights and the finite-support extension criterion agree with the source. The proof appeals without support to the field-specific classification of the roots of unity.

<a name="chosen-places-and-characters-finding-1"></a>

**Medium · Justify why every root of unity here is a power of ζ.** Kronecker’s theorem gives finite order for an integral norm-one γ. The next inference γ=ζᵏ uses a special property of E. Merely adjoining a primitive q₁-th root to a CM field does not ensure that it generates all roots of unity. This fact is needed to make the tame factor trivial. Name Kronecker’s theorem and link parts 6 and 7 of proofs/grh/reduction-main/field-e-properties, which prove μ(E)=⟨ζ⟩, N(E/K)(ζ)=1 and the product formula for the chosen embeddings. [Knowl line 40](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/chosen-places-and-characters.knowl.md#L40) · [FieldsAndPlaces.lean:482](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L482)

<a name="page-deduction-term"></a>

### Deduction term and exempt pairs of heights

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/deduction-term.knowl.md) · [NullFrames.lean:116](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean#L116)

The displayed cost, including height zero in r and the marking condition for t, and the asymmetric exemption agree with the definitions. The claim of optimality in the remark fails.

<a name="deduction-term-finding-1"></a>

**Medium · The deduction is an attainable cost, not a minimum.** The source constructs one covering choice of this cost. With N=3, no marks, one height-two column on each side, p=3 and e=1, the displayed D is 1. Imposing only the source-entry conditions at every height covers every pair and costs 2/3 by the source’s definitions of cost and covering. Describe D as the cost of the specified covering choice and an upper bound on the required determinant loss. Remove the global optimality claim. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/deduction-term.knowl.md#L29) · [NullFrames.lean:224](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean#L224)

<a name="page-frobenius-congruence-for-theta"></a>

### Frobenius congruence for the theta function

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta.knowl.md) · [FrobeniusCongruence.lean:224](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean#L224)

The low-degree coefficient bounds, extraction from R(x) using x=z²+⋯, and logarithmic closure give both congruences. Step 1 misdescribes the input on torsion values and points to an incorrect isogeny identifier.

<a name="frobenius-congruence-for-theta-finding-1"></a>

**Medium · The integrality input concerns twisted torsion values.** For a degree-n section f the library controls the image of f\[u\]=f(u) exp(−nπ|u|²/(2 area Λ)). Its isogeny pullback preserves these normalized values with the degree multiplied by q. Plain values f(u), as the text calls them, have an extra factor whose p-adic norm the cited result does not control. Define f\[u\] in Step 1 or link its exact definition, and use f\[u\] in degrees q and one when applying the pullback and even-section expansion. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta.knowl.md#L24) · [TorsionValues.lean:129](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Integrality/TorsionValues.lean#L129)

<a name="frobenius-congruence-for-theta-finding-2"></a>

**Low · Correct the isogeny reference.** The proposed dependency New.CMLattice.IsIsogeny is declared as PeriodPair.IsIsogeny. The CM lattice uses the inherited period pair, which explains the dot notation in the proof. Use PeriodPair.IsIsogeny as the declaration target for the isogeny of degree q. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/frobenius-congruence-for-theta.knowl.md#L24) · [Basic.lean:86](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/Sigma/Basic.lean#L86)

<a name="page-frobenius-on-generators"></a>

### Galois elements as powers of Frobenius: a criterion on generators

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/frobenius-on-generators.knowl.md) · [PrimeDecomposition.lean:495](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L495)

The criterion compares ζ and (1+√−d)/2. Reduction of ζ stays primitive in a domain when p does not divide q₁. The character calculation at the quadratic generator needs an additional arithmetic identity.

<a name="frobenius-on-generators-finding-1"></a>

**Medium · Euler’s criterion alone does not identify the two residue symbols.** Euler’s criterion gives (−d/p) from (−d)^((p−1)/2) modulo p. Here χ_K(p) is defined as (p/d), with the numerator and denominator exchanged. Lean explicitly uses quadratic reciprocity and d ≡ 3 modulo 4 to pass between them. For p ≠ d, insert (−d/p) = (−1/p)(d/p) = (p/d) by quadratic reciprocity, and mention that both symbols vanish for p = d. Then iterate Frobenius on √−d. [Knowl line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/frobenius-on-generators.knowl.md#L31) · [ImaginaryQuadraticField.lean:376](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean#L376)

<a name="page-partner-of-a-place"></a>

### Partner of an infinite place

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/partner-of-a-place.knowl.md) · [ThetaProducts.lean:107](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean#L107)

The tests on ζ and √−d, followed by clearing a denominator prime to p, prove both stated congruences for e∈Iₚ°. The unrestricted definition mishandles exponent zero at primes dividing q₁.

<a name="partner-of-a-place-finding-1"></a>

**Medium · Use the unit test on −pᵉ even at e=0.** The source tests whether the integer −pᵉ represents a unit. If p divides q₁ and e=0, this integer is −1 and is a unit. Its place is distinct from the identity since q₁&gt;2. For example the stated fallback gives the wrong partner for p=2, e=0. Use the class of −pᵉ whenever gcd(pᵉ,q₁)=1, and the identity otherwise. Equivalently the fallback requires p|q₁ and e&gt;0. [Knowl line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/partner-of-a-place.knowl.md#L19) · [FieldsAndPlaces.lean:287](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L287)

<a name="page-product-of-minors"></a>

### Product of minors attached to a filling

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/product-of-minors.knowl.md) · [Count.lean:119](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L119)

The determinant, row order and cutoff h &lt; |n′| agree with the definition. The remark reverses the Schur expansion in a setting where the converse can fail.

<a name="product-of-minors-finding-1"></a>

**Medium · The Schur expansion runs in the opposite direction over a general ring.** For R = F₂, rank two and three height-one columns filled with the first row (x,y), every evaluated product has the form (a x + b y)³. Its x²y and xy² coefficients are both ab, while the corresponding Schur row has separate entries x²y and xy². Hence their linear span cannot supply these entries individually. Other row fillings vanish when the second matrix row is set to zero. Say that P_y expands as a linear combination of Schur entries with coefficients given by evaluated minors. Over C_p the linked lemma gives, for each entry, an integral y whose jet is at least as large in norm. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/product-of-minors.knowl.md#L22) · [Count.lean:772](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L772)

<a name="page-weil-data-of-e"></a>

### The idele alpha and the Weil data of E

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/weil-data-of-e.knowl.md) · [WeilData.lean:420](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/WeilData.lean#L420)

The components of α, the negative different exponent for jαā, the positive sign of Im Φ(j), and the unit η = ζ^(q₁/4)(ζ−1) agree with the construction.

<a name="weil-data-of-e-finding-1"></a>

**Medium · The splitting-character construction assumes the full group of roots of unity.** A primitive q₁-th root in E supplies its powers, but alone does not show that they exhaust the roots of unity of E. Exhaustion is necessary because the cited character-existence theorem quantifies over every root of unity, and it is a separate field-specific result in Lean. Link the existing proof ‘field-e-properties’, part 6, at the assertion y = ζ^k. The result follows by embedding E in Q(ζ_(q₁d)) and excluding a primitive d-th root by degree. The primitive 5040-th root required by the existence theorem is recorded in ‘different-of-e’. [Knowl line 34](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/weil-data-of-e.knowl.md#L34) · [FieldsAndPlaces.lean:482](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L482)

<a name="weil-data-of-e-finding-2"></a>

**Low · Specify the integral finite ideles in the character normalization.** All finite ideles are units of the finite adele ring. The formula for υ(x) is imposed when the finite part is a unit of the integral finite adeles, so that every finite component has valuation zero. Write ‘when x_w lies in O_(E_w)^× for every finite place w’ in the definition of the splitting character. [Knowl line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/weil-data-of-e.knowl.md#L19) · [WeilData.lean:63](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/WeilData.lean#L63)

<a name="page-count-with-charges"></a>

### The count with charges

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/count-with-charges.knowl.md) · [Count.lean:662](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L662)

The determinant contributes one row charge per box. Assigning exponent one to absent heights leaves the filling charge unchanged and extends the charge condition to all heights.

<a name="count-with-charges-finding-1"></a>

**Low · The truncated bound needs the zero-box logarithm convention.** The diagrams can have B = 0. The displayed bound then contains floor(log_p 0), whereas Lean uses Nat.log p 0 = 0. The main bound uses max(B,1) and already covers this case. Declare floor(log_p 0) = 0 for the truncated form, or use floor(log_p max(B,1)) in both appearances. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/count-with-charges.knowl.md#L27) · [Count.lean:595](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L595)

<a name="page-exponent-on-one-curve"></a>

### The exponent on one curve

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/exponent-on-one-curve.knowl.md) · [Exponent.lean:702](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean#L702)

The functional equation has factor 2 in ramified degree two and a unit congruent to 1 in degrees above two. The resulting three ramified coefficients and the common inert unit match the body of the knowl.

<a name="exponent-on-one-curve-finding-1"></a>

**Low · The summary drops the zeroth ramified exponent.** The summary uses I_p, the positive partner exponents. The theorem uses I_p°. When p = d it includes e = 0 and supplies the diagonal terms of degrees 2p^j, starting with coefficient λ/2 at degree two. The body already has the right index set. Replace ‘e in I_p’ in the summary by ‘e in I_p° (including zero at the ramified prime)’. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/exponent-on-one-curve.knowl.md#L5) · [Exponent.lean:670](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean#L670)

<a name="page-exponent-series"></a>

### The exponent series of the theta function

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/exponent-series.knowl.md) · [Exponent.lean:196](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean#L196)

Averaging against ζ^(−i(p+1)) selects the claimed residue class. The q_p−1 power can be removed since it is coprime to p, and scaling gives the displayed factorization.

<a name="exponent-series-finding-1"></a>

**Low · The scaling factorization also holds at split primes.** The standing assumption χ_K(p) ≠ 1 is applied to all listed properties except the explicit exception for property 2. Property 3 also holds at every prime, with only ϖ ≠ 0 and |ϖ| ≤ p^(−ρ_p). Its proof uses property 2 and scaling, both valid at split primes. Restrict the nonsplit hypothesis to property 1, or explicitly say that properties 2 and 3 hold for all primes. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/exponent-series.knowl.md#L22) · [Exponent.lean:240](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Exponent.lean#L240)

<a name="page-normal-form-of-theta-products"></a>

### Normal form of theta products at non-split primes

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/normal-form-of-theta-products.knowl.md) · [ThetaProducts.lean:443](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean#L443)

The uniform order of the quantifiers, the involution on the first dagger factor, and the weighted Frobenius step all agree. For both nonsplit cases v(cϖπₚ)=1/(p−1), giving the promised integral correction.

<a name="normal-form-of-theta-products-finding-1"></a>

**Low · One indexed coefficient identity is absent.** The page lists New.coeff_subst_linearSeries as a translated declaration, but it gives only the rescaling consequence. A reader following that identifier here cannot find the coefficient of g(∑cₓzₓ), a formula reused by the sharpness proofs. State \[zᴰ\]g(∑ₓcₓzₓ) = g_{|D|} · (|D|! / ∏ₓDₓ!) · ∏ₓcₓ^{Dₓ} by the multinomial theorem, or assign this identifier to a page that states it. [Knowl line 10](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/normal-form-of-theta-products.knowl.md#L10) · [ThetaProducts.lean:54](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/ThetaProducts.lean#L54)

<a name="page-predicted-divisibility"></a>

### Predicted divisibility of a family of diagrams

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/predicted-divisibility.knowl.md) · [Count.lean:422](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L422)

Expanding both positive parts reproduces the deduction, including height-zero columns and half the zeroth term when p = d. Removing the marked height-one columns gives the truncated inequality.

<a name="predicted-divisibility-finding-1"></a>

**Low · The splitting terminology needs the congruence assumption on d.** The opening quantifies over primes d and p. For that generality Lean selects the odd exponents by the symbol (p/d). At d = 5, p = 3, the prime splits in Q(√−5), yet (3/5) = −1 and the positive-exponent sum is 3/8. The linked p-adic setting imposes d ≡ 7 modulo 8, where the two descriptions agree. Give the proof’s cases as (p/d) = −1, p = d and (p/d) = 1. Alternatively, explicitly restrict this presentation to d ≡ 7 modulo 8. [Knowl line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/predicted-divisibility.knowl.md#L35) · [PrimeNotation.lean:163](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/PrimeNotation.lean#L163)

<a name="page-supersingular-coefficient-unit"></a>

### The coefficient of z^(p-1) in x at an inert prime

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/supersingular-coefficient-unit.knowl.md) · [FrobeniusCongruence.lean:416](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean#L416)

The differentiated cubic gives the asserted three-term recurrence, and p&lt;p² gives the needed integrality in degree p. The contradiction hₘ=1 and both base cases work. The displayed derivation needs a separate zero-index interpretation.

<a name="supersingular-coefficient-unit-finding-1"></a>

**Low · Handle n=0 in the differentiated power formula.** The intermediate term n x^(n−1)(x′)² uses x⁻¹ when n=0, but x starts in degree two and has no inverse in the formal power series ring. The zero-index recurrence is used to propagate the induction and is already the displayed identity for x″. Apply the product-rule expression for n≥1 and say that n=0 follows directly from x″=6x²+a₁²x+2. [Knowl line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/supersingular-coefficient-unit.knowl.md#L25) · [FrobeniusCongruence.lean:330](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/FrobeniusCongruence.lean#L330)

## Other knowls checked

<a name="page-change-of-directions"></a>

### Change of directions

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/change-of-directions.knowl.md) · [NullFrames.lean:361](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean#L361)

Each congruence in the four-way cover applies at the required height. Source congruences carry the weight p⁻ᵉ, partner congruences carry weight one, and determinant divisibility yields the stated lower bound on the product of norms.

<a name="page-coupling"></a>

### Coupling of places with their partners

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/coupling.knowl.md) · [NormalForm.lean:38](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L38)

The second variable keeps the coordinate i and changes only τ to prₑτ. Each monomial has degree pᵉ+1, including at e=0 and for a partner rule with fixed points.

<a name="page-coupling-sum"></a>

### Sum of powers of couplings

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/coupling-sum.knowl.md) · [NormalForm.lean:43](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L43)

The lower bound pʲ(pᵉ+1) gives a finite set of contributing pairs in each bounded degree. It also supplies the exponent of α in the stated rescaling and survives substitution of series with zero constant term.

<a name="page-coupling-sum-derivatives"></a>

### Derivatives of a coupling sum modulo p

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/coupling-sum-derivatives.knowl.md) · [NormalForm.lean:355](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L355)

The derivative kills the j&gt;0 terms modulo p, and 0∉S removes the derivatives of the first factors at j=0. The pure monomial of degree pᵉ occurs once in its partner sum and no sum for e′≠e can contribute to that degree.

<a name="page-critical-pair"></a>

### Pairs of a character and a critical point

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/critical-pair.knowl.md) · [ChosenPlaces.lean:272](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L272)

The data include both the nonnegative weight function and the full residue-character family as well as ν and z. Restricting the tame part to the finitely many chosen primes preserves those data, and the fixed-weight, fixed-tame-part fibers are finite.

<a name="page-decomposition-of-primes-in-e"></a>

### Decomposition of primes in E = K(zeta)

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/decomposition-of-primes-in-e.knowl.md) · [PrimeDecomposition.lean:618](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L618)

The stabilizer test uses (v,1) and the conjugate-place test uses (v,−1). At a self-conjugate place the argument separately excludes p = d, then uses an odd-order unit in a finite 2-group to obtain p ≡ −1 modulo 2^(s+1).

<a name="page-different-of-e"></a>

### The different of E = K(zeta) and its imaginary generator

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/different-of-e.knowl.md) · [PrimeDecomposition.lean:243](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L243)

The two extended differents are coprime since their generators divide d and q₁. Tower transitivity gives the required divisibility, the conductor argument gives O_E = O_K\[ζ\], and pairing conjugate embeddings gives the f-th power of the root discriminant.

<a name="page-elimination-of-congruences"></a>

### Imposing congruences on the rows of a matrix by elimination

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/elimination-of-congruences.knowl.md) · [NullFrames.lean:68](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NullFrames.lean#L68)

Maximal p-adic norm gives the divisibility needed for the pivot column, whose replacement has determinant α in positive dimension. Left multiplication by the next matrix preserves the previous row congruences and multiplies determinants in the stated direction.

<a name="page-field-setting"></a>

### The field E = K(zeta) and its group of infinite places

Source checked · notation · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/field-setting.knowl.md) · [FieldsAndPlaces.lean:195](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L195)

The level multiplier is 3^(floor(log₃ s)+5)2^s, including s = 0. The integer-named place is the identity on nonunits modulo q₁, and the CM embeddings all restrict to the inclusion of K.

<a name="page-integral-above-p"></a>

### Elements of a number field integral above a prime

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/integral-above-p.knowl.md) · [Resolution.lean:84](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Resolution.lean#L84)

Removing the p-part from an integer denominator preserves integrality above p and uses that p is a unit everywhere else. Both the denominator and embedding arguments work for an arbitrary number field, as stated.

<a name="page-legendre-bound-for-jets"></a>

### Legendre's bound for the jet of an integral series

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/legendre-bound-for-jets.knowl.md) · [Count.lean:97](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L97)

Each exponent of a degree-l monomial is smaller than p^(floor(log_p l)+1). Legendre’s base-p digit sum gives the claimed factorial loss per variable, including the stated l = 0 convention.

<a name="page-normal-form"></a>

### Normal form of a power series

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/normal-form.knowl.md) · [NormalForm.lean:50](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L50)

The integral factor W has no unit condition. The rescaling uses ϖ on every variable and cϖ=ϖ^(p+1)/p on the full coupling sum, as required by the definition and its nonsplit-prime application.

<a name="page-normal-form-integrality"></a>

### Integrality in low degrees of a series with the normal form

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/normal-form-integrality.knowl.md) · [NormalForm.lean:262](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L262)

For e above the cutoff, substitution preserves order at least pᵉ+1&gt;B. For the remaining e, divisibility passes to all positive powers, and the low-degree exponential bound survives convolution with integral W.

<a name="page-normal-form-modulo-pi"></a>

### The exponent of a normal form need only be known modulo pi

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/normal-form-modulo-pi.knowl.md) · [NormalForm.lean:144](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L144)

The zero-constant difference G is divisible coefficientwise by π. The bound v(j!)≤j/(p−1) makes exp(cϖG) integral, so multiplication by this factor gives the claimed W in each degree.

<a name="page-normal-form-substitution"></a>

### Substitution into a series with the normal form

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/normal-form-substitution.knowl.md) · [NormalForm.lean:169](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L169)

Substituting the zero-constant integral family into the rescaled series gives F(ϖZ). Associativity of substitution transports the exponential and the new integral factor is W(Z), for any target variable set.

<a name="page-normal-form-valuation"></a>

### The normal form depends only on the valuation of varpi

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/normal-form-valuation.knowl.md) · [NormalForm.lean:206](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/NormalForm.lean#L206)

For α=ϖ′/ϖ the homogeneity factor is α^((pᵉ+1)pʲ). Multiplication of the resulting coefficients by (ϖ/ϖ′)^(p+1) exactly compensates the change from cϖ to cϖ′, using the two ratios’ norm one.

<a name="page-p-adic-setting"></a>

### The p-adic setting for derivatives of theta functions

Source checked · notation · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/p-adic-setting.knowl.md) · [PrimeNotation.lean:100](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/CM/FormalGroup/PrimeNotation.lean#L100)

I checked the factorial pairing for the jet, the ring-homomorphism definition of the p-adic place, and the three sets of entries for qₚ, ρₚ, γₚ and the partner exponents. Only the ramified column admits exponent zero.

<a name="page-place-permutation"></a>

### Automorphisms of C over K permute the embeddings of the CM type

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/place-permutation.knowl.md) · [PrimeDecomposition.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/PrimeDecomposition.lean#L56)

The fixed embedding of K rules out its complex conjugate as an embedding over K. This identifies σ∘Φ₁ with Φ_v₀, and composition gives the left translation v ↦ v₀v.

<a name="page-places-above-split-primes"></a>

### Places of E above a prime congruent to 1 modulo q1 d

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/places-above-split-primes.knowl.md) · [WeilData.lean:126](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/WeilData.lean#L126)

Writing aā = pc with p ∤ c forces exactly one of a and ā into each prime above p, with order one. Freeness of the action and transitivity up to conjugation give the stated bijection.

<a name="page-resolution-of-the-identity"></a>

### Resolution of the identity by vectors over a CM field

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/resolution-of-the-identity.knowl.md) · [Resolution.lean:60](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Resolution.lean#L60)

The matrix identity uses Φ_w(u) on the left and the complex conjugate at the second index. Applying ι_p gives the coordinate-extraction identity, while expanding against z and z′ gives the stated Parseval formula.

<a name="page-schur-entry-to-minor-product"></a>

### From entries of the Schur matrix to products of minors

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/schur-entry-to-minor-product.knowl.md) · [Count.lean:800](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Divisibility/Count.lean#L800)

The determinant exponent appears only when the smaller rank is strictly smaller. After normalization by a maximal coefficient, independence over the infinite residue field supplies an integral evaluation attaining that coefficient’s norm.

<a name="page-size-of-the-different"></a>

### Size of the different and of the root discriminant at the infinite places

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/size-of-the-different.knowl.md) · [ChosenPlaces.lean:354](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L354)

The cyclotomic chain rule and the geometric mean give the stated bounds. In the numerical step marked as an outline, 3l₀m²² lies between x¹¹ and 7776·2²²(log x)x¹¹, and the scale inequalities absorb this extra factor and exp(±c_P)√d inside the remaining factor x.

<a name="page-theta-product"></a>

### Product of theta functions along linear forms

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/theta-product.knowl.md) · [Resolution.lean:155](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/FormalGroup/Resolution.lean#L155)

Uniform rescaling carries each μ_j to aμ_j. For derivatives the integrality of μ_{j,x} and of y′ as a series in y is exactly what keeps the chain-rule terms in the same ring.

<a name="page-vacuum-root"></a>

### The number s_0 and the absolute values of its conjugates

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/derivatives-divisibility/vacuum-root.knowl.md) · [WeilData.lean:518](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/WeilData.lean#L518)

A positive power of χ_f(α) is the relative norm of ȳ, so every K-automorphism preserves |s₀|. The square on each complex local modulus yields |α| = ∏ᵥ|P′(ζ)|ᵥ and the stated root-discriminant ratio.
