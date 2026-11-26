+++
id = "proofs/grh/upper-seesaw/zero-term-lattice"
title = "The lattice of the finite zero term"
kind = "lemma"
summary = "The lattice induced on I-perp/I is the image of the standard lattice under a finite unitary element, is self-dual, and the finite zero term of the vacuum is a nonzero multiple of the sum of the translates of the vacuum over its classes."
aliases = ["zeroTermLattice"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.zeroTermLattice", "New.Seesaw.exists_zeroTermLattice_eq_map", "New.Seesaw.mem_zeroTermLattice_iff", "New.Seesaw.mem_zeroTermLattice_iff_selfDualAddChar", "New.Seesaw.zeroTermLattice_eq_map_of_le", "New.Seesaw.relIndex_zeroTermLattice_ne_zero", "New.Seesaw.finHeisenbergOp_zeroTermFin_vacElem", "New.Seesaw.exists_omega_vacElem_eq_sum", "New.Seesaw.exists_zeroTermFin_vacElem_eq_sum", "New.Seesaw.exists_zeroTermFin_finHeisenbergOp_eq_smul", "New.Seesaw.exists_isIntMatrix_iFin_mul_add_isotropicBasisFin_mul"]
lean_files = ["src/New/UpperBound/Seesaw/EdgePairEvaluation.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-seesaw/finite-zero-term|the finite zero term]] \(Z_D^f\) of a
splitting \(D\) of \(V\) over \(V_0\), with finite frames \(i_f\), \(k_f\); \(L=\widehat{\mathcal{O}}^{n}\)
and \(L^{\circ}=\widehat{\mathcal{O}}^{n_0}\) are the standard lattices of \(V\) and \(V_0\).

**Definition.** The **zero term lattice** is
\[
L'_D=\{\,w\in\mathbb{A}_f^{n_0}\;:\; i_fw+k_fb\in L\ \text{for some } b\in\mathbb{A}_f^{p}\,\},
\]
the image in \(V_0=I^{\perp}/I\) of \(L\cap I^{\perp}\), where \(I\) is the span of the columns of
\(k_f\).

**Lemma.**

1. There are a finite unitary point \(g\) of \(V_0\) and a matrix \(c\) such that
   \(B=i_fg+k_fc\) is integral. For any such pair, \(L'_D=gL^{\circ}\).
2. \(L'_D\) is [[?c:Self-dual lattice|self-dual]] for the self-dual [[?c:Additive character|additive character]] \(\psi\) of the [[?c:Finite adele ring of a number field|finite adeles]]:
   \(w\in L'_D\) iff \(\psi(\bar x\cdot w)=1\) for all \(x\in L'_D\). In particular a lattice
   \(gL^{\circ}\subseteq L'_D\) with \(g\) unitary equals \(L'_D\); and \(L'_D\cap L^{\circ}\) has
   finite index in \(L'_D\).
3. \(\varrho_f(x)Z_D^{f}(v_0)=Z_D^{f}(v_0)\) for \(x\in L'_D\).
4. If \((r_a)_{a\in R}\) is a finite system of representatives of \(L'_D\) modulo
   \(L'_D\cap L^{\circ}\), then \(Z_D^{f}(v_0)=c\sum_{a\in R}\varrho_f(r_a)v_0\) for some
   \(c\ne0\).
5. With \(B=i_fg+k_fc\) integral as in 1, for every \(y\in\mathbb{A}_f^{n}\) there is \(\zeta\),
   zero or a [[?c:Root of unity|root of unity]], with
   \(Z_D^{f}(\varrho_f(y)v_0)=\zeta\,\varrho_f(gB^{*}y)\,Z_D^{f}(v_0)\).

## Proof

(1) Existence: there is a point \(h\) adapted to the splitting with \(h^{-1}\) a radical
element times a Levi element \((a,g)\) ([[?lean:New.Space.Splitting.exists_eq_radicalElement_mul_levi_mul_isAdapted|Iwasawa decomposition for the splitting]]); then \(h^{-1}i=ig+kc'\) for a matrix \(c'\), and the finite part of \(h^{-1}i\) is a block of the adapted frame, hence integral. Equality: for integral \(x\),
\(Bx\in L\) has class \(gx\), so \(gL^{\circ}\subseteq L'_D\). Conversely \(B^{*}\) is integral and
sends \(i_fw+k_fb\) to \(g^{-1}w\) (as \(k\) is [[?c:Isotropic subspace|isotropic]] and orthogonal to \(i\), and \(i\), \(g\)
are isometries), so \(w\in L'_D\) implies \(g^{-1}w\in L^{\circ}\).

(2) \(L^{\circ}\) is self-dual and \(g\) preserves the hermitian pairing. Two self-dual lattices one
inside the other are equal. The index \([gL^{\circ}:gL^{\circ}\cap L^{\circ}]\) is
\(\lvert\Delta_f(g)\rvert^{2}\ne0\).

(3) By property 4 of the [[proofs/grh/upper-seesaw/finite-zero-term|finite zero term]], for \(x\in L'_D\) with \(i_fx+k_fb\in L\):
\(\varrho_f(x)Z^f_D(v_0)=Z_D^f(\varrho_f(i_fx+k_fb)v_0)=Z_D^f(v_0)\), since lattice translations fix
the vacuum.

(4) A vector of \(\mathcal{S}_f(V_0)\) fixed by the translations by \(gL^{\circ}\) is a multiple of
\(\omega(1,g)v_0\) ([[?lean:New.Space.exists_eq_smul_omega_vacElem|uniqueness of the vector of the finite part fixed by a moved lattice]]); the multiple is
nonzero because \(Z_D^f(v_0)\ne0\). And \(\omega(1,g)v_0\) is a nonzero multiple
(\(\Delta_f(g)/\lvert\Delta_f(g)\rvert^{2}\)) of the sum of the translates of \(v_0\) over
representatives of \(gL^{\circ}\) modulo \(gL^{\circ}\cap L^{\circ}\) ([[?lean:New.Space.omega_vacElem_sum|the moved vacuum]]; the given representatives \(r_a=g\,x_a\) correspond bijectively to the classes of \(L^{\circ}\) modulo \(L^{\circ}\cap g^{-1}L^{\circ}\)).

(5) If the left side is \(0\) take \(\zeta=0\). Otherwise \(y=i_fw+k_fb+l\) with \(l\in L\) and the
left side is a root of unity times \(\varrho_f(w)Z_D^f(v_0)\). Now \(gB^{*}y=w+x\) with
\(x=gB^{*}l\in gL^{\circ}=L'_D\), and by (3) \(\varrho_f(w+x)Z_D^f(v_0)\) is a root of unity times
\(\varrho_f(w)Z_D^f(v_0)\). \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Seesaw/EdgePairEvaluation.lean`.
