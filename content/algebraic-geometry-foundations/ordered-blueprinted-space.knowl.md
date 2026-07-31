+++
id = "algebraic-geometry-foundations/ordered-blueprinted-space"
title = "Ordered blueprinted space"
kind = "definition"
summary = "A topological space equipped with a sheaf of ordered blueprints."
aliases = ["OBlpr-space", "ordered blueprint space"]
domains = ["algebraic-geometry-foundations", "algebra-hyperstructures"]
section_mode = "progressive"
+++

An **ordered blueprinted space**, or **OBlpr-space**, is a topological space \(X\) together with a sheaf \(\mathcal O_X\) of [[algebraic-geometry-foundations/ordered-blueprint|ordered blueprints]].

A morphism
\[
(f,f^\#):(X,\mathcal O_X)\longrightarrow(Y,\mathcal O_Y)
\]
consists of a continuous map \(f:X\to Y\) and a morphism of sheaves \(f^\#:\mathcal O_Y\to f_*\mathcal O_X\) such that, for every \(x\in X\), the induced stalk map
\[
f_x^\#:\mathcal O_{Y,f(x)}\longrightarrow\mathcal O_{X,x}
\]
sends nonunits to nonunits. These objects and morphisms form the category \(\mathbf{OBlprSp}\).

Unlike the definition of a [[algebraic-geometry-foundations/locally-blueprinted-space|locally blueprinted space]], the definition does not require every stalk to have a unique maximal ideal. An [[algebraic-geometry-foundations/ordered-blue-scheme|ordered blue scheme]] is an OBlpr-space that is locally isomorphic to the spectrum of an ordered blueprint.

## Reference

Matthew Baker and Oliver Lorscheid, [*The moduli space of matroids*, §4.1.3](https://arxiv.org/abs/1809.03542).
