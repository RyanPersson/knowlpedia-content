+++
id = "fiber-bundles/sobolev-completion-of-connections-and-gauge-transformations"
title = "Sobolev completion of connections and gauge transformations"
kind = "definition"
summary = "The Banach configuration space obtained by completing connections and gauge transformations in compatible Sobolev norms."
aliases = ["Sobolev gauge group", "completed connection space"]
domains = ["fiber-bundles", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/gauge-group", "fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection", "functional-analysis/sobolev-space", "fiber-bundles/construction-adjoint-lie-algebra-bundle-ad", "fiber-bundles/adjoint-bundle-p-g-g-with-conjugation-action", "fiber-bundles/vector-bundle-valued-differential-form", "fiber-bundles/partition-of-unity-subordinate-to-an-open-cover"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a closed \(d\)-dimensional
[[differential-geometry/riemannian-manifold|Riemannian manifold]], \(P\to M\)
a principal bundle with compact structure group, and \(A_0\) a smooth
connection. Choose \(1<p<\infty\) and an integer \(k\geq1\) with \(kp>d\).
The **Sobolev-completed connection space and gauge group** are
\[
\mathcal A_k^p(P)=A_0+W^{k,p}(T^*M\otimes\operatorname{ad}P),
\qquad
\mathcal G_{k+1}^p(P)=W^{k+1,p}(\operatorname{Ad}P).
\]
Here \(\operatorname{ad}(P)=P\times_G\mathfrak g\) is the [[fiber-bundles/construction-adjoint-lie-algebra-bundle-ad|adjoint Lie algebra bundle]], while \(\operatorname{Ad}(P)=P\times_G G\) is the [[fiber-bundles/adjoint-bundle-p-g-g-with-conjugation-action|adjoint group bundle]]. The notation \(W^{j,p}\) means sections whose local coefficient functions have weak derivatives through order \(j\) in \(L^p\). Use a finite smooth atlas, bundle trivializations, and a subordinate partition of unity to sum the local [[functional-analysis/sobolev-space|Sobolev norms]]. For the group-valued sections, use a faithful matrix embedding of compact \(G\); require values in the corresponding group fibers, and use pointwise multiplication and inversion. The resulting topology is independent of these auxiliary choices. Every element of \(\mathcal A_k^p(P)\) is uniquely \(A_0+a\) with \(a\) in the stated vector-valued Sobolev space.

## Smooth gauge action

The first is a Banach affine space, the second is the completed
[[fiber-bundles/gauge-group|gauge group]] and a Banach Lie group, and the extra
derivative makes the usual gauge action
\(\mathcal G_{k+1}^p(P)\times\mathcal A_k^p(P)\to\mathcal A_k^p(P)\) smooth.

## Why the indices are offset

In a [[fiber-bundles/local-trivialization|local trivialization]] the action of a
[[fiber-bundles/gauge-transformation|gauge transformation]] contains a
derivative:
\[
u\!\cdot\!A=uAu^{-1}-(du)u^{-1},\qquad u\!\cdot\!A:=(\Phi_{u^{-1}})^*A.
\]
Thus a \(W^{k+1,p}\) gauge transformation acts on a \(W^{k,p}\) connection without losing the target regularity. The hypothesis \(kp>d\) supplies the Sobolev multiplication and continuity properties needed for nonlinear products and inversion. Using \(W^{k,p}\) for both factors is a near-miss: the \(du\) term generally has only \(W^{k-1,p}\) regularity.

## Geometry of the completion

Smooth connections and smooth gauge transformations are dense in their respective completions. On compact \(M\), different choices of reference connection, [[fiber-bundles/bundle-metric|bundle metric]], and finite atlas give equivalent Sobolev norms, so they do not change the resulting topology.

At an [[fiber-bundles/irreducible-connection|irreducible connection]], a
Coulomb condition such as \(d_{A_0}^*(A-A_0)=0\) provides a local slice under
standard hypotheses. This converts the quotient near that orbit into a
Banach-manifold or orbifold model. [[fiber-bundles/reducible-connection|Reducible connections]] retain a nontrivial
[[fiber-bundles/stabilizer-of-a-connection|stabilizer]].

## Conventions and scope

**Warning.** Authors write \(L_k^p\), \(W^{k,p}\), or \(H^k\) for closely related completions, and the threshold imposed on \(k,p\) varies with the nonlinear operation under study. The condition above is a convenient strong hypothesis, not a minimal one.

On noncompact manifolds one must specify decay, weights, boundary conditions, or behavior at infinity. Those choices are part of the configuration space and cannot be recovered from the symbols \(W^{k,p}\) alone.

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: chapter 3, manifolds of connections; appendix A, the group of Sobolev gauge transformations.
2. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [Publisher record](https://global.oup.com/academic/product/the-geometry-of-four-manifolds-9780198502692). Relevant: §4.2, Sobolev configuration spaces and gauge-group actions.
