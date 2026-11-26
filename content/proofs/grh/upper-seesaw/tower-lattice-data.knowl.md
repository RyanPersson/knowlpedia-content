+++
id = "proofs/grh/upper-seesaw/tower-lattice-data"
title = "The lattices of the tower Y_k are glued lattices"
kind = "lemma"
summary = "The chosen ideles have the expected valuations, the constant of the gradings of Y_k has the valuations of a a-bar, and the frame of Y_k spans the glued lattice."
aliases = ["valuations of the chosen ideles"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.absNorm_piM", "New.Data.v_chosenIdele", "New.Data.v_alpha_mul_star_eq_ideleA_norm_mul_M", "New.Data.v_gradingY_genericConst_eq_ideleA_mul_star", "New.Data.spansLattice_gradingY", "New.Data.chosenLevel_inf_trivialOn_le"]
lean_files = ["src/New/UpperBound/Seesaw/LevelIdeles.lean"]
proof_status = "full"
+++

Let \(D\) be the [[?lean:New.Data|data]], \(E\) its field with \(f\) infinite places,
\(M=p_0p_1\), and \(\pi_M\in\mathcal{O}_E\) the [[?lean:New.Data.piM|chosen integer]] with
\(\pi_M\bar\pi_M=M\) (an integer of \(K\) viewed in \(E\)). Let
\(\varpi\) be the [[?lean:New.Data.chosenIdele|chosen idele]], which generates the ideal
\((\pi_M)\) and is \(1\) away from the chosen places, let \(\alpha\) be the [[?c:Idele group|finite idele]] of the
Weil data, and \(a=\alpha/\bar\varpi\) the [[?lean:New.Data.ideleA|idele \(a\)]]. Let
\(\pi=\pi_N\) be the principal idele of the integer \(\pi_N\) with \(\pi_N\bar\pi_N=N\).

**Lemma.**

1. \(\mathrm{N}\bigl((\pi_M)\bigr)=M^{f}\).
2. \(\varpi\) has the valuation of \(\pi_M\) at every [[algebra-fields-galois/place-of-global-field|finite place]].
3. \(\alpha\bar\alpha\) has the valuation of \(a\bar a\,M\) at every finite place.
4. For \(k\le m-1\), the constant \(c=-(jM\delta_E)^{-1}\) of the
   [[proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data|grading of \(Y_k\)]] has the
   valuation of \(a\bar a\) at every finite place.
5. For \(k\le m-1\), the grading of \(Y_k\)
   [[proofs/grh/upper-seesaw/graded-lattice-basis|spans the lattice]] of
   \((a,\pi_N,u_k)\), where \(u_k\) is the [[?lean:New.Data.latticeScale|lattice scale]]
   \((a/\bar a)^{\lceil(m-k)/2\rceil}\).
6. For a tame character \(\vartheta\) with ramification set \(Q\): a finite unitary element that
   is integral with reduction \(1\) at the chosen places and has component \(1\) at the places of
   \(Q\) is integral with reduction \(1\) at all [[?lean:New.Data.levelPlaces|level places of
   \(\vartheta\)]] (the chosen places and those of \(Q\)).

## Proof

(2) Both valuations at \(w\) are \(\exp(-\operatorname{ord}_w(\pi_M))\), by the
definition of \(\varpi\). (1) The ideal \((\pi_M)\) is the product of the chosen places ([[?lean:New.Rows.span_piM|Lean statement]]), whose norms multiply to \(M^{f}\). (3) \(\alpha=a\bar\varpi\), so \(\alpha\bar\alpha=a\bar a\,\varpi\bar\varpi\), and
\(\varpi\bar\varpi\) has the valuation of \(\pi_M\bar\pi_M=M\) by (2).

(4) The Weil data satisfy: \(j\alpha\bar\alpha\) has, at each place, the inverse of the valuation
of the [[?c:Different of a number field|different]] ([[?lean:New.Parameters.v_weilData_j_mul_alpha_mul_star|a property of the Weil data]]), which \(\delta_E\) generates. So
\(j\alpha\bar\alpha\delta_E\) is a unit at every \(w\); by (3) so is \(jM\delta_E\cdot a\bar a\),
i.e. \(c=-(jM\delta_E)^{-1}\) has the valuation of \(a\bar a\).

(5) This is the choice of the adelic frame of \(Y_k\) ([[?lean:New.Data.exists_spaceY_xFin_eq|the frame of \(Y_k\)]], in the area defining the spaces \(Y_k\)). Note
\(\lceil(m-k)/2\rceil=\lfloor(s+2)/2\rfloor\) for the string length \(s=m-1-k\), the scale required
by [[proofs/grh/upper-seesaw/string-sum-lattice-criteria|the criteria in the basis of string powers]].

(6) At the chosen places the reduction is \(1\) by hypothesis; at the places of \(Q\) the component
itself is \(1\). \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Seesaw/LevelIdeles.lean`.
