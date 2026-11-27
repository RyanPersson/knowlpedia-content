# upper-objects

This area contains 64 individual knowls and a chapter page. The review records 42 comments. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports/upper-objects.md)

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Chapter page

<a name="page-upper-objects"></a>

### Upper bound: source forms, target forms, chains of lifts and theta kernels between definite spaces

Correction recorded · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects.knowl.md) · [LabelsAndIndexTypes.lean:376](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L376)

The shifted lift weight κ_j=κ+(j+½)Δ is correct. The top definite spaces have ranks n_m and n_m−1 as stated, and the single-lift gauge result is an upper bound on a multiplicative norm factor.

<a name="upper-objects-finding-1"></a>

**High · The mirror and glued identities require a target translate and scalar.** An unmodified mirror lift is described as Up after a direct lift, and a glued double lift as two direct lifts after Up. In the first formula the target is acted on by D_N=diag(1,…,1,N⁻¹), as in line 714 of the source. In the second, the same target translate is required and the right-hand side is multiplied by the number of primitive vectors times γ′γ. Both identities apply to ramified input. Say that the D_N-translate of the mirror lift equals Up of the direct lift on ramified vectors, and that the D_N-translate of the raw glued pair equals the stated scalar times the two direct lifts after Up. [Knowl line 47](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects.knowl.md#L47) · [LiftLawsModuloN.lean:808](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L808)

<a name="upper-objects-finding-2"></a>

**Medium · The good idempotent requires a primitive label above each level prime.** The single-prime description of a good tuple is correct. For e₀ the sum is indexed by a family containing one such tuple above each of p₀ and p₁. The wording can be read as asking for one primitive label anywhere in the entire family. Specify that each of the two tuples must contain a primitive label before its family contributes to e₀. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects.knowl.md#L21) · [LabelsAndIndexTypes.lean:364](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L364)

## Knowls with comments

<a name="page-archimedean-bounds-for-jets"></a>

### Archimedean bounds for the conjugates of jets of theta kernels

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/archimedean-bounds-for-jets.knowl.md) · [JetConjugatesAndBounds.lean:731](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean#L731)

The exponent from the polynomial bound, the dimension in the Gaussian integral, and the use of Gram duality for the Schur matrix agree with the source. The character hypothesis and the coordinate map in the intermediate integral require repairs.

<a name="archimedean-bounds-for-jets-finding-1"></a>

**High · The bound requires automorphic characters.** The theorem allows characters of U(1)(A) with specified weights and tame parts, but the source requires continuous unitary characters trivial on rational norm-one points. The stated local data only control points integral at finite places. At a split place w, for example, u ↦ ξ^ord_w(u_w) for transcendental ξ of modulus one is trivial on integral points and has weight zero. A complex field automorphism can send ξ off the unit circle. The argument on line 44 cannot discard this factor for arbitrary finite determinants. Require a and b to be automorphic characters of U(1)(E⁺)\U(1)(A). For arbitrary finite determinants cite AutChar.HasWeight.norm_map_eq_one (Lib/ClassField/HeckeCharacter/AlgebraicValues.lean:369), which uses algebraic base change. [Knowl line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/archimedean-bounds-for-jets.knowl.md#L23) · [JetConjugatesAndBounds.lean:731](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean#L731)

<a name="archimedean-bounds-for-jets-finding-2"></a>

**Medium · Restore the rescaling of the adelic argument in the Gaussian identity.** The integration variable y has complex Fock coordinates. The source evaluates the adelic function at realVec(y), whose finite coordinates are zero and whose coordinates at τ are (2π Im τ(ȷ))^(−1/2)y_τ. The formula F′(y), repeated for ΛF on line 42, drops this rescaling and does not give the cited identity under the ordinary inclusion of the archimedean vectors. Define realVec with its place-dependent scale and use F′(realVec y) and (ΛF)(realVec y). The uniform absolute-value estimate still applies at these points. [Knowl line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/archimedean-bounds-for-jets.knowl.md#L38) · [JetConjugatesAndBounds.lean:592](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean#L592)

<a name="page-definite-kernel-scale"></a>

### Rational equivariance, integrality and size of definite theta kernels

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/definite-kernel-scale.knowl.md) · [DefiniteKernelSize.lean:366](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/DefiniteKernelSize.lean#L366)

The two transposes, determinant exponents, factor (M²)^(2f|N||L|), homogeneous degree, and the scale of the integral jet agree. The archimedean argument uses one fixed automorphism for the polynomial bound and every automorphism for the finite datum, as stated.

<a name="definite-kernel-scale-finding-1"></a>

**High · Require automorphic characters in the kernel theorem.** Characters of the adelic group with specified archimedean exponents and tame parts can be nontrivial on rational points. For example a unitary character of the valuation at one split finite place is trivial on integral units and can detect a rational element of norm one. Rational invariance in part 1 and its proof requires both twists to be trivial on the rational norm-one subgroup. Take a and b to be continuous circle-valued automorphic characters of the norm-one adeles, trivial on rational norm-one points, with the indicated weights and tame parts. Link this condition in the opening sentence. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/definite-kernel-scale.knowl.md#L15) · [Basic.lean:74](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/HeckeCharacter/Basic.lean#L74)

<a name="definite-kernel-scale-finding-2"></a>

**Medium · Specify which ideals are moduli for these kernels.** The page calls 𝔪 a modulus without giving the project’s restriction that it is a nonzero ideal coprime to its complex conjugate. For instance 𝔪=(M²) contains M² as part 3 asks, but both primes of every conjugate pair in its support occur, so it is outside the kernel construction. Define 𝔪 as a nonzero ideal of the integers of E with no prime dividing both 𝔪 and its conjugate, and link the project definition of modulus. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/definite-kernel-scale.knowl.md#L15) · [Defs.lean:207](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/Defs.lean#L207)

<a name="page-grid-centres"></a>

### The centre system of a grid

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/grid-centres.knowl.md) · [Parameters.lean:835](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean#L835)

The separation of the distinguished first m up/down centres and the offset sign count agree. The claimed identification of the parameters mixes two normalizations and uses labels outside the stated domain.

<a name="grid-centres-finding-1"></a>

**High · The doubled grid parameter lists twice the half-integral centre parameter.** The linked centre-system definition uses λ_B in half-integer units. At z=1 and o=i=j=0, the node has no blocks or lowering: its doubled base entry is 2λ^Y_{τ,n}+1 (Parameters.lean:123), while λ_B has entry λ^Y_{τ,n}+½. The two vectors cannot be identified as asserted. Write l^o_{i,j}=2λ_B under the signed indexing (equivalently, l^o_{i,j}/2 lists λ_B), and preserve this convention in the proof. [Knowl line 28](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/grid-centres.knowl.md#L28) · [InsertBlock.lean:96](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/InsertBlock.lean#L96)

<a name="grid-centres-finding-2"></a>

**High · The stated index range can place an undefined centre in B.** The page only introduces u_l,d_l for l&lt;m and links a definition requiring B⊆C. The allowed choice o=j=0, i=m+1 puts u_m in B. Lean's parameter theorem genuinely allows this i because it defines the labels on ℕ ⊕ ℕ. Its separate containment lemma needs i≤m as well as o+j≤m. Define u_l,d_l for every natural l, distinguish the first m of each as C, and use the ambient-label definition of IsParam. If presenting only nodes inside the finite grid, say so and add i≤m to item 3 and appropriate bounds to the recurrences. [Knowl line 28](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/grid-centres.knowl.md#L28) · [Parameters.lean:538](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean#L538)

<a name="page-signs-and-parameter-of-w"></a>

### Signs of W_j, doubled target parameter, and entry signs

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/signs-and-parameter-of-w.knowl.md) · [LabelsAndIndexTypes.lean:328](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L328)

The threshold defining the sign and the two branches of the target parameter agree, including the shift a+2−k and doubling. The derived signature count extends beyond the range where that threshold is in the row index set.

<a name="signs-and-parameter-of-w-finding-1"></a>

**High · The stated signature count fails for j greater than m.** The entrywise sign rule is given for every natural j, but its asserted counts k+j−1 and m−j need j≤m. At j=m+1 the threshold is r+1, so all r entries are positive, whereas the text counts r+1 positive signs. The source proves the count for the lift indices 1≤j≤m in Rows.lean. Restrict the count to 0≤j≤m, including the convention for j=0, or give the all-j counts min(r,k+j−1) and r−min(r,k+j−1). [Knowl line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/signs-and-parameter-of-w.knowl.md#L19) · [LabelsAndIndexTypes.lean:328](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L328)

<a name="page-block-datum"></a>

### Block datum of a descent pair

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/block-datum.knowl.md) · [AuxiliaryPair.lean:348](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L348)

The determinants use the selected rows, and the identity indicator uses MQ while the block datum can be read modulo M²Q. The description of the finite vacuum drops its lattice phase.

<a name="block-datum-finding-1"></a>

**Medium · The finite vacuum is a twisted lattice indicator.** The parenthesis identifies the vacuum away from the designated places with the characteristic function of the lattice. In the development’s Heisenberg model it vanishes off the lattice and equals the semicharacter ψ₀(c₀ x\*x/2) on it. Substituting a plain indicator loses the phase. Use “the finite vacuum” or give its twisted lattice-indicator formula. Specify a different realization if intending an indicator in a local Schrödinger model. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/block-datum.knowl.md#L22) · [FiniteMultiplier.lean:255](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/FiniteMultiplier.lean#L255)

<a name="page-centre-system"></a>

### Centre system and its parameters

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/centre-system.knowl.md) · [InsertBlock.lean:38](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/InsertBlock.lean#L38)

The lowering by one half and the sign from omitted centres are correct in the undoubled convention. The definition restricts the ambient labels in a way that prevents the later grid parameter theorem from being stated with its actual quantifiers.

<a name="centre-system-finding-1"></a>

**Medium · Distinguish the ambient labels from the finite separated centres.** The page gives centre, length and kind only on C and defines λ_B only for B⊆C. The source defines all three functions on an ambient index type I, with distinguished finite C⊆I. Entries, rank, lowering and IsParam are defined for every finite B⊆I. The grid uses B with labels outside C for some nodes allowed by its parameter theorem. Introduce I and the distinguished finite set C. Define B-indexed data for any finite B⊆I, keep the sign count over C∖B, and impose B⊆C when proving a gap or inserting a separated centre. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/centre-system.knowl.md#L18) · [InsertBlock.lean:38](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/InsertBlock.lean#L38)

<a name="page-columns-of-the-weights"></a>

### The weights of X_j and Y_m in terms of their columns

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/columns-of-the-weights.knowl.md) · [Weights.lean:291](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Weights.lean#L291)

The diagram recurrence adds Δ−(t+1). The last determinant entry and the kept-column telescoping formula have the indicated signs. The all-index version of the branching identity calls on a weight beyond its declared range.

<a name="columns-of-the-weights-finding-1"></a>

**Medium · Define the extended weight sequences or restrict the branching identity.** The first identity in part 3 is stated for all p, although the linked definition gives μ(Xₘ) only for p&lt;nₘ and describes μ(Yₘ) as a weight of length nₘ−1. Both terms are undefined there at p=nₘ−1. Zero-padding cannot fix this, since kept(nₘ)&gt;0. Lean’s coefficient functions are defined by the infinite parameter sequences at every natural index. Either restrict the first identity to p+1&lt;nₘ or define the auxiliary continuation μ(Xⱼ)ₚ=λˣₚ−((nⱼ−1)/2−p), and analogously for Yₘ, for every p≥0. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/columns-of-the-weights.knowl.md#L21) · [Weights.lean:478](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Weights.lean#L478)

<a name="page-descent-pair"></a>

### Descent pair

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/descent-pair.knowl.md) · [AuxiliaryPair.lean:172](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L172)

The block stabilizers, inverse character on the Q-block, determinant exponent and action of the chosen group agree with the definitions. The stated data omit a joint restriction on the place families.

<a name="descent-pair-finding-1"></a>

**Medium · Require the level places to be jointly conjugate-apart.** Two finite families of split places can still contain w in M and its conjugate in Q, or repeat a place. Lean requires the family on the disjoint union to be injective and disjoint from its conjugate. Both requirements are used for independent reductions. Add that all listed places are pairwise distinct and that the conjugate of any listed place is absent from both lists. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/descent-pair.knowl.md#L18) · [PAdicGauge.lean:346](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean#L346)

<a name="page-descent-pair-fitting-parameters"></a>

### A parameter fits a descent pair

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/descent-pair-fitting-parameters.knowl.md) · [AuxiliaryPair.lean:704](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L704)

I checked the shifts in the block rule, descending signed numbering and vanishing above the sign ranks. The parameter and the staircase polynomial are misstated for a general descent pair.

<a name="descent-pair-fitting-parameters-finding-1"></a>

**Medium · Restrict the sum defining the determinant exponent.** The displayed exponent is −∑ᵢ k⁻(τ,i). Lean sums only over 1≤i&lt;|n|. Descent pairs impose no general support condition, and even a fitted pair permits a nonzero count at height zero. With k⁻(τ,0)=1 and all other negative counts zero the two interpretations give −1 and 0, changing the doubled parameter by 2. Write −∑_{1≤i&lt;|n|} k⁻(τ,i), consistently with the descent-pair page. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/descent-pair-fitting-parameters.knowl.md#L18) · [AuxiliaryPair.lean:229](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L229)

<a name="descent-pair-fitting-parameters-finding-2"></a>

**Medium · Define staircase entries for arbitrary numberings.** The definition uses the “first p columns” of a sign, although a descent pair’s numbering need not be injective or consecutive. A 1 by 1 block with two positive columns both numbered zero contains their sum in Lean. Picking the first column gives a different polynomial. For row position i and column number j, sum X_{a,c} over rows a of position i and columns c of the given sign with ν(c)=j. Explain that this reduces to a genuine leading minor for the positive powers under the fitting hypotheses. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/descent-pair-fitting-parameters.knowl.md#L27) · [Lift.lean:84](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Lift.lean#L84)

<a name="page-descent-pairs-of-the-data"></a>

### The descent pairs (W_j, V_j) of the data, and their parameters

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/descent-pairs-of-the-data.knowl.md) · [Rows.lean:841](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean#L841)

The inserted block is centred at −wⱼ, and raising the first character weight by u while raising the second doubled parameter by 2u keeps the shifted entries fixed. The proof mixes the two parameter conventions when applying the centre-system result.

<a name="descent-pairs-of-the-data-finding-1"></a>

**Medium · Use the same factor of two as the cited centre-system definition.** The linked centre-system page defines λ_B in half-integer units, and its stem here is {ςₚ}. The proof identifies 2ς with λ_∅ and l′−2u with λ_{ {d} }. Lean’s IsParam actually says that those vectors list twice λ_B. As written the entries of the first vector already differ from the cited stem before insertion. Write 2ς=2λ_∅ and l′−2u=2λ_{ {d} } up to indexing, or explicitly put the stem, blocks, sign thresholds and lowering in doubled units throughout. Then apply the undoubled insertion theorem to ς and l′/2−u. [Knowl line 37](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/descent-pairs-of-the-data.knowl.md#L37) · [InsertBlock.lean:96](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/InsertBlock.lean#L96)

<a name="descent-pairs-of-the-data-finding-2"></a>

**Low · The column formula uses truncated indices at actual heights.** The parenthesis says truncation only matters outside the range used. The valid step p=0 already evaluates k⁻ at height r+t−1&gt;r in c(1), so both of its target-parameter indices truncate to zero. Without the convention these entries have negative indices. Keep the definition of truncated subtraction and drop the parenthesis, or give c(1) as an example of an in-range use. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/descent-pairs-of-the-data.knowl.md#L22) · [Rows.lean:660](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean#L660)

<a name="page-gauge-bounds-for-one-lift"></a>

### p-adic gauge bounds for one theta lift between definite spaces

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/gauge-bounds-for-one-lift.knowl.md) · [ThetaLiftGauge.lean:186](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L186)

The reductions to gauges at 1 and d⁻¹, the weighted minor criterion, the p-exponent and the clearing multiple agree. The opening paragraph conflates two different integrality conditions.

<a name="gauge-bounds-for-one-lift-finding-1"></a>

**Medium · Name the character exponent in the lift-weight hypothesis.** The parenthesis gives the source and target determinant exponents e and eₐ, but the linked IsLiftWeight condition uses eᵦ and e. At each place the source exponent e must equal eᵦ plus the number of columns of full source height. The target exponent eₐ does not enter that compatibility equation. Specify IsLiftWeight(n,n′,κ,eᵦ,e), or write e(τ)=eᵦ(τ)+κ(τ,|n|) alongside the linked shape condition. Keep eₐ as the target determinant exponent. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/gauge-bounds-for-one-lift.knowl.md#L15) · [ThetaKernelDefs.lean:84](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/CompactLift/ThetaKernelDefs.lean#L84)

<a name="gauge-bounds-for-one-lift-finding-2"></a>

**Medium · Translation vectors need integral entries only.** As written, the definition of “integral above p” requires an invertible matrix immediately after using it for δx. Here x is an additive n′ by n translation vector, generally rectangular. The zero translation is always allowed, so the integral vacuum itself is a generator. Say that δx has integral entries at each place above p. Reserve integral invertibility for the unitary group elements g, h, x, y used to translate or compare gauges. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/gauge-bounds-for-one-lift.knowl.md#L15) · [IntegralVacuum.lean:328](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L328)

<a name="page-glued-datum-in-the-schrodinger-model"></a>

### The gluing of a double lift in the Schrödinger model above N

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/glued-datum-in-the-schrodinger-model.knowl.md) · [Columns.lean:522](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L522)

