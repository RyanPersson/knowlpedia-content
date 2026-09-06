+++
id = "algebraic-geometry-foundations/affine-blue-scheme"
title = "Affine blue scheme"
kind = "definition"
summary = "A blueprinted space isomorphic to the spectrum of a blueprint."
aliases = ["affine blueprint scheme"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/locally-blueprinted-space", "algebraic-geometry-foundations/blueprint", "algebra-commutative/zariski-topology", "algebraic-geometry-foundations/structure-sheaf"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An **affine blue scheme** is a [[algebraic-geometry-foundations/locally-blueprinted-space|locally blueprinted space]] isomorphic to
\[
\operatorname{Spec}B
\]
for some [[algebraic-geometry-foundations/blueprint|blueprint]] \(B\), where the spectrum carries its [[algebra-commutative/zariski-topology|Zariski topology]] and [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]].

Contravariantly, blueprint morphisms induce morphisms of affine blue schemes:
\[
\operatorname{Hom}_{\mathrm{Blpr}}(B,C)
\;\cong\;
\operatorname{Hom}_{\mathrm{BSch}}(\operatorname{Spec}C,\operatorname{Spec}B).
\]

## Role in blue geometry

Affine blue schemes are the local models for [[algebraic-geometry-foundations/blue-scheme|blue schemes]]. Principal opens \(U_h\subseteq\operatorname{Spec}B\) are affine and correspond to [[algebraic-geometry-foundations/localization-of-blueprint|blueprint localizations]] \(B[h^{-1}]\), so the usual scheme-theoretic gluing pattern survives.

Semiring schemes and ordinary affine schemes enter through the [[algebraic-geometry-foundations/semiring-as-a-blueprint|canonical embedding of commutative semirings into blueprints]]. The resulting base-extension functors carry extra hypotheses and should not be read as identifying all blue schemes with classical schemes.

## References
Oliver Lorscheid, [*The geometry of blueprints, Part I*, §3](https://arxiv.org/abs/1103.1745).
