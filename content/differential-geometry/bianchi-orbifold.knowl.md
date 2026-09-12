+++
id = "differential-geometry/bianchi-orbifold"
title = "Bianchi orbifold"
kind = "definition"
summary = "The hyperbolic orbifold obtained by quotienting three-space by a Bianchi group."
aliases = []
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["algebra-groups/bianchi-group", "differential-geometry/hyperbolic-three-orbifold", "lie-groups/psl2c-action-on-hyperbolic-three-space", "lie-groups/bianchi-group-nonuniform-lattice"]
+++

The **Bianchi orbifold** attached to \(K=\mathbb Q(\sqrt{-d})\), with \(d>0\) square-free, is
\[
M_d=\operatorname{PSL}_2(\mathcal O_K)\backslash\mathbb H^3,
\]
equipped with the [[differential-geometry/hyperbolic-three-orbifold|hyperbolic orbifold structure]] induced by the [[algebra-groups/bianchi-group|Bianchi group]] and its [[lie-groups/psl2c-action-on-hyperbolic-three-space|isometric action]]. The backslash denotes orbits for the left group action.

## Features

It is complete, orientable, noncompact, and of finite volume. Its [[differential-geometry/bianchi-cusp-ideal-class-correspondence|cusps]] encode the ideal class group, while its [[differential-geometry/bianchi-orbifold-volume-formula|volume]] involves a Dedekind zeta value.

## Why retain the orbifold structure?

The class of \(\begin{pmatrix}0&-1\\1&0\end{pmatrix}\) has order two in every Bianchi group: its square is \(-I\). Its hyperbolic action has fixed points. Thus a Bianchi quotient has nontrivial orbifold isotropy; one cannot simply apply a free-action manifold theorem.

## References

1. T. Church, B. Farb, and A. Putman, *Integrality in the Steinberg module and the top-dimensional cohomology of SL_n O_K*, Example 5.6, p. 31 of the linked version. [Author-hosted paper](https://math.uchicago.edu/~farb/papers/Steinberg2.pdf)
