# upper-elementary-divisors

This area contains 67 individual knowls and a chapter page. The review records 30 comments. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports/upper-elementary-divisors.md)

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Chapter page

<a name="page-upper-elementary-divisors"></a>

### Elementary divisors of a Hecke operator

Correction recorded · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors.knowl.md) · [ElementaryDivisorTheorem.lean:1166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L1166)

The stated colength constant is 3Nn(P⁻²ʳ+r²/(kP))+θm, with the full |X||I| factor. The calculation of the defect and the passage from the congruences to the Nakayama bound both need corrections.

<a name="upper-elementary-divisors-finding-1"></a>

**High · The positive root variable at the distinguished letter has an extra unit of weight.** For distinct root indices the weight of uᵢ is q/(q−1), while the displayed rule gives 1/(q−1). Thus the purported defect of every monomial containing uᵢ is short by its exponent there. This defect is used in the root lemma and later dimension conditions. Add +1 to the indicated weight on uᵢ, in addition to the signed cyclic contribution. Equivalently add the exponent of uᵢ to the weighted degree. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors.knowl.md#L21) · [TwistingData.lean:166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L166)

<a name="upper-elementary-divisors-finding-2"></a>

**Medium · Nakayama uses reductions after division by w^(c−1).** The dimension estimate applies to residues of every h with w^(c−1)h∈C. The chapter records only the smaller set of residues of C before invoking Nakayama. In a valuation ring, C=wO has zero reduction, although all h satisfy wh∈C. A bound only on the former residues cannot justify the generator count. Introduce the residue subspace S containing the reductions of all h with w^(c−1)h∈C, give its dimension bound and use that stronger property in the generator argument. [Knowl line 57](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors.knowl.md#L57) · [ElementaryDivisorTheorem.lean:635](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L635)

<a name="upper-elementary-divisors-finding-3"></a>

**Medium · The numerical large-degree conditions alone are insufficient for the stated theorem.** The chapter states the intertwining assumption separately and links the full theorem. Its displayed colength claim refers only to large degree, although Lean also takes a characteristic-zero valuation domain O with p a nonunit. The opening paragraph allows an arbitrary coefficient ring. Name the valuation-domain and nonunit hypotheses beside the displayed result and refer back to the finite edge data and intertwining identity. [Knowl line 59](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors.knowl.md#L59) · [ElementaryDivisorTheorem.lean:1166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L1166)

<a name="upper-elementary-divisors-finding-4"></a>

**Low · The cycle axiom permits algebraic twists.** The motivation states that the maps g↦ιₛ(g) are nonalgebraic. The axiom requires only a Frobenius congruence. For W=R=𝔽₂₅, p=P=5 and N=2, the identity and entrywise fifth power are polynomial maps satisfying it, with w=0. Say that the cycle gives no general algebraic formula for the maps. This motivates the generic-matrix construction and also covers the algebraic special cases. [Knowl line 45](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors.knowl.md#L45) · [TwistingData.lean:94](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L94)

## Knowls with comments

<a name="page-conjugation-invariant-average"></a>

### Average for a Levi subgroup on polynomials in matrix entries

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/conjugation-invariant-average.knowl.md) · [InvariantAverage.lean:262](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L262)

The three axioms, the direction of conjugation, and the column-minus-row exponent agree. The vanishing assertion in the properties and the comparison in the summary have wider scope than those axioms imply.

<a name="conjugation-invariant-average-finding-1"></a>

**High · Unequal weights do not force vanishing over arbitrary rings.** The definition allows arbitrary commutative W and O. Take W=O=𝔽₂, k=2 and distinct block labels. The Levi group is trivial, so extracting the coefficient of X₀₁ is invariant, yet it sends X₀₁ to 1 even for weights ρ=(1,0). The cited vanishing lemma assumes W local and O a characteristic-zero domain with a positive integer nonunit. State those extra hypotheses before asserting vanishing, or give the more general sufficient condition of a separating unit whose character difference acts injectively. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/conjugation-invariant-average.knowl.md#L30) · [InvariantAverage.lean:229](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L229)

<a name="conjugation-invariant-average-finding-2"></a>

**Medium · The comparison with evaluation concerns every conjugate.** The summary predicates agreement on the support of ψ alone. A Levi element can exchange a good diagonal variable with a bad one, so a polynomial supported on good monomials need not satisfy the comparison. The core correctly imposes a degree bound and tests every Levi conjugate. Describe the summary’s comparison as agreement in degrees ≤D when every Levi conjugate has no bad monomial modulo the chosen ideal. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/conjugation-invariant-average.knowl.md#L5) · [InvariantAverage.lean:272](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L272)

<a name="page-deep-forms-have-heavy-monomial"></a>

### A nonzero deep form has a monomial of large weight

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/deep-forms-have-heavy-monomial.knowl.md) · [Depth.lean:612](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Depth.lean#L612)

Specialization preserves nonvanishing and sends every deep factor of a translated monomial into the point ideal. I checked the multiplicity theorem in MultivariatePolynomials.lean at line 186, including its product-of-orders hypothesis.

<a name="deep-forms-have-heavy-monomial-finding-1"></a>

**Medium · Shallow variables need order one in the zero count.** The displayed cases define κ solely from the row index. The conclusion sums only over deep variables, but line 26 uses κ on every variable. For r=1 and k=2 the displayed definition makes the product P^(2N)=q², while the family contains only q points. Specify κ(v)=1 for shallow variables and apply the displayed P and P^(2r) branches only to deep variables. This gives the product in the unipotent-points construction and leaves the concluding sum over deep variables intact. [Knowl line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/deep-forms-have-heavy-monomial.knowl.md#L17) · [Depth.lean:99](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Depth.lean#L99)

<a name="page-depth-of-monomial"></a>

### Depth of a monomial

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/depth-of-monomial.knowl.md) · [TwistingData.lean:155](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L155)

The parity-dependent indicator and the tensor product of symmetric powers both give the stated diagonal entries. The interpretation of this diagonal endomorphism as an instance of the group representation fails for general t.

<a name="depth-of-monomial-finding-1"></a>

**Medium · An arbitrary depth scaling need not be a twisted group element.** The displayed tensor identity holds for every t∈R. The following sentence describes it as evaluation of the twisted GLₖ(W) representation at a diagonal matrix. For t=0, k=2, r=1 and n=1 the depth diagonal has zero entries, while every matrix in the image of a group representation is invertible. Describe the operator as the tensor product of symmetric powers of the separate letterwise diagonal matrices given in the display. The displayed identity is sufficient for general t. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/depth-of-monomial.knowl.md#L21) · [TwistingData.lean:286](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L286)

<a name="page-determinant-of-step-map"></a>

### Determinant of the step map

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/determinant-of-step-map.knowl.md) · [PieriCone.lean:166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L166)

The prefix products, the wraparound term, and the order of the permutation in det(1−AB) agree. The change-of-variables claim needs an outer-measure convention to apply to every set as stated.

<a name="determinant-of-step-map-finding-1"></a>

**Medium · Ordinary Lebesgue measure is undefined for some allowed sets.** The text quantifies over every Y but links to ordinary Lebesgue measure on measurable sets. For k=1, m=0, v=+, P=2, D=1, take a nonmeasurable subset Y of (0,1). The step map is the identity, and both advertised measures are undefined in that convention. Lean’s measure on arbitrary sets is its associated outer measure. Use Lebesgue outer measure for arbitrary sets, or state the ordinary-measure version for measurable Y. The downstream cone and slab are measurable. [Knowl line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/determinant-of-step-map.knowl.md#L19) · [PieriCone.lean:214](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L214)

<a name="page-edges-and-halfway-lattices"></a>

### Edges, normalised coefficients and forms in all halfway lattices

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices.knowl.md) · [Edges.lean:386](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L386)

The left-coset convention, the diagonal w^depth, and both conditions defining the all-edges submodule agree. The accompanying geometric interpretations need qualifications for the advertised range of rings and ranks.

<a name="edges-and-halfway-lattices-finding-1"></a>

**Medium · The normalized basis uses an inverse that may not exist.** A Frobenius cycle permits a coefficient field of characteristic p with w=0. For a positive-depth monomial the displayed w^(−depth) is then undefined, although the diagonal w^depth is still defined. For instance W=O=𝔽₂₅, p=5, N=2, with the identity and fifth-power maps, admits this cycle. Give the diagonal formula for every cycle. Describe the normalized monomial basis in the geometric setting of a domain with w nonzero, inside its fraction field. [Knowl line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices.knowl.md#L17) · [Edges.lean:302](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L302)

<a name="edges-and-halfway-lattices-finding-2"></a>

**Low · Quotients of dimension r require r≤k.** The definition permits r&gt;k. In that range the parahoric is all of GLₖ and its coset set is a singleton, whereas a residue-vector-space quotient of a rank-k lattice cannot have dimension r. The source qualifies the geometric interpretation by r≤k. Add r≤k to the sentence identifying the cosets with geometric edges. [Knowl line 16](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices.knowl.md#L16) · [Edges.lean:60](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L60)

<a name="edges-and-halfway-lattices-finding-3"></a>

**Low · The linked divided-power stability proof has additional hypotheses.** The remark asserts stability of both lattices for an arbitrary coefficient ring. The linked theorem proves the assertion for the divided-power lattice assuming O is a characteristic-zero domain. Its proof cancels factorials, which need not be cancellable over the ring stated here. State the characteristic-zero domain hypothesis for the linked divided-power result, or supply the universal polynomial identity over ℤ and specialize it to prove the more general assertion. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices.knowl.md#L26) · [Edges.lean:267](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L267)

<a name="page-existence-of-average"></a>

### Existence of an average for a Levi subgroup

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/existence-of-average.knowl.md) · [InvariantAverage.lean:946](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L946)

The proof correctly subtracts the trace on the large-weight submodule and tests every conjugate to obtain the ideal congruence. The published summary describes a comparison disproved by exchanging two diagonal variables.

<a name="existence-of-average-finding-1"></a>

**Medium · A single polynomial’s good support does not imply evaluation agreement.** Take W=O=ℤ localized at 3, p=3, f=D=1, k=2, a single Levi block, ρ=(1,0) and t=0. The monomial X₁₁ has no bad term, but a permutation conjugates it to the bad X₀₀. Any invariant average kills X₁₁, while scaled evaluation there is 3⁴. The precise guarantee also ends at D, which can be smaller than p^f−1. Say that for degree at most D the average agrees modulo J with scaled evaluation if every Levi conjugate has its bad coefficients in J. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/existence-of-average.knowl.md#L5) · [InvariantAverage.lean:949](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L949)

<a name="page-origin-functions"></a>

### Restriction to edges and functions depending only on the origin

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/origin-functions.knowl.md) · [Edges.lean:507](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L507)

Restriction, its transpose, and saturation by powers of w agree entrywise. Interpreting every saturated vector as depending on its origin requires care when w vanishes.

<a name="origin-functions-finding-1"></a>

**Medium · Saturation can include vectors that vary over one origin.** For w=0 the defining condition holds for every ψ with m=1 and φ=0. Take degree n=0 and two edges with the same origin and the same frame. The restriction has equal values on the two edges, while (0,1) belongs to the displayed module. Cycles over a field of characteristic p allow w=0. Call the general module the w-power saturation of the restriction image. Explain the interpretation as a restriction after inverting w in the geometric case where w is a non-zero-divisor. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/origin-functions.knowl.md#L21) · [Edges.lean:507](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L507)

<a name="page-power-packing"></a>

### Packing forms into powers of the variables

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/power-packing.knowl.md) · [DefectCount.lean:235](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L235)

