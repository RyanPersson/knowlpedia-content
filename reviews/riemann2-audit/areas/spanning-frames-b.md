# spanning-frames-b

This area contains 15 individual knowls. The review records 9 comments.

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Knowls with comments

<a name="page-frames-setting"></a>

### Standing notation for pairs of frames at one place

Correction recorded · notation · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/frames-setting.knowl.md) · [Shells.lean:36](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean#L36)

I checked the floor groups, head density, mass bound and place data in their defining files. The ambient ring, basis description, density range and integration convention need corrections.

<a name="frames-setting-finding-1"></a>

**High · The finite coefficient ring is a product of completed fields.** The page identifies A with a product of localized rings of integers. In the finite application A=∏_{w∈T} E_w. The compact open integer subring is ∏ O_w. A localization of the global integers at w is countable and does not give the completed local field used for Haar integration. Define A as the product of the local-field completions over the conjugation-stable finite set T. Identify the product of their rings of integers as its integral subring. [Knowl line 16](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/frames-setting.knowl.md#L16) · [LocalFactors.lean:432](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/LocalFactors.lean#L432)

<a name="frames-setting-finding-2"></a>

**Medium · Include the distinguished hyperbolic pair in the middle basis.** The description mentions m further pairs and the orthonormal part but never introduces the first pair. Lean requires m+1 middle hyperbolic pairs in addition to the outer ϱ, with k+1=|ι|+2m+2. Describe the middle basis as one distinguished hyperbolic pair, m additional pairs and |ι| orthonormal vectors. [Knowl line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/frames-setting.knowl.md#L19) · [FloorMeasures.lean:522](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorMeasures.lean#L522)

<a name="frames-setting-finding-3"></a>

**Medium · Use truncated subtraction in the head density.** The displayed d_a=k+1+2(ϱ−a−1) is given without a range restriction. At a=ϱ it gives k−1, whereas the source's natural subtraction gives k+1. This affects heads extending through the top entry. Write d_a=k+1+2 max(ϱ−a−1,0), or restrict the untruncated formula explicitly to a&lt;ϱ. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/frames-setting.knowl.md#L21) · [Densities.lean:63](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Densities.lean#L63)

<a name="frames-setting-finding-4"></a>

**Medium · Specify the lower integral for arbitrary shell functions.** The linked definition covers nonnegative measurable functions, while the one-shell and summed estimates quantify over arbitrary f and impose no measurability on the shells. Their integrals are defined in Lean for that generality. The ordinary measurable-only integral advertised here leaves some cases undefined. Use the lower Lebesgue integral, the supremum of integrals of measurable simple minorants. For a set integral, use the restricted measure as in the source. An alternative is to identify explicitly the measurable specialization throughout. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/frames-setting.knowl.md#L26) · [Shells.lean:92](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean#L92)

<a name="frames-setting-finding-5"></a>

**Low · Point the floor-group link to its declared namespace.** The text describes the correct fixer, but New.FloorGroups.floorGroup is not its Lean declaration. The definition is exported under New.Shape.Form.floorGroup, so the current token cannot resolve by declaration name. Use the placeholder for New.Shape.Form.floorGroup. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/frames-setting.knowl.md#L18) · [FloorGroups.lean:176](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/FloorGroups.lean#L176)

<a name="page-form-constant-real"></a>

### Normalising constant of the forms at a real place

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/form-constant-real.knowl.md) · [RealShells.lean:122](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L122)

The two volume factors and the squared denominator agree with the definition. Strict positivity additionally requires a nonempty index set.

<a name="form-constant-real-finding-1"></a>

**Medium · Positivity requires a nonempty value space.** The definition accepts an empty finite I. The scalar-commutant and normalization conditions permit the zero-dimensional cut pair. Then λ|I|=0, the displayed fraction is undefined in the usual real numbers, and Lean's totalized quotient equals zero. Assume I is nonempty for the positive formula, or specify that the source assigns zero when I is empty and assert positivity only when |I|&gt;0. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/form-constant-real.knowl.md#L14) · [RealShells.lean:122](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L122)

<a name="page-real-place-setting"></a>

### Standing notation at a real place

Correction recorded · notation · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/real-place-setting.knowl.md) · [RealShells.lean:31](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L31)

The loss L², depth d/π, group measure λ dy and power of π in the scaled volume agree. The description of the adapted middle basis leaves its distinguished pair implicit.

<a name="real-place-setting-finding-1"></a>

**Medium · Identify the two missing vectors of the real middle basis.** Saying m=0 further pairs and listing only x_i with i≠k₀ accounts for k−1 of the k+1 middle dimensions. The source takes a distinguished hyperbolic pair from the omitted direction x_k₀ and the negative vector z. Identify k₀ as the index distinguished by the shape, and give the pair (1+i)(x_k₀+z)/2 and (1+i)(x_k₀−z)/2 together with the remaining x_i. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/real-place-setting.knowl.md#L22) · [ComplexPlace.lean:102](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Bruhat/ComplexPlace.lean#L102)

<a name="page-shell-normalization"></a>

### Normalization of integrals over positions

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/shell-normalization.knowl.md) · [Shells.lean:44](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean#L44)

The product of floor moduli, the exponent |FreeIndex|·ϱ and the two-variable correlation are correctly normalized. The finite-place geometric interpretation needs its lattice hypotheses.

<a name="shell-normalization-finding-1"></a>

**Medium · Qualify the identification with the unipotent congruence volume.** The remark attaches this volume interpretation to finite places in general. The proved identification assumes large lattice data and an integral self-conjugate level. The abstract place datum used by the displayed definition requires self-conjugacy of M but does not require M to be integral. Keep the normalization formula for arbitrary place data and restrict the congruence-volume interpretation to the finite large-lattice data with integral level used in the application. [Knowl line 26](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/shell-normalization.knowl.md#L26) · [StandardLevel.lean:858](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/StandardLevel.lean#L858)

<a name="page-sum-over-shells"></a>

### The sum over the shells

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/sum-over-shells.knowl.md) · [Shells.lean:243](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean#L243)

The gain is required on positions only when e&lt;1. For e≥1 the no-gain estimate supplies the bound, and summing the inverse heights costs exactly 2. The proof itself agrees.

<a name="sum-over-shells-finding-1"></a>

**Low · Both shell-construction links point to absent pages.** The two literal internal IDs ending in real-shells and finite-shells have no files in the snapshot. The reader cannot follow the claimed constructions from this theorem. Link the real dyadic-shell definition where appropriate and use the canonical declaration placeholders New.Floors.IsCutBessel.isShell_dyadicShell and New.Floors.IntegralPlace.IsLargeLatticeData.isShell_dyadicShell for the two shell assertions. [Knowl line 48](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/sum-over-shells.knowl.md#L48) · [RealShells.lean:422](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L422)

## Other knowls checked

<a name="page-correlation-norm-real"></a>

### The norm of the correlation of a cut Bessel function

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/correlation-norm-real.knowl.md) · [RealShells.lean:229](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L229)

The two applications of the Haar-ratio identity are to left-unipotent-invariant nonnegative functions. The cut-pair orthogonality inequality on the nonempty value space supplies the inner bound, giving λ²|I|.

<a name="page-cut-bessel-function-real"></a>

### Cut Bessel function at a real place

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/cut-bessel-function-real.knowl.md) · [RealShells.lean:71](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L71)

The page correctly combines the cut-pair axioms with the seven size inequalities and the scalar-commutant condition. The cutoff, half-radius agreement, error exponent −2r³f and volume exponent agree with the source.

<a name="page-dyadic-shell"></a>

### Dyadic shell at a real place

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/dyadic-shell.knowl.md) · [RealShells.lean:90](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L90)