The complementary diagonal matrices, the absence of an overall scalar, and the uniqueness of the contributing residue class agree. The displayed gluing formula is correct, but the stated translate convention and the congruence proving its character phase are wrong.

<a name="glued-datum-in-the-schrodinger-model-finding-1"></a>

**Medium · Compare the sum of the phases directly with −c/N.** The proof says the phase argument is congruent at P to −(∑rᵢtᵢ−c/N). This latter expression is integral by the very definition of c, which would give phase 1 even for a nontrivial residue character. Lean proves that the sum of the two phase arguments differs from −c/N by the difference of two integral adeles. Write uᵢ=residueOverN_S(bᵢ), v_c=residueOverN_P(c), j=j_P. The difference from −v_c is ∑ᵢ j(tᵢ−uᵢ)j(rᵢ−ūᵢ) − j(∑ᵢ rᵢtᵢ−v_c), integral term by term. Thus the product is ψ(−v_c). [Knowl line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/glued-datum-in-the-schrodinger-model.knowl.md#L38) · [Columns.lean:493](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L493)

<a name="glued-datum-in-the-schrodinger-model-finding-2"></a>

**Medium · Reverse the general support sign for a Schrödinger translate.** The sentence about a translate by a identifies its support by X−a integral. The cited operator multiplies f(X+a) by the character factor. The negative pole vectors a=−b/N and a=−b̄/N then give precisely the later X−b/N and X−b̄/N tests. The two sentences presently disagree. Use X+a in the general translate and keep the subsequent negative pole substitutions. [Knowl line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/glued-datum-in-the-schrodinger-model.knowl.md#L38) · [SchwartzBruhat.lean:143](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/SchwartzBruhat.lean#L143)

<a name="page-grid-steps-correspond"></a>

### The parameters at the two ends of every step of a grid correspond

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/grid-steps-correspond.knowl.md) · [Parameters.lean:863](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean#L863)

The three step statements have the right orientations, including the sign flip only on the smaller space before using IsBlockRule.neg. The common introductory proof assertion misstates both its normalization and the grid-size hypotheses.

<a name="grid-steps-correspond-finding-1"></a>

**Medium · The cubic separation estimate needs bounds on both nodes.** The proof asserts Δ−t−2≥500(N+N′)³ after imposing only o+j≤m and o=0 or i=0. Fixing o=j=0 allows arbitrarily large i, hence arbitrarily large N. The source estimates the ranks only when i,j,i′,j′≤m, which each of the three step statements supplies. Separate the unconditional parameter-identification clause from the rank estimate with its four coordinate bounds. Invoke the latter individually for the endpoints in items 1–3. [Knowl line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/grid-steps-correspond.knowl.md#L25) · [Parameters.lean:853](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean#L853)

<a name="grid-steps-correspond-finding-2"></a>

**Medium · Use 2λ_B in the invocation of the centre system.** This proof identifies the explicitly doubled l^o_{i,j} with the half-integral λ_B introduced on the centre-system page. The same identification affects the description of the smaller node on line 31. The insertion theorem actually uses vectors listing 2λ_B. Identify l^o_{i,j} with 2λ_B, or say that l^o_{i,j}/2 is the half-integral centre parameter, throughout the argument. [Knowl line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/grid-steps-correspond.knowl.md#L25) · [InsertBlock.lean:96](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/InsertBlock.lean#L96)

<a name="page-highest-vector-polynomial-is-an-edge"></a>

### The polynomial of the highest vector is a product of joint harmonics, hence an edge

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/highest-vector-polynomial-is-an-edge.knowl.md) · [AuxiliaryPair.lean:984](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L984)

I checked the signs (r₋,−γ) for the local harmonic and (r₋,γ) for the global edge, as well as the real substitution, highest-vector embedding and the cited uniqueness and edge theorems. One hypothesis of the cited staircase theorem is missing from the outline.

<a name="highest-vector-polynomial-is-an-edge-finding-1"></a>

**Medium · The staircase theorem requires both parameter lists to be injective.** The proof’s list of conditions verifies injectivity only for l′. The cited theorem separately requires injectivity of l on W, which makes the numbering within each sign a bijection and is used to choose the first columns. The fitted block rule supplies it. State that l is injective by the left gap of the fitted block rule and l′ by the Harish-Chandra parameter identity (or the right gap), before applying the staircase theorem. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/highest-vector-polynomial-is-an-edge.knowl.md#L30) · [Lift.lean:150](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Lift.lean#L150)

<a name="page-jet-conjugation"></a>

### Jet conjugation: a semilinear map conjugating Taylor coefficients of theta functions

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/jet-conjugation.knowl.md) · [JetConjugatesAndBounds.lean:78](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean#L78)

The norm of the scale, the precise three translation conditions, and the inverse permutation on the coefficients agree. The introduction gives the formal jets an unconditional analytic interpretation.

<a name="jet-conjugation-finding-1"></a>

**Medium · Give the formal jet definition before identifying a Taylor series.** The page introduces all theta data on an arbitrary space V and identifies Jet_c(f) as the Taylor series of its theta function. The source defines formal coefficients using the integrated monomial operator. It identifies the ordinary Taylor series for finite-part f with all signs positive. Even the general constant term is θ(projReal f) (ThetaJets.lean:147). Define the α coefficient as c^|α| θ(V.integrated(v_α,f))/α! and state the Taylor-series interpretation under the finite-part and positive-sign assumptions. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/jet-conjugation.knowl.md#L14) · [ThetaJets.lean:90](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/ThetaJets.lean#L90)

<a name="page-lower-chain"></a>

### The chain of theta lifts along Y_0, ..., Y_m

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/lower-chain.knowl.md) · [RowChain.lean:178](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/RowChain.lean#L178)

The normalization of every step is the index of the source level in the standard level. The final identification uses the column numbers of Y and the determinant exponent at m, and the reversed arrow has both real types conjugated.

<a name="lower-chain-finding-1"></a>

**Medium · State the rapid-decay part of the two arrow conclusions.** The page describes an arrow only by preservation of the target type. In the source an arrow also asserts rapid decay of every form of its source type. This matters for the preceding identification of the abstract formLift with the ordinary theta integral: the general formLift uses linear projections, and the two arrows are proved here for j&lt;m. Specify 0≤j&lt;m for the ordinary lifts in the chain. Include rapid decay of the source-type forms on Yⱼ and of the conjugate source-type forms on Yⱼ₊₁ for the reverse arrow. [Knowl line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/lower-chain.knowl.md#L25) · [Lift.lean:773](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Lift.lean#L773)

<a name="page-lower-chain-level-and-equivariance"></a>

### Level, character and equivariance of the chain along the Y_j

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/lower-chain-level-and-equivariance.knowl.md) · [RowChain.lean:323](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/RowChain.lean#L323)

The one-step quotient of two tame-character values telescopes to the character on the last diagonal block. The initial block acts through the chosen group on principal-level forms, so the special lift diag(s,1) has scalar one.

<a name="lower-chain-level-and-equivariance-finding-1"></a>

**Medium · Justify the simultaneous unitary lift of the corner matrices.** The full proof says to lift k′ with reduction g₁₁. The corners are invertible residue matrices, and their independent lifts to one integral unitary element use the fact that the finite set of level places is pairwise distinct and contains no conjugate pair. The source invokes the chosen liftResidue and its reduction identity. Explain that the level places contain no conjugate pair, cite surjectivity of simultaneous reduction at such places, then choose k′ with the specified corner at each one. [Knowl line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/lower-chain-level-and-equivariance.knowl.md#L31) · [CongruenceLevels.lean:330](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/CongruenceLevels.lean#L330)

<a name="page-mirabolic-subgroup-at-split-level"></a>

### Mirabolic subgroup at a split level

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/mirabolic-subgroup-at-split-level.knowl.md) · [LiftLawsModuloN.lean:206](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L206)

The subgroup stabilizes the last column modulo N, and its D_N-conjugate stabilizes the last row. The two transformation formulas in the body give the correct actions on direct data and on the mirror function in the enlarged target coordinates.

<a name="mirabolic-subgroup-at-split-level-finding-1"></a>

**Medium · The unshifted mirror datum is not mirabolic-invariant.** The summary says the subgroup fixes the mirror datum. The proved invariant is T↦mirror(D_N⁻¹T). For rank two, a lower-unipotent target matrix fixes the last basis vector but its inverse changes T₂₂ by a multiple of T₁₂. On integral matrices this can change the corner character in the unshifted mirror datum. In the summary name the direct datum and the shifted mirror datum T↦mirror(D_N⁻¹T), as in property 3. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/mirabolic-subgroup-at-split-level.knowl.md#L5) · [LiftLawsModuloN.lean:481](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L481)

<a name="page-normalized-descent"></a>

### Fock polynomial, conjugate kernel and normalized descent of a descent pair

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/normalized-descent.knowl.md) · [AuxiliaryPair.lean:371](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L371)

The two coordinate conjugations make the kernel linear and the double-coset sum divides by the rational stabilizer order. The account of the letter substitution can misidentify its input index.

<a name="normalized-descent-finding-1"></a>

**Medium · Distinguish a tableau entry from its polynomial column index.** The text asks the reader to replace the “letter h of a filling,” leaving the row i of X_{τ,i,c} unexplained. The filling entries select rows i∈n. The independent array-column index h selects the columns c of the indicated sign and numbering. A height-one minor uses h=0 regardless of the letter in its box. Define P^η_a by taking the Weyl polynomial toPoly(a) in variables Y_{τ,i,h}, then substituting Y_{τ,i,h} ↦ ∑_{s(c)=η,ν(c)=h} X_{τ,i,c}. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/normalized-descent.knowl.md#L18) · [PAdicGauge.lean:376](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean#L376)

<a name="page-properties-of-grid-nodes"></a>

### Ranks, signs, gaps and interlacing of the grid nodes

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/properties-of-grid-nodes.knowl.md) · [Parameters.lean:776](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean#L776)

The sign counts, signed-set identifications, and doubled gaps match the source, as does the final interlacing inequality. The sign error is in the count increment used to prove that inequality.

<a name="properties-of-grid-nodes-finding-1"></a>

**Medium · Subtract the up-block count difference in the interlacing induction.** The induction controls D=count_tilde−count_Y. The down-block difference bounded in the text is down_tilde−down_Y, whereas the nonnegative up-block difference with the displayed bounds is up_Y−up_tilde. The instruction to add both reverses the up-block contribution. For x below every entry both block differences are 1 and the new base terms cancel, so the printed update would incorrectly increase D by 2. Put s=2λ^Y_{k−1+m′}, s′=2λ^Y_{k+m′}, and use D_new=D_old+D_down−D_up+φ(−s′−1)−φ(s). The endpoint inequalities then telescope as claimed. [Knowl line 46](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/properties-of-grid-nodes.knowl.md#L46) · [Parameters.lean:385](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean#L385)

<a name="page-source-form"></a>

### Source form

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/source-form.knowl.md) · [Columns.lean:760](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L760)

The stage-zero columns give one row of length a at each a-place, determinant exponent zero, and the stated last-row level. The description does not identify the coefficient representation precisely.

<a name="source-form-finding-1"></a>

**Medium · Specify the conjugate-matrix action in rational equivariance.** The defining law uses an undefined ρ(γ). The source uses the Weyl representation at the matrices Φτ(γ̄). Applying it at Φτ(γ) instead changes the defining character on rational scalar matrices of nonzero weight. The Poincaré-map page uses the correct convention explicitly. Define ρ(γ)=WeylRep(c,ℓ₀)((Φτ(γ̄))_τ) next to the equivariance equation. [Knowl line 16](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/source-form.knowl.md#L16) · [SchurNorm.lean:320](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/SchurNorm.lean#L320)

<a name="source-form-finding-2"></a>

**Low · Distinguish the rank of the group from the dimension of its coefficient module.** “The Weyl module … of rank k” reads as a dimension claim. Here k is the rank of the underlying hermitian space. At one a-place the coefficient module for (a,0,…,0) has a basis indexed by degree-a monomials in k variables, of dimension binomial(a+k−1,k−1). Call it the Weyl module for GL_k of the specified weight, reserving rank k for X₀. [Knowl line 16](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/source-form.knowl.md#L16) · [SchurMatrix.lean:908](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GLn/SchurModule/SchurMatrix.lean#L908)

<a name="page-spaces-y-and-w"></a>

### The hermitian spaces Y_j and W_j

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/spaces-y-and-w.knowl.md) · [Rows.lean:244](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean#L244)

I checked the antidiagonal form, its negative middle line for odd string length, and the integral right correction of the lattice basis at the chosen places. The presentation of Wⱼ leaves out its distinguished point.

<a name="spaces-y-and-w-finding-1"></a>

**Medium · Specify the point of the signed space Wⱼ.** The page defines a space as (J,x), then specifies only J=diag(sⱼ) for Wⱼ. That Gram matrix alone does not identify the chosen space: the identity point does not give the required finite Gram matrix 1 when a negative coordinate occurs. Give the signedSpace point: its archimedean component is 1, and its finite component is diagonal with entries 1 on positive coordinates and the chosen integral unit ε with ε̄ε=−1 on negative coordinates. [Knowl line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/spaces-y-and-w.knowl.md#L25) · [ComponentsAndBlockSums.lean:524](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/ComponentsAndBlockSums.lean#L524)

<a name="page-target-form"></a>

### Forms of principal level, good forms and target forms

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/target-form.knowl.md) · [Rows.lean:281](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean#L281)

The chosen finite group acts through reduction, the good forms are the range of the idempotent, and the target is that range on Y₀. The parenthesis describing the local level can admit an incorrect interpretation.

<a name="target-form-finding-1"></a>

**Medium · Forms are still spherical away from the chosen places.** The parenthesis “No condition at N or at a twist” can be read as allowing arbitrary ramification there. The level is a subgroup of K₀, and it contains every local maximal compact subgroup supported away from the chosen places and their conjugates. Invariance under those subgroups is required. Say that the level imposes no extra congruence at N or Q and that the forms are invariant under the full local maximal compact there. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/target-form.knowl.md#L18) · [PAdicGauge.lean:365](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean#L365)

<a name="page-vacuum-data-of-functions-modulo-an-ideal"></a>

### Data from functions modulo an ideal are standard data and vacuum combinations

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/vacuum-data-of-functions-modulo-an-ideal.knowl.md) · [ThetaLiftGauge.lean:464](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L464)

The three conclusions have the correct norm, rank and conjugate-size bounds, including the use of q=N₀=0 for the archimedean estimate. The quoted Fourier denominator in their proof loses a rank factor.

<a name="vacuum-data-of-functions-modulo-an-ideal-finding-1"></a>

**Medium · Use the rank of the matrix space in the Fourier denominator.** The quoted denominator is Norm((N₀))^|n| for a function Ψ already defined on n′ by n matrices. The Fourier lemma uses the cardinality of the full vector index set, here |n′|·|n|. The smaller denominator is not supplied by that lemma when |n′|&gt;1. Write Norm((N₀))^(|n′|·|n|) in this application, or state the Fourier input for an index set I and then put I=n′×n. Its absolute norm gives exactly the exponent in the displayed conclusion. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/vacuum-data-of-functions-modulo-an-ideal.knowl.md#L29) · [ThetaLiftGauge.lean:467](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L467)

<a name="page-bounds-for-the-vacuum-and-its-conjugates"></a>

### Uniform bounds for the values of the moved vacuum and of its Galois conjugates

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/bounds-for-the-vacuum-and-its-conjugates.knowl.md) · [JetConjugatesAndBounds.lean:386](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean#L386)

The trace makes squared distances between integral vectors positive integers, and the conjugate-vacuum estimate combines the multiplier of norm one with the bound for a moved vacuum.

<a name="bounds-for-the-vacuum-and-its-conjugates-finding-1"></a>

**Low · Keep the integral lattice as the summation index.** The rightmost sum suppresses the integrality condition and the following sentence calls the points γ_W separated. The introductory sum on line 30 ranges over Eⁿ. In positive rank the latter set contains e₁/j tending to zero, so an unrestricted exponential sum diverges and the packing bound cannot apply to it. Name the set of W-integral γ and retain it in both the last exponential sum and the application of the packing bound on line 34. [Knowl line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/bounds-for-the-vacuum-and-its-conjugates.knowl.md#L32) · [JetConjugatesAndBounds.lean:393](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean#L393)

<a name="page-chain-of-lifts"></a>

### Chain of theta lifts along a tower of definite unitary groups

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/chain-of-lifts.knowl.md) · [LiftChains.lean:67](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L67)

The class integral is taken with volume one for the subgroup at the source of each step. The chronological factors in one double lift are S₂ᵢ⊗S₂ᵢ₊₁, while the tensor for an entire chain lists its last factor first.

<a name="chain-of-lifts-finding-1"></a>

**Low · The class-points link resolves to a page without the definition.** The page claims the declaration classPoints but never introduces it. The upper-divisibility knowl on summing a chain refers to that declaration, so following the intended link here would not explain how representatives are used or what happens at the final coordinate. Add the definition that a tuple of classes supplies its chosen representative in slots j&lt;m, with the original tuple retained in slots j≥m, or assign the declaration to the plain-sum knowl where this is already stated. [Knowl line 10](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/chain-of-lifts.knowl.md#L10) · [LiftChains.lean:177](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L177)

<a name="page-data-modulo-n"></a>

### Direct, mirror and glued data modulo N

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/data-modulo-n.knowl.md) · [LiftLawsModuloN.lean:275](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L275)

The glued kernel on integral pairs is the character of the corner of RT. In the last-row conjugation the off-corner last row is multiplied by N and the off-corner last column by N⁻¹, as in the proof.

<a name="data-modulo-n-finding-1"></a>

**Low · Identify the mixed bases for the mirror datum.** The lattice interpretation switches from original bases to two enlarged bases for the direct datum and then presents the mirror formula without specifying its bases. The mirror uses the original source L and the enlarged target L′⁺. In original bases a matrix T must first be replaced by D_N⁻¹T before the corner-character formula is applied. State explicitly that the matrix for the mirror formula is written in bases of L and L′⁺, and that u′ takes values modulo N. [Knowl line 46](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/data-modulo-n.knowl.md#L46) · [LiftLawsModuloN.lean:269](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L269)

<a name="page-gauge-raising-data"></a>

### Data that raise the p-adic gauge by at most a factor

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/gauge-raising-data.knowl.md) · [ThetaLiftGauge.lean:73](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L73)

The source uses a right base-point shift on each side, max(c,0), and the stated bound under scalar multiplication. The diagonal-weight display leaves the place index of the box factors outside the visible product.

<a name="gauge-raising-data-finding-1"></a>

**Low · Put both diagonal factors inside the place product.** In the printed formula, the dot follows the closing determinant power and the box product still depends on τ. The binding of τ over this second factor is unclear for a field with several infinite places. Enclose both factors in the outer product: ∏τ \[(∏b |uτ,b|)^(e′τ) · ∏boxes of i′τ |uτ,entry|\]. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/gauge-raising-data.knowl.md#L21) · [ThetaLiftGauge.lean:120](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/ThetaLiftGauge.lean#L120)

<a name="page-index-sets-of-the-hermitian-spaces"></a>

### Index sets of the bases of X_j and Y_j

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/index-sets-of-the-hermitian-spaces.knowl.md) · [LabelsAndIndexTypes.lean:266](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L266)

The row count is two copies of m/2−1, the k indices of X₀ and the additional index z. Each subsequent disjoint summand contributes exactly t.

<a name="index-sets-of-the-hermitian-spaces-finding-1"></a>

**Low · The chosen bijection also assigns grid coordinates.** The remark says the arbitrary bijection for positive block length is used only for counting. The grid uses it twice to define gridBlockEquiv, and then reads each coordinate’s sign and doubled parameter through that bijection in gridSigns and gridParam. Remove “used only for counting” and say that the same arbitrary relabeling assigns base and block coordinates for the grid data. [Knowl line 37](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/index-sets-of-the-hermitian-spaces.knowl.md#L37) · [Parameters.lean:75](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean#L75)

<a name="page-poincare-map"></a>

### The Poincaré map from source forms to forms on Y_0

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/poincare-map.knowl.md) · [PoincareMap.lean:188](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/PoincareMap.lean#L188)

The Bessel integral, its conjugation in y, the Riesz convention and the finite-index trace formula all agree. The reference list and the definition of the unipotent subgroup need small repairs.

<a name="poincare-map-finding-1"></a>

**Low · Correct the namespaces of the trace and integrability references.** Four entries beginning New.Form.levelTrace or New.Form.hasLevel/integral_levelTrace are defined inside namespace New.Space, and New.IsEquivariant.integrable_mul is defined inside New.Grading. The names in the declaration metadata do not resolve to the proof's lemmas. Use New.Space.Form.levelTrace, New.Space.Form.levelTrace_apply, New.Space.Form.hasLevel_levelTrace, New.Space.Form.integral_levelTrace_mul, and New.Grading.IsEquivariant.integrable_mul. [Knowl line 10](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/poincare-map.knowl.md#L10) · [PoincareMap.lean:72](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/PoincareMap.lean#L72)

<a name="poincare-map-finding-2"></a>

**Low · Supply the missing lower bound in the name of the unipotent subgroup.** The printed decomposition R₀=U^{≥}⋊U(X₀) leaves the filtration degree blank. The group in the period-equivariance lemma consists of u with u−1 raising degrees by at least two. Write U^{≥2} and optionally spell out the degree-raising condition. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/poincare-map.knowl.md#L14) · [PoincareMap.lean:127](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/PoincareMap.lean#L127)

## Other knowls checked

<a name="page-block-datum-laws"></a>

### Laws of the block datum

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/block-datum-laws.knowl.md) · [AuxiliaryPair.lean:623](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L623)

The phase of the translate by a lift of A⁻¹ is ∏Q ψ(det A), and the transformation X ↦ k′⁻¹Xk contributes the Q-factors that cancel in the level law. I also checked the cited integral-point Weil action.

<a name="page-branching-exponent-formula"></a>

### The branching exponent

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/branching-exponent-formula.knowl.md) · [Weights.lean:617](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Weights.lean#L617)

Subtracting the block sums leaves aτ−mΔ/2 at each place. I also checked the separate column identity, including the last determinant entry, and the sum |Φₐ|a−fmΔ/2.

<a name="page-branching-map-and-restriction-to-y"></a>

### The integral branching map and the restriction of forms from X_m to Y_m

Source checked · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/branching-map-and-restriction-to-y.knowl.md) · [Columns.lean:675](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L675)

The matrix intertwines block scalars over every characteristic-zero field, has the stated bound on its squared Gram operator norm, and restricts a form at diag(h,1) with the factor ∏τ Φτ(π̄_N)^(−n_τ).

<a name="page-centre-system-parameter-has-gap"></a>

### Parameters of a separated centre system have a gap

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/centre-system-parameter-has-gap.knowl.md) · [InsertBlock.lean:225](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/InsertBlock.lean#L225)

Pairwise block separation gives the cardinality needed for injectivity. The parity shift from lowering and the omitted centre separating entries of opposite signs yield the required doubled distance of at least 2h.

<a name="page-chain-datum-and-composite-lift"></a>

### Chain datum and composite lift

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/chain-datum-and-composite-lift.knowl.md) · [Columns.lean:960](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L960)

The strong support and denominator conditions, the two size bounds, and the distinction between invariance of the glued and plain tensors agree. In the weak definition the integrality test omits all places over N. The simple poles in the remark arise in the displayed gluing construction.

<a name="page-chain-equivariance"></a>

### Equivariance of a chain of lifts

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/chain-equivariance.knowl.md) · [LiftChains.lean:78](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L78)

On a pure tensor, equivariance of the last lift cancels the translation coming from the inner chain. For the third identity the tuple equal to inverse z through j and 1 afterward acts only at factor j and has trivial final component because j&lt;m.

<a name="page-chain-of-glued-lifts-becomes-direct"></a>

### A chain of glued double lifts is a chain of direct lifts after a power of Up

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/chain-of-glued-lifts-becomes-direct.knowl.md) · [LiftLawsModuloN.lean:895](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L895)

