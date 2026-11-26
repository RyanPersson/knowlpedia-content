# spanning-unfolding-b

This area contains 12 individual knowls. The review records 7 comments.

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Knowls with comments

<a name="page-filling-data"></a>

### Filling data

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-data.knowl.md) · [Setup.lean:58](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L58)

The field, level, splitting, disjoint chosen places, freeness and size conditions agree. The auxiliary lattice Gram matrix is defined over every commutative ring, but its stated basis-change explanation requires invertibility.

<a name="filling-data-finding-1"></a>

**High · The lattice change of basis does not exist over every ring.** The description uses x_(k₀)/π̄ + z/N for arbitrary R, although π is a finite idele and N may be zero in R. Over R = 𝔽_N the rational middle form has a radical at z, whereas the lattice middle form has an invertible block with rows (0,−1) and (−1,0) on the distinguished coordinate and z. They cannot be related by a basis change there. Define the universal matrix by its distinguished block with rows (0,−1) and (−1,−N) and identity on the other coordinates. Explain the basis change over the finite adeles, or over a ring with a unit π satisfying ππ̄ = N. [Knowl line 51](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-data.knowl.md#L51) · [Basic.lean:599](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L599)

<a name="page-class-cutoff"></a>

### Class cutoff and reduced points

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/class-cutoff.knowl.md) · [Setup.lean:648](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L648)

The rational Gram–Schmidt entry has scale σ(fₐ)/σ(f_b), and the chosen cutoff for the subgroup fixing the frame really is multiplied by the indicator of the reduced points.

<a name="class-cutoff-finding-1"></a>

**Medium · State the hypotheses for the full-group cutoff.** The remark presents the full-group orbit-sum property in the context of an arbitrary filling datum and points to a declaration named isCutoff_classCutoff, which does not occur in the source. The actual theorem tsum_classCutoff_eq_one assumes a primitive 5040th root of unity in E and admissibility of S. Keep the unconditional construction, state both additional hypotheses for the orbit-sum property, and point to tsum_classCutoff_eq_one and measurable_classCutoff in Packing.lean. [Knowl line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/class-cutoff.knowl.md#L31) · [Packing.lean:134](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Packing.lean#L134)

<a name="page-filling-constants"></a>

### Constants of a filling datum

Correction recorded · notation · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-constants.knowl.md) · [Setup.lean:260](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L260)

I checked the exponents d = ϱ(ϱ+k) and 2d+ϱ in the algebraic covolume formula, the powers of the discriminant and finite volume, and the factors in both second moments.

<a name="filling-constants-finding-1"></a>

**Medium · Qualify the interpretation as a covolume.** The formula defines a positive constant for every filling datum, but the cited covolume_classUnipotent declaration does not exist. The source identifies the number with a covolume using the product of the specified Bessel Haar measures, for admissible S over E containing a primitive 5040th root of unity. Add those two hypotheses and the measure normalization to the geometric interpretation. Cite lintegral_classCutoff_eq_unipotentCovolume, together with the fundamental-domain measure identity at line 324 of CutoffIntegral.lean. [Knowl line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-constants.knowl.md#L35) · [CutoffIntegral.lean:728](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/CutoffIntegral.lean#L728)

<a name="page-filling-unitary-groups"></a>

### Unitary groups of a filling datum and the maps between them

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-unitary-groups.knowl.md) · [Setup.lean:355](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L355)

Both Dᵥ⁻¹Φᵥ(γ)Dᵥ and B⁻¹γB have the correct conjugation direction. The last claim about general changes of scalar ring is stronger than the map used to construct them.

<a name="filling-unitary-groups-finding-1"></a>

**Medium · A ring map of unitary groups must respect the involutions.** Mapping the entries of J correctly is insufficient. For the identity ring map from ℂ with complex conjugation to ℂ with trivial involution, multiplying one x-coordinate by i is unitary in the source and changes its norm coefficient to −1 in the target. Require f(star x) = star(f(x)) for every x before asserting that entrywise f induces a homomorphism G(R) → G(R′). Keep the assertion about J itself for arbitrary ring homomorphisms. [Knowl line 47](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-unitary-groups.knowl.md#L47) · [CongruenceSubgroups.lean:351](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/CongruenceSubgroups.lean#L351)

<a name="page-unipotent-character-agreement-stability"></a>

### Unipotent character, agreeing residues, stable sets and terms of a link

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability.knowl.md) · [Setup.lean:737](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L737)