Reduction of the exponents modulo m recovers the class and proves injectivity. The translation formula in the body correctly translates both the input forms and the extra monomials, contrary to the summary’s equivariance claim.

<a name="power-packing-finding-1"></a>

**Medium · Power substitution commutes with the action, while the packing has extra moving factors.** The summary attributes equivariance to packing. With k=2, m=q⁰=1 and n=0, packing the single constant 1 gives ∏ₛx_(a,s)². Swapping the two rows fixes the constant and changes this monomial. The correct formula in the body also translates the class monomial x^(γᵤ). Say the substitution x↦xᵐ commutes with the action when m=qʲ. Describe the packed translate as a sum in which both the input form and the class monomial are translated. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/power-packing.knowl.md#L5) · [DefectCount.lean:284](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L284)

<a name="page-adjoint-weights"></a>

### Adjoint weights from multinomial coefficients

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/adjoint-weights.knowl.md) · [InvariantAverage.lean:125](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L125)

The construction divides p^(|σ|f) by the multinomial in the permitted degrees and sets the other weights to zero. Comparing equal-degree terms by Fock adjointness works after cancellation of the common degree factorial.

<a name="adjoint-weights-finding-1"></a>

**Low · The logarithmic bound needs a degree-zero case.** The proof applies floor(logₚ(n+m)) when n=m=0, which satisfies 0&lt;p^f for every allowed f. The ordinary logarithm is undefined at zero. The source uses the natural-number logarithm, which handles this case. Handle n+m=0 first using the binomial coefficient 1, then apply the logarithmic estimate for n+m≥1. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/adjoint-weights.knowl.md#L29) · [InvariantAverage.lean:73](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L73)

