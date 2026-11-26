+++
id = "proofs/grh/upper-objects/properties-of-grid-nodes"
title = "Ranks, signs, gaps and interlacing of the grid nodes"
kind = "proposition"
summary = "The rank and number of negative signs of each node of the grids, the diagonal comparison of the two grids, the gap and size of the parameters, and the interlacing of the parameters of Y and Y-tilde at the node (m,m)."
aliases = ["grid parameters interlace"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.card_gridIndex", "New.Data.negCount_gridSigns", "New.Data.negCount_gridSigns_eq_sum", "New.Data.gridSigns_true_zero", "New.Data.exists_equiv_diagonal_signs", "New.Data.sumElim_gridSigns_comp_gridDiagEquiv_symm", "New.Data.card_gridIndex_mod_two", "New.Data.gridSigns_eq_one", "New.Data.gridParam_interlace", "New.Data.abs_gridParam_le", "New.Data.card_gridIndex_le", "New.Data.hasGap_gridParam", "New.Data.gridParam_injective", "New.Data.two_mul_gap_le_abs_gridParam_sub", "New.Data.even_gridParam_add_card_sub_one", "New.Data.targetParameter_strictAnti", "New.Data.targetParameter_add_liftWeight_gap", "New.Data.sum_ite_targetParameter_sub_sum_ite_mem_Icc"]
lean_files = ["src/New/UpperBound/Objects/Parameters.lean"]
proof_status = "outline"
+++

Notation as in [[proofs/grh/upper-objects/grid-nodes|grid nodes]]; \(z\in\{0,1\}\).

**Proposition.**

1. *(Rank.)* The node \((i,j)\) has \(r+z+i(t+z)+j(t-z)\) indices. This number is even for \(z=1\), and for \(z=0\) it is odd iff \(i+j\) is even. For \(i,j\le m\) it is at most \(2n_m\).
2. *(Negative signs.)* With offset \(0\), the node \((i,j)\) has \(\lfloor(m\dot-j+z)/2\rfloor\) negative signs, all on the base. For \(j\ge m\) all signs are \(+1\).
3. *(Diagonal.)* For \(j\le m\), with offset \(0\), there is a bijection between the index set of \(\tilde Y\) at \((j,j)\) and that of \(Y\) at \((j,j)\) plus one point under which the signs of \(\tilde Y\) are those of \(Y\) together with the sign \((-1)^j\) at the extra point. For \(j=0\) it is the identity (the extra point has sign \(+1\)).
4. *(Gap.)* At every \(\tau\) the doubled parameter of every node (any offset) has [[?lean:New.HCParam.HasGap|gap \(\Delta\)]]: its entries are pairwise distinct, congruent to (rank \(-1\)) mod \(2\), and two doubled entries at indices of different signs differ by at least \(2\Delta\).
5. *(Size.)* For \(i,j\le m\) and offset \(0\), all doubled entries have absolute value at most \(\lceil20b\rceil\).
6. *(Interlacing.)* At every \(\tau\), with offset \(0\), for every integer \(x\): the number of doubled entries of the parameter of \(\tilde Y^m_m\) above \(x\), minus the number of doubled entries of the parameter of \(Y^m_m\) above \(x\), is \(0\) or \(1\). So the two parameters alternate in decreasing order, the first entry coming from \(\tilde Y\).

## Proof

Throughout, the data satisfy \(k+t+1\le\Delta/2\), \(\Delta\le w_{l+1}\) and \(w_{l'+1}\ge w_{l+1}+\Delta\) for \(l<l'\) (more precisely \(w_b\ge w_a+\Delta\) for \(a<b\) and \(\ge w_a+2\Delta\) for \(a+1<b\)), and \(2\Delta\le w_{l+1}\) in the two places indicated (Lean: instances of the logarithmic size comparison). Write \(\varsigma=\lambda^Y_\tau\); recall \(\varsigma_p=k/2-1-p\) for \(p<k-1\) and \(\varsigma_{k-1+a}=\Delta/2-w_{a+1}\).

*1.* Count the blocks; for the parity use that \(r,t\) are odd; for the bound, \(r+1+m(t+1)+m(t-1)\le2(k+m(t+1))\) since \(r+1=k+m\).

*2.* The added blocks have sign \(+1\). The number of \(n<N\) with \(\epsilon(0,j,n+1\dot-k)=-1\) is \(\lfloor(N+1\dot-k\dot-j)/2\rfloor\), by induction on \(N\): \(\epsilon(0,j,a)=(-1)^{a+\min(a,j)}\) is \(-1\) exactly for \(a=j+1,j+3,\dots\). Take \(N=r+z\) and \(r+1-k=m\). If \(j\ge m\) then \(a\le m\le j\) and the exponent is \(2a\).

*3.* Two finite sets with sign functions are isomorphic as signed sets iff they have the same cardinality and the same number of negative signs. Cardinalities: \(j(t+1)+j(t-1)=2jt\). Negative signs: \(\lfloor(m\dot-j+1)/2\rfloor=\lfloor(m\dot-j)/2\rfloor+(\min(j,m)\bmod2)\), as \(m\) is even. For \(j=0\) the extra point has number \(r\), excess \(r+1-k=m\) even, hence sign \(+1\).

*4.* *Facts on \(\varsigma\).* (a) \(\varsigma\) is strictly decreasing and \(2\varsigma_n\le k\). (b) For \(p<k+j-1\): \(\varsigma_p+w_j\ge\Delta/2\); for \(p\ge k+j-1\): \(\varsigma_p+w_j\le-\Delta/2\). (If \(p<k-1\) the entry is \(\ge-k/2\) and \(w_j\ge\Delta\); otherwise \(\varsigma_p=\Delta/2-w_a\) with \(a=p+2-k\), and \(a=j\), \(a<j\), \(a>j\) give \(\Delta/2\), \(\ge\Delta/2+\Delta\), \(\le\Delta/2-\Delta\).) (c) If \(n+1\dot-k\ne n'+1\dot-k\) then \(\lvert\varsigma_n-\varsigma_{n'}\rvert\ge\Delta\) (one of the two is \(\Delta/2-w_{a+1}\) with a larger index, and the weights are \(\Delta\)-separated and \(\ge\Delta\)). (d) If the base entry \(n\) at the node \((i,j)\) with offset \(o\) has sign \(-1\) and \(l<j\), then \(\lvert\varsigma_n+w_{o+l+1}\rvert\ge3\Delta/2\): the sign \(-1\) forces the excess \(a=n+1\dot-k\) to differ from \(o+l\) and \(o+l+1\) (for \(o\le a\le o+j\) the exponent \(o+a+(a-o)=2a\) is even), so \(n+2-k\) differs from \(o+l+1\) and \(o+l+2\), and the weights are then \(\Delta\), resp. \(2\Delta\), apart.

*Distinctness.* After adding the lowering, the doubled entries are \(2\varsigma_n+z\) on the base, \(2w_{l+1}+(t+z)-1-2b\) and \(-2w_{o+l+1}+(t-z)-1-2b\) in the blocks. Base entries are distinct by (a); a base entry and an up-block entry differ because \(2\varsigma_n\le k\) and \(w\ge\Delta\); a base entry and a down-block entry by (b); entries of two up blocks or two down blocks with different centres because the centres are \(\Delta\) apart and \(t<\Delta/2\); up and down because \(w\ge\Delta\). *Parity.* From 1 and \(t\) odd, case by case. *Gap.* The index of sign \(-1\), say \(x\), is a base index \(n\). If \(y\) is a base index, use (c) (different signs force different excess). If \(y\) is in an up block, \(2\varsigma_n\le k\) and \(2\Delta\le w_{l+1}\). If \(y\) is in a down block, use (d). In each case the doubled entries differ by at least \(2\Delta\).

*5.* Each doubled entry is bounded in absolute value by \(10\,w_{2m}(\tau)\), and \(w_{2m}\le2b\) (Lean: `New.Data.liftWeight_le_two_mul_b`, cited); so by \(\lceil20b\rceil\).

*6.* Let \(\varphi(y)=1\) if \(x<y\) and \(0\) otherwise, and \(g(n,y)=\max(0,\min(n,\lfloor(y-x)/2\rfloor))\). A falling block \(A,A-2,\dots\) of length \(n\) has \(g(n,A+1)\) entries above \(x\), a rising block \(A,A+2,\dots\) has \(g(n,A+2n-1)\). Two blocks with the same centre \(c\) (doubled) and lengths \(n+1\), \(n\) interlace: the difference of their counts lies between \(\varphi(\mathrm{low})\) and \(\varphi(\mathrm{high})\) for any \(\mathrm{low}\le c-n\), \(\mathrm{high}\ge c+n\). Claim, by induction on \(m'\ge0\): for the systems truncated to \(m'\) pairs of blocks and a base of \(k-1+m'\) (resp. \(k+m'\)) entries, with \(s=2\varsigma_{k-1+m'}\),
\[
\varphi(s)\le\operatorname{count}_{\tilde Y}-\operatorname{count}_Y\le\varphi(-s-1).
\]
For \(m'=0\): the entries \(-2\varsigma_n-1\), \(n<k\), of \(\tilde Y\) are the rising block \(1-k,\dots,k-3\) and \(-s-1\); those of \(Y\) are the falling block \(k-2,\dots,2-k\); and \(s=\Delta-2w_1\) lies far below. For the step, the two new base entries and the two new pairs of blocks contribute: the down blocks at \(-w_{m'+1}\) (lengths \(t+1\) on \(\tilde Y\), \(t\) on \(Y\)) a difference between \(\varphi(2\varsigma_{k+m'})\) and \(\varphi(2\varsigma_{k-1+m'})\), and the up blocks at \(w_{m'+1}\) (lengths \(t\) on \(Y\), \(t-1\) on \(\tilde Y\)) a difference between \(\varphi(-2\varsigma_{k-1+m'}-1)\) and \(\varphi(-2\varsigma_{k+m'}-1)\); adding these to the induction hypothesis and to the new base entries \(\varphi(-2\varsigma_{k+m'}-1)\) (on \(\tilde Y\)) and \(\varphi(2\varsigma_{k-1+m'})\) (on \(Y\)) telescopes to the claim for \(m'+1\). For \(m'=m\), with \(r=k-1+m\), the counts are those of the nodes \((m,m)\), and \(0\le\varphi\le1\).

The verifications by linear integer arithmetic in (d), in the parity cases, in 5 and in the induction step of 6 are stated here with their inputs but not expanded; the Lean proofs discharge them with `omega`/`grind`. \(\square\)

## References

1. Lean: `New.Data.card_gridIndex`, `New.Data.negCount_gridSigns`, `New.Data.exists_equiv_diagonal_signs`, `New.Data.hasGap_gridParam`, `New.Data.abs_gridParam_le`, `New.Data.gridParam_interlace` in `src/New/UpperBound/Objects/Parameters.lean`.
