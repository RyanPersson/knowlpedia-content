+++
id = "proofs/grh/spanning-unfolding-a/common-vectors-of-two-flags"
title = "Common vectors of two flags and their top index"
kind = "definition"
summary = "A pair (mu, mu') occurs at index j for two matrices P, P' if some vector of both flags up to j has coefficients mu, mu' at j; the top index of a common vector is the least index above which both coordinate vectors vanish."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.PairOccursInColumnsAt", "New.IsTopIndex", "New.exists_isTopIndex", "New.IsTopIndex.ne_zero_or_ne_zero", "New.isTopIndex_of_ne_zero", "New.PairOccursInColumnsAt.of_le", "New.pairOccursInColumnsAt_of_forall_mul_vecMul_eq", "New.dotProduct_cons_zero_init"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
+++

Let \(F\) be a field and \(P,P'\) two matrices over \(F\) with the same rows and with columns \(P_0,\dots,P_n\), \(P'_0,\dots,P'_n\); they define two flags, the spans of the first columns. For \(\mu,\mu'\in F\) and an index \(j\), the pair \((\mu,\mu')\) **occurs at \(j\)** if there are \(x,y\in F^{n+1}\) with
\[
\sum_bx_bP_b=\sum_by_bP'_b,\qquad x_j=\mu,\quad y_j=\mu',\qquad x_b=y_b=0\ \text{ for } b>j .
\]
For coordinate vectors \(x,y\in F^{n+1}\), the **top index** of \((x,y)\) is the least \(j\) such that \(x_b=y_b=0\) for all \(b>j\).

## Properties

1. Every pair \((x,y)\) has a top index \(j\); if \(x\ne0\), then \(x_j\) and \(y_j\) are not both \(0\). Conversely an index above which \(x,y\) vanish and at which they are not both zero is the top index.
2. *(Induction.)* If, for every \(i<n\), occurrence of \((\mu,\mu')\) at \(i\) implies occurrence at \(i+1\), then occurrence at \(j\) implies occurrence at every \(l\ge j\).
3. *(Criterion by linear forms.)* Suppose the row index set is finite. If every linear form \(m\) on the ambient space with \(m(P_b)=m(P'_b)=0\) for all \(b<j\) satisfies \(\mu\,m(P_j)=\mu'\,m(P'_j)\), then \((\mu,\mu')\) occurs at \(j\).
4. *(Shift.)* If \(w_b=0\) for \(b\le i\) and \(x_b=0\) for \(b>i\), then \(\sum_bw_{b+1}x_b=x_i\,w_{i+1}\).

## Proof

1. The set of indices above which \(x,y\) vanish contains \(n\), so it has a least element \(j\). If \(x_j=y_j=0\) then \(x,y\) vanish from \(j\) on; for \(j=0\) this gives \(x=0\), and for \(j>0\) it contradicts minimality. The converse is clear.

2. Induction on \(l\).

3. A vector \(X\) lies in a subspace \(A\) plus another vector condition exactly when all forms killing the relevant spaces agree; precisely, by [[?lean:New.exists_mulVec_eq_of_annihilator|solvability from annihilators]] (if every form \(m\) that kills the columns of \(P\) in a set \(s\) and those of \(P'\) in \(s'\) has \(m(PX)=m(P'Y)\), then \(Px=P'y\) for some \(x,y\) equal to \(X,Y\) outside \(s,s'\)), applied with \(s=s'=\{b<j\}\), \(X=\mu\,\mathbf e_j\), \(Y=\mu'\mathbf e_j\): we get \(x,y\) with \(x_j=\mu\), \(y_j=\mu'\) and \(x_b=y_b=0\) for \(b>j\).

4. Only the term \(b=i\) is nonzero.

## References

1. Lean: `New.PairOccursInColumnsAt`, `New.IsTopIndex`, `New.exists_isTopIndex`, `New.IsTopIndex.ne_zero_or_ne_zero`, `New.isTopIndex_of_ne_zero`, `New.PairOccursInColumnsAt.of_le`, `New.pairOccursInColumnsAt_of_forall_mul_vecMul_eq`, `New.dotProduct_cons_zero_init` in `src/New/Spanning/Unfolding/Climbing.lean`.
