+++
id = "langlands-letter/knowls/root-vs-weight-lattice-isogeny"
title = "Root Lattice, Weight Lattice, and Isogeny Forms"
kind = "knowl"
summary = "For a semisimple group, intermediate lattices between the root and weight lattices encode its central isogeny form."
aliases = ["root-vs-weight-lattice-isogeny", "Root Lattice, Weight Lattice, and Isogeny Forms"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/root-vs-weight-lattice-isogeny.md"
+++

Let \(G\) be a split semisimple group with split maximal torus \(T\) and root system \(\Phi\subset X^*(T)\).

The **root lattice** is \(Q:=\mathbb{Z}\Phi\). The **weight lattice** is
\[
P:=\{\lambda\in X^*(T)\otimes_{\mathbb Z}\mathbb Q:
\langle \lambda,\alpha^\vee\rangle\in\mathbb Z
\text{ for every }\alpha\in\Phi\}.
\]
The character lattice lies between them:
\[
Q\subseteq X^*(T)\subseteq P.
\]
These intermediate lattices encode the central isogeny forms of the semisimple group. In particular, \(X^*(T)=P\) for the simply connected form.

## Interpretation

The letter's intermediate lattice \(L\) controls the isogeny form of \(G\). Dually, the corresponding cocharacter lattice controls the isogeny form of the [[langlands-letter/knowls/langlands-dual-group|Langlands dual group]].
