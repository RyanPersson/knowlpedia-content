# spanning-core

This area contains 52 individual knowls and a chapter page. The review records 38 comments. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports/spanning-core.md)

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Chapter page

<a name="page-spanning-core"></a>

### Spanning: the second moment, equal multiplicities, and Bessel systems

Correction recorded · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core.knowl.md) · [SpanningTheorem.lean:339](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L339)

The spread parameter is (3/2)/(8b²), and the Gram section is indeed defined on the positive-discriminant cell. The singular-minor hypothesis and the description of the ordinary matrix blocks require corrections.

<a name="spanning-core-finding-1"></a>

**High · The nonzero vector belongs to the source of each rectangular matrix.** For each nonzero v in kᵐ the theorem bounds both the π-stabilizer mass of A₀v and the inverse-transpose-stabilizer mass of A₁v. Either image can be zero. If A₀=0 then every determinant vanishes, even when the action is transitive on the ambient nonzero vectors and their stabilizers have small mass. Quantify over v in kᵐ with v≠0 and state the two stabilizer bounds on its respective images, including a zero image. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core.knowl.md#L26) · [PositiveType.lean:156](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/PositiveType.lean#L156)

<a name="spanning-core-finding-2"></a>

**High · The common Hecke algebra ranges over spaces with the fixed finite local model.** The product is indexed by pointed hermitian spaces having Gram matrix 1 at every finite place and the prescribed diagonal signs at infinity, as defined in Lib/Adelic/Unitary/Defs.lean:498. Rank alone permits other finite local classes. The single common group-algebra element must also preserve principal-level fixed vectors in every representation. Specify the common finite adelic model and varying signs, together with a spherical representative preserving principal-level invariants. [Knowl line 41](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core.knowl.md#L41) · [HeckeEigensystems.lean:184](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/HeckeEigensystems.lean#L184)

<a name="spanning-core-finding-3"></a>

**Medium · The matrix blocks are the conjugates of the normalized amplitude sums.** With the convention declared at line 15, the sum is the pairing ⟨sPe_y,Pe_x⟩. The row-x, column-y entry of P\* s P is the conjugate. Squared norms in the next estimate hide this distinction, but the two complex matrices need not agree. Insert “complex conjugates of” before “the amplitude sums”, or write the actual Petersson-pairing identity. [Knowl line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core.knowl.md#L32) · [Moments.lean:92](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L92)

## Knowls with comments

<a name="page-hecke-operators-at-split-places"></a>

### Hecke operators at split places off the level

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hecke-operators-at-split-places.knowl.md) · [HeckeEigensystems.lean:273](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/HeckeEigensystems.lean#L273)

Off the level the finite sum over local cosets preserves the principal level by sphericity. Elsewhere the project defines T_x to be zero. There is a second zero convention at split places for degrees beyond the rank.

<a name="hecke-operators-at-split-places-finding-1"></a>

**High · Define the split Hecke operators for i greater than the rank.** The diagonal matrix diag(ϖ1_i,1_(r−i)) belongs to GL_r only for 0 ≤ i ≤ r. The page uses it to define T_(w,i) for every i≥0. The source’s basic double coset is empty for i&gt;r, so T_(w,i)=0 at split off-level places as well. The eigensystem index ranges over all natural numbers. Use the displayed double coset for 0 ≤ i ≤ r, and explicitly set T_(w,i)=0 for i&gt;r. State that its restrictions are taken on forms of the pointed spaces with the standard finite model. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hecke-operators-at-split-places.knowl.md#L14) · [SplitHecke.lean:500](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/SplitHecke.lean#L500)

<a name="page-spherical-hecke-algebra-away-from-the-level"></a>

### Spherical Hecke algebra away from the level

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level.knowl.md) · [HeckeEigensystems.lean:184](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/HeckeEigensystems.lean#L184)

The universal-level criterion does follow from factoring each level element into a supported element and an integral off-level element. A single spherical group-algebra element supplies every member of the resulting family.

<a name="spherical-hecke-algebra-away-from-the-level-finding-1"></a>

**High · Correct the indexing family of the spherical Hecke algebra.** The page takes the family over all rank-r Hermitian spaces. The product defining the algebra actually ranges over Space E RowIndex s, whose objects include x with x\*Jx = 1 at each finite place and diag(s) at each infinite place. A form outside the finite local class has no coordinate of this family, and a point is needed to define the action. Define the product over all sign vectors and pointed hermitian spaces having that standard adelic model. Link that definition here so every use of the common algebra inherits the correct domain. [Knowl line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level.knowl.md#L19) · [Defs.lean:498](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L498)

<a name="page-bad-types-are-rare"></a>

### Bad types are rare

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bad-types-are-rare.knowl.md) · [SpanningTheorem.lean:244](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L244)

The coefficient calculation identifies two good tuples after reindexing the places. I checked the outside estimate at its declaration and its application with L = 9 log b and M = q₂.

<a name="bad-types-are-rare-finding-1"></a>

**Medium · Include M &gt; 0 in the quoted estimate for good tuples.** The stated general estimate omits the assumption NeZero M. If M = 0 then every field element satisfies x^M = 1, so the argument that discards at most M possible roots does not apply. The specialized application uses the positive integer q₂. State M ≥ 1 in the auxiliary estimate and mention that q₂ = (q₀d)^(s+6) is positive. [Knowl line 33](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bad-types-are-rare.knowl.md#L33) · [BadTypes.lean:230](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/BadTypes.lean#L230)

<a name="page-cut-pair-of-bessel-functions"></a>

### Cut pair of Bessel functions

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/cut-pair-of-bessel-functions.knowl.md) · [Basic.lean:987](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L987)

The support condition, threshold for a change, L² normalization, left invariance and the power 3r³f in the common majorant match. The standalone definition permits scales outside the positive range enforced by a Bessel system.

<a name="cut-pair-of-bessel-functions-finding-1"></a>

**Medium · Restore the positive-part operation before squaring.** For unrestricted real b, Lean squares the nonnegative part of (b⁻¹)^(r³f). With b = −1 and r and f odd, its error coefficient is 0, while the displayed b^(−2r³f) is 1. The scaled length also uses totalized division when b = 0. Give the coefficient as max(0,(b⁻¹)^(r³f))² with 0⁻¹ = 0, or explicitly specialize the page to b &gt; 0 and identify the larger domain of IsCutPair. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/cut-pair-of-bessel-functions.knowl.md#L24) · [Basic.lean:1001](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L1001)

<a name="page-dimension-of-the-target"></a>

### Dimension of the target

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/dimension-of-the-target.knowl.md) · [SpanningTheorem.lean:93](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L93)

The argument passes to the definite last space and counts free-level forms by class number times weight dimension, placing |G| and mass correctly. The field deg_eq supplies a different intermediate equality than the one attributed to it.

<a name="dimension-of-the-target-finding-1"></a>

**Medium · Identify the equality actually supplied by the Bessel degree field.** The outline attributes equality with the noncompact formal degree to deg_eq. That field states B.deg = weylDimensionPoly(l). SpanningTheorem.lean lines 99–101 use Harish-Chandra’s identity on the compact formal-degree side and identify the same polynomial on both sides. Start from B.deg = weylDimensionPoly(l) and apply the formal-degree formula to the all-positive parameter, whose entries give the same Weyl polynomial. [Knowl line 36](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/dimension-of-the-target.knowl.md#L36) · [LargeFunction.lean:64](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/LargeFunction.lean#L64)

<a name="page-eigensystem-parts-decompose-the-forms"></a>

### The eigensystem parts decompose the forms of principal level

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/eigensystem-parts-decompose-the-forms.knowl.md) · [HeckeEigensystems.lean:464](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/HeckeEigensystems.lean#L464)

Independence follows by shortening a relation using a coordinate that separates two eigensystems. The spectral theorem supplies spanning on a finite-dimensional subspace spherical and stable for the indicated Hecke operators.

<a name="eigensystem-parts-decompose-the-forms-finding-1"></a>

**Medium · Clarify which operators preserve the subspace.** The proof calls the subspace “invariant” in addition to being stable under the T operators, then says the hypotheses hold for principal-level forms. The library requires only simultaneous sphericity and Hecke stability. Invariance of a fixed-level space under the entire adelic representation is generally unavailable as translation changes its level. Describe a finite-dimensional subspace that is spherical at the stated places and stable under all their T operators. In the application use the pointed V underlying the principal-level forms. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/eigensystem-parts-decompose-the-forms.knowl.md#L27) · [SplitHecke.lean:348](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/SplitHecke.lean#L348)

<a name="page-equal-multiplicities-of-eigensystems"></a>

### Equality of multiplicities

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/equal-multiplicities-of-eigensystems.knowl.md) · [EqualMultiplicities.lean:372](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/EqualMultiplicities.lean#L372)

The union of the two finite eigensystem supports supplies one projector on both spaces. Its trace on good forms equals the dimension of their intersection with the selected joint eigenspace.

<a name="equal-multiplicities-of-eigensystems-finding-1"></a>

**Medium · Require the common finite adelic model in the multiplicity theorem.** Rank, archimedean signs and the gaps in the theorem body do not impose the finite local condition on V and V′. Each Lean Space carries an adelic point x with x\*Jx = 1 at every finite place. A Hermitian form whose determinant has a different local norm class cannot supply such an x, and the fixed finite group and principal level in this comparison have not been identified for it. State that both spaces come with adelic bases giving the identity form at each finite place and their respective sign matrices at each infinite place. Link the pointed-space definition before comparing multiplicities. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/equal-multiplicities-of-eigensystems.knowl.md#L15) · [Defs.lean:498](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L498)

<a name="page-equal-traces-on-good-forms"></a>

### Equal traces of Hecke operators on good forms

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/equal-traces-on-good-forms.knowl.md) · [EqualMultiplicities.lean:270](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/EqualMultiplicities.lean#L270)

The primitive label at one chosen split place gives the stated cuspidal test function. The trace comparison uses the gap 500r³+10r⁵, and equality at power zero supplies the common dimension for the characteristic-polynomial argument.

<a name="equal-traces-on-good-forms-finding-1"></a>

**Medium · State the finite-place hypothesis of trace comparison.** The summary says the spaces differ only at the real places, but the theorem body specifies only rank and archimedean signs. The cited comparison theorem takes two pointed spaces whose finite adelic forms are both identified with the identity. That assumption makes the same J_M, test function and Hecke operator available on the two sides. Require the pointed spaces of the project with x\*Jx equal to 1 at every finite place and diag(s) or diag(s′) at every infinite place. Carry the condition into the quoted trace-comparison statement in Step 2. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/equal-traces-on-good-forms.knowl.md#L15) · [Defs.lean:498](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L498)

<a name="page-gram-section"></a>

### The Gram section on the open cell

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/gram-section.knowl.md) · [GramSection.lean:582](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean#L582)

The matrices Y, S, M and the identity choice off the open cell agree with the construction. The introductory domain includes pairs at which the ordinary scalar reciprocal in M is undefined.

<a name="gram-section-finding-1"></a>

**Medium · Invertibility of Z and W does not guarantee an inverse square root.** The construction purports to give M for every invertible pair. At Z = W = I, both inverse corners are one and s = 0, so the displayed δ(s⁻¹) has no ordinary complex meaning. Lean uses a total scalar inverse, and its holomorphy statement at line 179 is restricted to Ω × Ω. State the two-variable analytic construction for Z,W in Ω, where s is nonzero. To retain the larger algebraic domain, specify the convention 0⁻¹ = 0 and state the holomorphy domain explicitly. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/gram-section.knowl.md#L14) · [GramSection.lean:104](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean#L104)

<a name="page-hecke-projector-onto-an-eigensystem"></a>

### A Hecke operator projecting onto one eigensystem

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hecke-projector-onto-an-eigensystem.knowl.md) · [HeckeEigensystems.lean:318](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/HeckeEigensystems.lean#L318)

The interpolation factor acts by (d(x)−e(x))/(q(x)−e(x)) on an eigenvector with system d before applying T. The construction controls precisely F∪{q}, independent of whether q already belongs to F.

<a name="hecke-projector-onto-an-eigensystem-finding-1"></a>

**Medium · Qualify the family on which the Hecke projector is simultaneous.** The phrase “for every hermitian space V of rank r over E” is wider than the source family. The common Hecke algebra acts on forms of pointed spaces whose finite adelic bases carry their forms to the identity. The polynomial in the Hecke operators gives the claimed projection for that family. Restrict the quantifier to the pointed spaces used in the definition of the common Hecke algebra, and identify the fixed finite adelic form. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hecke-projector-onto-an-eigensystem.knowl.md#L15) · [Defs.lean:498](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L498)

<a name="page-hilbert-schmidt-norm-of-a-linear-map"></a>

### Hilbert–Schmidt norm of a linear map (finite dimension)

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map.knowl.md) · [FewTranslates.lean:65](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L65)

The six displayed identities follow from the orthonormal-basis sums, cyclicity of the trace and contractivity of the two projections. The complex trace formula is sensitive to the inner-product convention.

<a name="hilbert-schmidt-norm-of-a-linear-map-finding-1"></a>

**Medium · Specify the convention where the Hilbert–Schmidt pairing is defined.** The chapter overview uses an inner product linear in the second variable. The linked general Hilbert–Schmidt knowl gives ⟨A,B⟩ = tr(B\*A), and the linked inner-product-space definition leads to an inner product linear in the first variable. For A = 1 and B = i on ℂ, those linked conventions give −i, while the trace in Property 1 is i. State on this page that inner products here are conjugate-linear in the first variable, so ⟨A,B⟩ = tr(A\*B), and identify the opposite convention in the general Hilbert–Schmidt entry. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map.knowl.md#L18) · [FewTranslates.lean:73](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L73)

<a name="hilbert-schmidt-norm-of-a-linear-map-finding-2"></a>

**Low · Distinguish the norm from its square in the summary.** The summary describes the norm by the sum of squared lengths. For multiplication by 2 on ℂ that sum is 4 and the norm is 2. The defining display already includes the square root. Describe the norm as the square root of the sum of squared lengths, or describe the sum as the squared norm. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map.knowl.md#L5) · [FewTranslates.lean:84](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L84)

<a name="page-integral-over-the-section-orbit"></a>

### Integrals over the orbit of the Gram section are bounded by integrals over the quotient

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/integral-over-the-section-orbit.knowl.md) · [SobolevBound.lean:239](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/SobolevBound.lean#L239)

The cutoff used here is an explicit consequence of the source’s unimodular-Haar instance. The two bounds on the cutoff-weighted integral preserve the order of u and h and give the stated exponent for c &gt; 0.

<a name="integral-over-the-section-orbit-finding-1"></a>

**Medium · The fixer measure for arbitrary real c needs a nonnegative density.** The definition is stated for every real c. With k = 2 and c = −1 its displayed coefficient is −c_G, which does not define a positive measure. Lean applies ENNReal.ofReal to the entire coefficient, giving the zero measure in this example. The inequality itself assumes c &gt; 0. Use max(0,c_G c^(k−1)) as the coefficient for arbitrary c, or restrict the definition on this page to c ≥ 0. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/integral-over-the-section-orbit.knowl.md#L15) · [SobolevBound.lean:137](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/SobolevBound.lean#L137)

<a name="page-local-bounds-of-a-bessel-function"></a>

### Local bounds of a Bessel function at a real place

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/local-bounds-of-a-bessel-function.knowl.md) · [Basic.lean:938](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L938)

