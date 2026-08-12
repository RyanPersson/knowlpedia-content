+++
id = "langlands-letter/knowls/maximal-torus-weight-lattice"
title = "Maximal torus, character lattice, and weights"
kind = "knowl"
summary = "A maximal torus with its geometric character and cocharacter lattices, carrying a Galois action over a nonsplit field."
aliases = ["maximal-torus-weight-lattice", "Maximal Torus and Weight Lattice"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/maximal-torus-weight-lattice.md"
section_mode = "progressive"
+++

A **torus** over a field \(k\) is an
[[algebraic-geometry-foundations/algebraic-group|algebraic \(k\)-group]]
\(T\) such that \(T_{\overline k}\simeq\mathbb G_m^r\) over an
[[algebra-fields-galois/algebraic-closure|algebraic closure]]. It is
**split** if this isomorphism
already exists over \(k\). A **maximal torus** \(T\subset G\) is a torus not
properly contained in another torus of \(G\).

The geometric character and cocharacter lattices are

\[
X^*(T)=
\operatorname{Hom}_{\overline k\text{-grp}}
(T_{\overline k},\mathbb G_m),
\qquad
X_*(T)=
\operatorname{Hom}_{\overline k\text{-grp}}
(\mathbb G_m,T_{\overline k}).
\]

They are dual finite free [[algebra-groups/abelian-group|abelian groups]]
with a natural action of the
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois group]]
\(\Gamma_k\). The characters defined over \(k\) are
\(X^*(T)^{\Gamma_k}\), not generally all of \(X^*(T)\).

## Weights

For a representation of \(G_{\overline k}\), its weights are characters in
\(X^*(T)\). The abstract [[lie-groups/weight-lattice|weight lattice]] of the [[lie-groups/root-system|root system]] can be larger
than the actual character lattice of \(T\); the intermediate lattice records
the
[[langlands-letter/knowls/root-vs-weight-lattice-isogeny|isogeny form]] of a
semisimple group.

## Example

For the diagonal torus in \(\operatorname{GL}_n\),

\[
X^*(T)\simeq\mathbb Z^n,
\qquad
(m_i)\longmapsto
\left(\operatorname{diag}(t_i)\mapsto\prod_i t_i^{m_i}\right).
\]

## Langlands role

The full [[langlands-letter/knowls/roots-weights-weyl|based root datum]] uses
both \(X^*(T)\) and \(X_*(T)\). Exchanging them, and
[[langlands-letter/knowls/coroots-and-pairing|roots with coroots]], defines
the
[[langlands-letter/knowls/langlands-dual-group|Langlands dual group]].

## References

1. A. Borel, *Linear Algebraic Groups*, second edition, Springer, 1991.
