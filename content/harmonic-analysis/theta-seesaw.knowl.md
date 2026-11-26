+++
id = "harmonic-analysis/theta-seesaw"
title = "Seesaw identity for theta lifts"
kind = "definition"
summary = "An adjunction of period pairings induced by two nested reductive dual pairs in the same Weil representation."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/theta-lift", "harmonic-analysis/automorphic-period"]
+++

A **theta seesaw** consists of [[harmonic-analysis/reductive-dual-pair|dual pairs]] \((G,H)\) and \((G',H')\) for the same [[harmonic-analysis/weil-representation|Weil representation]] with \(G\subset G'\) and \(H'\subset H\). For compatible forms \(f\) on \(G\), \(h\) on \(H'\), and kernel data, the **seesaw identity** identifies the [[harmonic-analysis/automorphic-period|pairing]] of the [[arithmetic-geometry/theta-lift|lift]] of \(f\) restricted to \(H'\) with the pairing of \(f\) against the lift of \(h\) restricted to \(G\), with conjugations set by the pairing convention.

## Proof under absolute convergence

Both sides integrate the same theta kernel against the two forms over the product of the two automorphic quotients. Reversing the order of integration gives the other side. A regularized identity requires its own convergence or regularization hypotheses.

## References

- [New/UpperBound/Seesaw/SeesawIdentity.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Seesaw/SeesawIdentity.lean)
