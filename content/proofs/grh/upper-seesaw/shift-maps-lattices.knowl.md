+++
id = "proofs/grh/upper-seesaw/shift-maps-lattices"
title = "A nonzero constant term at the shift forces a lattice inclusion"
kind = "theorem"
summary = "If the constant term at the shift of a translated datum does not vanish at (x, x'), then a multiple of the shift maps Lambda-plus of x into Lambda-minus of x' at graded points of the Bessel orbits."
aliases = ["frequency lemma"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Grading.IsGraded.mulVec_mem_of_homogeneous", "New.Grading.stringMap_eq_zero_of_gradeOf_ne", "New.Grading.hasDegreeGe_zero_ratCoordMatrixFin", "New.Grading.hasDegreeGe_zero_mul_mul_sub", "New.Grading.zeroTermFin_finHeisenbergOp_stringMap_ne_zero", "New.Grading.exists_mapsTo_lattice_hasDegreeGe_sub_smul_stringMap", "New.Grading.smul_map_stringMapFin_latticePlus_le", "New.Space.Splitting.conjTranspose_isotropicBasisFin", "New.Grading.xFin_mulVec_finCoord_homAtPoint_sub"]
lean_files = ["src/New/UpperBound/Seesaw/Frequency.lean"]
proof_status = "full"
+++

Let \(V,V'\) be [[?lean:New.Space|hermitian spaces with points]] over a [[?c:CM field|CM field]]
\(E\) with [[?lean:New.WeilData|Weil data]] ([[?c:Idele group|finite idele]] \(\alpha\)), with
[[?lean:New.Grading|gradings]] \(Y,Y'\) having strings of \(s\) and \(s-1\) vectors, and let
\(\operatorname{sh}\colon V\to V'\) be the [[?lean:New.Grading.stringMap|shift]], homogeneous of
degree \(-1\) for the grades. For a vector \(F\) of the [[?c:Weil representation|Weil representation]] of
\(\operatorname{Hom}(V,V')\), characters \(\mu\) and adelic points \((x,x')\) of
\(U(V)\times U(V')\), let \(c_{\operatorname{sh}}(F;x,x')\) be the
[[?lean:New.Grading.constTermAtStringMap|constant term at the shift]] of the twisted Weil
translate of \(F\) by \((x,x')\): the mean of its theta function, translated by
\(\operatorname{sh}\), over the adelic maps \(V\to V'\) that raise grades, modulo rational ones.

**Theorem.** Let \(t\) be a real [[?c:Fock model of the Weil representation|Fock vector]] and \(f\in\mathcal{S}(\operatorname{Hom}(V,V'))\)
such that \(c_{\operatorname{sh}}(t\otimes f;x,x')\ne0\), and let \(b\) be a finite idele such that
\(f\) is fixed by the finite Heisenberg operators of
\(b\,\widehat{\mathcal{O}}^{\iota'\times\iota}\).

1. There is a [[?c:Finite adele ring of a number field|finite adelic]] matrix \(W\) mapping the lattice \(\Lambda_{x_f}\) of \(V\) into the
   lattice \(\Lambda'_{x'_f}\) of \(V'\) such that
   \(W-(\bar b/\alpha)\operatorname{sh}_f\) does not lower grades (its entry \((p,q)\) vanishes
   when \(\operatorname{gr}'(p)<\operatorname{gr}(q)\)).
2. Let \(r,r'\) be finite points of the [[?lean:New.Grading.besselFin|Bessel subgroups]] such that
   the lattices of \(rx_f\) and \(r'x'_f\) are graded. Then
   \[
   (\bar b/\alpha)\cdot\operatorname{sh}\bigl(\Lambda^{+}_{rx_f}\bigr)\subseteq\Lambda'^{-}_{r'x'_f}.
   \]

## Proof

(1) There is a splitting \(\mathcal{D}\) of \(\operatorname{Hom}(V,V')\) whose isotropic frame \(k\) consists of the matrix entries of positive degree, with \(J^{-1}kk^{*}J\) the projection onto the entries of negative degree, such that the constant term at \(w\) is the theta value of the zero term of the translate by \(w\) ([[?lean:New.Grading.exists_splitting_constTerm|Lean statement]]). Each
operation acts separately on the real and finite factors of \(t\otimes f\) (property 2 of the
[[proofs/grh/upper-seesaw/finite-zero-term|finite zero term]]), so the nonvanishing gives
\[
Z^{f}_{\mathcal{D}}\bigl(\varrho_f(z)\,\omega(1,g)f\bigr)\ne0,
\]
with \(z\) the finite coordinates of \(\operatorname{sh}\) and \(g\) the finite part of \((x,x')\)
acting on \(\operatorname{Hom}(V,V')\). The vector \(\omega(1,g)f\) is fixed by the translations by
\(b\,g\widehat{\mathcal{O}}\). By property 5 of the finite zero term (with
\(M=bg\), \(M'=\bar b^{-1}g\), \(MM'^{*}=1\)), there is an integral \(l\) with
\(z-\bar b^{-1}gl\) orthogonal to the isotropic frame. Read \(l\) as an \(\iota'\times\iota\) matrix \([l]\) and put
\(W=(B'p')\,[l]\,(Bp)^{-1}\), where \(B,B'\) are the fixed finite frames of \(V,V'\) (they need not be unitary) and
\(p=x_f\), \(p'=x'_f\) the finite parts of the variable points. Then \(W\) maps
\(\Lambda_{p}=Bp\,\widehat{\mathcal{O}}^{\iota}\) into \(\Lambda'_{p'}\), because \([l]\) is
integral. In rational coordinates the vector \(z-\bar b^{-1}gl\) is the matrix
\(\alpha^{-1}\operatorname{sh}_f-\bar b^{-1}W\) (the finite coordinates of a map \(M\) are
\(\alpha^{-1}\) times its matrix in the frames, and \(g\) acts by \(m\mapsto p'mp^{-1}\)).
Orthogonality to the isotropic frame, after applying \(J^{-1}k\), says that the projection of this
matrix onto the entries of negative degree vanishes: for \(\operatorname{gr}'(p)<\operatorname{gr}(q)\),
\(\alpha^{-1}(\operatorname{sh}_f)_{pq}=\bar b^{-1}W_{pq}\), i.e.
\(\bigl(W-(\bar b/\alpha)\operatorname{sh}_f\bigr)_{pq}=0\).

(2) Put \(c=\bar b/\alpha\) and \(W_0=r'Wr^{-1}\) in rational coordinates; it maps
\(\Lambda_{rx_f}\) into \(\Lambda'_{r'x'_f}\). Elements of the Bessel groups do not lower grades and
fix \(\operatorname{sh}\) modulo matrices that do not lower grades; since degrees add under
products, \(W_0-c\operatorname{sh}_f\) does not lower grades. As \(\operatorname{sh}\) is
homogeneous of degree \(-1\), \(c\operatorname{sh}_f\) is the homogeneous part of degree \(-1\) of
\(W_0\). A homogeneous part of a map between graded lattices maps the first into the second (write
it as the sum over grades \(d\) of projections composed with \(W_0\)). Hence
\(c\operatorname{sh}(y)\in\Lambda'_{r'x'_f}\) for \(y\in\Lambda_{rx_f}\). Finally
\(\operatorname{sh}\) kills \(X\), so \(\operatorname{sh}(\operatorname{pr}y)=\operatorname{sh}(y)\),
and its image lies in the span of the string of \(V'\). \(\blacksquare\)

## References

1. Lean: `New.Grading.exists_mapsTo_lattice_hasDegreeGe_sub_smul_stringMap`, `New.Grading.smul_map_stringMapFin_latticePlus_le` and the auxiliary lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/Frequency.lean`.
