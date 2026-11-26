+++
id = "proofs/grh/derivatives-divisibility/field-setting"
title = "The field E = K(zeta) and its group of infinite places"
kind = "notation"
summary = "Notation for the parameters q0 and d, the CM field E generated over K by a root of unity of order q1, and the group of its infinite places."
aliases = ["group of infinite places of E", "place named by an integer"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = []
lean_files = ["src/New/Derivatives/Field/PrimeDecomposition.lean", "src/New/Derivatives/Field/WeilData.lean"]
+++

**Notation (the field \(E\)).** The [[?lean:New.Parameters|parameters]] \(P\) are a multiple \(q_0\) of \(18480=16\cdot3\cdot5\cdot7\cdot11\) and a prime \(d\) such that \(q_0\) divides \(2(d+1)\) but not \(d+1\); then \(d\equiv 7\pmod 8\). For an integer \(s\ge 0\) (the level) put
\[
q_1=q_0\cdot 3^{\lfloor\log_3 s\rfloor+5}\cdot 2^{s},\qquad K=\mathbb{Q}(\sqrt{-d})\subset\mathbb{C},\qquad E=K(\zeta),
\]
where \(\zeta\) is a chosen [[algebra-fields-galois/primitive-root-of-unity|primitive \(q_1\)-th root of unity]] (with the convention \(\lfloor\log_3 0\rfloor=0\)). Then \(E\) is a [[?c:CM field|CM field]], abelian over \(\mathbb{Q}\); \(x\mapsto\bar x\) denotes its complex conjugation, and \(\mathcal{O}_E\) its [[algebra-fields-galois/ring-of-integers|ring of integers]].

* \(\Phi\) is the set of [[?c:infinite place of a number field|infinite places]] of \(E\). A fixed embedding \(\Phi_1\colon E\to\mathbb{C}\) over \(K\) gives the bijection \(\operatorname{Gal}(E/K)\to\Phi\), \(g\mapsto\) (place of \(\Phi_1\circ g\)); through it \(\Phi\) is a commutative group, with isomorphisms
\[
\Phi\;\xrightarrow{\;v\mapsto\sigma_v\;}\;\operatorname{Gal}(E/K)\;\xrightarrow{\;\sim\;}\;(\mathbb{Z}/q_1)^\times ,\qquad \sigma_v(\zeta)=\zeta^{a}\ \text{ if } v\mapsto a .
\]
* \(\Phi_v=\Phi_1\circ\sigma_v\colon E\to\mathbb{C}\) is the embedding chosen at the place \(v\); it restricts to the inclusion on \(K\), and \(\Phi_{uv}=\Phi_u\circ\sigma_v\). The family \((\Phi_v)\) is the [[?c:CM type|CM type]] of \(E\).
* For an integer \(\nu\), the **place named by \(\nu\)** is the element of \(\Phi\) that corresponds to the class of \(\nu\) in \((\mathbb{Z}/q_1)^\times\) if \(\nu\) is prime to \(q_1\), and the identity otherwise.
* A **finite place** \(w\) of \(E\) is a nonzero prime ideal of \(\mathcal{O}_E\); \(\bar w\) is its complex conjugate, and \(N w\) its [[algebra-fields-galois/ideal-norm|absolute norm]]. A finite place lies **above** the prime \(p\) if \(p\in w\).

Two facts about the parameters are used: every prime that divides \(q_1\) divides \((d+1)/4\) and satisfies \(\chi_K=1\) (it splits in \(K\)); and \(q_1\) is prime to \(d\).

## References

1. Lean: `New.Parameters`, `New.Parameters.q₁`, `New.Parameters.E`, `New.Parameters.Φ`, `New.Parameters.galOfPlace`, `New.Parameters.placeOfInt`, `New.Parameters.ζ`, `New.Parameters.chiK_eq_one_of_dvd`, `New.Parameters.dvd_d_add_one_div_four_of_dvd_q₁` in `src/New/Reduction/Data/FieldsAndPlaces.lean`.
