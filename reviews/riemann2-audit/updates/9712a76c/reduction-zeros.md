# reduction-zeros

19 page records. Of 19 earlier findings, 19 are resolved. This review adds 0 findings. [Author’s report](https://github.com/RyanPersson/knowlpedia/blob/12cc7330341b6b4fb72c78b91a659e67e82a4b18/docs/riemann2/reports/reduction-zeros.md)

[Review overview](README.md) · [Status of earlier findings](response-ledger.tsv) · [New findings](findings.tsv)

<a name="page-reduction-zeros"></a>

## From a one-sided prime-sum bound to the zeros: the final theorems

Revised · page · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros.knowl.md) · [PrimeNumberTheorem.lean:233](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L233)

The independent prime number theorem takes an odd prime d and a modulus q coprime to d. The chapter also restores the analogous oddness and coprimality requirements for primitivity of a quadratic twist at line 49.

<a name="prior-reduction-zeros-1"></a>

**Resolved · medium · The remainder tends to zero for odd d coprime to q.** Lines 25, 49 and 53 now separate the ambient notation from the hypotheses of the two results. For d=q=3 all integers counted are 1 modulo 3, so the weight vanishes and the stated counterexample is correct. [Knowl, line 53](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros.knowl.md#L53) · [PrimeNumberTheorem.lean:217](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L217)

<a name="page-cauchy-estimate-for-slope"></a>

## Cauchy's estimate for the Taylor coefficients of a slope

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/cauchy-estimate-for-slope.knowl.md) · [Tauberian.lean:192](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L192)

The slope extends analytically at 1, which is inside the disc, and continuously to its boundary. The bound |s−1|≥η on the outer circle and the limit over inner circles yield the stated factor 4MH/η and exponential decay.

<a name="prior-cauchy-estimate-for-slope-1"></a>

**Resolved · low · A parameter-dependent estimate is assigned to the wrong page.** The front matter now stops at the exponential estimate and the geometry of the disc. The parameter-dependent u^(−B−1) corollary has a single owner, tauberian-theorem, which includes its calculation in lines 38–42 and cites it at line 52. [Knowl, line 10](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/cauchy-estimate-for-slope.knowl.md#L10) · [Tauberian.lean:292](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L292)

<a name="page-dirichlet-l-zeros-on-line"></a>

## Critical-line form of the generalized Riemann hypothesis

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/dirichlet-l-zeros-on-line.knowl.md) · [Statements.lean:10](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L10)

The open-strip propositions still quantify over all characters and over the primitive subclass. The added Euler factors now range over the prime divisors of the larger modulus that do not divide the conductor.

<a name="prior-dirichlet-l-zeros-on-line-1"></a>

**Resolved · medium · Some imprimitive characters acquire no additional zeros.** The remark correctly locates the possible additional zeros on Re s=0. Raising the modulus from 3 to 9 adds no prime factor and leaves that nonprincipal L-function unchanged. [Knowl, line 24](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/dirichlet-l-zeros-on-line.knowl.md#L24) · [Primes.lean:120](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L120)

<a name="page-jacobi-symbol-sums"></a>

## Sums of Jacobi symbols with non-square odd modulus

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/jacobi-symbol-sums.knowl.md) · [QuadraticTwist.lean:309](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L309)

At modulus two the character equals one on odd inputs and zero on even inputs. The nonprincipality and Pólya–Vinogradov steps still use an odd nonsquare modulus, with the odd part of n in the final estimate.

<a name="prior-jacobi-symbol-sums-1"></a>

**Resolved · medium · The even-denominator Jacobi symbol needs its convention.** Multiplicativity over prime factors now fixes every positive denominator, including the factor at two. This agrees with the induction by a Legendre twist and gives (3/2)=1 in the convention used here. [Knowl, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/jacobi-symbol-sums.knowl.md#L15) · [QuadraticTwist.lean:318](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L318)

<a name="page-laplace-transform-of-prime-remainder"></a>

## The Laplace transform of the remainder

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/laplace-transform-of-prime-remainder.knowl.md) · [PrimeError.lean:293](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L293)

For odd d coprime to q and Re(s)&gt;2, the two partial sums contribute D(s)/(s−1) and D(s)/s. Subtracting the constant and linear Laplace moments gives exactly (G_q(s)/s−c_q)/(s−1).

