+++
id = "langlands-letter/knowls/coroots-and-pairing"
title = "Coroots and the Weight–Coroot Pairing"
kind = "knowl"
summary = "Coroots and their integer pairing with weights, which control dominance and root-system duality."
aliases = ["coroots-and-pairing", "Coroots and the Weight–Coroot Pairing"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/coroots-and-pairing.md"
+++

For a root \(\alpha\in \Phi\subset X^*(T)\), the associated **coroot** is the distinguished cocharacter \(\alpha^\vee\in X_*(T)\) in the root datum. A weight \(\lambda\in X^*(T)\) pairs with it by composition:
\[
\lambda\circ\alpha^\vee:\mathbb G_m\longrightarrow\mathbb G_m,
\qquad
z\longmapsto z^{\langle\lambda,\alpha^\vee\rangle},
\]
which defines the integer \(\langle\lambda,\alpha^\vee\rangle\). In particular,
\(\langle\alpha,\alpha^\vee\rangle=2\).

## Lie-algebra interpretation

Differentiating \(\alpha^\vee\) gives \(H_\alpha=d\alpha^\vee(1)\) in the split Cartan Lie algebra. With the standard identification of differentials, \(d\lambda(H_\alpha)=\langle\lambda,\alpha^\vee\rangle\).

## Remarks

**Key uses:**
- Dominance: \(\lambda\) is dominant iff \(\langle \lambda,\alpha^\vee\rangle\ge 0\) for all simple \(\alpha\) (see [[langlands-letter/knowls/roots-weights-weyl|dominant weights]]).
- Duality: swapping roots and coroots produces the [[langlands-letter/knowls/langlands-dual-group|dual group]].
