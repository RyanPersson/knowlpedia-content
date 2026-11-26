+++
id = "proofs/grh/spanning-core/near-isometry-after-projection"
title = "Near isometries and orthogonal projections"
kind = "lemma"
summary = "Composing a near isometry with an orthogonal projection that misses little of its norm gives a near isometry; the part missed by a product of projections."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsNearIsometry.proj_comp", "New.hilbertSchmidtNorm_one_sub_mul_comp_sq_le", "New.norm_sq_eq_add_of_isSymmetricProjection"]
lean_files = ["src/New/Spanning/SecondMoment/FewTranslates.lean"]
proof_status = "full"
+++

**Lemma.** Let \(S,T\) be finite-dimensional complex inner product spaces, \(A\colon S\to T\) linear, and let \(p\colon T\to T\) be an [[linear-algebra/orthogonal-projection|orthogonal projection]] (a linear map with \(p^2=p\) and \(\langle px,y\rangle=\langle x,py\rangle\)). Norms of maps are [[proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map|Hilbert–Schmidt norms]].

1. If \(A\) is a [[proofs/grh/spanning-core/near-isometry-in-mean-square|near isometry]] with error \(\varepsilon\) and \(\lVert(1-p)A\rVert_{\mathrm{HS}}^2\le\delta\dim S\), then \(pA\) is a near isometry with error \(\varepsilon+\delta\).
2. For every linear map \(q\colon T\to T\),
\[
\lVert(1-pq)A\rVert_{\mathrm{HS}}^2\le\lVert(1-p)A\rVert_{\mathrm{HS}}^2+\lVert(1-q)A\rVert_{\mathrm{HS}}^2 .
\]

## Proof

For every \(y\in T\) the vectors \(py\) and \((1-p)y\) are orthogonal, so \(\lVert y\rVert^2=\lVert py\rVert^2+\lVert(1-p)y\rVert^2\) (Pythagoras).

(1) Let \(U\subseteq S\). Applying Pythagoras to \(y=A\,\mathrm{pr}_Ub_i\) for an orthonormal basis \((b_i)\) of \(S\) and summing,
\[
\lVert A\,\mathrm{pr}_U\rVert_{\mathrm{HS}}^2=\lVert pA\,\mathrm{pr}_U\rVert_{\mathrm{HS}}^2+\lVert(1-p)A\,\mathrm{pr}_U\rVert_{\mathrm{HS}}^2 ,
\]
and the last term is at most \(\lVert(1-p)A\rVert_{\mathrm{HS}}^2\le\delta\dim S\) (Property 5 of the norm). With \(\dim U-\varepsilon\dim S\le\lVert A\,\mathrm{pr}_U\rVert^2_{\mathrm{HS}}\) this gives the claim.

(2) It suffices to prove the inequality for each vector \(y=Ab_i\) in place of \(A\). Since \(p^2=p\), \(p(1-pq)=p(1-q)\) and \((1-p)(1-pq)=1-p\). By Pythagoras, \(\lVert(1-pq)y\rVert^2=\lVert p(1-q)y\rVert^2+\lVert(1-p)y\rVert^2\), and \(\lVert p(1-q)y\rVert\le\lVert(1-q)y\rVert\). \(\blacksquare\)

## References

1. Lean: `New.IsNearIsometry.proj_comp`, `New.hilbertSchmidtNorm_one_sub_mul_comp_sq_le` in `src/New/Spanning/SecondMoment/FewTranslates.lean`.

## References

1. Lean: `New.IsNearIsometry.proj_comp`, `New.hilbertSchmidtNorm_one_sub_mul_comp_sq_le`, `New.norm_sq_eq_add_of_isSymmetricProjection` in `src/New/UpperBound/ElementaryDivisors/.lean`.
