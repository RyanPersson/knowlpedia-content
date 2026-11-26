+++
id = "proofs/grh/spanning-core/unfolding-bound-on-the-real-group"
title = "An unfolding bound on the real unitary group"
kind = "lemma"
summary = "The integral of phi w over the group is bounded by the integral of w over the quotient by the unipotent group, when phi has bounded mass on orbits of the frame-fixing unipotent group and bounded frame matrices."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.lintegral_mul_le_of_frameMatrix_le", "New.volume_upperEntries_closedBall_le", "New.RealPlace.norm_frameMatrix_le_of_isBoundedInCell"]
lean_files = ["src/New/Spanning/Bessel/SobolevBound.lean"]
proof_status = "full"
+++

**Lemma (unfolding bound).** Let \(G_1\) be the real unitary group of a shape, \(n=\varrho+1\), \(\mathsf U\) the Bessel unipotent group with its Haar measure \(du\), \(\mathsf U^0\subseteq\mathsf U\) the subgroup fixing the frame with its Haar measure \(du_0\), \(S\) the Bessel subgroup, and \(\mu\) the [[?lean:New.besselQuotMeasure|measure for \(\mathsf U\backslash G_1\)]]. Let \(w,\varphi\colon G_1\to[0,\infty]\) be measurable, \(K\in[0,\infty]\), \(R\ge1\), such that

* \(w(sy)=w(y)\) for \(s\in S\);
* \(\int_{\mathsf U^0}\varphi(u_0y)\,du_0\le K\) for all \(y\);
* if \(\varphi(y)\neq0\), \(s\in\mathsf U\) and \(\varphi(sy)\ne0\), then all entries of the [[?lean:New.frameMatrix|frame matrix]] of \(s\) have modulus at most \(R\).

Then
\[
\int_{G_1}\varphi(y)w(y)\,dy\ \le\ K\,(2R)^{2n^2}\int w\,d\mu .
\]
**Complement.** If \(s\in\mathsf U\) and the [[proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry|frame Gram matrices]] \(Z(y)\), \(Z(sy)\) are both [[proofs/grh/spanning-core/open-cell-of-frame-matrices|bounded in the cell]] by \(P\), then the entries of the frame matrix of \(s\) have modulus at most \(P^2\).

## Proof

The measure \(\mu\) satisfies \(\int_{G_1}g(y)\,dy=\int\!\int_{\mathsf U}g(uy)\,du\,d\mu(y)\) for measurable \(g\ge0\) (library statement `New.lintegral_orbitMeasure_lintegral`). With \(g=\varphi w\) and the invariance of \(w\), it suffices to show \(\int_{\mathsf U}\varphi(uy)\,du\le K(2R)^{2n^2}\) for every \(y\). If \(\varphi(uy)=0\) for all \(u\) this is clear. Otherwise fix \(u_1\in\mathsf U\) with \(\varphi(u_1y)\ne0\). The Haar measure of \(\mathsf U\) is, by definition, the image of \(dx\,du_0\) under \((x,u_0)\mapsto u_0\,\lambda(x)\), where \(x\) runs over the families of entries above the diagonal of an \(n\times n\) matrix (Lebesgue measure) and \(\lambda(x)\in\mathsf U\) is the [[?lean:New.RealPlace.liftUnitriangular|lift]] with frame matrix the unitriangular matrix with entries \(x\); and it is right invariant. Hence
\[
\int_{\mathsf U}\varphi(uy)\,du=\int\!\!\int_{\mathsf U^0}\varphi\bigl(u_0\lambda(x)u_1y\bigr)\,du_0\,dx .
\]
If the inner integrand is nonzero for some \(u_0\), the third hypothesis applied to \(u_1y\) and \(s=u_0\lambda(x)\), whose frame matrix is that of \(\lambda(x)\) (as \(u_0\) fixes the frame), shows \(\lvert x_{ab}\rvert\le R\) for all \(a<b\). So the outer integral runs over a box of at most \(n^2\) discs of radius \(R\), of volume at most \((\pi R^2)^{n^2}\le(2R)^{2n^2}\), and the inner integral is at most \(K\).

*Complement.* By the [[proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry|frame Gram rules]], \(Z(y)=m(s)^*Z(sy)\), so \(m(s)^*=Z(y)Z(sy)^{-1}\) has norm at most \(P\cdot P\). \(\blacksquare\)

## References

1. Lean: `New.lintegral_mul_le_of_frameMatrix_le`, `New.RealPlace.norm_frameMatrix_le_of_isBoundedInCell` in `src/New/Spanning/Bessel/SobolevBound.lean`.
