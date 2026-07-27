+++
id = "algebra-groups/product-of-normal-subgroups"
title = "Product of normal subgroups is normal"
kind = "knowl"
summary = "If N and M are normal subgroups of G, then NM is a normal subgroup and NM = MN."
aliases = ["product-of-normal-subgroups", "Product of normal subgroups is normal"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/product-of-normal-subgroups.md"
+++

**Proposition (Product of normal subgroups).**
Let \(G\) be a [[algebra-groups/group|group]] and let \(N,M\trianglelefteq G\) be [[algebra-groups/normal-subgroup|normal subgroups]]. Define
\[
NM=\{nm:n\in N,\ m\in M\}.
\]

Then \(NM=MN\), and this set is a normal subgroup of \(G\).

## Remarks

Normality gives \(nm=m(m^{-1}nm)\in MN\), so \(NM\subseteq MN\); symmetry gives equality. Conjugation by any \(g\in G\) preserves both \(N\) and \(M\), hence preserves \(NM\).
