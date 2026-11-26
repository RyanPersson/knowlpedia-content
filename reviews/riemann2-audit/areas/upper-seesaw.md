# upper-seesaw

This area contains 51 individual knowls and a chapter page. The review records 48 comments. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports/upper-seesaw.md)

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Chapter page

<a name="page-upper-seesaw"></a>

### Upper bound: the seesaw identity

Correction recorded · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw.knowl.md) · [SeesawIdentity.lean:624](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L624)

The main identity correctly places the nonzero scalar before the twist quantifier and allows the datum to depend on the twist. The proof clears denominators to obtain the advertised M^(3fmn_m²) trivial-modulus size, including when both lifts vanish.

<a name="upper-seesaw-finding-1"></a>

**High · The string description stops one stage before the top.** The grading Y_j=X_j plus a string holds for j&lt;m. At j=m the separate last grading has n_m−1 grade-zero coordinates and an empty string. Y_m lies inside X_m with codimension one, reversing the inclusion in the notation paragraph. An even-length string at earlier stages also has no middle vector of norm −N. Restrict the description to j&lt;m and mention the middle norm only when the string length is odd. Give the separate codimension-one description of Y_m used for restriction. [Knowl line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw.knowl.md#L35) · [EdgePairEvaluation.lean:1144](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L1144)

<a name="upper-seesaw-finding-2"></a>

**Medium · The summary extends the coefficient bounds to all twists.** The displayed summary promises integral, bounded data. For a general twist the coefficients are integral only away from the modulus, and the archimedean size bound applies when the modulus is empty. The theorem in the body at lines 24–26 makes both qualifications correctly. Qualify the two properties in the summary as integrality away from the modulus and bounded size for the trivial modulus. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw.knowl.md#L5) · [SeesawIdentity.lean:624](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L624)

<a name="upper-seesaw-finding-3"></a>

**Medium · A tame character carries a chosen supporting modulus.** For the tame characters used in the intermediate cut and integral statements, the tame part must be trivial outside Q but may also be trivial at some places of Q. The quotient level, integrality away from q and multiplicity bounds in the cuts use this supplied Q. The final theorem really does use a Twist, which adds nontriviality at every place of Q. Say that Q is the chosen finite set supporting the tame part for a tame character and that it is the exact support for a twist. Use its full norm in the intermediate statements. [Knowl line 39](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw.knowl.md#L39) · [LevelAndTwists.lean:260](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L260)

<a name="upper-seesaw-finding-4"></a>

**Low · The seven outline labels include a construction.** The totals 42 proof labels, 35 full and seven outline are correct. By the actual item kinds there are 39 lemmas, propositions or theorems, of which 33 are full and six are outlines. The extra three proof-bearing items are the definition of cover multiplicity and the constructions of the finite zero term and the seesaw datum. Write “of the 42 items with proof-status labels, 35 are full and seven are outlines”. [Knowl line 152](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw.knowl.md#L152) · [EdgePairEvaluation.lean:93](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L93)

## Knowls with comments

<a name="page-iterated-unfolding"></a>

### Iterated unfolding of the lower chain applied to a Poincaré series

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/iterated-unfolding.knowl.md) · [SeesawIdentity.lean:413](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L413)

The normalization and the order in which the induction chooses a′ and c agree, including the dependence on the outer archimedean tuple. The written string length loses the last stage of that induction.

<a name="iterated-unfolding-finding-1"></a>

**High · The top stage has zero string vectors.** Part 4 permits k=m−1 but assigns the string length m−2−k, which is −1 at that endpoint with ordinary subtraction. The Lean expression is natural-number subtraction and equals zero there. The subsequent proof of the full lower chain invokes exactly this endpoint with the last grading. Use max(0,m−2−k), or give m−2−k for k≤m−2 and zero for k=m−1. Explicitly identify the empty-string case with the last grading. [Knowl line 45](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/iterated-unfolding.knowl.md#L45) · [SeesawIdentity.lean:417](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L417)

<a name="iterated-unfolding-finding-2"></a>

**Medium · Supply a graded point in the Bessel orbit.** The support theorem bounds every translate whose lattice is graded. To conclude that the orbit is bounded one needs a translate with graded lattice. The source uses the existence theorem for graded translates, invoking the primitive 5040th root of unity in the field of the data. Invoke part 3 of lattice-bounds-induction-step to obtain a graded representative, then apply the support bound to that representative before using the cut multiplicity theorem. [Knowl line 123](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/iterated-unfolding.knowl.md#L123) · [Sandwich.lean:238](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Sandwich.lean#L238)

<a name="page-neighbour-lattice-representatives"></a>

### Representatives of the neighbour lattice modulo its integral points

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/neighbour-lattice-representatives.knowl.md) · [NeighbourLattice.lean:996](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourLattice.lean#L996)

The local plus sign selects the unique pole-cancelling residue. Applying that result to −z gives the minus sign for the global representative, while the away part selects its quotient class.

<a name="neighbour-lattice-representatives-finding-1"></a>

**High · The quotient modulo β can be infinite.** The scaling hypotheses only make β a unit above N. For a place v away from N, take β to be zero at v and one elsewhere, with δ=1 and all κ_i=1. This satisfies the hypotheses and the residue ring has a quotient O_v, which is infinite. The claimed finite target for Lagrange’s theorem and the ordinary finite count in part 2 do not follow. Lean uses Nat.card of the target, equal to zero when it is infinite. State the finite-or-zero counting convention for the matrix space. If the target is infinite the finite away-quotient order divides 0. For a finite target apply the kernel argument in the text. A positive numerical bound requires finite index of (β), as holds for the specific level used later. [Knowl line 56](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/neighbour-lattice-representatives.knowl.md#L56) · [NeighbourLattice.lean:838](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourLattice.lean#L838)

<a name="page-support-of-unfolding-stages"></a>

### Support of the unfolding functions for ramified source forms

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/support-of-unfolding-stages.knowl.md) · [UnfoldingStages.lean:1104](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean#L1104)

The nonzero predecessor integral gives a graded Bessel representative with the preceding bounds, including the base case from y₀. The frequency factor is b̄/α=q̄/a, and the split branch forces the even-stage vanishing after left translation by (1,r′)⁻¹.

<a name="support-of-unfolding-stages-finding-1"></a>

**High · The lattice bounds use the chosen modulus, which can exceed the ramification support.** The theorem defines Q as the places where the tame character ramifies. Lean uses the field ϑ.Q: it only requires the tame part to be trivial outside Q. For a trivial tame part with one permitted auxiliary place in Q, the source’s twist idele is a uniformizer there. Taking actual ramification instead makes it a unit and incorrectly tightens both lattice bounds at that place. Let Q be the designated modulus set of the TameChar throughout the statement and induction. Write the bounds with the idele of this Q, and reserve identification with the support of the tame part for twists with the extra nontriviality assumption. [Knowl line 16](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/support-of-unfolding-stages.knowl.md#L16) · [LevelAndTwists.lean:269](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L269)

<a name="page-unfolding-stages"></a>

### The functions of the unfolding

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/unfolding-stages.knowl.md) · [UnfoldingStages.lean:610](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean#L610)

The recurrence moves the datum by (g_k,1), integrates on the previous rational Bessel quotient, then uses the right translate by g_{k+1} to define the next restricted function. The two sides of the pairing identity use different quotients as in the source.

<a name="unfolding-stages-finding-1"></a>

**High · Restrict unipotent covariance to degree at least two.** The all-stage property gives no qualification on transformation by the unipotent character. The source imposes W(ur)=ψ_U(u)W(r) only when u−1 raises grades by at least two. At stages with positive even string length there can be degree-one directions. The proof establishes no such scalar transformation law for them. Define U^{≥2} by the degree condition on u−1 and state the transformation law on this subgroup. It coincides with the whole unipotent radical when the string length is odd. [Knowl line 45](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/unfolding-stages.knowl.md#L45) · [Equivariant.lean:282](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Equivariant.lean#L282)

<a name="unfolding-stages-finding-2"></a>

**Medium · Quotient by the rational points over the fixed field.** The display uses R_{k+1}(E) for the divisor in the quotient, with E the CM field. The rational unitary subgroup is defined over its totally real fixed field F and consists of the E-rational matrices satisfying unitarity, inside the adelic group. After base change to E, the algebraic group’s E-points are a different group. Lean takes the intersection of the rational unitary group with the adelic Bessel subgroup. Write R_{k+1}(F)\G_{k+1}, F=E⁺, or define Γ_{R_{k+1}}=Γ_{Y_{k+1}}∩R_{k+1} and use that subgroup in both places in the formula. [Knowl line 49](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/unfolding-stages.knowl.md#L49) · [Grading.lean:184](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L184)

<a name="unfolding-stages-finding-3"></a>

**Low · Separate the terminal global function from the restricted recurrence.** The recursive bullet defines W^R_{k+1} without a bound on k. The restricted functions are defined only through k+1≤m−1. The unrestricted W_m still exists from the last unfolding with a chosen length-zero grading of Y_m. Give the index ranges explicitly: W^R_k for 0≤k≤m−1 and W_{k+1} for 0≤k≤m−1. At the last unrestricted step use the last grading of Y_m. [Knowl line 40](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/unfolding-stages.knowl.md#L40) · [UnfoldingStages.lean:629](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean#L629)

<a name="page-admissible-combination"></a>

### Admissible combination

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/admissible-combination.knowl.md) · [AdmissibleCombinations.lean:501](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L501)

The core quantifies correctly over every coefficient and every complex field automorphism, with the sum bound conditional on p. The remark merges the parameters of different applications.

<a name="admissible-combination-finding-1"></a>

**Medium · The example conflates the modulus, fixed denominator and empty-modulus condition.** For the displayed seesaw application the exceptional integer is q = ∏_{w∈Q} Nw, where Q is the chosen modulus of the tame character. The residue-matrix factor appears in d, and the source bounds the size when Q is empty. TameChar permits trivial local factors even on Q, so neither a minimal conductor nor the identity of the underlying character specifies this datum. State the example with n=q, d=𝒞^(2m) for the unrescaled seesaw datum, and p=(Q=∅). If describing the final chain coefficients with d=1, mention the rescaling in SeesawIdentity.lean:636. [Knowl line 37](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/admissible-combination.knowl.md#L37) · [SeesawIdentity.lean:592](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L592)

<a name="page-admissible-evaluation-of-edge-pairs"></a>

### The finite evaluation of a pair of edges is an admissible evaluation

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs.knowl.md) · [AdmissibleEvaluation.lean:596](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean#L596)

The integral lift kills the stacked shift under its adjoint, and the supported isotropic correction vanishes on vectors away from N. I also checked the split-level input to the residue representatives and the c times away-index normalization.

<a name="admissible-evaluation-of-edge-pairs-finding-1"></a>

**Medium · The stated description of split level omits residue degree one.** The partition of the places over N into P and its conjugate, even together with the split squarefree factorisation, does not imply that each residue field is ℤ/N. In residue degree f&gt;1 the N elements of ℤ/N cannot parametrize the Nᶠ classes of simple poles at a selected place. The representatives used in part 2 require the stronger IsSplitLevel assumption. Explicitly require N to split completely, with P choosing one place of each conjugate pair, or spell out the residue-cardinality condition |k(w)|=N and that N is a uniformiser at each w∈P. [Knowl line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs.knowl.md#L17) · [LiftLawsModuloN.lean:54](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L54)

<a name="admissible-evaluation-of-edge-pairs-finding-2"></a>

**Low · The scalar multiplying the zero-term constant is undefined.** K first appears in C=cK. The finite index it represents determines the normalization of the admissible combination and is only identifiable by following a later reference. Define K as the cardinality of the away quotient for X′⊔{e′} before setting C=cK. [Knowl line 115](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs.knowl.md#L115) · [AdmissibleEvaluation.lean:616](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean#L616)

<a name="admissible-evaluation-of-edge-pairs-finding-3"></a>

**Low · The dependency's proof-status description is stale.** The remark calls zero-term-lattice an outline, but zero-term-lattice.knowl.md:12 labels it full in this snapshot. The separate block identity is the stated limitation on the present page. Update the dependency description to its current full status, or remove the status reference. Retain the identified limitation in the proof of the block identity. [Knowl line 137](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs.knowl.md#L137) · [EdgePairEvaluation.lean:554](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L554)

<a name="page-double-lift-data"></a>

### Double lift data and the finite evaluation of a pair of edges

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/double-lift-data.knowl.md) · [EdgePairEvaluation.lean:785](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L785)

The middle plane has basis (z−z′)/(2N), z+z′. In the last case z/p has norm one, no plane is removed, and the inclusion of the extra line fixes that vector.

<a name="double-lift-data-finding-1"></a>

**Medium · Give the scaled finite translation vector.** The construction calls the input to the Heisenberg operator the finite part of the stacked map and links “its coordinates” back to this same page. The actual vector is α⁻¹ times the finite part after expressing (T\*,T′) in the Hom-space frame. A reader taking the unscaled finite part obtains a different evaluation in general. Define S=(T\*,T′) and write the translation explicitly as ρ_f(α⁻¹(homAtPoint(S))_f), explaining that homAtPoint takes coordinates in the Hom-space frame and α is the finite scaling idele of the Weil data. [Knowl line 63](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/double-lift-data.knowl.md#L63) · [EdgePairEvaluation.lean:756](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L756)

<a name="page-double-unfolding-integral"></a>

### Two unfolding steps: Bessel integrals of constant terms as a double theta integral

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/double-unfolding-integral.knowl.md) · [UnfoldingStages.lean:457](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean#L457)

The product of constant terms contributes z₀⁻¹, and the two quotient-measure reductions give κ and κ′. I checked the opposite signs in −TT\*+T′\*T′, the order of the two integrations, and that the resulting constant is uniform in both characters.

<a name="double-unfolding-integral-finding-1"></a>

**Medium · Specify the rank twists and adelic coefficients in the definite-lift identity.** The complement speaks of lifts for a_o and b_o and writes t(φ(x)), although its integration variables are adelic and an algebraic form is defined on finite points. The source assumes the rank-dependent characters rankTwist(a_o) and rankTwist(b_o) in the two lift identities and uses the coefficient t(ρ_X(x∞⁻¹)φ(x_f)), likewise at g on the right. Dropping either normalization changes the displayed integral. State that the two lift families use a_o υ^{⌊r/2⌋} and b_o υ^{⌊r/2⌋} at rank r. Define t(φ(x)) as the full adelic coefficient with the inverse archimedean action, and use the same convention for t″. [Knowl line 41](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/double-unfolding-integral.knowl.md#L41) · [UnfoldingStages.lean:134](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean#L134)

<a name="double-unfolding-integral-finding-2"></a>

**Low · Extend the pure finite tensor calculation by linearity.** Even when the real polynomial separates as P Q, the arbitrary finite tensor y in the complement need not be decomposable. The sentence that the datum is then a join of two pure tensors skips this distinction. Lean first handles y=Φ⊗Φ′ and then addition of finite tensors. Make the factorization for a pure finite tensor, absorbing the joining constant into the second real polynomial, and extend to arbitrary y by linearity. [Knowl line 82](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/double-unfolding-integral.knowl.md#L82) · [UnfoldingStages.lean:218](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean#L218)

<a name="page-evaluated-data-admissible"></a>

### The evaluated data are admissible combinations of glued vacua

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/evaluated-data-admissible.knowl.md) · [GoodDatum.lean:535](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/GoodDatum.lean#L535)

The constant for each pair is uniform in the character and all translates. The product of the vacuum normalizations yields the global constant, and the factor (𝒞⁴)^(ϱ+1) is indeed 𝒞^(2m).

<a name="evaluated-data-admissible-finding-1"></a>

**Medium · Excluding the π_N places does not prove rational coprimality.** A prime of Q over N could lie over conj(π_N). Its norm would still be divisible by N, so excluding only the places dividing π_N does not justify applying admissible evaluation with q. Lean uses the defining TameChar condition gcd(MN,∏_{w∈Q} Nw)=1. Deduce gcd(N,q)=1 directly from the tame-character coprimality hypothesis. [Knowl line 58](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/evaluated-data-admissible.knowl.md#L58) · [GoodDatum.lean:512](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/GoodDatum.lean#L512)

<a name="evaluated-data-admissible-finding-2"></a>

**Medium · The third matrix shape has up to twice the stated number of entries.** The proof says each of the three exponents is at most n_m² before saying the third may use two such bounds. Its actual exponent is (n_{2i}+n_{2i+2})n_{2i+1}, for which the source uses 2n_m². For the last pair this exponent is 2n_{m−1}² by the rank progression. Write the three bounds as n_m², n_m² and 2n_m². Their sum is at most 4n_m², which gives divisibility by 𝒞⁴. [Knowl line 60](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/evaluated-data-admissible.knowl.md#L60) · [GoodDatum.lean:433](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/GoodDatum.lean#L433)

<a name="evaluated-data-admissible-finding-3"></a>

**Low · The summary identifies the modulus norm with the conductor norm.** The formula in the body uses q=∏_{w∈Q} Nw and imposes its size bound for Q=∅. A TameChar carries an assigned Q that can include trivial tame factors, so its q need not be the character's conductor norm. Use ‘norm of the supplied modulus’ and ‘when this modulus is empty’ in the summary. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/evaluated-data-admissible.knowl.md#L5) · [LevelAndTwists.lean:277](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L277)

<a name="page-graded-lattice-basis"></a>

### The glued lattice basis of a graded space

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/graded-lattice-basis.knowl.md) · [AdmissibleCombinations.lean:78](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L78)

The odd glue column and the two diagonal factors on an even string agree entry by entry. The definition of the auxiliary Gram form and the self-duality remark need qualifications.

<a name="graded-lattice-basis-finding-1"></a>

**Medium · The odd glued Gram matrix leaves mixed entries unspecified.** The list specifies the pairing of y with the middle z_c and all pairings within the string, but leaves the values of ⟨y,z_b⟩ and ⟨z_b,y⟩ for b≠c open when s is odd. These entries are zero in the mixed block of gluedGram. Set both mixed pairings to zero for each b≠c, or end the list by setting all unspecified matrix entries to zero. [Knowl line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/graded-lattice-basis.knowl.md#L38) · [AdmissibleCombinations.lean:174](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L174)

<a name="graded-lattice-basis-finding-2"></a>

**Medium · Odd string length alone does not prevent self-duality.** The standard Gram matrix for s=1 and N=1 is diag(I,−1), which is already unimodular. For odd s the obstruction over the integral lattice is that N is a nonunit, since every other block is already unimodular. State that the unglued standard lattice fails to be self-dual at places where N is a nonunit. Specify that this occurs at the places over the level prime in the application. [Knowl line 58](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/graded-lattice-basis.knowl.md#L58) · [Grading.lean:85](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Grading.lean#L85)

<a name="page-integral-as-sum-over-cut"></a>

### An integral over the Bessel quotient as a weighted sum over a cut

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/integral-as-sum-over-cut.knowl.md) · [IntegralAsCosetSum.lean:367](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean#L367)

The cutoff, the normalization giving mass one to the finite Bessel subgroup inside A, and the cancellation of \[K:J\] agree. The construction of the uniform scalar needs the convention for a nonintegrable archimedean factor.

<a name="integral-as-sum-over-cut-finding-1"></a>

**Medium · Define the scalar for an arbitrary archimedean function.** The theorem allows every function a without a measurability or integrability hypothesis. The displayed ordinary integral of aα can therefore be undefined, even for a zero integrand f in the theorem. Lean takes the totalized Bochner integral of a against the measure with density α, including the nonintegrable case. Define κ using the weighted integral of a when a is integrable for that measure, and set κ=0 otherwise. State the totalized product-integral convention used in the factorization, or give its integrable and nonintegrable cases explicitly. [Knowl line 49](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/integral-as-sum-over-cut.knowl.md#L49) · [IntegralAsCosetSum.lean:391](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean#L391)

<a name="page-lifting-conditions-for-the-two-pairs"></a>

### The lifting and denominator conditions for the middle and the last double lift

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/lifting-conditions-for-the-two-pairs.knowl.md) · [AdmissibleEvaluation.lean:657](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean#L657)

Both lattice tests and the cancellation using η·conj(η)=−1 in the last pair work. The last case omits the generic-character compatibility that the construction of the double lift requires.

<a name="lifting-conditions-for-the-two-pairs-finding-1"></a>

**Medium · Lengths 1, 0, 0 do not by themselves define the last double lift.** HasConsecutiveStrings also requires that the generic constants of Y and Y′ agree. The last case only lists the lengths, and genericConst is a freely specified nonzero conjugation-invariant element in each grading. The last-double-lift construction requires this compatibility even though the subsequent coordinate calculation only uses the lengths. Add c_Y=c_Y′ as a common hypothesis of both cases and link the definition of consecutive strings. In particular make it explicit in the last case. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/lifting-conditions-for-the-two-pairs.knowl.md#L26) · [EdgePairEvaluation.lean:770](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L770)

<a name="page-lower-chain-of-poincare-series"></a>

### The lower chain of a Poincaré series is a restricted upper chain

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/lower-chain-of-poincare-series.knowl.md) · [SeesawIdentity.lean:540](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L540)

The top coefficient l_ξ and the resulting outer scalar are chosen before the twist or either test form. Linearity of the cut sum then identifies every Petersson pairing with the pairing of the seesaw datum.

<a name="lower-chain-of-poincare-series-finding-1"></a>

**Medium · Use Petersson nondegeneracy to separate the forms.** The text calls the space of all test forms on Y_m finite-dimensional. FormY fixes the archimedean type and allows varying finite level. The available finite-dimensionality theorem requires a fixed level. Lean uses nondegeneracy of the inner product for the whole form space. Let v be the difference of the two forms, set x=v in the equality of pairings, and conclude from ⟨v,v⟩=0. [Knowl line 61](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/lower-chain-of-poincare-series.knowl.md#L61) · [SeesawIdentity.lean:569](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L569)

<a name="page-neighbour-lattice"></a>

### The neighbour lattice of a pair of edges

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/neighbour-lattice.knowl.md) · [NeighbourLattice.lean:581](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourLattice.lean#L581)

Checked the order γ diag κ in the lattice action, both exceptional column coefficients, and their congruences with −\[j+(1−j)π⁻¹\]. The translation itself requires a specified lift of each residue.

<a name="neighbour-lattice-finding-1"></a>

**Medium · Qualify the identification with the zero-term lattice.** The remark identifies the constructed lattice with the zero-term lattice of a pair of edges without specifying hypotheses on the pair. The source requires a split prime, a middle grading spanning the prescribed lattice, and an integral lift for each neighbour vector. These hypotheses enter the proof of lattice containment. State the identification for pairs satisfying the spanning and neighbour-lifting conditions at the split level. Link to part 1 of the admissible-evaluation-of-edge-pairs knowl, which states the identification. [Knowl line 79](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/neighbour-lattice.knowl.md#L79) · [AdmissibleEvaluation.lean:350](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleEvaluation.lean#L350)

<a name="neighbour-lattice-finding-2"></a>

**Low · Specify the representatives used in y/N.** A component y_w belongs to ℤ/N, so division by N alone determines a class modulo integral elements. The page defines an actual adelic vector n(y). Changing an integer lift of y_w by N changes its component in y/N by 1. Use the integer representative in {0,…,N−1} in each component before dividing by N, as in the definition of residueOverN. [Knowl line 51](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/neighbour-lattice.knowl.md#L51) · [LiftLawsModuloN.lean:62](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftLawsModuloN.lean#L62)

<a name="page-neighbour-vacuum"></a>

### The vacuum of the neighbour lattice as a combination of glued translates

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/neighbour-vacuum.knowl.md) · [NeighbourVacuum.lean:318](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourVacuum.lean#L318)

The gluing gives the pole column −y/N and pole row −ȳ/N because ηη̄=−1. The class phases are roots of unity and K nonzero coefficients of norm 1/K sum to one under every embedding.

<a name="neighbour-vacuum-finding-1"></a>

**Medium · Distinguish the explicit sum from a sum over all lattice classes.** The summary describes a full system of representatives. The admissibility of the displayed sum needs only split squarefreeness, as its statement says. The separate theorem that these vectors exhaust the lattice classes also requires a split level, in particular residue degree one at the selected places. A split squarefree factorization alone does not identify each residue field with ℤ/N. State the admissibility result for the explicitly indexed sum as written, and qualify its interpretation as the sum over all neighbour-lattice classes by the split-level hypothesis. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/neighbour-vacuum.knowl.md#L5) · [NeighbourLattice.lean:996](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourLattice.lean#L996)

<a name="neighbour-vacuum-finding-2"></a>

**Medium · The denominator is a natural cardinal that can be zero.** Both the definition and theorem use the usual cardinality |Ô/(β)| to define an integer denominator, and line 117 divides it by K as an integer. Lean takes the natural cardinal of the entire matrix set, zero if infinite. For example, take δ=κ=1, X′ nonempty and β equal to 1 everywhere except β_v=0 for one v away from N. The scaling hypotheses hold while Ô/(β) has the infinite quotient Ô_v. Define D_β as the size of (Ô/(β))^{I×X′} if finite and zero otherwise. Its divisibility by K then includes the infinite case. Alternatively add a finite-quotient hypothesis and identify that version as the specialization used for the tower. [Knowl line 40](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/neighbour-vacuum.knowl.md#L40) · [NeighbourVacuum.lean:92](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourVacuum.lean#L92)

<a name="neighbour-vacuum-finding-3"></a>

**Low · Use scalar pairings when writing phases for matrices.** The page uses x\* for conjugate transpose, yet places x\*x and y\*x directly inside an additive character of the adeles. For matrices with multiple columns those products are matrices. The source applies its dot product to vectors indexed by all row-column pairs. For matrix arguments write ⟨y,x⟩=∑_{i,j}ȳ_{ij}x_{ij}=tr(y\*x), and use this scalar in the composition, commutation, and semicharacter formulas. [Knowl line 71](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/neighbour-vacuum.knowl.md#L71) · [TwoEdges.lean:164](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/DualPair/TwoEdges.lean#L164)

<a name="page-point-data-admissible"></a>

### Translated point data are admissible combinations of translates of the vacuum

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/point-data-admissible.knowl.md) · [GoodDatum.lean:370](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/GoodDatum.lean#L370)

The local-unit multiplier argument, the denominator (Nβ)^(dim H_k), both determinant-character factors, and the −ηt₁\* block in the joined translation agree with the source.

<a name="point-data-admissible-finding-1"></a>

**Medium · The chosen modulus is more general than the exact ramification set.** For TameChar the tame factors must be trivial outside Q and may also be trivial at places in Q. The point-mass operator nevertheless uses every place of Q in its modulus. Replacing Q by the actual ramification set can change Φ_k and its level even for the same underlying character. Call Q the chosen modulus supporting the tame part, including in the summary's description of q. Retain the stated product of norms and the condition Q=∅. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/point-data-admissible.knowl.md#L15) · [LevelAndTwists.lean:260](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L260)

<a name="page-point-datum-periods"></a>

### The point datum is fixed by translations by the modulus

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/point-datum-periods.knowl.md) · [UnfoldingStages.lean:977](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean#L977)

The phase of the period is trivial because (b̄t)\*x is integral when x and b̄t are integral. I also checked that the valuation of b divided by the chosen idele is exactly one uniformizer on the specified modulus set.

<a name="point-datum-periods-finding-1"></a>

**Medium · Use the prescribed modulus set of a tame character.** The set Q of a TameChar is allowed to include places with trivial tame part. A trivial character with a permitted nonempty Q still has a twist idele of uniformizer valuation at those extra places, so using its actual ramification set would give the wrong idele and point-datum modulus. Introduce Q as the chosen conjugate-disjoint finite modulus set containing the support of the tame part. The stronger condition that every place of Q has nontrivial tame part is imposed for a Twist. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/point-datum-periods.knowl.md#L15) · [LevelAndTwists.lean:260](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L260)

<a name="page-schrodinger-operator-admissible"></a>

### Values of the Schrödinger operators are admissible combinations of translates

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/schrodinger-operator-admissible.knowl.md) · [AdmissibleCombinations.lean:842](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L842)

The residue count, denominator and sign in ψₘ(−a·b) agree with the point-mass formula. The support restrictions on the lift, the projection and its translation vectors need to be distinguished.

<a name="schrodinger-operator-admissible-finding-1"></a>

**Medium · The projection averages over the conjugate places as well.** For S the primes dividing 𝔪, projOn S averages integral translations supported on S∪conj(S). The description only mentions places dividing 𝔪. By contrast the input residue function is read only on S: the lift is zero when the S-part is nonintegral and ignores coordinates off S. Define P^𝔪 as the normalized mean over translations on S∪conj(S). Specify that the lifted function takes x to Ψ(red(1_S x)) when 1_S x is integral and to zero otherwise. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/schrodinger-operator-admissible.knowl.md#L24) · [AdelicRepresentation.lean:972](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/AdelicRepresentation.lean#L972)

<a name="schrodinger-operator-admissible-finding-2"></a>

**Low · The integrality identity drops the support idempotent.** With arbitrary integral lifts z_b, qt is the conjugate of 1_S·ϖₘ⁻¹(dq) z_{b,i}, where S consists of the primes of 𝔪. Omitting 1_S gives the wrong components away from conj(S), even though the integrality conclusion survives. Insert 1_S inside the conjugation in the formula for qt, and write y_b=conj(1_S·ϖₘ⁻¹ z_b) to make the order of restriction and conjugation explicit. [Knowl line 50](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/schrodinger-operator-admissible.knowl.md#L50) · [AdmissibleCombinations.lean:822](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L822)

<a name="page-seesaw-identity"></a>

### The seesaw identity

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/seesaw-identity.knowl.md) · [SeesawIdentity.lean:624](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L624)

For fixed t and g, the source chooses one nonzero scalar for all twists, then one datum per twist for every ramified form. The denominator clearing, scalar in the zero case, and exponent 3fmn_m² agree.

<a name="seesaw-identity-finding-1"></a>

**Medium · State the terminal identity in joint invariance.** The description of what it means to be a chain datum says the levels of the U(X_j) fix its tensor, after listing X_0 through X_m. The defined action requires b_m=1 and permits the level factors to vary for j&lt;m. Allowing the terminal level to act freely is a stronger condition than the one used in the existence proof. Specify that the tensor is fixed by tuples with b_j in the level for j&lt;m and b_m=1. Link this bullet to property 1 of the seesaw datum. [Knowl line 42](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/seesaw-identity.knowl.md#L42) · [Columns.lean:932](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/Columns.lean#L932)

<a name="page-stage-cuts"></a>

### The cuts for the outer variables

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/stage-cuts.knowl.md) · [Cut.lean:100](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Cut.lean#L100)

The four cut conditions, including nonvanishing on bounded orbits, match the source. The existence argument uses the advertised local power and finite-representative facts, with a distinct argument for the specially chosen initial cut.

<a name="stage-cuts-finding-1"></a>

**Medium · The cuts use a chosen modulus that can exceed the ramification set.** Q is allowed to contain places where the tame character is trivial. J_j imposes its congruences at all places of this supplied Q. Computing J_j from the exact ramification set instead can change the quotient and the cuts. Describe Q as the finite modulus supporting the tame part, and take q to be the product of the norms of all its places. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/stage-cuts.knowl.md#L15) · [LevelAndTwists.lean:260](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L260)

<a name="stage-cuts-finding-2"></a>

**Medium · The initial cut needs invariance of the chosen level.** Ω₀ consists of classes of the chosen level, whereas the chosen stage cuts for j&gt;0 are invariant under the integral Bessel subgroup. Knowing that the image of level X₀ lies in K₀ does not imply it preserves those chosen-level classes, and Ω₀ was not defined as a stage cut. For j=0 use xJ₀∈Ω₀ iff x belongs to the chosen level and the fact that the image of level X₀ is contained in that chosen level. Its multiplicity is identically one. Apply the stage-cut argument for j&gt;0. [Knowl line 60](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/stage-cuts.knowl.md#L60) · [Cut.lean:186](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Cut.lean#L186)

<a name="page-top-of-the-chain"></a>

### The top of the chain: restriction to the definite space Y_m

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/top-of-the-chain.knowl.md) · [SeesawIdentity.lean:90](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L90)

The outline obtains C_t as the product of the branching scalar, the dimension of the weight space, and the normalization c. The library results supply both the archimedean branching average and the finite class integral.

<a name="top-of-the-chain-finding-1"></a>

**Medium · Define the adelic coefficient of the upper algebraic form.** The core writes t(ψ(diag(k,1))) for an adelic k. The algebraic form ψ is a vector-valued function on finite points. Its coefficient at h=diag(k,1) also uses the action of h_∞⁻¹ on that vector. The phrase about coefficients in line 42 leaves this operation implicit in the lemma whose integral uses it. Set h=diag(k,1) and write F(k)=t(ρ(h_∞⁻¹)ψ(h_f)), identifying ρ with the conjugate Weyl representation. This also fixes the meaning of the coefficient reused by the lower-chain proof. [Knowl line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/top-of-the-chain.knowl.md#L25) · [SmoothAlgebraicForms.lean:155](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/SmoothAlgebraicForms.lean#L155)

<a name="page-tower-gradings-and-evaluated-data"></a>

### Gradings of the tower Y_k and the evaluated data

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data.knowl.md) · [EdgePairEvaluation.lean:1167](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L1167)

The final evaluation is constructed with p=π_N, and the map is zero beyond i=ρ. The generic constant at the nonfinal stages and the exponent f n_m² in the residue count agree.

<a name="tower-gradings-and-evaluated-data-finding-1"></a>

**Medium · Identify the target of the evaluated datum, including the last pair.** The display introduces X″_{2i+2} without identifying it with the tower index X_{2i+2}. The last grading has definite part InitIndex(m), of size n_m−1, and the last double lift adjoins precisely the line that restores X_m. Leaving this unresolved obscures why this datum is an input to the next definite lift or to the terminal coefficient. Use Hom(X_{2i+1},X_{2i+2}) in the second factor. In the final grading identify the definite part as InitIndex(m), write X_m=InitIndex(m) ⊔ {∗}, and note that the final grading has constant 1. [Knowl line 44](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data.knowl.md#L44) · [EdgePairEvaluation.lean:1167](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L1167)

<a name="page-unfolding-stage-as-coefficient-of-chain"></a>

### After each double step the unfolding function is a coefficient of the definite chain

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/unfolding-stage-as-coefficient-of-chain.knowl.md) · [UnfoldingStages.lean:838](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean#L838)

The endpoint embedding goes from the definite part of the chosen last grading to X_{2i+2}, and right-coset invariance follows by factoring every new representative as y_k u_k in the finite Weil action. The coefficient is uniform in the character, source form and finite translates.

<a name="unfolding-stage-as-coefficient-of-chain-finding-1"></a>

**Medium · Use odd string length in the uniqueness step.** Equivariance alone gives transformation only for the subgroup where u−1 has degree at least two. Agreement on U(X_{2i+2}) determines the function here because m−1−(2i+2) is odd, so every unipotent at the induction stage belongs to that subgroup. The source supplies this parity when applying uniqueness. State that the terminal string of this induction step is odd and invoke the odd-length uniqueness lemma before concluding equality on the full Bessel group. [Knowl line 58](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/unfolding-stage-as-coefficient-of-chain.knowl.md#L58) · [Equivariant.lean:400](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/Equivariant.lean#L400)

<a name="unfolding-stage-as-coefficient-of-chain-finding-2"></a>

**Low · Absorb the double-unfolding scalar into the archimedean factor.** The preceding identity gives z times the double integral for v. Applying the complement to v alone yields a coefficient of the unscaled integral. The source applies the complement to z v to get exactly the original unfolding function. Apply the definite-lift identity to z v, or multiply the resulting linear functional by z. Note that z is independent of the character and the finite points. [Knowl line 53](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/unfolding-stage-as-coefficient-of-chain.knowl.md#L53) · [UnfoldingStages.lean:789](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/UnfoldingStages.lean#L789)

<a name="page-moved-vacuum-admissible"></a>

### A moved translate of the vacuum is an admissible combination of translates

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/moved-vacuum-admissible.knowl.md) · [AdmissibleCombinations.lean:735](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L735)

The index of L∩g⁻¹L in L gives exactly |Δ_f(g)|². The projective composition factor has the second vector conjugated, and the sum of absolute values of the normalized coefficients under σ is |σc|.

<a name="moved-vacuum-admissible-finding-1"></a>

**Low · The displayed Heisenberg phase uses two undefined symbols.** The only occurrence of ψ and c₀ on the page is the formula for ζ_z. Its exact scalar depends on the self-dual character and the chosen trace-one adele. Identify ψ as the fixed self-dual additive character and c₀ as the integral adele with c₀+conj(c₀)=1 from the Weil data, or state only the root-of-unity consequence of the cited composition formula. [Knowl line 51](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/moved-vacuum-admissible.knowl.md#L51) · [VacuumProjections.lean:102](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Construction/VacuumProjections.lean#L102)

<a name="page-seesaw-datum"></a>

### The seesaw datum

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/seesaw-datum.knowl.md) · [SeesawIdentity.lean:503](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L503)

The factors of the evaluated tensor run from the last pair to the first, and the cut-sum invariance uses tuples ending in the identity. The denominator is uniform in the tame character, while the absolute-size estimates are conditional.

<a name="seesaw-datum-finding-1"></a>

**Low · Keep the empty-modulus condition on both size bounds.** The statement records the correct condition, but the proof invokes a size of 1 for evaluated tensors and a size of C^m for the weighted cut without it. Both input results bound the absolute coefficient sums only when Q is empty. Attach “when Q is empty” to both size estimates in lines 60–62 and retain the denominator estimates for every Q. [Knowl line 60](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/seesaw-datum.knowl.md#L60) · [SeesawIdentity.lean:604](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean#L604)

<a name="page-shift-maps-lattices"></a>

### A nonzero constant term at the shift forces a lattice inclusion

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/shift-maps-lattices.knowl.md) · [Frequency.lean:307](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Frequency.lean#L307)

The finite zero term produces an integral matrix whose negative-degree entries equal those of (b̄/α)sh. Projecting the conjugated matrix onto its degree −1 part gives the claimed inclusion between the graded lattices.

<a name="shift-maps-lattices-finding-1"></a>

**Low · Distinguish the finite frame from the finite group point.** In the theorem x_f labels the finite part of the variable adelic point. Here x_f becomes the fixed frame of the space, the variable is renamed p, and line 66 again uses r x_f for the group point. The fixed frame can lie outside the finite unitary group. Use B and B′ for the fixed frames and p=x_f, p′=x′_f for the variable group points throughout. Then W=(B′p′)\[l\](Bp)⁻¹ and its source lattice at the translated point is Λ_{rp}. [Knowl line 54](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/shift-maps-lattices.knowl.md#L54) · [Frequency.lean:267](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Frequency.lean#L267)

<a name="page-standard-lattice-membership"></a>

### Membership in the glued standard lattice

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/standard-lattice-membership.knowl.md) · [StandardLines.lean:224](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/StandardLines.lean#L224)

The middle component solves to λ_b⁻¹y_b−π⁻¹y_e, where e is the distinguished vector outside the string, and both coordinates in that expression have grade zero. The page assigns the same written subscript to two different coordinates.

<a name="standard-lattice-membership-finding-1"></a>

**Low · Give the distinguished coordinate a separate subscript.** The notation y₀ denotes the coordinate on the distinguished non-string vector and also y_b at b=0 on the string. When s=1, the middle test on line 31 therefore appears to subtract two multiples of the same variable, although the source takes coordinates at two different basis indices. Write y_e for the distinguished non-string coordinate and y_{z_b} for the string coordinates, including in the solved basis coefficients. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/standard-lattice-membership.knowl.md#L26) · [StandardLines.lean:228](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/StandardLines.lean#L228)

<a name="page-string-lattices-line-by-line"></a>

### The string lattices are sums of lines

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/string-lattices-line-by-line.knowl.md) · [StandardLines.lean:301](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/StandardLines.lean#L301)

The extra factor N enters precisely through the middle gluing condition, and choosing distinguished coordinate πη constructs a preimage under projection. The construction needs different names for its two potentially zero-indexed coordinates.

<a name="string-lattices-line-by-line-finding-1"></a>

**Low · Disambiguate the coordinate changed in the lift.** The lift changes z₀ while keeping the string coordinate z_c fixed. For a one-vector string c=0, so lines 52–53 use z₀ for both the changed distinguished coordinate and the unchanged string coordinate. Lean updates only the extra basis index outside the string. Call the extra coordinate z_e, put z_e=πη, and retain z_{z_b}=y_{z_b} for every string index b. Use the same convention for y_e in part 3. [Knowl line 52](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/string-lattices-line-by-line.knowl.md#L52) · [StandardLines.lean:338](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/StandardLines.lean#L338)

<a name="page-tower-lattice-data"></a>

### The lattices of the tower Y_k are glued lattices

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/tower-lattice-data.knowl.md) · [LevelIdeles.lean:125](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/LevelIdeles.lean#L125)

I checked how jα·conj(α) cancels the valuation of the different, the latticeScale exponent, and the frame factorization over integral GL. The last level inclusion applies to the full declared modulus of the tame character.

<a name="tower-lattice-data-finding-1"></a>

**Low · The level places include all of the assigned modulus.** The last assertion calls Q the ramification set. The defining condition requires trivial tame factors outside Q only. LevelIdeles.lean:140 takes a level that also imposes reduction at unramified places deliberately included in Q. Use ‘a tame character with chosen modulus Q’ and describe the input as globally integral, reducing to one at the chosen places and equal to one at every place of Q. [Knowl line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/tower-lattice-data.knowl.md#L35) · [LevelAndTwists.lean:269](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L269)

## Other knowls checked

<a name="page-adjoint-on-weighted-translations"></a>

### Adjoints of integral matrices on weighted translations

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/adjoint-on-weighted-translations.knowl.md) · [NeighbourLattice.lean:62](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourLattice.lean#L62)

For equal weights the local bound is the product of the conjugate-place bound on the matrix entry and the bound on d_i y_i. For unequal weights that entry vanishes, and the conjugated reindexing uses that w and w̄ divide the same rational primes.

<a name="page-admissible-combination-calculus"></a>

### Calculus of admissible combinations

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/admissible-combination-calculus.knowl.md) · [AdmissibleCombinations.lean:624](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L624)

The single-term, scalar, bilinear and denominator-clearing arguments give the stated bounds. The tensor induction with disjoint pairs of coordinates is valid for the abelian index groups in the page and also works for the general additive groups in Lean.

<a name="page-admissible-combination-substitution"></a>

### Substitution in admissible combinations

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/admissible-combination-substitution.knowl.md) · [AdmissibleCombinations.lean:541](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L541)

The coefficient of y is the sum of c(x)rₓ(y) on the outer support. Multiplication by dd′k clears its denominator, and summing the triangle inequality gives B|B′| even when the bounds are arbitrary reals.

<a name="page-cover-multiplicity"></a>

### Cover multiplicity of a finite set of cosets

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/cover-multiplicity.knowl.md) · [IntegralAsCosetSum.lean:49](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean#L49)

The definition counts cosets admitting a representative and assigns zero to an infinite set. Left multiplication preserves the count, and for a saturated partial transversal the counted cosets form the stabilizer orbit of the identity coset.

<a name="page-cut-sum"></a>

### Weighted sums over the cuts

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/cut-sum.knowl.md) · [Cut.lean:356](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Cut.lean#L356)

The recursion puts the last cut coordinate in the innermost sum, and the level action on that coordinate preserves both the cut and its multiplicity. The reciprocal weight is integral away from q, with at most 𝒞 terms per stage when Q is empty.

<a name="page-cut-with-multiplicities-dividing-powers"></a>

### A cut whose multiplicities divide powers of q

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/cut-with-multiplicities-dividing-powers.knowl.md) · [IntegralAsCosetSum.lean:156](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean#L156)

The cut is the saturation of one compact-image representative per S-orbit. Its multiplicities on covered orbits are positive finite stabilizer indices, which gives nonvanishing even in the case q=0.

<a name="page-double-lift-evaluation-equivariant"></a>

### The finite evaluation of a pair of edges is equivariant

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/double-lift-evaluation-equivariant.knowl.md) · [EdgePairEvaluation.lean:929](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L929)

Writing n,m,l for the large ranks and r for the number of positive target weights, the bare υ-exponents at (det g,det g′,det k) are (⌈m/2⌉,−⌈n/2⌉−⌊l/2⌋,⌊m/2⌋). The stages add (−s′/2,r+|q|,−s′/2), giving exactly the small exponents by m=|X′|+s′, n+l=|X|+|X″|+2(r+|q|) and the even rank sum.

<a name="page-finite-zero-term"></a>

### The finite part of the zero term

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/finite-zero-term.knowl.md) · [EdgePairEvaluation.lean:93](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L93)

The adelic zero term is the quotient mean along k, and the finite construction inserts the moved real vacuum. The support proof produces l=Λ\* v using a primitive rescaling of M′\*k, and the nonzero value on a moved vacuum then rules out vanishing at the vacuum itself.

<a name="page-generator-of-plus-over-minus"></a>

### A vector of Lambda-plus outside Lambda-minus generates the quotient at a place above N

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/generator-of-plus-over-minus.knowl.md) · [StandardLines.lean:557](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/StandardLines.lean#L557)

A nonintegral middle coordinate of y has a simple pole at w because N is a uniformizer there. For each z the quotient of the two middle coordinates at that same w is integral, and extending it by zero gives the required global multiplier.

<a name="page-glued-level-congruences"></a>

### Congruence levels inside the stabiliser of the glued lattice

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/glued-level-congruences.knowl.md) · [GluedLevel.lean:99](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/GluedLevel.lean#L99)

The odd-length corner is divided by ππ̄. The last-row congruence for the integral unitary inverse supplies the conjugate-column congruence, and at least one divisor is a unit at each place. This also preserves strict smallness away from P and its conjugate.

<a name="page-graded-gram-signature"></a>

### Signature of the graded Gram matrix

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/graded-gram-signature.knowl.md) · [AdmissibleCombinations.lean:398](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L398)

The off-middle hyperbolic planes each contribute one negative sign. In an odd string the middle vector z/√N contributes one further negative sign, and for N=1 the displayed columns are orthonormal for the standard metric.

<a name="page-graded-lattice-basis-unimodular"></a>

### The glued lattice is unimodular

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/graded-lattice-basis-unimodular.knowl.md) · [AdmissibleCombinations.lean:298](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L298)

The odd glue plane has block ((0,−1),(−1,−N)) with inverse ((N,−1),(−1,0)). Together with the reversal and identity blocks, this puts both the Gram matrix and its inverse over any unital subring.

<a name="page-integral-away"></a>

### Complex numbers integral away from n

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/integral-away.knowl.md) · [AdmissibleCombinations.lean:97](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L97)

The definition uses every embedding into ℂₗ for every prime coprime to n, and the quotient argument correctly treats c=0. For c≠0 the relation dqᵏ=cm gives |d/c|ₗ=|m|ₗ.

<a name="page-l-adic-units-multiplier-and-characters"></a>

### The finite multiplier and character values are l-adic units at integral points

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/l-adic-units-multiplier-and-characters.knowl.md) · [AdmissibleCombinations.lean:451](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L451)

The algebraic finite character υ|·|^(−1/2) has exponents 0 and −1 on the two halves of the CM embeddings. The weight formula for the determinant has exponent −e(τ), and integral invertibility makes each local factor one.

<a name="page-lattice-bounds-induction-step"></a>

### Lattice bounds along the tower: the induction step and the dichotomy

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/lattice-bounds-induction-step.knowl.md) · [Sandwich.lean:208](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Sandwich.lean#L208)

Dualizing the previous upper inclusion gives the conjugate scaling on Λ⁺, and local generation of Λ⁺/Λ⁻ at a place where q and q̄ are units gives the splitting alternative. The orbit assertions are stated for ideles q, a valid specialization of the two orbit lemmas for finite adeles.

<a name="page-lattice-splitting-and-scalings"></a>

### Lattices that split along X at a place

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/lattice-splitting-and-scalings.knowl.md) · [Sandwich.lean:112](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/Sandwich.lean#L112)

Conjugating the idempotent at w gives the splitting at w̄ by Hermitian duality. Both components of y−pr(y) therefore lie locally in the lattice, so scaling by z and by its integral inverse preserves the lattice and is the identity away from the pair.

<a name="page-shift-of-string-lattice"></a>

### The shift takes Lambda-plus onto a times Lambda-minus of the shorter string

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/shift-of-string-lattice.knowl.md) · [StandardLines.lean:431](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/StandardLines.lean#L431)

For surviving indices the two tests 2i+1&lt;s and 2i&lt;s−1 coincide and ℓ_i=aℓ′_i. Extending the target coefficients by a final zero proves surjectivity for the stated positive source string length.

<a name="page-split-squarefree-factorisation"></a>

### Split squarefree factorisation of N

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/split-squarefree-factorisation.knowl.md) · [AdmissibleCombinations.lean:142](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L142)

The prescribed valuations and the disjointness of P from its conjugate give order one for N on P∪conj(P), and zero elsewhere. The application to π_N uses the separate complete-splitting property of the level prime.

<a name="page-string-sum-lattice-criteria"></a>

### The string lattices in the basis of string powers

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/string-sum-lattice-criteria.knowl.md) · [StandardLines.lean:406](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/StandardLines.lean#L406)

Computed both parities of the line idele and the powers of c in the string coefficient. Their ratio contributes a local unit and, in negative grade, a factor −N. Adding the middle factor in the projected lattice gives the cutoff 2i+1≥s.

<a name="page-translation-groups"></a>

### Groups of translations with denominators away from q

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/translation-groups.knowl.md) · [AdmissibleCombinations.lean:126](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/AdmissibleCombinations.lean#L126)

Each coordinate is tested after multiplication by its own weight at places whose prime ideal excludes q. Specializing all the weights to d gives the constant-denominator group used by the vacuum lemmas.

<a name="page-vacuum-translate-away-from-level"></a>

### Translates of the vacuum can be moved away from N

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/vacuum-translate-away-from-level.knowl.md) · [NeighbourVacuum.lean:166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/NeighbourVacuum.lean#L166)

At places over N, coprimality makes the weighted coordinates integral and β and β̄ are units. Subtracting the integral component there gives the required translate, with the phase from the finite Heisenberg composition law. These are the only consequences of the split-level and scaling assumptions used here.

<a name="page-zero-term-lattice"></a>

### The lattice of the finite zero term

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-seesaw/zero-term-lattice.knowl.md) · [EdgePairEvaluation.lean:265](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/EdgePairEvaluation.lean#L265)

For B=i_f g+k_f c integral, B\*(i_f w+k_f b)=g⁻¹w proves the reverse lattice inclusion. The nonzero vacuum multiple and the inverse multiplier Δ_f(g)/|Δ_f(g)|² give the stated sum over L′/(L′∩L°).
