+++
id = "analytic-number-theory/induced-dirichlet-character"
title = "Induced Dirichlet character"
kind = "definition"
summary = "Inflate a character along reduction on units and extend it by zero at the new modulus."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character","analytic-number-theory/dirichlet-conductor","analytic-number-theory/primitive-dirichlet-character","algebra-rings/chinese-remainder-theorem"]
+++

If \(f\mid q\), the [[analytic-number-theory/dirichlet-character|Dirichlet character]] modulo \(q\) **induced** by \(\psi\bmod f\) is the composite of reduction \((\mathbb Z/q\mathbb Z)^\times\to(\mathbb Z/f\mathbb Z)^\times\) and \(\psi\) on units, extended by zero to the other integers.

## Primitive representative

The [[analytic-number-theory/dirichlet-conductor|conductor]] is the least positive divisor \(f\) of \(q\) from which \(\chi\) is induced. This set of divisors contains \(q\). A character \(\psi\) inducing \(\chi\) at the least divisor is [[analytic-number-theory/primitive-dirichlet-character|primitive]], since induction from any proper divisor of \(f\) would also induce \(\chi\). Its values are uniquely specified on the units modulo \(f\). Indeed each such class lifts to a unit modulo \(q\), by imposing residue \(1\) at the primes dividing \(q\) but not \(f\) and applying the [[algebra-rings/chinese-remainder-theorem|Chinese remainder theorem]].

## References

- [Change of level and primitive representative](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/ZeroSymmetry.lean#L42)
