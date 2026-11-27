+++
id = "proofs/grh/spanning-unfolding-b/cell-rank-of-a-term"
title = "Cell rank of a term"
kind = "definition"
summary = "The flags of the frame and of its image under an isometry share vectors with prescribed leading coefficients; the cell rank records from which index a norm-one pair occurs, together with nonvanishing of a leading minor."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.PairOccursAt", "New.NormOnePairOccursFrom", "New.Filling.HasCellRank"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
+++

Let \(R\) be a commutative ring with involution, \(J\) the split Gram matrix of \(\varrho\) hyperbolic planes and a middle form, \(\gamma\) an isometry of \(J\), and \(f=(f_0,\dots,f_\varrho)=(e_0,\dots,e_{\varrho-1},z)\) the frame. For coefficient vectors \(x\in R^{\varrho+1}\) write \(f\cdot x=\sum_bx_bf_b\) and \(\gamma f\cdot x=\sum_bx_b\,\gamma f_b\).

* For \(c,c'\in R\) and \(0\le a\le\varrho\), **the pair \((c,c')\) occurs at \(a\)** for \(\gamma\) if there are \(x,y\in R^{\varrho+1}\) with
\[
f\cdot x=\gamma f\cdot y,\qquad x_a=c,\quad y_a=c',\qquad x_b=y_b=0\ \text{for }b>a .
\]
* For \(j\ge0\), **a norm-one pair occurs from \(j\)** for \(\gamma\) if there is \(c\in R\) with \(c\bar c=1\) such that the pair \((c,1)\) occurs at every \(a\) with \(j\le a\le\varrho\).

Now let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] and \(\gamma\in G(E)\), with [[proofs/grh/spanning-unfolding-b/filling-classes-and-terms|frame products \(Z(\gamma)\) and discriminant \(\operatorname{disc}(\gamma)\)]]. For \(0\le j\le\varrho+1\), \(\gamma\) **has cell rank \(j\)** if

1. a norm-one pair occurs from \(j\) for \(\gamma\);
2. the leading \(j\times j\) minor \(D_j\) of \(Z(\gamma)\) is nonzero (with \(D_0=1\));
3. \(j=\varrho+1\) if and only if \(\operatorname{disc}(\gamma)\ne0\).

## Remarks

The vector \(f\cdot x=\gamma f\cdot y\) lies in both the flag of the frame and the flag of its image, in the steps of index \(a\). For \(j=\varrho+1\) condition 1 is empty. If \(\operatorname{disc}(\gamma)\ne0\), then \(\gamma\) has cell rank \(\varrho+1\) ([[proofs/grh/spanning-unfolding-b/term-discriminant-is-totally-positive-or-zero|positivity of the discriminant]]). If \(\operatorname{disc}(\gamma)=0\), the [[proofs/grh/spanning-unfolding-b/characters-agree|characters agree]] at \(\gamma\) and \(E\) contains a primitive \(5040\)-th root of unity, then \(\gamma\) has a cell rank \(j\le\varrho\) ([[?lean:New.Filling.CharsAgree.exists_hasCellRank|existence of the cell rank]]), and it equals \(\varrho-\dim(A\cap\gamma A)\) ([[proofs/grh/spanning-unfolding-b/flags-of-a-term-and-the-cell-rank|flags of a term]]).

## References

1. Lean: `New.PairOccursAt`, `New.NormOnePairOccursFrom`, `New.Filling.HasCellRank` in `src/New/Spanning/Unfolding/Terms.lean`.
