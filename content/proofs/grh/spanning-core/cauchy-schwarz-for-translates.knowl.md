+++
id = "proofs/grh/spanning-core/cauchy-schwarz-for-translates"
title = "Cauchy–Schwarz for the translates of a map"
kind = "lemma"
summary = "For a unitary action of a finite group, the squared norms of B* s B form a function of positive type, and the mean of the parts of the translates sB in a subspace W is bounded by the second moment."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.inner_hilbertSchmidtVector_translate", "New.sq_sum_hilbertSchmidtNorm_orthoProj_comp_le", "New.adjoint_rep_of_unitary"]
lean_files = ["src/New/Spanning/SecondMoment/FewTranslates.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S,T\) be finite-dimensional complex inner product spaces, \(\Gamma\) a [[algebra-groups/group|group]], and \(\rho\) a [[algebra-representation-theory/group-representation|representation]] of \(\Gamma\) on \(T\) that preserves the inner product: \(\langle\rho(s)x,\rho(s)y\rangle=\langle x,y\rangle\). Let \(B\colon S\to T\) be linear, and write \(sB=\rho(s)B\). Norms and inner products of maps are [[proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map|Hilbert–Schmidt]].

1. For \(s,t\in\Gamma\),
\[
\bigl\langle (sB)(sB)^*,\ (tB)(tB)^*\bigr\rangle_{\mathrm{HS}}=\lVert B^*\rho(s^{-1}t)B\rVert_{\mathrm{HS}}^2 .
\]
In particular, for finite \(\Gamma\), \(s\mapsto\lVert B^*\rho(s)B\rVert^2_{\mathrm{HS}}\) is a [[proofs/grh/spanning-core/function-of-positive-type|function of positive type]] on \(\Gamma\).
2. If \(\Gamma\) is finite, then for every subspace \(W\subseteq T\)
\[
\Bigl(\sum_{s\in\Gamma}\lVert\mathrm{pr}_W\,\rho(s)B\rVert_{\mathrm{HS}}^2\Bigr)^2\le\dim W\cdot\lvert\Gamma\rvert\cdot\sum_{s\in\Gamma}\lVert B^*\rho(s)B\rVert_{\mathrm{HS}}^2 .
\]

## Proof

(1) As \(\rho(s)\) preserves the inner product, \(\rho(s)^*=\rho(s^{-1})\). Put \(X=\rho(s)B\), \(Y=\rho(t)B\); then \(X^*Y=B^*\rho(s^{-1}t)B\). The operator \(XX^*\) is self-adjoint, so
\[
\langle XX^*,YY^*\rangle_{\mathrm{HS}}=\operatorname{tr}(XX^*YY^*)=\operatorname{tr}(Y^*XX^*Y)=\operatorname{tr}\bigl((X^*Y)^*(X^*Y)\bigr)=\lVert X^*Y\rVert_{\mathrm{HS}}^2 .
\]

(2) Let \(\Sigma=\sum_{s}(sB)(sB)^*\), an endomorphism of \(T\). By (1) and the sum rule for functions of positive type, \(\lVert\Sigma\rVert_{\mathrm{HS}}^2=\lvert\Gamma\rvert\sum_s\lVert B^*\rho(s)B\rVert_{\mathrm{HS}}^2\). By Property 6 of the Hilbert–Schmidt norm, \(\sum_s\lVert\mathrm{pr}_W\,sB\rVert^2_{\mathrm{HS}}=\operatorname{Re}\langle\mathrm{pr}_W,\Sigma\rangle_{\mathrm{HS}}\), which by [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz]] is at most \(\lVert\mathrm{pr}_W\rVert_{\mathrm{HS}}\lVert\Sigma\rVert_{\mathrm{HS}}\), and \(\lVert\mathrm{pr}_W\rVert^2_{\mathrm{HS}}=\dim W\). Square. \(\blacksquare\)

## References

1. Lean: `New.inner_hilbertSchmidtVector_translate`, `New.sq_sum_hilbertSchmidtNorm_orthoProj_comp_le` in `src/New/Spanning/SecondMoment/FewTranslates.lean`.
