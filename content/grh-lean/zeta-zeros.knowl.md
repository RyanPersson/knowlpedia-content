+++
id = "grh-lean/zeta-zeros"
title = "Nontrivial zeros of the Riemann zeta function"
kind = "theorem"
summary = "Pass to the character modulo one and use the symmetry of the completed zeta function."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/riemann-zeta-function", "grh-lean/half-plane"]
+++

Let \(\zeta(s)=0\), where \(\zeta\) is the [[analytic-number-theory/riemann-zeta-function|Riemann zeta function]]. If \(s\ne1\) and \(s\notin\{-2,-4,-6,\ldots\}\), then \(\Re s=1/2\).

## Proof

Since \(\zeta(0)=-1/2\), this zero is also different from zero. The excluded negative even integers and zero are exactly the possible poles of the real [[real-analysis/gamma-function|gamma factor]] \(\Gamma_{\mathbb R}(s)\). The completed [[analytic-number-theory/riemann-zeta-function|zeta function]] therefore vanishes at \(s\). Its symmetry gives a zero at \(1-s\), hence \(\zeta(1-s)=0\). Neither argument is the pole at \(1\).

Zeta is the [[analytic-number-theory/dirichlet-l-function|\(L\)-function]] of the unique character modulo one. By [[grh-lean/half-plane|half-plane nonvanishing]], \(\Re s\le1/2\) and \(1-\Re s\le1/2\), so equality holds.

## References

- [New/Main.lean, New.zeta_zeros_on_line](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L47)
- [Main.lean, riemannZeta_eq_zero_re](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L8)
