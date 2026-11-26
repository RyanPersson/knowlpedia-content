+++
id = "grh-lean"
title = "A guided proof of the Riemann hypothesis and Dirichlet GRH"
kind = "document"
summary = "Read the five statements in grh-lean, follow the prime-sum argument, and unfold its local and global proofs."
domains = ["grh-lean"]
section_mode = "continuous"
prerequisites = ["grh-lean/half-plane", "grh-lean/strip-zeros", "grh-lean/zeta-zeros", "grh-lean/primitive-zeros", "grh-lean/riemann-hypothesis"]
+++

A zero of the [[analytic-number-theory/riemann-zeta-function|Riemann zeta function]] encodes a fluctuation in the distribution of primes. For a [[analytic-number-theory/dirichlet-l-function|Dirichlet \(L\)-function]], the corresponding sums distinguish [[complex-analysis/residue|residue]] classes. The readable edition of Levent Alpöge’s proof with Claude rules out a zero to the right of \(\Re s=1/2\) by bounding one of those sums. The same bound works for every [[analytic-number-theory/dirichlet-character|Dirichlet character]] of positive modulus.

## From a zero back to a prime sum

Fix a character \(\chi\bmod q\) and a putative zero \(\rho\) with \(\Re\rho>1/2\). Pick \(1/2<\beta<\Re\rho\). To detect the zero, take primes in a chosen [[complex-analysis/residue|residue]] class and weight each [[analytic-number-theory/prime-power|prime power]] by a [[analytic-number-theory/legendre-symbol|quadratic character]]. Subtract the expected logarithm and constant. Call the resulting [[analytic-number-theory/prime-remainder-in-progression|prime remainder]] \(R(x)\).

Two claims now meet. Arithmetic gives [[grh-lean/real-cutoffs|\(R(x)\le x^{\beta-1}\) for every sufficiently large \(x\)]]. Analysis gives a [[grh-lean/zero-criterion|one-sided criterion]] saying this bound excludes the zero. Its proof chooses a [[grh-lean/twist-avoidance|quadratic twist with no zeros in the relevant box]], so that the residue of a transform at \(\rho\) counts zeros with a single sign. [[grh-lean/landau|Landau’s argument]] makes that residue vanish.

## Where the square root comes from

At a prescribed integer \(x\), choose [[grh-lean/arithmetic-data|arithmetic data]] with a chain of \(m\) [[arithmetic-geometry/theta-lift|theta lifts]], where \(\sqrt x\le m\le2\sqrt x\). Two estimates measure the same family of forms. Open each theorem to see its hypotheses and proof.

1. [[grh-lean/short-forms|Theorem A · Short forms]]. A spanning family in the source has lifts with bounded size at every conjugate. Its local divisibility records a signed prime-sum remainder.
2. [[grh-lean/enough-forms|Theorem B · Enough forms]]. A small number of translates of the source spans almost every dimension of the target. This lets the short forms test a [[linear-algebra/determinant|determinant]] of nearly full rank.
3. [[grh-lean/long-forms|Theorem C · Integral forms are long]]. The [[arithmetic-geometry/product-formula|product formula]] gives a lower bound for the same [[arithmetic-geometry/twisted-lattice-covolume|squared covolume]], after correcting for the [[arithmetic-geometry/twisted-lattice-index|index]] of the forms.

In the [[grh-lean/main-inequality|comparison]], the main size term cancels. What survives is an upper bound for \(m\) times the total remainder. The [[grh-lean/prime-identity|identity between place sums and prime sums]] turns division by \(m\) into the saving \(x^{-1/2}\). Estimates at a much larger cutoff, followed by [[grh-lean/integer-cutoffs|the integer estimate]] and passage to real \(x\), account for the arbitrarily small loss in the exponent.

## The five formal conclusions

| Public declaration | Mathematical statement and proof |
| --- | --- |
| `LFunction_ne_zero_of_half_lt_re` | [[grh-lean/half-plane|Every Dirichlet \(L\)-function is nonzero to the right of the critical line, except at the principal pole.]] |
| `LFunction_eq_zero_re` | [[grh-lean/strip-zeros|Every zero in the open critical strip has real part \(1/2\).]] |
| `LFunction_eq_zero_re_of_isPrimitive` | [[grh-lean/primitive-zeros|The same conclusion holds for primitive characters.]] |
| `riemannZeta_eq_zero_re` | [[grh-lean/zeta-zeros|Every nontrivial zeta zero has real part \(1/2\).]] |
| `riemannHypothesis` | [[grh-lean/riemann-hypothesis|The zeta statement has exactly Mathlib’s RiemannHypothesis type.]] |

## Reading further

The [[grh-lean/dependencies|dependency index]] collects the proof steps and their mathematical prerequisites. The [Lean declaration index](/grh-lean/declarations/) follows the formal development down to individual statements. This reading follows the 803-module edition in `grh/` at commit `72fead10`. Luke Sernau credits his colleagues at Anthropic and Claude for this shorter rewriting. The compact edition in the same repository uses different intermediate proofs.

## Verification

Andrew Sutherland’s published checks for this exact revision report that both editions compile, that every module replays through Lean’s kernel, and that the five exported theorems depend on propositional extensionality, classical choice and quotient soundness. The formal statements are the four propositions in `Statements.lean` and Mathlib’s own statement of the [[analytic-number-theory/riemann-hypothesis|Riemann hypothesis]].

## References

- [Main.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean)
- [Statements.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean)
- [Alpöge with Claude, reading guide for the pinned readable edition](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/GUIDE.md)
- [Andrew Sutherland, verification files and checker logs for the shorter proof](https://math.mit.edu/~drew/shortgrh/)
- [Luke Sernau, introduction and attribution for the shorter proof](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/README.md)