<a name="page-defect-of-steps"></a>

### Defect of a vector of steps. The defect cone is the image of the Pieri cone

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/defect-of-steps.knowl.md) · [DefectCount.lean:499](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L499)

The cyclic sum leaves the exceptional contribution (St ν)(Yᵢ)−(ν(a,i)−ν(a′,i)). The preimage criterion and the product of flag factors agree with the volume theorem.

<a name="defect-of-steps-finding-1"></a>

**Low · Coincident root indices have a single combined weight.** Part 1 allows a=a′. In this case Xₛ=Yₛ, so the stated individual weights ±P^\[s−i\]/(q−1) are two contributions to one coordinate. The coordinate actually has weight 0 away from i and weight 1 at i. The telescoping identity still holds. Handle a=a′ first, when both sides are (St ν)(a,i), or describe the signed terms as indicator contributions that add when the indices coincide. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/defect-of-steps.knowl.md#L27) · [TwistingData.lean:166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L166)

<a name="page-defect-weight-bounds"></a>

### Bounds on the defect weights

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/defect-weight-bounds.knowl.md) · [TwistingData.lean:371](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L371)

The 3/2 and 2d estimates follow from 5P^\[s−i\]≤q and the finite geometric sum. The proof’s initial individual-weight identities require distinct indices, although its second estimate correctly handles coincident indices.

<a name="defect-weight-bounds-finding-1"></a>

**Low · The individual weight formulas assume a≠a′.** The opening proof line assigns two different values to ω(Yₛ) and ω(Xₛ) even though part 2 explicitly allows Xₛ=Yₛ. For equal indices their common weight is 0 away from i and 1 at i. The proof later uses the correct difference of indicator contributions. Place the two equalities inside the proof of part 1 under a≠a′. For part 2 start from the difference-of-indicators formula. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/defect-weight-bounds.knowl.md#L22) · [TwistingData.lean:166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L166)

<a name="page-edge-conditions"></a>

### Conditions on an edge

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/edge-conditions.knowl.md) · [ElementaryDivisorTheorem.lean:688](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L688)

The constructions of C and S use the strict cutoff 3c\*, and property 6 uses 2(k+1)≤c\* and 8Nkc\*P^(2r)≤θn. Cancellation in property 5 is justified in characteristic zero for the positive precision used in the theorem.

<a name="edge-conditions-finding-1"></a>

**Low · Precision zero uses a truncated predecessor.** The definition permits c=0, for which the displayed w^(c−1) is an inverse that a valuation domain need not contain. The natural-number exponent in the source is zero in that case, so property 5 applies directly to h∈C. Write w^max(c−1,0) in property 5, or spell out its c=0 case. Define the pairing exponent c₀=k²fN alongside the other parameters. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/edge-conditions.knowl.md#L21) · [ElementaryDivisorTheorem.lean:635](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L635)

<a name="page-edge-hecke-operator"></a>

### Edge coordinates and the edge Hecke operator

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/edge-hecke-operator.knowl.md) · [ElementaryDivisorTheorem.lean:747](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L747)

The inverse-transpose origin coset and inverse terminus coset agree with both coordinate axioms. The transposed three-matrix product acts on the exponent index and u acts on H in the order specified by the bijection J.

<a name="edge-hecke-operator-finding-1"></a>

