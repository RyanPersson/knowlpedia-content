+++
id = "proofs/grh/spanning-core/near-isometry-from-small-defect"
title = "A small defect gives a near isometry"
kind = "lemma"
summary = "If A*A - 1 has squared Hilbert–Schmidt norm at most eps^2 dim S then A is a near isometry with error eps."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.isNearIsometry_of_hilbertSchmidtNorm_le"]
lean_files = ["src/New/Spanning/SecondMoment/FewTranslates.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S,T\) be finite-dimensional complex inner product spaces, \(A\colon S\to T\) linear and \(\varepsilon\ge0\). If
\[
\lVert A^*A-1\rVert_{\mathrm{HS}}^2\le\varepsilon^2\dim S
\]
in the [[proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map|Hilbert–Schmidt norm]], then \(A\) is a [[proofs/grh/spanning-core/near-isometry-in-mean-square|near isometry]] with error \(\varepsilon\).

## Proof

Let \(U\subseteq S\) be a subspace and \(p=\mathrm{pr}_U\). By Properties 2 and 6 of the Hilbert–Schmidt norm, \(\lVert Ap\rVert^2_{\mathrm{HS}}=\lVert pA^*\rVert_{\mathrm{HS}}^2=\operatorname{Re}\langle p,A^*A\rangle_{\mathrm{HS}}\), and likewise \(\dim U=\lVert p\rVert_{\mathrm{HS}}^2=\operatorname{Re}\langle p,1\rangle_{\mathrm{HS}}\). Hence
\[
\lVert Ap\rVert_{\mathrm{HS}}^2-\dim U=\operatorname{Re}\langle p,A^*A-1\rangle_{\mathrm{HS}} .
\]
By the [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]], \(\lVert p\rVert_{\mathrm{HS}}^2=\dim U\le\dim S\) and the hypothesis,
\[
\bigl\lvert\langle p,A^*A-1\rangle_{\mathrm{HS}}\bigr\rvert\le\lVert p\rVert_{\mathrm{HS}}\lVert A^*A-1\rVert_{\mathrm{HS}}\le\sqrt{\dim S}\cdot\varepsilon\sqrt{\dim S}=\varepsilon\dim S .
\]
So \(\lVert Ap\rVert^2_{\mathrm{HS}}\ge\dim U-\varepsilon\dim S\). \(\blacksquare\)

## References

1. Lean: `New.isNearIsometry_of_hilbertSchmidtNorm_le` in `src/New/Spanning/SecondMoment/FewTranslates.lean`.