The sign of ψ_f, the shift by −1/(Mϖ), both sides of the residue agreement relation and the nonzero-discriminant filter on the link all agree with the declarations.

<a name="unipotent-character-agreement-stability-finding-1"></a>

**Medium · Multiplicativity on the Bessel subgroup is not exclusive.** The cited lemma proves additivity of the simple-root sum for two elements of the Bessel subgroup. The word “only” adds a false exclusivity claim. On the scalar subgroup {I,−I} every simple-root sum is zero, so the character is multiplicative there as well, even though −I fails the frame unitriangularity condition. Say that the function restricts to a character on the Bessel subgroup, where the simple-root sum is additive. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability.knowl.md#L27) · [FloorGroups.lean:912](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorGroups.lean#L912)

<a name="page-filling-admissible"></a>

### Admissible filling datum (standing hypotheses)

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-admissible.knowl.md) · [Setup.lean:501](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L501)

All nine numbered conditions match the structure fields, including the relative index inside the standard stabilizer and the square on cov_U Λ / |I|.

<a name="filling-admissible-finding-1"></a>

**Low · Condition 6 also involves the rank-r mass and the local degrees.** The remark singles out condition 9 as the only such comparison. For condition 6 the source computes the main-to-identity ratio with deg · mass_r in the denominator, and deg is the product of the local Bessel degrees. The linked admissibility page is also absent in the snapshot. Say specifically that condition 9 compares the scaled Siegel constant with the covolume and open-cell factors. Cite scaledSiegelConst_le at line 539 and the admissibility instance at line 743 of FillingAdmissible.lean until a corresponding knowl exists. [Knowl line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-admissible.knowl.md#L35) · [FillingAdmissible.lean:604](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FillingAdmissible.lean#L604)

<a name="page-frame-products-at-infinity"></a>

### Frame products of a rational term at the infinite places

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/frame-products-at-infinity.knowl.md) · [Setup.lean:707](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L707)

The determinant identity holds for an arbitrary map of the indexing set, including repeated indices. The column- and row-scaling factors multiply to N^(−|m|) times the product of the squared κᵥ powers.

<a name="frame-products-at-infinity-finding-1"></a>

**Low · Group the denominator inside the product in the proof.** The theorem display puts N in every factor. The final product of the proof is printed as ∏ᵢ κᵥ^(2(ϱ−e(i)))/N, which can be read as dividing once. For two distinct indices the denominator is N². Use the product of the parenthesized quotients as in the statement, or write N^(−|m|) times the product of the powers of κᵥ. [Knowl line 28](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/frame-products-at-infinity.knowl.md#L28) · [Setup.lean:710](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L710)

## Other knowls checked

<a name="page-box-partition-of-unity"></a>

### Box partition of unity for a class

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/box-partition-of-unity.knowl.md) · [Setup.lean:434](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L434)

The support uses the box for the moved frame yᵥ⁻¹fₐ. The weight is normalized on the right cosets U⁰_c(M)γ and acts on y by left multiplication, as in the defining orbit sum.

<a name="page-class-unipotent-discrete"></a>

### Discreteness of the class unipotent groups and existence of cutoffs

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/class-unipotent-discrete.knowl.md) · [Setup.lean:622](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L622)

The finite-place compact set is conjugated by Bh_c and the archimedean entry is multiplied by the inverse scale ratio. The matrix-space argument gives discreteness, and injectivity transports the counting-measure cutoff from the image back to any subgroup.

<a name="page-filling-amplitude"></a>

### Bessel kernel, amplitude of a term and amplitude sums

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-amplitude.knowl.md) · [Setup.lean:669](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L669)

The second tensor coordinate is conjugated after evaluating at γ∞⁻¹y. The amplitude uses the real value of the product of the cutoffs, while the majorant uses the extended nonnegative product, and the sum is over T intersected with the block.

<a name="page-filling-classes-and-terms"></a>

### Classes, terms over a block, and the unipotent groups of a class

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-classes-and-terms.knowl.md) · [Setup.lean:382](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L382)

The representative occurs with its inverse on the left and the second representative on the right. The last two leading minors enter with coefficients 1 and −N², and the level-M unipotent group is cut out after the same conjugation.

<a name="page-filling-level-and-reduction"></a>

### Lattice stabiliser, reduction and principal level of a filling datum

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-b/filling-level-and-reduction.knowl.md) · [Setup.lean:205](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Setup.lean#L205)

K requires integral entries for the matrix and its inverse. The principal level is the kernel embedded in the finite adelic group, and the image of a subgroup A is taken after intersection with K.
