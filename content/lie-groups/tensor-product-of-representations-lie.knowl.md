+++
id = "lie-groups/tensor-product-of-representations-lie"
title = "Tensor product of representations"
kind = "knowl"
summary = "The diagonal action on a tensor product, defined by tensoring group actions or by the Leibniz rule for Lie algebras."
aliases = ["tensor-product-of-representations-lie", "Tensor product of representations"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/representation-of-a-lie-group"]
dependency_review_count = 1
legacy_source_path = "lie-groups/tensor-product-of-representations-lie.md"
+++

Let \(G\) be a Lie group and let \(\pi_V:G\to\operatorname{GL}(V)\) and \(\pi_W:G\to\operatorname{GL}(W)\) be [[lie-groups/representation-of-a-lie-group|representations of \(G\)]]. Their **tensor product representation** on \(V\otimes W\) is
\[
\pi_{V\otimes W}(g)=\pi_V(g)\otimes\pi_W(g).
\]
Thus
\[
\pi_{V\otimes W}(g)(v\otimes w)
=\pi_V(g)v\otimes\pi_W(g)w,
\]
extended linearly from pure tensors.

## Lie-algebra version

Let \(\mathfrak g\) be a Lie algebra, and let \(\rho_V:\mathfrak g\to\mathfrak{gl}(V)\) and \(\rho_W:\mathfrak g\to\mathfrak{gl}(W)\) be [[lie-groups/representation-of-a-lie-algebra|representations of \(\mathfrak g\)]]. The tensor product representation \(\rho_{V\otimes W}:\mathfrak g\to\mathfrak{gl}(V\otimes W)\) is
\[
\rho_{V\otimes W}(X)
=\rho_V(X)\otimes\operatorname{Id}_W
+\operatorname{Id}_V\otimes\rho_W(X),
\]
or, equivalently,
\[
X\cdot (v\otimes w)=(X\cdot v)\otimes w + v\otimes (X\cdot w).
\]

A direct computation using the commutator bracket on \(\mathfrak{gl}(V\otimes W)\) shows that \(\rho_{V\otimes W}\) is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]].

## Weight behavior

If \(\mathfrak g\) is semisimple and \(\mathfrak h\) is a [[lie-groups/cartan-subalgebra|Cartan subalgebra]], then tensor products interact cleanly with the [[lie-groups/weight-space|weight-space decomposition]]: if \(v\in V_\lambda\) and \(w\in W_\mu\), then
\[
v\otimes w \in (V\otimes W)_{\lambda+\mu}.
\]

Thus the set of [[lie-groups/weight-of-a-representation|weights]] of \(V\otimes W\) is contained in the Minkowski sum of the weight sets of \(V\) and \(W\). This underlies Clebsch–Gordan decompositions and highest-weight calculations.