**Low · The lattice illustration omits its uniformizer assumption.** The geometric change of basis uses a diagonal matrix with entries p⁻¹. The source’s geometric model explicitly makes p a uniformizer of W, while the knowl only assumes a local ring W. For instance its algebraic definition permits W to be a finite field of characteristic p, where the displayed p⁻¹ has no meaning. Introduce the illustrative lattice construction by assuming p is a uniformizer of W and read the diagonal matrix over its fraction field. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/edge-hecke-operator.knowl.md#L29) · [ElementaryDivisorTheorem.lean:337](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L337)

<a name="page-elementary-divisors-of-edge-hecke-operator"></a>

### Theorem on elementary divisors of the edge Hecke operator

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/elementary-divisors-of-edge-hecke-operator.knowl.md) · [ElementaryDivisorTheorem.lean:1166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L1166)

The bound descends along the surjective regrouping followed by f using only inclusion of the factored image in Y(L). The DVR length corollary uses the very same exponent through finite generation of L and the quotient-length lemma at Colength.lean:257.

<a name="elementary-divisors-of-edge-hecke-operator-finding-1"></a>

**Low · The abstract image need not be a lattice.** The summary calls L a lattice. The theorem allows an arbitrary O-module M and an arbitrary linear image L, which may have p-torsion. For example, coefficientwise reduction of the source modulo p intertwines the operator with its reduction. Call L the image submodule in the summary. The core theorem and its length corollary already use the correct generality. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/elementary-divisors-of-edge-hecke-operator.knowl.md#L5) · [ElementaryDivisorTheorem.lean:1170](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L1170)

<a name="page-few-forms-of-bounded-defect"></a>

### Few forms have bounded defect

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/few-forms-of-bounded-defect.knowl.md) · [DefectCount.lean:939](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L939)

The flag index cancels the cone fraction, and the positive application B=n+4tP^(2a′) gives 2Nk′E/n≤θ. The auxiliary single-letter slab estimate omits the sign restriction used in this application.

<a name="few-forms-of-bounded-defect-finding-1"></a>

**Low · The single-letter volume bound needs a nonnegative upper endpoint.** The auxiliary estimate assumes only d≤B and drops Lean’s absolute value around B^k′/k′!. With k′=1 and d=B=−1 the set is empty, yet its claimed upper bound is −1. The value of B used in the theorem is positive. Restrict the auxiliary estimate to B≥0, or retain |B^k′/k′!| as in the source. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/few-forms-of-bounded-defect.knowl.md#L30) · [DefectCount.lean:803](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L803)

<a name="page-gauss-filtration"></a>

### Real filtrations and the Gauss filtration

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/gauss-filtration.knowl.md) · [RootLemma.lean:117](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean#L117)

The truncated ceiling and the signs in the iterated weights c(z)−v(z)ρ agree. The coefficientwise group in the source also exists for a family of additive subgroups before any filtration axioms are assumed.

<a name="gauss-filtration-finding-1"></a>

**Low · The coefficientwise Gauss groups have a wider domain.** The definition requires F to be a real filtration, while the linked substitution lemma accepts any real-indexed family of additive subgroups of R. Lean defines the Gauss groups for this general family and invokes the filtration axioms only to prove that the groups themselves form a real filtration. Define Gₜ(F,c) for any real-indexed family of additive subgroups, then state the real-filtration property under the additional axioms on F. [Knowl line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/gauss-filtration.knowl.md#L17) · [RootLemma.lean:117](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean#L117)

<a name="page-interlacing-determinant"></a>

### Interlacing as a determinant of indicators

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/interlacing-determinant.knowl.md) · [PieriCone.lean:82](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L82)

Equal all-one rows give the failed-interlacing case. Expansion down the first column retains the strict diagonal comparisons and the weak adjacent comparisons, with a minor indexing problem at k=1.

<a name="interlacing-determinant-finding-1"></a>

**Low · The final step refers to x₁ in rank one.** The induction only assumes k≥1. For k=1 there is no x₁, although the sentence justifies the conclusion by x₁≤y₀. The universally quantified adjacent-index condition in Lean is vacuous in this case. Say that every adjacent condition involving y₀ is automatic in Case 2, or state x₁≤y₀ only when k≥2. [Knowl line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/interlacing-determinant.knowl.md#L23) · [PieriCone.lean:103](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L103)

<a name="page-lattices-of-forms-are-stable"></a>

### The lattices of monomials and of divided powers are stable

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/lattices-of-forms-are-stable.knowl.md) · [Edges.lean:267](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L267)

The product of the one-letter adjoint identities gives precisely the coefficients for the divided-power generators. The scalar named in the cancellation step differs from the one produced by the stated multiplication.

<a name="lattices-of-forms-are-stable-finding-1"></a>

**Low · Cancel the common factorial actually produced.** Multiplying α! S(A)αβ = β! S(Aᵀ)βα by the two multinomial coefficients gives n! times each side of the desired identity. The text tells the reader to cancel α!β!, which need not be a common factor of n!. Cancel n! after multiplying the known identity. Equivalently, follow the source by multiplying the desired equality by α!β! and invoking Fock adjointness. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/lattices-of-forms-are-stable.knowl.md#L24) · [Edges.lean:197](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L197)

<a name="page-step-map-pieri-cone-slab"></a>

### Step map, Pieri cone and degree slab

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/step-map-pieri-cone-slab.knowl.md) · [PieriCone.lean:52](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L52)

The source-column permutation, the weak upper and lower slab endpoints, and both sign-dependent adjacent cone inequalities agree. The auxiliary determinant has one unstated scalar convention.

<a name="step-map-pieri-cone-slab-finding-1"></a>

