+++
id = "lie-groups/generation-sl2-subalgebras"
title = "Generation sl2 subalgebras"
kind = "construction"
summary = "The three regular sl2 subalgebras associated with the three root lines of the generation A2 root system."
aliases = ["generation sl2s", "three generation sl2 subalgebras", "sl2 beta k"]
domains = ["lie-groups", "mathematical-physics"]
section_mode = "progressive"
prerequisites = ["lie-groups/generation-plane", "lie-groups/root-sl2-subalgebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(A\subset P\) be the \(A_2\) roots in the [[lie-groups/generation-plane|generation plane]]. Write
\[
A=\{\pm\beta_1,\pm\beta_2,\pm\beta_3\},
\]
one opposite pair for each of the three root lines. The corresponding **generation \(\mathfrak{sl}_2\) subalgebras** are
\[
\mathfrak{sl}_2(\beta_k)
=(\mathfrak e_7)_{\beta_k}
\oplus\mathbb C h_{\beta_k}
\oplus(\mathfrak e_7)_{-\beta_k}
\subset\mathfrak{sl}_3^{\mathrm{gen}},
\qquad k=1,2,3.
\]
Each is the [[lie-groups/root-sl2-subalgebra|root \(\mathfrak{sl}_2\)-subalgebra]] associated with its root line and is regular. Replacing \(\beta_k\) by \(-\beta_k\) gives the same subalgebra.

## Relation to the defining weights

Choose the weights \(w_1,w_2,w_3\) of the defining generation \(\mathfrak{sl}_3\)-module and set
\[
\beta_k=w_i-w_j
\]
when \((i,j,k)\) is cyclic. Then \(w_k\perp\beta_k\), while the other two weights pair with \(\beta_k\) by \(\pm1\). Thus the \(k\)-th root line fixes the weight direction labeled \(k\) and mixes the other two.

## Centralizers in e7

For each \(k\), the roots orthogonal to \(\beta_k\) form the [[lie-groups/three-d6-subsystems-in-e7|corresponding \(D_6\) subsystem]]. Consequently \(\mathfrak{sl}_2(\beta_k)\) and a copy \(\mathfrak{so}_{12}(\beta_k)\) are [[lie-groups/mutual-centralizers-in-a-lie-algebra|mutual centralizers]] in \(\mathfrak e_7\).

## Dependence on choices

The unordered set of three root-line subalgebras is determined after choosing a [[lie-groups/cartan-subalgebra|Cartan subalgebra]] of \(\mathfrak{sl}_3^{\mathrm{gen}}\). Their labels \(1,2,3\) and the signs of the \(\beta_k\) are conventions. Without a Cartan choice, the generation \(\mathfrak{sl}_3\) is intrinsic but no distinguished triple of these \(\mathfrak{sl}_2\)'s is selected.

## References

1. John C. Baez, “Three Generations in E7,” 2026, §4. [arXiv:2608.06271](https://arxiv.org/abs/2608.06271).
