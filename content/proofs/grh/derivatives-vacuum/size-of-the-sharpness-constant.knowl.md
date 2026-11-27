+++
id = "proofs/grh/derivatives-vacuum/size-of-the-sharpness-constant"
title = "Conjugates of the constant in the sharpness bound"
kind = "lemma"
summary = "For degrees at most the weights plus x^42, all conjugates of M^(12f) times the product of the squared loss products times a value of the integral vacuum are at most exp(f m b / k)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.norm_map_mul_intVacuum_le"]
lean_files = ["src/New/Derivatives/Sharpness/BoundAttained.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(D\) be admissible data, \(l\colon\Phi\to\mathbb{N}\) with \(l_\tau\le\kappa(\tau)+x^{42}\) for all \(\tau\), \(y\) a finite adelic vector of \(V_{12}\) and \(\sigma\) a field automorphism of \(\mathbb{C}\). Then
\[ \Bigl\lvert\sigma\Bigl(M^{12f}\prod_{\tau}B(l_\tau)^2\cdot\theta^\circ(y_f)\Bigr)\Bigr\rvert\le\exp\Bigl(\frac{f\,m}{k}\,b\Bigr), \]
with \(B\) the [[proofs/grh/derivatives-vacuum/loss-product|loss product]] and \(m\) the number of lifts.

## Proof

The integer factor is fixed by \(\sigma\). By [[proofs/grh/derivatives-vacuum/integral-vacuum-values|the values of the integral vacuum]], \(\lvert\sigma\theta^\circ(y_f)\rvert\le\exp(12\,C_{\mathrm{vac}}q_1^2)\), and \(C_{\mathrm{vac}}\) is at most the [[?lean:New.Parameters.constantBound|constant bound]] of the parameters. A product of \(n^\sharp\) consecutive integers up to at most \(l_\tau+n^\sharp\le2b+n^\sharp\) is at most \((2b+n^\sharp)^{n^\sharp}\). Multiplying these bounds (no logarithm of the value of the vacuum is taken, which may be \(0\)), the left side is at most \(\exp(L)\) with
\[ L=12f\log M+2f\,n^\sharp\log(2b+n^\sharp)+12\,C\,q_1^2 . \]
That \(L\le fmb/k\) is a scale inequality of the data, verified in Lean by the magnitude calculus ([[?lean:New.Data.le_of_hasLogBound|comparison of logarithmic sizes]]) and asserted here (heuristically: \(n^\sharp\approx6b/k\), \(\log(2b+n^\sharp)\approx\log b\), and \(m\approx\sqrt x\) is much larger than \(\log b\)).

## References

1. Lean: `New.Data.norm_map_mul_intVacuum_le` in `src/New/Derivatives/Sharpness/BoundAttained.lean`.
