+++
id = "proofs/grh/determinant-exchange/hecke-polynomial-of-theta-lift"
title = "Hecke polynomial of the theta lift of a descent pair"
kind = "lemma"
summary = "At a split place off the level, the lift of a spherical eigenform is spherical, with Hecke polynomial a q-Pochhammer factor of rank t times the rescaled polynomial of the form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.hasHeckePolynomial_thetaLift"]
lean_files = ["src/New/Determinant/Norms/AdjointThetaLift.lean"]
proof_status = "outline"
+++

**Lemma.** Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with spaces \(W\) of rank \(r\ge1\) and \(V=I_n\), and \(t=n-r\). Let \(l\) fit the pair and let \(y\) be a form on \(W\) of parameter \(l\). Let \(w\) be a finite place of \(E\) that is split over the maximal totally real subfield (\(\bar w\neq w\)) and such that neither \(w\) nor \(\bar w\) is a chosen place or a place of the twist. Suppose that \(y\) [[?lean:New.HasHeckePolynomial|has Hecke polynomial]] \(p\) at \(w\): it is spherical at \(w\) and the [[?c:Hecke operator|Hecke]] polynomial operator \(H_w(X)\) acts on it by the scalar \(p(X)\) for every \(X\in\mathbb{C}\). Then the [[proofs/grh/determinant-exchange/theta-lift-of-descent-pair|theta lift]] \(\Theta_Wy\), as a function on \(U(V)(\mathbb{A}_f)\), has at \(w\) the Hecke polynomial
\[
X\longmapsto\prod_{i=0}^{t-1}\bigl(1-q^{i}\alpha X\bigr)\cdot p\bigl(q^{t}\alpha\beta^{-1}X\bigr),
\]
where \(q\) is the norm of \(w\) and \(\alpha\), \(\beta\) are the [[?lean:New.AutChar.frobValue|Frobenius values]] at \(w\) of the characters \(\nu_W\) (in rank \(r\)) and \(\nu_V\) (in rank \(n\)) of the pair.

## Proof

Outline. At \(w\) both characters are unramified: \(\nu_W\) is a power of the character of the Weil data, and the tame part of the character of the pair is trivial off the places of the pair, at \(w\) and at \(\bar w\). The finite datum is the block datum at the places of the pair and the vacuum elsewhere, so the datum \(\varphi_{\xi_0}\) is fixed by the projection to the vacuum at \(w\). With these three facts the statement is the transfer of Hecke polynomials under a theta lift with unramified data, [[?lean:New.SiegelWeil.hasHeckePolynomial_formLift|Hecke polynomial of a lift]], applied to the arrow \(\varphi_{\xi_0}\), followed by the compatibility of the isomorphism between functions on \(U(V)(\mathbb{A})\) and algebraic forms with Hecke operators. The transfer theorem itself is not reproved here.

## References

1. Lean: `New.DescentPair.hasHeckePolynomial_thetaLift` in `src/New/Determinant/Norms/AdjointThetaLift.lean`.
