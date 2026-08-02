+++
id = "algebraic-geometry-foundations/semirings-and-monoids-as-blueprints"
title = "Monoid blueprint to semiring blueprint"
kind = "construction"
summary = "The canonical morphism from the monoid blueprint of a semiring to its semiring blueprint."
aliases = ["Semirings and monoids as blueprints", "canonical blueprints of semirings and monoids"]
domains = ["algebraic-geometry-foundations", "algebra-rings", "algebra-groups"]
section_mode = "progressive"
+++

Let \(R\) be a [[algebra-rings/commutative-semiring|commutative semiring]]. Its multiplicative monoid with zero \(R^\bullet\) determines a [[algebraic-geometry-foundations/commutative-monoid-with-zero-as-a-blueprint|monoid blueprint]]
\[
(R^\bullet)^{\mathrm{blpr}}=R^\bullet/\!/\mathcal R_{\min},
\]
while its addition determines the [[algebraic-geometry-foundations/semiring-as-a-blueprint|semiring blueprint]]
\[
R^{\mathrm{blpr}}=R^\bullet/\!/\mathcal R_R.
\]

Since \(\mathcal R_{\min}\subseteq\mathcal R_R\), the identity on \(R^\bullet\) induces a canonical blueprint morphism
\[
(R^\bullet)^{\mathrm{blpr}}\longrightarrow R^{\mathrm{blpr}}.
\]
It is the universal morphism from the monoid blueprint that imposes the additive equalities of \(R\). Its source has the free-semiring completion on \(R^\bullet\), whereas its target has [[algebraic-geometry-foundations/semiring-completion-of-a-blueprint|semiring completion]] \(R\); therefore this morphism is generally not an isomorphism.

## References
Oliver Lorscheid, [*The geometry of blueprints, Part I*, §§1.1–1.2](https://arxiv.org/abs/1103.1745).
