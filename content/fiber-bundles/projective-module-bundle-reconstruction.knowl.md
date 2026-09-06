+++
id = "fiber-bundles/projective-module-bundle-reconstruction"
title = "Reconstructing a vector bundle from a projective module"
kind = "definition"
summary = "The vector bundle whose fibers are obtained by evaluating a finitely generated projective smooth-function module at each point."
aliases = ["fiberwise evaluation reconstruction", "bundle associated to a projective smooth-function module"]
domains = ["fiber-bundles", "algebra-modules"]
prerequisites = ["fiber-bundles/smooth-manifold", "algebra-modules/projective-summand-of-free", "fiber-bundles/vector-bundle", "fiber-bundles/section-of-a-fiber-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a finite-dimensional Hausdorff second-countable
[[fiber-bundles/smooth-manifold|smooth manifold]], let
\(\mathbb F\in\{\mathbb R,\mathbb C\}\), and put
\(A=C^\infty(M,\mathbb F)\). For a finitely generated
[[algebra-modules/projective-summand-of-free|projective \(A\)-module]] \(Q\),
choose \(N\) and an idempotent \(p\in M_N(A)\) with \(Q\cong pA^N\). The
**vector bundle reconstructed from \(Q\)** is the
[[fiber-bundles/vector-bundle|smooth vector bundle]]
\[
E_Q=\coprod_{x\in M}\operatorname{im}p(x)\longrightarrow M.
\]
Its fibers have locally constant dimension, and its [[fiber-bundles/section-of-a-fiber-bundle|smooth sections]] satisfy \(\Gamma(E_Q)\cong pA^N\cong Q\). Different choices of the finite free summand and idempotent produce canonically isomorphic bundles up to the module isomorphism chosen.

## Intrinsic fiberwise description

For \(x\in M\), let \(I_x=\{f\in A:f(x)=0\}\). Evaluation identifies the reconstructed fiber with
\[
(E_Q)_x\cong Q/I_xQ.
\]
This formula does not mention a chosen embedding into a
[[algebra-modules/free-module|free module]]. Projectivity ensures that these
quotient spaces have locally constant dimension and fit together smoothly; the
idempotent presentation supplies explicit [[fiber-bundles/local-trivialization|local trivializations]].

The natural map to the [[fiber-bundles/module-of-smooth-sections|module of smooth sections]]
\[
Q\longrightarrow \Gamma(E_Q),
\qquad
q\longmapsto \bigl(x\mapsto q\bmod I_xQ\bigr),
\]
is an \(A\)-module isomorphism. Swan’s construction proves this reconstruction and the converse passage from bundles to projective section modules.

## Functoriality and equivalence

An \(A\)-linear map \(Q\to Q'\) induces fiber maps \(Q/I_xQ\to Q'/I_xQ'\) varying smoothly with \(x\). Consequently, reconstruction is functorial and is inverse, up to [[algebra-category-theory/natural-isomorphism|natural isomorphism]], to taking smooth sections. For connected \(M\), this gives the Serre–Swan equivalence between finite-rank smooth vector bundles and finitely generated projective \(C^\infty(M,\mathbb F)\)-modules without a compactness assumption.

For \(Q=eA^N\), the construction is exactly the [[fiber-bundles/serre-swan-idempotent-construction|image bundle of the idempotent]] \(e\). If \(Q=A^r\), it yields the trivial rank-\(r\) bundle.

## Conventions and scope

**Warning.** Finite generation and projectivity play different roles: finite
generation gives a finite ambient trivial bundle, while projectivity gives an
idempotent splitting and constant local rank. A merely
[[algebra-modules/finitely-generated-module|finitely generated module]] can
have jumping fiber dimension and need not define a vector bundle.

On a disconnected base, a finitely generated projective module reconstructs a
bundle whose locally constant rank is globally bounded by \(N\). Conversely,
that bounded-rank condition is needed if the vector-bundle convention permits
different ranks on different components. No condition at infinity is needed
because the coefficient algebra is all of \(C^\infty(M,\mathbb F)\), rather
than an algebra of functions vanishing at infinity.

## References

1. Richard G. Swan, “Vector Bundles and Projective Modules,” *Transactions of the American Mathematical Society* 105 (1962), 264–277. [DOI record](https://doi.org/10.1090/S0002-9947-1962-0143225-6). Relevant: §§1–3, reconstruction and equivalence of vector bundles with projective modules.
2. Alain Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted edition](https://www.alainconnes.org/docs/book94bigpdf.pdf). Relevant: chapter I, finitely generated projective modules as noncommutative vector bundles.
