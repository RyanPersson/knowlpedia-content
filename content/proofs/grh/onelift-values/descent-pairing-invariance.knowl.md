+++
id = "proofs/grh/onelift-values/descent-pairing-invariance"
title = "Invariance of the descent pairing under the maximal level"
kind = "lemma"
summary = "Translating the finite datum by an integral point k of U(V) and the form by the same k leaves the descent pairing unchanged; on the level group this gives invariance under the twisted translation of the datum alone."
aliases = ["level translate"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.descentPairing_translate", "New.DescentPair.descentPairing_levelTranslate", "New.DescentPair.levelTranslate", "New.DescentPair.leftMul_mem_integralBox_iff", "New.DescentPair.cosetIndicator_leftMul_inv", "New.DescentPair.cosetIndicator_leftMul_inv_of_fixed", "New.DescentPair.finite_range_levelTranslate", "New.exists_fixed_forall_linearMap_eq_of_finite"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/onelift-values/descent-pairing|the descent pairing]] \(B=B_{u,P,g}\) of a
descent pair \(O\). Let \(K_0\) be the [[?lean:New.stdLevel|maximal level]] of \(U(V)(\mathbb{A}_f)\) (the
points with integral matrix and integral inverse), \(K_O\subset K_0\) the
[[?lean:New.DescentPair.levelGroup|level group]] of \(O\) and
\(\psi_O\colon K_O\to\mathbb{C}^\times\) its [[?lean:New.DescentPair.levelChar|level character]],
\(\psi_O(h)=\prod_{w\in Q}\chi_w(\det h'_w)^{-1}\) with \(h'_w\) the \(\iota\times\iota\) block of the
reduction of \(h\) at \(w\). For \(h\in K_O\) the **level translate** of a function \(\Psi\) on
\(M_{n\times r}(\mathbb{A}_f)\) is
\[
(T_h\Psi)(x)=\overline{\psi_O(h)}\;\Psi(h^{-1}x);
\]
this is a representation of \(K_O\).

**Lemma.** Let \(\Psi\) be Schwartz–Bruhat above \(S_O\).

1. If \(k\in K_0\) and \(y,y'\in\mathcal{F}_V\) satisfy \(y'=k\cdot y\) (right translation by \(k\)), then
   \(B(\Psi(k^{-1}\,\cdot\,),y')=B(\Psi,y)\).
2. For \(h\in K_O\), \(B(T_h\Psi,y)=B(\Psi,y)\).
3. For \(k\in K_0\), an idele \(t\) and a point \(z\), the indicator \(\mathbf 1_{z,t}\) of the class
   \(\{x: t^{-1}(x-z)\ \text{integral at } S_O\}\) satisfies
   \(\mathbf 1_{z,t}(k^{-1}x)=\mathbf 1_{kz,t}(x)\); in particular it is unchanged if \(kz\) and \(z\) have
   the same components at \(S_O\).
4. The indicator of a class modulo \(i!\) has only finitely many level translates \(T_h\mathbf 1\),
   \(h\in K_O\). Hence there is a function \(\Psi_1\), their mean, that is fixed by all \(T_h\) and such
   that \(L(\Psi_1)=c\) for every linear form \(L\) taking the constant value \(c\) on these translates.

## Proof

(1) The theta lift is equivariant: for an automorphic function \(Y\) on \(U(V)\), a datum \(\varphi\) and
\(k\in U(V)(\mathbb{A})\), the lift of \(Y(\,\cdot\,k)\) with datum \(\omega(1,k)\varphi\) equals the lift of
\(Y\) with datum \(\varphi\) (change of variable \(h\mapsto hk^{-1}\) in the integral over \([U(V)]\);
[[?lean:New.ThetaKernel.lift_equivariant|equivariance of the lift]]). Take \(Y=\overline{c_u(y)}\); since
\(c_u(k\cdot y)(h)=c_u(y)(hk)\), the function \(\overline{c_u(y')}\) is \(Y(\,\cdot\,k)\). The Weil
representation of the finite integral element \(k\) fixes the Fock vector \(v_P\) (it acts at the finite
places only), fixes the vacuum at the places outside \(S_O\) and their conjugates (\(k\) is integral there,
and \(S_O\) is disjoint from its conjugate), and at the places of \(S_O\), which are split, acts on
functions of \(x\) by \(\Psi\mapsto\Psi(k^{-1}x)\) with trivial scalar because \(k\) is integral
([[?lean:New.pairWeil_schrodingerOp_of_mem|action on Schrödinger data]]). So
\(\omega(1,k)(v_P\otimes\Psi\otimes\mathrm{vac})=v_P\otimes\Psi(k^{-1}\cdot)\otimes\mathrm{vac}\) and (1)
follows.

(2) A form \(y\in\mathcal{F}_V\) satisfies \(h\cdot y=\psi_O(h)\,y\) for \(h\in K_O\). By
conjugate-linearity in \(y\) and (1),
\(B(T_h\Psi,y)=\overline{\psi_O(h)}B(\Psi(h^{-1}\cdot),y)=B(\Psi(h^{-1}\cdot),\psi_O(h)y)=B(\Psi,y)\).

(3) Elements of \(K_0\) preserve the matrices that are integral at \(S_O\) (their entries and those of the
inverse are integral). Since \(k\bigl(t^{-1}(k^{-1}x-z)\bigr)=t^{-1}(x-kz)\), the first claim follows; the
second because the indicator depends on \(kz\) only through its components at \(S_O\).

(4) By (3), \(T_h\mathbf 1_{z,i!}=\overline{\psi_O(h)}\,\mathbf 1_{hz,i!}\). The character \(\psi_O\) factors
through a finite group, and \(k\mapsto\mathbf 1_{kz,i!}\) is a locally constant map on the compact group
\(K_0\) (the class of a point modulo \(i!\) is locally constant in the point), hence has finite image. For
the mean: if \(T\) is the finite set of translates, each \(T_h\) permutes \(T\), so
\(\Psi_1=\lvert T\rvert^{-1}\sum_{f\in T}f\) is fixed, and \(L(\Psi_1)=c\) when \(L\equiv c\) on \(T\).
\(\blacksquare\)

## References

1. Lean: `New.DescentPair.descentPairing_translate`, `New.DescentPair.descentPairing_levelTranslate`, `New.DescentPair.finite_range_levelTranslate`, `New.exists_fixed_forall_linearMap_eq_of_finite` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
