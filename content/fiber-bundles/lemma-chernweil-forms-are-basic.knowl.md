+++
id = "fiber-bundles/lemma-chernweil-forms-are-basic"
title = "Lemma: Chern–Weil forms are basic"
kind = "knowl"
summary = "Applying an invariant polynomial to the curvature of a principal connection produces a basic differential form."
aliases = ["lemma-chernweil-forms-are-basic", "Lemma: Chern–Weil forms are basic"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/lemma-chernweil-forms-are-basic.md"
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection", "fiber-bundles/curvature-2-form-of-a-principal-connection", "fiber-bundles/basic-differential-form-on-a-principal-bundle", "fiber-bundles/invariant-polynomial-on-a-lie-algebra", "fiber-bundles/pullback-of-differential-forms", "fiber-bundles/wedge-product-of-differential-forms"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]], let \(\omega\) be a [[fiber-bundles/principal-connection|principal connection]], and let \(\Omega\in\Omega^2(P;\mathfrak g)\) be its [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature \(2\)-form]]. If \(Q\) is a real- or complex-valued [[fiber-bundles/invariant-polynomial-on-a-lie-algebra|Ad-invariant symmetric multilinear polynomial]] of degree \(k\) on \(\mathfrak g\), then
\[
Q(\Omega)=Q(\underbrace{\Omega,\dots,\Omega}_{k\text{ times}})\in\Omega^{2k}(P)
\]
is a [[fiber-bundles/basic-differential-form-on-a-principal-bundle|basic differential form]], with the same real or complex coefficient field as \(Q\). Hence there is a unique \(\alpha\in\Omega^{2k}(M)\) satisfying \(\pi^*\alpha=Q(\Omega)\).

Here substitution is defined directly: if \(\Omega=\sum_a\Omega^a e_a\) in a basis of \(\mathfrak g\), then \(Q(\Omega)=\sum_{a_1,\ldots,a_k}Q(e_{a_1},\ldots,e_{a_k})\,\Omega^{a_1}\wedge\cdots\wedge\Omega^{a_k}\); for \(k=0\) it is the constant \(Q\). This expression is independent of the basis.

## Horizontality and invariance

1. **Horizontality:** for every fundamental vertical vector field \(X^\#\) on \(P\) (see [[fiber-bundles/convention-fundamental-vector-field-x-is-defined-using-the-right-action|fundamental vector field convention]]),
   \[
   \iota_{X^\#}\,Q(\Omega)=0.
   \]
   Equivalently, \(Q(\Omega)\) vanishes whenever any argument is vertical.

2. **\(G\)-invariance:** for every \(g\in G\),
   \[
   R_g^*\,Q(\Omega)=Q(\Omega),
   \]
   so it is an [[fiber-bundles/invariant-differential-form|invariant differential form]].

## Examples
1. **Abelian case: \(U(1)\)**
   For \(G=U(1)\), the adjoint action is trivial, and \(Q\) can be taken to be the identity on \(\mathfrak{u}(1)\cong i\mathbb{R}\). Then the Chern–Weil form is simply \(Q(\Omega)=\Omega\), and the lemma says \(\Omega\) is basic, hence descends to a 2-form on \(M\). This is exactly what happens in the [[fiber-bundles/dirac-monopole-connection-on-the-hopf-bundle|Dirac monopole]] example on the Hopf bundle.

2. **Unitary bundles**
   For a principal \(U(n)\)-bundle, take \(Q(X)=\mathrm{tr}(X)\) or \(Q(X)=\mathrm{tr}(X^k)\). The lemma guarantees that \(\mathrm{tr}(\Omega)\) and \(\mathrm{tr}(\Omega^k)\) are basic forms on \(P\), so they correspond to well-defined differential forms on \(M\) whose normalized trace powers represent the components of the Chern character; the Chern classes are obtained from appropriate polynomial combinations of these normalized traces (see [[fiber-bundles/chern-class|Chern class]]).

3. **Orthogonal bundles and Pontryagin forms**
   For \(G=SO(n)\), invariant polynomials such as \(Q(X)=\mathrm{tr}(X^2)\) produce Pontryagin forms after the standard normalization (see [[fiber-bundles/pontryagin-class|Pontryagin class]]). The lemma ensures these forms are basic and hence live on the base manifold, not just on the total space of frames.
