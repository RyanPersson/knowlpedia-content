+++
id = "arithmetic-geometry/iterated-theta-lifts"
title = "The theta-lift chain in Alpöge’s announcement"
kind = "construction"
summary = "Successive lifts between unitary groups accumulate a gain analogous to multiplicity, with chain length near the square root of the prime-sum scale."
aliases = ["iterated theta lifts", "square-root-length chain"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/theta-lift", "analytic-number-theory/square-root-bound", "arithmetic-geometry/stepanov-method"]
+++

The **theta-lift chain** in Alpöge’s announcement successively applies [[arithmetic-geometry/theta-lift|global theta lifts]] along unitary groups \(U(V_0),\ldots,U(V_m)\). The proposal uses the accumulated gain from \(m\) steps in the role played by [[arithmetic-geometry/order-of-vanishing|vanishing multiplicity]] in Stepanov’s method. For a prime-sum cutoff \(x\), the chosen integer \(m\) has scale \(\sqrt{x}\).

## Why that length?

In the comparison, the chain contributes competing error terms of sizes \(x/m\) and \(m\), up to mild power losses. If \(x=10^4\), then \(m=100\) makes both terms \(100\). Making the chain ten times longer reduces the first term to \(10\) and increases the second to \(1000\). This balance explains one appearance of the [[analytic-number-theory/square-root-bound|square-root exponent]]. The argument also needs estimates for the remaining twisted prime sums.

## References

- Levent Alpöge, [announcement, p. 1 and p. 4, items 8–10](https://alpo.ge/remark.pdf).
- Manvir Jaswal, [Remark 3.6, the two square-root estimates](https://manvirjaswal.github.io/papers/rh-dirichlet-after-alpoge/jaswal-rh-dirichlet-after-alpoge.pdf).
