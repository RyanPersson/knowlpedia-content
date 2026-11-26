+++
id = "analytic-number-theory/legendre-factorial-valuation"
title = "Legendre’s factorial valuation formula"
kind = "theorem"
summary = "The exponent of a prime in a factorial counts its successive multiples."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/prime-power", "shared-foundations/p-adic-valuation"]
+++

For a prime \(p\) and \(n\ge0\), the [[shared-foundations/p-adic-valuation|\(p\)-adic valuation]] of \(n!\) is
\[
 v_p(n!)=\sum_{j\ge1}\left\lfloor n/p^j\right\rfloor .
\]
The sum stops once the [[analytic-number-theory/prime-power|prime power]] \(p^j\) exceeds \(n\).

## Proof

Every multiple of \(p\) contributes one factor. Each multiple of \(p^2\) contributes one additional factor, and likewise for every higher power. Counting each layer gives the formula.
