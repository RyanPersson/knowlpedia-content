+++
id = "langlands/endoscopic-datum"
title = "Endoscopic datum"
kind = "knowl"
summary = "Dual-group data defining a reductive endoscopic group and its L-embedding into a given L-group."
aliases = ["endoscopy datum", "endoscopic data", "elliptic endoscopic datum"]
domains = ["langlands", "algebraic-geometry-foundations", "representation-theory"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "algebra-fields-galois/local-field", "langlands-letter/knowls/global-local-fields-completions", "algebraic-geometry-foundations/quasi-split-reductive-group", "langlands-letter/knowls/semisimple-element-and-class", "langlands-letter/knowls/langlands-functoriality-l-homomorphism", "langlands/l-group", "langlands-letter/knowls/langlands-dual-group", "algebra-groups/centralizer", "shared-foundations/equivalence-relation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over a
[[algebra-fields-galois/local-field|local]] or [[langlands-letter/knowls/global-local-fields-completions|global field]] \(F\).
An **endoscopic datum** for \(G\) is, in a commonly used shorthand, a triple

\[
\mathfrak e=(H,s,\eta),
\]

where \(H\) is a
[[algebraic-geometry-foundations/quasi-split-reductive-group|quasi-split]]
connected reductive \(F\)-group, \(s\in\widehat G\) is
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]], and

\[
\eta:{}^L H\longrightarrow {}^L G
\]

\(\eta\) is an
[[langlands-letter/knowls/langlands-functoriality-l-homomorphism|\(L\)-homomorphism]]
between [[langlands/l-group|\(L\)-groups]], identifying the
[[langlands-letter/knowls/langlands-dual-group|dual group]] \(\widehat H\)
with the identity component
\(\operatorname{Cent}(s,\widehat G)^\circ\) of a
[[algebra-groups/centralizer|centralizer]], subject to the
standard Galois-action and central conditions. Data are taken up to an
[[shared-foundations/equivalence-relation|equivalence relation]] involving \(\widehat G\)-conjugacy.

## Full form of the datum

In general the relevant extension need not be presented as the ordinary
\(L\)-group of \(H\). One therefore writes

\[
(H,\mathcal H,s,\xi),
\]

where \(\mathcal H\) is an extension of the [[langlands/weil-group|Weil group]] by \(\widehat H\) and
\(\xi:\mathcal H\to{}^LG\) realizes the prescribed centralizer. The shorter
triple is appropriate only after an \(L\)-embedding or auxiliary \(z\)-pair
has been chosen.

## Endoscopic group

The group \(H\) is usually not a subgroup of \(G\). Its dual group is a
connected centralizer inside \(\widehat G\), so the relation is naturally
visible on the dual side. Matching strongly regular [[langlands/stable-conjugacy|stable conjugacy classes]]
of \(H(F)\) map to stable classes of \(G(F)\).

The datum is **elliptic** when the connected component of the relevant
Galois-fixed center of \(\widehat H\), modulo that of \(\widehat G\), is
trivial. Elliptic data govern discrete terms.

## Purpose

Endoscopic data index correction terms in the
[[langlands/stable-trace-formula|stable trace formula]]. A
[[langlands/transfer-factor|transfer factor]] and matching functions compare
[[langlands/stable-orbital-integral|stable orbital integrals]] on \(H\) with
[[langlands/kappa-orbital-integral|\(\kappa\)-orbital integrals]] on \(G\).
On the spectral side this becomes a relation among packet characters.

## Ordinary versus twisted endoscopy

Twisted endoscopy adds an automorphism or a twisted space and is essential
for transfers from classical groups to general linear groups. Its datum and
transfer factors contain extra structure; an ordinary datum should not be
silently used in the twisted setting.

## References

1. Robert P. Langlands and Diana Shelstad, “On the definition of transfer
   factors,” *Mathematische Annalen* 278 (1987), 219–271.
   [DOI](https://doi.org/10.1007/BF01458070).
2. Robert E. Kottwitz and Diana Shelstad, *Foundations of Twisted
   Endoscopy*, Astérisque 255, 1999.
   [Numdam](https://www.numdam.org/item/AST_1999__255__R1_0/).
