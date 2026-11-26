+++
id = "grh-lean/half-plane"
title = "Nonvanishing to the right of the critical line"
kind = "theorem"
summary = "The central implication from an upper bound for prime sums to the half-plane form of Dirichlet GRH."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-l-function", "grh-lean/real-cutoffs", "grh-lean/zero-criterion"]
+++

For every \(q\ge1\) and every [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\bmod q\), the [[analytic-number-theory/dirichlet-l-function|value \(L(\rho,\chi)\)]] is nonzero when \(\Re\rho>1/2\), with the [[analytic-number-theory/principal-dirichlet-character|principal character]] at \(\rho=1\) excepted.

## Proof

For \(\rho=1\) use the classical nonvanishing of the nonprincipal values \(L(1,\chi)\). Otherwise take \(1/2<\beta<\Re\rho\). Enlarge the modulus to \(q_0=18480q\). The class \(d_0=q_0/2-1\) is coprime to \(q_0\) and is \(7\) modulo \(8\).

For each prime \(d\) in this class the [[grh-lean/real-cutoffs|arithmetic estimate for every large real cutoff]] gives \(R_{d,q_0}(x)\le x^{\beta-1}\), by taking \(\epsilon=\beta-1/2\). The [[grh-lean/zero-criterion|one-sided zero criterion]] rules out a zero at \(\rho\) for every character modulo \(q_0\). Apply it to the character induced by \(\chi\). Changing the level multiplies \(L(\rho,\chi)\) by finitely many [[langlands/euler-product-and-local-factor|Euler factors]], so nonvanishing of the product implies nonvanishing of \(L(\rho,\chi)\).

## References

- [New/Reduction/OneSidedBound.lean, grh](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L239)
- [Main.lean, LFunction_ne_zero_of_half_lt_re](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L13)
