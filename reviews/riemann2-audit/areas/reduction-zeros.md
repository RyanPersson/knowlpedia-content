# reduction-zeros

This area contains 59 individual knowls and a chapter page. The review records 19 comments. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports/reduction-zeros.md)

[Audit overview](../README.md) · [All findings](../findings.tsv)

## Chapter page

<a name="page-reduction-zeros"></a>

### From a one-sided prime-sum bound to the zeros: the final theorems

Correction recorded · page · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros.knowl.md) · [Criterion.lean:37](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/Criterion.lean#L37)

The one-sided criterion correctly quantifies the primes in a fixed coprime class and excludes s=1. The bad-prime count has exponent 1−δ/2 and the reflection exchanges χ and its inverse.

<a name="reduction-zeros-finding-1"></a>

**Medium · The remainder tends to zero for odd d coprime to q.** The chapter-wide notation only assumes that d is prime and q ≥ 1. The independent prime number theorem in this paragraph also requires d ≠ 2 and gcd(d,q)=1. For d=q=3 every n≡1 mod 3 has (n/3)=1, so the entire weighted sum is zero and R₃(y)=−log(y)/2−c₃ tends to minus infinity. State the hypotheses d odd and (d,q)=1 here. Specify likewise at line 49 that the quadratic prime is coprime to the conductor of the primitive character, as holds in the residue class used in the proof. [Knowl line 53](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros.knowl.md#L53) · [PrimeNumberTheorem.lean:217](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L217)

## Knowls with comments

<a name="page-theta-series-of-coefficients"></a>

### Theta series with a Gaussian weight

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/theta-series-of-coefficients.knowl.md) · [DirichletTheta.lean:31](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L31)

The weight and the factor Γ_R(s+j)/2 agree, as do the Gaussian estimates for bounded coefficients and positive argument. The defining display also allows a divergent series.

<a name="theta-series-of-coefficients-finding-1"></a>

**High · The proposed theta series can diverge on its stated domain.** For j = 0, u = 1 and c(n) = exp(πn²), every summand equals 1. Even bounded coefficients c(n) = 1 give the same divergence at u = 0. The source defines a totalized sum and proves classical summability under boundedness and u &gt; 0. State the classical definition on u &gt; 0 under an explicit summability assumption, for example |c(n)| ≤ 1. To retain Lean’s full domain, explain that a nonsummable sum and the real square root at negative u are assigned zero. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/theta-series-of-coefficients.knowl.md#L14) · [DirichletTheta.lean:110](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L110)

<a name="page-theta-tail-integral-and-mollifier"></a>

### The tail integral J and the mollifier

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier.knowl.md) · [QuadraticTwist.lean:61](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L61)

The normalization u^(s−1/2)du/u and the strip estimates agree under bounded coefficients. Pointwise convergence of the Gaussian series above the cutoff is insufficient for convergence of the tail integrals themselves.

<a name="theta-tail-integral-and-mollifier-finding-1"></a>