The Weyl element, square-root factor, head weights, exponents, and condition pϱ = qϱ = h(z,σz) agree with the normalized top form. The standalone definitions of its integrals and pairing bound allow singular inputs.

<a name="local-bounds-of-a-bessel-function-finding-1"></a>

**Medium · Specify the convention for divergent orbital integrals.** The page assigns a complex matrix to every W and measure. For the constant scalar function 1 on a group of infinite Haar measure its single coordinate diverges in ordinary integration. The source uses the coordinatewise Bochner integral, which returns zero for each nonintegrable coordinate. Require integrability of the displayed coordinate products when using an ordinary integral, or give the zero convention for each nonintegrable coordinate. In the normalized orbital integral, identify the fixed Haar measure haarU(J₁). [Knowl line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/local-bounds-of-a-bessel-function.knowl.md#L20) · [Basic.lean:890](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L890)

<a name="local-bounds-of-a-bessel-function-finding-2"></a>

**Medium · Define the pairing bound on its singular locus.** The formula is stated for every y and real degree. At y = 1 the two frames coincide, so their Gram determinant and the frame discriminant vanish. Division by the discriminant is undefined in the displayed formula, whereas Lean assigns the bound zero there. Degree zero also occurs in the declared domain. State the totalized inverse convention for these formulas, including the scaled frequencies and an empty finite index set, or restrict the ordinary formula to nonzero denominators and give the singular values separately. [Knowl line 31](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/local-bounds-of-a-bessel-function.knowl.md#L31) · [Basic.lean:881](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L881)

<a name="page-rallis-series-is-a-hecke-operator"></a>

### The series of Rallis' formula is a spherical Hecke operator

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/rallis-series-is-a-hecke-operator.knowl.md) · [EqualMultiplicities.lean:300](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/EqualMultiplicities.lean#L300)

Each scaled vacuum coefficient is the same for the two spaces. The simultaneous operator follows by closedness of a finite-dimensional image in the pointwise topology, followed by multiplication by the common residue-matrix count.

<a name="rallis-series-is-a-hecke-operator-finding-1"></a>

**Medium · Restrict the simultaneous Rallis operator to the specified spaces.** Saying only that V and V′ have rank r and signatures s,s′ allows different finite adelic Hermitian forms. The Rallis operators and the common cosets, local level and Hecke algebra in this proof use the finite adelic identity model from their chosen points. Specify pointed spaces with bases identifying their finite forms with the identity, or refer explicitly to the project definition of Space when quantifying over V,V′ and W. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/rallis-series-is-a-hecke-operator.knowl.md#L15) · [Defs.lean:498](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L498)

<a name="page-sobolev-bound-at-the-gram-section"></a>

### The L2 bound at the Gram section via Sobolev's inequality

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/sobolev-bound-at-the-gram-section.knowl.md) · [SobolevBound.lean:592](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/SobolevBound.lean#L592)

The trace constant and its 2n²-fold power agree with the library. I checked the local bound for the logarithmic derivative and the convolution weights, including the y⁻¹ and y indices that give coefficients R²X_dc.

<a name="sobolev-bound-at-the-gram-section-finding-1"></a>

**Medium · The quoted cube inequality requires 0 &lt; ε ≤ 1.** The cube estimate is described for a cube of side ε without its scale restriction. In dimension one, with one letter, Λ = 1, a one-point parameter space and f_w(x) = exp(−x) for every word, ε = 4 gives a = 1 and K = (1−exp(−8))/2 &lt; 1, although the squared corner value is 1. The application at ε = P⁻⁸ satisfies the restriction. Include 0 &lt; ε ≤ 1 in the statement of the trace estimate, and note that P ≥ 8 gives this for ε = P⁻⁸. [Knowl line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/sobolev-bound-at-the-gram-section.knowl.md#L32) · [PackingAndSobolev.lean:191](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/PackingAndSobolev.lean#L191)

<a name="sobolev-bound-at-the-gram-section-finding-2"></a>

**Low · Specify the matrix size in the scale hypothesis.** The phrase “real unitary group … of rank r” can be read as real rank. Lean uses r = 2ϱ + k + 1, the size of the matrices, and counts r⁴ letters. For instance, U(k,1) has real rank one but matrix size k + 1. Define r = 2ϱ + |κ| + 1 as the ambient complex dimension before imposing P ≥ 8r. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/sobolev-bound-at-the-gram-section.knowl.md#L15) · [SobolevBound.lean:365](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/SobolevBound.lean#L365)

<a name="page-translation-as-a-hecke-operator"></a>

### Translations off the level as Hecke operators

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/translation-as-a-hecke-operator.knowl.md) · [EqualMultiplicities.lean:69](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/EqualMultiplicities.lean#L69)

The subgroup H is open in compact K. Averaging kγ over K/H produces a single spherical group-algebra element, and dividing by \[K:H\] gives the required unaveraged matrix coefficient.

<a name="translation-as-a-hecke-operator-finding-1"></a>

**Medium · Give the domain of the universal translation claim.** The quantified “every hermitian space W of rank r” includes spaces whose finite form is not locally the identity. The source quantifies over W with a chosen adelic point that realizes the fixed G_f action and its principal level. The coset average itself is correct in that setting. Say “every pointed hermitian space W with the standard finite adelic form” and identify or link its adelic-point condition. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/translation-as-a-hecke-operator.knowl.md#L15) · [Defs.lean:498](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L498)

<a name="page-unfolding-of-the-scaled-poincare-map"></a>

### Unfolding: the blocks of P\* s P are amplitude sums

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/unfolding-of-the-scaled-poincare-map.knowl.md) · [SpanningTheorem.lean:168](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L168)

The displayed Petersson pairing and the division by ν agree with HasAmplitudeBlocks and with the scaling of both arguments. Conjugate-linearity changes how that pairing represents the actual matrix block.

<a name="unfolding-of-the-scaled-poincare-map-finding-1"></a>

**Medium · Distinguish the Petersson pairing from the matrix block.** The title describes the blocks of P\*ρ(s)P as amplitude sums. With the chapter’s inner product conjugate-linear in its first argument, the display is ⟨P\*ρ(s)P e_y,e_x⟩ = A_xy/ν. The ordinary row-x, column-y matrix entry is its complex conjugate. The source specifies this conjugation at lines 86–89. Title the page in terms of unfolded Petersson pairings, or state that the matrix blocks are the conjugates of the normalized amplitude sums. Keep the displayed pairing. [Knowl line 3](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/unfolding-of-the-scaled-poincare-map.knowl.md#L3) · [Moments.lean:92](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/Moments.lean#L92)

<a name="page-bessel-lattice-basis"></a>

### Lattice basis of the Bessel space

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bessel-lattice-basis.knowl.md) · [Basic.lean:640](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L640)

The replacement vector and the inverse change of basis give the stated zero self-pairing and both cross-pairings −1. The basis calculation requires the unit p.

<a name="bessel-lattice-basis-finding-1"></a>

**Low · Separate the middle matrix from its change-of-basis interpretation.** The opening assumption N = p p̄ with p a unit also governs the named lattice middle matrix here. Its entrywise definition accepts every scalar N, including N = 0, when the displayed matrix is still defined and the basis change may be unavailable. Define the middle matrix for arbitrary N. Impose the unit norm factorization for the basis and its Gram identity. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bessel-lattice-basis.knowl.md#L22) · [Basic.lean:599](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L599)

<a name="page-bessel-length"></a>

### Bessel length of a point of the real unitary group

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bessel-length.knowl.md) · [Basic.lean:66](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L66)

Right translation in S gives invariance of the infimum. The actual Bessel decomposition lemma permits the required factorization over ℂ with N = 1, and the two norm inequalities squeeze the length at each point.

<a name="bessel-length-finding-1"></a>

**Low · Include both orders of the hyperbolic pairing.** The phrase “all other products of basis vectors vanish” includes h(eᵢ\*,eᵢ), although this is 1 by Hermitian symmetry and by the second identity block of the source Gram matrix. Give h(eₐ,eᵦ\*) = h(eᵦ\*,eₐ) = δₐᵦ, or specify that the listed entries determine the others by Hermitian symmetry before declaring the remaining entries zero. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bessel-length.knowl.md#L14) · [BesselGroups.lean:147](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Groups/BesselGroups.lean#L147)

<a name="page-bessel-length-versus-orthogonal-frame"></a>

### The Bessel length is comparable to the lengths of the orthogonal frame

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bessel-length-versus-orthogonal-frame.knowl.md) · [Basic.lean:481](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L481)

