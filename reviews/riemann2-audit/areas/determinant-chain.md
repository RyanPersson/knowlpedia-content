# determinant-chain

This area contains 14 individual knowls. The review records 5 comments.

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Knowls with comments

<a name="page-left-inverses-of-complementary-blocks"></a>

### Left inverses of complementary blocks

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/left-inverses-of-complementary-blocks.knowl.md) · [SquareLaw.lean:335](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean#L335)

Extension by zero proves the complementary-column implication, and the stated idempotent divisibility condition is the one used for completing primitive matrices. The determinant computation needs an explicit identification of the row labels.

<a name="left-inverses-of-complementary-blocks-finding-1"></a>

**Medium · Restore the row reindexing in the determinant identity.** If P is read as the displayed stack of s above xₖ in the ambient column order, its determinant can have the opposite sign. Over ℤ, take singleton blocks, k = I, e the transposition and s = (0,1). Then syₖ = 1, while the raw stack has rows (0,1), (1,0) and determinant −1. Specify that the rows of the stack are transported to the ambient labels using e⁻¹ before taking its determinant. Equivalently, order both axes by e, or use only that the raw determinant is a unit. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/left-inverses-of-complementary-blocks.knowl.md#L24) · [PartnerAlgebra.lean:157](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/LinearAlgebra/PartnerAlgebra.lean#L157)

<a name="page-triangle-of-arrows"></a>

### Triangle of arrows

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/triangle-of-arrows.knowl.md) · [TriangleNorms.lean:157](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleNorms.lean#L157)

The four axioms distinguish the return-to-range and trivial-kernel conditions, and the displayed chain has the correct weight on each arrow. The application uses a twist parameter that contains more information than the modulus.

<a name="triangle-of-arrows-finding-1"></a>

**Medium · Specify the twist parameter in the application.** In the concrete triangle the parameter ranges over m-fold twists. Each twist carries an automorphic character as well as its modulus Q, and the character occurs in the lift at TriangleLifts.lean:235. Indexing by moduli loses that dependence. The direct link to the application has no target in the snapshot. Say I is the set of m-fold twists ϑ and Q is the modulus associated to ϑ. Use New.Data.exists_isTriangle as the application reference. [Knowl line 42](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/triangle-of-arrows.knowl.md#L42) · [ChainNorms.lean:590](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/ChainNorms.lean#L590)

<a name="page-fourier-transform-of-next-datum"></a>

### Fourier transform of the next datum

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/fourier-transform-of-next-datum.knowl.md) · [SquareLaw.lean:421](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean#L421)

Summing the free block forces C = 0, leaving the Fourier transform at −A. The square-matrix Gauss sum times the number of N-by-T blocks gives exactly the stated squared modulus.

<a name="fourier-transform-of-next-datum-finding-1"></a>

**Low · Correct the matrix orthogonality citation.** The identity used here is New.sum_addChar_trace_mul. The cited New.Exchange.sum_addChar_trace_mul does not name a declaration, so the orthogonality step cannot be traced using its reference. Change the reference to New.sum_addChar_trace_mul. [Knowl line 39](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/fourier-transform-of-next-datum.knowl.md#L39) · [FiniteFourier.lean:114](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Analysis/FiniteFourier.lean#L114)

<a name="page-matched-function-of-a-function"></a>

### The matched function of a function

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/matched-function-of-a-function.knowl.md) · [SquareLaw.lean:262](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean#L262)

The two inverse row-column products give the change of basis h, and its determinant is the needed ratio. This makes the partner independent of its representative and gives the stated factor under translation.

<a name="matched-function-of-a-function-finding-1"></a>

**Low · Specify the identification in the empty-block remark.** With a empty, an arbitrary splitting e can still permute the b coordinates, so the resulting map reindexes g. For b = n with two elements, swapping them sends diag(1,−1) to diag(−1,1) over ℤ. State that the embedding is literally the identity for the canonical identification b ⊔ ∅ ≃ b, and is transport along e for a general splitting. [Knowl line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/matched-function-of-a-function.knowl.md#L35) · [SquareLaw.lean:224](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean#L224)

<a name="page-square-moduli"></a>

### Moduli of the squares of a triangle

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/square-moduli.knowl.md) · [TriangleNorms.lean:170](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleNorms.lean#L170)

The abstract multiplicativity axioms, the two quantified adjoint pairings and the square index Lᵢ₊₁,ᵢ₊ₙ₊₂ agree. The remark mischaracterizes the relation used for the application.

<a name="square-moduli-finding-1"></a>

**Low · Describe the chain modulus up to its uniform factors.** The text calls the application a finer modulus statement and points to a missing page. Its actual relation allows |c(ϑ)|² = C·Nm(Qϑ)ᵏ·f(ϑ)² for a uniform real C and integer k. For instance, c ≡ 2 and f ≡ 1 satisfy it. Give the up-to-a-constant-and-norm-power formula, and refer to New.Data.HasAbsUpToNormPower until its target knowl exists. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/square-moduli.knowl.md#L30) · [Moduli.lean:134](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/Moduli.lean#L134)

## Other knowls checked

<a name="page-chains-commute-and-adjoint-in-a-triangle"></a>

### Chains commute with the descent and are adjoint to it

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/chains-commute-and-adjoint-in-a-triangle.knowl.md) · [TriangleNorms.lean:330](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleNorms.lean#L330)

The square step multiplies β by β′ in the conjugated denominator, while adjointness multiplies κ by κ′. The accumulated commutation modulus runs from k = i + 2 through i + n + 1, inclusive.

<a name="page-gram-form-of-a-full-chain"></a>

### Gram form of a full chain in a triangle

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/gram-form-of-a-full-chain.knowl.md) · [TriangleNorms.lean:442](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleNorms.lean#L442)

Conjugate-linearity changes the conjugated β in the commutation law into β in the Gram factor. The induction contributes precisely the pairs i &lt; r &lt; k ≤ m and composes the first endomorphism on the left.

<a name="page-order-of-block-triangular-group"></a>

### Order of a group of block triangular matrices

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/order-of-block-triangular-group.knowl.md) · [TriangleNorms.lean:101](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleNorms.lean#L101)

Removing the last diagonal block contributes one copy of GL(T) and an unrestricted upper-right block of size #Bⱼ·#T. The natural-cardinality convention on infinite rings and the empty-block base case agree with the source.

<a name="page-point-datum-and-next-datum"></a>

### Point datum and next datum

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/point-datum-and-next-datum.knowl.md) · [SquareLaw.lean:78](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean#L78)

The lower blocks C = 0 and D = 1, the sign in p(−η) and division by the number of n-by-b blocks give the stated summation formula. The real denominator explains why complex conjugation commutes with the construction.

<a name="page-square-law"></a>

### Square law over a finite ring

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/square-law.knowl.md) · [SquareLaw.lean:58](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean#L58)

Both determinant equivariances use χ, with left multiplication on L and right multiplication on L′. The coefficient c multiplies the sum tested against the inverse-row partner Φ.

<a name="page-square-law-after-fourier-transform"></a>

### The square law after Fourier transform

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/square-law-after-fourier-transform.knowl.md) · [SquareLaw.lean:477](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean#L477)

At the stated shapes the two general linear groups in the square rule coincide. Dividing by the nonzero Gauss factor gives the reciprocal squared modulus and places γc on the transformed-next-datum side.

<a name="page-square-law-at-a-point"></a>

### The square law at a point

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/square-law-at-a-point.knowl.md) · [SquareLaw.lean:152](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean#L152)

The matched delta tests select y₂ = −wg and x₁ = gw on the invertible blocks. The inverse determinant character removes the singular blocks and cancels the remaining character factors, giving the two different group orders.

<a name="page-square-law-for-next-datum"></a>

### The rule for a square

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/square-law-for-next-datum.knowl.md) · [SquareLaw.lean:185](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/SquareLaw.lean#L185)

After exchanging the first two blocks, the shear fixes the inclusion of n and introduces the free block s. Averaging over s leaves precisely the next-datum measure and the two stated group orders.

<a name="page-weighted-chains-are-injective"></a>

### Weighted chains of a triangle are injective

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/determinant-chain/weighted-chains-are-injective.knowl.md) · [TriangleNorms.lean:349](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/TriangleNorms.lean#L349)

Moving a zero chain to the next row and using the injectivity of the initial descent composite proves injectivity on jᵢ(V). The separate nontriviality assumption on V is exactly what rules out a vanishing commutation factor under totalized division.
