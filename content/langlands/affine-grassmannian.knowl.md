+++
id = "langlands/affine-grassmannian"
title = "Affine Grassmannian"
kind = "definition"
summary = "The ind-projective loop-group quotient parametrizing a G-bundle on a formal disc with a punctured-disc trivialization."
aliases = ["affine Grassmannian", "Gr_G"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(k\) be an algebraically closed field and \(G\) a connected reductive
group over \(k\). Its **affine Grassmannian** is the ind-projective ind-scheme
\[
\operatorname{Gr}_G=LG/L^+G,
\qquad
LG(R)=G(R((t))),\quad L^+G(R)=G(R\lbrack\!\lbrack t\rbrack\!\rbrack)
\]
for \(k\)-algebras \(R\).
Functorially, it classifies a principal \(G\)-bundle on the formal disc
\(\operatorname{Spec}k\lbrack\!\lbrack t\rbrack\!\rbrack\) together with a
trivialization on the punctured disc \(\operatorname{Spec}k((t))\).

## Orbits

The \(G\lbrack\!\lbrack t\rbrack\!\rbrack\)-orbits are indexed by dominant
coweights \(\lambda\). Their
closures are affine Schubert varieties. The coweight records the relative
position of a [[langlands/hecke-modification|Hecke modification]].

## Langlands role

With a specified sheaf theory and coefficients satisfying the hypotheses of
[[langlands/geometric-satake-equivalence|geometric Satake]], the spherical
equivariant sheaf category on \(\operatorname{Gr}_G\) is identified with
representations of the Langlands dual group. This supplies the labels for
geometric Hecke functors.

## References

1. Ivan Mirković and Kari Vilonen, “Geometric Langlands duality and
   representations of algebraic groups over commutative rings,” *Annals of
   Mathematics* 166 (2007), 95–143.
   [arXiv](https://arxiv.org/abs/math/0401222).
