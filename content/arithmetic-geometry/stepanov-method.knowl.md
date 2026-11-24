+++
id = "arithmetic-geometry/stepanov-method"
title = "Stepanov’s method for curves over finite fields"
kind = "construction"
summary = "Bounding rational points by constructing an auxiliary function with many prescribed multiple zeros and limited pole degree."
aliases = ["Stepanov's proof", "Stepanov method"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/order-of-vanishing", "arithmetic-geometry/degree-of-a-divisor", "algebra-fields-galois/finite-field"]
+++

**Stepanov’s method** bounds rational points on a curve over a [[algebra-fields-galois/finite-field|finite field]] by constructing a nonzero auxiliary function. Suppose it vanishes to [[arithmetic-geometry/order-of-vanishing|order]] at least \(m\) at \(N\) distinct rational points and its poles have total [[arithmetic-geometry/degree-of-a-divisor|degree]] at most \(D\). Then \(mN\le D\). The work is to produce such a function with \(D/m\) small and to account for any exceptional points.

## The finite-field problem

For a [[algebraic-geometry-foundations/smooth-projective-curve|smooth projective]] geometrically connected curve of genus \(g\) over \(\mathbb F_q\), the Hasse–Weil bound is \(\bigl|\#C(\mathbb F_q)-(q+1)\bigr|\le2g\sqrt q\). Stepanov’s construction and its refinements give a route to this estimate.

## References

- Enrico Bombieri, [Counting points on curves over finite fields, §§1–2](https://www.numdam.org/item/SB_1972-1973__15__234_0.pdf).
