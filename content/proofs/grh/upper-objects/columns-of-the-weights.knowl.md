+++
id = "proofs/grh/upper-objects/columns-of-the-weights"
title = "The weights of X_j and Y_m in terms of their columns"
kind = "proposition"
summary = "The lift diagrams and the weights of X_j and Y_m are given by explicit column counts common to all lifts; the weights of X_m and Y_m interlace; bounds for rows and columns."
aliases = ["weights interlace"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.liftDiagram_eq_sum_columnCount", "New.Data.weightX_eq", "New.Data.weightY_eq", "New.Data.weightY_eq_weightX_add", "New.Data.weightX_succ", "New.Data.liftDiagram_zero", "New.Data.liftDiagram_succ", "New.Data.liftDiagram_le", "New.Data.lastEntry_eq", "New.Data.keptColumns_le_columnCount", "New.Data.keptColumns_n_sub_one", "New.Data.sortedParamY_sub_paramX", "New.Data.columnsY_le", "New.Data.columnCount_le", "New.Data.sum_columnsY_add_keptColumns", "New.Data.cast_columnCount_k", "New.Data.cast_columnCount_n_succ"]
lean_files = ["src/New/UpperBound/Objects/Weights.lean"]
proof_status = "full"
+++

Notation as in [[proofs/grh/upper-objects/weights-of-the-definite-spaces|parameters, weights and lift diagrams]]: \(c_\tau(h)\), \(\ell_j(\tau)\), \(\operatorname{kept}(h)\), \(c^Y_\tau(h)\), \(\mu(X_j)\), \(\mu(Y_m)\), \(\mu^+_{j+1}\). The admissible data satisfy \(k>1\) and \(k+t+1\le\Delta/2\).

**Proposition.** Let \(\tau\) be an infinite place of \(E\).

1. For all \(j,p\ge0\): \(\mu^+_{j+1,\tau,p}=\sum_{p<u<n_{j+1}}c_\tau(u)\). That is, the diagram of lift \(j+1\) is a Young diagram with \(c_\tau(u)\) columns of height \(u\) for each \(u<n_{j+1}\).
2. For \(p<n_j\): \(\mu(X_j)_{\tau,p}=\ell_j(\tau)+\sum_{p<u<n_j}c_\tau(u)\); and \(\ell_j(\tau)=n_{j+1}/2-\kappa_{j+1}(\tau)+c_\tau(n_j)\).
3. For all \(p\): \(\mu(Y_m)_{\tau,p}=\mu(X_m)_{\tau,p+1}+\operatorname{kept}(p+1)\), and \(\operatorname{kept}(u)\le c_\tau(u)\) for all \(u\). Hence \(\mu(X_m)_{p+1}\le\mu(Y_m)_p\le\mu(X_m)_p\) for \(p+1<n_m\): the weights interlace.
4. For \(p<n_m-1\): \(\mu(Y_m)_{\tau,p}=\ell_m(\tau)+\sum_{p<u<n_m-1}c^Y_\tau(u)\).
5. *(Bounds.)* For \(j<m\): \(\mu^+_{j+1,\tau,0}\le a_\tau+\kappa_{j+1}(\tau)\); \(\mu^+_{j+1,\tau,p}\le\kappa_{j+1}(\tau)\) for \(0<p<k\); and \(\mu^+_{j+1,\tau,p}\le m\Delta\) for \(p\ge k\). Moreover \(c^Y_\tau(u)\le\Delta\) for \(u\ge k\), and \(c_\tau(h)\le\kappa_1(\tau)[h=k]+\Delta\) for \(h\ne1\).

## Proof

*Values of the column counts.* Since \(k>1\) and \(k+t+1\le\Delta/2\le\kappa_1(\tau)\): \(c_\tau(k)=\kappa_1(\tau)-n_1/2\ge0\), \(c_\tau(n_{j+1})=\Delta-(t+1)\ge0\), \(c_\tau(u)=0\) for \(1\ne u<k\), and \(c_\tau(u)=0\) for \(n_j<u<n_{j+1}\) (then \(t+1\nmid u-k\)).

*Recursions.* (a) For \(p<n_{j+1}\), \(\mu(X_{j+1})_p=\mu^+_{j+1,p}+n_j/2-\kappa_{j+1}\). For \(p<n_j\) this is the definition together with \([n_{j+1}]_p=[n_j]_p+(t+1)/2\). For \(p=n_j+b\), \([n_{j+1}]_p=[t+1]_b-n_j/2\) and \(\lambda^X_p=[t+1]_b-\kappa_{j+1}\), so \(\mu(X_{j+1})_p=n_j/2-\kappa_{j+1}\) while \(\mu^+_{j+1,p}=0\). (b) For \(p<k\): \(\mu(X_0)_p=a_\tau[p=0]\), so \(\mu^+_{1,p}=a_\tau[p=0]+\kappa_1-n_1/2\). (c) For \(p<n_{j+1}\): by (a) and \(\kappa_{j+2}=\kappa_{j+1}+\Delta\), \(n_{j+2}=n_j+2(t+1)\), we get \(\mu^+_{j+2,p}=\mu^+_{j+1,p}+\Delta-(t+1)\).

*1.* Induction on \(j\). For \(p\ge n_j\) both sides are \(0\) (no column has height strictly between \(n_j\) and \(n_{j+1}\)). For \(p<n_j\), \(\sum_{p<u<n_{j+1}}c_\tau(u)=\sum_{p<u<n_j}c_\tau(u)+c_\tau(n_j)\). For \(j=0\) the first sum is \(a_\tau[p=0]\) (only height \(1\) occurs below \(k\)) and \(c_\tau(k)=\kappa_1-n_1/2\): this is (b). For the step use (c) and \(c_\tau(n_{j+1})=\Delta-(t+1)\).

*2.* For \(j=0\) this is \(\mu(X_0)_p=a_\tau[p=0]\). For \(j+1\) combine (a) with 1 and the definition \(\ell_{j+1}=n_j/2-\kappa_{j+1}\). For the formula for \(\ell_j\): the last row \(p=n_j-1\) of \(\mu^+_{j+1}\) is \(c_\tau(n_j)\) by 1 and is \(\ell_j+\kappa_{j+1}-n_{j+1}/2\) by definition and the first part of 2.

*3.* First, \(\lambda^{Y,\mathrm{sorted}}_p-\lambda^X_{p+1}-\tfrac12=\operatorname{kept}(p+1)\), checked in three cases. If \(p+1<k\): \([k-1]_p-[k]_{p+1}-\tfrac12=0\). If \(p+1=n_i\) (\(i\ge0\)): \(\lambda^{Y,\mathrm{sorted}}_p=-\kappa_{i+1}+\Delta/2\) and \(\lambda^X_{n_i}=[t+1]_0-\kappa_{i+1}=t/2-\kappa_{i+1}\), difference \(\Delta/2-(t+1)/2\). Otherwise \(p=n_i+b\), \(b<t\), \(b+1\le t\): \([t]_b-[t+1]_{b+1}-\tfrac12=0\). Second, \([n_m-1]_p=[n_m]_{p+1}+\tfrac12\). Subtracting gives the identity for the weights. The inequality \(\operatorname{kept}(u)\le c_\tau(u)\): for \(u=k\), \(\Delta/2-(t+1)/2\le\kappa_0+\Delta-(k+t+1)/2\) as \(k\le\Delta\); for \(u>k\), \(\Delta/2-(t+1)/2\le\Delta-(t+1)\) as \(t+1\le\Delta\). Finally \(\mu(X_m)_p-\mu(X_m)_{p+1}=c_\tau(p+1)\) by 2.

*4.* By induction on \(N\ge u\), \(\sum_{u\le v<N}c^Y_\tau(v)+\operatorname{kept}(N)=\sum_{u<v\le N}c_\tau(v)+\operatorname{kept}(u)\) (the kept terms telescope, using \(\operatorname{kept}\le c_\tau\)). Take \(u=p+1\), \(N=n_m-1\); \(\operatorname{kept}(n_m-1)=0\) because \(n_{m-1}<n_m-1<n_m\) (as \(t\ge1\), \(m\ge1\)). Then use 3 and 2.

*5.* From (b), (c): \(\mu^+_{i+1,p}\le a_\tau[p=0]+\kappa_1[p<k]+i\Delta\) by induction on \(i\) (for \(p\ge k\), \(i=0\) the row is empty). Since \(\kappa_{j+1}=\kappa_1+j\Delta\) and \(j\Delta\le m\Delta\), the three bounds follow. For \(c^Y\): \(\operatorname{kept}\le\Delta/2\) and, for \(u>k\), \(c_\tau(u)-\operatorname{kept}(u)\le\Delta/2\). The bound for \(c_\tau\) is read off the definition. \(\square\)

## References

1. Lean: `New.Data.liftDiagram_eq_sum_columnCount`, `New.Data.weightX_eq`, `New.Data.weightY_eq`, `New.Data.weightY_eq_weightX_add`, `New.Data.liftDiagram_le` in `src/New/UpperBound/Objects/Weights.lean`.
