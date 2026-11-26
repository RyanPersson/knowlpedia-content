+++
id = "proofs/grh/onelift-comparison/hecke-polynomial-is-normal"
title = "The idempotent is self-adjoint and the Hecke polynomial is normal at every conjugate"
kind = "lemma"
summary = "For every pairing at sigma the group action is unitary, central idempotents are self-adjoint, Hecke polynomials commute and are normal, and their image is orthogonal to their kernel."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.isOfFinOrder_prod_tamePart_det", "New.DescentPair.innerAt_formAction", "New.DescentPair.range_groupAlgAction_mem_invtSubmodule", "New.DescentPair.heckePolyOnForms_comm", "New.DescentPair.innerAt_groupAlgAction", "New.DescentPair.exists_adjoint_heckePolyOnForms_comm", "New.DescentPair.innerAt_heckePolyOnForms_eq_zero", "New.DescentPair.orthogonal_range_heckePolyOnForms_le_ker", "New.DescentPair.normSqAt_eq_re_innerAt", "New.DescentPair.normSqAt_le_add_of_innerAt_eq_zero"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
proof_status = "full"
+++

**Lemma.** Notation as in [[proofs/grh/onelift-comparison/false-lifts|false lifts]] and [[proofs/grh/onelift-comparison/adjoint-of-hecke-polynomial|the adjoint of the Hecke polynomial]]; \(\sigma\in\operatorname{Aut}(\mathbb{C})\), \(w\ne\bar w\) and \(u\ne\bar u\) finite places off the level, \(X,Y\in\mathbb{C}\).

1. \(\langle gx,gy\rangle_\sigma=\langle x,y\rangle_\sigma\) for \(g\in\bar G_M\) and forms \(x,y\).
2. If \(e_0\in\mathbb{C}[\bar G_M]\) is a central idempotent (an [[algebra-rings/idempotent-element|idempotent]] whose coefficients form a [[algebra-groups/class-function|class function]]), then \(\langle e_0x,y\rangle_\sigma=\langle x,e_0y\rangle_\sigma\).
3. \(H_w(X)H_u(Y)=H_u(Y)H_w(X)\) (the places may be equal or conjugate). An operator commuting with the action of \(\bar G_M\) preserves \(\operatorname{im}(e_0)\) for every \(e_0\).
4. \(H_w(X)\) has an adjoint for \(\langle\ ,\ \rangle_\sigma\) with which it commutes, namely \(H_{\bar w}(c_\sigma X)\).
5. If \(H_w(X)z=0\) then \(\langle H_w(X)v,z\rangle_\sigma=0\) for all \(v\). For \(\sigma=1\): \((\operatorname{im}H_w(X))^\perp\subseteq\ker H_w(X)\).
6. With \(\lVert v\rVert_\sigma^2\) the [[?lean:New.LevelPlaces.LevelForm.normSqAt|squared norm at \(\sigma\)]] (the class sum of the squared Gram norms of the vectors \(\sigma(v(g))\)): \(\lVert v\rVert^2_\sigma=\operatorname{Re}\sigma(\langle v,v\rangle_\sigma)\); and if \(\langle x,z\rangle_\sigma=0\) then \(\lVert z\rVert_\sigma^2\le\lVert z+x\rVert_\sigma^2\).

## Proof

1. \(g\) acts as \(c\,T\) with \(T\) a right translation and \(c=\prod_w\psi_w(\det g_w)\) a root of unity (a product of values of finite-order characters at units). Then \(\lvert\sigma c\rvert=1\), so \(c_\sigma(c)\,c=\sigma^{-1}(\overline{\sigma c}\,\sigma c)=1\), and with the invariant pairing \(B\) of the adjoint lemma, \(\langle gx,gy\rangle_\sigma=c_\sigma(c)c\,B(Tx,Ty)=B(x,y)\).

2. By 1, \(\langle gx,y\rangle_\sigma=\langle x,g^{-1}y\rangle_\sigma\). Write \(e_0=\sum_g a_g\,g\). The element \(\sigma(e_0)=\sum\sigma(a_g)g\) is again a central idempotent, and for a central idempotent the function \(g\mapsto\#\bar G_M\cdot(\text{coefficient at }g)\) is a character of \(\bar G_M\) ([[?lean:New.IsCentralProj.isChar_card_mul_coeff|coefficients of a central idempotent]]); a character takes complex-conjugate values at \(g\) and \(g^{-1}\). Hence \(\sigma(a_{g^{-1}})=\overline{\sigma(a_g)}\), i.e. \(c_\sigma(a_g)=a_{g^{-1}}\). Therefore \(\langle a_g\,gx,y\rangle_\sigma=c_\sigma(a_g)\langle x,g^{-1}y\rangle_\sigma=\langle x,a_{g^{-1}}g^{-1}y\rangle_\sigma\), and summing over \(g\) gives the claim ([[?lean:New.IsCentralProj.self_adjoint|self-adjointness of central idempotents]]).

3. Both sides are double sums of products \(T_{w,i}T_{u,j}\) of Hecke operators, which commute on forms spherical at both places (for \(u\in\{w,\bar w\}\) because the spherical Hecke algebra at a place is commutative; otherwise because they act at different places). The second claim holds since \(e_0\) acts as a linear combination of the operators of \(g\in\bar G_M\).

4. This is the [[proofs/grh/onelift-comparison/adjoint-of-hecke-polynomial|adjoint formula]] together with 3 (note \(\bar w\) is off the level when \(w\) is).

5. Let \(A=H_w(X)\) with adjoint \(A'\), \(AA'=A'A\). If \(Az=0\) then \(\langle A'z,A'z\rangle_\sigma=\langle AA'z,z\rangle_\sigma=\langle A'Az,z\rangle_\sigma=0\), so \(A'z=0\) by definiteness of \(\langle\ ,\ \rangle_\sigma\) ([[?lean:New.LevelPlaces.LevelForm.eq_zero_of_innerAt_self|definiteness]]), and \(\langle Av,z\rangle_\sigma=\langle v,A'z\rangle_\sigma=0\). For the second claim take \(u\perp\operatorname{im}A\); then \(\langle Au,Au\rangle=\langle u,A'Au\rangle=\langle u,AA'u\rangle=0\), so \(Au=0\).

6. The first identity is the class-sum formula for \(\langle\ ,\ \rangle_\sigma\) applied to \(v,v\). If \(\langle x,z\rangle_\sigma=0\) then also \(\langle z,x\rangle_\sigma=0\) (the pairing is \(c_\sigma\)-hermitian), so \(\lVert z+x\rVert_\sigma^2=\lVert z\rVert_\sigma^2+\lVert x\rVert_\sigma^2\ge\lVert z\rVert_\sigma^2\).

## References

1. Lean: `New.DescentPair.isOfFinOrder_prod_tamePart_det`, `New.DescentPair.innerAt_formAction`, `New.DescentPair.range_groupAlgAction_mem_invtSubmodule`, `New.DescentPair.heckePolyOnForms_comm`, `New.DescentPair.innerAt_groupAlgAction`, `New.DescentPair.exists_adjoint_heckePolyOnForms_comm`, `New.DescentPair.innerAt_heckePolyOnForms_eq_zero`, `New.DescentPair.orthogonal_range_heckePolyOnForms_le_ker`, `New.DescentPair.normSqAt_eq_re_innerAt`, `New.DescentPair.normSqAt_le_add_of_innerAt_eq_zero` in `src/New/OneLift/TestedForms.lean`.
