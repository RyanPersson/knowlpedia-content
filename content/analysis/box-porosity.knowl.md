+++
id = "analysis/box-porosity"
title = "Box porosity"
kind = "definition"
summary = "A discrete multiscale porosity condition expressed by an empty child in every occupied cube."
aliases = ["box porous set", "L-adic box porosity"]
domains = ["analysis", "geometric-measure-theory", "harmonic-analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Fix an integer \(L\ge3\). Partition \([-1,1]^d\) at depth \(n\) into congruent
cubes of side length proportional to \(L^{-n}\). A set \(X\subseteq[-1,1]^d\)
is **box porous at scale \(L\) with depth \(n\)** if every depth-\(n\) cube
\(Q\) meeting \(X\) contains a depth-(n+1) child cube \(Q'\subset Q\) with
\(Q'\cap X=\varnothing\).

## Iterated form

If the condition holds at depths \(0,\ldots,N-1\), then at least one of the
\(L^d\) children is discarded at every occupied node. Consequently
\[
|X|\le 2^d(1-L^{-d})^N,
\]
where \(|X|\) denotes [[measure-theory/lebesgue-measure|Lebesgue measure]].

## Comparison with ball porosity

A set that is \(\nu\)-[[analysis/porosity-on-balls|porous on balls]] down to
scale \(h\) is box porous at all depths with \(L^{-n}\gtrsim h\), for a choice
\(L\asymp_d\nu^{-1}\). Box porosity is useful because the preceding counting
estimate turns geometric holes into a power-law volume bound.

## References

1. Rui Han and Wilhelm Schlag, “A higher-dimensional Bourgain–Dyatlov fractal uncertainty principle,” *Analysis & PDE* 13 (2020), 813–863. [DOI record](https://doi.org/10.2140/apde.2020.13.813).
2. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: Appendix A.1.
