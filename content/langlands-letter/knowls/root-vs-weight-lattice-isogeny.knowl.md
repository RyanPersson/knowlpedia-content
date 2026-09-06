+++
id = "langlands-letter/knowls/root-vs-weight-lattice-isogeny"
title = "Root, weight, and isogeny lattices"
kind = "knowl"
summary = "Intermediate character lattices between the root and weight lattices encode central isogeny forms."
aliases = ["root-vs-weight-lattice-isogeny", "Root Lattice, Weight Lattice, and Isogeny Forms"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/root-vs-weight-lattice-isogeny.md"
section_mode = "progressive"
prerequisites = ["langlands-letter/knowls/split-reductive-group", "langlands-letter/knowls/maximal-torus-weight-lattice", "lie-groups/root-lattice", "lie-groups/weight-lattice", "langlands-letter/knowls/simply-connected-semisimple-group", "lie-groups/root-system"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a
[[langlands-letter/knowls/split-reductive-group|split semisimple group]]
with [[langlands-letter/knowls/maximal-torus-weight-lattice|maximal torus]]
\(T\) and root system \(\Phi\subset X^*(T)\). The
[[lie-groups/root-lattice|root lattice]] and abstract
[[lie-groups/weight-lattice|weight lattice]] are

\[
Q=\mathbb Z\Phi,
\qquad
P=
\{\lambda\in X^*(T)_\mathbb Q:
\langle\lambda,\alpha^\vee\rangle\in\mathbb Z
\text{ for all }\alpha\in\Phi\}.
\]

The actual character lattice satisfies

\[
Q\subseteq X^*(T)\subseteq P.
\]

Intermediate lattices classify the
[[langlands-letter/knowls/simply-connected-semisimple-group|central isogeny
forms]] with the given [[lie-groups/root-system|root system]]. The
[[langlands-letter/knowls/simply-connected-semisimple-group|simply connected
form]] has character lattice \(P\), while
the adjoint form has character lattice \(Q\).

## Dual statement

On cocharacters one has

\[
Q^\vee\subseteq X_*(T)\subseteq P^\vee,
\]

where \(Q^\vee\) here denotes the
[[langlands-letter/knowls/coroots-and-pairing|coroot lattice]] and
\(P^\vee\) the
coweight lattice—not the integral duals of \(Q\) and \(P\) with the same
symbols. The simply connected form has \(X_*(T)=Q^\vee\), while the adjoint
form has the full coweight lattice. The
[[langlands-letter/knowls/langlands-dual-group|Langlands dual group]]
exchanges the two lattice diagrams.

## Type A1

Let \(\omega\) be the fundamental weight and
\(\alpha=2\omega\). Then

\[
Q=2\mathbb Z\omega
\subset
P=\mathbb Z\omega,
\qquad
P/Q\simeq\mathbb Z/2\mathbb Z.
\]

Thus \(\operatorname{SL}_2\to\operatorname{PGL}_2\) is the central isogeny
with kernel \(\mu_2\), and

\[
\widehat{\operatorname{SL}_2}=\operatorname{PGL}_2(\mathbb C),
\qquad
\widehat{\operatorname{PGL}_2}=\operatorname{SL}_2(\mathbb C).
\]

## Relation to the letter

The letter's intermediate lattice \(L\) fixes the isogeny form; its
[[langlands-letter/knowls/dual-lattice|dual lattice]] fixes the dual group's
form. Recording only the abstract root system would lose this information.

## References

1. Robert Steinberg, *Lectures on Chevalley Groups*, AMS, 2016.
2. A. Borel, *Linear Algebraic Groups*, second edition, Springer, 1991.
