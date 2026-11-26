+++
id = "proofs/grh/upper-seesaw/tower-gradings-and-evaluated-data"
title = "Gradings of the tower Y_k and the evaluated data"
kind = "construction"
summary = "The gradings of the spaces Y_k as X_k plus a string of length m-1-k, the evaluation of the pairs Y_2i -> Y_2i+1 -> Y_2i+2, and the evaluated data of translated point data."
aliases = ["evaluated datum", "translated point datum", "grading of Y_k"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.gradingY", "New.Data.lastGrading", "New.Data.doubleLiftEvalY", "New.Data.residueMatrixCount", "New.Data.translatedPointDatumY", "New.Data.evaluatedDatum"]
lean_files = ["src/New/UpperBound/Seesaw/EdgePairEvaluation.lean"]
+++

Let \(D\) be the [[?lean:New.Data|data]] of the proof, with \(m=2\varrho+2\) lifts, level \(N\),
and the tower of [[?c:Hermitian space|hermitian spaces]] [[?lean:New.Data.spaceY|\(Y_0,\dots,Y_m\)]] over \(E\).

**Gradings.** For \(k\le 2\varrho+1=m-1\), \(Y_k\) carries the
[[?lean:New.Grading|grading]] \(\mathcal{Y}_k\) with definite part \(X_k\) and a string of length
\(m-1-k\), parameter \(N\), and constant
\[
c=-\bigl(j\cdot M\cdot\delta_E\bigr)^{-1},
\]
independent of \(k\), where \(j\) is the purely imaginary element of the Weil data, \(M=p_0p_1\)
and \(\delta_E\) the chosen purely imaginary generator of the [[?c:Different of a number field|different]]. The space \(Y_m\), whose
Gram matrix is \(1\), carries the **last grading** with an empty string.

**Evaluation of pair \(i\).** The pair of lifts \(Y_{2i}\to Y_{2i+1}\to Y_{2i+2}\) has strings of
lengths \(m-1-2i\) (odd), \(m-2-2i\), \(\max(m-3-2i,0)\). The map
\(\operatorname{ev}_i\) is the [[proofs/grh/upper-seesaw/double-lift-data|finite evaluation]] of
the middle double lift if \(i<\varrho\), of the last double lift (with \(N=\pi_N\bar\pi_N\)) if
\(i=\varrho\), and \(0\) for \(i>\varrho\).

**Evaluated data.** Let \(\vartheta\) be a tame character and \(y=(y_k)_k\) [[?c:Finite adele ring of a number field|finite adelic]] points
of the unitary groups of the \(Y_k\). The **translated point datum** of lift \(k+1\) is
\[
\Phi_k^{y}=\omega_{\mu_{k+1}}(y_k,y_{k+1})\,\Phi_k ,
\]
the [[?lean:New.Data.pointDatumY|point datum]] \(\Phi_k\) on \(\operatorname{Hom}(Y_k,Y_{k+1})\)
moved by the finite Weil action twisted by the character
\(\mu_{k+1}\) = [[?lean:New.Data.chainChar|the character of lift \(k+1\)]]. The **evaluated datum**
of pair \(i\) is
\[
\operatorname{ev}_i\bigl(\Phi_{2i}^{y}\ast\Phi_{2i+1}^{y}\bigr)\in
\mathcal{S}_f(\operatorname{Hom}(X_{2i},X_{2i+1}))\otimes\mathcal{S}_f(\operatorname{Hom}(X_{2i+1},X_{2i+2}'')),
\]
where the last index set is that of the double lift data. The number
\(M^{f\,n_m^{2}}\) (\(f\) the number of infinite places, \(n_m\) the rank of \(X_m\)) is the
**residue matrix count** used as a denominator bound later.

## References

1. Lean: `New.Data.gradingY`, `New.Data.lastGrading`, `New.Data.doubleLiftEvalY`, `New.Data.translatedPointDatumY`, `New.Data.evaluatedDatum`, `New.Data.residueMatrixCount` in `src/New/UpperBound/Seesaw/EdgePairEvaluation.lean`.