At the (i+1)-st pair, the new scalar includes the two factors γ₂ᵢ and γ₂ᵢ₊₁ and all earlier γ from moving Up through the previous direct lifts. This gives the nested product through 2i+1 and one further power of Up on the source.

<a name="page-chains-kill-ramified-source-forms"></a>

### A chain with data fixed by a scaling above N annihilates ramified source forms

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/chains-kill-ramified-source-forms.knowl.md) · [CharactersAtLevel.lean:152](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/CharactersAtLevel.lean#L152)

The scalar law passes z through each lift. I verified the proposed cyclic-average primitive: for T^(N−1)=1 and ∑Tᵉφ=0, applying 1−T to −(N−1)⁻¹∑eTᵉφ gives φ. The double-step condition acts on factor 2i+1.

<a name="page-chosen-places-and-chosen-group-order"></a>

### Chosen places, the chosen level and the chosen group order

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/chosen-places-and-chosen-group-order.knowl.md) · [LiftChains.lean:422](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L422)

Each prime contributes f places of norm pᵢ, hence the norm product M^f. The GL rank bound uses diagonal-block inclusion, and the test for nontrivial character powers uses q₁d dividing q₂ together with |e|≤8m&lt;q₁d.

<a name="page-existence-of-jet-conjugation"></a>

