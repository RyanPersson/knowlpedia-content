+++
id = "arithmetic-geometry/vandiver-type-bound"
title = "A Vandiver-type bound in the Riemann argument"
kind = "statement"
summary = "A bound on sizes of certain arithmetic cohomology groups, modeled on the plus-part question for class groups."
aliases = ["Vandiver type", "Vandiver-type estimate", "Kummer–Vandiver conjecture"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/ideal-class-group", "arithmetic-geometry/galois-cohomology", "algebra-fields-galois/cyclotomic-extension"]
+++

**Vandiver’s conjecture** says that an odd prime \(\ell\) does not divide the class number of the maximal real subfield \(\mathbb Q(\zeta_\ell+\zeta_\ell^{-1})\) of the [[algebra-fields-galois/cyclotomic-extension|cyclotomic field]] \(\mathbb Q(\zeta_\ell)\). It predicts that the \(\ell\)-primary part of that real field’s [[algebra-fields-galois/ideal-class-group|ideal class group]] is trivial.

## What “Vandiver type” means here

The post refers to quantitative control of related arithmetic groups. The objects are kernels of maps from global [[arithmetic-geometry/galois-cohomology|Galois cohomology]] to local cohomology, with coefficients modified by powers of the cyclotomic character (Tate twists). Their lengths measure possible losses of integrality. The comparison needs a bound on their aggregate size over suitable [[analytic-number-theory/scale-window|windows]]. A bound allows nonzero groups, so this use of “Vandiver type” makes a weaker demand than universal vanishing.

## References

- J. Buhler and D. Harvey, [Irregular primes to 163 million, §1, the Kummer–Vandiver conjecture](https://arxiv.org/pdf/0912.2121).
- Levent Alpöge, [announcement, p. 4, item 17](https://alpo.ge/remark.pdf).
- Siniša Slijepčević, [§9, Theorem 9.1, the window bound](https://hexagonmath.org/pdf/2611.00812).