**High · The ordinary tail integrals can diverge for the allowed coefficients.** Take j=0, T=1 and c(p)=p² exp(πp²) on primes, zero otherwise, so μc=−c. Both theta series converge for every u&gt;1. On 1&lt;u&lt;1+p⁻² the p term of θc(u)/u is at least p² exp(−3π)/√2, so the integral receives a fixed positive contribution from every prime. Thus J is infinite and the ordinary complex mollifier integral diverges at s=1/2. Lean uses totalized integrals and proves integrability under bounded coefficients. Impose |c(n)|≤1 before introducing the ordinary integrals, or state their summability/integrability domain and explain Lean’s values outside it. [Knowl line 14](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier.knowl.md#L14) · [QuadraticTwist.lean:74](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L74)

<a name="theta-tail-integral-and-mollifier-finding-2"></a>

**Low · The full reciprocal Mellin integral has a half-plane restriction.** The last sentence calls the mollifier a truncation of the integral for Γj(s)/L(s,χ) without specifying s. The cited Mellin identity is proved for Re s&gt;1. The strip bound for the truncated transform does not give the same domain for the integral starting at zero. Add “for Re s&gt;1” to the reciprocal integral identification. [Knowl line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier.knowl.md#L32) · [DirichletTheta.lean:243](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L243)

<a name="page-dirichlet-l-zeros-on-line"></a>

### Critical-line form of the generalized Riemann hypothesis

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/dirichlet-l-zeros-on-line.knowl.md) · [Statements.lean:10](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L10)

Both propositions have the open strip 0 &lt; Re s &lt; 1, and the second adds primitivity. The remark overstates when changing the level contributes additional zeros.

<a name="dirichlet-l-zeros-on-line-finding-1"></a>

**Medium · Some imprimitive characters acquire no additional zeros.** The remark assigns extra imaginary-axis zeros to imprimitive characters in general. Inducing the nontrivial primitive character modulo 3 to modulus 9 leaves every value on integers unchanged. The two L-functions coincide, as there is no new prime divisor of the modulus. Say that imprimitive characters can acquire zeros on Re s = 0 from factors 1−ψ(p)p^(−s) for primes p dividing the modulus and not the conductor. [Knowl line 24](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/dirichlet-l-zeros-on-line.knowl.md#L24) · [Primes.lean:120](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L120)

<a name="page-jacobi-symbol-sums"></a>

### Sums of Jacobi symbols with non-square odd modulus

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/jacobi-symbol-sums.knowl.md) · [QuadraticTwist.lean:358](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L358)

The odd nonsquare factorization and nonprincipal twist justification both yield the stated Pólya–Vinogradov estimates. The first part also covers even denominators and needs a definition for them.

<a name="jacobi-symbol-sums-finding-1"></a>

**Medium · The even-denominator Jacobi symbol needs its convention.** Part 1 ranges over every b≥1. The classical Jacobi symbol has odd positive denominator, and the usual Kronecker extension gives (3/2)=−1. The character modulo 2 in Lean necessarily takes value 1 on every odd integer, including 3, so that extension cannot be used in the displayed claim. Define the project’s extension by prime factorization, taking the factor at 2 to be 1 on odd numerators and 0 on even ones. Alternatively state the odd-denominator specialization and restrict the induction accordingly. [Knowl line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/jacobi-symbol-sums.knowl.md#L17) · [QuadraticTwist.lean:309](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L309)

<a name="page-one-sided-criterion"></a>

### The one-sided criterion for a zero-free half-plane

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/one-sided-criterion.knowl.md) · [Criterion.lean:37](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/Criterion.lean#L37)

The zero-free twist removes the negative terms from the residue sum throughout the required height range. The real-axis sign, the exception at 1 and the passage from a zero total multiplicity to nonvanishing of each character agree with Lean.

<a name="one-sided-criterion-finding-1"></a>

**Medium · The application cites an integer bound for a real-variable hypothesis.** The cited eventually_primeRemainder_natCast_le controls integer x only. The hypothesis at line 17 quantifies over every sufficiently large real x, and New.grh invokes eventually_primeRemainder_le_rpow with ε=β−1/2 after the floor comparison and absorption of constants. Link to the real-variable theorem eventually_primeRemainder_le_rpow or to step 2 of the one-sided-bound page. If retaining the explicit constant, label that estimate as the integer intermediate result. [Knowl line 53](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/one-sided-criterion.knowl.md#L53) · [OneSidedBound.lean:262](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L262)

<a name="page-prime-remainder-is-polar"></a>

### The remainder is polar, with residues counting zeros

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/prime-remainder-is-polar.knowl.md) · [PrimeError.lean:414](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L414)

The residue numerator lists untwisted orders minus twisted orders, with the factor s(1−s) in the denominator. At 1 the transform has a removable singularity because G_q(1)=c_q.

<a name="prime-remainder-is-polar-finding-1"></a>

**Medium · The displayed residue function is undefined at zero.** The first branch covers every s≠1, including s=0, where s(1−s)=0. The linked polar definition takes a function on all of ℂ, although its residue requirement only concerns Re s&gt;0. Lean assigns 0 at both denominator zeros. Use the quotient for s outside {0,1} and set r(0)=r(1)=0, or explicitly restrict the displayed residue law to Re s&gt;0 and extend r arbitrarily elsewhere. [Knowl line 17](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/prime-remainder-is-polar.knowl.md#L17) · [PrimeError.lean:415](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L415)

<a name="page-tauberian-theorem"></a>

### A Tauberian theorem with a power of the logarithm

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/tauberian-theorem.knowl.md) · [Tauberian.lean:319](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L319)

I checked the floor in k, the containment of the closed disc in the region, the Gamma variance term, and the powers of u in the final bound. The argument needs the closed-disc version of Cauchy's estimate at its leftmost boundary point.

<a name="tauberian-theorem-finding-1"></a>

**Medium · The Cauchy citation assumes a holomorphic neighborhood at the boundary.** Line 19 assumes complex differentiability at each point of the region, whereas the linked slope lemma asks for F to be holomorphic at every point of the closed disc. For A=0 and R=0, the function F(z)=min(Re z,0)² satisfies line 19 on Re z≥0 and has derivative zero on the boundary, yet it is not holomorphic on any neighborhood of the disc's leftmost point 0. Lean applies the estimate with interior holomorphy and continuity on the closed disc. State the slope lemma and its use with F complex differentiable at each point of the closed disc. Apply Cauchy's estimate on the interior and pass to the boundary by continuity, or explicitly take the limit along smaller concentric circles. [Knowl line 38](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/tauberian-theorem.knowl.md#L38) · [Tauberian.lean:173](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L173)

<a name="page-totient-lower-bound"></a>

### A lower bound for Euler's totient

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/totient-lower-bound.knowl.md) · [Primes.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L56)

The application to the distinct prime factors takes a = 1, and 2^j ≤ n gives the claimed totient bound. The auxiliary inequality as stated lacks the integer hypothesis on its cutoff.

<a name="totient-lower-bound-finding-1"></a>

**Medium · The product estimate requires an integer cutoff.** The proof infers b ≥ a+1 from b &gt; a. As written a need only be nonnegative: with a = 3/2 and S = {2}, the claimed inequality reads 1/2 ≥ 3/5. Also the quotient is 0/0 when a = 0 and S is empty in ordinary arithmetic. For the stated application take a to be a positive integer and give the empty-set base case. To include all natural a as in Lean, write (a+|S|) times the product ≥ a, which includes the zero denominator. [Knowl line 22](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/totient-lower-bound.knowl.md#L22) · [Primes.lean:36](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L36)

<a name="page-weight-lambda-k"></a>

### The weight on prime powers in the class 1 that do not split

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/weight-lambda-k.knowl.md) · [PrimeError.lean:45](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L45)

The indicator of n≡1 mod q, the factor 1−χ_K(n), and the inequalities through 2n agree with the declarations. Interpreting the weight by splitting in the imaginary quadratic field needs an additional condition on d.

<a name="weight-lambda-k-finding-1"></a>

**Medium · The splitting interpretation needs d≡3 modulo 4.** The support formula in terms of the Legendre symbol holds for all prime d, but the title and the final sentence interpret it as splitting in ℚ(√−d) without repeating the necessary qualification. For d=5, q=1, the prime 3 splits because X²+5 reduces to (X−1)(X+1) modulo 3, yet (3/5)=−1 and λ(3)=2 log 3. Keep the formula for general prime d. Explicitly restrict the splitting interpretation to d≡3 mod 4, as the character definition does, and qualify the title or describe the support using χ_K(pᵏ)≠1. [Knowl line 25](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/weight-lambda-k.knowl.md#L25) · [ImaginaryQuadraticField.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean#L56)

<a name="page-zero-free-disc-uniform"></a>

### A zero-free disc about 1, uniform in powers of a fixed modulus

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/zero-free-disc-uniform.knowl.md) · [Primes.lean:138](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L138)

The square-root argument uses the nilpotent constant Mmt, with M = 4m. The descended characters have fixed level M², so their finitely many radii at 1 yield a uniform bound for the pole-removed functions.

<a name="zero-free-disc-uniform-finding-1"></a>

**Medium · The summary gives the derivative bound to the unregularized L-function.** The summary says all L-functions have bounded logarithmic derivative on this disc. For a principal character, L′/L = −1/(s−1) + O(1) near 1, so it is unbounded on every punctured disc about 1. The proposition itself correctly bounds Eχ′/Eχ. Name the pole-removed functions Eχ in the summary and state the bound for their logarithmic derivatives. [Knowl line 5](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/zero-free-disc-uniform.knowl.md#L5) · [Primes.lean:138](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L138)

<a name="page-cauchy-estimate-for-slope"></a>

### Cauchy's estimate for the Taylor coefficients of a slope

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/cauchy-estimate-for-slope.knowl.md) · [Tauberian.lean:192](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L192)

The distance to 1 on the contour is at least η, and the inequality H/(H+η) ≤ exp(−η/(2H)) gives the claimed constant 4MH/η. The polynomial specialization listed in the metadata is developed on the Tauberian theorem page.

<a name="cauchy-estimate-for-slope-finding-1"></a>

**Low · A parameter-dependent estimate is assigned to the wrong page.** The front matter maps norm_taylorCoeff_dslope_le_inv_pow to this page, but the page ends with the exponential estimate. The named declaration also takes u, l, A and B and concludes a bound of u^(−B−1). Its calculation appears in the Tauberian theorem's proof. Move that Lean name to tauberian-theorem, or include its quantitative statement here and link its calculation. [Knowl line 10](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/cauchy-estimate-for-slope.knowl.md#L10) · [Tauberian.lean:292](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L292)

<a name="page-laplace-transform-of-prime-remainder"></a>

### The Laplace transform of the remainder

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/laplace-transform-of-prime-remainder.knowl.md) · [PrimeError.lean:293](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L293)

The r=0 and r=1 terms yield D(s)/(s−1) and D(s)/s. Their difference cancels the transform of v/φ(q) and leaves exactly (G_q(s)/s−c_q)/(s−1).

<a name="laplace-transform-of-prime-remainder-finding-1"></a>

**Low · The Laplace moment helper is in a second source file.** The header claims New.laplace_pow but lists only PrimeError.lean. The source list misses the declaration used for k=0,1 even though the References section gives its actual location. Add src/Lib/Analytic/EntireLFunction.lean to lean_files, or keep laplace_pow solely as a cited dependency if only the prime-remainder proposition is being attributed to this knowl. [Knowl line 11](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/laplace-transform-of-prime-remainder.knowl.md#L11) · [EntireLFunction.lean:105](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean#L105)

<a name="page-log-deriv-mean"></a>

### The mean of logarithmic derivatives G_q

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/log-deriv-mean.knowl.md) · [PrimeError.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L56)

The −1 is inside the numerator before division by φ(q), and the logarithmic derivative of each twist precedes the untwisted one. I also checked the two nonvanishing hypotheses for the local analyticity assertion in PrimeNumberTheorem.lean.

<a name="log-deriv-mean-finding-1"></a>

**Low · The source list omits the general local analyticity lemma.** The header attributes New.analyticAt_logDerivMean to this page but lists only PrimeError.lean. That file contains the half-plane specialization, while the arbitrary-point nonvanishing criterion is in PrimeNumberTheorem.lean as the body references correctly indicate. Add src/New/Reduction/Zeros/PrimeNumberTheorem.lean to lean_files. [Knowl line 11](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/log-deriv-mean.knowl.md#L11) · [PrimeNumberTheorem.lean:152](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L152)

<a name="page-mellin-of-theta-series"></a>

### The Mellin transform of a theta series

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/mellin-of-theta-series.knowl.md) · [DirichletTheta.lean:231](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L231)

Substitution z = nu produces n^(−s), and the absolutely convergent sum of integrals justifies the interchange for Re s &gt; 1. The exponential majorant also gives the asserted strip bound.

<a name="mellin-of-theta-series-finding-1"></a>

**Low · Supply the local uniform bound for holomorphy.** The two majorants as written depend on Re s. They show absolute convergence for fixed s, but the proof does not state the uniform domination on compact subsets or a theorem giving holomorphy of the parameter integral. On a compact subset of Re s &gt; 0, choose 0 &lt; a ≤ Re s ≤ b. Use D t^(a−1) on (0,1\] and D exp(−t)t^(b−1) on \[1,∞), then invoke the holomorphic parameter integral theorem. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/mellin-of-theta-series.knowl.md#L30) · [DirichletTheta.lean:65](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L65)

<a name="page-no-pole-right-of-beta"></a>

### No pole to the right of the exponent of a one-sided bound

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/no-pole-right-of-beta.knowl.md) · [Landau.lean:217](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean#L217)

The residue sign changes when subtracting the polar transform from K/(s−β), and the least upper bound of {β} together with the complement of the convergence set handles both cases. The continuation step needs the meromorphic version of uniqueness.

<a name="no-pole-right-of-beta-finding-1"></a>

**Low · The identity-theorem link covers holomorphic functions only.** The linked knowl assumes both functions holomorphic throughout the domain. At this point Ψ is merely meromorphic and showing that its potential poles are removable is part of the argument. State uniqueness for meromorphic germs, or apply the linked holomorphic theorem on the connected half-plane with the discrete singular set removed. This gives equality on the punctured neighbourhoods used below. [Knowl line 32](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/no-pole-right-of-beta.knowl.md#L32) · [Landau.lean:143](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean#L143)

<a name="page-regularised-l-function"></a>

### The regularised L-function

Correction recorded · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/regularised-l-function.knowl.md) · [LFunctionGrowth.lean:177](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean#L177)

The character mean and the factor (s−δ)/s agree on Re s&gt;1, and the denominator is nonzero on the stated half-plane of holomorphy. The definition excludes one ordinary evaluation for nonprincipal characters.

<a name="regularised-l-function-finding-1"></a>

**Low · The restriction s≠0 also removes the nonprincipal value.** The common restriction on both branches leaves the regularised function undefined at 0 even for a nonprincipal character. Its denominator in that branch is 1, so its value is the ordinary L(0,χ). Apply the restriction only to the principal quotient. State that the nonprincipal branch is L(s,χ) for all s, and, if giving the total Lean convention, that the principal branch is assigned 0 at s=0. [Knowl line 18](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/regularised-l-function.knowl.md#L18) · [LFunctionGrowth.lean:177](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean#L177)

<a name="page-taylor-coefficient-as-gamma-mean"></a>

### A Taylor coefficient of a Laplace transform as a Gamma mean

Correction recorded · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/taylor-coefficient-as-gamma-mean.knowl.md) · [Tauberian.lean:119](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L119)

Differentiation uses the integrable majorant at 2+ε. I checked the moments, the variance (k+1)/H² and its substitution u²/(k+1) in the Lipschitz estimate.

<a name="taylor-coefficient-as-gamma-mean-finding-1"></a>

**Low · The unit-step lemma inherits hypotheses it is meant to establish.** The common preamble requires an exponential bound on R and a transform Φ even for part 4. The Tauberian theorem invokes part 4 before deriving exponential growth, and Lean's abs_sub_le_of_unit_steps uses only the unit-step inequality. The partition argument printed here already proves that version. State part 4 independently for any R satisfying the unit-step inequality. Scope the exponential-growth hypothesis to parts 1–2 and explain that part 3 derives it from the Lipschitz bound. [Knowl line 30](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/taylor-coefficient-as-gamma-mean.knowl.md#L30) · [Tauberian.lean:219](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L219)

## Other knowls checked

<a name="page-bad-primes-are-rare"></a>

### Bad primes are rare

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/bad-primes-are-rare.knowl.md) · [QuadraticTwist.lean:732](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L732)

For d≡7 mod 8 all twists of a fixed primitive character have the opposite parity, so one mean-value estimate bounds the entire count. Passing to T=√(NX) and summing over the finitely many inducing characters gives the exponent 1−δ/2, with the removed Euler factors nonzero for Re s&gt;0.

<a name="page-bound-for-log-deriv-mean-near-one"></a>

### A bound for G_q(s)/s slightly to the left of the line Re s = 1

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/bound-for-log-deriv-mean-near-one.knowl.md) · [PrimeNumberTheorem.lean:178](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L178)

