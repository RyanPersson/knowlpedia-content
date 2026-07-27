+++
id = "fiber-bundles/invariant-differential-form"
title = "Invariant differential form"
kind = "knowl"
summary = "A differential form preserved by pullback under a Lie group action."
aliases = ["invariant-differential-form", "Invariant differential form"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/invariant-differential-form.md"
+++

Let \(G\) act on a manifold \(M\) by a [[fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold|smooth action]]. A [[fiber-bundles/differential-k-form|differential \(k\)-form]] \(\omega\in\Omega^k(M)\) is **\(G\)-invariant** if
\[
\Phi_g^*\omega=\omega\qquad\text{for every }g\in G,
\]
where \(\Phi_g(x)=g\cdot x\).

If \(G\) is connected, this is equivalent to \(\mathcal L_{X_M}\omega=0\) for every \(X\) in the Lie algebra of \(G\), where \(X_M\) is the generated vector field.

Invariant forms form a subcomplex of the de Rham complex: if \(\omega\) is invariant, then so is its [[fiber-bundles/exterior-derivative|exterior derivative]] \(d\omega\).

## Examples
1. For \(M=G\) with the left translation action, every left-invariant form is \(G\)-invariant.
2. The standard volume form on \(S^n\) is invariant under the natural \(SO(n+1)\)-action.
3. **Basic forms are invariant.** Any [[fiber-bundles/basic-differential-form-on-a-principal-bundle|basic form]] on a principal bundle is invariant under the principal right action by definition.