### Existence and first properties of jet conjugations

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/existence-of-jet-conjugation.knowl.md) · [JetConjugatesAndBounds.lean:149](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean#L149)

On a standard space the proof constructs the semilinear map using a left inverse to the injective, renamed jet map on the finite part. A separate rank-one generator establishes the additive-character law, after which span induction gives translation compatibility on the full finite part.

<a name="page-free-levels-at-the-chosen-places"></a>

### Levels that are principal at the chosen places are free

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/free-levels-at-the-chosen-places.knowl.md) · [LiftChains.lean:518](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L518)

The cited freeness lemma requires distinct places and a strict norm-product inequality. Its application at a single level prime allows rank 4nₘ, and for rank 2nₘ the reduction of the conjugated stabilizer injects into the residue groups because the reduction kernel has trivial stabilizer.

<a name="page-glued-double-lift"></a>

### A glued double lift is two direct lifts after Up

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/glued-double-lift.knowl.md) · [LiftLawsModuloN.lean:808](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L808)

Nonprimitive columns vanish at one residue place. Every primitive column is in the orbit of the last basis vector, and lifting the same matrix into both middle representations cancels it, leaving one contribution per primitive vector and scalar cγ′γ.

<a name="page-good-idempotent"></a>

### The group of the chosen places and the good idempotent e_0

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/good-idempotent.knowl.md) · [LabelsAndIndexTypes.lean:376](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L376)

