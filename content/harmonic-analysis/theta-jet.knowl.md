+++
id = "harmonic-analysis/theta-jet"
title = "Differential jet of a theta function"
kind = "definition"
summary = "Application of a homogeneous constant-coefficient differential operator to a theta function at a point."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/multi-index-notation", "real-analysis/partial-derivative"]
+++

Let \(F(z)\) be a holomorphic theta function in local coordinates at \(0\). For a homogeneous polynomial \(P(X)=\sum_{|\alpha|=a}c_\alpha X^\alpha\), its **theta jet paired with \(P\)** is \(P(\partial)F(0)=\sum_{|\alpha|=a}c_\alpha\partial^\alpha F(0)\). The [[real-analysis/multi-index-notation|multi-index]] \(\alpha\) specifies the orders of the [[real-analysis/partial-derivative|partial derivatives]].

## Factorials in a jet

If \(P(X)=X^\alpha\), the jet is \(\alpha!\) times the coefficient of \(z^\alpha\). A bound on the coefficient and a divisibility assertion about the derivative can therefore differ by the [[algebra-fields-galois/valuation-on-a-field|valuation]] of a factorial.

## References

- [New/UpperBound/Kernels/JetConjugatesAndBounds.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Kernels/JetConjugatesAndBounds.lean)
