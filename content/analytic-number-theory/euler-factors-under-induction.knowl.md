+++
id = "analytic-number-theory/euler-factors-under-induction"
title = "Euler factors under induction of a Dirichlet character"
kind = "theorem"
summary = "Changing modulus adds finitely many inverse Euler factors and preserves the zeros off the imaginary axis away from poles."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/induced-dirichlet-character","analytic-number-theory/dirichlet-l-function","langlands/euler-product-and-local-factor","complex-analysis/identity-theorem","complex-analysis/analytic-continuation"]
+++

If \(\chi\bmod q\) is [[analytic-number-theory/induced-dirichlet-character|induced]] from \(\psi\bmod f\), \(f\mid q\), their [[analytic-number-theory/dirichlet-l-function|Dirichlet \(L\)-functions]] satisfy the meromorphic identity
\[
 L(s,\chi)=L(s,\psi)\prod_{p\mid q}(1-\psi(p)p^{-s}).
\]
The finite product is nonzero whenever \(\Re s\ne0\).

## Proof

For \(\Re s>1\) take the absolutely convergent [[langlands/euler-product-and-local-factor|Euler products]]. The local factors agree for primes outside \(q\). For primes dividing \(q\), \(\chi(p)=0\), so the displayed factor cancels the factor for \(\psi\). The [[complex-analysis/identity-theorem|identity theorem]] extends the equality by [[complex-analysis/analytic-continuation|meromorphic continuation]].

If \(\psi(p)=0\), its correction factor is \(1\). Otherwise \(\psi(p)\) has absolute value \(1\), since a character on a finite group takes values that are roots of unity. If \(1-\psi(p)p^{-s}=0\), then \(1=|\psi(p)p^{-s}|=p^{-\Re s}\). Since \(p>1\), this forces \(\Re s=0\).

## References

- [Nonvanishing of the correction factors](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L24)
- [Use of the change-of-level identity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L61)
