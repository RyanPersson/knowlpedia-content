+++
id = "differential-geometry/oriented-cobordism"
title = "Oriented cobordism"
kind = "definition"
summary = "A cobordism whose orientation induces the reversed incoming and given outgoing boundary orientations."
aliases = ["oriented bordism", "orientation-preserving cobordism"]
domains = ["differential-geometry", "topology"]
section_mode = "progressive"
+++

Let \(M_0\) and \(M_1\) be closed oriented \(n\)-manifolds. An **oriented cobordism from \(M_0\) to \(M_1\)** is an oriented compact \((n+1)\)-manifold \(W\) together with an orientation-preserving diffeomorphism
\[
(-M_0)\sqcup M_1\longrightarrow \partial W,
\]
where \(\partial W\) has its [[differential-geometry/boundary-orientation|outward-normal-first boundary orientation]] and \(-M_0\) denotes \(M_0\) with reversed orientation. Thus an [[differential-geometry/cobordism|ordinary cobordism]] becomes oriented only when its orientation is compatible with the specified signs on both boundary components.
The boundary identification is part of the data, so merely knowing that the underlying unoriented manifolds bound the same \(W\) is insufficient.

## Why the incoming sign reverses

For the product \(W=M\times[0,1]\) with product orientation, the boundary at \(t=1\) has the orientation of \(M\), while the boundary at \(t=0\) has the opposite orientation. The formula \(\partial W=(-M_0)\sqcup M_1\) therefore makes the cylinder the identity oriented cobordism. It also makes orientations agree when outgoing and incoming boundary components are glued.

## Oriented bordism groups

Disjoint union defines addition on oriented cobordism classes, the empty manifold is the zero element, and orientation reversal gives the inverse. In each dimension \(n\), these classes form the [[differential-geometry/bordism-group|oriented bordism group]] \(\Omega_n^{SO}\). [[shared-foundations/cartesian-product|Cartesian product]] supplies a graded multiplication, yielding the oriented bordism ring. [[fiber-bundles/characteristic-number|Characteristic numbers]] provide important invariants of these classes [Milnor–Stasheff, Appendix B](https://doi.org/10.1515/9781400881826).

## Examples and non-examples

An oriented disk bounds its sphere with the induced orientation, so the oriented sphere is null-cobordant. An orientation on \(W\) chosen without regard to the boundary identifications may fail the definition: if it induces the wrong orientation on one specified outgoing component, the identification is not an oriented cobordism from the stated \(M_0\) to \(M_1\).

## Conventions and scope

Some sources phrase the defining identification as \(\partial W=M_0\sqcup(-M_1)\), reversing the direction assigned to a cobordism. This is a directional convention, not a different [[shared-foundations/equivalence-relation|equivalence relation]], provided it is used consistently. This knowl adopts the convention in which an arrow \(M_0\to M_1\) has boundary \((-M_0)\sqcup M_1\).

## References

1. Robert E. Stong, *Notes on Cobordism Theory*, Princeton University Press, 1968. [Publisher record](https://press.princeton.edu/books/paperback/9780691622728/notes-on-cobordism-theory). Relevant: Chapter I, oriented cobordism.
2. John Milnor and James Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [DOI record](https://doi.org/10.1515/9781400881826). Relevant: Appendix B, cobordism and characteristic numbers.
