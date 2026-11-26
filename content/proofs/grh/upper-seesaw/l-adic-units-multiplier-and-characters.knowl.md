+++
id = "proofs/grh/upper-seesaw/l-adic-units-multiplier-and-characters"
title = "The finite multiplier and character values are l-adic units at integral points"
kind = "lemma"
summary = "For a finite adelic unitary element integral above l, the Weil multiplier and the value of an algebraic character at its determinant have l-adic norm one."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_finMultiplier_eq_one", "New.AutChar.HasWeight.norm_apply_detFin_eq_one", "New.Seesaw.localLevel_le_integralAbove_of_coprime"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a [[?c:CM field|CM field]] with [[?lean:New.WeilData|Weil data]], \(l\) a
prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_l\) a ring homomorphism, and \(g\) an element of the
[[?lean:New.Gf|finite adelic unitary group]] \(G_f\) (matrices indexed by a finite set \(n\)) that
is *integral above \(l\)*: at every [[algebra-fields-galois/place-of-global-field|finite place]] \(w\mid l\) the component \(g_w\) lies in
\(\mathrm{GL}_n(\mathcal{O}_w)\).

1. The [[?lean:New.finMultiplier|finite multiplier]]
   \(\Delta_f(g)=\upsilon(\det u)\,\lvert\det u\rvert^{-1/2}\), where \(\upsilon\) is the splitting
   character of the Weil data and \(u\) a chosen invertible [[?c:Finite adele ring of a number field|finite adelic]] matrix with
   \(u\,\widehat{\mathcal{O}}^{n}=\widehat{\mathcal{O}}^{n}\cap g^{-1}\widehat{\mathcal{O}}^{n}\),
   satisfies \(\lVert\iota(\Delta_f(g))\rVert=1\).
2. Let \(\mu\) be an [[?lean:New.AutChar|automorphic character]] of the norm-one adeles that
   [[?lean:New.AutChar.HasWeight|has a weight \(e\) and a tame part \(\psi\)]]. Then
   \(\lVert\iota(\mu(\det(1,g)))\rVert=1\), where \(\det(1,g)\) is the determinant of the adelic
   point with trivial infinite part and finite part \(g\).
3. If \(l\) is coprime to \(q\), every \(g\in G_f\) integral at all places not dividing \(q\) is
   integral above \(l\).

## Proof

(3) A place above \(l\) does not divide \(q\), since \(l\) and \(q\) are coprime.

(1) By definition \(\Delta_f(g)\) is the value at \(\det u\) of the character
\(\upsilon\lvert\cdot\rvert^{-1/2}\) of the finite ideles, which is an algebraic Hecke character
(with exponents \(0\) on the CM type and \(-1\) on its conjugate). The value of an algebraic Hecke
character at a finite idele that is a unit at all primes above \(l\) has \(\iota\)-norm \(1\)
([[?lean:New.AlgHeckeChar.norm_padic_eq_one|values of algebraic Hecke characters at \(l\)-units]]).
So it suffices that \(\det u\) is a unit at each \(w\mid l\). There \(g_w\) is integral, so the
identity matrix also satisfies the saturation condition
\(1\cdot\mathcal{O}_w^{n}=\mathcal{O}_w^{n}\cap g_w^{-1}\mathcal{O}_w^{n}\); and the determinant of
the chosen saturating matrix has, at \(w\), the valuation of the determinant of any matrix
saturating at \(w\) ([[?lean:New.IsSaturating.v_det_saturatingElem|determinant of the saturating
matrix]]), here \(\det1=1\).

(2) For a character \(\mu\) with weight \(e\) and tame part \(\psi\), and \(u\) in the norm-one
adeles with trivial archimedean part,
\[
\lVert\iota(\mu(u))\rVert=\prod_{\tau}\lVert u_{\tau,\iota}\rVert^{-e(\tau)},
\]
the product over the infinite places \(\tau\), where \(u_{\tau,\iota}\in\mathbb{C}_l\) is the image
of the finite part of \(u\) at the prime above \(l\) induced by \(\iota\circ\Phi_\tau\)
([[?lean:New.AutChar.HasWeight.norm_padic_eq_prod|\(l\)-adic norm of a character value]]). For
\(u=\det(1,g)\), the finite part is \(\det g\), a unit at every prime above \(l\) because \(g\) is
integral with integral inverse there; so every factor is \(1\). \(\blacksquare\)

## References

1. Lean: `New.Parameters.norm_finMultiplier_eq_one`, `New.AutChar.HasWeight.norm_apply_detFin_eq_one`, `New.Seesaw.localLevel_le_integralAbove_of_coprime` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
