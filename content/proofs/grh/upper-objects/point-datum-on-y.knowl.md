+++
id = "proofs/grh/upper-objects/point-datum-on-y"
title = "Levels, theta kernels and point data along the spaces Y_j"
kind = "definition"
summary = "For a tame character: the level of U(Y_j) principal at the chosen places and at Q, the theta kernel of the pair (Y_j, Y_{j+1}), and the datum that is the indicator of the inclusion at the level places and the vacuum elsewhere, with its transformation law."
aliases = ["point datum", "level of Y_j"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.inclY", "New.Data.levelY", "New.Data.levelY_le_chosenLevel", "New.Data.LevelReductionsY", "New.Data.pointDatumY", "New.Data.thetaKernelY", "New.Data.chainTamePart", "New.Data.liftTamePart_eq_of_mem_Q", "New.Data.thetaKernelY_omega_pointDatumY_eq_smul", "New.Data.isHCParam_paramY", "New.Data.card_Y_le"]
lean_files = ["src/New/UpperBound/Objects/Rows.lean"]
+++

Let \(D\) be admissible data, \(\vartheta\) a tame character with places \(Q\), and \(Y_j\) the [[proofs/grh/upper-objects/spaces-y-and-w|spaces \(Y_j\)]]; the index set of \(Y_j\) is the first summand of that of \(Y_{j+1}\).

**Definition.**

* The **level of \(Y_j\)** is the group \(K_{Y_j}(\vartheta)\) of the integral finite adelic points of \(U(Y_j)\) reducing to \(1\) at every level place (the chosen places and the places of \(Q\)). It is contained in the chosen level.
* The **theta kernel of \((Y_j,Y_{j+1})\)** is the [[?lean:New.pairThetaKer|theta kernel of the pair]] with the characters \(\nu\upsilon^{\lfloor n/2\rfloor}\) for the two ranks \(n\), where \(\nu=\mu^0_{j+1}\vartheta^{j+1}\) is the [[?lean:New.Data.chainChar|chain character]] of lift \(j+1\).
* The **point datum** \(\Upsilon_{j+1}\) on \(\operatorname{Hom}(Y_j,Y_{j+1})\): at the level places the indicator of the matrices congruent to the inclusion matrix modulo the product of these places, and the vacuum at the other finite places.

**Lemma.** Let \(k\), \(k'\) be integral finite points of \(U(Y_j)\), \(U(Y_{j+1})\) with reductions \(g,g'\) at the level places such that \(g'\iota=\iota g\) at each of them (\(\iota\) the inclusion matrix). Then
\[
\omega(k,k')\,\Upsilon_{j+1}=\prod_{w}\frac{\psi_w(\det g'_w)}{\psi_w(\det g_w)}\cdot\Upsilon_{j+1},
\]
the product over the level places, with \(\psi\) the tame part of \(\nu\).

**Lemma.** The doubled parameter of \(Y_m\) (see [[proofs/grh/upper-objects/grid-nodes|grid nodes]]) lists, in some order, the entries of twice the Harish-Chandra parameter of the weight \(\mu(Y_m)\) (column numbers \(c^Y_\tau\), determinant exponent \(\ell_m\)); for \(j\le m\) the rank of \(Y_j\) is at most \(n_m\).

## Proof

*First lemma.* Let \(\mathfrak m\) be the product of the level places. The hypothesis says \(g'\iota=\iota g\) at each level place, hence \(\bar k'^{-1}\,\iota\,\bar k=\iota\) modulo \(\mathfrak m\) by the Chinese remainder theorem for matrices. The Lean lemma `New.Exchange.pairWeil_modDatum_single` (cited) states: if the reductions of integral points \((k,k')\) fix a matrix \(y_0\) modulo \(\mathfrak m\) in this sense, then \(\omega(k,k')\) multiplies the datum (indicator of \(y_0\) at \(\mathfrak m\), vacuum elsewhere) by the value of the pair of characters at \((k,k')\). This value is \(\nu'(\det k')\,\nu(\det k)^{-1}\) for the two rank twists; on integral points a character with a weight is the product of its tame parts at the determinants of the reductions, and the tame part of \(\mu^0_{j+1}\vartheta^{j+1}\) is trivial off the level places.

*Second lemma.* Since \(m\) is even nothing is lowered at the node \((0,m)\), whose doubled entries are \(2\varsigma_y\) (\(y<r\)) and \([t]_b\)-blocks \(2[t]_b-2w_{l+1}\) (\(l<m\), \(b<t\)). By the [[proofs/grh/upper-objects/columns-of-the-weights|column description]] of \(\mu(Y_m)\), the sorted sequence \(2\lambda^{Y,\mathrm{sorted}}_p\), \(p<n_m-1\), is twice the Harish-Chandra parameter of the weight \((c^Y,\ell_m)\). Each entry of the node occurs in it: \(2\varsigma_y\) at position \(y\) if \(y+1<k\), and at position \(n_i-1\) if \(y=k-1+i\) (\(i<m\)); the entry \(b\) of block \(l+1\) at position \(n_l+b\). The entries of the node are distinct ([[proofs/grh/upper-objects/properties-of-grid-nodes|gap]]), and the two sets have the same number \(n_m-1\) of elements. The rank bound: \(r+jt\le r+mt\le k+m(t+1)\) since \(r+1=k+m\). \(\square\)

## References

1. Lean: `New.Data.levelY`, `New.Data.pointDatumY`, `New.Data.thetaKernelY`, `New.Data.thetaKernelY_omega_pointDatumY_eq_smul`, `New.Data.isHCParam_paramY` in `src/New/UpperBound/Objects/Rows.lean`.