**Low · The definition includes q=0 but uses its reciprocal.** The displayed determinant is specified for every real q and uses q⁻¹. In usual real arithmetic this is undefined at q=0. In the source the totalized reciprocal of zero equals zero, so Δ₀(π)=1. Take q≠0 in the textbook definition, or explicitly set Δ₀(π)=1 to cover the full source domain. All applications use q&gt;1. [Knowl line 28](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/step-map-pieri-cone-slab.knowl.md#L28) · [PieriCone.lean:130](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L130)

<a name="page-substitution-operator"></a>

### Substitution operator of Frobenius powers of generic matrices

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/substitution-operator.knowl.md) · [FrobeniusFactors.lean:89](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean#L89)

I checked the reversed factor product separately on the two row blocks, the transposed adjugate on odd letters, and the two frame changes surrounding the entrywise P^d power.

<a name="substitution-operator-finding-1"></a>

**Low · Nonalgebraicity is not required of every cycle.** The remark says the twists are not algebraic in g. The axiom only prescribes a Frobenius congruence, and algebraic twists occur even within this chapter. For W=O=F₂₅, p=P=5, N=2, the identity and the entrywise fifth-power map give the two letters of a cycle. Say that a general cycle need not have polynomial twists and that the guaranteed relation among them is the congruence modulo p. [Knowl line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/substitution-operator.knowl.md#L32) · [TwistingData.lean:93](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L93)

<a name="page-sum-of-dimensions-of-deep-forms"></a>

### Few forms have only deep translates

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/sum-of-dimensions-of-deep-forms.knowl.md) · [Depth.lean:755](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Depth.lean#L755)

Restriction to monomials of cost at least d is injective, and summing the restrictions counts each monomial at most its cost. The uniform coordinate mean n/k is valid under the theorem’s assumption 0&lt;2r≤k.

<a name="sum-of-dimensions-of-deep-forms-finding-1"></a>

**Low · The divisor constant is undefined at rank zero as written.** The definition announces integer k,n,r and divides by kP, even when k=0. The source takes natural parameters and totalizes division by zero. For k=0 its second summand is zero, even if r is positive. Use nonnegative integer parameters and give the second summand the value zero when k=0, or explicitly specialize the displayed definition to k&gt;0. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/sum-of-dimensions-of-deep-forms.knowl.md#L15) · [Depth.lean:676](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Depth.lean#L676)

<a name="page-unipotent-points-for-deep-forms"></a>

### Points attached to unipotent matrices, and the orders of the deep variables

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/unipotent-points-for-deep-forms.knowl.md) · [Depth.lean:372](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Depth.lean#L372)

The entries in rows below r and columns at least r give A²=0. With the odd-letter inverse transpose, the negative coefficient in ε gives the asserted translation of every deep variable.

<a name="unipotent-points-for-deep-forms-finding-1"></a>

**Low · The low-power span is indexed on a page that never defines it.** The declaration lowPowerForms is assigned here, but the core defines positions, points, specialization and orders only. The actual span is displayed as Λᵢ in the spanning paragraph of “The unipotent points satisfy equations with small leading powers,” line 27. Move lowPowerForms to the declaration list and references on the low-power-equations page, or define Λᵢ and link the spanning argument here. [Knowl line 10](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/unipotent-points-for-deep-forms.knowl.md#L10) · [Depth.lean:278](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Depth.lean#L278)

<a name="page-volume-of-pieri-cone-in-slab"></a>

### Volume of the Pieri cone in a slab

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/volume-of-pieri-cone-in-slab.knowl.md) · [PieriCone.lean:499](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L499)

For k≥1 the triangular coordinate map has diagonal (q^(b+1)−1)/(q−1), and the telescoping sum preserves total degree. The calibration proof uses coordinates and a division that are undefined at the allowed rank zero.

<a name="volume-of-pieri-cone-in-slab-finding-1"></a>

**Low · Handle the zero-dimensional case before dividing by k.** The proof uses the cube \[0,1/k\]^k and the last coordinate β_{k−1} with k≥0. Neither 1/k nor the last coordinate is defined for k=0 in ordinary notation. Lean’s empty-index formulation covers this case. Dispose of k=0 first. The cone and Ω are the entire one-point ambient space, the product is empty and equals one, and the volume identity follows for any slab. Then run the cube and triangular-map argument for k≥1. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/volume-of-pieri-cone-in-slab.knowl.md#L24) · [PieriCone.lean:427](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L427)

## Other knowls checked

<a name="page-averaging-map"></a>

### The averaging map

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/averaging-map.knowl.md) · [AveragingMap.lean:579](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/AveragingMap.lean#L579)

The degree inequality gives D+k&lt;q for the individual averages. I checked both uses of the row-weight cutoff and the induction from the empty average, which supplies the factor p^(N c₀).

<a name="page-bounded-defect-dimension-by-lattice-points"></a>

### Forms of bounded defect are counted by flags and lattice points

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/bounded-defect-dimension-by-lattice-points.knowl.md) · [DefectCount.lean:674](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L674)

The shifted exponent 4tσ+α/m lies on the indicated grid and the recovery map gives back α. The fixed bounded convex slab has null boundary, so the normalized counts along m=qʲ give the asserted volume bound.

<a name="page-colength-of-factored-operator"></a>

### Colength of the image of the operator factored through edges

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/colength-of-factored-operator.knowl.md) · [ElementaryDivisorTheorem.lean:1080](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L1080)

