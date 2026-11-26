+++
id = "proofs/grh/derivatives-vacuum/vacuum-as-sum-of-translates"
title = "A multiple of the vacuum is a sum of translates of a theta-function vector"
kind = "lemma"
summary = "If the entire theta function of F is a theta function for the lattice conj(delta) a0^n and theta(F) = 1, then a nonzero multiple of the vacuum is a sum of N^(f n) finite Heisenberg translates of F; hence the translates of F span the finite part."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_smul_vac_eq_sum", "New.Parameters.IsThetaProduct.exists_smul_vacElem_eq_sum", "New.Parameters.finitePart_le_span_translates"]
lean_files = ["src/New/Derivatives/Vacuum/IntegralVacuum.lean"]
proof_status = "outline"
+++

Let \(E\) be a CM field with CM type and [[?lean:New.WeilData|Weil data]], with \(f\) infinite places, and let \(V\) be a [[?lean:New.Space.IsStd|standard]] space over \(E\) with index set \(n\). Write \(\mathrm{vac}\) for the [[?lean:New.Space.vacElem|vacuum]] of \(V\) and \(h(x)\) for the [[?lean:New.Space.finHeisenbergOp|finite Heisenberg operator]] of a finite adelic vector \(x\) (translation \(\varrho(x_f)\) times a scalar of absolute value one, the semicharacter of \(x\)).

**Lemma.**

1. Let \(\delta\in E\) be integral at all finite places with \(\delta\bar\delta=N\in\mathbb{N}\), \(N\ne0\), and let \(F\in\mathcal{S}(V)\) be such that \(\Theta_F\) is a [[?lean:New.IsThetaFunction|theta function]] for \(\bar\delta\,\mathfrak{a}_0^{\,n}\) and \(\theta(F)=1\). Then there are \(c\in\mathbb{C}^\times\), a finite set \(\Gamma\) with \(\lvert\Gamma\rvert=N^{f\lvert n\rvert}\), finite adelic vectors \(a_j\) (\(j\in\Gamma\)) and \(b\) with
\[ c\cdot\mathrm{vac}=\sum_{j\in\Gamma}h(a_j)\,\varrho(b_f)F . \]
2. In particular, if \(F\) is a [[proofs/grh/derivatives-vacuum/theta-product|theta product]] of level \(1\) (for any \(C,\Omega\); here \(E\) is the field of the parameters), this holds with \(\lvert\Gamma\rvert=(q_1^2)^{f\lvert n\rvert}\).
3. For any space \(V\), if \(c\cdot\mathrm{vac}=\sum_jh(a_j)\varrho(b_f)F\) with \(c\ne0\), then the [[?lean:New.Space.finitePart|finite part]] of \(V\) is contained in the complex span of the translates \(\varrho(x_f)F\), \(x\) a finite adelic vector.

## Proof

1. This rests on the finite Fourier inversion of the Lib ([[?lean:New.Space.exists_fourier_coefficients|Fourier coefficients of a theta function]]), which is asserted here: under the hypotheses there are a finite index set \(Y\) and coefficients \(c_i\) (\(i\in Y\)) such that (a) each \(c_i\cdot\mathrm{vac}\) is a sum over a set \(\Gamma\) of cardinality \(N^{f\lvert n\rvert}\) of translates \(h(a_j)\varrho(b_f)F\), and (b) a positive power of \(N\) times \(F\) is a linear combination, with the coefficients \(c_i\), of translates of the vacuum. If all \(c_i\) were \(0\), (b) would give \(N^{r}F=0\), contradicting \(\theta(F)=1\). So some \(c_i\ne0\), and (a) for this \(i\) is the claim.

2. Take \(\delta=q_1\), \(N=q_1^2\); condition 5 of a theta product of level \(1\) and \(\theta(F)=1\) are the hypotheses.

3. The finite part is spanned by the vectors \(h(z)\mathrm{vac}\). Now \(h(z)\mathrm{vac}=c^{-1}\sum_jh(z)h(a_j)\varrho(b_f)F\), and a composition of finite Heisenberg translations is a scalar multiple of one translation \(\varrho(x_f)\).

## References

1. Lean: `New.Parameters.exists_smul_vac_eq_sum`, `New.Parameters.IsThetaProduct.exists_smul_vacElem_eq_sum`, `New.Parameters.finitePart_le_span_translates` in `src/New/Derivatives/Vacuum/IntegralVacuum.lean`.
