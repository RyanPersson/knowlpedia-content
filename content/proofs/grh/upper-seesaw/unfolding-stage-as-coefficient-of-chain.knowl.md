+++
id = "proofs/grh/upper-seesaw/unfolding-stage-as-coefficient-of-chain"
title = "After each double step the unfolding function is a coefficient of the definite chain"
kind = "theorem"
summary = "At even stages the function of the unfolding equals a coefficient of the composite of the first pairs of theta lifts between the definite spaces X_k applied to the source form, with the evaluated data as finite data."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_zeroTerm_eq_integrated", "New.Data.exists_unfoldStage_eq_algFormCoeff_of_sourceFn", "New.Data.exists_unfoldStageOn_even_eq_sourceFn", "New.Data.exists_unfoldStage_eq_algFormCoeff", "New.Data.liftWeilFin_pointDatumY", "New.Data.doubleLiftEvalY_inclXFin", "New.Data.liftWeilFin_translatedPointDatumY", "New.Data.map_evaluatedDatum_of_conj_mem", "New.Data.evaluatedDatum_out"]
lean_files = ["src/New/UpperBound/Seesaw/UnfoldingStages.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/upper-seesaw/unfolding-stages|the functions of the unfolding]] and
[[proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data|the evaluated data]]
\(E_i(\vartheta,y)=\operatorname{ev}_i(\Phi^{y}_{2i}\ast\Phi^{y}_{2i+1})\). Let
\(\Theta_i(\vartheta,y)\) be the composite of the first \(i\) pairs of [[?c:Theta lift|theta lifts]]
\(X_0\to X_1\to\dots\to X_{2i}\) between the definite spaces, with the
[[?lean:New.Data.liftKernel|lift kernels of \(\vartheta\)]] and finite data \(E_0,\dots,E_{i-1}\)
([[?lean:New.doubleLiftChain|Lean: the chain of double lifts]]).

**Theorem.** Fix \(t\) and the archimedean points \(\xi_k\).

1. For every \(i\) with \(2i\le m-1\) there is a linear form \(l_i\), independent of
   \(\vartheta,\varphi,y\), such that \(\mathcal{W}^{R}_{2i}\) is the source function of
   \(\bigl(l_i,\Theta_i(\vartheta,y)\varphi\bigr)\): it is equivariant and equals
   \(g\mapsto l_i\bigl((\Theta_i\varphi)(g)\bigr)\) on \(U(X_{2i})\).
2. Let \(2i<m-1\), let \(\mathcal{R}\) be double lift data for \(Y_{2i}\to Y_{2i+1}\to Y_{2i+2}\)
   (the last with a grading \(Y\) with definite part \(X\)) whose finite evaluation is
   \(\operatorname{ev}_i\), and \(x\) an archimedean point of \(U(Y_{2i+2})\). There is a linear form
   \(l\), independent of \(\vartheta,\varphi,y\), with
   \[
   \mathcal{W}_{2i+2}\bigl(g\cdot(x,y_{2i+2})\bigr)=l\bigl((\Theta_{i+1}(\vartheta,y)\varphi)(\epsilon(g))\bigr)\qquad(g\in U(X)(\mathbb{A})).
   \]
3. (**Invariance of the evaluated data.**) If \(u\) is a finite point of \(U(X_{2i+2})\)
   (\(2i+2\le m-1\)) whose image in \(U(Y_{2i+2})\), conjugated by \(y_{2i+2}\), lies in the
   [[?lean:New.Data.levelY|level of \(Y_{2i+2}\)]], then the Weil operator of \((1,u)\) on the
   second tensor factor fixes \(E_i(\vartheta,y)\). The evaluated data depend only on the classes
   of the \(y_k\) modulo the levels.

## Proof

(Outline.) (2) for one step, assuming \(\mathcal{W}^{R}_{2i}\) is the source function of
\((l,\psi)\): write the two unfolding steps \(2i\to2i+1\to2i+2\) as an iterated integral of
\(\mathcal{W}^{R}_{2i}\) times two constant terms and apply
[[proofs/grh/upper-seesaw/double-unfolding-integral|the double unfolding integral]]. The datum
inside is \(Z_{\mathcal{R}}\varrho(T^{*},T')\) of the join of the two Weil-translated data. Every
operation acts separately on the real and finite factors of a [[?c:Tensor product of vector spaces|pure tensor]]
([[proofs/grh/upper-seesaw/finite-zero-term|property 2 of the finite zero term]]); on the real
factor the characters act through their weights, which do not depend on \(\vartheta\). Hence the
datum is \(v\otimes E_i(\vartheta,y)^{\ast}\) with a real [[?c:Fock model of the Weil representation|Fock vector]] \(v\) independent of
\(\vartheta\) and \(y\). The double unfolding integral gives \(z\) times the double theta integral with datum \(v\otimes E_i^{\ast}\), where the constant \(z\) depends only on the double lift data; so apply the complement to the double unfolding integral to the Fock vector \(zv\) (still independent of \(\vartheta\) and \(y\)): the result is a coefficient \(l''\) of the composite of the two lifts applied
to \(\psi\), evaluated at \(\epsilon(g)\).

(1) Induction on \(i\); \(i=0\) is the definition with \(l_0=t\). For the step, the function
\(\mathcal{W}^{R}_{2i+2}\) is equivariant, and the string of \(Y_{2i+2}\) has odd length \(m-1-(2i+2)\); for an odd string every element of the unipotent radical raises grades by at least two, so an equivariant function is determined by its values on the image of
\(U(X_{2i+2})\) ([[?lean:New.Grading.IsEquivariant.eq_sourceFn|uniqueness for odd strings]]), which are given by the one-step statement with \(x=\xi_{2i+2}\) (for the middle
double lift \(\epsilon\) is the identity). (2) in general follows from (1) and the one-step
statement.

(3) Elements of the levels fix the point data (they reduce to \(1\) at every place of the level, so
the factor in the finite Weil action is \(1\)); hence an element \(z\) with
\(y_{j+1}^{-1}zy_{j+1}\) in the level fixes the translated point datum. By
[[proofs/grh/upper-seesaw/double-lift-evaluation-equivariant|equivariance of the finite evaluation]],
\(\operatorname{ev}_i\) carries the action of the image of \(u\) on the data of the \(Y_k\) to the
action of \(u\) on the second factor. \(\blacksquare\)

## References

1. Lean: `New.Data.exists_unfoldStage_eq_algFormCoeff`, `New.Data.exists_unfoldStageOn_even_eq_sourceFn`, `New.Data.map_evaluatedDatum_of_conj_mem`, `New.Data.evaluatedDatum_out` and the lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/UnfoldingStages.lean`.