The primitivity condition is imposed separately above each of the two primes. In the finite product group algebra, distinct tuples have orthogonal idempotents and their class-function coefficients give a central projection when summed.

<a name="page-good-idempotent-kills-hyperplane-sums"></a>

### The good idempotent kills hyperplane sums

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/good-idempotent-kills-hyperplane-sums.knowl.md) · [LabelsAndIndexTypes.lean:409](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L409)

The cited Green-character lemma tests the name of the character against the roots of the label, uses the nonzero vector, and kills the label idempotent on the right. The allowed-label condition excludes that name since the name map preserves the q₂-th power.

<a name="page-good-tuple-of-labels"></a>

### Allowed polynomial and good tuple of labels

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/good-tuple-of-labels.knowl.md) · [LabelsAndIndexTypes.lean:143](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L143)

The forbidden M-th roots are tested in each base field. Every component must be allowed, and the existential primitive component makes the good set empty for an empty family.

<a name="page-grid-nodes"></a>

### Index sets, signs and parameters of the nodes of the two grids

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/grid-nodes.knowl.md) · [Parameters.lean:97](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Parameters.lean#L97)

The base sign at offset o uses truncated subtraction. For z=1 the nonnegated computational vector lists the shifted base and blocks of lengths t+1 and t−1. The physical tilde parameter at offset zero has the opposite sign.

<a name="page-inserting-a-block-satisfies-the-block-rule"></a>

### Inserting a block into a parameter satisfies the block rule

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/inserting-a-block-satisfies-the-block-rule.knowl.md) · [InsertBlock.lean:292](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/InsertBlock.lean#L292)

Undoing the two lowerings produces the centred block and preserves common entries. For a down centre the changed signs are below the centre and use floor(N/2). The up case negates both parameters and uses ceil(N/2).

<a name="page-jointly-invariant-chain-is-a-plain-sum"></a>

### At free levels a jointly invariant combination of chains is a plain sum

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/jointly-invariant-chain-is-a-plain-sum.knowl.md) · [LiftChains.lean:225](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L225)

