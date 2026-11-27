# spanning-unfolding-a

This area contains 5 individual knowls. The review records 3 comments.

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Knowls with comments

<a name="page-product-of-frame-masses-upper-bound"></a>

### Upper bound for the product of the frame masses

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-a/product-of-frame-masses-upper-bound.knowl.md) · [FrameMass.lean:248](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FrameMass.lean#L248)

The telescoping argument gives the stated direction and the factor (1 − N^(−k))^(2f). The only substantial step left without its numerical inputs is the comparison of the two errors.

<a name="product-of-frame-masses-upper-bound-finding-1"></a>

**Medium · Give the size estimates behind the error bound.** The cited comparison principle needs actual upper and lower exponents. The displayed error budget is the substantive numerical step in this full proof, and the source uses the stronger bound b¹⁰ ≤ 2^ϱ. The filling datum’s elementary bound only gives b⁶ ≤ 2^ϱ. Cite b¹⁰ ≤ 2^ϱ, N ≥ b¹⁰¹, and r − k ≤ k ≤ f ≤ b/1000. For y = b⁻⁹ ≤ 1, these bound the left side by 6y/1000 ≤ 2y/(2+y). [Knowl line 34](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-a/product-of-frame-masses-upper-bound.knowl.md#L34) · [FillingData.lean:448](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Bessel/FillingData.lean#L448)

<a name="page-size-of-different-generator-at-infinite-places"></a>

### Size of the generator of the different at the infinite places

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-a/size-of-different-generator-at-infinite-places.knowl.md) · [FrameMass.lean:88](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FrameMass.lean#L88)

The estimates for 2/w and 1/√w follow from 2 ≤ w ≤ b in the stated directions. The first and arithmetically substantive inequality needs its generator-specific input.

<a name="size-of-different-generator-at-infinite-places-finding-1"></a>

**Medium · Cite the actual bound for the generator.** The two cited results compare exponents and constrain the scales x, x₁ and b. Neither supplies the exponents of |ϖ|ᵥ. These come from the arithmetic of the different, which the full proof skips. Link the existing size-of-the-different knowl for x¹⁰ ≤ |ϖ|ᵥ ≤ x¹² and apply the scale inequalities 2 ≤ x¹⁰ and x¹² ≤ b. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-a/size-of-different-generator-at-infinite-places.knowl.md#L26) · [ChosenPlaces.lean:421](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L421)

<a name="page-unit-sphere-mass"></a>

### Mass of the unit sphere at an infinite place

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-a/unit-sphere-mass.knowl.md) · [FrameMass.lean:113](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FrameMass.lean#L113)

I checked the zero-rank convention, the fibre-measure normalization, the logarithmic discriminant factor, and the two hypotheses and sign of the consecutive-mass estimate in SiegelClassSum.lean.

<a name="unit-sphere-mass-finding-1"></a>

**Low · Identify the arithmetic input to the local sphere bounds.** Properties 2 and 3 invoke the comparison of exponents for 2π ≤ √w and wr ≤ x¹⁸ without identifying any bound for this particular w. The needed estimate is already a translated result. Link the size-of-the-different knowl for x¹⁰ ≤ w ≤ x¹². Since r ≤ 3x⁵ and x ≥ 3, one obtains 2π ≤ x⁵ ≤ √w and wr ≤ 3x¹⁷ ≤ x¹⁸. [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-a/unit-sphere-mass.knowl.md#L29) · [ChosenPlaces.lean:421](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L421)

## Other knowls checked

<a name="page-frame-mass"></a>

### Mass of frames at an infinite place

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-a/frame-mass.knowl.md) · [FrameMass.lean:118](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FrameMass.lean#L118)

The interval k ≤ i &lt; r has 2ϱ + 1 terms with mean k + ϱ. I checked both the lower bound from x³⁶ ≤ b and the resulting coefficients of log(2π) and log rd in the product.

<a name="page-product-of-frame-masses-and-open-cell-constant"></a>

### The product of the frame masses in terms of the Siegel constant and the open cell constant

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-unfolding-a/product-of-frame-masses-and-open-cell-constant.knowl.md) · [FrameMass.lean:329](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Unfolding/FrameMass.lean#L329)

The unitary volume quotient cancels the entire factorial sum. Using |disc E| = rd^(2f) leaves exactly the displayed exponents ϱ/2 on the discriminant and ϱ + 1 + 2ϱ(ϱ + k) on the finite volume.
