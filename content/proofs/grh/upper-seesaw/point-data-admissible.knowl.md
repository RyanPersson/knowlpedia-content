+++
id = "proofs/grh/upper-seesaw/point-data-admissible"
title = "Translated point data are admissible combinations of translates of the vacuum"
kind = "lemma"
summary = "The point data of the chain, moved by finite points integral away from the norm q of the chosen modulus, and their joins, are admissible combinations of translates of the vacuum with denominators bounded by powers of the norm of pi_M."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.mulVec_mem_translations", "New.Seesaw.mem_translations_of_mem_stdLattice", "New.Seesaw.isAdmissibleCombination_weil_of_mem_localLevel", "New.Seesaw.exists_arrowProduct_eq_smul_finHeisenbergOp", "New.Data.piM_mul_normQ_mem_ideal", "New.Data.isAdmissibleCombination_pointDatumY", "New.Data.isAdmissibleCombination_translatedPointDatumY", "New.Data.isAdmissibleCombination_arrowProduct_translatedPointDatumY"]
lean_files = ["src/New/UpperBound/Seesaw/GoodDatum.lean"]
proof_status = "full"
+++

Let \(D\) be the [[?lean:New.Data|data]], \(\vartheta\) a tame character with chosen modulus \(Q\) (a finite set of places outside which its tame part is trivial; the tame part may also be trivial at places of \(Q\), and \(Q\) is the exact support only for a [[?lean:New.Data.Twist|twist]]), and \(q=\mathrm{N}Q\) the product of the norms of the places of \(Q\)
([[?lean:New.Data.TameChar.normQ|Lean: the norm of \(Q\)]]). Let \(\beta=\pi_M\) and
\(\mathrm{N}\beta=\mathrm{N}((\pi_M))\). Let \(\Phi_k\) be the
[[?lean:New.Data.pointDatumY|point datum]] on \(H_k=\operatorname{Hom}(Y_k,Y_{k+1})\): the indicator
of the inclusion matrix modulo the modulus \(\mathfrak{m}\) of the twist (chosen places times
\(Q\)), and the vacuum at the other [[algebra-fields-galois/place-of-global-field|finite places]]. "Admissible" refers to
[[proofs/grh/upper-seesaw/admissible-combination|admissible combinations]] away from \(q\), with
the proposition \(p\) = "\(Q=\emptyset\)" unless stated.

**Lemma.**

1. Let \(V\) be a [[?c:Hermitian space|hermitian space]], \(g\in G_f(V)\) integral at all places not dividing \(q\),
   \(d\) an integral adele and \(x\in T_q(d)\)
   ([[proofs/grh/upper-seesaw/translation-groups|translations]]). Then
   \(\omega(1,g)\varrho_f(x)v_0\) is an admissible combination of the \(\varrho_f(y)v_0\),
   \(y\in T_q(d)\), with denominator \(1\) and size \(1\) under any \(p\) that implies \(q=1\).
2. \(\Phi_k\) is an admissible combination of the \(\varrho_f(x)v_0\),
   \(x\in T_q(\bar\beta)\), with denominator \((\mathrm{N}\beta)^{\dim H_k}\) and size \(1\) under
   every proposition.
3. If all \(y_k\) are integral away from \(q\), the
   [[proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data|translated point datum]]
   \(\Phi^{y}_k\) is an admissible combination of the same family with the same denominator, and
   size \(1\) if \(Q=\emptyset\).
4. Under the same hypothesis, the join \(\Phi^{y}_k\ast\Phi^{y}_{k+1}\) on
   \(\operatorname{Hom}(Y_{k+1},Y_k^{-}\oplus Y_{k+2})\) is an admissible combination of the
   translates \(\varrho_f(z)v_0\) with \(z\) in the weighted translations (rows of \(Y_k\) weighted
   by \(\beta\), rows of \(Y_{k+2}\) by \(\bar\beta\)), with denominator
   \((\mathrm{N}\beta)^{\dim H_k}(\mathrm{N}\beta)^{\dim H_{k+1}}\) and size \(1\) if
   \(Q=\emptyset\).

## Proof

(1) By [[proofs/grh/upper-seesaw/moved-vacuum-admissible|moved vacua]] with
\(C=1\), \(c=\Delta_f(g)\): the coefficients are [[?c:Root of unity|roots of unity]] times
\(\Delta_f(g)/\lvert\Delta_f(g)\rvert^{2}\) (equivalently \(\Delta_f(g^{-1})^{-1}\)), which is a
unit at every prime \(l\nmid q\) by
[[proofs/grh/upper-seesaw/l-adic-units-multiplier-and-characters|the \(l\)-adic unit lemma]]; \(g\)
preserves \(T_q(d)\), which contains the lattice. If \(q=1\), \(g\) is integral everywhere and its
multiplier is \(1\).

(2) \(\Phi_k\) is the Schrödinger operator of the indicator \(\Psi\) of one residue class, applied
to the vacuum, and \(P^{\mathfrak m}v_0=v_0\). Since \(\mathfrak{m}\mid\pi_M\cdot q\), apply
[[proofs/grh/upper-seesaw/schrodinger-operator-admissible|the Schrödinger operator lemma]] with
\(g=d=\pi_M\); \(\sum\lvert\sigma\Psi\rvert=1\).

(3) By definition \(\Phi_k^{y}=c\cdot\omega(1,g)\Phi_k\), where \(g\) is the finite part of the
image of \((y_k,y_{k+1})\) in the unitary group of \(H_k\) (acting by \(x\mapsto y_{k+1}xy_k^{-1}\)),
integral away from \(q\), and \(c=\mu(\det y_{k+1})\,\mu'(\det y_k)^{-1}\) for the rank twists
\(\mu,\mu'\) of the character of lift \(k+1\). These characters have a weight, so by
[[proofs/grh/upper-seesaw/l-adic-units-multiplier-and-characters|the \(l\)-adic unit lemma]] \(c\)
is a unit at every prime \(l\nmid q\); and every conjugate \(\sigma c\) has absolute value \(1\)
([[?lean:New.AutChar.HasWeight.norm_map_eq_one|values of characters with a weight]]). Expand
\(\Phi_k\) by (2), move each translate by (1) (with \(d=\bar\pi_M\) and the proposition
\(Q=\emptyset\), which implies \(q=1\)),
[[proofs/grh/upper-seesaw/admissible-combination-substitution|substitute]], and multiply by \(c\)
(rule 4 of the calculus).

(4) The join is bilinear, and the join of two translated vacua is a root of unity times a
translated vacuum \(\varrho_f(z)v_0\) whose first block is \(-\eta\,t_1^{*}\) and whose second block
is \(t_2\): by the [[?lean:New.Seesaw.finHeisenbergOp_arrowProduct|translation formula for a join]], \(\varrho_f(z)v_0\) is a squared semicharacter times the join of \(\varrho_f(\eta\overline{(-\eta t_1^{*})}{}^{\mathsf T})v_0=\varrho_f(t_1)v_0\) (as \(-\eta\bar\eta=1\)) and \(\varrho_f(t_2)v_0\); and \(z\) has the stated weights because conjugation exchanges \(\beta\) and \(\bar\beta\). Apply the
[[proofs/grh/upper-seesaw/admissible-combination-calculus|rule for bilinear maps]]. \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Seesaw/GoodDatum.lean`.