With N = φ(q), the finitely many twisted and untwisted functions give |G_q| ≤ 4Nl^25 + 1. The smaller zero-free region gives |s| ≥ 1/2, and l ≥ 8N+2 absorbs the constant into l^26.

<a name="page-bound-regular-l-near-one-line"></a>

### Growth of the regularised L-function near the line Re s = 1

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/bound-regular-l-near-one-line.knowl.md) · [LFunctionGrowth.lean:297](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean#L297)

On the strip of width 1/3 the left boundary has weight 6/l at s, giving exp(18), and the quotient defining g has denominator 2 there. The disc of radius 1/(2l) fits inside the range with bound l², yielding 2l³ for the derivative.

<a name="page-choice-of-prime"></a>

### Choice of a prime whose twists have no zero in a box

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/choice-of-prime.knowl.md) · [QuadraticTwist.lean:796](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L796)

Under failure of the conclusion every prime of the invertible class is bad. The count with exponent 1−δ/2 makes the log-weighted Dirichlet series converge at 1, contradicting its divergence in that class. The author’s omission of the preliminary reduction β&lt;1 is valid by dyadic summation.

<a name="page-dirichlet-l-nonvanishing-right-of-half"></a>

### Half-plane form of the generalized Riemann hypothesis

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/dirichlet-l-nonvanishing-right-of-half.knowl.md) · [Statements.lean:6](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L6)

