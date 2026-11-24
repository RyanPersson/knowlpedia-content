+++
id = "arithmetic-geometry/chowla-selberg-period"
title = "Chowla–Selberg period"
kind = "definition"
summary = "A period of a CM elliptic curve whose value, up to algebraic normalization, is expressed by gamma values at rational arguments."
aliases = ["Chowla-Selberg period", "CM period"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/complex-multiplication", "real-analysis/gamma-function"]
+++

Take an [[algebraic-geometry-foundations/elliptic-curve|elliptic curve]] with [[arithmetic-geometry/complex-multiplication|complex multiplication]] and a nonzero invariant differential, both defined over the algebraic numbers in \(\mathbb C\). Integrating that differential around a closed cycle gives a **period**. The **Chowla–Selberg formula** expresses a basic period for an imaginary quadratic discriminant, up to algebraic factors and explicit powers of \(\pi\), by a product of [[real-analysis/gamma-function|gamma values]] at rational arguments.

## Why a logarithmic derivative appears

The gamma product has exponents involving the quadratic character of the discriminant. After taking logarithms, special-value formulas and the functional equation relate that character-weighted expression to the [[analytic-number-theory/l-logarithmic-derivative-at-one|logarithmic derivative at one]], with elementary normalization terms. For a fixed cycle \(\gamma\), replacing the differential \(\omega\) by \(a\omega\) multiplies \(\int_\gamma\omega\) by \(a\). Thus an algebraic change of differential leaves the period defined up to a nonzero algebraic factor.

## References

- A. Selberg and S. Chowla, [On Epstein’s zeta-function, pp. 86–110](https://doi.org/10.1515/crll.1967.227.86).
