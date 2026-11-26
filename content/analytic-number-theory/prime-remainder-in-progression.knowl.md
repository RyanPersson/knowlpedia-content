+++
id = "analytic-number-theory/prime-remainder-in-progression"
title = "Centered quadratic prime sum in a residue class"
kind = "definition"
summary = "A ramp-weighted sum in the identity residue class with its logarithmic main term and limiting constant removed."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/legendre-symbol", "analytic-number-theory/von-mangoldt-function", "analytic-number-theory/euler-totient", "analytic-number-theory/quadratic-dirichlet-twist", "analytic-number-theory/entire-dirichlet-l-function"]
+++

Let \(q\ge1\) and let \(d\) be an odd prime coprime to \(q\). Set \(\lambda(n)=\mathbf1_{n\equiv1\bmod q}\Lambda(n)(1-(n/d))\), using the [[analytic-number-theory/von-mangoldt-function|von Mangoldt function]] and [[analytic-number-theory/legendre-symbol|Legendre symbol]]. For \(x\ge1\) the **centered quadratic prime sum** is
\[
 R_{d,q}(x)=\sum_{n\le x}\lambda(n)(1/n-1/x)-\frac{\log x}{\varphi(q)}-c_{d,q},
\]
where \(\varphi\) is [[analytic-number-theory/euler-totient|Euler’s totient]] and \(c_{d,q}\) is the unique constant making the remainder tend to zero.

## The constant as a logarithmic derivative

Write \(F_\psi\) for the [[analytic-number-theory/entire-dirichlet-l-function|pole-removed \(L\)-function]], \(D_\psi=F'_\psi/F_\psi\), and \(\eta_d(n)=(n/d)\). With the [[analytic-number-theory/quadratic-dirichlet-twist|quadratic twist]] \(\psi\eta_d\), the normalization is
\[
 c_{d,q}=\operatorname{Re}\frac{\sum_{\psi\bmod q}(D_{\psi\eta_d}(1)-D_\psi(1))-1}{\varphi(q)}.
\]
For \(n=p^k\) away from \(d\), the weight \(1-(n/d)\) is two precisely when \(p\) is a nonsquare modulo \(d\) and \(k\) is odd.

## References

- [New/Reduction/Zeros/PrimeError.lean, primeRemainder](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean#L65)
- [New/Reduction/Zeros/PrimeNumberTheorem.lean, tendsto_primeRemainder](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeNumberTheorem.lean#L233)
