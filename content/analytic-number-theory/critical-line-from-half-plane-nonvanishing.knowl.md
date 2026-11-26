+++
id = "analytic-number-theory/critical-line-from-half-plane-nonvanishing"
title = "From half-plane nonvanishing to the critical line"
kind = "theorem"
summary = "A uniform zero-free right half-plane puts every open-strip Dirichlet zero on its boundary."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-character","analytic-number-theory/dirichlet-l-function","analytic-number-theory/principal-dirichlet-character","analytic-number-theory/critical-strip","analytic-number-theory/dirichlet-zero-reflection","analytic-number-theory/primitive-dirichlet-character"]
+++

Assume that for every [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\eta\) of every positive modulus, its [[analytic-number-theory/dirichlet-l-function|\(L\)-function]] is nonzero whenever \(\Re w>1/2\), with the [[analytic-number-theory/principal-dirichlet-character|principal character]] at its pole \(w=1\) excepted. Then every zero of \(L(s,\chi)\) in the [[analytic-number-theory/critical-strip|open critical strip]], for any \(\chi\), satisfies \(\Re s=1/2\).

## Proof

Let \(L(s,\chi)=0\) and \(0<\Re s<1\). Then \(s\ne1\). The hypothesis applied to \(\chi\) implies \(\Re s\le1/2\). By [[analytic-number-theory/dirichlet-zero-reflection|reflection of zeros]], \(L(1-s,\bar\chi)=0\). The reflected point also lies in the open strip. Applying the hypothesis to \(\bar\chi\) gives \(\Re(1-s)\le1/2\). As \(\Re(1-s)=1-\Re s\), we obtain \(\Re s\ge1/2\). Together the inequalities give equality. Restricting \(\chi\) to the [[analytic-number-theory/primitive-dirichlet-character|primitive characters]] gives the primitive-character statement.

## References

- [Half-plane nonvanishing implies the open-strip statement](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L28)