<a name="prior-laplace-transform-of-prime-remainder-1"></a>

**Resolved · low · The Laplace moment helper is in a second source file.** The revised header includes EntireLFunction.lean. Its laplace_pow applies at s−1 for both k=0 and k=1, exactly as in PrimeError.lean lines 309–310. [Knowl, line 11](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/laplace-transform-of-prime-remainder.knowl.md#L11) · [EntireLFunction.lean:105](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/EntireLFunction.lean#L105)

<a name="page-log-deriv-mean"></a>

## The mean of logarithmic derivatives G_q

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/log-deriv-mean.knowl.md) · [PrimeError.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L56)

The displayed mean subtracts 1 inside the numerator before division by φ(q). The local analyticity criterion needs all twisted and untwisted pole-removed functions nonzero at the point, a property available throughout Re(s)≥1.

<a name="prior-log-deriv-mean-1"></a>

**Resolved · low · The source list omits the general local analyticity lemma.** Both source files appear in the header. PrimeNumberTheorem.lean contains the general local nonvanishing criterion, and PrimeError.lean line 172 contains the specialization to Re(s)≥1. [Knowl, line 11](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/log-deriv-mean.knowl.md#L11) · [PrimeNumberTheorem.lean:152](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L152)

<a name="page-mellin-of-theta-series"></a>

## The Mellin transform of a theta series

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/mellin-of-theta-series.knowl.md) · [DirichletTheta.lean:231](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L231)

The substitution z=nu produces n^(−s), and the compact-set majorant now justifies the separate holomorphy assertion throughout Re s&gt;0. The reciprocal Mellin identity is still confined to Re s&gt;1.

<a name="prior-mellin-of-theta-series-1"></a>