The two end determinants divide w^(2|V|D)=p^(|V|D). The middle chain contributes p^(2Nc₀ times the source rank) and p^(m·#s), giving precisely the displayed coefficient 3Δ+θm. The finite-family colength definition and pushforward agree with Colength.lean.

<a name="page-conjugated-frobenius-factors-level"></a>

### Gauss level of the conjugated Frobenius factors

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/conjugated-frobenius-factors-level.knowl.md) · [FrobeniusFactors.lean:538](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean#L538)

Reduction modulo p sends the inner conjugation through the entrywise P^d-power map to the inverse of the outer frame change. Each occurring monomial has weight at least −1, so w²=p covers every required error exponent, which is at most two.

<a name="page-consequences-of-large-degree"></a>

### Numerical consequences of large degree

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/consequences-of-large-degree.knowl.md) · [ElementaryDivisorTheorem.lean:577](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L577)

I checked all six claims, including the advertised outline: q≥2⁴⁰ gives log q≥27, and for N=2ℓ the left side in item 3 is below n²≤P^ℓ. With u=Nk log q, c₀P^(2r)≤u²P^(2r)≤n and 8Nkc\*P^(2r)≤180Nk³uP^(2r)≤u⁵P^(3r)≤θn verify the two remaining estimates.

<a name="page-contraction-change-of-frame"></a>

### Change of frame for contractions of the substitution operator

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/contraction-change-of-frame.knowl.md) · [AveragingMap.lean:236](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/AveragingMap.lean#L236)

Conjugation in copy j uses the pullback by ιⱼ(g⁻¹)Xιⱼ(g). The coefficient-functional calculation gives ρₙ(g⁻¹) on the left-hand coordinate vector, and partial contraction preserves the stated copy-degree bound.

<a name="page-copy-weight"></a>

### Weight of a monomial in the copies at a copy

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/copy-weight.knowl.md) · [FrobeniusFactors.lean:116](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean#L116)

The distinguished copy contributes row weight only. On a different copy the row-minus-column weight is scaled by P^(\[j−i\])/(qP^ℓ), whose absolute-value bound yields the stated entry estimate.

<a name="page-defect-cone"></a>

### Defect cone

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/defect-cone.knowl.md) · [DefectCount.lean:130](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L130)

The inequalities range over actual adjacent row indices, with threshold h only at b=a. Nonnegativity and boundedness enter when the degree slab is imposed.

<a name="page-defect-of-monomial"></a>

### Defect of a monomial at a letter along a root

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/defect-of-monomial.knowl.md) · [TwistingData.lean:166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L166)

The exceptional positive numerator at s=i is q, while the negative numerator there is 1. The two indicator contributions combine for a=a′, leaving net weight 1 at (a,i) and zero elsewhere.

<a name="page-density-of-points-over-local-ring"></a>

### Density of unit points for forms over a local ring

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/density-of-points-over-local-ring.knowl.md) · [InvariantAverage.lean:301](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L301)

The quotient-dual argument makes F times the reduced g vanish at every residue point. At degree exactly q the pure powers xᵢ^q reduce to distinct linear monomials, so they still cannot cancel the other degree-q terms. For an infinite residue field the stated natural-cardinality bound leaves only constants.

<a name="page-dual-operator-conjugation"></a>

### Conjugation and trace of the dual operator

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/dual-operator-conjugation.knowl.md) · [InvariantAverage.lean:566](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L566)

The transpose on the generic block matrix produces conjugation of the operator by a^⊗d on the left. The trace is the coefficient of (ΣXᵢᵢ)^d multiplied by η, which yields precisely the diagonal-support and degree qualifications.

<a name="page-edge-pairing"></a>

### Edge pairing

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/edge-pairing.knowl.md) · [Edges.lean:425](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L425)

The per-letter adjoint weight contributes p^(k²fN) after rescaling. Multiplication over the N letters gives the required p^(Nc₀), and transposition commutes with the odd-letter inverse-transpose action.

<a name="page-few-further-generators"></a>

### Few further generators for the image of the pairing

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/few-further-generators.knowl.md) · [ElementaryDivisorTheorem.lean:162](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L162)

The square matrix (B−QRB)R has the Smith factorization used in the source, and only a diagonal decomposition is needed. The exceptional columns have independent reductions via the displayed dual rows, while Nakayama applied to the image of aO^E modulo G proves the span inclusion.

<a name="page-frobenius-cycle"></a>

### Frobenius cycle

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/frobenius-cycle.knowl.md) · [TwistingData.lean:76](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L76)

The residue cardinality, alternating parity, square root, and one-step congruence are precisely the cycle data. Iterating the congruence yields exponent Pⁿ, and base change sends both the embeddings and square root along the ring map.

<a name="page-halfway-forms-divisible-at-large-defect"></a>

### Forms in all halfway lattices are divisible at monomials of large defect

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/halfway-forms-divisible-at-large-defect.knowl.md) · [Edges.lean:750](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L750)

The root variables have depth difference one in both parities. The Gauss estimate and cancellation of w^m give divisibility at defect ≥3j, and transposing a Levi element gives the claimed pairing bound at defect &gt;3kc.

<a name="page-hecke-operator-factors-through-edges"></a>

### The edge Hecke operator factors through functions on edges

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/hecke-operator-factors-through-edges.knowl.md) · [ElementaryDivisorTheorem.lean:807](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L807)

The origin restriction uses the transpose of o, and adjointness moves that transpose across diag(b). After summing over the incoming coset and H, the left operator acts on the b-weighted input required in the source.

<a name="page-integral-shift-into-pieri-cone"></a>

### An integral shift into the cone of Pieri's inequalities

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/integral-shift-into-pieri-cone.knowl.md) · [DefectCount.lean:529](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L529)

The explicit shift is (P²−1)μ on even letters and zero on odd letters. The recurrence for μ gives defect −1 on the distinguished root at even letters and at most −1 there at odd letters.

