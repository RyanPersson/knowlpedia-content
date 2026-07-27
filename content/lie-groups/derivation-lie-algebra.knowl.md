+++
id = "lie-groups/derivation-lie-algebra"
title = "Derivation of a Lie algebra"
kind = "knowl"
summary = "A linear map satisfying the Leibniz rule for the Lie bracket; derivations form a Lie algebra."
aliases = ["derivation-lie-algebra", "Derivation of a Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/derivation-lie-algebra.md"
+++

Let \(\mathfrak g\) be a [[lie-groups/lie-algebra|Lie algebra]] over a field. A **derivation** of \(\mathfrak g\) is a linear map \(D:\mathfrak g\to\mathfrak g\) satisfying

\[
D([x,y]) \;=\; [D x, y] + [x, D y].
\]
for all \(x,y\in\mathfrak g\). The space of derivations is denoted \(\operatorname{Der}(\mathfrak g)\).

## Lie algebra structure
With bracket given by the commutator of endomorphisms,
\[
[D_1,D_2] := D_1\circ D_2 - D_2\circ D_1,
\]
the space \(\operatorname{Der}(\mathfrak g)\) is a Lie subalgebra of \(\mathfrak{gl}(\mathfrak g)\).

## Inner vs. outer
For each \(x\in\mathfrak g\), the adjoint map \(\operatorname{ad}_x:\mathfrak g\to\mathfrak g\), defined by \(\operatorname{ad}_x(y)=[x,y]\), is a derivation. These are the [[lie-groups/inner-derivation|inner derivations]], and \(x\mapsto\operatorname{ad}_x\) is the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]].

Derivations not of the form \(\operatorname{ad}_x\) are [[lie-groups/outer-derivation|outer derivations]]; they measure the failure of \(\operatorname{ad}(\mathfrak g)\) to exhaust all infinitesimal symmetries.

## Motivation
Derivations are the infinitesimal analog of [[lie-groups/lie-algebra-automorphism|Lie algebra automorphisms]]: if \(\varphi_t\) is a smooth one-parameter family of automorphisms with \(\varphi_0=\operatorname{id}\), then \(\left.\frac{d}{dt}\right|_{t=0}\varphi_t\) is a derivation.
