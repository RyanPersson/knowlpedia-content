+++
id = "fiber-bundles/slice-theorem-for-the-gauge-action"
title = "Slice theorem for the gauge action"
kind = "theorem"
summary = "A local normal-form theorem modeling a neighborhood of a gauge orbit by a Coulomb slice modulo the connection stabilizer."
aliases = ["Coulomb slice theorem", "local slice theorem for gauge transformations"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/sobolev-completion-of-connections-and-gauge-transformations", "fiber-bundles/gauge-transformation", "fiber-bundles/coulomb-gauge"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal bundle]] with compact structure group over a closed Riemannian \(n\)-manifold. Use the [[fiber-bundles/sobolev-completion-of-connections-and-gauge-transformations|Sobolev completions]] of connections in \(W^{k,p}\) and [[fiber-bundles/gauge-transformation|gauge transformations]] in \(W^{k+1,p}\), with \(kp>n\). For a connection \(A\), there is \(\varepsilon>0\) such that the [[fiber-bundles/coulomb-gauge|Coulomb slice]]
\[
\mathcal S_{A,\varepsilon}
=\{A+a\mid d_A^*a=0,\ \|a\|_{W^{k,p}}<\varepsilon\}
\]
meets every sufficiently nearby gauge orbit. Moreover, a neighborhood of the orbit of \(A\) in the connection space is modeled equivariantly by
\[
\mathcal G\times_{\operatorname{Stab}(A)}\mathcal S_{A,\varepsilon}.
\]

## Why the Coulomb condition is transverse

The tangent to the gauge orbit at \(A\) is \(\operatorname{im}d_A\), while \(d_A^*a=0\) selects its \(L^2\)-orthogonal complement. Solving for a gauge transformation that places \(A+a\) in the slice reduces, after linearization, to the elliptic operator \(d_A^*d_A\). The implicit-function theorem then supplies existence and local uniqueness up to the [[fiber-bundles/stabilizer-of-a-connection|stabilizer of \(A\)]].

The offset in Sobolev regularity is essential: a \(W^{k+1,p}\) gauge transformation acts on a \(W^{k,p}\) connection without losing a derivative. The hypothesis \(kp>n\) provides the multiplication and continuity properties required by the nonlinear action.

## Quotient structure

Passing to the quotient gives a local model
\[
\mathcal S_{A,\varepsilon}/\operatorname{Stab}(A)
\]
for the moduli problem near \([A]\). If the stabilizer acts trivially after central symmetries are removed, this behaves like a Banach-manifold chart. A nontrivial stabilizer produces an orbifold-type or more singular local quotient. Thus the theorem explains why [[fiber-bundles/irreducible-connection|irreducible connections]] form the regular stratum and [[fiber-bundles/reducible-connection|reducible connections]] create singular strata.

## Conventions and scope

**Warning.** The theorem depends on the chosen Sobolev indices, based versus full [[fiber-bundles/gauge-group|gauge group]], and treatment of the center. “Unique Coulomb representative” means unique only after these residual stabilizer symmetries are accounted for. A Coulomb condition by itself, without a small-neighborhood restriction, is not a global [[fiber-bundles/gauge-fixing-condition|gauge fixing]].

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 3, especially Theorem 3.4, the slice theorem for the gauge action.
2. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [DOI record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §4.2, Sobolev gauge groups and local slices.
