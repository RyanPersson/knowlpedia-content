+++
id = "harmonic-analysis/hecke-operator"
title = "Double-coset Hecke operator"
kind = "definition"
summary = "The operator obtained by integrating translates over a compact double coset."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["algebra-representation-theory/group-representation"]
+++

Let \(K\) be a compact open subgroup of a locally compact group \(G\), normalize left [[harmonic-analysis/haar-measure|Haar measure]] by \(\operatorname{vol}(K)=1\), and let \(\pi\) be a smooth [[algebra-representation-theory/group-representation|representation]]. For \(g\in G\), the **Hecke operator** of \(KgK\) on \(K\)-fixed vectors is \(T_gv=\int_{KgK}\pi(h)v\,dh\).

## Finite sum

A compact double coset is a finite disjoint union of cosets \(h_iK\). On a \(K\)-fixed vector the integral is \(\sum_i\pi(h_i)v\).

## References

- [Lib/Adelic/Hecke/Basic.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Hecke/Basic.lean)