The universal quantifiers cover every positive modulus and every character. The exception excludes only the pair consisting of a principal character and s = 1, exactly as in the definition.

<a name="page-dirichlet-series-of-chi-lambda"></a>

### The Dirichlet series of a character times the von Mangoldt function

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/dirichlet-series-of-chi-lambda.knowl.md) · [EntireLFunction.lean:143](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean#L143)

Taking the logarithmic derivative of (s−1)L(s,χ) adds 1/(s−1) only in the principal case. Subtracting this regularized logarithmic derivative gives the indicated Dirichlet series with the correct sign.

<a name="page-dirichlet-series-of-weight"></a>

### The Dirichlet series of the weight

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/dirichlet-series-of-weight.knowl.md) · [PrimeError.lean:263](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L263)

Abel summation at w=s+r−1 gives the common kernel exp((1−s)v) for Re s&gt;2. Orthogonality and the nonprincipal twist for odd d coprime to q leave exactly one 1/(s−1), giving s/\[φ(q)(s−1)\]+G_q(s) for Re s&gt;1.

<a name="page-entire-l-basic-properties"></a>

### Basic properties of the L-function with the pole removed

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/entire-l-basic-properties.knowl.md) · [EntireLFunction.lean:124](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean#L124)

For a principal character the argument at 1 uses the nonzero residue, and away from 1 it uses nonvanishing of L on Re s ≥ 1. The analytic continuation and boundary nonvanishing are declared inputs, and the identity theorem supplies finite order.

<a name="page-euler-factors-nonvanishing"></a>

### Inverse Euler factors do not vanish off the imaginary axis

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/euler-factors-nonvanishing.knowl.md) · [ZeroSymmetry.lean:24](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L24)