Taking the dual columns J oₐ/‖oₐ‖² gives the required Kronecker pairings and zero Hermitian Gram matrix. The triangular dual estimate obtains the same lower bound by pairing with V₂ϱ₋ₐ.

<a name="bessel-length-versus-orthogonal-frame-finding-1"></a>

**Low · Correct the namespace of the dual-column lemma.** The dependency named New.exists_mul_unipotentOf_dualCols_eq is declared in New.RealPlace. The actual lemma has exactly the dual-pairing and isotropic-column hypotheses used here. Cite New.RealPlace.exists_mul_unipotentOf_dualCols_eq and point to Lib/DiscreteSeries/Bessel/Basic.lean. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bessel-length-versus-orthogonal-frame.knowl.md#L27) · [Basic.lean:543](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/Basic.lean#L543)

<a name="page-bounds-for-the-gram-section"></a>

### Polynomial bounds for the Gram section and its derivative

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bounds-for-the-gram-section.knowl.md) · [GramSection.lean:453](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean#L453)

The value, perturbation and derivative bounds give the stated exponents 12, 18 and 25. The Schwarz estimate controls differences from the centre and suffices for the derivative estimate.

<a name="bounds-for-the-gram-section-finding-1"></a>

**Low · The Schwarz estimate compares with the centre only.** The cited inequality fixes the second point at Z. It does not itself prove the stated two-point Lipschitz estimate with the same constant on a neighbourhood. Lean takes the pointwise difference estimate directly to the derivative in GramSection.lean lines 312–318. Use the estimate for the difference from Z and pass to a directional difference quotient at Z. Real differentiability on the cell then gives the claimed operator norm. [Knowl line 34](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bounds-for-the-gram-section.knowl.md#L34) · [HolomorphicIntegrals.lean:343](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/HolomorphicIntegrals.lean#L343)

<a name="page-coordinates-on-frames-over-a-gram-matrix"></a>

### Coordinates on the tuples with given products with the frame

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/coordinates-on-frames-over-a-gram-matrix.knowl.md) · [MeanValue.lean:346](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/MeanValue.lean#L346)

The unipotent and polar coordinate formulas give the factor 2^(−ϱ)π^k/(k−1)! and the two Jacobians leave |det Z|^(2(k−1)). Conjugation by the compact factor preserves the unipotent measure as required for inversion.

<a name="coordinates-on-frames-over-a-gram-matrix-finding-1"></a>

**Low · The integral uses the dual tuple outside its stated domain.** The definition at line 17 gives y(T) only for 1 + Tₙₙ ≥ 0. Parts 1 and 2 integrate over all Hermitian coordinates, hence call y(T) or y(T′) on a full half-space where it has not been defined. The density is zero there, and Lean defines the tuple everywhere with its total real square root. Restrict each t-integral to the set where the corresponding sphere argument is positive, or define the root as √max(0,1 + Tₙₙ) for all Hermitian T and reserve the Gram identity for 1 + Tₙₙ ≥ 0. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/coordinates-on-frames-over-a-gram-matrix.knowl.md#L27) · [MeanValue.lean:132](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/MeanValue.lean#L132)

<a name="page-frame-discriminant"></a>

### The frame discriminant and the Gram determinant of two frames

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/frame-discriminant.knowl.md) · [Basic.lean:784](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L784)

Splitting the two exceptional rows produces the negative adjugate term. Exchanging the two column blocks contributes (−1)^(ϱ+1), with the corner adjugate equal to the order-ϱ leading minor.

<a name="frame-discriminant-finding-1"></a>

**Low · Allow the exceptional Gram entry to vanish.** The theorem assumes only N̄ = N. At N = 0 the block C is zero, although the page calls −N a nonzero entry. Say that all entries of C vanish except possibly its bottom-right entry, which is −N. [Knowl line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/frame-discriminant.knowl.md#L23) · [Basic.lean:758](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L758)

<a name="page-gram-section-is-a-section"></a>

### The Gram section is a measurable section of the frame Gram matrix

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/gram-section-is-a-section.knowl.md) · [GramSection.lean:533](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean#L533)

The action on the frame, the block congruence, holomorphy on Ω × Ω and piecewise measurability follow the source. The entrywise polynomial verification is correctly identified as the omitted step of the outline.

<a name="gram-section-is-a-section-finding-1"></a>

**Low · The description of the block columns drops Δ.** The displayed blocks are correct, but the following parenthesis identifies the second column families without their common right factor Δ. In the ambient basis they are Fᵛ(Z\*)Δ and F(Z\*)⁻¹Δ. The distinction matters for the last column whenever ν(Z) differs from one. Include Δ in both descriptions, or say that the two unscaled families have equal Gram matrices after cancelling the common invertible column scaling. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/gram-section-is-a-section.knowl.md#L30) · [GramSection.lean:542](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean#L542)

<a name="page-hecke-action-on-good-forms"></a>

### Action of the Hecke algebra on good forms

Correction recorded · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hecke-action-on-good-forms.knowl.md) · [HeckeEigensystems.lean:410](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/HeckeEigensystems.lean#L410)

Residue lifts are supported at the chosen places and their conjugates. This commutation gives stability of the idempotent image and of the joint eigenspaces, and the lift preserves the level in every adelic representation.

<a name="hecke-action-on-good-forms-finding-1"></a>

**Low · Identify the structure on V used for the action.** The fixed G_f action on forms and the lift of the chosen finite group refer to the adelic point of V. A rank-r Hermitian form alone, as in the opening, does not carry that identification in the development. Introduce V as a pointed hermitian space in the sense of the project, with the standard model at the finite places, and link the definition. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hecke-action-on-good-forms.knowl.md#L14) · [Defs.lean:498](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L498)

<a name="page-hecke-eigensystem-part"></a>

### Part of the forms with a given Hecke eigensystem

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hecke-eigensystem-part.knowl.md) · [HeckeEigensystems.lean:287](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Multiplicities/HeckeEigensystems.lean#L287)

The intersection includes every pair (w,i) and forces the eigenvalue to vanish off the specified split places on a nonzero part. The degree-i coefficient of the Hecke polynomial is (−X)^i q^(i choose 2).

<a name="hecke-eigensystem-part-finding-1"></a>

**Low · Specify the underlying pointed space of principal-level forms.** The subspace uses the fixed adelic Hecke operators of D. These are defined on forms of a project Space, including its point identifying every finite local form with the identity, whereas the opening states only that V is a rank-r Hermitian space. Qualify V as a pointed space with the standard finite adelic model, or link that precise definition alongside principal-level forms. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/hecke-eigensystem-part.knowl.md#L14) · [Defs.lean:498](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L498)

<a name="page-mean-value-inequality-over-the-gram-section"></a>

### The mean value inequality over the Gram matrix of two frames

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/mean-value-inequality-over-the-gram-section.knowl.md) · [MeanValue.lean:588](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/MeanValue.lean#L588)

The fibre criterion uses continuity at t₀ where the sphere argument is positive. The section density and the compact-dual Haar normalization give the stated constant after convolution on the right.

<a name="mean-value-inequality-over-the-gram-section-finding-1"></a>

**Low · The quoted convolution comparison requires an s-finite measure.** The general theorem as paraphrased says it applies to any measure on G₁ with the stated fibre bound. Its declaration assumes the measure is s-finite, meaning a countable sum of finite measures. The specific section measure λ has this property by MeanValue.lean line 456. Qualify the library theorem by s-finiteness and state that λ has it as the pushforward of the density-weighted product used in its definition. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/mean-value-inequality-over-the-gram-section.knowl.md#L26) · [FrameFibre.lean:293](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bessel/FrameFibre.lean#L293)

<a name="page-near-isometry-from-small-defect"></a>

### A small defect gives a near isometry

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/near-isometry-from-small-defect.knowl.md) · [FewTranslates.lean:157](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L157)

Taking the real part of the Hilbert–Schmidt pairing of pr_U with A\*A−1 gives exactly the norm deficit. The proof uses ε ≥ 0 when taking the square root of the defect bound.

<a name="near-isometry-from-small-defect-finding-1"></a>

**Low · Carry the nonnegative error into the conditional summary.** The body correctly assumes ε ≥ 0. The stand-alone summary also admits ε = −1 and A = 1 on ℂ, for which the defect vanishes but the alleged near-isometry inequality on U = 0 would give 1 ≤ 0. Start the summary with “For ε ≥ 0” or replace the asserted error in an unrestricted version by |ε|. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/near-isometry-from-small-defect.knowl.md#L5) · [FewTranslates.lean:157](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L157)

<a name="page-open-cell-of-frame-matrices"></a>

### Open cell of frame Gram matrices

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/open-cell-of-frame-matrices.knowl.md) · [GramSection.lean:58](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean#L58)

The cofactor identity gives the positive-discriminant criterion, also in the singular case. The boundedness definition uses the positive real root of the signed corner expression.

<a name="open-cell-of-frame-matrices-finding-1"></a>

**Low · The choice of square root affects boundedness in the cell.** The page specifies ν² and later requires 1/ν ≤ P. On the cell ν² is positive, but the displayed equation permits either sign and a negative choice can satisfy the upper bound spuriously. Off the cell the signed expression can itself be negative. Define q(Z) = 1 − |ξ(Z)|² where Z is invertible, and put ν(Z) = √q(Z) &gt; 0 on Ω. Use q(Z) in the discriminant identity for general invertible Z. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/open-cell-of-frame-matrices.knowl.md#L14) · [GramSection.lean:75](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean#L75)

<a name="page-schur-bound-for-a-bessel-function"></a>

### Schur bound for a Bessel function and its derivatives

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/schur-bound-for-a-bessel-function.knowl.md) · [Basic.lean:905](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L905)

