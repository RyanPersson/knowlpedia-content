+++
id = "operator-algebras/cstar-exact-sequence"
title = "Short exact sequence of C*-algebras"
kind = "definition"
summary = "An injective ideal inclusion followed by a surjective C*-quotient map with matching image and kernel."
aliases = ["C*-extension", "extension of C*-algebras", "Exact sequence of C*-algebras"]
domains = ["operator-algebras", "algebra-category-theory"]
section_mode = "progressive"
+++

A **short exact sequence of \(C^*\)-algebras** is a diagram
\[
0\longrightarrow I\xrightarrow{\iota}A\xrightarrow{q}B
\longrightarrow 0
\]
of [[operator-algebras/star-homomorphism|\(*\)-homomorphisms]] in which
\(\iota\) is injective, \(q\) is surjective, and
\(\operatorname{im}\iota=\ker q\). After identifying \(I\) with its image,
\(I\) is a [[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]]
of \(A\), and the induced map from
[[operator-algebras/quotient-cstar-algebra|\(A/I\)]] to \(B\) is an
isometric \(*\)-isomorphism. The sequence is also called an
**extension of \(B\) by \(I\)**; this word order records that \(I\) is the
ideal and \(B\) is the quotient.

## Canonical ideal–quotient sequence

Every closed [[algebra-rings/two-sided-ideal|two-sided ideal]] \(I\triangleleft A\) gives the exact sequence
\[
0\longrightarrow I\longrightarrow A\longrightarrow A/I
\longrightarrow 0.
\]
Conversely, every short exact sequence of \(C^*\)-algebras is isomorphic to
one of this form. The closedness of \(I\) is automatic when it is the kernel
of a \(*\)-homomorphism, and it is essential for \(A/I\) to carry its
quotient \(C^*\)-norm.

## Splittings

The extension is **split** if there is a \(*\)-homomorphism
\(s:B\to A\) with \(q\circ s=\operatorname{id}_B\). A bounded linear or a
completely positive section is weaker and does not make the extension split
as a \(C^*\)-algebra extension. Even when a \(*\)-splitting exists, the
middle algebra need not be a direct product: the section can encode a
nontrivial action of \(B\) on \(I\).

## Functorial significance

The underlying vector-space or module sequence is a
[[algebra-modules/short-exact-sequence|short exact sequence]], but the
\(C^*\)-structure supplies extra analytic rigidity: injective
\(*\)-homomorphisms are isometric, quotient norms are fixed, and ideals are
closed. A [[algebra-category-theory/functor|functor]] on \(C^*\)-algebras is
called exact when it preserves these sequences. Operator \(K\)-theory instead
produces a cyclic six-term exact sequence from them.

## Multiplier example

For any \(C^*\)-algebra \(I\), its embedding as an essential ideal in
[[operator-algebras/multiplier-algebra|the multiplier algebra]] yields
\[
0\longrightarrow I\longrightarrow M(I)
\longrightarrow M(I)/I\longrightarrow 0.
\]
The quotient \(M(I)/I\) is the [[operator-algebras/corona-algebra|corona algebra]]. Extensions with ideal \(I\)
can often be encoded by homomorphisms from the quotient algebra into this
corona algebra.

## References

1. Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006. [DOI record](https://doi.org/10.1007/3-540-28517-2). Relevant: §§II.5 and II.8 on ideals, quotients, and extensions.
2. Niels E. Wegge-Olsen, *K-Theory and C*-Algebras: A Friendly Approach*, Oxford University Press, 1993. [DOI record](https://doi.org/10.1093/oso/9780198596943.001.0001). Relevant: Chapters 2–3 on multiplier algebras and extensions.
