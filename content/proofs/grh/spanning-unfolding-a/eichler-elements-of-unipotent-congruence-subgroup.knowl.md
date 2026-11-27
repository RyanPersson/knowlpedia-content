+++
id = "proofs/grh/spanning-unfolding-a/eichler-elements-of-unipotent-congruence-subgroup"
title = "Eichler elements of the unipotent congruence subgroups"
kind = "lemma"
summary = "Eichler's formula along isotropic basis vectors e_a gives explicit elements of the rational unipotent group of level M at a class c, which fix the frame when u is orthogonal to it."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_mem_classUnipotent_eq_one_add_smul", "New.Filling.eichler_apply_eq_zero_of_level_le", "New.Filling.isIntMatrix_ideleM_inv_smul_eichler"]
lean_files = ["src/New/Spanning/Unfolding/ReducedPoints.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity ([[?lean:New.HasPrimitiveRoot5040|stably unramified]]), and let \(S\) be [[?lean:New.Filling|filling data]] over \(E\), with level \(M=p_0p_1\). The [[?c:Hermitian form|hermitian space]] is \(V=\bigoplus_{a=1}^{\varrho}(Ee_a\oplus Ee_a^{*})\oplus X_0\oplus Ez\) with [[?c:Gram matrix|Gram matrix]] \(J\) ([[?lean:New.Filling.ratGram|rational Gram matrix]]): \(h(e_a,e_a^{*})=1\), \(X_0\) has the standard form, \(h(z,z)=-N\), and all other products of basis vectors vanish. Let \(c\) be a [[?lean:New.Filling.Classes|class]], \(\Lambda_c\) the lattice of the class (the \(\widehat{\mathcal O}\)-span of the columns of the [[?lean:New.Filling.classBasis|class basis]]), and \(\mathsf U_c(M)\) the [[?lean:New.Filling.classUnipotent|group of rational unipotent elements of level \(M\) at \(c\)]], with its subgroup \(\mathsf U^{0}_c(M)\) [[?lean:New.Filling.classUnipotent₀|fixing the frame]] \((e_1,\dots,e_\varrho,z)\).

Let \(m\) be a finite index set, \(p:m\to\{1,\dots,\varrho\}\) a map, and \(x\) the matrix whose \(b\)-th column is \(e_{p(b)}\). Let \(u\) be a matrix over \(E\) with columns indexed by \(m\) and \(s\) an \(m\times m\) matrix over \(E\), such that

1. for all \(b,b'\in m\) and every \(a\le p(b')\), the coordinate of the column \(u_b\) at \(e_a^{*}\) is \(0\);
2. \(s^{*}=-s\) and the entries of \(s\) are integral at all finite places;
3. the columns of \(u\) lie in \(\Lambda_c\) (their coordinates in the class basis are in \(\widehat{\mathcal O}\)).

Then there are \(\tau\in E\) and \(\gamma\in\mathsf U_c(M)\) with matrix
\[
\gamma=1+M\Bigl(x\,u^{*}J-\bigl(u+x(\tau\,u^{*}Ju-s)\bigr)x^{*}J\Bigr),
\]
and \(\gamma\in\mathsf U^{0}_c(M)\) whenever every column of \(u\) is orthogonal to every vector of the frame.

## Proof

*Choice of \(\tau\).* Since \(E\) contains a primitive 5040-th root of unity, \(\mathcal O_E\) contains \(\tau_0\) with \(\tau_0+\bar\tau_0=1\) ([[?lean:New.HasPrimitiveRoot5040.exists_mul_self_eq_neg_one_and_mul_star_eq_two|an integer of trace one]]). Put \(\tau=M\tau_0\), so \(\tau+\bar\tau=M\).