Vanishing of one inverse Euler factor forces |χ(p)| = p^(Re s) &gt; 0. A nonzero complex character value has modulus 1, so p &gt; 1 forces Re s = 0 as required.

<a name="page-g-one-and-chowla-selberg-constant"></a>

### The constant c_1 for the modulus 1

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/g-one-and-chowla-selberg-constant.knowl.md) · [PrimeError.lean:166](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L166)

At q=1 the untwisted logarithmic derivative is γ from the constant Laurent coefficient of ζ. Keeping the twisted pole-removed E in the formula also covers d=2, and the sign of γ−Re(E′/E)(1) agrees with the definition of the constant.

<a name="page-g-q-at-one-is-real"></a>

### The value G_q(1) is real

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/g-q-at-one-is-real.knowl.md) · [PrimeError.lean:335](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L335)

The transform of the real remainder shows Im(G_q(x)/x−c_q)=0 for real x&gt;2. Analyticity near each point of the connected real interval \[1,∞) propagates the vanishing to 1 with the oddness and coprimality assumptions intact.

<a name="page-gauss-sum-modulus"></a>

### The modulus of the Gauss sum of a primitive character

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/gauss-sum-modulus.knowl.md) · [PolyaVinogradov.lean:29](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PolyaVinogradov.lean#L29)

I checked the Fourier signs using the positive-exponential convention for τ. Applying the negative-exponential transform twice at −1 gives qχ(1), and the remaining sum becomes the conjugate of τ after replacing a by −a.

<a name="page-growth-of-prime-remainder"></a>

### Exponential growth of the partial sums and of the remainder

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/growth-of-prime-remainder.knowl.md) · [PrimeError.lean:178](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L178)

