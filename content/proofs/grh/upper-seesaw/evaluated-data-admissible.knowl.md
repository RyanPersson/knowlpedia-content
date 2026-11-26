+++
id = "proofs/grh/upper-seesaw/evaluated-data-admissible"
title = "The evaluated data are admissible combinations of glued vacua"
kind = "theorem"
summary = "The tensor of the evaluated data of all pairs of edges is a combination of glued translates of the vacuum with coefficients integral away from the conductor norm up to a fixed power of the norm of pi_M, and of size one for the trivial twist."
aliases = ["good datum", "chosen ratio"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.chosenRatio", "New.Data.chosenRatio_mul_star", "New.Data.v_star_piM_mul_chosenRatio", "New.Data.flipScale_mul_divStar_ideleA", "New.Data.isScalingAtM_of_eq_one_or_eq", "New.Data.isScalingAtM_one", "New.Data.isScalingAtM_lastScaling", "New.Data.latticeScale_two_mul", "New.Data.isAdmissibleEval_doubleLiftEvalY", "New.Data.absNorm_pow_mul_card_dvd_residueMatrixCount_pow", "New.Data.exists_isAdmissibleCombination_evaluatedDatum", "New.Data.exists_isAdmissibleCombination_gluedVacuum"]
lean_files = ["src/New/UpperBound/Seesaw/GoodDatum.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-seesaw/point-data-admissible|the admissibility of point data]]
and [[proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data|the evaluated data]]
\(E_i(\vartheta,y)\), \(0\le i\le\varrho\). Let \(\mathcal{C}=M^{f\,n_m^{2}}\) be the residue matrix
count, and for a tuple \(t\) of [[?c:Finite adele ring of a number field|finite adelic]] matrices on the edges \(X_k\to X_{k+1}\) let
[[?lean:New.Data.gluedVacuum|\(\mathrm{gv}(t)\)]] be the glued vacuum: the [[?c:Tensor product of vector spaces|pure tensor]] over the
pairs \(i\) of the glued translates of the (integral) vacua by \((t_{2i},t_{2i+1})\). A tuple is
[[?lean:New.Data.admissibleTranslations|admissible for \(q\)]] if \(\bar\pi_Mt_k\) is integral away
from \(q\) for all \(k\).

**Theorem.**

1. For \(i\le\varrho\), the evaluation \(\operatorname{ev}_i\) is an
   [[proofs/grh/upper-seesaw/neighbour-vacuum|admissible evaluation]] for \(N\), the places
   dividing \(\pi_N\), \(\beta=\pi_M\), and row weights \(\beta\) on \(Y_{2i}\), \(\bar\beta\) on
   \(Y_{2i+2}\).
2. For \(i\le\varrho\) there is a constant \(C_i\) such that for all \(\vartheta\) and all \(y\)
   integral away from \(q=\mathrm{N}Q\): \(E_i(\vartheta,y)\) is an
   [[proofs/grh/upper-seesaw/admissible-combination|admissible combination]] of the
   \(C_i\,\mathrm{gl}(t_1,t_2)\), \(t_1,t_2\in T_q(\bar\pi_M)\), with denominator
   \(\mathcal{C}^{4}\) away from \(q\), and size \(1\) if \(Q=\emptyset\).
3. There is a constant \(C\) such that for all such \(\vartheta,y\): the pure tensor
   \(E_\varrho\otimes\dots\otimes E_0\) is an admissible combination of the \(C\,\mathrm{gv}(t)\),
   \(t\) admissible for \(q\), with denominator \(\mathcal{C}^{2m}\) away from \(q\), and size
   \(1\) if \(Q=\emptyset\).

## Proof

(1) Apply
[[proofs/grh/upper-seesaw/admissible-evaluation-of-edge-pairs|the admissible evaluation theorem]]
to the middle double lift (\(i<\varrho\)) or the last one (\(i=\varrho\)). Inputs:
[[proofs/grh/upper-seesaw/tower-lattice-data|the lattices of the tower are glued lattices]] with
scales \(u_k=(a/\bar a)^{\lceil(m-k)/2\rceil}\), so \(u_{2i}=(a/\bar a)u_{2i+2}\); the **chosen
ratio** \(\delta=\varpi/\bar\varpi\) (\(\varpi\) the chosen idele) has norm one, is \(1\) above
\(N\), and \(s_E\cdot(a/\bar a)=\bar\eta\,\delta\) because \(s_E=\bar\eta\bar\alpha/\alpha\) and
\(a=\alpha/\bar\varpi\); hence \(s_Eu_{2i}=\bar\eta\delta u_{2i+2}\), the scale condition of
[[proofs/grh/upper-seesaw/lifting-conditions-for-the-two-pairs|the lifting conditions]] (for the
last pair \(u_m=1\) and the last space is standard). The scalings \(\kappa=1\), resp. the last
scaling, are scalings at \(M\) for \((N,\pi_M,\delta)\): \(\pi_M\) is a unit above \(N\), and
\(\bar\pi_M\delta\) has the valuations of \(\pi_M\).

(2) By part 4 of the point data lemma, the join \(\Phi^{y}_{2i}\ast\Phi^{y}_{2i+1}\) is an
admissible combination of translates of the vacuum with weights as in (1); \(\operatorname{ev}_i\)
is linear and by (1) sends each such translate to an admissible combination of the
\(C_i\,\mathrm{gl}(t_1,t_2)\) (here \(q\) is coprime to \(N\), since places above \(\pi_N\) are not
in \(Q\)). [[proofs/grh/upper-seesaw/admissible-combination-substitution|Substitution]] multiplies
the three denominators, all powers of \(\mathrm{N}\pi_M=M^{f}\) with exponents at most
\(n_m^{2}\) each (the third is at most two such), so their product divides \(\mathcal{C}^{4}\).

(3) The [[proofs/grh/upper-seesaw/admissible-combination-calculus|rule for pure tensors]] with
\(\varrho+1\) factors gives denominator \((\mathcal{C}^{4})^{\varrho+1}=\mathcal{C}^{2m}\) and size
\(1\). The glued vacuum uses the integral vacua, which are the vacua multiplied by fixed nonzero scalars \(\kappa_j\) (a power of the [[?lean:New.Parameters.vacuumScale|vacuum scale]] with exponent the number of matrix entries of the edge \(j\)); the constants \(C_i\) are divided by these factors and multiplied together to give
\(C\). \(\blacksquare\)

## References

1. Lean: `New.Data.exists_isAdmissibleCombination_gluedVacuum`, `New.Data.exists_isAdmissibleCombination_evaluatedDatum`, `New.Data.isAdmissibleEval_doubleLiftEvalY` and the lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/GoodDatum.lean`.