*[[?c:Isometry of a hermitian space|Isometry]].* The columns \(e_{p(b)}\) of \(x\) are isotropic and mutually orthogonal, so \(x^{*}Jx=0\); and \(h(e_{p(b)},u_{b'})\) is the conjugate of the coordinate of \(u_{b'}\) at \(e^{*}_{p(b)}\), which is \(0\) by hypothesis 1, so \(x^{*}Ju=0\). By [[proofs/grh/spanning-unfolding-a/eichler-map-is-isometry|Eichler's formula]] with \(g=M\), the matrix \(\gamma=1+MA\), \(A=xu^{*}J-(u+xW)x^{*}J\), \(W=\tau u^{*}Ju-s\), preserves \(J\); thus \(\gamma\) is a rational isometry.

*Unitriangularity.* Give \(e_a\) the level \(a\), the vectors of \(X_0\oplus Ez\) the level \(\varrho\), and \(e_a^{*}\) the level \(2\varrho-a\); the [[?lean:New.Shape.Form.besselU|unipotent group \(\mathsf U\)]] consists of the isometries \(\gamma\) with \(\gamma_{ij}=\delta_{ij}\) whenever \(\operatorname{level}(j)\le\operatorname{level}(i)\). We check \(A_{ij}=0\) for such \(i,j\). The matrix \(x\,u^{*}J\) has nonzero rows only at \(i=e_{p(b)}\), where its entry in column \(j\) is \((u^{*}J)_{bj}\); for \(j=e_a\) this is the conjugate of the coordinate of \(u_b\) at \(e_a^{*}\), which vanishes when \(a\le p(b)\), and the remaining columns have level \(>p(b)\). The matrix \(x^{*}J\) has in row \(b\) the single nonzero entry \(1\) in column \(e^{*}_{p(b)}\), of level \(2\varrho-p(b)\); a row index \(i\) of level at least that is \(e_a^{*}\) with \(a\le p(b)\), and the entry of \(u+xW\) in row \(e_a^{*}\) is that of \(u\) (the rows of \(x\) at \(e^{*}\) vanish), which is \(0\) by hypothesis 1. Hence \(\gamma\in\mathsf U\).

*Level.* Let \(C\) be the inverse of the class basis ([[?lean:New.Filling.classCoord|coordinates in the class lattice]]) and \(J'\) the Gram matrix in the lattice basis; \(J'\) is integral and unimodular over \(\widehat{\mathcal O}\) ([[?lean:New.Filling.isUnimodular_latticeMiddle|unimodularity of the lattice form]]), and the class basis carries \(J\) to \(J'\) ([[?lean:New.Filling.classCoord_conj_splitGram|change of basis of the Gram matrix]]). Write \(\gamma'=h_c^{-1}\gamma h_c\) in the lattice basis, \(X=Cx\), \(U=Cu\). Then
\[
M^{-1}(\gamma'-1)=\bigl(XU^{*}-(U+X(\tau\,U^{*}J'U-s))X^{*}\bigr)J' .
\]
Here \(U\) is integral by hypothesis 3, \(X\) is integral because the \(e_a\) belong to the class basis (block form of \(C\)), \(s\) and \(\tau=M\tau_0\) are integral, and \(J'\) is integral; so \(M^{-1}(\gamma'-1)\) has entries in \(\widehat{\mathcal O}\). For a unimodular form, an isometry \(k\) with \(M^{-1}(k-1)\) integral lies in the level subgroup of integral isometries congruent to \(1\) modulo \(M\) ([[?lean:New.IsUnimodular.mem_unitaryLevel|membership in the unitary level]]), and this subgroup is the [[?c:Principal congruence subgroup|principal congruence subgroup]] \(K(M)\) ([[?lean:New.Filling.principalLevel_eq_unitaryLevel|description of the principal level]]). Hence \(\gamma\in\mathsf U_c(M)\).

*The frame.* If \(u^{*}Jf=0\) for every frame vector \(f\), then, as also \(x^{*}Jf=0\) (each \(e_{p(b)}\) is orthogonal to \(e_1,\dots,e_\varrho\) and \(z\)), \(Af=x(u^{*}Jf)-(u+xW)(x^{*}Jf)=0\). So \(\gamma f=f\) and \(\gamma\in\mathsf U^{0}_c(M)\).

## References

1. Lean: `New.Filling.exists_mem_classUnipotent_eq_one_add_smul`, with `New.Filling.eichler_apply_eq_zero_of_level_le` and `New.Filling.isIntMatrix_ideleM_inv_smul_eichler`, in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
