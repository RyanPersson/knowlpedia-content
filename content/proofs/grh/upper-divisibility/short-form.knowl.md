+++
id = "proofs/grh/upper-divisibility/short-form"
title = "Short algebraic form"
kind = "definition"
summary = "An algebraic form whose values are integral at every p-adic embedding and whose conjugates have squared norm at most B."
aliases = ["short form", "B-short form", "B-short"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsShort"]
lean_files = ["src/New/UpperBound/Size/ShortColumns.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with a fixed [[?c:CM type|CM type]], \(n\) a finite index set, and \(\varphi\) an [[?lean:New.AlgForm|algebraic form]] of weight \((\kappa,e)\) on the finite adelic points \(G_f\) of the definite unitary group of the standard hermitian space \(E^{n}\) (form \(\sum_i x_i\bar x_i\)); its values \(\varphi(g)\) are complex coordinate vectors of the [[?c:Weyl module|Weyl module]] of weight \(\kappa\). Let \(B\) be a real number. The form \(\varphi\) is **\(B\)-short** if

1. (**integrality**) for every prime \(p\) and every embedding \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), and every \(g\in G_f\), the [[?lean:New.weylGauge|gauge]] of \(\varphi(g)\) at \(g\) is at most \(1\): every coordinate of \(g^{-1}\cdot\iota(\varphi(g))\), with \(g^{-1}\) acting in weight \((\kappa,e)\), has \(p\)-adic absolute value at most \(1\); and
2. (**size**) for every field automorphism \(\sigma\) of \(\mathbb{C}\) and every \(g\in G_f\), the conjugate vector \(\sigma(\varphi(g))\) has [[?lean:New.weylNormSq|squared norm]] \(\sigma(\varphi(g))^{*}\,G\,\sigma(\varphi(g))\le B\), where \(G\) is the integer Gram matrix of the Weyl module.

## Properties

If \(\varphi\) is \(B\)-short and \(k\in G_f\) has integral entries (lies in the standard level), then \(\varphi-k\varphi\) is \(4B\)-short, where \(k\varphi(g)=\varphi(gk)\) is the right translate. Indeed the integral forms at \(p\) form a module, and the gauge at \(gk\) equals the gauge at \(g\) for integral \(k\), so integrality is kept; and the parallelogram law \(\lVert u-v\rVert^2+\lVert u+v\rVert^2=2\lVert u\rVert^2+2\lVert v\rVert^2\) for the positive form \(G\) gives \(\lVert\sigma(\varphi(g)-\varphi(gk))\rVert^2\le 2B+2B\). (Lean: `New.IsShort.sub_translate`.)

## References

1. Lean: `New.IsShort`, `New.IsShort.sub_translate` in `src/New/UpperBound/Size/ShortColumns.lean`.
