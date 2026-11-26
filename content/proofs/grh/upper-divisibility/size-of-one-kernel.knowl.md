+++
id = "proofs/grh/upper-divisibility/size-of-one-kernel"
title = "Size of one kernel and of the rows of the chain"
kind = "lemma"
summary = "The kernel of a translated vacuum multiplies norms of all conjugates by at most exp(x^50 + half the row size sum), and the row size sums of the m lifts add up to at most the chain size plus half the error unit."
aliases = ["row size sum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.sqrt_weylNormSq_jetMap_le", "New.Data.rowSizeSum", "New.Data.sum_rowSizeSum_le", "New.Data.sum_range_jetSize_add_eq", "New.Data.rowMainLength_add_rowSlack_le", "New.Data.jetSize_zero"]
lean_files = ["src/New/UpperBound/Size/ArchimedeanSize.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]]. For a stage \(j\) the **row size sum** is
\[
\operatorname{rs}(j)=\sum_{\tau\in\Phi}\sum_{i<n_j}s_\infty\bigl(\lambda_{j+1}(\tau,i)\bigr),
\]
where \(\lambda_{j+1}(\tau,i)\) is the length of row \(i\) of the Young diagram at \(\tau\) with \(c(\tau,h)\) columns of height \(h<n_{j+1}\), and \(s_\infty\) is the jet size.

**Lemma.**

1. (**One kernel.**) Let \(j<m\), \(\sigma\) an automorphism of \(\mathbb{C}\), \(t\) a tuple of translations, \(g\in G_f(X_j)\), \(g'\in G_f(X_{j+1})\). For the untwisted kernel, the linear map \(\mathcal K_j(\omega(g,g')\Phi^{0}_{t,j})\) between the weight spaces of \(X_j\) and \(X_{j+1}\) satisfies, for every vector \(\xi\),
\[
\bigl\lVert\sigma\bigl(\mathcal K_j(\omega(g,g')\Phi^{0}_{t,j})\,\xi\bigr)\bigr\rVert\le\exp\bigl(x^{50}+\tfrac12\operatorname{rs}(j)\bigr)\,\lVert\sigma(\xi)\rVert,
\]
with \(\lVert\cdot\rVert^2\) the [[?lean:New.weylNormSq|squared Gram norm]].
2. (**The rows.**) \(\displaystyle\sum_{j<m}\operatorname{rs}(j)\le\operatorname{cs}+\tfrac12\mathrm{err}\), with \(\operatorname{cs}\) the [[proofs/grh/upper-divisibility/level-compensates-the-excess|chain size]] and \(\mathrm{err}=fa(\log b)^3\).

## Proof

(1) The general bound for the jets of a combination of vacuum translates ([[?lean:New.Parameters.sqrt_weylNormSq_schurJet_le_of_isVacuumCombination|`sqrt_weylNormSq_schurJet_le_of_isVacuumCombination`]], quoted from the file on jets, conjugates and bounds), applied with growth rate \(a+1\), gives the factor \(\exp\bigl(\mathrm{const}+\mathrm{count}+\tfrac12(\mathrm{lengths}+\operatorname{rs}(j))\bigr)\), where \(\mathrm{const}\) is a constant of \(q_0,d\) times \((q_0Tn_{j+1}n_j+1)^2\), \(\mathrm{count}=f\,n_{j+1}n_j\log(2(a+1)+2)\), and \(\mathrm{lengths}=\sum_{\tau,i}\lambda_{j+1}(\tau,i)/(a+1)\); the jets are scaled by a conjugate of \(\overline{\bar\pi_M}\), of squared absolute value \(M\) ([[proofs/grh/upper-divisibility/row-lengths-and-jet-sizes|part 3 there]]), which is what produces \(\log(M/\Omega)\) in \(s_\infty\). Each row has length at most main length plus slack, at most \(2a\); so \(\mathrm{lengths}\le2fn_j\), and \(\mathrm{const}+\mathrm{count}+\tfrac12\mathrm{lengths}\le x^{50}\) is a size comparison (quoted).

(2) For \(j<m\): \(\lambda_{j+1}(\tau,i)\le\operatorname{main}(\tau,i)+\operatorname{slack}(i)\le2a\) ([[proofs/grh/upper-divisibility/row-lengths-and-jet-sizes|row lengths]]), so by the growth of the jet size
\[
s_\infty(\lambda_{j+1}(\tau,i))\le s_\infty(\operatorname{main}(\tau,i))+\operatorname{slack}(i)\bigl(\log(2a+1)+\log(M/\Omega)\bigr)\le s_\infty(\operatorname{main}(\tau,i))+25\log b\cdot\operatorname{slack}(i),
\]
using \(2a+1\le b^{2}\) and \(\log(M/\Omega)\le23\log b\) (quoted). Summing over the rows \(i<n_j\) at \(\tau\): the main lengths contribute \(s_\infty(c(\tau,1))+(k-1)s_\infty(w(\tau))\) (as \(s_\infty(0)=0\)), the slacks add up to \(b+\lfloor a/\lfloor x_1\rfloor\rfloor+n_j(\Delta/2)^2\). Summing over \(\tau\): \(\sum_\tau s_\infty(c(\tau,1))=\lvert\Phi_a\rvert s_\infty(a)\). As \(s_\infty(w(\tau))\ge0\), \(k-1\) may be replaced by \(k\). Summing over \(j<m\) gives \(\operatorname{cs}\) plus \(m\cdot f\cdot25\log b\,(b+\lfloor a/\lfloor x_1\rfloor\rfloor+n_m(\Delta/2)^2)\le\tfrac12\mathrm{err}\) (size comparison, quoted). \(\blacksquare\)

*Status.* The analytic bound for jets of vacuum translates is the main quoted input; the numerical comparisons are quoted.

## References

1. Lean: `New.Data.sqrt_weylNormSq_jetMap_le`, `New.Data.sum_rowSizeSum_le` in `src/New/UpperBound/Size/ArchimedeanSize.lean`.