The tuple supported in slot j makes the combined last integrand right Kⱼ-invariant. The class sum then has denominator one, and absorbing the last jet into each coefficient map preserves joint invariance, which permits the shorter induction and the one-term-per-tuple membership corollary.

<a name="page-jointly-invariant-combination"></a>

### Jointly invariant combination of chain data

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/jointly-invariant-combination.knowl.md) · [LiftChains.lean:170](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean#L170)

The level tuple acts jointly on neighboring factors, is the identity starting at m, and the same arbitrary linear test map is applied to every summand. Linear tests separate the stated finite coefficient tensor.

<a name="page-level-places-of-the-data"></a>

### The places dividing pi_N and the levels of the stages X_j

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/level-places-of-the-data.knowl.md) · [Columns.lean:635](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L635)

The chosen places over N are split and disjoint from the other level places. The intersection defining K_X includes the last-row congruence (g−1)_{\*,i}∈π_N Ô at every stage.

<a name="page-lift-hecke-polynomial"></a>

### Hecke polynomial of a lift

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/lift-hecke-polynomial.knowl.md) · [AuxiliaryPair.lean:419](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L419)

The q-binomial coefficients of the operator, both Frobenius ranks, the argument qᵗνT/ν′ and the final q-Pochhammer factor’s reciprocal root agree. The inclusion into the right regular representation intertwines the operators.

