+++
id = "grh-lean/twist-polynomials"
title = "Choosing one character for many local conditions"
kind = "theorem"
summary = "Polynomial evaluations at roots of unity give a common anticyclotomic twist."
domains = ["grh-lean"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/anticyclotomic-character", "arithmetic-geometry/selmer-group"]
+++

Under the finite-datum hypotheses of the twisting theorem, one [[arithmetic-geometry/anticyclotomic-character|anticyclotomic character]] satisfies the required [[arithmetic-geometry/selmer-group|Selmer-length]] and special-value bounds simultaneously for all powers from \(1\) to \(m\).

## Proof

Choose auxiliary places and assign a variable to each. A presentation minor gives a polynomial bounding a twisted Selmer length. Norm relations in group rings give polynomials for the special values. Restriction to a suitable line produces, for each polynomial, a point where its valuation is small. A simultaneous specialization lemma chooses roots of unity \(\zeta_v\) so that taking \(X_v=\zeta_v^j-1\) preserves the required bounds for all \(j\). The product character \(\prod_v\zeta_v^{\lambda_v}\), for the chosen local character maps \(\lambda_v\), has precisely these specializations.

## References

- [New/Congruences/Selmer/Line.lean, exists_twistPolynomials](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Line.lean#L646)
- [New/Congruences/Selmer/GeneralTheorem.lean, exists_anticyclotomic_twist](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean#L392)
