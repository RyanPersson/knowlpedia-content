+++
id = "functional-analysis/symplectic-hilbert-space"
title = "Symplectic Hilbert Space (K,B)"
kind = "definition"
summary = "A real Hilbert space with a continuous skew form, weakly or strongly nondegenerate according to convention."
aliases = ["symplectic-hilbert-space", "Symplectic Hilbert Space (K,B)"]
domains = ["functional-analysis"]
legacy_source_path = "shale-paper/symplectic-hilbert-space.md"
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/symplectic-form", "linear-algebra/bilinear-form"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **weak symplectic [[linear-algebra/hilbert-space|Hilbert space]]** is a real
[[linear-algebra/hilbert-space|Hilbert space]] \(K\) equipped with a continuous,
skew-symmetric [[linear-algebra/bilinear-form|bilinear form]] \(B:K\times K\to\mathbb R\) such that
\[
B(x,y)=0\ \text{for every }y\in K\quad\Longrightarrow\quad x=0.
\]
Thus \(B\) is a continuous [[linear-algebra/symplectic-form|symplectic form]] in
the algebraic sense.

## Strong versus weak nondegeneracy

The form defines a [[functional-analysis/bounded-linear-operator|bounded operator]]
\[
B^\flat:K\longrightarrow K^*,\qquad
B^\flat(x)=B(x,\mathord{-}).
\]
Weak nondegeneracy says that \(B^\flat\) is injective. The [[linear-algebra/symplectic-form|symplectic form]] is
**strong** if \(B^\flat\) is an isomorphism of [[linear-algebra/banach-space|Banach spaces]]. These conditions
coincide in finite dimensions but not in infinite dimensions. Authors who use
“symplectic Hilbert space” without a qualifier may mean either the weak or the
strong notion, so the convention must be stated.

## Shale's setting

If \(H\) is a complex Hilbert space, its underlying real Hilbert space \(H_{\mathbb R}\) becomes symplectic with
\[
B(z_1,z_2)=\operatorname{Im}\langle z_1,z_2\rangle.
\]
This form is strong: multiplication by \(i\), together with the real Riesz
isomorphism, identifies \(H_{\mathbb R}\) continuously with its dual. Its
bounded real-linear symplectic automorphisms form
[[lie-groups/symplectic-group-spk|\(\operatorname{Sp}(K)\)]].
