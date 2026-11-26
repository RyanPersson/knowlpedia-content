+++
id = "proofs/grh/derivatives-vacuum/divisibility-of-derivatives-along-minors"
title = "Divisibility of derivatives of standard data along products of minors and Schur entries"
kind = "theorem"
summary = "At a non-split prime the jets of standard data of level one on a space of matrices, along products of minors and along entries of Schur matrices, have the predicted divisibility up to an explicit loss, also with erased columns and charges."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Parameters.norm_jet_minorProd_jetSeries_le", "New.Parameters.norm_schurJet_jetSeries_le_of_charges"]
lean_files = ["src/New/Derivatives/Vacuum/Divisibility.lean"]
proof_status = "outline"
+++

Let \(n,n'\) be finite sets, \(V=\operatorname{Hom}\) of the [[?lean:New.stdSpace|standard spaces]] of index sets \(n\) and \(n'\) over \(E\) (the space of \(n'\times n\) matrices; the variable \((\tau,b,a)\) of its jet series is the entry \((b,a)\) of the matrix \(z_\tau\)). Let \(p\) be a prime with \(\chi_K(p)\ne1\), \(\iota_p\) a \(p\)-adic place, \(f\) [[proofs/grh/derivatives-vacuum/standard-data|standard data]] of level \(1\) at \(p\) on \(V\), \(c\in\mathbb{C}\) with \(\lvert\iota_pc\rvert_p\le1\), and \(F=J_{c\lambda}(f)\). Let \(\kappa_\tau(h)\) be the number of columns of height \(h\) of a diagram at each infinite place \(\tau\), \(N=\lvert n'\rvert\), \(B\) the [[?lean:New.boxes|number of boxes]] of \(\kappa\) in columns of height \(<N\), and \(f_0\) the number of infinite places of \(E\). Put \(\mathrm{loss}=f_0N^3\bigl(1+\log_p\max(B,1)\bigr)\).

**Theorem.**

1. For every standard filling \(i'\) of \(\kappa\) by elements of \(n'\) ([[?lean:New.WeylIndex|Weyl index]]) and all matrices \(y_\tau\) with entries in \(\mathcal{O}_{\mathbb{C}_p}\) (rows indexed by \(n\)), the jet of \(\iota_pF\) along the [[?lean:New.minorProd|product of minors]] of \(i'\) and \(y\) has absolute value at most
\[ p^{-(D(\kappa)-\mathrm{loss})}, \]
where \(D(\kappa)\) is the [[?lean:New.predictedDivisibility|predicted divisibility]] of \(\kappa\) at \(p\) for the partner map of \(p\) and the bound \(N\).
2. Suppose \(\kappa\) [[?lean:New.FitsRanks|fits the ranks]] \(n,n'\). Let \(S\) be a finite set of infinite places (erased places) and \(\chi(\tau,h,b)\in\mathbb{N}\) charge exponents such that for every partner exponent \(e\) the [[?lean:New.IsChargeExponent|charge condition]] holds for the partner map of \(e\). Then for all Weyl indices \(i'\) (in \(n'\)) and \(i\) (in \(n\)), the [[?lean:New.schurJet|Schur jet]] of \(F\) at the entry \((i',i)\) satisfies
\[ \bigl\lvert\iota_p\,\mathrm{schurJet}_\kappa(F)_{i',i}\bigr\rvert_p\le p^{\,\chi(i')-\bigl(D(\kappa^{S})+\gamma'_p\,(B-B^{S})-\mathrm{loss}\bigr)}, \]
where \(\chi(i')\) is the [[?lean:New.fillingCharge|filling charge]] of \(i'\), \(\kappa^{S}\) is \(\kappa\) with the columns of height one [[?lean:New.eraseHeightOne|erased]] at the places of \(S\), \(B^S\) its number of boxes in columns of height \(<N\), and \(\gamma'_p\) is the [[?lean:New.gammaPrime|gain per box]].

## Proof

By [[proofs/grh/derivatives-vacuum/normal-form-of-standard-data|the normal form of standard data]], \(\iota_pF\) has the normal form with \(\lvert\varpi_p\rvert_p=p^{-v}\).

1 is then the count of the divisibility of series in normal form of the chapter on derivatives that count primes ([[?lean:New.Parameters.norm_jet_minorProd_le_of_hasNormalForm|divisibility along products of minors]]; not reproved here).

2. A Schur entry is bounded by a jet along a product of minors: there are integral matrices \(y\) with \(\lvert\mathrm{schurJet}_\kappa(\iota_pF)_{i',i}\rvert\le\lvert\)jet of \(\iota_pF\) along the minor product of \(i'\), \(y\rvert\) ([[?lean:New.exists_norm_schurJet_le_norm_jet_minorProd|Schur entries and minors]]), and \(\iota_p\) commutes with the Schur jet. Then apply the version of the count with erased places and charges ([[?lean:New.Parameters.norm_jet_minorProd_le_of_charges|divisibility with charges]]). Both cited results belong to another area and are not reproved here.

## References

1. Lean: `New.Parameters.norm_jet_minorProd_jetSeries_le`, `New.Parameters.norm_schurJet_jetSeries_le_of_charges` in `src/New/Derivatives/Vacuum/Divisibility.lean`.