The derivative uses the right logarithmic velocity γ′ = γX, prepends the letter to the word, and charges a factor B² per letter up to order 2(ϱ+1)².

<a name="schur-bound-for-a-bessel-function-finding-1"></a>

**Low · Clarify the convolution for a general function W.** The standalone Schur predicate quantifies over every integrable φ, yet no measurability or boundedness of W is assumed on this line. An ordinary Bochner integral of φ(y)W(γy) need not exist for that generality. In the derivative-family application, the Bessel functions are continuous and bounded, so those convolutions are integrable. For the standalone predicate give the source’s convention that the Bochner integral of a nonintegrable function is zero, or present it explicitly for bounded strongly measurable W. [Knowl line 16](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/schur-bound-for-a-bessel-function.knowl.md#L16) · [Basic.lean:894](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L894)

<a name="page-singular-minors-have-small-mass"></a>

### Singular minors have small mass

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/singular-minors-have-small-mass.knowl.md) · [PositiveType.lean:153](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/PositiveType.lean#L153)

The theorem and proof quantify over nonzero source vectors even when their matrix images vanish. The q left-kernel count, character average and two axial terms give the displayed constants.

<a name="singular-minors-have-small-mass-finding-1"></a>

**Low · Describe which vectors the stabilizer hypotheses concern.** The summary suggests that small stabilizers of nonzero vectors suffice. The hypotheses concern A₀v and A₁v for v ≠ 0, and either image can vanish. For G = 𝔽₇ˣ acting by scalars on 𝔽₇, all nonzero vectors have stabilizer mass 1 for Θ = 1. With A₀ = 0, A₁ = 1 and m = n = 1, the suggested bound with Y = 1 would give 42 ≤ 12 + 7√7. Refer in the summary to stabilizers of the images A₀v and A₁v of nonzero source vectors. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/singular-minors-have-small-mass.knowl.md#L5) · [PositiveType.lean:156](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/PositiveType.lean#L156)

<a name="singular-minors-have-small-mass-finding-2"></a>

**Low · Give the direct use and the correct file for the final bound.** MomentBounds applies the determinant estimate in sum_leadingMinor_eq_zero_le. The named HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le is declared in Unfolding/Moments.lean at line 567, so searching the indicated file for the named result fails. Cite sum_leadingMinor_eq_zero_le in MomentBounds as the direct use and HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le in Moments as the eventual application. [Knowl line 47](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/singular-minors-have-small-mass.knowl.md#L47) · [MomentBounds.lean:385](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/MomentBounds.lean#L385)

## Other knowls checked

<a name="page-bessel-system"></a>

### Bessel system at a real place

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/bessel-system.knowl.md) · [Basic.lean:1018](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L1018)

The scalar commutant condition is stated explicitly. The Schur bound uses the full function for every P ≥ b⁵ with constant |I|/deg, while the local bounds concern the cut and the degree is positive.

<a name="page-cauchy-schwarz-for-translates"></a>

### Cauchy–Schwarz for the translates of a map

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/cauchy-schwarz-for-translates.knowl.md) · [FewTranslates.lean:288](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L288)