There are at most exp(v) summands and λ(n)/n≤2. This gives |S_r(exp v)|≤2 exp(v) for all real v, while the remainder estimate uses v≥0 to absorb both v/φ(q) and the constant term.

<a name="page-landau-lemma"></a>

### Landau's lemma

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/landau-lemma.knowl.md) · [Landau.lean:160](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean#L160)

The disc about z has radius ε/2 and reaches every σ between z−ε/2 and a. Since X≤0 and σ≤z, the Taylor coefficients are integrals of nonnegative terms, so monotone convergence gives integrability at σ.

<a name="page-landau-lemma-with-simple-pole"></a>

### Landau's lemma at a simple pole with residue of non-positive real part

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/landau-lemma-with-simple-pole.knowl.md) · [Landau.lean:182](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean#L182)

Equality of germs near real x&gt;a gives M(x)≥0, hence the residue limit is a nonnegative real number. Its assumed nonpositive real part forces it to vanish and permits division of the holomorphic extension by z−a.

<a name="page-legendre-as-jacobi-of-odd-part"></a>

### Reciprocity: the Legendre symbol modulo d as a Jacobi symbol of -d

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/legendre-as-jacobi-of-odd-part.knowl.md) · [QuadraticTwist.lean:628](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L628)

The modulus condition d≡7 mod 8 gives (2/d)=1, and its reduction modulo 4 makes the reciprocity sign exactly (−1/m). The noncoprime case gives zero on both sides and the formula covers odd part m=1.

<a name="page-linear-bound-regular-l"></a>

### A linear bound for the regularised L-function

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/linear-bound-regular-l.knowl.md) · [LFunctionGrowth.lean:213](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean#L213)

The zero-mean character sum is periodic after each block of N consecutive terms, yielding the 2N estimate with the fractional part of x. Partial summation then gives κ+(s−δ)Φ(s), and |s−δ|≤|s| holds up to the boundary Re s=1/2.

<a name="page-lower-bound-right-of-one"></a>

### A lower bound for L-functions to the right of the line Re s = 1

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/lower-bound-right-of-one.knowl.md) · [ZeroFreeRegion.lean:43](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean#L43)

At σ+2it the height can double, while the distance from 1 can only increase. This permits the regularized bounds for both χ and χ² and gives exactly 256l⁷. The two cases at distance 1/l then give 12/l²².

<a name="page-main-theorems"></a>

### The five final theorems

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/main-theorems.knowl.md) · [Main.lean:5](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L5)

The five wrappers give the nontrivial zeta-zero predicate twice, the exact principal-character exception in the half-plane, and the open-strip statement and its primitive specialization. The last is obtained by ignoring the extra primitivity hypothesis, as in Main.lean.

<a name="page-mean-value-theta-jacobi"></a>

### A mean value estimate for theta series with Jacobi symbols

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/mean-value-theta-jacobi.knowl.md) · [QuadraticTwist.lean:536](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L536)

