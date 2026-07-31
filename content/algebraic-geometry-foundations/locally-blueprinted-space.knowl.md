+++
id = "algebraic-geometry-foundations/locally-blueprinted-space"
title = "Locally blueprinted space"
kind = "definition"
summary = "A topological space with a sheaf of blueprints whose stalks are local blueprints."
aliases = ["locally blueprint ringed space", "LocBlpr-space"]
domains = ["algebraic-geometry-foundations"]
section_mode = "progressive"
+++

A **blueprinted space** is a topological space \(X\) together with a sheaf \(\mathcal O_X\) of [[algebraic-geometry-foundations/blueprint|blueprints]]. It is **locally blueprinted** if every stalk \(\mathcal O_{X,x}\) is a local blueprint, meaning that it has a unique maximal ideal \(\mathfrak m_x\).

A morphism
\[
(f,f^\#):(X,\mathcal O_X)\longrightarrow(Y,\mathcal O_Y)
\]
of locally blueprinted spaces consists of a continuous map \(f:X\to Y\) and a morphism of sheaves
\[
f^\#:\mathcal O_Y\longrightarrow f_*\mathcal O_X
\]
such that the induced map on every stalk
\[
f_x^\#:\mathcal O_{Y,f(x)}\longrightarrow\mathcal O_{X,x}
\]
is local: it sends the maximal ideal of the source into the maximal ideal of the target.

The resulting category is commonly denoted \(\mathbf{LocBlprSp}\). [[algebraic-geometry-foundations/blue-scheme|Blue schemes]] form the full subcategory of locally blueprinted spaces that admit affine open covers by blueprint spectra.

## Reference

Oliver Lorscheid, [*The geometry of blueprints, Part I: Algebraic background and scheme theory*, §3.1](https://arxiv.org/abs/1103.1745).
