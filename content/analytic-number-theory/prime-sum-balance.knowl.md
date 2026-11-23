+++
id = "analytic-number-theory/prime-sum-balance"
title = "Prime-sum balance on an abelian CM field"
kind = "identity"
summary = "The character expansion of inert-prime weights relates the divisibility and size terms to centered prime sums."
aliases = ["divisibility minus size", "character balance identity"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/finite-fourier-inversion", "analytic-number-theory/centered-prime-sum", "arithmetic-geometry/inert-prime"]
+++

In the post, **divisibility minus size** denotes a difference of two logarithmic quantities. The first adds prescribed divisibility at finite primes. The second collects the archimedean main terms. For the auxiliary fields and weights in the argument, expanding the prime conditions in [[analytic-number-theory/galois-character|Galois characters]] expresses this difference as a weighted combination of [[analytic-number-theory/centered-prime-sum|centered prime sums]].

## The simplest instance of the expansion

For unramified primes in a quadratic field let \(\chi(p)=1\) at split primes and \(-1\) at inert primes. For any finite choice of weights \(b_p\),
\[
2\sum_{p\ {\rm inert}} b_p=\sum_p b_p-\sum_p\chi(p)b_p ,
\]
where both sums on the right run over the same unramified primes. This illustrates the [[analytic-number-theory/finite-fourier-inversion|Fourier step]]. The full identity also accounts for prime powers, inertia at ramified primes, rescaled cutoffs and the centering terms. The [[arithmetic-geometry/slope-inequality|slope inequality]] provides the separate estimate on its size.

## References

- Manvir Jaswal, [§3.6, Proposition 3.3 and its proof](https://manvirjaswal.github.io/papers/rh-dirichlet-after-alpoge/jaswal-rh-dirichlet-after-alpoge.pdf).
