+++
id = "differential-geometry/bordism-group"
title = "Bordism group"
kind = "definition"
summary = "The abelian group of bordism classes of closed manifolds under disjoint union."
aliases = ["cobordism group", "unoriented bordism group", "oriented bordism group"]
domains = ["differential-geometry", "topology"]
prerequisites = ["differential-geometry/cobordism-equivalence", "topology/closed-manifold", "differential-geometry/disjoint-union-of-smooth-manifolds", "algebra-groups/abelian-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Fix \(n\geq0\) and a bordism theory. The **\(n\)-dimensional bordism group** is the set of [[differential-geometry/cobordism-equivalence|bordism-equivalence classes]] of [[topology/closed-manifold|closed]] \(n\)-manifolds with the chosen structure, with operation
\[
[M]+[N]=[M\sqcup N].
\]
The identity is the class of the empty manifold. In unoriented bordism every class is its own inverse, since \(M\sqcup M\) is the boundary of \(M\times[0,1]\). In oriented bordism the inverse of \([M]\) is \([-M]\), the manifold with reversed orientation. The symmetry of [[differential-geometry/disjoint-union-of-smooth-manifolds|disjoint union]] makes this an [[algebra-groups/abelian-group|abelian group]]. Standard notations are \(\Omega_n^O\) and \(\Omega_n^{SO}\).

## Why the operation descends

Suppose \(M_0\) is bordant to \(M_1\) through \(W\), and \(N_0\) is bordant to \(N_1\) through \(W'\). Then \(W\sqcup W'\) is a bordism from \(M_0\sqcup N_0\) to \(M_1\sqcup N_1\). Hence addition is independent of representatives. Associativity and commutativity follow from canonical diffeomorphisms of disjoint unions, while the empty manifold acts as a unit. These geometric constructions establish the group laws directly.

## Grading and multiplication

Taking all dimensions together gives a graded abelian group
\[
\Omega_*^O=\bigoplus_{n\geq0}\Omega_n^O
\]
and similarly in the oriented or other structured theories. [[shared-foundations/cartesian-product|Cartesian product]] defines a graded multiplication \([M][N]=[M\times N]\), producing a bordism ring when the structures are closed under products. This multiplication is additional structure; it is not the group operation, which remains disjoint union.

## Dependence on tangential structure

Changing the allowed structure changes both the [[shared-foundations/equivalence-relation|equivalence relation]] and the group. Forgetting orientation induces a homomorphism \(\Omega_n^{SO}\to\Omega_n^O\), but oriented null-bordism is stronger than unoriented null-bordism. Framed, spin, complex, and other bordism groups require the relevant structure to extend over every bordism. The notation \(\Omega_n\) is therefore incomplete unless the underlying theory is understood.

## Examples

Two standard choices are unoriented bordism and [[differential-geometry/oriented-cobordism|oriented smooth bordism]].
The class of any boundary is zero by definition. In unoriented dimension zero, a closed manifold is a finite set of points, and a compact one-manifold has an even number of [[differential-geometry/boundary-and-interior-of-a-manifold|boundary points]]; therefore \(\Omega_0^O\cong\mathbb Z/2\). With orientations, signed point counts give \(\Omega_0^{SO}\cong\mathbb Z\). These examples also exhibit the different inverse conventions.

## References

1. Robert E. Stong, *Notes on Cobordism Theory*, Princeton University Press, 1968. [DOI record](https://doi.org/10.1515/9781400879977). Relevant: Chapter I, cobordism categories and bordism groups.
2. John Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [Publisher record](https://press.princeton.edu/books/paperback/9780691081229/characteristic-classes). Relevant: Appendix B, cobordism.
