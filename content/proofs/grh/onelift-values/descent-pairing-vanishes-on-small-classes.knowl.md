+++
id = "proofs/grh/onelift-values/descent-pairing-vanishes-on-small-classes"
title = "The descent pairing vanishes on indicators of small classes"
kind = "proposition"
summary = "For a form whose block descent vanishes and which is annihilated by the hyperplane sums, the descent pairing with the indicator of the class of any point modulo i! is zero for large i."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.eventually_descentPairing_eq_zero_of_hasIntegralBlockRatio", "New.DescentPair.descentPairing_eq_zero_of_not_hasIntegralBlockRatio"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
proof_status = "full"
+++

Let \(O\) be a [[?lean:New.DescentPair|descent pair]], \(y\in\mathcal{F}_V\) a form, and
\(B=B_{u,P,g}\) the [[proofs/grh/onelift-values/descent-pairing|descent pairing]]. For
\(z\in M_{n\times r}(\mathbb{A}_f)\) and a finite idele \(t\) let \(\mathbf 1_{z,t}\) be the indicator of the
class \(\{x:t^{-1}(x-z)\text{ integral at }S_O\}\).

**Proposition.**

(a) Suppose the [[proofs/grh/onelift-values/descent-pairing|block descent]] of \(y\) vanishes for \(u\) and
\(P\). If \(z_w\) has an [[proofs/grh/onelift-values/integral-block-ratio|integral block ratio]] at every
place \(w\in S_O\), then \(B(\mathbf 1_{z,i!},y)=0\) for all sufficiently large \(i\).

(b) Suppose \(\chi_w\ne1\) for all \(w\in Q\) and the
[[proofs/grh/onelift-values/hyperplane-sums-annihilate|hyperplane sums annihilate]] \(y\). If at some place
\(w\in S_O\) the component \(z_w\) has no integral block ratio, then \(B(\mathbf 1_{z,t},y)=0\) for every
idele \(t\).

## Proof

(a) Let \(A\) be the finite adelic point of \(U(W)\) with components \(z'^{-1}_w\) at the places of \(S_O\)
and \(1\) away from \(S_O\) and its conjugate. By
[[proofs/grh/onelift-values/translated-block-datum|the translated block datum]] (4), \(\Psi_A(z)=1\). Since
\(\Psi_A\) is Schwartz–Bruhat above \(S_O\), it is constant, equal to \(1\), on the class \(C_i\) of \(z\)
modulo \(i!\) for all large \(i\)
([[proofs/grh/onelift-values/factorial-classes-span-schwartz-bruhat|Step 1]]). Fix such \(i\) and let
\(\Psi_1\) be the mean of the level translates \(T_h\mathbf 1_{C_i}\), \(h\in K_O\)
([[proofs/grh/onelift-values/descent-pairing-invariance|invariance]] (4)). Then:

* \(B(\Psi_1,y)=B(\mathbf 1_{C_i},y)\), because \(\Psi\mapsto B(\Psi,y)\) is constant on the translates;
* \(\Psi_1\) depends only on the components at \(S_O\), because each translate does;
* \(\Psi_1\) vanishes where \(\Psi_A\) does: if \(\Psi_A(x)=0\) then \(\Psi_A(h^{-1}x)=0\) for all \(h\in K_O\)
  (eigenfunction property), so \(h^{-1}x\notin C_i\) (where \(\Psi_A=1\)), so every translate vanishes at
  \(x\);
* \(T_h\Psi_1=\Psi_1\).

By uniqueness, \(\Psi_1=\Psi_1(z)\Psi_A\), and \(B(\Psi_A,y)=0\) by the vanishing property (5). Hence
\(B(\mathbf 1_{C_i},y)=0\).

(b) By [[proofs/grh/onelift-values/annihilating-row-exists|the dichotomy]] \(z_w\) has an annihilating row
\(l\); let \(\bar\lambda\ne0\) be the reduction of its part on \(\iota\) and \(H=H_{\bar\lambda}\). For each
\(s\in H\), the [[proofs/grh/onelift-values/triangular-level-action|shear corollary]] gives \(h\in K_0\) with
\(hz\equiv z\) at \(S_O\) and \(h\cdot y=s\star y\). By
[[proofs/grh/onelift-values/descent-pairing-invariance|invariance]] (1) and (3),
\(B(\mathbf 1_{z,t},s\star y)=B(\mathbf 1_{z,t}(h^{-1}\cdot),h\cdot y)=B(\mathbf 1_{z,t},y)\). Summing over
\(s\in H\) and using conjugate-linearity,
\[
\lvert H\rvert\,B(\mathbf 1_{z,t},y)=B\Bigl(\mathbf 1_{z,t},\sum_{s\in H}s\star y\Bigr)=0,
\]
by [[proofs/grh/onelift-values/hyperplane-sums-annihilate|property (2)]]. \(\blacksquare\)

## References

1. Lean: `New.DescentPair.eventually_descentPairing_eq_zero_of_hasIntegralBlockRatio`, `New.DescentPair.descentPairing_eq_zero_of_not_hasIntegralBlockRatio` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
