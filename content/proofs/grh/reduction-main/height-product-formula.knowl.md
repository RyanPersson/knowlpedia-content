+++
id = "proofs/grh/reduction-main/height-product-formula"
title = "Product formula for heights: the constant family 1 has nonnegative height"
kind = "theorem"
summary = "If the constant family 1 has height at most c then c is nonnegative; hence a nonzero number of height at most c with conjugates bounded by exp(c') has -c at most c'."
aliases = ["heights are nonnegative", "nonneg_of_one"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.HeightLe.nonneg_of_one", "New.HeightLe.neg_le_of_norm_map_le", "New.HeightLe.norm_algebraMap_norm_gen_le"]
lean_files = ["src/New/Reduction/Lattices/Heights.lean"]
proof_status = "full"
+++

**Theorem.** We use the relation [[proofs/grh/reduction-main/height-bound|\(\operatorname{ht}(y)\le c\)]] for families indexed by the [[proofs/grh/reduction-main/prime-padic-iso|finite places of \(\mathbb C\)]].

1. If the constant family \(1\) has height at most \(c\), then \(c\ge0\).
2. Let \(z\ne0\) be a complex number. If the constant family \(z\) has height at most \(c\), and \(\lvert\sigma(z)\rvert\le e^{c'}\) for every field automorphism \(\sigma\) of \(\mathbb C\), then \(-c\le c'\).

## Proof

**A norm estimate.** Let \(H\in\mathbb C\) be algebraic over \(\mathbb Q\), of degree \(n=[\mathbb Q(H):\mathbb Q]\), and let \(F\) be an algebraically closed normed field of characteristic \(0\) with the cardinality of \(\mathbb C\). Suppose \(\lVert\iota(H)\rVert\le e^{b}\) for every field isomorphism \(\iota:\mathbb C\cong F\). Then the [[algebra-fields-galois/norm-field|norm]] \(q=\mathrm N_{\mathbb Q(H)/\mathbb Q}(H)\in\mathbb Q\) satisfies \(\lVert q\rVert_F\le e^{nb}\). Indeed \(q=\prod_{\tau}\tau(H)\), the product over the \(n\) field embeddings \(\tau:\mathbb Q(H)\to F\). Each \(\tau\) extends to an isomorphism \(\mathbb C\cong F\) (two algebraically closed fields of characteristic \(0\) and equal uncountable cardinality have equal transcendence degree over the algebraic number field \(\mathbb Q(H)\), embedded by the inclusion and by \(\tau\) respectively; see [[?c:isomorphism of algebraically closed fields of equal characteristic and uncountable cardinality|Steinitz's theorem]]). So each factor has norm at most \(e^b\).

**(1)** Let \((H,\alpha,(h_\ell))\) witness \(\operatorname{ht}(1)\le c\): \(H\ne0\), \(\lvert\sigma H\rvert\le e^\alpha\) for all \(\sigma\in\operatorname{Aut}(\mathbb C)\), \(\lvert H\rvert_\iota\le\ell^{h_\ell}=\exp(h_\ell\log\ell)\) for all \(\iota\mid\ell\), and \(\alpha+\sum_{\ell\in T}h_\ell\log\ell\le c\).

*\(H\) is algebraic.* The numbers \(\lvert\iota(H)\rvert_2\), \(\iota:\mathbb C\cong\overline{\mathbb Q}_2\), are bounded by \(2^{h_2}\). A complex number whose images under all isomorphisms \(\mathbb C\cong\overline{\mathbb Q}_\ell\) have bounded \(\ell\)-adic absolute value is algebraic over \(\mathbb Q\) ([[?lean:New.isAlgebraic_of_norm_complexToCp_le|bounded conjugates at a prime are algebraic]]).

Let \(n=[\mathbb Q(H):\mathbb Q]\ge1\) and \(q=\mathrm N_{\mathbb Q(H)/\mathbb Q}(H)\), a nonzero rational number. The norm estimate with \(F=\mathbb C\) (isomorphisms \(\mathbb C\cong\mathbb C\) are the automorphisms) gives \(\log\lvert q\rvert\le n\alpha\). With \(F=\overline{\mathbb Q}_\ell\), whose norm restricts to the \(\ell\)-adic absolute value on \(\mathbb Q\), it gives \(\log\lvert q\rvert_\ell\le n\,h_\ell\log\ell\) for every prime \(\ell\). Choose \(N\) larger than the numerator and the denominator of \(q\). By the [[proofs/grh/reduction-main/log-product-formula|product formula]],
\[
0=\log\lvert q\rvert+\sum_{\ell<N\ \text{prime}}\log\lvert q\rvert_\ell\ \le\ n\Bigl(\alpha+\sum_{\ell<N\ \text{prime}}h_\ell\log\ell\Bigr)\ \le\ nc ,
\]
and \(n>0\) gives \(c\ge0\).

**(2)** By rule (5) of [[proofs/grh/reduction-main/height-calculus|the calculus of heights]] the constant family \(z^{-1}\) has height at most \(c'\); by rule (6) the product of the constant families \(z^{-1}\) and \(z\), which is the constant family \(1\), has height at most \(c'+c\). By (1), \(c'+c\ge0\).

## References

1. Lean: `New.HeightLe.norm_algebraMap_norm_gen_le`, `New.HeightLe.nonneg_of_one`, `New.HeightLe.neg_le_of_norm_map_le` in `src/New/Reduction/Lattices/Heights.lean`. The extension of embeddings to isomorphisms is `exists_ringEquiv_extend`, and algebraicity is `New.isAlgebraic_of_norm_complexToCp_le`, both in `src/Lib/General/NumberTheory/PadicLimitsValuation.lean` (or its imports).
