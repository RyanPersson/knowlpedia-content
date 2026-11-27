+++
id = "proofs/grh/upper-objects/index-sets-of-the-hermitian-spaces"
title = "Index sets of the bases of X_j and Y_j"
kind = "definition"
summary = "The index sets of the standard bases of the hermitian spaces X_j (n_j elements) and Y_j (r + jt elements), and the number of hyperbolic planes of Y_0."
aliases = ["row index", "block index", "index set of Y_0"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.BlockIndex", "New.BlockIndex.firstBlock", "New.BlockIndex.equivSum", "New.BlockIndex.card", "New.Data.ϱ", "New.Data.InitIndex", "New.Data.X", "New.Data.shape", "New.Data.RowIndex", "New.Data.Y", "New.Data.card_rowIndex", "New.Data.basisNumber"]
lean_files = ["src/New/UpperBound/Objects/LabelsAndIndexTypes.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]], with number of lifts \(m\) (even, \(m\ge2\)), ranks \(k\) and \(r=k+m-1\), block size \(t\), and \(n_j=k+j(t+1)\).

**Definition.**

* \(\varrho=m/2-1\).
* The index set of \(X_j\) is \(X_j^{\mathrm{idx}}=\{0,\dots,n_j-2\}\sqcup\{\ast\}\); it has \(n_j\) elements and a distinguished *last* index \(\ast\).
* The **row index set** \(\mathcal R\) (index set of \(Y_0\)) is the disjoint union
\[
\mathcal R=\{e_1,\dots,e_\varrho\}\sqcup\big(X_0^{\mathrm{idx}}\sqcup\{z\}\big)\sqcup\{e_1^*,\dots,e_\varrho^*\},
\]
the [[?lean:New.Shape.BesselIndex|Bessel index set]] of the shape with \(\varrho\) hyperbolic planes, middle block \(X_0^{\mathrm{idx}}\) and distinguished middle index \(\ast\).
* The index set of \(Y_j\) is \(\mathcal R\sqcup\{0,\dots,t-1\}\sqcup\dots\sqcup\{0,\dots,t-1\}\) with \(j\) copies of \(\{0,\dots,t-1\}\) (defined recursively: \(Y_{j+1}^{\mathrm{idx}}=Y_j^{\mathrm{idx}}\sqcup\{0,\dots,t-1\}\)). The first block \(\mathcal R\) embeds in every \(Y_j^{\mathrm{idx}}\).

Moreover a bijection \(\beta\colon\mathcal R\to\{0,\dots,r-1\}\) (the **basis numbering**) is fixed once and for all; it is an arbitrary bijection.

## Properties

\(\lvert\mathcal R\rvert=r\) and \(\lvert Y_j^{\mathrm{idx}}\rvert=r+jt\).

*Proof.* \(\lvert\mathcal R\rvert=\varrho+(n_0+1)+\varrho=2(m/2-1)+k+1=k+m-1=r\), using that \(m\) is even, \(m\ge2\), and \(n_0=k>0\). The second count follows by induction on \(j\). \(\square\)

## Remarks

For \(j>0\) the Lean text also fixes a bijection of \(Y_j^{\mathrm{idx}}\) with \(\alpha\sqcup(\{0,\dots,j-1\}\times\{0,\dots,t-1\})\) for any bijection \(\mathcal R\cong\alpha\); it is an arbitrary bijection which need not respect the blocks. It is used for counting, and the same arbitrary relabelling assigns the base and block coordinates through which the [[proofs/grh/upper-objects/grid-nodes|signs and parameters of the grid nodes]] are defined.

## References

1. Lean: `New.BlockIndex`, `New.Data.X`, `New.Data.RowIndex`, `New.Data.Y`, `New.Data.card_rowIndex`, `New.Data.basisNumber` in `src/New/UpperBound/Objects/LabelsAndIndexTypes.lean`.
