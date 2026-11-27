+++
id = "proofs/grh/upper-objects/descent-pair-fitting-parameters"
title = "A parameter fits a descent pair"
kind = "definition"
summary = "The condition that the data of a descent pair are those of a Harish-Chandra parameter l on W corresponding to the parameter of the weight on V; and the product of minors attached to the pair."
aliases = ["fits parameters", "parameter of V of a descent pair", "product of minors"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.paramV", "New.DescentPair.isHCParam_paramV", "New.DescentPair.FitsParams", "New.DescentPair.productOfMinors", "New.DescentPair.decreasingPosition_paramV"]
lean_files = ["src/New/UpperBound/Objects/AuxiliaryPair.lean"]
+++

Let \(O\) be a [[proofs/grh/upper-objects/descent-pair|descent pair]] with signs \(s\) on \(r\), numbering \(\nu\), column numbers \(k^\pm\), weight \(\operatorname{wt}\), ranks \(\lvert r\rvert<\lvert n\rvert\); let \(r_\pm\) be the numbers of signs \(\pm1\). Fix the standard bijection \(n\cong\{0,\dots,\lvert n\rvert-1\}\).

**Definition.**

* The **parameter of \(V\)**, \(l'=l'_O\), assigns to an infinite place \(w\) and \(i\in n\) twice the entry, at the position of \(i\), of the [[?lean:New.hcParameter|Harish-Chandra parameter]] of the weight of \(O\) on \(V\) (column numbers \(k^+(\tau,i)+k^-(\tau,\lvert n\rvert-i)\), determinant exponent \(-\sum_{1\le i<\lvert n\rvert}k^-(\tau,i)\)) in rank \(\lvert n\rvert\). It is strictly decreasing in the position of \(i\).
* A family \(l=(l_w)\), \(l_w\colon r\to\mathbb Z\) (a doubled parameter on \(W\)), **fits \(O\)** if
  1. \(l\) and \(l'\) [[?lean:New.ParamsCorrespond|correspond]]: at each infinite place \(w\) they satisfy the [[?lean:New.IsBlockRule|block rule]] for \(\gamma=r_-\) and \(\gamma'_w=\lfloor n/2\rfloor+\operatorname{wt}_w\) (signs \(s\) on \(W\), all \(+1\) on \(V\));
  2. for every \(w\) and \(c\in r\): \(\nu(c)=\#\{c': s_{c'}=s_c,\ s_c\,l_w(c)<s_c\,l_w(c')\}\) (the basis vectors of each sign are numbered from \(0\) by decreasing \(s\cdot l_w\));
  3. \(k^+(\tau,i)=0\) for \(i>r_+\) and \(k^-(\tau,i)=0\) for \(i>r_-\).
* The **product of minors** at \(w\) is the polynomial in variables \(X_{a,c}\) (\(a\in n,c\in r\))
\[
\Pi_w=\prod_{\eta=\pm1}\ \prod_{p<\lvert n\rvert}\Big(\det S_{\eta,p}\Big)^{k^\eta(w,p)},
\]
where \(S_{\eta,p}\) is the [[?lean:New.staircaseBlock|staircase block]]: the \(p\times p\) matrix whose entry in position \((i,j)\), \(i,j<p\), is \(\sum X_{a,c}\) over the rows \(a\) of position \(i\) (in the order by decreasing \(\eta\,l'_w\)) and the columns \(c\) with \(s_c=\eta\) and \(\nu(c)=j\). The numbering of a general descent pair need not be injective; under the fitting hypotheses it is a bijection of the columns of each sign onto an initial segment, and the blocks occurring with positive exponent are genuine leading minors.

## References

1. Lean: `New.DescentPair.paramV`, `New.DescentPair.FitsParams`, `New.DescentPair.productOfMinors` in `src/New/UpperBound/Objects/AuxiliaryPair.lean`.
