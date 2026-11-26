+++
id = "proofs/grh/onelift-comparison/point-lift"
title = "Point lift: an integral element with prescribed columns and rows"
kind = "lemma"
summary = "An element of the integral level with given columns at the chosen places and unit rows at the twist places exists."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Rows.IsPointLift", "New.Rows.exists_isPointLift", "New.Rows.pointLift", "New.Rows.isPointLift_pointLift"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
proof_status = "full"
+++

Let \(E\) be a [[?c:CM field|CM field]] with a fixed [[?c:CM type|CM type]], let \(r,n\) be finite index sets with \(\lvert r\rvert<\lvert n\rvert\), and let \(O\) be a [[?lean:New.DescentPair|descent pair]]: a [[?c:Hermitian space|hermitian space]] \(W\) of rank \(\lvert r\rvert\) over \(E\), the standard definite space \(V=I_n\) of rank \(\lvert n\rvert\), an injection \(\operatorname{incl}\colon r\hookrightarrow n\), two finite sets of split finite places \(M\) (the chosen places) and \(Q\) (the places of the twist), and a character \(\mu\) of \(U(1)(\mathbb{A})\) with tame parts \(\psi_w\), characters of the [[algebra-commutative/residue-field|residue fields]] \(k_w\), trivial for \(w\notin M\cup Q\).

For a field \(R\) and an injection \(u\colon r\hookrightarrow n\) write \(\iota_u\in R^{n\times r}\) for the inclusion matrix whose \(j\)-th column is the unit vector at \(u(j)\). For each \(w\in M\) let \(Y_w\in k_w^{n\times r}\) and let \(e\colon r\hookrightarrow n\) be an injection. An element \(k\) of the integral level \(\prod_v \mathrm{GL}_n(\mathcal{O}_v)\cap U(V)(\mathbb{A}_f)\) (the [[?lean:New.stdLevel|standard level]]) is a **point lift** for \((Y,e)\) if

1. \(k\) has component \(1\) at every finite place outside \(M\cup Q\) and their complex conjugates;
2. for \(w\in M\), the reduction \(\bar k_w\in\mathrm{GL}_n(k_w)\) satisfies \(\bar k_w\,\iota_{\operatorname{incl}}=Y_w\) (the columns \(\operatorname{incl}\) of \(\bar k_w\) are \(Y_w\));
3. for \(w\in Q\), \(\bar k_w^{\mathsf T}\,\iota_e=\iota_{\operatorname{incl}}\) (row \(e(j)\) of \(\bar k_w\) is the unit vector at \(\operatorname{incl}(j)\)).

**Lemma.** If every \(Y_w\) (\(w\in M\)) has full column rank, i.e. \(x\mapsto Y_wx\) is injective, then a point lift for \((Y,e)\) exists. One such element, chosen once and for all, is denoted \(A_{Y,e}\).

## Proof

Over a field, an \(n\times r\) matrix of full column rank is the first-columns block of an invertible matrix: for \(w\in M\) there is \(A_w\in\mathrm{GL}_n(k_w)\) with \(A_w\iota_{\operatorname{incl}}=Y_w\) (extend the \(r\) independent columns of \(Y_w\) to a basis and place them at the indices \(\operatorname{incl}\)). Likewise, since \(\iota_{\operatorname{incl}}\) has full column rank, for \(w\in Q\) there is \(B_w\in\mathrm{GL}_n(k_w)\) with \(B_w\iota_e=\iota_{\operatorname{incl}}\). The places of \(M\cup Q\) are split and pairwise non-conjugate, so the reduction map from the elements of the integral level supported on \(M\cup Q\) and conjugates to \(\prod_{w\in M\cup Q}\mathrm{GL}_n(k_w)\) is surjective ([[?lean:New.stdLevel.exists_reduceFamily_eq|surjectivity of reduction]]). Take \(k\) with reductions \(A_w\) at \(w\in M\) and \(B_w^{\mathsf T}\) at \(w\in Q\); then 2 and 3 hold by construction.

## References

1. Lean: `New.Rows.IsPointLift`, `New.Rows.exists_isPointLift`, `New.Rows.pointLift`, `New.Rows.isPointLift_pointLift` in `src/New/OneLift/TestedForms.lean`.