I checked the two weight exponents 1/2+δ and 3/2+δ, the representation kn=ab² and m=ac² for square pairs, and the nonsquare summable exponent −1−δ/2. Cauchy–Schwarz followed by the tail integral gives √C/δ and the Möbius copy doubles it.

<a name="page-measure-for-one-sided-bound"></a>

### The nonnegative measure attached to a one-sided bound

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/measure-for-one-sided-bound.knowl.md) · [Landau.lean:104](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean#L104)

K=max(1,|C|exp(2Y)) handles the bounded initial interval as well as the tail. Weighting Lebesgue measure by the nonnegative difference on v&gt;0 gives the stated sign and factor 1/(s−β) in its transform.

<a name="page-mertens-type-bound"></a>

### A bound of Mertens type

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/mertens-type-bound.knowl.md) · [PrimeError.lean:96](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L96)

For positive N the proof correctly bounds N/n by twice its floor, counts multiples of n, and identifies the resulting divisor sum with log m. The empty sum at N=0 is handled explicitly using the source convention for log 0.

<a name="page-newman-circle-bound"></a>

### The bound on the circle in Newman's method

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/newman-circle-bound.knowl.md) · [Primes.lean:297](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L297)

On |z| = 1/X the real exponent becomes 2−(U+t)Re z for t = X²(1+X Re z)/2. The split at Re z = 1/U uses the head on the left and the two tail majorants on the right with compatible endpoints.

<a name="page-pnt-for-prime-remainder"></a>

### The prime number theorem for the remainders R_q

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/pnt-for-prime-remainder.knowl.md) · [PrimeNumberTheorem.lean:217](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L217)

The twist hypothesis d odd and coprime to q supplies the transform at Re s &gt; 2 with F(1) = c_q. The Tauberian theorem applies with both exponents/constants 26 as specified, then v = log y and B = 1 give the claimed limit.

<a name="page-poisson-summation-for-character-theta"></a>

### Poisson summation for the theta series of a character

Source checked · author’s proof status outline · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/poisson-summation-for-character-theta.knowl.md) · [DirichletTheta.lean:361](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L361)

The positive-exponent inverse Fourier transform has factor 1/q. Summing the shifted kernels gives i^j t after doubling the two positive-index series, with the zero terms removed by character orthogonality. The kernel identities are explicitly cited in the outline.

<a name="page-polar-function"></a>

### Polar function

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/polar-function.knowl.md) · [EntireLFunction.lean:76](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean#L76)

The growth bound is imposed for v ≥ 0, the transform identity for Re s &gt; 2, and the punctured residue limits for Re ρ &gt; 0. The substitution y = exp(v) gives y^(−s)dy as stated.

<a name="page-polya-vinogradov"></a>

### The Pólya–Vinogradov inequality for initial intervals

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/polya-vinogradov.knowl.md) · [PolyaVinogradov.lean:182](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PolyaVinogradov.lean#L182)

The geometric-sum bound has constant q/2 and both reciprocal terms, so the primitive estimate gives √q(1+log q). The Möbius sieve only removes common divisors of v and q/M, and bounding its divisor count by 2√(q/M) gives the stated general constant.

<a name="page-prime-in-log-window"></a>

### A prime congruent to 1 modulo M^k with logarithm in a window

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/prime-in-log-window.knowl.md) · [Primes.lean:389](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L389)

Orthogonality leaves the single 1/z term, giving F(0) = 1/φ(M^k). The circle bound would force exp(X/4) ≤ 3 exp(2) X^(4A), an eventual contradiction uniform in k and U with W = X².

<a name="page-prime-remainder"></a>

### The remainder R_q of the weighted prime sum

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/prime-remainder.knowl.md) · [PrimeError.lean:65](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L65)

On the stated domain x&gt;0, subtracting S₁ from S₀ gives the correct weight 1/n−1/x. Both positive-part cutoffs, the subtraction of Re G_q(1), and the odd-coprime condition for decay agree with their sources.

<a name="page-prime-remainder-as-integral"></a>

### The remainder as an integral of the counting error

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/prime-remainder-as-integral.knowl.md) · [PrimeNumberTheorem.lean:80](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L80)

Partial summation cancels A(y)/y and integrating t/φ(q) against dt/t² gives log(y)/φ(q). The upper bounds 12t for the weight sum and t for the main term imply the stated 13t estimate.

<a name="page-prime-remainder-varies-slowly"></a>

### The remainder varies slowly

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/prime-remainder-varies-slowly.knowl.md) · [PrimeNumberTheorem.lean:116](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L116)

The integrand is bounded in modulus by 13/y throughout \[y,z\]. Under y = exp u and z = exp v the same estimate gives 13(exp(v−u)−1), hence 26(v−u) on steps of length at most one.

