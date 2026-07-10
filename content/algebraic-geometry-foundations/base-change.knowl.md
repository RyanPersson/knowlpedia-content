+++
id = "algebraic-geometry-foundations/base-change"
title = "Base change"
kind = "definition"
summary = "Pulling an object over a base back along a morphism to a new base."
aliases = ["base change", "change of base", "pullback along the base"]
domains = ["algebraic-geometry-foundations"]
+++

The map \(\operatorname{Spec}K\to\operatorname{Spec}F\) becomes trivial after changing the base from \(\operatorname{Spec}F\) to \(\operatorname{Spec}K\): its pullback has coordinate ring \(K\otimes_F K\), which splits into one factor for each Galois automorphism.

Precisely, for a morphism \(X\to S\) and a new base \(S'\to S\), the **base change of \(X\) along \(S'\to S\)** is

\[
X_{S'}:=X\times_S S'\longrightarrow S'.
\]

It is formed using the [[algebraic-geometry-foundations/fiber-product-of-schemes|fiber product]]. A morphism \(f:X\to Y\) over \(S\) similarly pulls back to

\[
f_{S'}:X\times_S S'\longrightarrow Y\times_S S'.
\]

On [[algebraic-geometry-foundations/affine-scheme|affine schemes]], if \(R\to R'\) changes the base and \(X=\operatorname{Spec}A\), then

\[
X_{R'}\cong\operatorname{Spec}(A\otimes_R R').
\]

**Warning.** This is a categorical pullback, not merely a substitution of coordinates or a restriction of underlying topological spaces. Many geometric properties are stable under base change, but that stability is a theorem to check for each property.
