+++
id = "proofs/grh/spanning-core/translation-as-a-hecke-operator"
title = "Translations off the level as Hecke operators"
kind = "lemma"
summary = "The matrix coefficients between forms of principal level of a translation by an element trivial at the chosen places are those of a spherical Hecke operator, the same for all spaces."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.exists_heckeAlgebra_inner_eq_inner_translate"]
lean_files = ["src/New/Spanning/Multiplicities/EqualMultiplicities.lean"]
proof_status = "full"
+++

**Lemma.** Let \(D\) be admissible data and \(\gamma\in G^M\) an element of the [[proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level|off-level group]]. There is \(p\) in the spherical Hecke algebra away from \(M\) such that for every hermitian space \(W\) of rank \(r\) over \(E\) and all forms \(z,y\) of principal level on \(W\),
\[
\langle z,\ p_W\,y\rangle=\langle z,\ \gamma\cdot y\rangle ,
\]
where \(\gamma\cdot y\) is the translate of \(y\) under the [[?lean:New.Space.formRep|action of \(G_f\) on forms]] and \(\langle\ ,\ \rangle\) is the Petersson product.

## Proof

Let \(K=K_0\cap G^M\), a subgroup of \(G^M\). The group \(G^M\) is closed in \(G_f\) (an intersection of the closed conditions "component at \(w\) is \(1\)"), so \(K\) is compact; and \(\gamma K\gamma^{-1}\cap G^M\) is open in \(G^M\). Hence \(H=K\cap\gamma K\gamma^{-1}\) has finite index in \(K\). Put
\[
a=\sum_{kH\in K/H}k\gamma\ \in\mathbb{C}[G^M] ,
\]
with a fixed representative \(k\) of each coset.

*\(a\) is spherical.* Let \(\rho\) be a representation of \(G^M\) and \(y\) a \(K\)-fixed vector. For \(k\in K\), \(h\in H\) we have \(\gamma^{-1}h\gamma\in K\), so \(\rho(kh\gamma)y=\rho(k\gamma)\rho(\gamma^{-1}h\gamma)y=\rho(k\gamma)y\): the vector \(\rho(k\gamma)y\) depends only on the coset \(kH\). Therefore left translation by an element of \(K\) permutes the terms of \(\rho(a)y=\sum_{kH}\rho(k\gamma)y\), which is thus \(K\)-fixed. By the criterion (Property 2) for the [[proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level|spherical algebra]], \(a\in\mathcal S\), and \(a\) defines \(p'\in\mathcal H\).

*Matrix coefficients.* Let \(z,y\) be forms of principal level on \(W\). Every \(k\in K\) lies in \(J_M\) (as \(K_0\cap G^M\subseteq J_M\)), so it fixes \(z\); the action is unitary, hence \(\langle z,k\gamma y\rangle=\langle k^{-1}z,\gamma y\rangle=\langle z,\gamma y\rangle\). Summing, \(\langle z,p'_Wy\rangle=[K:H]\,\langle z,\gamma y\rangle\). Take \(p=[K:H]^{-1}p'\). \(\blacksquare\)

## References

1. Lean: `New.Data.exists_heckeAlgebra_inner_eq_inner_translate` in `src/New/Spanning/Multiplicities/EqualMultiplicities.lean`.
