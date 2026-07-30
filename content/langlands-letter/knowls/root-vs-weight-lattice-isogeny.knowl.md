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

## Type A1

For type \(A_1\), let \(\omega\) be the fundamental weight and let
\(\alpha=2\omega\) be the positive root. Then
\[
Q=\mathbb Z\alpha=2\mathbb Z\omega
\subset
P=\mathbb Z\omega,
\qquad P/Q\cong\mathbb Z/2\mathbb Z.
\]
The simply connected form \(SL_2\) has character lattice \(P\), while the
adjoint form \(PGL_2\) has character lattice \(Q\). The central isogeny
\[
SL_2\longrightarrow PGL_2
\]
has kernel \(\mu_2\). Exchanging character and cocharacter lattices under
Langlands duality gives
\(\widehat{SL_2}=PGL_2(\mathbb C)\) and
\(\widehat{PGL_2}=SL_2(\mathbb C)\).

## References

1. Robert Steinberg, *Lectures on Chevalley Groups*, Yale University lecture
   notes, 1968; revised AMS edition, 2016.
