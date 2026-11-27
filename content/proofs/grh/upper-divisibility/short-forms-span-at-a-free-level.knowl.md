+++
id = "proofs/grh/upper-divisibility/short-forms-span-at-a-free-level"
title = "Short forms span at a free level"
kind = "theorem"
summary = "At a free level, the algebraic forms of a given weight are spanned by forms that are integral everywhere and of explicitly bounded size at every conjugate."
aliases = ["short forms span"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.span_isShort_eq_top", "New.isShort_deltaForm", "New.norm_weylRep_mulVec_det_smul_weylEval_le_one", "New.weylNormSq_det_smul_weylRep_mulVec_weylEval_le", "New.norm_weylEval_le_one_of_integral", "New.weylRep_mul_weylRep_zero"]
lean_files = ["src/New/UpperBound/Size/ShortColumns.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] with a fixed CM type and \(f\) infinite places, \(n\) a nonempty finite index set, and \(G_f\) the finite adelic points of the unitary group of the standard hermitian space \(E^{n}\), with group of rational points \(\Gamma\). Let \((\kappa,e)\) be a weight: at the infinite place \(\tau\) the [[?c:Young diagram|Young diagram]] has \(\kappa(\tau,h)\) columns of height \(h\), and \(e(\tau)\in\mathbb{Z}\) is the power of the determinant. Let \(K\subset G_f\) be a [[?lean:New.IsLevel|level]] (an open subgroup of the standard level of integral elements) that is **free**: \(\Gamma\cap gKg^{-1}=1\) for every \(g\in G_f\). Let \(N\ne0\) be a natural number lying in the [[?c:Different ideal|different]] of \(E/\mathbb{Q}\), let \(M\ge \lvert n\rvert f+\operatorname{boxes}\), where \(\operatorname{boxes}=\sum_\tau\sum_{h<\lvert n\rvert}h\,\kappa(\tau,h)\) is the number of [[?lean:New.boxes|boxes]] of \(\kappa\) in columns of height below \(\lvert n\rvert\), and put \(C=6N(f\lvert n\rvert)^2\) (the [[?lean:New.Space.shortBasisConst|short basis constant]]). If \(B\ge C^{6M}\), then the space of [[?lean:New.AlgForm|algebraic forms]] of weight \((\kappa,e)\) fixed by \(K\) is spanned over \(\mathbb{C}\) by its [[proofs/grh/upper-divisibility/short-form|\(B\)-short]] elements.

## Proof

*Step 1 (delta forms).* For \(x\in G_f\) and a coordinate vector \(v\) of the Weyl module, the delta form \(\delta_{x,v}\) is supported on \(\Gamma xK\) and has value \(\sum_\gamma\gamma^{-1}v\) at \(y\), summed over the \(\gamma\in\Gamma\) with \(x^{-1}\gamma y\in K\). At a free level every \(K\)-fixed form is a sum of delta forms, one for each class \(c\in\Gamma\backslash G_f/K\) with a chosen representative ([[?lean:New.freeLevelEquiv|`freeLevelEquiv`]]). So it suffices to show that for each representative \(c\) and each \(v\) the form \(\delta_{c,v}\) lies in the span \(S\) of the \(B\)-short forms.

*Step 2 (a delta form of a short integral vector is short).* If the gauge of \(v\) at \(x\) is at most \(1\) for every \(p\)-adic embedding and every conjugate of \(v\) has squared norm at most \(B\), then \(\delta_{x,v}\) is \(B\)-short. The gauge of \(\delta_{x,v}(g)\) at \(g\) is at most the gauge of \(v\) at \(x\) ([[?lean:New.Rows.weylGauge_deltaForm_le|`weylGauge_deltaForm_le`]]), and the squared norm of a conjugate of \(\delta_{x,v}(g)\) is at most \(\lvert\Gamma\cap xKx^{-1}\rvert^{2}\) times that of the conjugate of \(v\) ([[?lean:New.Rows.weylNormSq_deltaForm_le|`weylNormSq_deltaForm_le`]]); the group is trivial because \(K\) is free.

*Step 3 (short bases).* Because \(N\) lies in the different, each \(g\in G_f\) has a short basis ([[?lean:New.Space.exists_short_basis_stdSpace|`exists_short_basis_stdSpace`]]): an invertible matrix \(Y(g)\) over \(E\) such that \(g^{-1}Y(g)\) has entries in \(\widehat{\mathcal O}_E\) and every entry of every conjugate of \(Y(g)\) (under every embedding of \(E\) in \(\mathbb{C}\)) has absolute value at most \(C\).

*Step 4 (test vectors).* The Weyl module has coordinates given by products of minors with integer coefficients; let \(\operatorname{ev}(y)\) be the vector of their values at an array \(y\) of complex numbers. For a class representative \(c\) put
\[
A\;=\;\Bigl(\prod_\tau\det Y\bigl(c^{e(\tau)}\bigr)^{\tau}\Bigr)\cdot\rho_{\kappa,0}\bigl(Y(c)\bigr),
\]
where \((\cdot)^{\tau}\) denotes the weight embedding at \(\tau\), \(x\mapsto\Phi_\tau(\bar x)\) (the embedding \(\Phi_\tau\) of the CM type composed with complex conjugation of \(E\)), and \(\rho_{\kappa,0}\) is the action in weight \((\kappa,0)\) through these embeddings. The same embeddings, followed by \(\iota\colon\mathbb{C}\to\mathbb{C}_p\) and extended to the finite adeles, define the gauge; using \(\Phi_\tau\) without conjugation would read the other prime above \(p\). Let \(y\) be an array of roots of unity and \(v=A\operatorname{ev}(y)\).

*Integrality.* Acting by \(c^{-1}\) in weight \((\kappa,e)\) after \(A\) gives \(\prod_\tau d_\tau\) times the Schur matrix of the family \(c^{-1}Y(c)\), applied to \(\operatorname{ev}(\iota y)\), where \(d_\tau=\det\bigl(Y(c^{e(\tau)})\bigr)\det(c^{-1})^{e(\tau)}=\det\bigl((c^{e(\tau)})^{-1}Y(c^{e(\tau)})\bigr)\). The matrices \(c^{-1}Y(c)\) and \((c^{e(\tau)})^{-1}Y(c^{e(\tau)})\) are integral, so \(\lvert d_\tau\rvert_p\le1\); a Schur matrix of matrices with entries of absolute value at most \(1\) does not increase the maximum norm ([[?lean:New.Rows.norm_schur_mulVec_le|`norm_schur_mulVec_le`]]); and \(\operatorname{ev}(\iota y)\) consists of values of integer polynomials at numbers of absolute value \(1\). Hence the gauge of \(v\) at \(c\) is at most \(1\).

*Size.* For an automorphism \(\sigma\) of \(\mathbb{C}\), \(\sigma(v)\) has the same shape with \(Y\) replaced by conjugates and \(y\) by \(\sigma y\). With \(R=C\ge\lvert n\rvert\): the vector \(\rho_{\kappa,0}(Y_0)\operatorname{ev}(y)\) is the Schur matrix of \(z_\tau=Y_{0,\tau}\cdot(\text{square part of }y)\) applied to a fixed vector of squared norm \(1\); a Schur matrix multiplies squared norms by at most \(\prod_{\tau,i}\rho_{\tau,i}^{\lambda(\tau,i)}\) with \(\sum_i\rho_{\tau,i}\le\sum_{a,b}\lvert z_{\tau,ab}\rvert^2\le\lvert n\rvert^4R^2\le R^6\) ([[?lean:New.weylNormSq_schur_le|`weylNormSq_schur_le`]]), and the exponents \(\lambda(\tau,i)\) add up to the number of boxes; and \(\lvert\det Y_\tau\rvert^2\le(\lvert n\rvert^2R)^{2\lvert n\rvert}\le R^{6\lvert n\rvert}\). Together the squared norm of \(\sigma(v)\) is at most \(R^{6(\lvert n\rvert f+\operatorname{boxes})}\le C^{6M}\le B\).

By Step 2, \(\delta_{c,A\operatorname{ev}(y)}\in S\) for every array \(y\) of roots of unity.

*Step 5 (conclusion).* The linear map \(v\mapsto\delta_{c,Av}\) modulo \(S\) vanishes on all \(\operatorname{ev}(y)\) with entries of \(y\) in the infinite set of roots of unity; since the coordinates are polynomials, such evaluation vectors span the Weyl module ([[?lean:New.GL.ext_weylEval|`GL.ext_weylEval`]]). So the map is zero. The matrix \(A\) is invertible (a nonzero scalar times the action of invertible matrices), hence every \(\delta_{c,v}\) lies in \(S\). \(\blacksquare\)

*Status.* Steps 1 to 3 and the two Schur-matrix bounds and the spanning of evaluation vectors are quoted from the named declarations of other files; the combination is proved here in full.

## References

1. Lean: `New.span_isShort_eq_top` and the lemmas listed in the front matter, in `src/New/UpperBound/Size/ShortColumns.lean`.
