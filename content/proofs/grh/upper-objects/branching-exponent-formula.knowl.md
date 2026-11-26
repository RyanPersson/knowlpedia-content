+++
id = "proofs/grh/upper-objects/branching-exponent-formula"
title = "The branching exponent"
kind = "lemma"
summary = "The difference of the sizes of the weights of X_m and Y_m at a place tau is a_tau - m Delta/2; it is the number of columns losing a box plus the last entry."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.branchExponent_eq", "New.Data.branchExponent_eq_sum_columns", "New.Data.sum_branchExponent", "New.Data.sum_paramX", "New.Data.sum_sortedParamY", "New.sum_twiceBlockEntry"]
lean_files = ["src/New/UpperBound/Objects/Weights.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-objects/weights-of-the-definite-spaces|parameters, weights and lift diagrams]].

**Lemma.** For every infinite place \(\tau\) of \(E\), the branching exponent \(n_\tau=\lvert\mu(X_m)_\tau\rvert-\lvert\mu(Y_m)_\tau\rvert\) satisfies

1. \(n_\tau=a_\tau-m\,\Delta/2\);
2. \(n_\tau=\sum_{0<u<n_m}\big(c_\tau(u)-\operatorname{kept}(u)\big)+\ell_m(\tau)\);
3. \(\sum_\tau n_\tau=\lvert\Phi_a\rvert\,a-f\,m\,\Delta/2\), where \(f\) is the number of infinite places of \(E\).

## Proof

*1.* The blocks \([n]\) have sum \(0\), so \(n_\tau\) is the sum of the first \(n_m\) entries of \(\lambda^X_\tau\) minus the sum of the first \(n_m-1\) entries of \(\lambda^{Y,\mathrm{sorted}}_\tau\). By induction on \(j\) (adding one block \(-\kappa_{j+1}+[t+1]\) of \(t+1\) entries), \(\sum_{p<n_j}\lambda^X_{\tau,p}=a_\tau-(t+1)\sum_{i=1}^j\kappa_i(\tau)\). By induction on \(j\) (adding the entry \(-\kappa_{j+1/2}=\Delta/2-\kappa_{j+1}\) and the block \(-\kappa_{j+1}+[t]\)), \(\sum_{p<n_j-1}\lambda^{Y,\mathrm{sorted}}_{\tau,p}=-\sum_{i=1}^{j}(\kappa_i(\tau)-\Delta/2)-t\sum_{i=1}^j\kappa_i(\tau)\). The difference at \(j=m\) is \(a_\tau-m\Delta/2\).

*2.* By the [[proofs/grh/upper-objects/columns-of-the-weights|column description]], part 3, \(\mu(Y_m)_p=\mu(X_m)_{p+1}+\operatorname{kept}(p+1)\), so \(n_\tau=\mu(X_m)_0-\sum_{0<u<n_m}\operatorname{kept}(u)\); and \(\mu(X_m)_0=\ell_m+\sum_{0<u<n_m}c_\tau(u)\) by part 2, with \(\operatorname{kept}\le c_\tau\).

*3.* Sum 1 over \(\tau\). \(\square\)

## Remarks

Form 2 is the exponent that appears in the [[?lean:New.exists_branching_matrix|integral branching map]] from \(U(X_m)\) to \(U(Y_m)\): each column that loses a box contributes one factor.

## References

1. Lean: `New.Data.branchExponent_eq`, `New.Data.branchExponent_eq_sum_columns`, `New.Data.sum_branchExponent` in `src/New/UpperBound/Objects/Weights.lean`.
