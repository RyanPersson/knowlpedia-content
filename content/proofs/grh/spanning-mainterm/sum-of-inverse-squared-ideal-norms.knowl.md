+++
id = "proofs/grh/spanning-mainterm/sum-of-inverse-squared-ideal-norms"
title = "Bound for the sum of inverse squares of ideal norms"
kind = "lemma"
summary = "Any finite sum of N(b)^(-2) over ideals of the ring of integers of a number field E is at most exp(2[E:Q])."
aliases = ["sum_absNorm_inv_sq_le"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.sum_absNorm_inv_sq_le"]
lean_files = ["src/New/Spanning/MainTerm/Frequencies.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a number field and \(s\) a finite set of ideals of \(\mathcal O_E\). Then

\[
  \sum_{\mathfrak b\in s}(N\mathfrak b)^{-2}\;\le\;\exp\bigl(2[E:\mathbb Q]\bigr),
\]

where \(N\mathfrak b\) is the [[algebra-fields-galois/ideal-norm|absolute norm]] and the zero
ideal (of norm \(0\)) contributes \(0\).

## Proof

The series \(\sum_{\mathfrak b}(N\mathfrak b)^{-2}\) over all ideals has nonnegative terms and
converges to \(\zeta_E(2)\), the value at \(2\) of the
[[algebra-fields-galois/dedekind-zeta-function|Dedekind zeta function]], which is the Euler
product \(\prod_{\mathfrak p}(1-N\mathfrak p^{-2})^{-1}\) with all coefficients equal to \(1\)
([[?lean:New.hasSum_eulerProd|Dirichlet series of an Euler product]]). A finite partial sum of
a series of nonnegative terms is at most its sum, so the left-hand side is at most
\(\zeta_E(2)\). By the
[[?lean:New.eulerProd_ne_zero_and_abs_log_norm_le|bound for Euler products with coefficients of modulus at most one]]
at \(s=\sigma=2\), \(\lvert\log\zeta_E(2)\rvert\le2[E:\mathbb Q]\cdot2^{2-2}=2[E:\mathbb Q]\).
Hence \(\zeta_E(2)\le\exp(2[E:\mathbb Q])\). \(\blacksquare\)

## References

1. Lean: `New.sum_absNorm_inv_sq_le` in `src/New/Spanning/MainTerm/Frequencies.lean`.
