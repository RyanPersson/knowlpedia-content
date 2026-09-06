+++
id = "fiber-bundles/leibniz-rule-for-a-connection"
title = "Leibniz rule for a connection"
kind = "knowl"
summary = "The product rule relating differentiation of a scaled section to derivatives of the function and the section."
aliases = ["leibniz-rule-for-a-connection", "Leibniz rule for a connection"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/exterior-derivative", "fiber-bundles/vector-field", "fiber-bundles/module-of-smooth-sections"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
legacy_source_path = "fiber-bundles/leibniz-rule-for-a-connection.md"
+++

Let \(E\to M\) be a vector bundle, and consider an \(\mathbb R\)-bilinear operation \((X,s)\mapsto\nabla_Xs\) on smooth vector fields and smooth sections, with values in smooth sections. Assume this operation is \(C^\infty(M)\)-linear in \(X\). For \(f\in C^\infty(M)\), the identity below is the additional axiom that defines a [[fiber-bundles/connection-on-a-vector-bundle|connection]].

**Definition.** The Leibniz rule (product rule) for \(\nabla\) is the identity
\[
\nabla_X (f s) \;=\; X(f)\,s \;+\; f\,\nabla_X s.
\]

This rule encodes that \(\nabla\) differentiates sections “like a derivation” in the section slot, while remaining \(C^\infty(M)\)-linear in the vector field slot.

## Equivalent characterizations

Equivalently, using the 1-form \(df\) defined by the [[fiber-bundles/exterior-derivative|exterior derivative]] of \(f\), one can write
\[
\nabla(fs)=df\otimes s + f\,\nabla s
\]
as an identity in \(\Gamma(T^*M\otimes E)\).

## Examples
1. **Trivial connection.** On \(E=M\times\mathbb R^r\) with \(\nabla_X s=X(s)\), the formula reduces to the usual product rule for differentiating a product of a scalar function and a vector-valued function.
2. **Constant scalars.** If \(f\) is constant, then \(X(f)=0\) and the rule becomes \(\nabla_X(fs)=f\,\nabla_X s\), expressing homogeneity over real constants in the section argument. Additivity is part of the separately assumed bilinearity.
3. **Local frame computation.** In a local frame, writing \(s=\sum_i s^i e_i\) and using the connection matrix \(A\), the rule is reflected in the identity \(\nabla(s^i e_i)=ds^i\otimes e_i + s^i \nabla e_i\).