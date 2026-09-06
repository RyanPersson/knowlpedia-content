+++
id = "shale-paper/wiener-transform"
title = "Wiener Transform W"
kind = "knowl"
summary = "A unitary transform on Gaussian L₂ intertwining T with T^{*-1}"
aliases = ["wiener-transform", "Wiener Transform W"]
domains = ["shale-paper"]
prerequisites = []
dependency_review_count = 1
legacy_source_path = "shale-paper/wiener-transform.md"
+++

The **Wiener transform** \(W\) is the unitary operator on the Gaussian space \(L_2(M,n)\) whose action on the polynomial subspace is
\[
(Wf)(x)=\int f(\sqrt2\,y+i x)\,dn(y).
\]

and whose action on all of \(L_2(M,n)\) is obtained by continuous extension.

## Intertwining properties

For \(T\) in the [[shale-paper/restricted-general-linear-group-rgl|restricted general linear group]], the [[shale-paper/segal-unitary-representation-Ufrak|Segal–Shale representation]] satisfies
\[
W\mathfrak U(T)W^{-1}=\mathfrak U(T^{*-1}).
\]
For the Fock–Cook field operators used in the paper,
\[
P(x)=WQ(x)W^{-1}.
\]

In one dimension, under the standard unitary identification, \(W\) becomes the Fourier transform.
