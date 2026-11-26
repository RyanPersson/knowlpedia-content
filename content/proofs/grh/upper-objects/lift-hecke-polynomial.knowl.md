+++
id = "proofs/grh/upper-objects/lift-hecke-polynomial"
title = "Hecke polynomial of a lift"
kind = "definition"
summary = "The Hecke polynomial operator on the forms on V of a descent pair at a split place off the level, and the condition that a form has the Hecke polynomials of a theta lift of a given eigensystem."
aliases = ["Hecke polynomial of a lift", "has lift Hecke polynomial"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.heckePolyOnForms", "New.DescentPair.heckePolyOnForms_eq_smul", "New.DescentPair.liftHeckeRoot", "New.DescentPair.HasLiftHeckePolynomial"]
lean_files = ["src/New/UpperBound/Objects/AuxiliaryPair.lean"]
+++

Let \(O\) be a [[proofs/grh/upper-objects/descent-pair|descent pair]] with ranks \(r<n\), \(t=n-r\), forms \(\mathcal F_V(O)\), and characters \(\nu_W,\nu_V\). Let \(w\) be a split finite place of \(E\) (\(\bar w\ne w\)) such that neither \(w\) nor \(\bar w\) is a place of \(M\) or \(Q\); let \(q\) be its norm.

**Definition.** The **Hecke polynomial operator** at \(w\) and \(X\in\mathbb C\) is the endomorphism
\[
H_w(X)=\sum_{i\le n}(-X)^i q^{i(i-1)/2}\,T_{w,i}
\]
of \(\mathcal F_V(O)\), where \(T_{w,i}\) are the [[?lean:New.heckePolyOp|Hecke operators at the split place \(w\)]] (they preserve the level and its character because the forms are spherical at \(w\)).

Let \(z\) assign to every finite place \(w\) a sequence \(z(w)\colon\mathbb N\to\mathbb C\) (Hecke eigenvalues in rank \(r\)). A form \(y\in\mathcal F_V(O)\) **has the Hecke polynomials of a lift of \(z\)** if for every such \(w\), \(y\) is spherical at \(w\) and \(H_w(T)\,y=p_w(T)\,y\) for all \(T\in\mathbb C\) ([[?lean:New.HasHeckePolynomial|has Hecke polynomial]] \(p_w\)), where
\[
p_w(T)=\prod_{l<t}\big(1-q^l\,\nu\,T\big)\cdot H_{z(w)}\!\Big(\frac{q^{t}\,\nu}{\nu'}\,T\Big),
\]
\(H_{z(w)}\) is the rank \(r\) [[?lean:New.heckePolyEval|Hecke polynomial with eigenvalues \(z(w)\)]], and \(\nu,\nu'\) are the [[?lean:New.AutChar.frobValue|Frobenius values]] at \(w\) of \(\nu_W\) in rank \(r\) and of \(\nu_V\) in rank \(n\).

The **Hecke root of the lift** at \(w\) is \(\big(\nu\,q^{\,t-1}\big)^{-1}\), the inverse of the largest root factor of the first product.

## Remarks

If \(y\) has Hecke polynomial \(p\) at \(w\) as a function on the finite adelic points, then \(H_w(X)y=p(X)y\) in \(\mathcal F_V(O)\), since the inclusion of algebraic forms into functions commutes with the Hecke operators. The first product is the [[?lean:New.SiegelWeil.qPochhammer|\(q\)-Pochhammer product]] \(\prod_{l<t}(1-q^l x)\) at \(x=\nu T\).

## References

1. Lean: `New.DescentPair.heckePolyOnForms`, `New.DescentPair.liftHeckeRoot`, `New.DescentPair.HasLiftHeckePolynomial` in `src/New/UpperBound/Objects/AuxiliaryPair.lean`.