Cycling the trace gives the squared norm of B\*ρ(s⁻¹t)B. Counting s⁻¹t over the two group indices supplies precisely one factor of |Γ| in the finite-group inequality.

<a name="page-character-sum-bound-by-stabilisers"></a>

### Character sums against a function of positive type

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/character-sum-bound-by-stabilisers.knowl.md) · [PositiveType.lean:102](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/PositiveType.lean#L102)

The inverse transpose acts on x and the original representation acts on z. The mixed inner product uses the positive character after conjugation and gives q^(|n|/2)Y, since nontriviality over a field persists under every nonzero dilation.

<a name="page-few-spread-maps-span-almost-everything"></a>

### Few spread maps span almost everything

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/few-spread-maps-span-almost-everything.knowl.md) · [FewTranslates.lean:479](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L479)

The rank-nullity identity gives the claimed greedy gain above codimension 16ε dim W. Both spaces are nonzero, and the first step bounds the rate by one, which justifies the ceiling in the logarithmic count.

<a name="page-fibres-of-the-frame-gram-map"></a>

### Fibres of the frame Gram matrix over the open cell

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/fibres-of-the-frame-gram-map.knowl.md) · [GramSection.lean:656](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/GramSection.lean#L656)

The common invertible Gram matrix gives left inverses for both frame pairs. Complex conjugation satisfies Witt’s nontrivial-involution hypothesis via i, and the frame-fixer lemma gives g u = k on each side, with the inverses in the displayed order.

<a name="page-frame-gram-matrix-of-an-isometry"></a>

### The frame Gram matrix of an isometry at a real place

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry.knowl.md) · [Basic.lean:255](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L255)

