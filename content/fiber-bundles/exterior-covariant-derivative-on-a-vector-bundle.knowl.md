+++
id = "fiber-bundles/exterior-covariant-derivative-on-a-vector-bundle"
title = "Exterior covariant derivative on a vector bundle"
kind = "definition"
summary = "The degree-one extension of a vector-bundle connection to bundle-valued differential forms."
aliases = ["covariant exterior derivative on E-valued forms"]
domains = ["fiber-bundles"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/vector-bundle-valued-differential-form", "fiber-bundles/exterior-derivative", "fiber-bundles/wedge-product-of-differential-forms"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 1
+++

Let \(E\to M\) be a smooth vector bundle with a [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\). The **exterior covariant derivative** is the unique linear operator of degree one on [[fiber-bundles/vector-bundle-valued-differential-form|\(E\)-valued forms]],
\[
d_\nabla:\Omega^k(M;E)\longrightarrow\Omega^{k+1}(M;E),
\]
whose action on a local scalar \(k\)-form \(\alpha\) and a local section \(s\) is
\[
d_\nabla(\alpha\otimes s)
=d\alpha\otimes s+(-1)^k\alpha\wedge\nabla s.
\]
Here \(d\) is the [[fiber-bundles/exterior-derivative|exterior derivative]], \(\nabla s\) is viewed as an \(E\)-valued one-form, and the [[fiber-bundles/wedge-product-of-differential-forms|wedge product]] acts on the scalar-form factors. In degree zero this gives \(d_\nabla s=\nabla s\). Linearity is over \(\mathbb R\), or over \(\mathbb C\) for a complex connection.

## Well-definedness and local formula

The connection Leibniz identity makes the formula compatible with the equality \((f\alpha)\otimes s=\alpha\otimes(fs)\). Local frames then give existence and uniqueness, and the locally defined operators agree on overlaps.

If \(\nabla=d+A\) in a local frame and \(\omega\) is a column of coefficient forms, then
\[
d_\nabla\omega=d\omega+A\wedge\omega.
\]
Consequently \(d_\nabla^2\omega=F_\nabla\wedge\omega\), where \(F_\nabla=dA+A\wedge A\) is the curvature matrix. The operator need not square to zero.

## Examples and principal bundles

For the trivial real line with its product connection, \(d_\nabla=d\). For a line bundle with local connection one-form \(A\), it is \(d+A\wedge\cdot\).

A principal connection induces this operator on associated vector bundles. Under the correspondence with tensorial forms on the principal bundle, it agrees with the [[fiber-bundles/exterior-covariant-derivative|horizontal-projection definition of exterior covariant differentiation]].
