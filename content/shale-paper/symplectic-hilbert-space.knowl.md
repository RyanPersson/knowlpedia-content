+++
id = "shale-paper/symplectic-hilbert-space"
title = "Symplectic Hilbert Space (K,B)"
kind = "definition"
summary = "A real Hilbert space with a continuous skew form, weakly or strongly nondegenerate according to convention."
aliases = ["symplectic-hilbert-space", "Symplectic Hilbert Space (K,B)"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/symplectic-hilbert-space.md"
+++

A **weak symplectic Hilbert space** is a real
[[linear-algebra/hilbert-space|Hilbert space]] \(K\) equipped with a continuous,
skew-symmetric bilinear form \(B:K\times K\to\mathbb R\) such that
\[
B(x,y)=0\ \text{for every }y\in K\quad\Longrightarrow\quad x=0.
\]
Thus \(B\) is a continuous [[shale-paper/symplectic-form|symplectic form]] in
the algebraic sense.

## Strong versus weak nondegeneracy

The form defines a bounded operator
\[
B^\flat:K\longrightarrow K^*,\qquad
B^\flat(x)=B(x,\mathord{-}).
\]
Weak nondegeneracy says that \(B^\flat\) is injective. The symplectic form is
**strong** if \(B^\flat\) is an isomorphism of Banach spaces. These conditions
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
[[shale-paper/symplectic-group-spk|\(\operatorname{Sp}(K)\)]].