<a name="page-quad-twist-not-principal"></a>

### A quadratic twist by an odd prime not dividing the modulus is not principal

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/quad-twist-not-principal.knowl.md) · [EntireLFunction.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean#L56)

The product formula also covers nonunits, where at least one character value vanishes. For odd d coprime to N, the two congruences pick a unit with twisted value −1, proving nonprincipality.

<a name="page-residue-of-log-deriv-entire-l"></a>

### Residues of the logarithmic derivative of an L-function

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/residue-of-log-deriv-entire-l.knowl.md) · [EntireLFunction.lean:180](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean#L180)

Writing E(z) = (z−s)^n g(z) yields the same punctured-neighborhood equality as the source. The limit of (z−s)g′/g is zero because g stays nonzero near s, including when n = 0.

<a name="page-residues-of-log-deriv-mean"></a>

### Residues of G_q and of the transform

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/residues-of-log-deriv-mean.knowl.md) · [PrimeError.lean:363](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L363)

Summing individual logarithmic derivative residues gives the twisted orders minus the untwisted orders. Dividing by ρ(ρ−1) reverses this difference when the denominator is written as ρ(1−ρ), and both excluded points 0 and 1 are retained.

<a name="page-riemann-formula-for-character"></a>

### The L-function of a character as a Mellin transform, and the symmetry of its theta series

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/riemann-formula-for-character.knowl.md) · [DirichletTheta.lean:466](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L466)

The Mellin exponent drops by 1/2 for the square-root normalization. For a primitive character the inverse Fourier transform contributes 1/√q in modulus, and inversion about q^(−1/2) yields the stated factor of two.

<a name="page-riemann-zeta-zeros-on-line"></a>

### The Riemann hypothesis as stated here

Source checked · definition · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/riemann-zeta-zeros-on-line.knowl.md) · [Statements.lean:3](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L3)

The excluded sequence begins at −2 and omits zero, and the condition s ≠ 1 is independent. The direct use of the two propositions interchangeably in Main.lean lines 5 and 8 confirms the identification with Mathlib’s RiemannHypothesis.

<a name="page-twist-of-primitive-is-primitive"></a>

### A quadratic twist of a primitive character is primitive

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/twist-of-primitive-is-primitive.knowl.md) · [QuadraticTwist.lean:644](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L644)

The conductor of the odd-prime quadratic character is d. After raising both factors to level Md, cancellation of either factor shows M divides nd and d divides nM, giving conductor Md by coprimality.

<a name="page-zero-forces-large-tail-integral"></a>

### A zero in the box forces a large tail integral

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/zero-forces-large-tail-integral.knowl.md) · [QuadraticTwist.lean:275](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L275)

I verified the 9/T bound on the right edge, the factor 2J from folding on the left, and the three-lines weight (Re s−1/2)/(3/2)≥6δ. The terminal strictly positive minimum follows from the zero-free Gamma factor on the compact rectangle.

<a name="page-zero-free-region"></a>

### A zero-free region for Dirichlet L-functions

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/zero-free-region.knowl.md) · [ZeroFreeRegion.lean:196](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean#L196)

The shift from s to s+2l⁻²⁵ costs at most 4/l²² against the previously proved 12/l²². I checked both the resulting l²⁵/4 regularized logarithmic derivative and the separate s factor for the principal character.

<a name="page-zero-symmetry"></a>

### Symmetry of the zeros of Dirichlet L-functions

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/zero-symmetry.knowl.md) · [ZeroSymmetry.lean:61](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L61)

The initial Euler-factor product is nonzero off the imaginary axis. The primitive functional equation reflects the completed zero to χ inverse, and multiplying there by the entire reciprocal gamma factor permits a gamma pole at the reflected point.

<a name="page-zeros-on-line-from-half-plane"></a>

### From the half-plane to the critical line for Dirichlet L-functions

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/zeros-on-line-from-half-plane.knowl.md) · [Main.lean:28](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L28)

Positive real part excludes a pole of either parity-dependent Gamma factor. The reflected zero belongs to χ⁻¹ at 1−s, and the open-strip inequalities exclude the principal exceptional point on both applications of the half-plane theorem.

<a name="page-zeta-zeros-on-line-from-half-plane"></a>

### From the half-plane to the critical line for the zeta function

Source checked · author’s proof status full · [Translation](https://github.com/RyanPersson/knowlpedia-content/blob/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh/reduction-zeros/zeta-zeros-on-line-from-half-plane.knowl.md) · [Main.lean:47](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L47)

ζ(0)=−1/2 excludes the additional Gamma pole at zero. The reciprocal Gamma identity gives the reflected zero, and the modulus-one half-plane bound applies to both s and 1−s because neither equals 1.
