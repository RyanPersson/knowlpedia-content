+++
id = "arithmetic-geometry/order-of-vanishing"
title = "Order of vanishing on a smooth curve"
kind = "definition"
summary = "The exponent of a local parameter in a nonzero rational function at a smooth point."
aliases = ["vanishing to order", "zero multiplicity on a curve"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/algebraic-curve", "algebra-fields-galois/valuation-on-a-field"]
+++

At a smooth closed point \(P\) of an integral [[algebraic-geometry-foundations/algebraic-curve|algebraic curve]], choose a local parameter \(t\), a generator of the maximal ideal of the local ring. A nonzero rational function has the form \(f=t^m u\) with \(u\) a unit in that ring. The integer \(m=\operatorname{ord}_P(f)\) is the [[algebra-fields-galois/valuation-on-a-field|valuation]] at \(P\). Positive \(m\) is the **order of vanishing**.

## Counting a repeated zero

On the affine line, \((t-a)^3(t-b)\) has a triple zero at \(a\) when \(a\ne b\). Knowing that a function vanishes to order at least \(m\) at each of \(N\) rational points accounts for at least \(mN\) in its zero divisor. [[arithmetic-geometry/stepanov-method|Stepanov’s method]] uses this multiplicity count.
