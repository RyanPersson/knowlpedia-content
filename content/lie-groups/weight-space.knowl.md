+++
id = "lie-groups/weight-space"
title = "Weight space"
kind = "knowl"
summary = "The simultaneous eigenspace of a representation corresponding to a weight on an abelian subalgebra."
aliases = ["weight-space", "Weight space"]
domains = ["lie-groups"]
prerequisites = []
dependency_review_count = 1
legacy_source_path = "lie-groups/weight-space.md"
+++

Let \(\mathfrak g\) be a complex Lie algebra, let \(\mathfrak h\subseteq\mathfrak g\) be an abelian subalgebra, and let \(\rho:\mathfrak g\to\mathfrak{gl}(V)\) be a representation. For \(\lambda\in\mathfrak h^\ast\), the **\(\lambda\)-weight space** is
\[
V_\lambda=\{v\in V\mid \rho(H)v=\lambda(H)v\ \text{for all }H\in\mathfrak h\}.
\]

If \(V_\lambda\neq 0\), then \(\lambda\) is a [[lie-groups/weight-of-a-representation|weight of the representation]].

## Interaction with roots (semisimple context)
When \(\mathfrak g\) is semisimple and \(\mathfrak h\) is a [[lie-groups/cartan-subalgebra|Cartan subalgebra]], \(\mathfrak g\) decomposes into [[lie-groups/root-space|root spaces]] \(\mathfrak g_\alpha\). For \(X\in\mathfrak g_\alpha\) and \(v\in V_\lambda\),
\[
X\cdot v \in V_{\lambda+\alpha},
\]
so root vectors “shift” weights by roots.

## Context
For a finite-dimensional representation of a complex semisimple Lie algebra, the Cartan subalgebra acts semisimply, giving
\[
V=\bigoplus_\lambda V_\lambda.
\]
This weight-space decomposition is one of the main inputs to highest-weight methods and depends crucially on complete reducibility phenomena (compare [[lie-groups/weyls-theorem-complete-reducibility|Weyl’s complete reducibility theorem]]).
