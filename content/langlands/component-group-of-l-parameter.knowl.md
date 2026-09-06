+++
id = "langlands/component-group-of-l-parameter"
title = "Component group of an \\(L\\)-parameter"
kind = "definition"
summary = "The finite group of connected components of the dual-group centralizer of a Langlands parameter, with refinements used to index packets."
aliases = ["Langlands component group", "Arthur component group", "A_phi", "S_phi"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["langlands/local-l-parameter", "algebra-groups/centralizer", "langlands-letter/knowls/langlands-dual-group", "langlands/l-packet"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\varphi:L_F\to{}^LG\) be a
[[langlands/local-l-parameter|local \(L\)-parameter]] and set

\[
S_\varphi=
Z_{\widehat G}\bigl(\operatorname{im}\varphi\bigr).
\]

The raw **component group of \(\varphi\)** is the finite group

\[
A_\varphi=\pi_0(S_\varphi).
\]

Here \(Z_{\widehat G}(\operatorname{im}\varphi)\) is the
[[algebra-groups/centralizer|centralizer]] of the parameter image in the
[[langlands-letter/knowls/langlands-dual-group|dual group]]. It measures the
disconnectedness of the dual-group symmetries that commute
with the parameter and is the starting point for the internal
parametrization of the [[langlands/l-packet|\(L\)-packet]].

## Quotient convention

For a fixed
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split
group]], the packet-indexing group is often

\[
\mathcal S_\varphi=
\pi_0\!\left(
S_\varphi/Z(\widehat G)^{W_F}
\right),
\]

or a closely related quotient. Removing the fixed center prevents central
symmetries already accounted for by the group from artificially enlarging the
packet.

## Refined cover

For packets across inner forms, one uses the preimage \(S_\varphi^+\) of
\(S_\varphi\) in an appropriate cover of \(\widehat G\), and representations
of \(\pi_0(S_\varphi^+)\) with a prescribed
[[algebra-representation-theory/central-character|central character]]. This
larger
group retains the cohomological data that identifies the inner form.

Consequently, the notations \(A_\varphi\), \(\mathcal S_\varphi\), and
\(S_\varphi^+\) are not interchangeable. A theorem must specify which
component-group convention it uses.

## References

1. Tasho Kaletha, “Representations of reductive groups over local fields,”
   §2.2, 2022. [arXiv](https://arxiv.org/abs/2201.07741).
2. James Arthur, *The Endoscopic Classification of Representations:
   Orthogonal and Symplectic Groups*, Chapter 1, American Mathematical
   Society, 2013. [AMS](https://bookstore.ams.org/COLL/61).
