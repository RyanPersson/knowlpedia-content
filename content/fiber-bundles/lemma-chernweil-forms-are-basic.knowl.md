+++
id = "fiber-bundles/lemma-chernweil-forms-are-basic"
title = "Lemma: Chern–Weil forms are basic"
kind = "knowl"
summary = "Applying an invariant polynomial to the curvature of a principal connection produces a basic differential form."
aliases = ["lemma-chernweil-forms-are-basic", "Lemma: Chern–Weil forms are basic"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection", "fiber-bundles/curvature-2-form-of-a-principal-connection", "fiber-bundles/basic-differential-form-on-a-principal-bundle"]
dependency_review_count = 1
legacy_source_path = "fiber-bundles/lemma-chernweil-forms-are-basic.md"
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]], let \(\omega\) be a [[fiber-bundles/principal-connection|principal connection]], and let \(\Omega\in\Omega^2(P;\mathfrak g)\) be its [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature \(2\)-form]]. If \(Q\) is an \(\operatorname{Ad}\)-invariant symmetric multilinear polynomial of degree \(k\) on \(\mathfrak g\), then
\[
Q(\Omega)=Q(\underbrace{\Omega,\dots,\Omega}_{k\text{ times}})\in\Omega^{2k}(P)
\]
is a [[fiber-bundles/basic-differential-form-on-a-principal-bundle|basic differential form]]. Hence there is a unique \(\alpha\in\Omega^{2k}(M)\) satisfying \(\pi^*\alpha=Q(\Omega)\).

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
   For a principal \(U(n)\)-bundle, take \(Q(X)=\mathrm{tr}(X)\) or \(Q(X)=\mathrm{tr}(X^k)\). The lemma guarantees that \(\mathrm{tr}(\Omega)\) and \(\mathrm{tr}(\Omega^k)\) are basic forms on \(P\), so they correspond to well-defined differential forms on \(M\) representing Chern classes (see [[fiber-bundles/chern-class|Chern class]]).

3. **Orthogonal bundles and Pontryagin forms**
   For \(G=SO(n)\), invariant polynomials such as \(Q(X)=\mathrm{tr}(X^2)\) produce Pontryagin forms (see [[fiber-bundles/pontryagin-class|Pontryagin class]]). The lemma ensures these forms are basic and hence live on the base manifold, not just on the total space of frames.
