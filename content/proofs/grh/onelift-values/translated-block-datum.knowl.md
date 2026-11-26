+++
id = "proofs/grh/onelift-values/translated-block-datum"
title = "Right translates of the block datum and their characterisation"
kind = "lemma"
summary = "The right translate of the block function by a point A of GL_r is an eigenfunction of the level group whose support is one orbit; any level-invariant function supported there is a multiple of it, and its descent pairing vanishes when the block descent does."
aliases = ["translated block function"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.translatedBlockFn", "New.DescentPair.translatedBlockFn_leftMul", "New.DescentPair.exists_leftMul_eq_of_translatedBlockFn_ne_zero", "New.DescentPair.eq_smul_translatedBlockFn", "New.DescentPair.translatedBlockFn_eq_one_of_hasIntegralBlockRatio", "New.DescentPair.exists_pairWeil_blockDatum_eq_smul", "New.DescentPair.descentPairing_translatedBlockFn_eq_zero", "New.DescentPair.residueBlockDatum_mul", "New.completeColumns", "New.DescentPair.exists_atPlace_eq", "New.DescentPair.exists_stdLevel_atPlace_eq"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/onelift-values/descent-pairing|the descent pairing]] and
[[proofs/grh/onelift-values/descent-pairing-invariance|its invariance]]. For a finite adelic point \(A\) of
\(U(W)\), read as an element of \(\mathrm{GL}_r(\mathbb{A}_f)\), the **translated block function** is
\[
\Psi_A(x)=\Psi_{\mathrm{bl}}(xA),\qquad x\in M_{n\times r}(\mathbb{A}_f).
\]
It is Schwartz–Bruhat above \(S_O\). Let \(e=(1,0)^{\mathsf T}\) be the \(n\times r\) matrix with the
identity in the rows \(\iota\) and zero elsewhere.

**Lemma.**

1. (Eigenfunction.) \(\Psi_A(hx)=\overline{\psi_O(h)}\,\Psi_A(x)\) for \(h\in K_O\).
2. (Support is one orbit.) If \(\Psi_A(x)\ne0\) there is \(h\in K_O\) such that \(x\) and \(h\,e\,A^{-1}\)
   have the same components at the places of \(S_O\).
3. (Uniqueness.) Let \(\Psi\) depend only on the components at \(S_O\), satisfy \(T_h\Psi=\Psi\) for all
   \(h\in K_O\), and vanish wherever \(\Psi_A\) does. If \(\Psi_A(z)=1\) then \(\Psi=\Psi(z)\,\Psi_A\).
4. (Value one.) If \(z\) has an [[proofs/grh/onelift-values/integral-block-ratio|integral block ratio]] at
   every place \(w\) of \(S_O\) (with "chosen" meaning that \(w\) is a chosen place) and \(A_w=z'^{-1}_w\) at
   these places, then \(\Psi_A(z)=1\).
5. (Vanishing.) Suppose \(A\) is \(1\) at all places outside \(S_O\) and their conjugates. If the
   [[proofs/grh/onelift-values/descent-pairing|block descent]] of \(y\) vanishes for \(u\) and \(P\), then
   \(B_{u,P,g}(\Psi_A,y)=0\) for every \(g\).

Moreover every family of invertible local matrices at the places of \(S_O\) is the family of components of
a finite adelic point of the relevant unitary group that is \(1\) away from \(S_O\) and its conjugate; if the
matrices are invertible over the local integers, the point lies in \(K_0\).

## Proof

*Preliminary.* The places of \(S_O\) are split and no two of them are conjugate, so at such a place the
unitary group is a general linear group and one may prescribe the component at a place freely, the
component at the conjugate place being then determined
([[?lean:New.Gf.ofSplitPlace|point supported at a split place]]); multiplying such points for the
finitely many places gives the last assertion.

(1) Both sides vanish unless \(u=xA\) is integral at \(S_O\), since \(h\) preserves integrality. If \(u\) is
integral, both sides are read on reductions: with \(\tau_w\) the reduction of \(h\) and \(X_w\) that of
\(u\), we must show \(\Psi^{\mathrm{res}}(\tau X)=\overline{\psi_O(h)}\,\Psi^{\mathrm{res}}(X)\), where
\(\Psi^{\mathrm{res}}(X)=\prod_{w\in Q}\chi_w(\det X'_w)\) if \(X_w=e\) at all chosen \(w\), and \(0\)
otherwise. At a chosen place \(\tau_w e=e\), so \(\tau_wX_w=e\iff X_w=e\). At \(w\in Q\), \(\tau_w\) is block
lower triangular (zero entries in rows \(\iota\), columns outside \(\iota\)), so
\((\tau_wX_w)'=\tau'_wX'_w\) and \(\chi_w(\det(\tau_wX_w)')=\chi_w(\det\tau'_w)\chi_w(\det X'_w)\). The product
of the \(\chi_w(\det\tau'_w)\) is \(\psi_O(h)^{-1}=\overline{\psi_O(h)}\), as \(\psi_O\) is unitary.

(2) If \(\Psi_A(x)\ne0\), then \(xA\) is integral at \(S_O\) with components \(u_w\in M_{n\times r}(\mathcal
O_w)\), \(u_w\equiv e\) at chosen places and \(\det u'_w\) a unit at \(w\in Q\). Complete the columns: let
\(c_w=\begin{pmatrix}u'_w&0\\u''_w&1\end{pmatrix}\) (columns \(\iota\) those of \(u_w\), other columns those
of the identity). Then \(\det c_w=\det u'_w\) is a unit, \(c_we=u_w\), and \(c_w\) has zero upper right
block. By the preliminary there is \(h\in K_0\) with components \(c_w\); its reductions fix \(e\) at chosen
places and are block lower triangular at \(Q\), so \(h\in K_O\). At each \(w\in S_O\),
\((h\,e\,A^{-1})_w=u_wA_w^{-1}=x_w\).

(3) Both \(\Psi\) and \(\Psi_A\) depend only on the components at \(S_O\). Put \(b=eA^{-1}\). For \(x\) in the
support of \(\Psi_A\), (2) gives \(h\) with \(x\equiv hb\) at \(S_O\), so by invariance
\(\Psi(x)=(T_h\Psi)(hb)=\overline{\psi_O(h)}\Psi(b)\), and by (1)
\(\Psi_A(x)=\overline{\psi_O(h)}\Psi_A(b)\). Applying this to \(x\) and to \(z\) (where \(\Psi_A(z)=1\)) gives
\(\Psi(x)=\Psi(z)\Psi_A(x)\). Off the support of \(\Psi_A\) both sides vanish.

(4) The components of \(zA\) at \(S_O\) are \(z_wz'^{-1}_w=(1,\,z''_wz'^{-1}_w)^{\mathsf T}\), which are
integral, with upper block \(1\), and \(\equiv e\) at chosen places. So the support condition holds and
every factor \(\chi_w(\det 1)\) is \(1\).

(5) The Weil representation of the element \(A\) of \(U(W)(\mathbb{A}_f)\), which is supported on the split
places \(S_O\) and their conjugates, sends \(\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) to
\(c\cdot\Psi_A\otimes\mathrm{vac}\) with
\(c=\epsilon_n(\det A)^{-1}\lvert\det A\rvert^{n/2}\ne0\), the inverse of a value of the splitting character \(\epsilon_n\) of rank \(n\) (for the trivial character of \(U(1)\)) times a power of the idele norm
of the determinant of the part of \(A\) at \(S_O\) ([[?lean:New.pairWeil_schrodingerOp_of_mem_supportedOn|action on Schrödinger data]]);
it commutes with the Fock vector at infinity. The lift is equivariant in the \(U(W)\) variable: the lift
with datum \(\omega(A,1)\varphi\) at \(g\) is the lift with datum \(\varphi\) at \(gA\). Hence
\(c\,B_{u,P,g}(\Psi_A,y)\) is the value at \(gA\) of the lift with the block datum, which is \(0\).
\(\blacksquare\)

## References

1. Lean: `New.DescentPair.translatedBlockFn_leftMul`, `New.DescentPair.exists_leftMul_eq_of_translatedBlockFn_ne_zero`, `New.DescentPair.eq_smul_translatedBlockFn`, `New.DescentPair.translatedBlockFn_eq_one_of_hasIntegralBlockRatio`, `New.DescentPair.descentPairing_translatedBlockFn_eq_zero` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