<a name="page-lift-kernels-of-the-chain"></a>

### The theta kernels of the chain X_0 to X_m and the restricted chain

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/lift-kernels-of-the-chain.knowl.md) · [Columns.lean:849](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L849)

The dual-pair characters and the increment of the determinant exponent agree in each direction. The special jet scale uses the conjugate of the designated generator, and the translated vacua use the normalised finite Heisenberg operator.

<a name="page-lift-law"></a>

### Lift law modulo N

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/lift-law.knowl.md) · [LiftLawsModuloN.lean:296](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L296)

Integral equivariance uses b on the target, a on the source and bTa in the datum. Its scalar specialization takes b=x and a=x⁻¹, and the separate change-of-lattice equation multiplies the direct lift on the source side by γ.

<a name="page-lift-law-vanishing-on-ramified-vectors"></a>

### Lifts by scalar-invariant data kill ramified vectors

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/lift-law-vanishing-on-ramified-vectors.knowl.md) · [LiftLawsModuloN.lean:623](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L623)

At a fixed place a ramified vector is a difference under a unit scalar, so a scalar-invariant fibre contributes zero. A nonunit corner has a zero component in the product of residue fields, exactly the condition needed to discard it.

<a name="page-mirror-lift-through-direct-lift"></a>

### A mirror lift is Up after a direct lift

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/mirror-lift-through-direct-lift.knowl.md) · [LiftLawsModuloN.lean:714](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L714)

