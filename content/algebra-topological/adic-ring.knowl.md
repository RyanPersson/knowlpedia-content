+++
id = "algebra-topological/adic-ring"
title = "Adic ring"
kind = "definition"
summary = "A topological ring whose topology is defined by the powers of a finitely generated ideal."
aliases = ["I-adic ring"]
domains = ["algebra-topological", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

An **adic ring** is a commutative topological ring \(A\) whose topology is the
\(I\)-adic topology for some finitely generated
[[algebra-topological/ideal-of-definition|ideal of definition]] \(I\subseteq
A\). Thus the powers \(I^n\) form a neighborhood basis of \(0\).

The ring is **separated** if
\[
\bigcap_{n\geq 1} I^n=0,
\]
and it is **complete** if every compatible family of residue classes modulo
the \(I^n\) is represented by an element of \(A\). Equivalently, \(A\) is
complete and separated exactly when the canonical map
\[
A\longrightarrow\varprojlim_n A/I^n
\]
is an isomorphism. A **complete adic ring** means an adic ring that is
complete and separated.

## Independence of the defining ideal

Different ideals of definition can determine the same topology. Because
their powers are cofinal, separatedness and completeness depend on the adic
topology, not on the chosen ideal.

For example, the formal power-series ring
\[
R[[X_1,\ldots,X_n]]
\]
is complete and separated for the \((X_1,\ldots,X_n)\)-adic topology.

## Formal spectrum

A complete adic ring \(A\) determines the
[[algebraic-geometry-foundations/formal-spectrum|formal spectrum]]
\(\operatorname{Spf}(A)\). Continuous homomorphisms of complete adic rings
induce morphisms of formal spectra in the opposite direction.

## References

1. The Stacks Project Authors, “Topological rings and modules.”
   [Section 15.36, Tag 07E8](https://stacks.math.columbia.edu/tag/07E8).
2. The Stacks Project Authors, “Formal schemes à la EGA.”
   [Section 87.2, Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY).