The identity for left and right multiplication uses Z(x′⁻¹γx) = m′\* Z(γ)m, precisely as in the library declaration. Taking x′ = s, x = 1 and γ = sy gives the displayed order of the factors.

<a name="page-function-of-positive-type"></a>

### Function of positive type on a finite group

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/function-of-positive-type.knowl.md) · [PositiveType.lean:51](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/PositiveType.lean#L51)

The two-family sum rule uses the bijection b ↦ a⁻¹b for each a. Orthonormality then selects exactly the stabilizer of x, which also proves the stated generalization from the matrix action in Lean to a finite G-set.

<a name="page-good-poincare-map-is-a-near-isometry"></a>

### The projected Poincaré map is a near isometry

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/good-poincare-map-is-a-near-isometry.knowl.md) · [SpanningTheorem.lean:257](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L257)

The amplitude-block theorem first bounds the unprojected defect by D_X/b¹² and then adds a 4b⁻⁴ projection loss to the b⁻⁴ near-isometry error. The nonzero source and 5b⁻⁴ &lt; 1 yield the range corollary.

<a name="page-link-of-an-isometry"></a>

### Link of an isometry

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/link-of-an-isometry.knowl.md) · [Basic.lean:817](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L817)

The source takes the kernel of the pairing against (e,γe), then maps it to the middle coordinate rows of 1 and γ⁻¹ in that order. The page gives its Hermitian interpretation, a specialization of the matrix definition.

