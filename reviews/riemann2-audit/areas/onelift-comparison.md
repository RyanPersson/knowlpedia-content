# onelift-comparison

This area contains 14 individual knowls. The review records 14 comments.

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Knowls with comments

<a name="page-one-exchange"></a>

### One exchange: confining the twist to a pair of equal rank

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/one-exchange.knowl.md) · [OneExchange.lean:223](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean#L223)

The right-invariant datum does produce a matched partner for χ⁻¹, and an invertible top block supplies the left inverse needed for convergence. The kernel identity requires coordinated twists on the three pairs.

<a name="one-exchange-finding-1"></a>

**High · The direct-sum kernel needs the product of the two twists.** The combined kernel has twists (a, ββ′), while the two factors have (a, β) and (a, β′). The page suppresses the characters without giving this relation. Using the same two twists in all three kernels, for instance, counts β twice on the product side. Fix a, β, β′ and specify the three character pairs in the assumed exchange identity, the product formula and its summed version. [Knowl line 21](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/one-exchange.knowl.md#L21) · [OneExchange.lean:233](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean#L233)

<a name="one-exchange-finding-2"></a>

**Low · Give the value when the determinant is a nonunit.** Φ₀ is presented on every matrix using x″⁻¹, and the proof removes −y′⁻¹ by GL-invariance. In ordinary matrix notation those expressions are undefined for non-invertible blocks. Lean treats the y′ case separately using the zero of χ at a nonunit. Define Φ₀ to be zero for non-invertible x″. In the matching argument apply invariance when y′ is invertible and use χ(det y′)=0 otherwise. [Knowl line 23](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/one-exchange.knowl.md#L23) · [OneExchange.lean:205](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean#L205)

<a name="one-exchange-finding-3"></a>

**Low · Both references for matching point to the wrong namespace.** The assumptions link to New.Exchange.AreMatched (line 19) and the proof to New.Exchange.areMatched_block. Their declarations are New.AreMatched in PartnerAlgebra.lean:76 and New.Rows.areMatched_block in MatchingPartners.lean:74. Link to New.AreMatched and New.Rows.areMatched_block, specifying the whole residue ring and the displayed block decomposition. [Knowl line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/one-exchange.knowl.md#L38) · [MatchingPartners.lean:74](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Exchange/MatchingPartners.lean#L74)

<a name="page-class-sum-at-row-stabilizer"></a>

### Class sums at the level of a row stabilizer

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/class-sum-at-row-stabilizer.knowl.md) · [OneExchange.lean:499](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean#L499)

The tower index and the two signed substitutions give the stated class-sum identity. The proof reverses the determinant character in its last translation.

<a name="class-sum-at-row-stabilizer-finding-1"></a>

**Medium · The character multiplying a translated datum is inverted.** For a lift k reducing to A, the source translates Ψ to χ(det A) Ψ(A⁻¹x). Substitution into χ(det x″) introduces χ(det A)⁻¹. The proof calls the prefactor χ(det A)⁻¹, which does not give the cancellation for a general character. Write the twisted translate explicitly as χ(det A) Ψ(A⁻¹x) and identify χ(det A)⁻¹ as the factor coming from the argument. [Knowl line 45](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/class-sum-at-row-stabilizer.knowl.md#L45) · [OneExchange.lean:526](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean#L526)

<a name="page-descent-of-point-form"></a>

### The descent of a point form is a conjugate theta kernel

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/descent-of-point-form.knowl.md) · [TestedForms.lean:277](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L277)

The class sum evaluates the conjugate kernel at the chosen point. The inverse of its finite lift transfers the prescribed columns at M and the selected determinant rows at Q, giving the three stated identities.

<a name="descent-of-point-form-finding-1"></a>

**Medium · State the scope of adjointness for normalized descent.** The introduction calls normalized descent adjoint to the theta lift for every descent pair in the setup. It exists there as a class sum (AuxiliaryPair.lean:371). The adjoint identity for the lift from W chooses a source parameter fitting O, a form of the corresponding type, and requires nonempty rank index r. Introduce the map by its class-sum definition. When describing the adjoint interpretation, specify positive rank and a fitted parameter and identify the source space of the lift. [Knowl line 15](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/descent-of-point-form.knowl.md#L15) · [AdjointThetaLift.lean:297](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Norms/AdjointThetaLift.lean#L297)

<a name="page-point-form"></a>

### Class forms and point forms

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/point-form.knowl.md) · [TestedForms.lean:201](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L201)

The full definition is the unnormalized transporter sum with ρ(γ)⁻¹, and the point form replaces h by hA. The summary gives that construction an incorrect evaluation property.

<a name="point-form-finding-1"></a>

**Medium · The input vector need not equal the value of the point form.** At its center the delta form is the stabilizer sum of the weighted transforms of v. For trivial weight and character it has value #Aut(h) · v, which need not equal v. The displayed formula in the body is correct. Describe the form as supported on the specified class and formed from v by the transporter sum. If its central value is mentioned, give the stabilizer sum. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/point-form.knowl.md#L5) · [HeckeEigenforms.lean:217](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/HeckeEigenforms.lean#L217)

<a name="page-test-form"></a>

### Test form of a descent pair

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/test-form.knowl.md) · [TestedForms.lean:392](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L392)

The all-embeddings integral lattice, the descent kernel, and the rank-one group mean agree with the source. The local idempotent has an essential zero convention outside rank one.

<a name="test-form-finding-1"></a>

**Medium · Explain the X−1 idempotent outside rank one.** A label for GL_r must have degree |r|. The formal labelIdem returns zero for a polynomial of the wrong degree. Thus for |r| ≠ 1 and a nonempty family M the tensor e₀ is zero, the false-lift space is zero, and the test condition reduces to integrality. The page describes X−1 as a label idempotent without specifying this branch. State that an invalid-rank label contributes the zero idempotent, and give the consequence for positive-size M. An empty tensor remains the unit. [Knowl line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/test-form.knowl.md#L17) · [TauFunctions.lean:171](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/LocalGL/Green/TauFunctions.lean#L171)

<a name="test-form-finding-2"></a>

**Low · Point the integral-lattice reference to its declaration.** New.integralForms is not the name of this lattice. The integralForms used by IsTestForm is in the New.LevelPlaces.LevelForm namespace. Use New.LevelPlaces.LevelForm.integralForms as the Lean target. [Knowl line 16](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/test-form.knowl.md#L16) · [PAdicGauge.lean:738](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/AutomorphicForms/PAdicGauge.lean#L738)

<a name="page-adjoint-of-hecke-polynomial"></a>

### Adjoint of the Hecke polynomial operator for the conjugate pairings

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/adjoint-of-hecke-polynomial.knowl.md) · [TestedForms.lean:340](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L340)

The smooth extension is the level index times the invariant Gram pairing. Passing a split double coset across the pairing conjugates the place and sends the argument to σ⁻¹(conj(σX)), as in the cited general adjoint theorem.

<a name="adjoint-of-hecke-polynomial-finding-1"></a>

**Low · Give the upper bound of the Hecke polynomial sum.** The index of the sum defining H_w(X) is left unspecified. Its degree bound is the rank |n| of the larger space V, and the constant term is included. Write the summation as i = 0,…,|n|. [Knowl line 19](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/adjoint-of-hecke-polynomial.knowl.md#L19) · [SplitHecke.lean:371](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Unramified/SplitHecke.lean#L371)

<a name="page-denominator-bound"></a>

### Denominator bound for the projection to a space of forms

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/denominator-bound.knowl.md) · [TestedForms.lean:413](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L413)

The determinant bound uses dim Z times the rank of W. The projected input is integral at the chosen isomorphism, whereas the test vectors paired with its image must be integral at every ℓ-adic embedding.

<a name="denominator-bound-finding-1"></a>

**Low · The exponent β′ in the denominator interpretation is undefined.** The definition bounds |det Λ| below by exp(−dim Z · |r| · β). The remark switches to ℓ raised to −β′ without defining β′, so it is impossible to recover the factor in those units from the remark. Give the per-dimension, per-row lower factor as exp(−β), or set β′ = β/log ℓ before writing ℓ^(−β′). [Knowl line 29](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/denominator-bound.knowl.md#L29) · [TestedForms.lean:416](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L416)

<a name="page-false-lifts"></a>

### False lifts and forms orthogonal to them

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/false-lifts.knowl.md) · [TestedForms.lean:373](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L373)

The definition takes the intersection of the range of e₀, the kernel at the specified root, and Z, separately at each admissible place. Orthogonality uses the pairing at the identity automorphism.

<a name="false-lifts-finding-1"></a>

**Low · The summary unnecessarily requires an idempotent.** The formal definition and the body allow any element e₀ of the chosen-place group algebra. Idempotence is used in later projection results. The summary calls every input an idempotent. Describe the first factor as the image of a group-algebra element e₀, which in the applications can be an idempotent. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/false-lifts.knowl.md#L5) · [TestedForms.lean:373](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L373)

<a name="false-lifts-finding-2"></a>

**Low · Identify the character entering the Hecke root.** The introduction lists the tame character μ, then the formula introduces a different character χ_W without identifying the Weil data that determine it. Its rank-r Frobenius value uses the Weil splitting character, and χ_W itself is υ_U(1) raised to the number of minus signs of W (AuxiliaryPair.lean:332). Fix the Weil data and identify χ_W when defining the root, or link directly to the two attached characters of a descent pair. [Knowl line 20](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/false-lifts.knowl.md#L20) · [AuxiliaryPair.lean:413](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/AuxiliaryPair.lean#L413)

<a name="page-point-lift"></a>

### Point lift: an integral element with prescribed columns and rows

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/point-lift.knowl.md) · [TestedForms.lean:93](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L93)

Independent columns are extended to local bases at M, and a transposed completion gives the specified rows at Q. Surjectivity of simultaneous reduction produces one level element supported on these places and their conjugates.

<a name="point-lift-finding-1"></a>

**Low · Correct the reference for simultaneous reduction.** New.stdLevel.exists_reduceFamily_eq is not the declaration that lifts the whole residue family. The source uses New.exists_reduceFamily_eq, which also supplies the required support property. Replace the Lean target with New.exists_reduceFamily_eq. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/point-lift.knowl.md#L27) · [CongruenceLevels.lean:330](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Unitary/CongruenceLevels.lean#L330)

<a name="page-row-stabilizer-and-column-datum"></a>

### Row stabilizer and column datum

Correction recorded · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/row-stabilizer-and-column-datum.knowl.md) · [OneExchange.lean:102](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean#L102)

Writing z=1+uιᵀ gives the claimed determinant and reduces both row conditions to wφ(u)=0. The displayed formula needs a convention outside the invertible locus.

<a name="row-stabilizer-and-column-datum-finding-1"></a>

**Low · The right side calls for an inverse of every square matrix.** The stated domain includes singular z, for which ordinary z⁻¹ and hence F(z⁻¹y) are undefined even after multiplying by an indicator. The source puts the expression within the membership branch of an if. Give the right side as χ(det z)F(z⁻¹y) for z∈H and 0 otherwise, or declare this zero-extension convention. [Knowl line 27](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/row-stabilizer-and-column-datum.knowl.md#L27) · [OneExchange.lean:107](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean#L107)

## Other knowls checked

<a name="page-hecke-polynomial-is-normal"></a>

### The idempotent is self-adjoint and the Hecke polynomial is normal at every conjugate

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/hecke-polynomial-is-normal.knowl.md) · [TestedForms.lean:505](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L505)

The conjugate-place polynomial provides a commuting adjoint at every σ. The proof of self-adjointness for a central idempotent uses the finite-group character of its image, so the conjugation identities hold after applying σ.

<a name="page-inner-product-with-point-form"></a>

### Inner product with a class form is evaluation at the point

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/inner-product-with-point-form.knowl.md) · [TestedForms.lean:138](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L138)

The transporter terms in a class contribute the same invariant Gram pairing. Their number cancels the reciprocal stabilizer factor, giving exactly the pairing of v with the value at h and, after translating h, at hA.

<a name="page-projection-to-lifts-does-not-increase-norm"></a>

### Projection to a space of lifts does not increase any conjugate norm

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/projection-to-lifts-does-not-increase-norm.knowl.md) · [TestedForms.lean:591](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/TestedForms.lean#L591)

The decomposition from false-lift orthogonality allows arbitrary Z. The norm bound next requires Z to lie in both the central idempotent image and the Hecke kernel at one place. Orthogonality at all σ identifies the same projection defined at σ = 1.

<a name="page-sum-of-translates-of-datum"></a>

### Translates of a datum give the same period

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/onelift-comparison/sum-of-translates-of-datum.knowl.md) · [OneExchange.lean:316](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/OneExchange.lean#L316)

Reduction from the smaller ideal and right multiplication by γ occur in that order. A lift of γ contributes no β′ factor, and the source pairs rapid decay of F with moderate growth of the kernel to justify integrating the finite sum.
