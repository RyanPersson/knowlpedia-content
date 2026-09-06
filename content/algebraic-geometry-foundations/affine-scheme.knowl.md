+++
id = "algebraic-geometry-foundations/affine-scheme"
title = "Affine scheme"
kind = "knowl"
summary = "A locally ringed space obtained as the prime spectrum of a commutative ring."
aliases = ["affine-scheme", "Affine scheme"]
domains = ["algebraic-geometry-foundations"]
legacy_source_path = "algebraic-geometry-foundations/affine-scheme.md"
prerequisites = ["algebraic-geometry-foundations/locally-ringed-space", "algebra-rings/commutative-ring", "algebra-commutative/prime-spectrum", "algebra-commutative/zariski-topology", "algebraic-geometry-foundations/structure-sheaf"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

An **affine scheme** is a [[algebraic-geometry-foundations/locally-ringed-space|locally ringed space]] isomorphic to
\[
(\operatorname{Spec}A,\mathcal O_{\operatorname{Spec}A})
\]
for some [[algebra-rings/commutative-ring|commutative ring]] \(A\). Here \(\operatorname{Spec}A\) is the [[algebra-commutative/prime-spectrum|prime spectrum]] with its [[algebra-commutative/zariski-topology|Zariski topology]], and \(\mathcal O_{\operatorname{Spec}A}\) is its [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]]. The ring is recovered from global sections:
\[
\Gamma(\operatorname{Spec}A,\mathcal O_{\operatorname{Spec}A})\cong A.
\]

## Examples

For example, if \(k\) is a field, \(\operatorname{Spec}k\) is a one-point affine scheme whose local ring is \(k\). The [[algebraic-geometry-foundations/affine-line|affine line]] \(\operatorname{Spec}k[x]\) is another affine scheme, but it contains more than the familiar \(k\)-valued points: it also has points corresponding to other prime ideals, including a [[algebraic-geometry-foundations/generic-point|generic point]]. General [[algebraic-geometry-foundations/scheme|schemes]] are assembled by gluing affine schemes along open subsets.
