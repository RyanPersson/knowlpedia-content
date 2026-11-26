+++
id = "proofs/grh/upper-elementary-divisors/determinant-of-step-map"
title = "Determinant of the step map"
kind = "lemma"
summary = "For P > 1 the step map is invertible, and its determinant is a constant independent of the permutations times det(1 - pi/P^(m+1)) for the product pi of the permutations."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_det_permStep_eq", "New.det_permStep_ne_zero", "New.det_one_sub_comp_comm", "New.volume_positiveStepSet"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/PieriCone.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\mathcal{T}=\{0,\dots,m\}\) with addition modulo \(m+1\), signs \(v\), and \(P>1\); notation of the [[proofs/grh/upper-elementary-divisors/step-map-pieri-cone-slab|step map]].

1. \(\det\mathrm{St}_\sigma\ne0\) for every family \(\sigma\).
2. There is \(c\in\mathbb{R}\), independent of \(\sigma\), with \(\det\mathrm{St}_\sigma=c\cdot\Delta_{P^{m+1}}(\sigma_0\sigma_1\cdots\sigma_m)\) for all \(\sigma\).
3. For all \(D,\sigma,\tau\) and every set \(Y\): \(\operatorname{vol}\mathrm{Pos}_D(\sigma,\tau,Y)=\lvert\det\mathrm{St}_\sigma\rvert^{-1}\operatorname{vol}\bigl(Y\cap\mathrm{Slab}_k(D)\bigr)\) for [[measure-theory/lebesgue-measure|Lebesgue measure]].

## Proof

(1) If \(\mathrm{St}_\sigma\nu=0\) then \(P\nu(b,j+1)=\nu(\sigma_j(b),j)\) for all \(b,j\), so \(P\nu\) is a rearrangement of the entries of \(\nu\) and \(P\lVert\nu\rVert_\infty\le\lVert\nu\rVert_\infty\); as \(P>1\), \(\nu=0\).

(2) Let \(\pi_j=\sigma_0\cdots\sigma_{j-1}\) (so \(\pi_0=1\), \(\pi_{m+1}=\bar\sigma:=\sigma_0\cdots\sigma_m\), and \(\pi_{j+1}=\pi_j\sigma_j\)). Define linear maps: \(G\nu(b,j)=\nu(\pi_j(b),j)\); \(E\nu(b,j)=v_j\nu(b,j+1)\); \(N\nu(b,j)=P\nu(b,j)-\nu(b,j-1)\) for \(j\ge1\) and \(N\nu(b,0)=P\nu(b,0)\); \(A\colon\mathbb{R}^{k\times\mathcal{T}}\to\mathbb{R}^{k}\), \(A\nu(b)=\nu(\bar\sigma(b),m)\); \(B\colon\mathbb{R}^{k}\to\mathbb{R}^{k\times\mathcal{T}}\), \(Bx(b,j)=P^{-(j+1)}x(b)\). One checks \(N(1-BA)\nu(b,i)=P\nu(b,i)-\nu(b,i-1)\) for \(i\ge1\) and \(=P\nu(b,0)-\nu(\bar\sigma(b),m)\) for \(i=0\) (the terms \(P\cdot P^{-(i+1)}-P^{-i}\) cancel for \(i\ge1\)). Comparing entries with \(\pi_{j+1}=\pi_j\sigma_j\) gives the factorisation
\[
\mathrm{St}_\sigma\,G=E\,G\,N\,(1-BA).
\]
\(G\) is a permutation matrix, so \(\det G=\pm1\) cancels. By the identity \(\det(1-BA)=\det(1-AB)\) ([[?c:Weinstein–Aronszajn identity|Sylvester's determinant identity]]) and \(AB=P^{-(m+1)}\Pi_{\bar\sigma}\), we get \(\det\mathrm{St}_\sigma=\det E\cdot\det N\cdot\Delta_{P^{m+1}}(\bar\sigma)\), and \(E,N\) do not depend on \(\sigma\).

(3) Let \(L\nu=\mathrm{St}_\sigma(\nu^{\tau})\); \(\lvert\det L\rvert=\lvert\det\mathrm{St}_\sigma\rvert\ne0\). The degrees do not see the permutations: \(\sum_b(L\nu)(b,j)=\sum_b(\mathrm{St}\,\nu)(b,j)\). Hence \(\mathrm{Pos}_D(\sigma,\tau,Y)=L^{-1}\bigl(Y\cap\mathrm{Slab}_k(D)\cap\{\beta:\beta(x)\ne0\ \forall x\}\bigr)\); the coordinate hyperplanes are null sets, and the volume of the preimage of a set under an invertible linear map \(L\) is \(\lvert\det L\rvert^{-1}\) times its volume. \(\square\)

## References

1. Lean: `New.exists_det_permStep_eq`, `New.det_permStep_ne_zero`, `New.det_one_sub_comp_comm`, `New.volume_positiveStepSet` in `src/New/UpperBound/ElementaryDivisors/PieriCone.lean`.
