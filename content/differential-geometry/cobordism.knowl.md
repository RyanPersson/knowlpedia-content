+++
id = "differential-geometry/cobordism"
title = "Cobordism"
kind = "definition"
summary = "A compact manifold whose boundary is identified with a pair of closed manifolds."
aliases = ["smooth cobordism", "cobordant manifolds"]
domains = ["differential-geometry", "topology"]
section_mode = "progressive"
+++

Let \(M_0\) and \(M_1\) be [[topology/closed-manifold|closed smooth manifolds]] of dimension \(n\). A **smooth cobordism from \(M_0\) to \(M_1\)** is a compact smooth \((n+1)\)-dimensional [[differential-geometry/manifold-with-boundary|manifold with boundary]] \(W\), together with a diffeomorphism
\[
\partial W\cong M_0\sqcup M_1.
\]
The two identified boundary pieces are regarded respectively as the incoming and outgoing boundary. The manifolds \(M_0\) and \(M_1\) are **cobordant** if such a \(W\) exists. Additional structures—such as orientations, framings, [[fiber-bundles/spin-structure|spin structures]], or maps to a space—must extend over \(W\) when one speaks of cobordism with that structure.

## Basic constructions

The cylinder \(M\times[0,1]\) is a cobordism from \(M\) to itself. Reversing the designation of incoming and outgoing boundary gives a cobordism in the opposite direction. If \(W_{01}\) and \(W_{12}\) share the boundary \(M_1\), chosen collars allow them to be glued smoothly along \(M_1\), producing a cobordism from \(M_0\) to \(M_2\). These constructions underlie cobordism equivalence and composition.

## Handle viewpoint

A Morse function on a cobordism, constant on its boundary components and with critical points in the interior, decomposes the cobordism into elementary handle attachments. The index of each critical point records the handle index. This translates geometric questions about \(W\) into changes of level manifolds and is the bridge between cobordism, handle theory, and surgery [Milnor, Chapter 3](https://doi.org/10.1515/9781400881802).

## Examples

The disk \(D^{n+1}\) is a cobordism from the empty manifold to \(S^n\), so a sphere is null-cobordant. A pair of pants is a two-dimensional cobordism from two circles to one circle. A compact manifold with boundary is not by itself a cobordism between specified manifolds until its entire boundary has been identified and partitioned into incoming and outgoing pieces.

## Conventions and scope

Some authors use **bordism** for the geometric manifold \(W\) and **cobordism** for the induced [[shared-foundations/equivalence-relation|equivalence relation]]; others use the words interchangeably. This knowl follows the common differential-topology usage in which \(W\) is a cobordism. Boundary components may be empty, permitting cobordisms to or from the empty manifold.

## References

1. John Milnor, *Morse Theory*, Annals of Mathematics Studies 51, Princeton University Press, 1963. [DOI record](https://doi.org/10.1515/9781400881802). Relevant: Chapter 3, cobordisms and handle attachments.
2. Robert E. Stong, *Notes on Cobordism Theory*, Princeton University Press, 1968. [Publisher record](https://press.princeton.edu/books/paperback/9780691622728/notes-on-cobordism-theory). Relevant: Chapter I, definitions and basic properties of cobordism.
