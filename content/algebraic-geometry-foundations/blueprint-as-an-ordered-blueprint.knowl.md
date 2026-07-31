+++
id = "algebraic-geometry-foundations/blueprint-as-an-ordered-blueprint"
title = "Blueprint as an ordered blueprint"
kind = "construction"
summary = "The fully faithful embedding that regards additive equalities as an ordered blueprint with equality order."
aliases = ["blueprints embedded in ordered blueprints", "canonical ordered blueprint of a blueprint"]
domains = ["algebraic-geometry-foundations", "algebra-category-theory"]
section_mode = "progressive"
+++

Let \(B=A/\!/\mathcal R\) be a [[algebraic-geometry-foundations/blueprint|blueprint]]. Its associated [[algebraic-geometry-foundations/ordered-blueprint|ordered blueprint]] is
\[
B^{\mathrm{ord}}=(A,B^+,=),
\]
where \(B^+=\mathbb N[A]/\mathcal R\) is the [[algebraic-geometry-foundations/semiring-completion-of-a-blueprint|semiring completion]], \(A\) is its distinguished multiplicative generating subset, and the order on \(B^+\) is equality.

Equivalently, each additive relation \(\sum a_i\equiv\sum b_j\) may be encoded by the two inequalities
\[
\sum a_i\leq\sum b_j
\qquad\text{and}\qquad
\sum b_j\leq\sum a_i.
\]

## Fully faithful embedding

The assignment \(B\mapsto B^{\mathrm{ord}}\) defines a fully faithful functor
\[
\mathbf{Blpr}\hookrightarrow\mathbf{OBlpr}.
\]
Indeed, a blueprint morphism induces an order-preserving semiring homomorphism of completions that preserves the distinguished monoids. Conversely, a morphism between equality-ordered objects preserves precisely the additive equalities defining the original blueprints.

## References
Oliver Lorscheid, [*A unifying approach to tropicalization*, §2.7](https://arxiv.org/abs/1508.07949).
