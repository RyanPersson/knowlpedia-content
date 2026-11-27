+++
id = "proofs/grh/spanning-unfolding-a/frame-matrices-of-unipotent-congruence-subgroup"
title = "Frame matrices of the unipotent congruence subgroups"
kind = "proposition"
summary = "The entries above the diagonal of the frame matrix of an element of the unipotent congruence subgroup are multiples of M by integers, and every elementary matrix 1 + M x E_ab occurs."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_frameMatrix_classUnipotent_eq_mul", "New.Filling.exists_classUnipotent_frameMatrix_eq", "New.Filling.exists_integral_form_besselFrame"]
lean_files = ["src/New/Spanning/Unfolding/ReducedPoints.lean"]
proof_status = "full"
+++

**Proposition.** Let \(E\) be a [[?c:CM field|CM field]], \(S\) [[?lean:New.Filling|filling data]] over \(E\) with level \(M\), \(c\) a [[?lean:New.Filling.Classes|class]] and \(\mathsf U_c(M)\) the [[?lean:New.Filling.classUnipotent|unipotent congruence subgroup at \(c\)]]. For \(u\in\mathsf U_c(M)\) let \(\Theta(u)\) be its [[?lean:New.frameMatrix|frame matrix]]: the \((\varrho+1)\times(\varrho+1)\) submatrix of \(u\) on the rows and columns of the frame \((f_0,\dots,f_\varrho)=(e_1,\dots,e_\varrho,z)\); it is [[?c:Unitriangular matrix|upper unitriangular]]. Let \(a<b\) be frame indices.

1. For every \(u\in\mathsf U_c(M)\) there is \(x\in\mathcal O_E\) with \(\Theta(u)_{ab}=Mx\).
2. If \(E\) contains a primitive 5040-th root of unity, then for every \(x\in\mathcal O_E\) there is \(u\in\mathsf U_c(M)\) with \(\Theta(u)=1+Mx\,E_{ab}\), where \(E_{ab}\) is the matrix unit.

The proof of 2 uses:

3. For every frame index \(b\) there is a row vector \(l\) over \(E\) that is integral on the lattice \(\Lambda_c\) of the class, has \(l(f_b)=1\), and vanishes at all other basis vectors outside \(X_0\).

## Proof

*1.* As \(a<b\), \(f_a=e_a\) is not the last frame vector. Let \(u'=h_c^{-1}uh_c\in K(M)\), written in the lattice basis. By the description of the principal level as the integral [[?c:Isometry of a hermitian space|isometries]] congruent to \(1\) modulo \(M\) ([[?lean:New.Filling.principalLevel_eq_unitaryLevel|description of the principal level]]), \(M^{-1}(u'-1)\) has entries in \(\widehat{\mathcal O}\). The frame belongs to the class basis and the entry of \(u'\) at \((e_a,f_b)\) is the image of \(\Theta(u)_{ab}\) in the finite adeles ([[?lean:New.Filling.frameImage_translateByClassReps|frame columns in the class basis]]). Since \(e_a\ne f_b\), \(M^{-1}\Theta(u)_{ab}\) is an element of \(E\) lying in \(\widehat{\mathcal O}\), that is, an element of \(\mathcal O_E\).

*3.* The frame vector \(f_b\) belongs to the class basis, and its coordinate function \(\lambda\) (row \(f_b\) of the inverse of the class basis) is a finite-adelic form with \(\lambda(\text{class basis})\) a standard basis vector, hence integral; in rational coordinates \(\lambda\) equals \(1\) at \(f_b\), \(0\) at the other basis vectors outside \(X_0\), and has some adelic values \(w_0\) on the basis of \(X_0\). The set of tuples \(w\) of finite adeles such that the form "\(1\) at \(f_b\), \(w\) on \(X_0\), \(0\) elsewhere" is integral on \(\Lambda_c\) is open and contains \(w_0\). Since \(E\) is dense in the [[catalog/arithmetic/adeles-number-field-finite|finite adeles]] ([[?c:Strong approximation for the additive group|strong approximation]]), it contains a tuple with entries in \(E\), which gives \(l\).

*2.* Here \(a\) is one of \(1,\dots,\varrho\). Take \(l\) from 3 for \(f_b\). The form \(x\,l\) is integral on \(\Lambda_c\) and vanishes at \(e_{b'}\) and \(e^{*}_{b'}\) for \(b'\le a\): these are outside \(X_0\) and different from \(f_b\) (which is \(e_b\) with \(b>a\), or \(z\)). By the lemma on [[proofs/grh/spanning-unfolding-a/eichler-element-with-prescribed-row|a prescribed row]] (with \(s=0\)) there is \(u\in\mathsf U_c(M)\) whose rows at the \(e_i\), outside the column \(e_a^{*}\), are \(\delta+M[i=a]\,x\,l\). No frame vector is \(e_a^{*}\), so \(\Theta(u)_{ij}=\delta_{ij}+Mx\,[i=a]\,l(f_j)=\delta_{ij}+Mx[i=a][j=b]\) for \(i\le\varrho\); the last row of \(\Theta(u)\) is that of the identity by unitriangularity.

## References

1. Lean: `New.Filling.exists_frameMatrix_classUnipotent_eq_mul` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
2. Lean: `New.Filling.exists_classUnipotent_frameMatrix_eq` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
3. Lean: `New.Filling.exists_integral_form_besselFrame` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