<a name="page-near-isometry-after-projection"></a>

### Near isometries and orthogonal projections

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/near-isometry-after-projection.knowl.md) · [FewTranslates.lean:239](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L239)

Only p needs to be a self-adjoint idempotent. The identity (1−pq)y = (1−p)y + p(1−q)y gives an orthogonal decomposition for arbitrary linear q, and the bound on (1−p)A adds δ dim S to the loss.

<a name="page-near-isometry-in-mean-square"></a>

### Near isometry in mean square

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/near-isometry-in-mean-square.knowl.md) · [FewTranslates.lean:151](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L151)

The error uses dim S for every U, and increases monotonically with ε. Applying the bound to U = S proves the range is nonzero for an arbitrary endomorphism p as soon as S is nonzero and ε &lt; 1.

<a name="page-norm-bound-from-frame-and-dual-columns"></a>

### A norm bound from the frame and the dual columns

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/norm-bound-from-frame-and-dual-columns.knowl.md) · [Basic.lean:205](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L205)

The rank-one column estimate gives (4ϱ+2)M for ‖A(1−J)‖, and AJA\* = J supplies the operator norm inequality after division by ‖A‖ ≥ 1. The relaxed constant 8(ϱ+1)M follows.

<a name="page-normalisation-of-a-bessel-function"></a>