<a name="page-invariant-forms-vanish-on-unbalanced-monomials"></a>

### Conjugation-invariant forms vanish on unbalanced monomials

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/invariant-forms-vanish-on-unbalanced-monomials.knowl.md) · [InvariantAverage.lean:229](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L229)

Locality makes 1+p a unit of W, and characteristic zero makes its image infinite order. For a nonzero column-minus-row weight the resulting scalar differs from one, so cancellation in the domain forces the coefficient functional to vanish.

<a name="page-large-defect-forces-divisibility"></a>

### A large defect forces a divisible coefficient

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/large-defect-forces-divisibility.knowl.md) · [RootLemma.lean:991](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean#L991)

Subtracting one third of the defect weight leaves each increment in \[1/2,1\]. Choosing the least violating pair across all translates supplies the exact nondivisibility and common filtration level needed for the root lemma.

<a name="page-large-degree-conditions"></a>

### Size conditions of large degree

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/large-degree-conditions.knowl.md) · [ElementaryDivisorTheorem.lean:382](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L382)

The two-sided conditions on r and θ, the upper bound n⁴≤q and the factor P^(3r) in the lower bound on n are exact. The parity shift proves evenness of positive N, and the precision is 5N times k²fN.

<a name="page-large-weight-submodule"></a>

### Large weight submodule of a tensor power

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/large-weight-submodule.knowl.md) · [InvariantAverage.lean:391](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L391)

The sum of Schur orbits is over the basis tensors of strictly larger weight. Spanning by group points gives stability in two applications, and finite generation plus torsion-freeness gives freeness over the stated valuation domain.

<a name="page-least-height-term-at-a-flag"></a>

### A term of least height occurs at a flag and has nonpositive defects

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/least-height-term-at-a-flag.knowl.md) · [DefectCount.lean:455](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L455)

For a right coset representative x one writes g=yx with the Iwahori element on the left. Triangularity preserves the coefficient of a least-height exponent up to a scalar, and each same-block root subgroup keeps all translates in the Levi orbit.

<a name="page-levels-of-substitution-operator"></a>

### Filtration levels of the entries of a substitution operator

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/levels-of-substitution-operator.knowl.md) · [FrobeniusFactors.lean:353](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean#L353)

The product loses (m+1)u, while a cofactor in row b uses all other rows and changes the sign of its potential. Taking degree n in each of N letters gives the displayed loss, and the negative weight on one copy recovers the degree bound.

<a name="page-levi-points-span-schur-algebra"></a>

### Points of a Levi subgroup span its Schur algebra

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/levi-points-span-schur-algebra.knowl.md) · [InvariantAverage.lean:628](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L628)

The homogeneous determinant has degree k and takes value one at the identity. Evaluating at an arbitrary array b with unit block determinant yields the tensor of the transposed block part of b, exactly the group-point image needed in the density argument.

<a name="page-maps-of-cycle-kill-maximal-ideal"></a>

### The maps of a Frobenius cycle send the maximal ideal into pR

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/maps-of-cycle-kill-maximal-ideal.knowl.md) · [TwistingData.lean:228](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L228)

The q-th power congruence factors through the unit ιₛ(1−y^(q−1)). The upper- and lower-triangular conditions have opposite directions in odd and even letters because the odd matrix uses the inverse transpose.

<a name="page-number-of-flags-bound"></a>

### Parahoric index times the number of flags of the Levi subgroup

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/number-of-flags-bound.knowl.md) · [DefectCount.lean:869](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/DefectCount.lean#L869)

The two subgroup inclusions give the Iwahori-index bound. The finite-field GL order is the product qⁱ(q^(i+1)−1), which divided by the lower-triangular count yields the displayed product even for a general local ring of that residue size.

<a name="page-origin-functions-summand-of-small-colength"></a>

### Origin functions form a direct summand in which integral functions have small colength

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/origin-functions-summand-of-small-colength.knowl.md) · [Edges.lean:612](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L612)

The inverse cosets give γ=u gₑ with u parahoric. The reduction of each column for which tᵢ does not divide w^δ lies in the depth-(δ+1) subspace, yielding the determinant exponent after summing over 0≤δ&lt;x.

<a name="page-pairing-map-and-near-inverse"></a>