**Resolved · low · Supply the local uniform bound for holomorphy.** For a compact subset choose 0&lt;a≤Re s≤b. The revised proof dominates the Mellin integrand by D t^(a−1) below one and D exp(−t)t^(b−1) above one, both integrable independently of s. The linked parameter-integral theorem applies to the stated measurable f. [Knowl, line 30](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/mellin-of-theta-series.knowl.md#L30) · [DirichletTheta.lean:65](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L65)

<a name="page-no-pole-right-of-beta"></a>

## No pole to the right of the exponent of a one-sided bound

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/no-pole-right-of-beta.knowl.md) · [Landau.lean:217](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean#L217)

The polar residue for the difference Ψ=K/(s−β)−Φ is −r(ρ) on Re ρ&gt;β. Equality of the punctured germs there suffices both for the zero residue when a=β and for the abscissa contradiction when a&gt;β.

<a name="prior-no-pole-right-of-beta-1"></a>

**Resolved · low · The identity-theorem link covers holomorphic functions only.** With the usual meromorphic representative of the linked definition, deleting the relatively closed discrete pole set leaves a connected open set on which both functions are holomorphic. Agreement far to the right gives equality there and hence on punctured neighborhoods, exactly the conclusion of the source lemma. [Knowl, line 32](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/no-pole-right-of-beta.knowl.md#L32) · [Landau.lean:143](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean#L143)

<a name="page-one-sided-criterion"></a>

## The one-sided criterion for a zero-free half-plane

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/one-sided-criterion.knowl.md) · [Criterion.lean:37](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/Criterion.lean#L37)

The criterion quantifies over all sufficiently large real x for each prime in the residue class. In its application the floor estimate contributes 26/y and the constant 2C+26 is absorbed before the real-variable theorem is used.

<a name="prior-one-sided-criterion-1"></a>

**Resolved · medium · The application cites an integer bound for a real-variable hypothesis.** The revised remark links the real-variable theorem with q₀=18480q, d₀=q₀/2−1 and ε=β−1/2, so −1/2+ε=β−1. It identifies the integer estimate as an intermediate step. [Knowl, line 53](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/one-sided-criterion.knowl.md#L53) · [OneSidedBound.lean:262](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L262)

<a name="page-prime-remainder-is-polar"></a>

## The remainder is polar, with residues counting zeros

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/prime-remainder-is-polar.knowl.md) · [PrimeError.lean:414](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L414)

The numerator is the untwisted zero multiplicity minus the twisted one. The factor 1−s supplies the compensating sign when the residue of G_q is divided by s(s−1). The possible singularity at 1 is removable because G_q(1)=c_q.

<a name="prior-prime-remainder-is-polar-1"></a>

**Resolved · medium · The displayed residue function is undefined at zero.** The revised formula assigns 0 at both denominator zeros and uses the quotient away from {0,1}. The remarks distinguish Lean’s value at zero from the punctured residue limits required only for Re(s)&gt;0. [Knowl, line 17](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/prime-remainder-is-polar.knowl.md#L17) · [PrimeError.lean:418](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L418)

<a name="page-regularised-l-function"></a>

## The regularised L-function

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/regularised-l-function.knowl.md) · [LFunctionGrowth.lean:177](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean#L177)

The denominator is s in the principal branch and 1 in the nonprincipal branch. On Re s&gt;0 it never vanishes, which gives the stated differentiability.

<a name="prior-regularised-l-function-1"></a>

**Resolved · low · The restriction s≠0 also removes the nonprincipal value.** The nonprincipal branch now gives Eχ(s)=L(s,χ) on all of ℂ, including zero. Line 18 separately records the source’s assigned value 0 for the principal branch at zero. [Knowl, line 16](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/regularised-l-function.knowl.md#L16) · [LFunctionGrowth.lean:177](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean#L177)

<a name="page-riemann-zeta-zeros-on-line"></a>

## The Riemann hypothesis as stated here

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/riemann-zeta-zeros-on-line.knowl.md) · [Statements.lean:3](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L3)

The header now claims only the locally declared RiemannZetaZerosOnLine. Its exclusion of the negative even integers and of s=1 agrees with the statement in the cited source, and the imported Mathlib name is still credited in References.

<a name="page-tauberian-theorem"></a>

## A Tauberian theorem with a power of the logarithm

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/tauberian-theorem.knowl.md) · [Tauberian.lean:319](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L319)

The closed Cauchy disc lies in the region Re s≥1−l^(−A), |s|≤eˡ, giving pointwise complex differentiability on the disc. Combining l^(2A)≤u, 4H≤u^(2B+5) and the exponential bound gives |T|≤u^(−B−1).

<a name="prior-tauberian-theorem-1"></a>

**Resolved · medium · The Cauchy citation assumes a holomorphic neighborhood at the boundary.** The application and the revised slope lemma both use differentiability at points of the closed disc. Cauchy’s inequality is applied on smaller circles and passed to the boundary by continuity, matching the source’s holomorphy inside and continuity up to the boundary. [Knowl, line 38](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/tauberian-theorem.knowl.md#L38) · [Tauberian.lean:173](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L173)

<a name="page-taylor-coefficient-as-gamma-mean"></a>

## A Taylor coefficient of a Laplace transform as a Gamma mean

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/taylor-coefficient-as-gamma-mean.knowl.md) · [Tauberian.lean:119](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L119)

Partitioning \[x,y\] into n&gt;y−x equal steps proves the global Lipschitz bound on the nonnegative half-line. Part 3 derives the required exponential growth from that Lipschitz bound and uses variance u²/(k+1) in the Gamma estimate.

<a name="prior-taylor-coefficient-as-gamma-mean-1"></a>

**Resolved · low · The unit-step lemma inherits hypotheses it is meant to establish.** The new preamble explicitly exempts part 4 from the transform, measurability and exponential bound. The growth bound is assumed in parts 1–2 and derived in part 3, which is exactly the order needed in the Tauberian proof. [Knowl, line 15](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/taylor-coefficient-as-gamma-mean.knowl.md#L15) · [Tauberian.lean:219](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/PrimeNumberTheorem/Tauberian.lean#L219)

<a name="page-theta-series-of-coefficients"></a>

## Theta series with a Gaussian weight

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/theta-series-of-coefficients.knowl.md) · [DirichletTheta.lean:110](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L110)

For positive u the Gaussian estimate bounds each summand by 3 exp(−2nu) whenever |c(n)|≤1. The classical definition and the explanation of Lean’s zero value for a nonsummable series now handle the two different domains.

<a name="prior-theta-series-of-coefficients-1"></a>

**Resolved · high · The proposed theta series can diverge on its stated domain.** Both positivity of u and bounded coefficients now precede the displayed definition. Line 35 explicitly covers the totalized sum and gives the earlier divergence example outside the classical domain. [Knowl, line 14](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/theta-series-of-coefficients.knowl.md#L14) · [DirichletTheta.lean:110](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L110)

<a name="page-theta-tail-integral-and-mollifier"></a>

## The tail integral J and the mollifier

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier.knowl.md) · [QuadraticTwist.lean:74](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L74)

The lower cutoff 1/T is positive. On that tail both c and μc satisfy the Gaussian decay bound, which makes the integral defining the mollifier absolutely convergent for each fixed complex s.

<a name="prior-theta-tail-integral-and-mollifier-1"></a>

**Resolved · high · The ordinary tail integrals can diverge for the allowed coefficients.** The opening now imposes |c(n)|≤1 and T&gt;0. Applying the theta bound to both c and μc controls J and the mollifier even with the power u^(s−1/2) present. Line 35 describes the totalized integrals. [Knowl, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier.knowl.md#L22) · [QuadraticTwist.lean:74](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L74)

<a name="prior-theta-tail-integral-and-mollifier-2"></a>

**Resolved · low · The full reciprocal Mellin integral has a half-plane restriction.** The comparison with the integral over all positive u now states Re s&gt;1, exactly the hypothesis for the Mellin transform of χμ to equal Γ_j(s)/L(s,χ). [Knowl, line 31](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/theta-tail-integral-and-mollifier.knowl.md#L31) · [DirichletTheta.lean:243](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L243)

<a name="page-totient-lower-bound"></a>

## A lower bound for Euler's totient

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/totient-lower-bound.knowl.md) · [Primes.lean:56](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L56)

For n=1 the empty product gives equality. For positive n the induction with cutoff 1 gives φ(n)/n≥1/(1+j), with 2^j≤n supplying j≤2 log n.

<a name="prior-totient-lower-bound-1"></a>

**Resolved · medium · The product estimate requires an integer cutoff.** The product induction now assumes an integer a≥1 and treats the empty set. Removing its least element b gives b≥a+1. The separate remark also accounts for the zero-cutoff and empty-set case under Lean’s division convention. [Knowl, line 22](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/totient-lower-bound.knowl.md#L22) · [Primes.lean:36](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L36)

<a name="page-weight-lambda-k"></a>

## The weight on prime powers in the class 1 with Legendre symbol different from 1

Revised · definition · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/weight-lambda-k.knowl.md) · [PrimeError.lean:45](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L45)

The support condition is χ_K(p^k)≠1 on prime powers congruent to 1 modulo q. For d≡3 mod 4, multiplicativity explains vanishing at split primes and even powers of inert primes.

<a name="prior-weight-lambda-k-1"></a>

**Resolved · medium · The splitting interpretation needs d≡3 modulo 4.** The title uses the Legendre symbol and the body restricts the splitting interpretation to d≡3 mod 4. Its example is correct: 3 splits in Q(√−5) while 3 is a nonsquare modulo 5. [Knowl, line 25](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/weight-lambda-k.knowl.md#L25) · [ImaginaryQuadraticField.lean:58](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/ImaginaryQuadraticField.lean#L58)

<a name="page-zero-free-disc-uniform"></a>

## A zero-free disc about 1, uniform in powers of a fixed modulus

Revised · full · [Knowl](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/zero-free-disc-uniform.knowl.md) · [Primes.lean:138](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L138)

For k&gt;1, the proof factors characters whose square is principal through M² and uses the resulting finite family to choose one scale. The bounds ‖s−1‖≤1/X and 2l²⁵≤X lead to the displayed estimate for Eχ.

<a name="prior-zero-free-disc-uniform-1"></a>

**Resolved · medium · The summary gives the derivative bound to the unregularized L-function.** The summary now explicitly removes the pole for principal characters and assigns the derivative bound to those pole-removed functions. This agrees with the bound on |logDeriv(entireL χ)| at every point of the closed disc, including its center. [Knowl, line 5](https://github.com/RyanPersson/knowlpedia-content/blob/9712a76c5437e43a3c0af1665f02b9d9203c5bd8/content/proofs/grh/reduction-zeros/zero-free-disc-uniform.knowl.md#L5) · [Primes.lean:140](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Primes.lean#L140)
