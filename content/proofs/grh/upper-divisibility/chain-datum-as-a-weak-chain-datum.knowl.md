+++
id = "proofs/grh/upper-divisibility/chain-datum-as-a-weak-chain-datum"
title = "Two weak chain data attached to a chain datum"
kind = "theorem"
summary = "Expanding the gluing turns a chain datum into a weak chain datum computing the same composite lift; and the chain datum itself is a weak chain datum, its plain tensor being invariant."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsChainDatum.exists_isWeakChainDatum_compositeLift_eq", "New.Data.IsChainDatum.isWeakChainDatum", "New.Data.IsChainDatum.isInvariant_plainTensor", "New.Data.isJointlyInvariant_of_plainTensor", "New.Data.isAdmissibleCombination_sum_ungluedVacuum", "New.Data.add_mem_admissibleTranslations_mul_N", "New.Data.vacuumProjFinPart_gluedDoubleLiftDatum", "New.Data.vacuumProjFinPart_translateDatum", "New.Data.eq_zero_of_poleColumn_mem_integralBox", "New.Data.TameChar.normQ_notMem_of_N_mem"]
lean_files = ["src/New/UpperBound/Divisibility/ChainDatumExpansion.lean"]
proof_status = "outline"
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(\vartheta\) a [[?lean:New.Data.Twist|twist]] with modulus of norm \(q=\mathrm N\vartheta\) (prime to \(N\)), and \(\Psi\) a [[?lean:New.Data.IsChainDatum|chain datum]] for \(\vartheta\): a finitely supported function on tuples of translations, supported on tuples admissible for \(q\) and vanishing at the places prime to \(Mq\), with values integral away from \(q\), with conjugates of \(\ell^1\)-norm at most \(M^{3fmn_m^2}\) when the modulus is empty, and whose [[proofs/grh/upper-divisibility/expanding-the-gluing|glued tensor]] is invariant under the levels \(K_j\), \(j<m\). A [[?lean:New.Data.IsWeakChainDatum|weak chain datum]] asks instead: support on tuples admissible for \(qN\); values integral away from \(q\); conjugates of \(\ell^1\)-norm at most \(\exp(x^{60})\) when the modulus is empty; and joint invariance of the plain (unglued) tensor.

**Theorem.**

1. There is a weak chain datum \(\Psi'\) for \(\vartheta\) such that for every source form \(\varphi\) the [[?lean:New.Data.compositeLift|composite lift]] of \(\varphi\) for \(\Psi\) (lift through the double lifts with the glued tensor, restrict from \(X_m\) to \(Y_m\)) equals the [[?lean:New.Data.restrictedChain|restricted chain]] of \(\varphi\) for \(\Psi'\) (the \(\Psi'\)-combination of chains of \(m\) single lifts with translated vacua, restricted to \(Y_m\)).
2. The plain tensor of \(\Psi\) is invariant under the levels, and \(\Psi\) itself is a weak chain datum for \(\vartheta\).

## Proof

(1) By [[proofs/grh/upper-divisibility/expanding-the-gluing|expanding the gluing]], the glued tensor of \(\Psi\) is \(\sum_x\Psi(x)\sum_y\Omega(x+z(y))\). Collect terms: \(\Psi'(x')=\sum_{x+z(y)=x'}\Psi(x)\). Then the glued tensor of \(\Psi\) is the plain tensor of \(\Psi'\). The tuples \(x+z(y)\) are admissible for \(qN\), since \(z(y)\) vanishes off \(N\). The coefficients are sums of values of \(\Psi\), hence integral away from \(q\). For the empty modulus, the \(\ell^1\)-norm of each conjugate is at most \(M^{3fmn_m^2}\) times the number of classes, at most \(M^{3fmn_m^2}N^{fmn_m}\le\exp(x^{60})\) (size comparison, quoted). (In Lean this bookkeeping is the calculus of [[?lean:New.IsAdmissibleCombination|admissible combinations]].) The plain tensor of \(\Psi'\), equal to the glued tensor of \(\Psi\), is invariant; regrouping the \(\varrho+1\) pairs into \(m\) single factors shows that invariance of the tensor grouped in pairs gives joint invariance in the sense used for chains. Finally the chain built from a tensor is linear in the tensor, so the chain of the glued tensor of \(\Psi\) is the \(\Psi'\)-combination of chains of single lifts; restrict to \(Y_m\).

(2) Let \(\mathrm{pr}\) be the projection on the vacuum at the primes dividing \(\pi_N\) and their conjugates (the mean of the Heisenberg translations by integral vectors there), applied in every factor. (i) \(\mathrm{pr}\) fixes each \(\Phi^{0}_{t,j}\) with \(t\) admissible for \(q\): \(t_j\) is integral above \(N\), because the places above \(N\) do not divide \(q\) and neither they nor their conjugates are chosen ([[proofs/grh/upper-divisibility/data-of-a-weak-chain-datum-are-standard|integrality lemma]]). (ii) \(\mathrm{pr}\) multiplies a further translate by \(c\) of such a vector by the indicator of "\(c\) integral at these places"; the pole column of \(y_i\) has entries \(-y_i/N\), integral only if \(y_i=0\). Hence \(\mathrm{pr}\) applied to the glued datum of a double lift keeps only the term \(y_i=0\): \(\mathrm{pr}(\mathrm{Glue}\,\Omega(t))=\Omega(t)\), and \(\mathrm{pr}\) maps the glued tensor of \(\Psi\) to its plain tensor. (iii) The levels consist of integral elements, whose Weil action commutes with \(\mathrm{pr}\) ([[?lean:New.omega_projOn|`omega_projOn`]], quoted). So for a tuple \(b\) of level elements, \(b\cdot\mathrm{plain}=b\cdot\mathrm{pr}(\mathrm{glued})=\mathrm{pr}(b\cdot\mathrm{glued})=\mathrm{pr}(\mathrm{glued})=\mathrm{plain}\).

The other conditions of a weak chain datum follow from those of a chain datum: admissible for \(q\) implies admissible for \(qN\); integrality is the same; and \(M^{3fmn_m^2}\le\exp(x^{60})\) (quoted). \(\blacksquare\)

*Status.* The precise definitions of chain datum, weak chain datum and admissible combination, the behaviour of the vacuum projection under Heisenberg translations and Weil operators, and the size comparisons are quoted.

## Remarks

The first weak chain datum serves for sizes (sums of norms) and for the primes \(p\ne N\); the second, whose support stays integral above \(N\), serves for \(p=N\).

## References

1. Lean: `New.Data.IsChainDatum.exists_isWeakChainDatum_compositeLift_eq`, `New.Data.IsChainDatum.isWeakChainDatum`, `New.Data.IsChainDatum.isInvariant_plainTensor` in `src/New/UpperBound/Divisibility/ChainDatumExpansion.lean`.
