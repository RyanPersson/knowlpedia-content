+++
id = "arithmetic-geometry/integral-lattice-comparison"
title = "Comparing integral lattices"
kind = "construction"
summary = "Measuring which rationally equivalent integral structures differ at finite primes."
aliases = ["integral comparison", "integral structures"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-modules/full-lattice", "linear-algebra/integer-lattice-index"]
+++

An **integral comparison** between two [[algebra-modules/full-lattice|lattices]] in the same rational vector space asks how an identification over the field acts on integral vectors. Given \(L\subseteq M\) of full rank over \(\mathbb Z\), the finite quotient \(M/L\) records the discrepancy. Its \(p\)-part measures how much of the discrepancy is visible at \(p\).

## A denominator at one prime

The submodule \(3\mathbb Z\) and the lattice \(\mathbb Z\) both span \(\mathbb Q\). Their [[linear-algebra/integer-lattice-index|index]] is three. They become the same lattice over \(\mathbb Z_p\) for \(p\ne3\), since three is a unit there. In the post, estimates for [[arithmetic-geometry/galois-cohomology|Galois cohomology groups]] control losses in comparing lattices that carry more structure.

## References

- Siniša Slijepčević, [§1, local defects of the lattices, and §9, bounds on localization kernels](https://hexagonmath.org/pdf/2611.00812).
