# determinant-exchange

This area contains 11 individual knowls. The review records 4 comments.

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Knowls with comments

<a name="page-block-datum-is-sharp"></a>

### The block datum is sharp for the principal level at the chosen places

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/block-datum-is-sharp.knowl.md) · [AdjointThetaLift.lean:599](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean#L599)

The outline verifies the sharp-function conditions using the inclusion transpose and obtains the required mean-square mass divided by the level index. The surjectivity result used to lift the residue block has an incorrect citation.

<a name="block-datum-is-sharp-finding-1"></a>

**Low · Point to the reduction surjectivity lemma in its actual namespace.** The residue-family lifting theorem used here is New.exists_reduceFamily_eq. Only the reduction map is in New.stdLevel. The cited New.stdLevel.exists_reduceFamily_eq cannot resolve. Cite New.exists_reduceFamily_eq and identify pairwise distinct places with no conjugate pair as the hypothesis supplied by the descent pair. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/block-datum-is-sharp.knowl.md#L29) · [CongruenceLevels.lean:330](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/CongruenceLevels.lean#L330)

<a name="page-lift-and-descent-equivariant-for-chosen-group"></a>

### Lift and descent commute with the finite group of the chosen places

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/lift-and-descent-equivariant-for-chosen-group.knowl.md) · [AdjointThetaLift.lean:195](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean#L195)

The datum picks up χ(s)⁻¹ and the action picks up χ(s), which give the stated translations under the lift and descent. The account of independence of the integral lift gives the wrong reason.

<a name="lift-and-descent-equivariant-for-chosen-group-finding-1"></a>

**Low · Use the reduction kernel to justify independence of the lift.** Multiplication by χ(s) depends only on s, so it cannot remove dependence on a choice of k′. Right translation is already independent of that choice on these level forms: two lifts differ by an element with identity reduction at M and Q, where the level character is trivial. Explain the reduction-kernel argument first. Introduce χ(s) as the character twist in the chosen-group action, which cancels the datum factor in the equivariance identity. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/lift-and-descent-equivariant-for-chosen-group.knowl.md#L26) · [CongruenceLevels.lean:521](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/CongruenceLevels.lean#L521)

<a name="page-single-lift"></a>

### The single lift from W_j to V_j

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/single-lift.knowl.md) · [AdjointThetaLift.lean:256](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean#L256)

The lift is the restriction to principal-level forms when 1 ≤ j ≤ m and is zero at every other natural index. The symbol for its fixed character needs identification.

<a name="single-lift-finding-1"></a>

**Low · Identify the character of the individual lift.** The expression χⱼϑ introduces χⱼ without a definition. The descent-pair construction uses the untwisted character μⱼ⁰ multiplied by ϑ, and the surrounding descent-pair knowl calls it μⱼ⁰ϑ. Use μⱼ⁰ϑ and link the untwisted lift character, or define χⱼ = μⱼ⁰ at first use. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/single-lift.knowl.md#L14) · [LevelAndTwists.lean:332](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/LevelAndTwists.lean#L332)

<a name="page-vector-kernel-equivariance"></a>

### Equivariance of the vector-valued theta kernel. The kernel as an algebraic form

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/vector-kernel-equivariance.knowl.md) · [VectorKernel.lean:104](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/VectorKernel.lean#L104)

The inverse determinant character at the twist places and the rational weight action give a unitary operator, so testing against its image proves equivariance. The smoothness argument needs the openness of the character kernel.

<a name="vector-kernel-equivariance-finding-1"></a>

**Low · Use the open subgroup that fixes the kernel form.** Transformation by a character under an open subgroup establishes smoothness when the character is trivial near the identity. Openness of the subgroup alone, as stated in the last sentence, does not give an open stabilizer. Here the level character factors through finite residue reduction. State that the principal reduction kernel is open and fixes the function, since the level character is one there. [Knowl line 37](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/vector-kernel-equivariance.knowl.md#L37) · [HeckeEigenforms.lean:118](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/HeckeEigenforms.lean#L118)

## Other knowls checked

<a name="page-block-datum-function-and-norm"></a>

### The block datum as a function of residue matrices, and its squared norm

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/block-datum-function-and-norm.knowl.md) · [AdjointThetaLift.lean:485](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean#L485)

The modulus of exponent one yields the same vacuum datum because both functions use only the residue reductions. The local count contributes one at each chosen place and #GLᵣ(k_w)·q_w^(tr) at each twist place.

<a name="page-descent-adjoint-to-theta-lift"></a>

### The normalized descent is adjoint to the theta lift

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/descent-adjoint-to-theta-lift.knowl.md) · [AdjointThetaLift.lean:297](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean#L297)

The class-sum-to-Petersson factor is the level index times the dimension of the weight representation. It is absorbed in the second argument of the Petersson pairing, after taking the conjugate lift through the swapped kernel.

<a name="page-descent-as-pairing-with-kernel-form"></a>

### The normalized descent is the inner product with the kernel form

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/descent-as-pairing-with-kernel-form.knowl.md) · [VectorKernel.lean:164](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/VectorKernel.lean#L164)

The normalized descent and the class-sum inner product use the same stabilizer denominators. The first slot contains the kernel vector, whose Gram pairing with Ξ(h) is the conjugate-kernel functional itself.

<a name="page-hecke-polynomial-of-theta-lift"></a>

### Hecke polynomial of the theta lift of a descent pair

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/hecke-polynomial-of-theta-lift.knowl.md) · [AdjointThetaLift.lean:221](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean#L221)

The outline checks both unramified characters and the vacuum projection off the level and its conjugate. The transfer theorem then gives the q-Pochhammer factor and the rescaling qᵗα/β with the stated ranks.

<a name="page-theta-lift-as-integral-of-kernel-form"></a>

### The theta lift is the integral against the kernel form

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/theta-lift-as-integral-of-kernel-form.knowl.md) · [AdjointThetaLift.lean:391](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean#L391)

The kernel coefficients in an orthonormal basis are the conjugates of the corresponding descents, so the product with y is integrable by the L² bound. Continuous evaluation then identifies the Bochner integral with the scalar theta lift.

<a name="page-theta-lift-of-descent-pair"></a>

### Theta lift of a descent pair

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/theta-lift-of-descent-pair.knowl.md) · [AdjointThetaLift.lean:160](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean#L160)

The highest-vector datum is an arrow for fitting parameters in both the forward and conjugate swapped directions. The finite level acts through the character required by the codomain, and the attached adelic function is the ordinary theta integral.

<a name="page-vector-valued-theta-kernel"></a>

### Vector-valued theta kernel of a descent pair

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-exchange/vector-valued-theta-kernel.knowl.md) · [VectorKernel.lean:63](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/VectorKernel.lean#L63)

The real coordinate vectors remove the two conjugations in the inverse-Gram coordinate formula. Pairing the resulting kernel on the right gives the theta function of the conjugated vector, and interchanging the slots recovers the conjugate-kernel functional.
