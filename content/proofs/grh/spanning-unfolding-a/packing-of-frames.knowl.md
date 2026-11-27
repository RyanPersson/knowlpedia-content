+++
id = "proofs/grh/spanning-unfolding-a/packing-of-frames"
title = "Packing of frames"
kind = "theorem"
summary = "Terms gamma over a fixed class whose translates of a point lie in a box have at most (b^(6 n^2) R^2)^(dim V) distinct images of the frame."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.encard_image_frameImage_le"]
lean_files = ["src/New/Spanning/Unfolding/Packing.lean"]
proof_status = "full"
+++

**Theorem (packing of frames).** Let \(E\) be a [[?c:CM field|CM field]] and \(S\) [[?lean:New.Filling|filling data]] over \(E\) satisfying the [[?lean:New.Filling.IsAdmissible|standing hypotheses]], with parameter \(b\), \(n=\varrho+1\). Let \(c\) be a class, \(y\in G_\infty\), \(R\ge1\), and \(A\) a set of rational [[?c:Isometry of a hermitian space|isometries]] such that every \(\gamma\in A\) is a [[?lean:New.Filling.termsOver|term]] over \((c,s,c')\) for some \(s,c'\), and such that for every \(\gamma\in A\) and every [[?c:Infinite place of a number field|infinite place]] \(v\) the point \(x=(\gamma^{-1}y)_v\) has [[?lean:New.besselLength|Bessel length]] at most \(b^{6n+2}R\) and frame vectors \(x^{-1}f_a\) of norm at most \(b^{37n}R\). Let \(\mathcal V\) be a real subspace of the space of families \((w_{v,a})\) of vectors of \(\mathbb C^{r}\) (indexed by the infinite places and the frame indices) which contains the difference of the families of frame vectors of \(\gamma^{-1}y\) and \(\gamma'^{-1}y\) for all \(\gamma,\gamma'\in A\). Then the number of distinct frame images \(\gamma f=(\gamma f_0,\dots,\gamma f_\varrho)\), \(\gamma\in A\), is at most
\[
\bigl(b^{6n^2}R^2\bigr)^{\dim_{\mathbb R}\mathcal V}.
\]

## Proof

We may assume \(A\ne\emptyset\); fix \(\gamma_0\in A\). Put \(\rho=b^{37n}R\), and let \(F(\gamma)\) be the family of the frame vectors of \(\gamma^{-1}y\), normed by the maximum over \(v\) and \(a\) of the Euclidean norms; so \(\lVert F(\gamma)\rVert\le\rho\) for \(\gamma\in A\). Choose a subset \(u\subseteq A\) on which \(\gamma\mapsto\gamma f\) is injective with the same image as on \(A\), and put \(\phi(p)=F(\gamma_0)-F(p)\in\mathcal V\), so \(\lVert\phi(p)\rVert\le2\rho\).

*Separation.* Let \(p\ne q\) in \(u\) and suppose \(\lVert\phi(p)-\phi(q)\rVert=\lVert F(q)-F(p)\rVert<(N\rho)^{-1}\). Terms are closed under inverses and products of composable blocks, so \(g=p^{-1}q\) is a term. The point \(z=p^{-1}y\) satisfies the size and box hypotheses of the theorem on [[proofs/grh/spanning-unfolding-a/rigidity-of-frames|rigidity of frames]], and \(g^{-1}z=q^{-1}y\), so the frame vectors of \(g^{-1}z\) and \(z\) are at distance \(<(N\rho)^{-1}\) at every place. Hence \(p^{-1}q\) fixes the frame, that is \(pf=qf\) ([[?lean:New.Filling.frameImage_inv_mul_eq_iff|equal frame images]]), contradicting injectivity on \(u\). So the points \(\phi(p)\), \(p\in u\), are pairwise at distance at least \((N\rho)^{-1}\) and lie in the ball of radius \(2\rho\) of \(\mathcal V\).

*Counting.* By the [[?lean:New.encard_le_of_separated|packing bound]] in a finite-dimensional real normed space (comparison of volumes: \(m\)-separated points of norm at most \(r\) number at most \((1+2r/m)^{\dim}\)), the number of frames is at most \((1+4N\rho^2)^{\dim\mathcal V}\). Finally \(N\le b^{60n}\) (standing hypotheses) and \(1\le b^{60n}\rho^2\), so
\[
1+4N\rho^2\le5\,b^{60n}\rho^2\le b\cdot b^{60n}\cdot b^{74n}R^2=b^{134n+1}R^2\le b^{6n^2}R^2,
\]
using \(b\ge1000\) and \(n\ge23\) (indeed \(\varrho\ge10^5\)).

## References

1. Lean: `New.Filling.encard_image_frameImage_le` in `src/New/Spanning/Unfolding/Packing.lean`.
