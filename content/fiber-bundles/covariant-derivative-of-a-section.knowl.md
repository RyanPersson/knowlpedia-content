+++
id = "fiber-bundles/covariant-derivative-of-a-section"
title = "Covariant derivative of a section"
kind = "knowl"
summary = "The derivative of a vector bundle section along a vector field as defined by a connection."
aliases = ["covariant-derivative-of-a-section", "Covariant derivative of a section"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/vector-field", "fiber-bundles/leibniz-rule-for-a-connection"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "fiber-bundles/covariant-derivative-of-a-section.md"
+++

Let \(E\to M\) be a [[fiber-bundles/vector-bundle|vector bundle]] with a [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\). For a [[fiber-bundles/vector-field|vector field]] \(X\) on \(M\) and a section \(s\in\Gamma(E)\), the connection produces another section \(\nabla_X s\).

**Definition.** The covariant derivative of \(s\) along \(X\) is the section
\[
\nabla_X s \in \Gamma(E)
\]
defined by the connection’s bilinear map \(\nabla:\mathfrak X(M)\times\Gamma(E)\to\Gamma(E)\). It is characterized by:
- \(C^\infty(M)\)-linearity in \(X\): \(\nabla_{fX}s=f\,\nabla_X s\),
- \(\mathbb R\)-linearity in \(s\), and
- the Leibniz rule in the section slot (see [[fiber-bundles/leibniz-rule-for-a-connection|Leibniz rule for a connection]]).

## Equivalent characterizations

Equivalently, viewing \(\nabla s\) as a \(T^*M\otimes E\)-valued object, one has \((\nabla_X s)(p)=(\nabla s)(p)(X_p)\) by contraction.

## Examples
1. **Trivial bundle: ordinary directional derivative.** For \(E=M\times\mathbb R^r\) with the trivial connection, \(\nabla_X s\) is just the usual derivative of the vector-valued function \(s\) in the direction \(X\).
2. **Tangent bundle: covariant derivative of vector fields.** For a connection on \(TM\), \(\nabla_X Y\) is the covariant derivative of the vector field \(Y\) along \(X\), recovering the classical Christoffel-symbol formula in coordinates.
3. **[[fiber-bundles/line-bundle|Line bundle]] with connection 1-form.** In a local trivialization of a complex line bundle with connection form \(A\), if \(s=f\,e\) for a local frame \(e\), then \(\nabla_X s = (Xf + A(X)\,f)\,e\).