### The pairing map on functions on edges and its near inverse

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/pairing-map-and-near-inverse.knowl.md) · [ElementaryDivisorTheorem.lean:958](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean#L958)

The transitions cancel in each edge block, leaving diag(b) Av diag(b′). The identity case returns p^(Nc₀)(R′Q′) transposed, and the edge-pairing congruence contributes the second factor p^(Nc₀).

<a name="page-parahoric-preserves-halfway-lattice"></a>

### The stabiliser of an edge preserves its halfway lattice

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/parahoric-preserves-halfway-lattice.knowl.md) · [Edges.lean:323](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Edges.lean#L323)

The only off-block entries needing a factor of w are upper-right for even letters and lower-left for odd letters after inverse transpose. Block-diagonal elements commute with each letter’s diagonal scaling, so their tensor powers do as well.

<a name="page-partial-average"></a>

### Contraction of the substitution operator by linear forms. Partial averages

Source checked · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/partial-average.knowl.md) · [AveragingMap.lean:457](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/AveragingMap.lean#L457)

Contracting all copies except j leaves the j-th monomial intact. Evaluation of each generic matrix at the identity sends each Frobenius factor to the identity and makes the empty partial average p^(N c₀) times the identity.

<a name="page-points-satisfy-low-power-equations"></a>

### The unipotent points satisfy equations with small leading powers

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/points-satisfy-low-power-equations.knowl.md) · [Depth.lean:531](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/Depth.lean#L531)

In each nonzero position column the determinant monomials distinguish the exponents P^J even when the corresponding letters coincide modulo N. The pivot for column zero and the test by coordinate unit vectors then give the spanning and injectivity claims.

<a name="page-root-data"></a>

### Root data: the SL2 of a root and the auxiliary substitution

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/root-data.knowl.md) · [RootLemma.lean:212](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean#L212)

The signed swap-transvection and both cross terms agree in each parity. The pole weight is qPₛ at Xₛ and the exceptional zero weight is q at Yᵢ, giving the stated defect formula.

<a name="page-root-lemma"></a>

### Root lemma: an extreme term has nonpositive defect

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/root-lemma.knowl.md) · [RootLemma.lean:942](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean#L942)

The zero count gives qν≤d, which yields nonpositive defect with the stated normalization. In characteristic p the square root w vanishes in the field and the coefficient hypothesis reduces to a nonzero coefficient at l=0.

<a name="page-schur-algebra-of-levi"></a>

### Schur algebra of a Levi subgroup and the operator dual to a polynomial

Source checked · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/schur-algebra-of-levi.knowl.md) · [InvariantAverage.lean:357](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/InvariantAverage.lean#L357)

The generic (i,j) entry is Xⱼᵢ on a common block. Consequently the monomial’s row indices are the input tensor indices, and evaluating the entries at a transposed Levi point gives its ordinary tensor power.

<a name="page-signed-count-of-positive-steps"></a>

### Signed count of permutations with positive steps

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/signed-count-of-positive-steps.knowl.md) · [PieriCone.lean:250](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L250)

Reindexing multiplies adjacent determinants by signs that cancel around the cycle. A point with positive steps in the cone has strictly decreasing sorted blocks, which justifies counting at most one sorting family even when the original coordinates have ties.

<a name="page-stepanov-count"></a>

### Stepanov's count at the residue classes of a local ring

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/stepanov-count.knowl.md) · [RootLemma.lean:61](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean#L61)

Distinct residue classes give lifts with unit differences after any ring homomorphism. The coprime monic factors have product of degree Eq even over a target ring with zero divisors, and the infinite-field convention makes its case immediate.

<a name="page-substitution-operator-conjugation"></a>

### Conjugating the factors conjugates the substitution operator

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/substitution-operator-conjugation.knowl.md) · [FrobeniusFactors.lean:233](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean#L233)

For an odd letter the identity B adj(AMB) A=adj(M) gives the required order after transposition. Block diagonality then ensures the left factor only combines rows with the same product length.

<a name="page-substitution-respects-gauss-filtration"></a>

### Substitution respects weights, with a gain on the difference

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/substitution-respects-gauss-filtration.knowl.md) · [RootLemma.lean:159](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean#L159)

Only the target filtration needs its multiplicative and decreasing axioms. Disjoint monomial support treats addition, and the displayed product difference preserves the extra 1/20 on one factor.

<a name="page-translate-conditions"></a>

### Coefficient conditions on all Levi translates. Deep forms

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/translate-conditions.knowl.md) · [TwistingData.lean:174](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L174)

The Levi conditions quantify over every group element and every bad exponent. An exponent is bad for defect if the inequality is strict at some letter, and the deep-forms condition uses the opposite strict inequality with the full group.

<a name="page-twisted-action"></a>

### Twisted action of GL_k(W) on forms

Source checked · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/twisted-action.knowl.md) · [TwistingData.lean:142](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/TwistingData.lean#L142)

The action uses columns of gₛ in the variable substitution. Expanding one monomial in each letter gives the specified Kronecker product on column coefficient vectors and commutes with change of coefficient ring.

<a name="page-volume-of-cone-in-slab-signed-sum"></a>

### Share of the Pieri cone in the slab as a signed sum

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/volume-of-cone-in-slab-signed-sum.knowl.md) · [PieriCone.lean:366](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/PieriCone.lean#L366)

The pullback hypothesis makes the positive-step sets in the signed identity measurable, and the slab bounds their volume. Counting product permutations cancels (k!)^m and leaves exactly the factor |Δq(1)|/k!.

<a name="page-weight-and-defect"></a>

### Weight of a monomial in the copies against the defect of a row

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/weight-and-defect.knowl.md) · [FrobeniusFactors.lean:736](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/FrobeniusFactors.lean#L736)

I checked all four parity and root-row cases left open in the author handoff. With j=i+ℓ the positive deep member gives P^(1+\[s−1−j\])/q and the shallow member gives −P^(\[s−j\])/q in either parity, followed by the ±½ estimates and the bound 3kc.

<a name="page-weight-and-defect-in-one-copy"></a>

### Weight and defect in one copy

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/weight-and-defect-in-one-copy.knowl.md) · [AveragingMap.lean:381](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/AveragingMap.lean#L381)

A coefficient surviving modulo wᶜ comes from a monomial whose other copies survive their functionals. Levi invariance balances their row and column weights, leaving the j-th row weight divided by P^ℓ even when the frame g is arbitrary.

<a name="page-zeros-against-degree"></a>

### Zeros against degree for the auxiliary polynomial

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/upper-elementary-divisors/zeros-against-degree.knowl.md) · [RootLemma.lean:873](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors/RootLemma.lean#L873)

For Yₛ with s≠i the two errors after translation are E_(N+\[s−i\])Xₛ and −εₛ E_\[s−i\]Yₛ, with the same overall sign. The merged exponents at i give the degree bound, a surviving top coefficient, and vanishing for every power below ν after shifting.