The index minimizes over nonnegative exponents beginning at zero. The separation estimate uses i≥1 and the contradiction supplied by the admissible smaller exponent i−1.

<a name="page-gauge-for-two-heads"></a>

### A gauge in which two sequences are heads

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/gauge-for-two-heads.knowl.md) · [RealShells.lean:194](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L194)

The induction enlarges L by the inverse moduli of the two new partial products. Each enlargement costs exactly the permitted max(1,|δ|⁻¹)^K factor once the common bound R holds.

<a name="page-one-shell-bound"></a>

### The integral over one shell

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/one-shell-bound.knowl.md) · [Shells.lean:92](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean#L92)

Only q needs to be a head. I checked the extra factor of Λ in the two-gauge estimate and the cover's cardinality factor before rounding the powers to 2·10⁶n³ and 10⁵n². The integration convention is addressed on the standing-notation page.

<a name="page-orbital-integral-minors-real"></a>

### A nonzero orbital integral bounds the leading minors

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/orbital-integral-minors-real.knowl.md) · [RealShells.lean:151](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L151)

The conjugated coordinate is evaluated at γ⁻¹y. Nonvanishing forces both values to be nonzero at a common point, and the general gauge estimate at L=ρ covers every order from zero through n.

<a name="page-position-ball-real"></a>

### Position ball at a real place

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/position-ball-real.knowl.md) · [RealShells.lean:81](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/RealShells.lean#L81)

The ball bounds individual entries of x−1 by T^(99n). Its measurability follows by intersecting the measurable inequalities in the two basis indices.

<a name="page-remote-shell-gain"></a>

### The gain on a remote shell

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/remote-shell-gain.knowl.md) · [Shells.lean:143](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean#L143)

Squaring the required shell inequality gives Λ^(2400n²)≤h, using τ^(800n²)h=1. The resulting depth is (τ²)⁻¹, and the squared pointwise gain becomes (Vτˢ)² before the one-shell bound.

<a name="page-shell"></a>

### Shell of positions

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/shell.knowl.md) · [Shells.lean:50](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean#L50)

The gauge-cover cardinality, loss limit and strict σ&lt;1 agree. Each active y has a possibly different deep-vector index a between j and ϱ−1.

<a name="page-shell-inverse-height"></a>

### A few factors of the gain pay for the height of a shell

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-frames-b/shell-inverse-height.knowl.md) · [Shells.lean:174](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/Frames/Shells.lean#L174)

The near/far split and g=min(e,τ) reproduce the source. The exact identity 800·112500=9·10⁷ pays the power of h, and h is finite and nonzero when its inverse is cancelled.
