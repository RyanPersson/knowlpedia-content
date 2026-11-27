+++
id = "proofs/grh/spanning-core/sizes-near-a-point-of-the-open-cell"
title = "Sizes at and near a point of the open cell"
kind = "lemma"
summary = "A lower bound for the frame discriminant and an upper bound for the entries bound the matrix, its inverse and 1/nu by a power, also on a small ball."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.RealPlace.isBoundedInCell_of_inv_le_gramDiscReal", "New.RealPlace.gramDiscReal_div_two_le_and_isBoundedInCell", "New.RealPlace.l2_opNorm_le_pow_four", "New.gramDiscReal_le_pow", "New.inv_pow_div_gramDiscReal_le", "New.le_pow_div_gramDiscReal"]
lean_files = ["src/New/Spanning/Bessel/OpenCellBound.lean"]
proof_status = "full"
+++

**Lemma.** Let \(Z\) be a complex \(n\times n\) matrix, \(n=\varrho+1\), with [[proofs/grh/spanning-core/frame-discriminant|frame discriminant]] \(\mathsf g(Z)\), and \(M\) a real number such that all entries of \(Z\) have modulus at most \(M^2\) and \(\mathsf g(Z)\ge M^{-1}\).

1. If \(M\ge n\), then \(Z\) is [[proofs/grh/spanning-core/open-cell-of-frame-matrices|bounded in the cell]] by every \(T\ge M^{8n}\).
2. If \(M\ge8n\) and \(P\ge M^{9n}\), then every \(Z'\) with \(\lVert Z'-Z\rVert<P^{-6}\) satisfies \(\mathsf g(Z')\ge\tfrac12\mathsf g(Z)\) and is bounded in the cell by \(P\).
3. If \(\mathsf g(Z)>0\), \(\rho\ge n\) and the entries of \(Z\) have modulus at most \(\rho^2\), then \(\mathsf g(Z)\le\rho^{8n}\) and \(\rho\le\rho^{9n}/\mathsf g(Z)\).

## Proof

A square matrix of size \(l\le M\) with entries bounded by \(M^2\) has operator norm at most \(l\cdot l\cdot M^2\le M^4\) (the Lean entrywise bound), hence determinant of modulus at most \((M^4)^l\).

(1) \(\mathsf g(Z)>0\) gives \(Z\in\Omega\). \(\lVert Z\rVert\le M^4\). From \(M^{-1}\le\mathsf g(Z)=\lvert\det Z\rvert^2\nu(Z)^2\) and \(M^{-2}\le M^{-1}\): \((\lvert\det Z\rvert\nu(Z))^{-1}\le M\). As \(\nu\le1\), \(\lvert\det Z\rvert^{-1}\le M\); by Cramer's rule the entries of \(Z^{-1}\) are minors of size \(\varrho\) divided by \(\det Z\), so \(\lVert Z^{-1}\rVert\le M\cdot n^2(M^4)^\varrho\le M\cdot M^2\cdot M^{4\varrho}=M^{3+4\varrho}\). And \(1/\nu(Z)\le\lvert\det Z\rvert M\le M^{4n+1}\). All exponents are at most \(8n\).

(2) \(M^{8n}\le P/2\) (since \(M^{8n+1}\le P\) and \(M\ge2\)), so by (1) \(Z\) is bounded in the cell by \(P/2\), and \(P^{-6}\le(P/2)^{-6}\). Apply the perturbation part of the [[proofs/grh/spanning-core/bounds-for-the-gram-section|bounds for the Gram section]] with \(T=P/2\ge8\), \(T\ge n\).

(3) \(\mathsf g(Z)=\lvert\det Z\rvert^2\nu(Z)^2\le((\rho^4)^n)^2\); and \(\rho\,\mathsf g(Z)\le\rho^{8n+1}\le\rho^{9n}\). \(\blacksquare\)

## References

1. Lean: `New.RealPlace.isBoundedInCell_of_inv_le_gramDiscReal`, `New.RealPlace.gramDiscReal_div_two_le_and_isBoundedInCell`, `New.gramDiscReal_le_pow`, `New.le_pow_div_gramDiscReal` in `src/New/Spanning/Bessel/OpenCellBound.lean`.
