+++
id = "proofs/grh/onelift-comparison/adjoint-of-hecke-polynomial"
title = "Adjoint of the Hecke polynomial operator for the conjugate pairings"
kind = "lemma"
summary = "For the pairing at an automorphism sigma, the adjoint of the Hecke polynomial at a split place w is the Hecke polynomial at the conjugate place with conjugated argument."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.exists_invariant_pairing_eq_innerAt", "New.LevelPlaces.LevelForm.innerAt_heckePolyOnForms"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
proof_status = "outline"
+++

Let \(E\) be a [[?c:CM field|CM field]] with a fixed [[?c:CM type|CM type]], let \(r,n\) be finite index sets with \(\lvert r\rvert<\lvert n\rvert\), and let \(O\) be a [[?lean:New.DescentPair|descent pair]]: a [[?c:Hermitian space|hermitian space]] \(W\) of rank \(\lvert r\rvert\) over \(E\), the standard definite space \(V=I_n\) of rank \(\lvert n\rvert\), an injection \(\operatorname{incl}\colon r\hookrightarrow n\), two finite sets of split finite places \(M\) (the chosen places) and \(Q\) (the places of the twist), and a character \(\mu\) of \(U(1)(\mathbb{A})\) with tame parts \(\psi_w\), characters of the [[algebra-commutative/residue-field|residue fields]] \(k_w\), trivial for \(w\notin M\cup Q\).

For \(\sigma\in\operatorname{Aut}(\mathbb{C})\) let \(\langle\varphi,\varphi'\rangle_\sigma\) be the [[?lean:New.LevelPlaces.LevelForm.innerAt|pairing at \(\sigma\)]] on forms on \(V\): \(\sigma^{-1}\) applied to the inner product of the \(\sigma\)-conjugates of \(\varphi,\varphi'\). It is linear in \(\varphi'\) and semilinear in \(\varphi\) for the automorphism \(c_\sigma=\sigma^{-1}\circ\overline{\phantom{x}}\circ\sigma\). For a finite place \(w\ne\bar w\) with \(w,\bar w\notin M\cup Q\cup\overline{M\cup Q}\) and \(X\in\mathbb{C}\) let
\[
H_w(X)=\sum_{i}(-X)^i q_w^{i(i-1)/2}\,T_{w,i}
\]
be the [[?lean:New.DescentPair.heckePolyOnForms|Hecke polynomial operator]] on forms on \(V\), with \(T_{w,i}\) the [[?c:Hecke operator|Hecke operators]] at \(w\) and \(q_w\) the norm of \(w\).

**Lemma.**

1. \(\langle\ ,\ \rangle_\sigma\) is the restriction to the forms of level \(K\) of a pairing \(B\) on all smooth forms of the same weight, \(c_\sigma\)-semilinear in the first variable and linear in the second, that is invariant under right translation by every \(g\in U(V)(\mathbb{A}_f)\).
2. For all forms \(\varphi,\varphi'\) and \(X\in\mathbb{C}\):
\[
\langle H_w(X)\varphi,\varphi'\rangle_\sigma=\langle\varphi,H_{\bar w}(c_\sigma(X))\varphi'\rangle_\sigma,\qquad c_\sigma(X)=\sigma^{-1}\bigl(\overline{\sigma(X)}\bigr).
\]

## Proof

1. Let \(G_\sigma\) be the \(c_\sigma\)-sesquilinear form on \(\mathbb{C}^{\mathcal I}\) with the (integral, hence \(\sigma\)-fixed) Gram matrix of the weight. Applying \(\sigma\) to \(G_\sigma(\rho(\gamma)u,\rho(\gamma)v)\) gives the Gram pairing of the \(\sigma\)-conjugate representation on the conjugate vectors, which is invariant; so \(G_\sigma\) is \(\rho\)-invariant. Let \(B\) be the index of the level times the smooth pairing built from \(G_\sigma\) ([[?lean:New.smoothPairing|pairing of smooth forms]]), which is translation invariant. By definition \(\langle\ ,\ \rangle_\sigma\) is its restriction.

2. Both forms are spherical at \(w\) and \(\bar w\). For a translation-invariant sesquilinear pairing, the adjoint of the double-coset operator \(T_{w,i}\) on vectors spherical at \(w\) is the operator of the inverse double coset, which for the unitary group at a split place is \(T_{\bar w,i}\); the scalar \((-X)^iq^{i(i-1)/2}\) moves across as \(c_\sigma\) of itself, and \(q\) is rational. This step is the general lemma [[?lean:New.heckePolyOp_adjoint|adjoint of the Hecke polynomial operator]], which is only cited here.

## References

1. Lean: `New.DescentPair.exists_invariant_pairing_eq_innerAt`, `New.LevelPlaces.LevelForm.innerAt_heckePolyOnForms` in `src/New/OneLift/TestedForms.lean`.