Sorting the restricted mirror kernel by last column produces Up on the target. Sorting by last row and applying the lattice-change equation instead produces γ times the direct lift of Up on the source, with the same D_N on the left.

<a name="page-normalized-descent-is-a-transposed-lift"></a>

### The normalized descent is a multiple of the conjugate transposed lift

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/normalized-descent-is-a-transposed-lift.knowl.md) · [AuxiliaryPair.lean:1048](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L1048)

The comparison multiplies the conjugated swapped lift by d\[K₀:K_O\], with the inner scalar form also conjugated. I checked the rational/level equivariance, archimedean integration identity, stabilizer weights and the three residue-index assertions.

<a name="page-point-datum-on-y"></a>

### Levels, theta kernels and point data along the spaces Y_j

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/point-datum-on-y.knowl.md) · [Rows.lean:399](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean#L399)

The inclusion condition gives k′⁻¹ιk=ι modulo MQ, and the pair character on these integral points is the stated ratio of tame determinants. The target-parameter entries and the t-block entries occupy the claimed positions in the sorted list.

<a name="page-primitive-polynomial"></a>

### Primitive polynomial (primitive label)

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/primitive-polynomial.knowl.md) · [LabelsAndIndexTypes.lean:54](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L54)

Monicity, squarefreeness, degree, and nonzero constant term are the four label conditions. The extra requirements of irreducibility and a root of order q^r−1 are both present, and this forces r≥1.

<a name="page-primitive-polynomial-scaling-and-norm"></a>

### Primitive polynomials: scaling of roots, and the product of the roots

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/primitive-polynomial-scaling-and-norm.knowl.md) · [LabelsAndIndexTypes.lean:70](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean#L70)

With o the order of the scaling unit and n=q^r−1, o² divides n, so n divides eo only when n/o divides e, forcing o to divide e. The geometric sum applied to a primitive root has exact order q−1 and yields the same product from every Frobenius conjugate.

<a name="page-principal-forms-are-finite-dimensional"></a>

### The target parameter has gap Delta, and the forms of principal level are finite-dimensional

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/principal-forms-are-finite-dimensional.knowl.md) · [Rows.lean:497](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Rows.lean#L497)

Opposite Wⱼ signs straddle the cutoff k+j−1 and give at least 2Δ between doubled entries. The source then uses 500r³≤Δ/2 and applies finite_levelSpace to the open principal level with trivial character.

<a name="page-ramified-vector-at-split-level"></a>

### Ramified vector at a split level

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/ramified-vector-at-split-level.knowl.md) · [LiftLawsModuloN.lean:222](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L222)

For each place separately the witness scalar is only required to reduce to one away from that place, and both the scalar and its preimage vector may vary with the place. Intertwining these scalars sends a difference witness to its image.

<a name="page-split-level"></a>

### Split level at a prime N

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/split-level.knowl.md) · [LiftLawsModuloN.lean:50](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L50)

All four conditions on the places occur, including that the listed places and their conjugates exhaust those above N. The residue character uses the negative of the finite adele with components ỹ/N, and the page consistently reserves D_N for the inverse diagonal.

<a name="page-up-operator"></a>

### The operator Up at a split level

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/up-operator.knowl.md) · [LiftLawsModuloN.lean:200](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L200)

The last entry must be a unit at every component. The displayed two-matrix construction realizes both the row and column condition, and conjugating a mirabolic element by D_N changes summands by a permutation preserving the last entry and its character weight.

<a name="page-weights-of-the-definite-spaces"></a>

### Parameters, weights and lift diagrams of X_j and Y_m

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-objects/weights-of-the-definite-spaces.knowl.md) · [Weights.lean:146](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Weights.lean#L146)

For the actual weight indices, the X and Y block sequences, determinant-row shift, column multiplicities and last-entry normalization agree. Their parities make division of the doubled entries by two exact.
