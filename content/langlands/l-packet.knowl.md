+++
id = "langlands/l-packet"
title = "\\(L\\)-packet"
kind = "definition"
summary = "The finite family of irreducible admissible representations sharing one local Langlands parameter."
aliases = ["Langlands packet", "local L-packet", "packet of representations"]
domains = ["langlands", "harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/local-field", "langlands/local-l-parameter"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Assume the [[langlands/local-langlands-correspondence|basic local Langlands
correspondence]] for a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] \(G\) over a
[[algebra-fields-galois/local-field|local field]]. For
a relevant parameter \(\varphi\), its **\(L\)-packet** is the fiber

\[
\Pi_\varphi(G)=
\{\pi\in\operatorname{Irr}(G(F)):\varphi_\pi=\varphi\}.
\]

Thus an \(L\)-packet is not an arbitrary family of similar representations: it
is the finite set sharing one [[langlands/local-l-parameter|local
\(L\)-parameter]].

## Packet size

Packets for tori and \(\operatorname{GL}_n\) are singletons. For groups with
nontrivial endoscopy, several inequivalent representations can share a
parameter. Their internal distinctions are encoded by a finite
[[langlands/component-group-of-l-parameter|component group]].

## Stable character

For a [[harmonic-analysis/tempered-representation-p-adic-group|tempered]]
packet of a \(p\)-adic group, an appropriately weighted sum of the
[[harmonic-analysis/harish-chandra-character-p-adic-group|Harish–Chandra
characters]] of its members is expected to be a
[[langlands/stable-distribution|stable distribution]]. Other linear combinations
are related by [[langlands/endoscopic-transfer|endoscopic transfer]]. This character-theoretic structure is part
of what makes the partition into packets mathematically meaningful.

## Inner forms

The notation \(\Pi_\varphi(G)\) fixes one group \(G(F)\). A **compound packet**
ranges over suitable pure or
[[langlands/rigid-inner-twist|rigid inner forms]] of a
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split
group]]. The
refined correspondence uses the compound packet because its component-group
parametrization naturally records which inner form contains each member.

## References

1. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §§2.1–2.2, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
2. James Arthur, *The Endoscopic Classification of Representations:
   Orthogonal and Symplectic Groups*, American Mathematical Society, 2013.
   [AMS](https://bookstore.ams.org/COLL/61).
