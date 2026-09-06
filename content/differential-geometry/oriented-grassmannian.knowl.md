+++
id = "differential-geometry/oriented-grassmannian"
title = "Oriented Grassmannian"
kind = "definition"
summary = "The manifold whose points are fixed-dimensional real subspaces equipped with orientations."
aliases = ["oriented Grassmann manifold"]
domains = ["differential-geometry", "topology"]
prerequisites = ["linear-algebra/vector-space", "fiber-bundles/smooth-manifold", "differential-geometry/grassmannian"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V\) be an \(n\)-dimensional real [[linear-algebra/vector-space|vector space]] and \(1\leq k\leq n\). The **oriented Grassmannian**
\[
\widetilde{\operatorname{Gr}}_k(V)
=\{(W,o):W\in\operatorname{Gr}_k(V),\ o\text{ is an orientation of }W\}
\]
is the [[fiber-bundles/smooth-manifold|smooth manifold]] of oriented \(k\)-dimensional subspaces of \(V\). Forgetting \(o\) defines a smooth two-sheeted covering
\[
\widetilde{\operatorname{Gr}}_k(V)\longrightarrow
\operatorname{Gr}_k(V).
\]
The target is the [[differential-geometry/grassmannian|ordinary real Grassmannian]]. The covering transformation reverses the orientation of \(W\). Because the orientation choice is discrete, the oriented Grassmannian has the same dimension \(k(n-k)\) as its target.

## Homogeneous-space model

Choose an orientation and [[linear-algebra/inner-product|inner product]] on \(V\cong\mathbb R^n\). For \(0<k<n\), the [[lie-groups/special-orthogonal-group|special orthogonal group]] acts transitively, and the stabilizer of a reference oriented plane is \(SO(k)\times SO(n-k)\). Hence
\[
\widetilde{\operatorname{Gr}}_k(\mathbb R^n)
\cong SO(n)/(SO(k)\times SO(n-k)).
\]
The corresponding quotient for the ordinary Grassmannian uses \(S(O(k)\times O(n-k))\); the difference records whether changes of frame preserve the plane's orientation.

## Tautological orientation and universal role

The pullback of the [[differential-geometry/tautological-bundle-grassmannian|tautological rank-\(k\) bundle]] from \(\operatorname{Gr}_k(V)\) has fiber \(W\) over \((W,o)\), equipped with the orientation \(o\). It is therefore canonically an [[fiber-bundles/orientation-of-a-real-vector-bundle|oriented vector bundle]]. In the stable limit, oriented Grassmannians serve as classifying spaces for oriented real [[fiber-bundles/vector-bundle|vector bundles]], and the tautological orientation supports the [[fiber-bundles/euler-class|Euler class]] and oriented characteristic constructions.

## Examples and boundary cases

\(\widetilde{\operatorname{Gr}}_1(\mathbb R^n)\) is the sphere \(S^{n-1}\): an oriented line is determined by its positive unit vector. The forgetful map to \(\mathbb RP^{n-1}\) is the antipodal double cover. At \(k=n\), the underlying subspace is \(V\) itself, so the oriented Grassmannian consists of its two possible orientations; the homogeneous-space formula above was intentionally restricted to \(0<k<n\).

Complex Grassmannians are not examples of this double-cover construction. A complex subspace carries a canonical real orientation, so no independent binary orientation choice is required.

## References

1. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [Publisher DOI record](https://doi.org/10.1515/9781400881826). Relevant: §§5–6 on Grassmann manifolds and universal bundles, and §9 on oriented bundles.
2. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [Springer DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Grassmannians and classifying bundles.
