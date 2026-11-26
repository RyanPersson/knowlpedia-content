# spanning-mainterm

This area contains 15 individual knowls. The review records 4 comments.

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Knowls with comments

<a name="page-damped-power"></a>

### Damped power

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/damped-power.knowl.md) · [SieveSystem.lean:36](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SieveSystem.lean#L36)

The defining formula agrees for all real r and natural k. The application is a sum over nonzero frequencies integral outside a selected finite set, with an additional denominator factor.

<a name="damped-power-finding-1"></a>

**Medium · Identify the places and the finite weight in the frequency sum.** The remark calls the application a sieve over all places and attributes convergence to the extra archimedean decay. The global sieve uses all infinite places and a chosen finite T. Its bound includes a finite factor with the inverse cube of the denominator index, which controls frequencies with bounded archimedean components and growing denominators. Both literal application links lead to absent pages. Describe the global product over infinity and T and say that the sixth power supplies the archimedean part of the height bound. Link New.Filling.IsGlobalSieveSystem and New.Filling.sum_frequencies_le, or the already present inverse-cubed-height estimate as appropriate. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/damped-power.knowl.md#L22) · [GlobalSieve.lean:177](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/GlobalSieve.lean#L177)

<a name="page-product-of-sieve-systems"></a>

### A finite product of sieve systems is a sieve system

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/product-of-sieve-systems.knowl.md) · [SieveSystem.lean:147](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SieveSystem.lean#L147)

I checked the two component maps, products of bounds, and the Schur-product step for the top form. The Fubini citation establishes the integration step only under a stronger finiteness hypothesis.

<a name="product-of-sieve-systems-finding-1"></a>

**Medium · The linked Fubini theorem assumes σ-finiteness.** The proposition allows an s-finite measure on C. The linked Fubini knowl assumes σ-finiteness for both factors. An s-finite measure can put infinite mass on a single atom, so that theorem does not directly justify the factorization under the stated assumptions. Cite the s-finite product-integral formula used in Lean, or decompose the measure on C as a countable sum of finite measures, apply ordinary Fubini to the separate-variable integrands and their absolute values, and sum. [Knowl line 58](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/product-of-sieve-systems.knowl.md#L58) · [SieveSystem.lean:174](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SieveSystem.lean#L174)

<a name="page-sieve-system"></a>

### Sieve system

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/sieve-system.knowl.md) · [SieveSystem.lean:59](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SieveSystem.lean#L59)

The six axioms match, including the different weights Λᵢ for a twisted integral and Λᵢ₊₁ for an off-diagonal value. The example of the entry map needs a qualification for the global product.

<a name="sieve-system-finding-1"></a>

**Medium · The global entry map handles nonunits factor by factor.** The remark says a nonunit of C is sent to 1 in the applications. In the global sieve, unitOrOne acts separately on every complex factor and on the finite ring as one factor. For example, archimedean components (2,0) become (2,1), although the input is a nonunit in the product. Qualify the remark as the rule for each local factor. State that the global entry map combines those local choices componentwise. [Knowl line 67](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/sieve-system.knowl.md#L67) · [GlobalSieve.lean:490](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/GlobalSieve.lean#L490)

<a name="page-archimedean-head-weight"></a>

### Weight of a head at an infinite place

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/archimedean-head-weight.knowl.md) · [SieveSystem.lean:41](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SieveSystem.lean#L41)

The product runs over the first i nonempty prefixes, is zero as soon as one exceeds R, and equals one for i=0. The application to a global weight is correct, but its literal link is missing.

<a name="archimedean-head-weight-finding-1"></a>

**Low · The global-weight link has no target page.** The literal global-weight knowl ID has no file in this snapshot. Lean defines the product of the archimedean and finite factors as New.Filling.globalWeight. Use the declaration placeholder New.Filling.globalWeight until its knowl is published. [Knowl line 35](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/archimedean-head-weight.knowl.md#L35) · [GlobalSieve.lean:927](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/GlobalSieve.lean#L927)

## Other knowls checked

<a name="page-archimedean-weight-sum-over-integer-coset"></a>

### Sum of archimedean weights over numbers that differ by integers

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/archimedean-weight-sum-over-integer-coset.knowl.md) · [Frequencies.lean:198](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/Frequencies.lean#L198)

Two embeddings in the same half-unit square differ in norm by less than one. I checked the norm-product contradiction for algebraic integers and the packing constants giving 5²·(3/2)≤38, followed by the factor 64 per place.

<a name="page-bessel-coset-sum-is-kloosterman-sum"></a>

### A sum of finite Bessel functions over cosets is a Kloosterman sum

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/bessel-coset-sum-is-kloosterman-sum.knowl.md) · [KloostermanSum.lean:155](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/KloostermanSum.lean#L155)

The incidence condition uses sK, and integrality of s allows moving s⁻¹ to the right. I checked both directions of the supported reindexing (w,w′)↦xw′K and the conjugation of the second character.

<a name="page-coset-labels-for-bounded-denominator"></a>

### Numbers with denominator dividing an ideal lie in norm-many cosets of the integers

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/coset-labels-for-bounded-denominator.knowl.md) · [Frequencies.lean:68](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/Frequencies.lean#L68)

The containment b⊆d(ν) has the right direction. Choosing 0≠a∈b and (a)=bc puts aν in c, and the additive quotient c/(a) has N(b) elements, so equal labels give an integral difference.

<a name="page-denominator-ideal"></a>

### Denominator ideal of an element of a number field

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/denominator-ideal.knowl.md) · [Frequencies.lean:28](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/Frequencies.lean#L28)

Membership is precisely integrality of aν for a∈O_E. A nonzero denominator from a fraction representation proves nonvanishing even for ν=0, whose denominator ideal is the whole ring.

<a name="page-integral-over-cosets-of-open-subgroup"></a>

### Integral of a function constant on the cosets of an open subgroup

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/integral-over-cosets-of-open-subgroup.knowl.md) · [KloostermanSum.lean:41](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/KloostermanSum.lean#L41)

The pushforward gives each singleton in the countable discrete quotient mass μ(J). The stated convention is compatible both with a non-absolutely-summable function for counting measure and with the case μ(J)=0.

<a name="page-kloosterman-sum-at-finite-places"></a>

### Kloosterman sum of a unitary group at the finite places

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/kloosterman-sum-at-finite-places.knowl.md) · [KloostermanSum.lean:89](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/KloostermanSum.lean#L89)

The term tests s⁻¹w⁻¹xw′∈K(M) and conjugates the character of w′. The remark correctly confines independence of the incidence condition from chosen representatives to integral s, which normalizes K(M).

<a name="page-orbital-integral-of-bessel-vector-is-kloosterman-sum"></a>

### The orbital integral of the finite Bessel vector is a Kloosterman sum

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/orbital-integral-of-bessel-vector-is-kloosterman-sum.knowl.md) · [KloostermanSum.lean:216](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/KloostermanSum.lean#L216)

From a b⁻¹∈sK and integrality of a,b one obtains integrality of s. The right translation by b leaves the second character at x⁻¹y and gives the stated normalization μ(K) times the coset sum.

<a name="page-sieve-system-sum-nonneg-and-lower-semicontinuous"></a>

### Sums of a sieve system over heads with a common entry are nonnegative and lower semicontinuous

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/sieve-system-sum-nonneg-and-lower-semicontinuous.knowl.md) · [SieveSystem.lean:317](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SieveSystem.lean#L317)

I checked the all-ones quadratic form at the top and the update at i+1 in the descending induction. First countability permits the Fatou argument at x, and nonnegativity makes the passage to the real part faithful.

<a name="page-sieve-system-summed-recursion"></a>

### The recursion of a sieve system summed over pairs of heads

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/sieve-system-summed-recursion.knowl.md) · [SieveSystem.lean:250](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/SieveSystem.lean#L250)

No shared entry is required in the initial family because the update imposes it. Finite-sum integrability and the triangle inequality give β(ξ)(∑Λᵢ)² at each unit frequency.

<a name="page-sum-of-inverse-cubed-heights"></a>

### Sum of inverse cubes of heights over a totally complex field

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/sum-of-inverse-cubed-heights.knowl.md) · [Frequencies.lean:253](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/Frequencies.lean#L253)

Grouping by each nonzero denominator costs its norm in coset labels and leaves the inverse square of that norm. The identity \[E:ℚ\]=2f yields the factor e⁴ per infinite place, while the archimedean factors use ordinary complex absolute values.

<a name="page-sum-of-inverse-squared-ideal-norms"></a>

### Bound for the sum of inverse squares of ideal norms

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/spanning-mainterm/sum-of-inverse-squared-ideal-norms.knowl.md) · [Frequencies.lean:102](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/MainTerm/Frequencies.lean#L102)

The zero ideal contributes zero by convention. The Euler-product sum with constant coefficient one and its logarithmic bound at s=σ=2 give exp(2\[E:ℚ\]) for every finite set, as stated.
