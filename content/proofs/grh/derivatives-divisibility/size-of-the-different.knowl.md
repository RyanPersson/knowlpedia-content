+++
id = "proofs/grh/derivatives-divisibility/size-of-the-different"
title = "Size of the different and of the root discriminant at the infinite places"
kind = "proposition"
summary = "At every infinite place the generator delta_E of the different has absolute value A (q1/q0) sqrt(d) with |log A| bounded by a constant of the parameters; it is within a bounded factor of the root discriminant, and both lie between x^10 and x^12."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.exists_abs_log_le_and_apply_deltaE_eq", "New.Parameters.abs_log_deltaE_sub_log_rootDiscr_le", "New.Data.hasLogBound_deltaE", "New.Data.rootDisc_mem_Icc", "New.Data.hasLogBound_rootDisc"]
lean_files = ["src/New/Derivatives/Field/ChosenPlaces.lean"]
proof_status = "outline"
+++

**Proposition.** Let \(E=K(\zeta)\) at level \(s\), \(T=q_1/q_0=3^{\lfloor\log_3s\rfloor+5}2^s\), and \(\delta_E\) the imaginary generator of the different (see the [[proofs/grh/derivatives-divisibility/different-of-e|theorem on the different]]). Let \(c_P\) be the [[?lean:New.Parameters.constantBound|constant bound]] of the parameters, a number depending only on \(q_0\) and \(d\).

1. For every infinite place \(v\) there is \(A>0\) with \(\lvert\log A\rvert\le c_P\) and \(\lvert\delta_E\rvert_v=A\cdot T\cdot\sqrt d\).
2. For every \(v\), \(\bigl\lvert\log\lvert\delta_E\rvert_v-\log\mathrm{rd}_E\bigr\rvert\le2c_P\).
3. If \(D\) is [[?lean:New.Data|admissible data]] of level \(s\) with smallest scale \(x\), then \(x^{10}\le\lvert\delta_E\rvert_v\le x^{12}\) for every \(v\), and \(x^{10}\le\mathrm{rd}_E\le x^{12}\).

## Proof

1. All prime factors of \(T\) divide \(q_0\), so \(\Phi_{q_1}(X)=\Phi_{q_0}(X^T)\). Let \(\xi=\Phi_v(\zeta)^T\), a primitive \(q_0\)-th root of unity. By the chain rule, \(\Phi_v(P'(\zeta))=\Phi_{q_0}'(\xi)\cdot T\,\Phi_v(\zeta)^{T-1}\), so \(\lvert P'(\zeta)\rvert_v=A\,T\) with \(A=\lvert\Phi_{q_0}'(\xi)\rvert>0\), and \(\lvert\delta_E\rvert_v=\lvert P'(\zeta)\rvert_v\sqrt d\). The constant \(c_P\) contains as a summand \(\sum_w\lvert\log\lvert\Phi_{q_0}'(w)\rvert\rvert\) over the primitive \(q_0\)-th roots of unity \(w\in\mathbb{C}\), its other summands being nonnegative; hence \(\lvert\log A\rvert\le c_P\).

2. Let \(Q=\log(T\sqrt d)\). By 1, \(\lvert\log\lvert\delta_E\rvert_v-Q\rvert\le c_P\) for all \(v\). Since \(f\log\mathrm{rd}_E=\sum_v\log\lvert\delta_E\rvert_v\), the mean also satisfies \(\lvert\log\mathrm{rd}_E-Q\rvert\le c_P\); apply the triangle inequality.

3. By 1, \(\log\lvert\delta_E\rvert_v=\log A+\log T+\tfrac12\log d\). In the source the comparison of this sum with \(10\log x\) and \(12\log x\) is carried out by its bookkeeping of logarithmic bounds ([[?lean:New.Data.HasLogBound|the class of log bounds]]) together with the [[?lean:New.Data.scale_inequalities|scale inequalities]] of the data; the facts used are that \(T\) is of size about \(x^{11}\) and that \(\log A\) and \(\log d\) are bounded by \(c_P\), which is negligible against \(\log x\). This numerical step is only asserted here; it is proved by `New.Data.hasLogBound_deltaE`. The bounds for \(\mathrm{rd}_E\) follow since \(\mathrm{rd}_E^{\,f}=\prod_v\lvert\delta_E\rvert_v\) is a product of \(f\) numbers in \([x^{10},x^{12}]\). \(\blacksquare\)

## References

1. Lean: `New.Parameters.exists_abs_log_le_and_apply_deltaE_eq`, `New.Parameters.abs_log_deltaE_sub_log_rootDiscr_le`, `New.Data.hasLogBound_deltaE`, `New.Data.rootDisc_mem_Icc`, `New.Data.hasLogBound_rootDisc` in `src/New/Derivatives/Field/ChosenPlaces.lean`.
