+++
id = "proofs/grh/upper-objects/descent-pairs-of-the-data"
title = "The descent pairs (W_j, V_j) of the data, and their parameters"
kind = "theorem"
summary = "For each lift index j the descent pair with W = W_j, V of rank r + t and the character of lift j; the target parameter fits it: the parameter of V_j is the target parameter with the block of length t centred at -w_j inserted."
aliases = ["descent pair of the data", "descent pair (W_j, V_j)"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.descentPair", "New.Data.descentCentres", "New.Data.descentCentres_centre", "New.Data.sign_descentCentres", "New.Data.isParam_paramW", "New.Data.isParam_paramV", "New.Data.hcParameter_descentPair", "New.Data.hcParameter_descentPair_sub", "New.Data.sum_Ioo_posRank_columnCount_descentPair", "New.Data.paramsCorrespond_descentPair", "New.Data.fitsParams_descentPair"]
lean_files = ["src/New/UpperBound/Objects/Rows.lean"]
proof_status = "full"
+++

Let \(D\) be admissible data, \(\vartheta\) a [[?lean:New.Data.TameChar|tame character]], \(1\le j\le m\), \(\varsigma_\tau\) the [[?lean:New.Data.targetParameter|target parameter]] (entries numbered from \(0\)), \(w_j(\tau)\) the lift weight, \(\beta\) the basis numbering of the row index set \(\mathcal R\).

**Definition.** The **\(j\)-th descent pair** is the [[proofs/grh/upper-objects/descent-pair|descent pair]] with

* level places: the [[proofs/grh/upper-objects/spaces-y-and-w|level places of \(\vartheta\)]] (chosen places and \(Q\));
* \(W=W_j\) with its signs; index sets \(\mathcal R\hookrightarrow\mathcal R\sqcup\{0,\dots,t-1\}\) (so \(V=V_j\) is standard definite of rank \(r+t\));
* numbering \(\nu(c)=\beta(c)\) if the sign of \(c\) is \(+\), and \(\nu(c)=r-1-\beta(c)\) if it is \(-\);
* \(k^+(\tau,i)=\big(\varsigma_\tau(i\dot-1)-\max(\varsigma_\tau(i),\ \lfloor t/2\rfloor-w_j(\tau))-1\big)^+\) and \(k^-(\tau,i)=\big(\min(\varsigma_\tau(r\dot-i\dot-1),\ -w_j(\tau)-\lfloor t/2\rfloor)-\varsigma_\tau(r\dot-i)-1\big)^+\), where \((\cdot)^+\) is the positive part and \(\dot-\) is subtraction of natural numbers truncated at \(0\) (truncation does occur at heights that are used: e.g. the column number of height \(1\) of \(V_j\) involves \(k^-\) at height \(r+t-1>r\), where both indices truncate to \(0\));
* character the [[?lean:New.Data.liftChar|character of lift \(j\)]] \(\mu^0_j\vartheta\), of weight \(-w_j\), with its [[?lean:New.Data.liftTamePart|tame part]] (trivial off the chosen places and \(Q\)).

**Theorem.**

1. At \(\tau\), the doubled Harish-Chandra parameter of the weight of forms on \(V_j\), in decreasing order and lowered by \(2u-1\) with \(u=m-j+w_j(\tau)-\lfloor r/2\rfloor\), is: \(2\varsigma_\tau(p)\) for \(p<k+j-1\); then the doubled block of length \(t\) centred at \(-w_j(\tau)\); then \(2\varsigma_\tau(p-t)\).
2. The doubled target parameter on \(W_j\) and the parameter \(l'\) of \(V_j\) [[?lean:New.ParamsCorrespond|correspond]] for the weights \(m-j\) (the number of minus signs of \(W_j\)) and \(\lfloor(r+t)/2\rfloor-w_j(\tau)\).
3. The doubled target parameter [[proofs/grh/upper-objects/descent-pair-fitting-parameters|fits]] the \(j\)-th descent pair.

## Proof

Put \(a=k+j-1\) (the number of plus signs of \(W_j\)); \(W_j\) has \(m-j\) minus signs since \(r+1=k+m\). Use the facts on \(\varsigma\) from the [[proofs/grh/upper-objects/properties-of-grid-nodes|properties of the nodes]]: \(\varsigma\) is strictly decreasing, \(\varsigma_q+w_j\ge\Delta/2\) for \(q<a\), \(\le-\Delta/2\) for \(q\ge a\), and \(t/2<\Delta/2\).

*1.* Define the list \(L_p=r-2a+2\ell_p\) with \(\ell_p=\varsigma_p+w_j\) for \(p<a\); \(\ell_p=\lfloor t/2\rfloor-(p-a)\) for \(a\le p<a+t\); \(\ell_p=\varsigma_{p-t}+w_j\) for \(p\ge a+t\). The column numbers of \(V_j\), \(c(i)=k^+(i)+k^-(r+t-i)\), are exactly its steps: \(L_p=L_{p+1}+2c(p+1)+2\). (For \(p<a\) only \(k^+\) is nonzero: the maximum in its definition is \(\varsigma_{p+1}\) if \(p+1<a\) and \(\lfloor t/2\rfloor-w_j\) if \(p+1=a\); for \(p\ge a\) only \(k^-\) is nonzero, it vanishes inside the block, and below it the minimum is decided in the same way.) Moreover \(L_a\) agrees with the doubled Harish-Chandra parameter at position \(a\): the number of columns of height in \((a,r+t)\) equals \(\sum_{1\le i<r+t}k^-(i)\), which cancels the determinant exponent. A decreasing list with the right steps that agrees with the parameter at one position is the parameter (Lean: `hcParameter_eq_of_steps`, cited). Subtracting \(2u-1\), with \(r\) and \(t\) odd, gives the stated entries.

*2.* Consider the [[proofs/grh/upper-objects/centre-system|centre system]] \(\mathcal C\) with the stem of the [[proofs/grh/upper-objects/grid-centres|grid \(Y\)]] and the single down centre \(d_{j-1}\) of value \(-w_j\) and length \(t\); it is separated with bound \(\Delta-t-2\ge500(r+(r+t))^3\), as a subsystem of a separated system. Here, as in the Lean statements, the integer vectors are the *doubled* parameters: "\(l\) is \(2\lambda_B\)" means that \(l/2\) is the parameter \(\lambda_B\) of the centre-system page. (i) The doubled target parameter \(2\varsigma\) on \(W_j\) is \(2\lambda_\emptyset\) with common sign \(1\): rank \(r\), lowering \(0\), entries the stem, and the centre counts for the entry of \(c\) (it is down and the entry lies below it) iff \(\beta(c)\ge a\), which is where the sign of \(W_j\) is \(-1\). (ii) The parameter \(l'-2u\) on \(V_j\) (all signs \(+\)) is \(2\lambda_{\{d_{j-1}\}}\) with common sign \(1\): rank \(r+t\); the lowering is \(1\) (doubled; \(r\) and \(1\) are odd) and by 1 the entries \(l'-2u+1\) are the stem and the block; all signs are \(+\) since no centre is outside. The [[proofs/grh/upper-objects/inserting-a-block-satisfies-the-block-rule|insertion theorem]] (down case) gives the block rule for \((2\varsigma,\,l'-2u)\) with \(\gamma=-w_j+\lfloor r/2\rfloor\), \(\gamma'=-w_j+\lfloor(r+t)/2\rfloor\). The block rule only involves the shifted entries \(l-2\gamma'+n'\) and \(l'-2\gamma+n\) (and the gaps), so replacing \(l'-2u\) by \(l'\) and \(\gamma\) by \(\gamma+u\) preserves it (Lean: `IsBlockRule.shift`); and \(\gamma+u=m-j\).

*3.* Correspondence is 2. Numbering: since \(\varsigma\) decreases in the basis number, for a vector \(c\) of sign \(+\) the vectors of sign \(+\) with larger \(\varsigma\) are those with smaller number, \(\beta(c)\) of them; for sign \(-\) the vectors of sign \(-\) with smaller \(\varsigma\) are those with larger number, \(r-1-\beta(c)\) of them. Vanishing: for \(i>a\), \(\varsigma_{i-1}+w_j\le-\Delta/2<\lfloor t/2\rfloor\), so the positive part in \(k^+(i)\) vanishes; for \(i>m-j\), \(r-i<a\), so \(\varsigma_{r-i}+w_j\ge\Delta/2>-\lfloor t/2\rfloor\) and \(k^-(i)=0\). \(\square\)

## Remarks

Consequently ([[proofs/grh/upper-objects/highest-vector-polynomial-is-an-edge|edge theorem]]) the Fock vector of the highest weight vector of \(V_j\) is an edge between the type kernels of \(W_j\) and \(V_j\).

## References

1. Lean: `New.Data.descentPair`, `New.Data.paramsCorrespond_descentPair`, `New.Data.fitsParams_descentPair` in `src/New/UpperBound/Objects/Rows.lean`.