### Normalisation of a Bessel function and of its cut

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/normalisation-of-a-bessel-function.knowl.md) · [Orthonormality.lean:74](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Orthonormality.lean#L74)

The character cancels in Wᵢ times its conjugate coordinate, and conjugation and left translation meet the quotient transport hypotheses. Taking the trace of the scalar moment matrix gives the normalization, including c ≤ 1 for the cut by its defining squared-mass bound.

<a name="page-one-translate-from-second-moment"></a>

### One translate: a small second moment makes the translates spread

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/one-translate-from-second-moment.knowl.md) · [FewTranslates.lean:320](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L320)

The hypothesis multiplies the unnormalized moment by dim T₀, and the proof handles T₀ = 0 using share zero. Commutation and orthogonality identify the two maps on the chosen preimage, yielding exactly 3ε/2.

<a name="page-orthogonal-frame-of-a-point"></a>

### Orthogonal frame and Gram–Schmidt matrix of a point

Source checked · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/orthogonal-frame-of-a-point.knowl.md) · [Basic.lean:328](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/Basic.lean#L328)

The library lifts any upper unitriangular matrix over ℂ for the unit scalar N = 1. Inverting that triangular frame action yields the lower norm bound, and the covariance identity has gs(sy) on the left of m(s).

<a name="page-restricting-maps-to-a-subspace"></a>

### Restricting finitely many maps to a subspace

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/restricting-maps-to-a-subspace.knowl.md) · [FewTranslates.lean:537](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L537)

A complement C has dimension dim V − dim U, and subadditivity bounds the span of all Bₛ(C) by |t| dim C. The derivation also covers the empty index set.

<a name="page-scaled-poincare-map"></a>

### Scaled Poincaré map and the translates of the good Poincaré map

Source checked · construction · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/scaled-poincare-map.knowl.md) · [SpanningTheorem.lean:153](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L153)

The Euclidean source coordinates carry the factor (vol(J)·ν)^(-1/2). The translated good map applies |G| to the unscaled map after translating and projecting, with its target restricted to the projector range.

<a name="page-second-moment-of-the-poincare-map"></a>

### Second moment of the Poincaré map

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/second-moment-of-the-poincare-map.knowl.md) · [SpanningTheorem.lean:270](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L270)

The unnormalized group sum and its reindexing have the same bound with main term D_X²/(deg·massᵣ). Positivity lets the bound for the target dimension cancel exactly that denominator.

<a name="page-spread-family-of-linear-maps"></a>

### Spread family of linear maps

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/spread-family-of-linear-maps.knowl.md) · [FewTranslates.lean:41](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/FewTranslates.lean#L41)

The order of quantifiers allows the translate to depend on F. The ratio uses real division of finite ranks, correctly handling a zero or infinite-dimensional target, and the dimension-gain interpretation is restricted to finite dimension.

<a name="page-translates-of-the-good-poincare-map-spread"></a>

### One good translate of the Poincaré map

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/translates-of-the-good-poincare-map-spread.knowl.md) · [SpanningTheorem.lean:339](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L339)

The moment and isometry errors both fit ε₀ = 1/(8b²), since b ≥ 1000. The coordinate isomorphism identifies the preimages because their defining maps differ only by the nonzero scale and group order.

<a name="page-unfolding-bound-on-the-real-group"></a>

### An unfolding bound on the real unitary group

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-core/unfolding-bound-on-the-real-group.knowl.md) · [SobolevBound.lean:74](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/SobolevBound.lean#L74)

The canonical unipotent Haar measure is invariant under inversion and has the cutoff needed for quotient unfolding. Right translation centres the support at a nonzero value, and the box bound and identity m(s)\* = Z(y)Z(sy)⁻¹ give the stated factors.
