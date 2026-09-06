+++
id = "langlands/a-packet"
title = "Arthur packet"
kind = "knowl"
summary = "A finite packet of irreducible representations attached to an Arthur parameter."
aliases = ["A-packet", "Arthur packets", "local Arthur packet", "global Arthur packet"]
domains = ["langlands", "representation-theory", "number-theory"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/local-field", "langlands/arthur-parameter", "algebraic-geometry-foundations/reductive-algebraic-group", "harmonic-analysis/admissible-representation-p-adic-group", "lie-groups/admissible-representation-real-reductive-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(F\) be a
[[algebra-fields-galois/local-field|local field]]. For a
local [[langlands/arthur-parameter|Arthur parameter]] \(\psi\) of a
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]]
\(G\) over \(F\), its **Arthur packet** or **\(A\)-packet**
\(\Pi_\psi(G)\) is a finite collection, more precisely often a finite
multiset, of irreducible admissible representations of \(G(F)\), where
admissibility has its
[[harmonic-analysis/admissible-representation-p-adic-group|nonarchimedean]]
or
[[lie-groups/admissible-representation-real-reductive-group|archimedean]]
meaning according to \(F\). The packet is equipped with a pairing against a
component group associated to \(\psi\).

## Relation to L-packets

The parameter \(\psi\) has an associated ordinary [[langlands/local-l-parameter|Langlands parameter]]
\(\varphi_\psi\), but \(\Pi_\psi\) need not equal the
[[langlands/l-packet|\(L\)-packet]] \(\Pi_{\varphi_\psi}\). An \(A\)-packet
can contain nontempered unitary representations and can intersect several
\(L\)-packets. When the Arthur \(\operatorname{SL}_2\)-factor is trivial,
the expected packet is the tempered \(L\)-packet.

## Internal structure

Write \(\mathcal S_\psi\) for an appropriate finite quotient of the
component group of the centralizer of \(\psi\) in \(\widehat G\). After
normalization by a [[langlands/whittaker-datum|Whittaker datum]], members of
the packet carry characters or representations of \(\mathcal S_\psi\).
The exact enhancement depends on the group and on
[[langlands/rigid-inner-twist|inner-form data]].

## Global packet

A [[langlands/global-langlands-parameter|global parameter]] has localizations
\(\psi_v\). Its global packet is built from
[[langlands/restricted-tensor-product-automorphic-representation|restricted
tensor products]]

\[
\pi=\bigotimes_v'\pi_v,
\qquad
\pi_v\in\Pi_{\psi_v},
\]

subject to almost-all
[[harmonic-analysis/unramified-representation-p-adic-group|unramified]]
normalization. Not every such tensor
product occurs in the [[langlands/discrete-automorphic-spectrum|discrete automorphic spectrum]]. The
[[langlands/arthur-multiplicity-formula|Arthur multiplicity formula]]
imposes a global component-group character condition.

## Status

For
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split]]
symplectic and [[lie-groups/special-orthogonal-group|special orthogonal groups]], Arthur constructed
the relevant packets and classification; extensions cover inner forms and
unitary groups in specified settings. For a general connected reductive
group, \(A\)-packets remain conjectural and several candidate constructions
can require comparison.

## References

1. James Arthur, *The Endoscopic Classification of Representations:
   Orthogonal and Symplectic Groups*, AMS, 2013.
   [AMS](https://bookstore.ams.org/COLL/61).
2. Chung Pang Mok, “Endoscopic classification of representations of
   quasi-split unitary groups,” *Memoirs of the AMS* 235 (2015).
   [AMS](https://bookstore.ams.org/memo-235-1108).
