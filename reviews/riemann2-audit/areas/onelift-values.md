# onelift-values

This area contains 11 individual knowls. The review records 7 comments.

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Knowls with comments

<a name="page-descent-pairing"></a>

### The descent pairing of a finite datum and a form

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/descent-pairing.knowl.md) · [BottomOfTower.lean:1063](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L1063)

The coefficient is conjugated, the kernel is swapped, and the pairing is linear in Ψ and conjugate-linear in y. The literal local interpretation of the datum has a smaller domain than the formal linear map.

<a name="descent-pairing-finding-1"></a>

**Medium · Distinguish a local test function from the extension to arbitrary functions.** The page introduces every function Ψ and describes its tensor with the vacuum. The operator on that whole function space uses a chosen generalized inverse. Its coefficients reproduce Ψ in the relative Schwartz–Bruhat subspace. For example, a constant nonzero function on a positive-dimensional noncompact local space cannot be that local Schwartz vector. Moreover, the vacuum projection is guaranteed away from S and its conjugates (NamedData.lean:153). Give the ordinary tensor interpretation for Ψ Schwartz–Bruhat above S. For the all-functions definition, state that the named operator uses a chosen linear extension and that vacuum is imposed outside S ∪ S̄. [Knowl line 40](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/descent-pairing.knowl.md#L40) · [NamedData.lean:77](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/MixedModel/NamedData.lean#L77)

<a name="page-descent-pairing-invariance"></a>

### Invariance of the descent pairing under the maximal level

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/descent-pairing-invariance.knowl.md) · [BottomOfTower.lean:1103](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L1103)

The right translate of the form, pullback of the datum by k⁻¹, conjugated level character, and unweighted mean over the orbit of indicators agree with the source. The proof elides a character evaluation needed to fix the vacuum.

<a name="descent-pairing-invariance-finding-1"></a>

**Medium · Explain why the twist acts trivially on the vacuum.** The displayed action on Ψ still leaves the Weil action on the vacuum. For an integral k that action has scalar ν_W(det k). The formal proof evaluates this scalar using that ν_W is a power of υ_U(1), which is trivial on determinants of the maximal integral level. Integrality alone would not dispose of an arbitrary twist. Separate the pullback of the relative test function from the action on the vacuum, and invoke upsilonU1_detFin_eq_one_of_mem_stdLevel for the latter. [Knowl line 51](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/descent-pairing-invariance.knowl.md#L51) · [BottomOfTower.lean:1117](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L1117)

<a name="page-translated-block-datum"></a>

### Right translates of the block datum and their characterisation

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/translated-block-datum.knowl.md) · [BottomOfTower.lean:833](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L833)

Column completion yields a level point with prescribed S-components, and the uniqueness argument compares two eigenfunctions on that projected orbit. The action used for vanishing evaluates its splitting character and norm on the partial determinant.

<a name="translated-block-datum-finding-1"></a>

**Medium · The one-orbit assertion holds after projection to S.** The summary and the heading of item 2 describe the whole support as one level orbit. The equation in item 2 is only at S. In positive rank one can change the component of eA⁻¹ to zero at another place without changing Ψ_A. Multiplication by a level element preserves local rank there, so the resulting point is outside that adelic orbit. Describe the support as the inverse image of one level orbit on the components at S in both the summary and the heading. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/translated-block-datum.knowl.md#L5) · [BottomOfTower.lean:835](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L835)

<a name="translated-block-datum-finding-2"></a>

