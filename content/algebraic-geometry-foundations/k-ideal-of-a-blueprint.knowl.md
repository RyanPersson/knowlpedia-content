+++
id = "algebraic-geometry-foundations/k-ideal-of-a-blueprint"
title = "\\(k\\)-ideal of a blueprint"
kind = "definition"
summary = "A multiplicative ideal of a blueprint that is closed under subtraction encoded by additive relations."
aliases = ["subtractive ideal of a blueprint", "blueprint k-ideal"]
domains = ["algebraic-geometry-foundations", "algebra-rings"]
section_mode = "progressive"
+++

Let \(B\) be a [[algebraic-geometry-foundations/blueprint|blueprint]]. A **\(k\)-ideal** of \(B\) is a subset \(I\subseteq B^\bullet\) such that:

1. \(0\in I\);
2. \(BI\subseteq I\);
3. whenever an additive relation
   \[
   \sum_{i=1}^{n}a_i+c\equiv\sum_{j=1}^{m}b_j
   \]
   holds in \(B\), with every \(a_i,b_j\in I\), then \(c\in I\).

The third axiom is the subtractive condition. For a blueprint induced by a semiring, it specializes to the usual condition that \(x,x+y\in I\) implies \(y\in I\).

A proper \(k\)-ideal \(\mathfrak p\) is **prime** if its complement \(B^\bullet\setminus\mathfrak p\) is multiplicatively closed. These prime \(k\)-ideals are the points of the [[algebraic-geometry-foundations/spectrum-of-blueprint|prime spectrum of a blueprint]].

## Reference

Oliver Lorscheid, [*The geometry of blueprints, Part I: Algebraic background and scheme theory*, §§2.1–2.2](https://arxiv.org/abs/1103.1745).
