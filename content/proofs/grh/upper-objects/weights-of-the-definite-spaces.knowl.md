+++
id = "proofs/grh/upper-objects/weights-of-the-definite-spaces"
title = "Parameters, weights and lift diagrams of X_j and Y_m"
kind = "definition"
summary = "The doubled Harish-Chandra parameters and the highest weights of the definite spaces X_j and Y_m at each infinite place, the Young diagrams of the lifts, their column counts, and the branching exponent."
aliases = ["weight of X_j", "weight of Y_m", "lift diagram", "column count", "kept columns", "branching exponent"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.twiceBlockEntry", "New.Data.firstRowExcess", "New.Data.paramX", "New.Data.weightX", "New.Data.liftDiagram", "New.Data.columnCount", "New.Data.lastEntry", "New.Data.keptColumns", "New.Data.columnsY", "New.Data.sortedParamY", "New.Data.weightY", "New.Data.branchExponent", "New.Data.two_mul_weightX", "New.Data.two_mul_weightY", "New.Data.paramX_block", "New.Data.sortedParamY_n_sub_one", "New.Data.sortedParamY_block"]
lean_files = ["src/New/UpperBound/Objects/Weights.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]]: \(m\) lifts, ranks \(k\) (even) and \(r\), \(t=5r\) (odd), \(n_j=k+j(t+1)\) (even), gap \(\Delta=2r^8\), the integer \(a\), the set \(\Phi_a\) of [[?lean:New.Data.aPlaces|\(a\)-places]] and, for an infinite place \(\tau\) of \(E\), the [[?lean:New.Data.liftWeight|lift weights]] \(\kappa_j(\tau)=\kappa(\tau)+(j+\tfrac12)\Delta\), and \(\kappa_{j-1/2}=\kappa_j-\Delta/2\). Entries and rows are numbered from \(0\). For \(n\ge0\) let \([n]=\big(\tfrac{n-1}2,\tfrac{n-3}2,\dots,\tfrac{1-n}2\big)\), so \([n]_p=\tfrac{n-1}2-p\); its entries sum to \(0\). Put \(a_\tau=a\) if \(\tau\in\Phi_a\) and \(a_\tau=0\) otherwise.

**Definition.** Fix \(\tau\).

1. *(Parameter of \(X_j\).)* The infinite sequence \(\lambda^X_\tau\) is the concatenation of \([k]+(a_\tau,0,\dots,0)\) and of the blocks \(-\kappa_i(\tau)+[t+1]\), \(i=1,2,\dots\). The **Harish-Chandra parameter of \(X_j\)** at \(\tau\) consists of its first \(n_j\) entries. (The Lean text stores \(2\lambda^X_\tau\), which is integral.)
2. *(Weight of \(X_j\).)* \(\mu(X_j)_{\tau,p}=\lambda^X_{\tau,p}-[n_j]_p\) for \(p<n_j\). These are integers.
3. *(Lift diagram.)* The **diagram of lift \(j+1\)** (from \(U(X_j)\) to \(U(X_{j+1})\)) is \(\mu^+_{j+1,\tau,p}=\mu(X_j)_{\tau,p}+\kappa_{j+1}(\tau)-n_{j+1}/2\) for \(p<n_j\), and \(0\) for \(p\ge n_j\).
4. *(Column counts.)* For a height \(h\ge0\): \(c_\tau(1)=a_\tau\); if \(k\neq1\), \(c_\tau(k)=\max(\kappa_1(\tau)-(k+t+1)/2,\,0)\); \(c_\tau(h)=\max(\Delta-(t+1),0)\) if \(h>k\) and \((t+1)\mid h-k\); and \(c_\tau(h)=0\) otherwise. The **last entry** is \(\ell_j(\tau)=0\) for \(j=0\) and \(\ell_j(\tau)=n_{j-1}/2-\kappa_j(\tau)\) for \(j\ge1\).
5. *(Parameter and weight of \(Y_m\).)* The sequence \(\lambda^{Y,\mathrm{sorted}}_\tau\) is the concatenation of \([k-1]\) and, for \(i=1,2,\dots\), of the entry \(-\kappa_{i-1/2}(\tau)\) followed by the block \(-\kappa_i(\tau)+[t]\). The block \([k-1]\) and the entries \(-\kappa_{i-1/2}\) are the entries of the [[?lean:New.Data.targetParameter|target parameter]]. The parameter of \(Y_m\) consists of the first \(n_m-1\) entries and \(\mu(Y_m)_{\tau,p}=\lambda^{Y,\mathrm{sorted}}_{\tau,p}-[n_m-1]_p\).
6. *(Kept columns.)* \(\operatorname{kept}(h)=\Delta/2-(t+1)/2\) if \(h\ge k\) and \((t+1)\mid h-k\), and \(0\) otherwise; \(c^Y_\tau(h)=\operatorname{kept}(h)+\max\big(c_\tau(h+1)-\operatorname{kept}(h+1),0\big)\).
7. *(Branching exponent.)* \(n_\tau=\sum_{p<n_m}\mu(X_m)_{\tau,p}-\sum_{p<n_m-1}\mu(Y_m)_{\tau,p}\).

## Remarks

Entry \(n_j+b\) of \(\lambda^X_\tau\) (\(b\le t\)) is \([t+1]_b-\kappa_{j+1}(\tau)\). Entry \(n_j-1\) of \(\lambda^{Y,\mathrm{sorted}}_\tau\) is \(-\kappa_{j+1/2}(\tau)\), and entry \(n_j+b\) (\(b<t\)) is \([t]_b-\kappa_{j+1}(\tau)\). Integrality of the weights: \(k\), \(t+1\), \(n_j\) are even, so \(2\lambda^X\) and \(2[n_j]\) are odd entrywise; similarly for \(Y_m\).

The truncated subtractions in 4 and 6 are never truncated for admissible data, because \(k+t+1\le\Delta/2\le\kappa_j(\tau)\); see the [[proofs/grh/upper-objects/columns-of-the-weights|column description]]. That the parameters are decreasing also follows from that description. This file concerns only the combinatorics of the weights; the spaces \(X_j,Y_m\) are the standard definite hermitian spaces of ranks \(n_j\) and \(n_m-1\).

## References

1. Lean: `New.Data.paramX`, `New.Data.weightX`, `New.Data.liftDiagram`, `New.Data.columnCount`, `New.Data.lastEntry`, `New.Data.sortedParamY`, `New.Data.weightY`, `New.Data.keptColumns`, `New.Data.columnsY`, `New.Data.branchExponent` in `src/New/UpperBound/Objects/Weights.lean`.
