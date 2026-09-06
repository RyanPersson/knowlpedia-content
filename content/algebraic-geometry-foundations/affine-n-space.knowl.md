+++
id = "algebraic-geometry-foundations/affine-n-space"
title = "Affine n-space"
kind = "knowl"
summary = "The affine scheme Spec(k[x_1,...,x_n]) representing n algebraic coordinates."
aliases = ["affine-n-space", "Affine n-space", "affine space"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/affine-scheme", "algebra-rings/polynomial-ring", "algebra-rings/prime-ideal", "algebra-rings/maximal-ideal", "algebraic-geometry-foundations/algebraically-closed-field", "algebraic-geometry-foundations/closed-point", "topology/irreducible-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebraic-geometry-foundations/affine-n-space.md"
+++

Let \(k\) be a field and \(n\ge 0\). The **affine \(n\)-space over \(k\)** is the [[algebraic-geometry-foundations/affine-scheme|affine scheme]]
\[
\mathbb A_k^n:=\operatorname{Spec}k[x_1,\ldots,x_n].
\]
The variables \(x_1,\ldots,x_n\) are coordinate functions. A \(k\)-valued point \((a_1,\ldots,a_n)\in k^n\) determines the [[algebra-rings/maximal-ideal|maximal ideal]] \((x_1-a_1,\ldots,x_n-a_n)\). If \(k\) is [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed]], every [[algebraic-geometry-foundations/closed-point|closed point]] arises this way, though the spectrum also contains nonclosed points corresponding to [[topology/irreducible-space|irreducible]] subvarieties.

The case \(n=1\) is the [[algebraic-geometry-foundations/affine-line|affine line]]. The standard open charts of [[algebraic-geometry-foundations/projective-space|projective \(n\)-space]] are each isomorphic to \(\mathbb A_k^n\).

## Examples

For example, in \(\mathbb A_k^2\), the [[algebra-rings/prime-ideal|prime ideal]] \((y-x^2)\subseteq k[x,y]\) represents the whole parabola, not a single coordinate pair. This illustrates how scheme points encode both ordinary points and generic behavior of algebraic loci.
