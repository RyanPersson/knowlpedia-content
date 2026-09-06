+++
id = "algebraic-geometry-foundations/semiring-as-a-blueprint"
title = "Semiring as a blueprint"
kind = "construction"
summary = "The blueprint whose additive relations record every equality in a commutative semiring."
aliases = ["canonical blueprint of a semiring", "semiring blueprint"]
domains = ["algebraic-geometry-foundations", "algebra-rings"]
prerequisites = ["algebra-rings/commutative-semiring", "algebraic-geometry-foundations/pre-addition-on-a-monoid", "algebraic-geometry-foundations/semiring-completion-of-a-blueprint"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(R\) be a [[algebra-rings/commutative-semiring|commutative semiring]], and let \(R^\bullet\) be its multiplicative monoid with zero. The **blueprint associated with \(R\)** is
\[
R^{\mathrm{blpr}}=R^\bullet/\!/\mathcal R_R,
\]
where
\[
\sum a_i\equiv_{\mathcal R_R}\sum b_j
\quad\Longleftrightarrow\quad
\sum a_i=\sum b_j\ \text{in }R.
\]
Thus its [[algebraic-geometry-foundations/pre-addition-on-a-monoid|pre-addition]] records all and only the formal additive equalities that hold in \(R\).

Its [[algebraic-geometry-foundations/semiring-completion-of-a-blueprint|semiring completion]] is canonically isomorphic to \(R\). Moreover, the construction defines a fully faithful functor
\[
\mathbf{CSRng}\hookrightarrow\mathbf{Blpr},
\]
because morphisms between semiring blueprints are exactly homomorphisms of the original commutative semirings.

## References
Oliver Lorscheid, [*The geometry of blueprints, Part I: Algebraic background and scheme theory*, §1.5](https://arxiv.org/abs/1103.1745).
