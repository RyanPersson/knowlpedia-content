+++
id = "analytic-number-theory/zeta-zeros-from-half-plane-nonvanishing"
title = "From half-plane nonvanishing to the nontrivial zeta zeros"
kind = "theorem"
summary = "Reflection gives the zeta conclusion for all zeros other than the negative even integers."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/riemann-zeta-function", "analytic-number-theory/completed-dirichlet-l-function", "analytic-number-theory/dirichlet-functional-equation", "complex-analysis/complex-gamma-function", "analytic-number-theory/dirichlet-character", "analytic-number-theory/dirichlet-l-function"]
+++

Suppose the [[analytic-number-theory/riemann-zeta-function|Riemann zeta function]] is nonzero for \(\Re s>1/2\) away from its pole at \(1\). Every zero \(s\) other than \(-2,-4,-6,\ldots\) then satisfies \(\Re s=1/2\).

## Proof

Use the modulus-one [[analytic-number-theory/completed-dirichlet-l-function|completed function]] \(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\). Its [[analytic-number-theory/dirichlet-functional-equation|functional equation]] gives \(\Lambda(s)=\Lambda(1-s)\). The integral in that proof gives a simple pole with residue \(-1\) at \(s=0\). Since \(\Gamma(s/2)\) has residue \(2\) there by the [[complex-analysis/complex-gamma-function|gamma recurrence]], \(\zeta(0)=-1/2\).

For a zero as in the statement, \(s\) is therefore neither \(0\) nor \(1\) nor a negative even integer. The gamma factor at \(s\) is finite, so \(\Lambda(s)=0\) and hence \(\Lambda(1-s)=0\). Multiplication by the entire reciprocal gamma factor gives \(\zeta(1-s)=\pi^{(1-s)/2}\Lambda(1-s)/\Gamma((1-s)/2)=0\). Both \(s\) and \(1-s\) differ from \(1\). The nonvanishing hypothesis at these two points gives \(\Re s\le1/2\) and \(1-\Re s\le1/2\). Thus \(\Re s=1/2\).

## From a hypothesis for all characters

The premise holds if half-plane nonvanishing is assumed for every [[analytic-number-theory/dirichlet-character|Dirichlet character]], since the [[analytic-number-theory/dirichlet-l-function|\(L\)-function]] for modulus \(1\) is \(\zeta\).

## References

- [The zeta conclusion from the half-plane hypothesis](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L47)
