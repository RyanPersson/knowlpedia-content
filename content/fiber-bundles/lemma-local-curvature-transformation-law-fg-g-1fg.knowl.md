+++
id = "fiber-bundles/lemma-local-curvature-transformation-law-fg-g-1fg"
title = "Lemma: local curvature transforms by conjugation"
kind = "knowl"
summary = "Under a gauge transformation, the local curvature 2-form is conjugated by the gauge function"
aliases = ["lemma-local-curvature-transformation-law-fg-g-1fg", "Lemma: local curvature transforms by conjugation"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/lemma-local-curvature-transformation-law-fg-g-1fg.md"
prerequisites = ["fiber-bundles/local-curvature-formula-f-da-aa", "fiber-bundles/local-connection-1-form", "fiber-bundles/lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg", "lie-groups/adjoint-action-of-a-lie-group", "fiber-bundles/curvature-2-form-of-a-principal-connection"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 4
+++

Let \(A\) be a [[fiber-bundles/local-connection-1-form|local connection form]] on \(U\) for a Lie group \(G\), and let \(g:U\to G\) be smooth. If \(A^g\) is its [[fiber-bundles/lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg|gauge transform]], then the corresponding [[fiber-bundles/local-curvature-formula-f-da-aa|local curvatures]] satisfy
\[
F_{A^g}=\operatorname{Ad}(g^{-1})F_A,
\]
where \(\operatorname{Ad}\) is the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]].

## Formulas and matrix notation

For an arbitrary Lie group,
\[
A^g=\operatorname{Ad}(g^{-1})A+g^{-1}dg,
\qquad F_A=dA+\tfrac12[A\wedge A].
\]
Here \(g^{-1}dg\) denotes the pullback of the left Maurer–Cartan form. For matrix Lie groups these become
\[
A^g=g^{-1}Ag+g^{-1}dg,\qquad F_A=dA+A\wedge A,
\qquad F_{A^g}=g^{-1}F_Ag.
\]

## Geometric proof

Write \(A=s^*\omega\) and \(A^g=(s\cdot g)^*\omega\). The [[fiber-bundles/curvature-2-form-of-a-principal-connection|principal curvature]] \(\Omega\) is horizontal and equivariant. In differentiating \(s\cdot g\), terms from differentiating \(g\) are vertical and therefore vanish when inserted into \(\Omega\). Equivariance gives
\[
(s\cdot g)^*\Omega=\operatorname{Ad}(g^{-1})s^*\Omega,
\]
which is the claimed formula.

## Overlapping trivializations

On overlaps with transition function \(g_{ij}\), the local curvature forms satisfy
\[
F_j=\operatorname{Ad}(g_{ij}^{-1})F_i.
\]
Consequently, invariant polynomials applied to the local curvatures agree on overlaps and define global [[fiber-bundles/chernweil-form|Chern–Weil forms]].

## Examples

1. **Abelian groups (electromagnetism).**
   If \(G\) is abelian (for example \(U(1)\)), then \(g^{-1}Fg=F\), so the curvature 2-form is gauge invariant. In particular, the transformation reduces to \(A^g=A+g^{-1}dg\) while \(F^g=dA^g=dA=F\).

2. **Pure gauge connections have zero curvature.**
   On a trivial bundle, if \(A=g^{-1}dg\) is [[fiber-bundles/pure-gauge-connection-ag-1dg-on-a-trivial-bundle|pure gauge]], then \(F=dA+\tfrac12[A\wedge A]=0\). The lemma then gives \(F^h=h^{-1}0\,h=0\) for any further gauge transformation \(h\).

3. **Associated vector bundles (matrix conjugation).**
   If \(G\) acts on a vector space via a representation (see [[lie-groups/representation-of-a-lie-group|representation]]), the induced curvature on the associated vector bundle is a matrix-valued 2-form, and this lemma becomes the familiar rule “curvature matrices conjugate under change of frame.”

## Reference

Adam Marsh, *Gauge Theories and Fiber Bundles: Definitions, Pictures, and Results*, §5.4, especially equations (5.17)–(5.19), on horizontal equivariant curvature and its local forms. [Author paper](https://arxiv.org/pdf/1607.03089).
