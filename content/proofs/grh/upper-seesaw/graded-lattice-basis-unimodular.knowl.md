+++
id = "proofs/grh/upper-seesaw/graded-lattice-basis-unimodular"
title = "The glued lattice is unimodular"
kind = "lemma"
summary = "If N = pi pi-bar, the Gram matrix of the glued lattice basis is the glued Gram matrix G(N,0), hermitian and invertible over every subring."
aliases = ["unimodularity of the glued lattice basis"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.gram_gradedLatticeBasis_eq_gluedGram", "New.Seesaw.isUnimodular_gradedLatticeBasis_gram", "New.Seesaw.gluedGram_mul_eq_one", "New.Seesaw.map_gluedGram", "New.Seesaw.map_gradedGram", "New.Seesaw.isHermitian_map_gradedGram_natCast"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
proof_status = "full"
+++

**Lemma.** Let \(R\) be a commutative ring with involution, \(N\) a natural number, and
\(a,\pi\in R^{\times}\), \(u\in R\) with \(\bar uu=1\). Let \(J\) be the
[[?lean:New.gradedGram|graded Gram matrix]] with parameter \(N\) (identity on \(X=X'\sqcup\{y\}\),
string paired antidiagonally, \(-N\) at the middle), and let \(\mathcal{B}=\mathcal{B}(a,\pi,u)\) be
the [[proofs/grh/upper-seesaw/graded-lattice-basis|glued lattice basis]]. If \(N=\pi\bar\pi\) in
\(R\), then
\[
\mathcal{B}^{*}J\,\mathcal{B}=G(N,0),
\]
the glued Gram matrix with parameters \((N,0)\). Moreover \(G(N,0)\,G(0,N)=1\). Consequently, for
every subring \(O\subseteq R\), the matrix \(\mathcal{B}^{*}J\mathcal{B}\) is unimodular over
\(O\): it is [[linear-algebra/hermitian-matrix|hermitian]], has entries in \(O\) and is invertible
in \(\mathrm{GL}(O)\).

## Proof

*Gram matrix.* The vectors \(x_i\) are unchanged and orthogonal to everything else.

For even \(s\): \(y\) is unchanged, of norm \(1\), orthogonal to the string. For \(2b<s\) the
partner \(s-1-b\) lies in the second half, and
\(\langle ua^{-1}z_b,\,u\bar a z_{s-1-b}\rangle=\overline{ua^{-1}}\cdot u\bar a\) or its conjugate
\(\overline{u\bar a}\cdot ua^{-1}\); both equal \(\bar uu=1\). All other pairings of string vectors
vanish. This is \(G(N,0)\) (for even \(s\) the parameters do not enter).

For odd \(s\) with middle index \(c\): the string vectors \(uz_b\) pair as the \(z_b\) do, because
\(\bar uu=1\); in particular \(\langle uz_c,uz_c\rangle=-N\). For
\(y'=\bar\pi^{-1}y+u(\pi\bar\pi)^{-1}z_c\),
\[
\langle y',y'\rangle=(\pi\bar\pi)^{-1}+(\pi\bar\pi)^{-2}\,\bar uu\,(-N)=(\pi\bar\pi)^{-1}-(\pi\bar\pi)^{-1}=0,
\]
\[
\langle y',uz_c\rangle=\overline{u(\pi\bar\pi)^{-1}}\,u\,(-N)=-1,
\]
using \(N=\pi\bar\pi\) and that \(\pi\bar\pi\) is fixed by the involution; and \(y'\perp uz_b\) for
\(b\ne c\). This is \(G(N,0)\).

*Inverse.* Compute \(G(p,0)G(0,p)\) by blocks. For even \(s\) both are the same involutive matrix
(identity on \(X\), antidiagonal on the string). For odd \(s\), on the plane spanned by \(y,z_c\) the
two matrices are \(\begin{pmatrix}0&-1\\-1&-p\end{pmatrix}\) and
\(\begin{pmatrix}p&-1\\-1&0\end{pmatrix}\), whose product is the identity; elsewhere both are the
identity on \(X'\) and the antidiagonal pairing on \(z_b\), \(b\neq c\).

*Unimodularity.* \(J\) is hermitian since its entries \(0,1,-N\) are fixed by the involution and it
is symmetric; hence so is \(\mathcal{B}^{*}J\mathcal{B}\). The matrices \(G(N,0)\) and \(G(0,N)\)
have entries in every subring \(O\) and are mutually inverse. \(\blacksquare\)

## Remarks

In Lean the form \(J\) is given over a ring \(S\) and carried to \(R\) by a homomorphism \(f\);
\(f\) commutes with forming the graded and glued Gram matrices.

## References

1. Lean: `New.Seesaw.gram_gradedLatticeBasis_eq_gluedGram`, `New.Seesaw.gluedGram_mul_eq_one`, `New.Seesaw.isUnimodular_gradedLatticeBasis_gram` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
