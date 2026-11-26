+++
id = "proofs/grh/upper-seesaw/finite-zero-term"
title = "The finite part of the zero term"
kind = "construction"
summary = "The finite part of the constant term of the Weil representation along a splitting, with its parabolic law, its action on translates and its nonvanishing at the vacuum."
aliases = ["finite zero term", "zeroTermFin"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.zeroTermFin", "New.Seesaw.zeroTermFin_eq", "New.Seesaw.exists_zeroTermFin_ne_zero", "New.Seesaw.zeroTermFin_omega", "New.Seesaw.zeroTermFin_mem_finitePart", "New.Seesaw.exists_zeroTerm_rho_integrated_eq", "New.Seesaw.zeroTermFin_finHeisenbergOp_finFrameVector", "New.Seesaw.exists_sub_orthogonal_of_zeroTermFin_ne_zero", "New.Seesaw.exists_eq_add_of_zeroTermFin_ne_zero", "New.Seesaw.exists_zeroTermFin_finHeisenbergOp_add", "New.Seesaw.zeroTermFin_vacElem_ne_zero"]
lean_files = ["src/New/UpperBound/Seesaw/EdgePairEvaluation.lean"]
proof_status = "outline"
+++

Let \(E\) be a [[?c:CM field|CM field]] with [[?lean:New.WeilData|Weil data]], and let \(D\) be a
[[?lean:New.Space.Splitting|splitting]] of a [[?lean:New.Space|hermitian space with a point]] \(V\)
over \(V_0\): dual [[?c:Isotropic subspace|isotropic]] frames \(k,l\) with columns indexed by a finite set \(p\), and an
isometry \(i\colon V_0\to V\) onto their orthogonal complement. Let
\(Z_D\colon\mathcal{S}(V)\to\mathcal{S}(V_0)\) be the [[?lean:New.Space.Splitting.zeroTerm|zero term]]
along \(k\) (the constant term in the [[?c:Mixed model of the Weil representation|mixed model]]:
\(Z_Df(y)\) is the mean of \(f(iy+kb)\) over \(b\in\mathbb{A}^{p}/E^{p}\)).

Choose an adelic point \(g\) of the unitary group of \(V\) *adapted* to \(D\) (the frame of \(D\)
moved by \(g^{-1}\) is orthonormal at the infinite places and integral at the [[algebra-fields-galois/place-of-global-field|finite places]]). The
**finite part of the zero term** is the continuous linear map
\[
Z_D^{f}\colon\mathcal{S}(V)\to\mathcal{S}(V_0),\qquad
Z_D^{f}(f)=Z_D\Bigl(\omega(g)\,P_{\infty}\,\omega(1,g_f^{-1})f\Bigr),
\]
where \(P_\infty\) is the projection onto the real vacuum and \(g_f\) is the finite part of \(g\).
Equivalently \(Z_D^f(f)=Z_D(v\otimes f)\) with \(v\) the [[?c:Fock model of the Weil representation|Fock vacuum]] moved by the real part of \(g\).

## Properties

Write \(\varrho_f(x)\) for the [[?lean:New.Space.finHeisenbergOp|finite Heisenberg operators]],
\(v_0\) for the vacuum, \(\mathcal{S}_f(V)\) for the span of the \(\varrho_f(x)v_0\) (the
*finite part*), and \(i_f,k_f\) for the finite parts of \(i,k\) in lattice coordinates.

1. (**Finite parts.**) \(Z_D^{f}\) maps \(\mathcal{S}_f(V)\) into \(\mathcal{S}_f(V_0)\).
2. (**Pure tensors.**) For an adelic vector \(y\) and a real Fock vector \(v\) there is a real Fock
   vector \(v_0\), independent of \(f\), with
   \(Z_D\bigl(\varrho(y)(v\otimes f)\bigr)=v_0\otimes Z_D^{f}\bigl(\varrho_f(\alpha^{-1}y_f)f\bigr)\).
3. (**Parabolic law.**) If a finite point \(g\) satisfies \(gk=ka\) with \(\det a=d\) and acts on
   \(V_0\) as \(g_0\), then
   \(Z_D^{f}\circ\omega(1,g)=\chi(d)^{-1}\,\omega(g_0)\circ Z_D^{f}\), where
   \(\chi(d)=\upsilon(d)\lvert d\rvert^{-1/2}\) with \(\upsilon\) the splitting character.
4. (**Translations.**) \(Z_D^{f}\circ\varrho_f(i_fw+k_fb)=\varrho_f(w)\circ Z_D^{f}\) for
   \(w\in\mathbb{A}_f^{n_0}\), \(b\in\mathbb{A}_f^{p}\).
5. (**Support, general form.**) Let \(M,M'\) be finite adelic matrices with \(MM'^{*}=1\), and let \(f\) be fixed by \(\varrho_f(Mx)\) for all \(x\) in the standard lattice. If \(Z_D^{f}(\varrho_f(y)f)\ne0\), then there is \(l\) in the standard lattice with \(k_f^{*}(y-M'l)=0\).
6. (**Support.**) If \(Z_D^{f}(\varrho_f(y)v_0)\ne0\) then \(y=i_fw+k_fb+l\) for some \(w,b\) and
   some \(l\) in the standard lattice \(\widehat{\mathcal{O}}^{n}\); and then
   \(Z_D^{f}(\varrho_f(y)v_0)=\zeta\,\varrho_f(w)\,Z_D^{f}(v_0)\) for a [[?c:Root of unity|root of unity]] \(\zeta\).
7. (**Nonvanishing.**) \(Z_D^{f}(v_0)\ne0\).

## Proof

(Outline: the structure follows the Lean proofs, which were read in full; the statements about the
mixed model named below are taken from the library and not reproduced.)

Let \(g\) be the chosen adapted point.

(1) For an adapted point, the mixed model of \(\omega(g)v_0\) is a multiple of the vacuum
(Lean: `IsAdapted.slice_omega_vacElem`). With \(\omega(g)\varrho_f(x)=\varrho_f(g_fx)\omega(g)\)
and the law of the mixed model for translations, the zero term of \(\omega(g)\varrho_f(x)v_0\) is
a multiple of a translate of the vacuum of \(V_0\). As \(P_\infty\) is the identity on the finite
part, \(Z_D^f=Z_D\circ\omega(g)\circ\omega(1,g_f^{-1})\) there, and \(\omega(1,g_f^{-1})\) preserves
the finite part.

(2) Write \(\varrho(y)(v\otimes f)=w\otimes\varrho_f(\alpha^{-1}y_f)f\) for a Fock vector \(w\)
(Lean: `Space.exists_rho_integrated_eq`), and
\(w\otimes f'=\omega(g)\bigl(\omega_\infty(g_\infty^{-1})w\otimes\omega(1,g_f^{-1})f'\bigr)\). For an
adapted point there is a bounded map \(L\) of Fock spaces with
\(Z_D\,\omega(g)(v'\otimes f')=L(v')\otimes Z_D\,\omega(g)P_\infty f'\) (Lean:
`IsAdapted.exists_map_vacVector_apply_zero_omega_eq`). Take \(v_0=L(\omega_\infty(g_\infty^{-1})w)\).

(3) From the law of the zero term on the parabolic subgroup
([[?lean:New.Space.Splitting.zeroTerm_omega|Lean statement]]), since finite points commute with the
tensor by a Fock vector.

(4) The vector \(z=i_fw+k_fb\) has coordinates \((b,0,w)\) in the frame \((k,l,i)\); the law of the
mixed model gives \(Z_D\varrho(z)=\varrho(w)Z_D\) for such vectors, and the semicharacters of \(z\)
and \(w\) agree because \(z^{*}z=w^{*}w\) (\(k\) is isotropic and orthogonal to \(i\), and \(i\) is
an isometry).

(5) Let \(k=k_f\). Since \(k\) has a left inverse and \(MM'^{*}=1\), the matrix \(M'^{*}k\) has a
left inverse; so there is an invertible \(t\) such that \(M'^{*}kt\) is integral and has an
integral left inverse \(\Lambda\) (a lemma on primitive matrices over the integral adeles; Lean:
`exists_isPrimitiveMatrix_mul`). Put \(v=(kt)^{*}y\). *Claim: \(v\) is integral.* By self-duality of
the standard lattice it suffices that \(\psi(x^{*}v)=1\) for integral \(x\). Let \(z=ktx\). Then
\(z=M(M'^{*}ktx)\) is \(M\) times an integral vector, so \(\varrho_f(z)f=f\); and \(z=k_f(tx)\), so by
(4) (with \(w=0\); its semicharacter is \(1\)) \(Z_D^f\circ\varrho_f(z)=Z_D^f\). By the commutation
law, \(\varrho_f(y)f=\varrho_f(y)\varrho_f(z)f=\psi(z^{*}y)\,\varrho_f(z)\varrho_f(y)f\); applying
\(Z_D^f\) gives \(Z_D^f(\varrho_f(y)f)=\psi(z^{*}y)Z_D^f(\varrho_f(y)f)\), and the vector is nonzero,
so \(\psi(z^{*}y)=\psi(x^{*}v)=1\). Now \(l=\Lambda^{*}v\) is integral and
\((kt)^{*}M'l=(\Lambda M'^{*}kt)^{*}v=v=(kt)^{*}y\); as \(t\) is invertible, \(k^{*}(y-M'l)=0\).

(6) Apply (5) with \(M=M'=1\) and \(f=v_0\): \(k_f^{*}(y-l)=0\) with \(l\) integral. A vector
orthogonal to the columns of \(k_f\) has no component along the dual frame, so
\(y-l=i_fw+k_fb\). For the value: translates of the vacuum by \(x\) and \(x-l\) differ by the root
of unity \(\psi(\bar c_0\,(-l)^{*}x)\) (composition law, and \(\varrho_f(l)v_0=v_0\)); then apply (4).

(7) The vector \(f=\omega(1,g_f)v_0\) lies in the finite part and
\(Z_D^f(f)=Z_D(\omega(g)v_0)\) is a nonzero multiple of the vacuum of \(V_0\) (same library
statement as in (1)). If \(Z_D^f(v_0)=0\), then by (6) \(Z_D^f\) vanishes on every translate of the
vacuum, hence on the finite part; contradiction. \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Seesaw/EdgePairEvaluation.lean`; sources for the mixed model are given in `Lib/Weil/MixedModel/ZeroTerm`.
