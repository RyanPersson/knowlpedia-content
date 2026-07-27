+++
id = "fiber-bundles/covariant-derivative-of-a-section"
title = "Covariant derivative of a section"
kind = "knowl"
summary = "The derivative of a vector bundle section along a vector field as defined by a connection."
aliases = ["covariant-derivative-of-a-section", "Covariant derivative of a section"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/covariant-derivative-of-a-section.md"
+++

Let \(E\to M\) be a smooth real vector bundle with a [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\). For a [[fiber-bundles/vector-field|vector field]] \(X\in\mathfrak X(M)\) and a section \(s\in\Gamma(E)\), the **covariant derivative of \(s\) along \(X\)** is
\[
\nabla_X s \in \Gamma(E)
\]
It is \(\mathbb R\)-bilinear in \(X\) and \(s\), \(C^\infty(M)\)-linear in \(X\), and satisfies
\[
\nabla_X(fs)=X(f)s+f\nabla_Xs
\]
for \(f\in C^\infty(M)\).

## Equivalent characterizations

Equivalently, viewing \(\nabla s\) as a \(T^*M\otimes E\)-valued object, one has \((\nabla_X s)(p)=(\nabla s)(p)(X_p)\) by contraction.

## Examples
1. **Trivial bundle: ordinary directional derivative.** For \(E=M\times\mathbb R^r\) with the trivial connection, \(\nabla_X s\) is just the usual derivative of the vector-valued function \(s\) in the direction \(X\).
2. **Tangent bundle: covariant derivative of vector fields.** For a connection on \(TM\), \(\nabla_X Y\) is the covariant derivative of the vector field \(Y\) along \(X\), recovering the classical Christoffel-symbol formula in coordinates.
3. **Line bundle with connection 1-form.** In a local trivialization of a complex line bundle with connection form \(A\), if \(s=f\,e\) for a local frame \(e\), then \(\nabla_X s = (Xf + A(X)\,f)\,e\).