**Low · Correct the split-place construction reference.** The target New.Gf.ofSplitPlace has an extra namespace component. The construction that realizes the prescribed local point is declared as New.ofSplitPlace. Change the Lean target to New.ofSplitPlace. [Knowl line 47](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/translated-block-datum.knowl.md#L47) · [Defs.lean:317](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/Defs.lean#L317)

<a name="translated-block-datum-finding-3"></a>

**Low · Use the partial determinant in both factors of the Weil scalar.** The displayed character and norm are written at det A, although the source uses detOn O.places A for both. The following sentence qualifies the norm only. The global idele norm of a unitary determinant is one, whereas its selected split side can have nonunit norm. Introduce d_S as the idele equal to det A at S and one elsewhere, then write ε_n(d_S)⁻¹ |d_S|^{n/2}. [Knowl line 80](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/translated-block-datum.knowl.md#L80) · [BottomOfTower.lean:1167](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L1167)

<a name="page-factorial-classes-span-schwartz-bruhat"></a>

### Indicators of classes modulo i! span the Schwartz-Bruhat functions

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/factorial-classes-span-schwartz-bruhat.knowl.md) · [BottomOfTower.lean:534](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L534)

The varying threshold belongs to each center separately. Compactness reduces to a finite cover and subtraction of a largest nested coset proves membership in the span.

<a name="factorial-classes-span-schwartz-bruhat-finding-1"></a>

**Low · Specify the ordering of the integer multiples.** The assertion that N times the integral lattice shrinks to zero needs divisibility ordering. In the ordinary order, arbitrarily large odd N give no containment in twice the integral lattice, already over the rationals. The proof uses existence of one suitable N and then divisibility of factorials. Say that the positive integer multiples form a neighborhood basis under divisibility, or that every neighborhood contains one such multiple. Then N divides i! for i ≥ N. [Knowl line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/factorial-classes-span-schwartz-bruhat.knowl.md#L38) · [BottomOfTower.lean:517](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L517)

<a name="page-hyperplane-sums-annihilate"></a>

### Forms annihilated by the hyperplane sums

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/hyperplane-sums-annihilate.knowl.md) · [BottomOfTower.lean:1275](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L1275)

A family with one nonzero row gives the one-place identity. The character in the block action supplies the inverse determinant weight at a chosen place and the whole action at a twist place.

<a name="hyperplane-sums-annihilate-finding-1"></a>

**Low · The rank-one example links to a missing knowl.** There is no knowl with the directly linked ID proofs/grh/onelift-values/false-lifts-from-a-line in the audited corpus. The rank-one assertion does have a specific source theorem on the image of the group mean. Point the reference to New.Rows.hyperplaneSum_apply_eq_zero_of_rank_one or to an existing knowl for that theorem. [Knowl line 48](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/hyperplane-sums-annihilate.knowl.md#L48) · [PeriodsOfFalseLifts.lean:494](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/PeriodsOfFalseLifts.lean#L494)

## Other knowls checked

<a name="page-annihilating-row-exists"></a>

### A matrix without an integral block ratio has an annihilating row

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/annihilating-row-exists.knowl.md) · [BottomOfTower.lean:365](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L365)

For a singular upper block the proof extends and normalizes a left-kernel vector. In the invertible case the maximal coordinate of a lower row of x″x′⁻¹ gives a primitive row, with the strict inequality needed for the off-block residue at a twist place.

<a name="page-bottom-of-tower"></a>

### The bottom of the tower: from the block datum to all data

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/bottom-of-tower.knowl.md) · [BottomOfTower.lean:1466](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L1466)

The nontriviality assumption concerns twist places, and the block-descent hypothesis quantifies over all polynomials at the fixed coefficient functional. Testing the kernel on factorial classes gives every relative Schwartz–Bruhat function, after which the mixed-model criterion gives vacuum away from the places and their conjugates.

<a name="page-descent-pairing-vanishes-on-small-classes"></a>

### The descent pairing vanishes on indicators of small classes

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/descent-pairing-vanishes-on-small-classes.knowl.md) · [BottomOfTower.lean:1226](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L1226)

In the integral-ratio case the claim is eventual in the factorial index, via a level-orbit mean and the normalized translate. If the ratio fails at one place, the shear fixes the class for every idele modulus and the hyperplane sum gives zero after division by the group order (line 1437).

<a name="page-hyperplane-group-character-sum"></a>

### The hyperplane group of a row and its character sum

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/hyperplane-group-character-sum.knowl.md) · [BottomOfTower.lean:210](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L210)

For a nonzero row λ, varying the one coordinate of v with λ_b ≠ 0 realizes every nonzero determinant τ = 1 + λv. The determinant character is therefore nontrivial on the hyperplane group, and the weighted sum is zero.

<a name="page-integral-block-ratio"></a>

### Integral block ratio and annihilating rows

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/integral-block-ratio.knowl.md) · [BottomOfTower.lean:266](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L266)

The upper block needs invertible determinant over the local field. Integrality concerns x″x′⁻¹, whose reduction must also vanish at a chosen place. The complementary annihilating-row condition puts its extra vanishing requirement at twist places.

<a name="page-triangular-level-action"></a>

### Integral elements with block triangular reductions act through their first blocks

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-values/triangular-level-action.knowl.md) · [BottomOfTower.lean:998](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/FalseLifts/BottomOfTower.lean#L998)

The chosen-place character factors cancel when the triangular element is factored into a lift and a level element. The local shear fixes z because its row annihilates z, and its lift and completion are independent of the translated form (lines 1384–1394).
