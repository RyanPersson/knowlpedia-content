+++
id = "harmonic-analysis/automorphic-period"
title = "Automorphic period integral"
kind = "definition"
summary = "Integration of an automorphic form over a subgroup quotient, optionally against a character."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["langlands/automorphic-form", "harmonic-analysis/haar-measure", "algebra-fields-galois/adeles-restricted-product"]
+++

Let \(H\subseteq G\) be algebraic groups over a [[algebra-fields-galois/number-field|number field]] \(F\). For an [[langlands/automorphic-form|automorphic form]] \(\varphi\) on \(G(\mathbb A_F)\) and a unitary character \(\nu\) of \(H(\mathbb A_F)\) trivial on \(H(F)\), the **period** along \(H\) is \(\int_{H(F)\backslash H(\mathbb A_F)}\varphi(h)\overline{\nu(h)}\,dh\) when convergent. Here \(\mathbb A_F\) denotes the [[algebra-fields-galois/adeles-restricted-product|adeles]] and \(dh\) is the chosen invariant measure induced by [[harmonic-analysis/haar-measure|Haar measure]].

## Fixed vectors and symmetry

For the trivial character the period averages the restriction of the form. Translation by an element of the subgroup preserves this functional when the quotient measure is right invariant.

## References

- [Lib/Weil/Periods/BesselIntegral.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Periods/BesselIntegral.lean)
