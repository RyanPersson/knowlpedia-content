+++
id = "proofs/grh/spanning-unfolding-b/common-link"
title = "Common link of two isometries"
kind = "definition"
summary = "The module of vectors of X0 that are the first component of a pair, orthogonal to z in both components, lying in the links of two isometries."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.commonLink", "New.Filling.zRowBlockDiagonal", "New.Filling.linkForm"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
+++

Let \(R\) be a commutative ring with involution, \(T\) a matrix on the middle indices \(\kappa\sqcup\{z\}\) and \(\gamma,\gamma'\) isometries of the split Gram matrix of \(\varrho\) hyperbolic planes and \(T\). The [[?lean:New.link|link]] of an isometry is a submodule of \(R^{\kappa\sqcup\{z\}}\oplus R^{\kappa\sqcup\{z\}}\). The **common link** of \(\gamma\) and \(\gamma'\) is the submodule of \(R^\kappa\) of the vectors \(x\) for which there is a pair \((w_1,w_2)\) such that

* \((w_1,w_2)\) lies in the link of \(\gamma\) and in the link of \(\gamma'\);
* \(\sum_iT_{z,i}(w_1)_i=0\) and \(\sum_iT_{z,i}(w_2)_i=0\) (both components are orthogonal to \(z\) for \(T\));
* \(x\) is the restriction of \(w_1\) to \(\kappa\).

For a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] \(S\), the **link form** is the block diagonal matrix \(\operatorname{diag}(T_E,-T_E)\) on two copies of the middle space, with \(T_E=\operatorname{diag}(1,\dots,1,-N)\).

## References

1. Lean: `New.commonLink`, `New.Filling.zRowBlockDiagonal`, `New.Filling.linkForm` in `src/New/Spanning/Unfolding/Terms.lean`.
