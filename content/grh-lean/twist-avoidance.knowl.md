+++
id = "grh-lean/twist-avoidance"
title = "One quadratic twist avoids all the zeros in a box"
kind = "theorem"
summary = "A density estimate for bad primes leaves a usable prime in each allowed residue class."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/quadratic-dirichlet-twist", "analytic-number-theory/dirichlet-functional-equation"]
+++

Fix \(\beta>1/2\) and \(H\ge0\). In an invertible [[complex-analysis/residue|residue]] class whose primes \(d\) are coprime to the modulus \(q\) and \(7\bmod8\), some \(d\) makes every [[analytic-number-theory/quadratic-dirichlet-twist|quadratic twist]] \(F_{\chi(\cdot/d)}\), for \(\chi\bmod q\), nonzero throughout \(\Re s\ge\beta,\ |\Im s|\le H\).

## Proof

A zero forces a large integral of two [[harmonic-analysis/dirichlet-theta-series|theta series]], one for the character and one with Möbius-weighted coefficients. Their [[harmonic-analysis/mellin-transform|integral transforms]] express the completed \(L\)-function and an approximation to its reciprocal. The [[analytic-number-theory/dirichlet-functional-equation|functional equation]] and the [[complex-analysis/three-lines-theorem|three-lines theorem]] between \(\Re s=1/2\) and \(2\) give the lower bound at a zero.

Average the squares of the short theta sums over twists. The diagonal terms have square product of odd parts. For the other terms the [[analytic-number-theory/polya-vinogradov|Pólya–Vinogradov character-sum bound]] gives cancellation. [[analytic-number-theory/quadratic-reciprocity|Quadratic reciprocity]] turns the estimate into \(O(X^{1-\eta})\) exceptional primes up to \(X\) for some \(\eta>0\). Such a set has finite \(\sum_d(\log d)/d\), whereas this sum diverges in the allowed class by the [[analytic-number-theory/prime-number-theorem-progressions|prime number theorem in progressions]].

## References

- [Lib/Analytic/QuadraticTwist.lean, exists_entireL_quadTwist_ne_zero](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L796)
- [Lib/Analytic/QuadraticTwist.lean, zero_density_quadTwist](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean#L732)
