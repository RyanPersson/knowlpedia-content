+++
id = "proofs/grh/upper-objects/principal-forms-are-finite-dimensional"
title = "The target parameter has gap Delta, and the forms of principal level are finite-dimensional"
kind = "theorem"
summary = "For the signs of Y_0 and of every W_j the doubled target parameter has gap Delta; hence its type kernel is a cusp kernel of order Delta/2 and the spaces of forms of principal level are finite-dimensional."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.hasGap_signsY_paramW", "New.Data.hasGap_paramW", "New.Data.isCuspKernel_typeKernel_paramW", "New.Data.paramW_lt_iff", "New.Data.negCount_signsW", "New.Data.card_filter_basisNumber"]
lean_files = ["src/New/UpperBound/Objects/Rows.lean"]
proof_status = "outline"
+++

Let \(D\) be admissible data, \(\lambda\) the [[proofs/grh/upper-objects/signs-and-parameter-of-w|doubled target parameter]] on the row index set, with gap \(\Delta\) and half gap \(\Delta/2\).

**Theorem.**

1. At each infinite place, \(\lambda\) [[?lean:New.HCParam.HasGap|has gap \(\Delta\)]] for the signs of \(Y_0\) and for the signs of \(W_j\), every \(j\).
2. If \(\lambda\) has gap \(\Delta\) at each infinite place for signs \(s\), then the type kernel of \((\lambda,s)\) is a [[?lean:New.IsCuspKernel|cusp kernel]] of order \(\Delta/2\).
3. Under the hypothesis of 2, for every space \(V\) of rank \(r\) with signs \(s\), the space of [[proofs/grh/upper-objects/target-form|forms of principal level]] on \(V\) is finite-dimensional. In particular the target dimension is finite.

Moreover \(\lambda_\tau\) is strictly decreasing in the basis number, and \(W_j\) has exactly \(m-j\) minus signs for \(1\le j\le m\).

## Proof

*1.* For \(Y_0\) this is the node \((0,0)\) of the grid \(Y\) in the [[proofs/grh/upper-objects/properties-of-grid-nodes|properties of the grid nodes]]. For \(W_j\): distinctness and parity do not depend on the signs; and the signs of \(W_j\) differ exactly for basis numbers on either side of \(k+j-1\), where \(\varsigma_p+w_j\ge\Delta/2\), resp. \(\le-\Delta/2\); so the doubled entries differ by at least \(2\Delta\).

*2.* The Lean theorem `New.isCuspKernel_typeKernel` (theory of discrete series with a large gap, in `Lib`; cited) states that the type kernel of a parameter with gap \(500r^3+A\) at every infinite place is a cusp kernel of order \(A\). Here \(500r^3\le\Delta/2\), so gap \(\Delta\) gives order \(\Delta/2\).

*3.* The Lean theorem `New.Space.finite_levelSpace` (cited) states that the forms of a cusp kernel fixed by an open subgroup form a finite-dimensional space. \(\square\)

## References

1. Lean: `New.Data.hasGap_paramW`, `New.Data.isCuspKernel_typeKernel_paramW` in `src/New/UpperBound/Objects/Rows.lean`.
