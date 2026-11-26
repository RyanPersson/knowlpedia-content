+++
id = "proofs/grh/onelift-comparison/point-form"
title = "Class forms and point forms"
kind = "definition"
summary = "The form on the definite space supported on one class with a given vector value, at a point moved by a point lift."
aliases = ["class form", "point form"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Rows.classForm", "New.Rows.pointForm"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with a fixed [[?c:CM type|CM type]], let \(r,n\) be finite index sets with \(\lvert r\rvert<\lvert n\rvert\), and let \(O\) be a [[?lean:New.DescentPair|descent pair]]: a [[?c:Hermitian space|hermitian space]] \(W\) of rank \(\lvert r\rvert\) over \(E\), the standard definite space \(V=I_n\) of rank \(\lvert n\rvert\), an injection \(\operatorname{incl}\colon r\hookrightarrow n\), two finite sets of split finite places \(M\) (the chosen places) and \(Q\) (the places of the twist), and a character \(\mu\) of \(U(1)(\mathbb{A})\) with tame parts \(\psi_w\), characters of the [[algebra-commutative/residue-field|residue fields]] \(k_w\), trivial for \(w\notin M\cup Q\).

Let \(\rho\) be the irreducible algebraic representation of \(U(V)\) on \(\mathbb{C}^{\mathcal{I}}\) given by the weight of \(O\) (column counts and determinant exponents), \(K\subset U(V)(\mathbb{A}_f)\) the level group of \(O\) and \(\lambda\colon K\to\mathbb{C}^\times\) its level character, so that the [[?lean:New.DescentPair.FormV|forms on \(V\)]] are the functions \(\varphi\colon U(V)(\mathbb{A}_f)\to\mathbb{C}^{\mathcal I}\) with \(\varphi(\gamma hk)=\lambda(k)\rho(\gamma)\varphi(h)\) for rational \(\gamma\) and \(k\in K\) (an [[?c:Algebraic modular form|algebraic modular form]]).

For \(h\in U(V)(\mathbb{A}_f)\) and \(v\in\mathbb{C}^{\mathcal I}\) the **class form** \(\delta_h(v)\) is the form
\[
\delta_h(v)(y)=\sum_{\gamma}\lambda(h^{-1}\gamma y)\,\rho(\gamma)^{-1}v ,
\]
the sum over the rational points \(\gamma\in U(V)(\mathbb{Q})\) with \(h^{-1}\gamma y\in K\) (a finite sum, as \(V\) is definite). It is supported on the class \(U(V)(\mathbb{Q})\,h\,K\), and \(v\mapsto\delta_h(v)\) is linear.

For matrices \(Y_w\in k_w^{n\times r}\) (\(w\in M\)) of full column rank and an injection \(e\colon r\hookrightarrow n\), the **point form** is
\[
\delta_{h,Y,e}(v)=\delta_{hA_{Y,e}}(v),
\]
where \(A_{Y,e}\) is the [[proofs/grh/onelift-comparison/point-lift|point lift]] of \((Y,e)\).

## References

1. Lean: `New.Rows.classForm`, `New.Rows.pointForm` in `src/New/OneLift/TestedForms.lean`.
