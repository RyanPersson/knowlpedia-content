+++
id = "arithmetic-geometry"
title = "Arithmetic geometry"
kind = "section"
summary = "Curves over finite fields, abelian varieties, complex multiplication and arithmetic invariants of lattices."
aliases = []
domains = ["arithmetic-geometry"]
section_mode = "continuous"
prerequisites = []
+++

Arithmetic geometry studies geometric objects over fields such as the rational numbers and finite fields, and over rings such as the integers. A curve can have many complex points yet only finitely many rational points. Its arithmetic depends on which field the coordinates must belong to.

## Curves and rational points

- [[algebraic-geometry-foundations/algebraic-curve|Algebraic curves]] and [[algebra-fields-galois/finite-field|finite fields]]
- [[arithmetic-geometry/order-of-vanishing|Order of vanishing]] and [[arithmetic-geometry/degree-of-a-divisor|degree of a divisor]]
- [[arithmetic-geometry/stepanov-method|Stepanov’s method]] and [[arithmetic-geometry/diophantine-inequality|Diophantine inequalities]]

## Abelian varieties and complex multiplication

- [[arithmetic-geometry/abelian-variety|Abelian varieties]], [[algebraic-geometry-foundations/elliptic-curve|elliptic curves]], [[arithmetic-geometry/power-of-an-elliptic-curve|their powers]] and [[arithmetic-geometry/isogeny|isogenies]]
- [[arithmetic-geometry/complex-multiplication|Complex multiplication]], [[algebra-fields-galois/imaginary-quadratic-field|imaginary quadratic fields]], [[arithmetic-geometry/cm-field|CM fields]] and [[arithmetic-geometry/abelian-cm-field|abelian CM fields]]
- [[arithmetic-geometry/shimura-datum|Shimura data]], [[arithmetic-geometry/shimura-variety|Shimura varieties]] and [[arithmetic-geometry/unitary-shimura-variety|unitary Shimura varieties]]
- [[arithmetic-geometry/cm-point|CM points]], [[arithmetic-geometry/integral-automorphic-form|integral automorphic forms]] and [[arithmetic-geometry/evaluation-at-a-cm-point|their evaluations]]

## Divisibility, size and slopes

- [[arithmetic-geometry/inert-prime|Inert primes]], [[shared-foundations/p-adic-valuation|\(p\)-adic valuation]] and [[arithmetic-geometry/inert-prime-divisibility|forced logarithmic divisibility]]
- [[arithmetic-geometry/archimedean-size|Archimedean size]], [[asymptotics/stirlings-approximation|Stirling’s approximation]] and the [[arithmetic-geometry/chowla-selberg-period|Chowla–Selberg period]]
- [[arithmetic-geometry/arakelov-degree|Arakelov degree]], [[arithmetic-geometry/arakelov-slope|Arakelov slopes]] and the [[arithmetic-geometry/slope-inequality|slope inequality]]

## Theta lifts and cohomology

- [[arithmetic-geometry/theta-lift|Global theta lifts]] and [[arithmetic-geometry/iterated-theta-lifts|iterated global theta lifts]]
- [[arithmetic-geometry/integral-lattice-comparison|Comparing integral lattices]], [[arithmetic-geometry/galois-cohomology|Galois cohomology]] and [[arithmetic-geometry/galois-localization-kernel|localization kernels]]
- [[algebra-fields-galois/ideal-class-group|Ideal class groups]] and [[arithmetic-geometry/vandiver-conjecture|Vandiver’s conjecture]]

For prime sums, characters and zeros of \(L\)-functions, see the [analytic number theory index](/analytic-number-theory/).

The [[grh-lean/main-inequality|covolume comparison in the Dirichlet GRH proof]] has three inputs. Open [[grh-lean/short-forms|short forms]], [[grh-lean/enough-forms|enough forms]] or [[grh-lean/long-forms|the lower bound for integral forms]] for the corresponding argument.
