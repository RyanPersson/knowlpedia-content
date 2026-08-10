+++
id = "harmonic-analysis/smooth-representation-totally-disconnected-group"
title = "Smooth representation of a totally disconnected group"
kind = "definition"
summary = "A representation in which every vector is fixed by an open subgroup."
aliases = ["smooth representation of a locally profinite group", "smooth p-adic representation"]
domains = ["harmonic-analysis", "langlands", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a totally disconnected [[topology/locally-compact-group|locally compact group]]. A complex
representation \((\pi,V)\) of \(G\) is **smooth** if every vector has an open
stabilizer:

\[
V=\bigcup_{K\leq G\text{ open}}V^K,
\qquad
V^K=\{v\in V:\pi(k)v=v\text{ for all }k\in K\}.
\]

Equivalently, every orbit map \(g\mapsto\pi(g)v\) is locally constant. No
topology on \(V\) is part of this algebraic notion of smoothness.

## Smooth vectors

If a continuous representation is initially given on a topological vector
space, its smooth part is the union of its open-subgroup fixed spaces. This is
different from differentiable smooth vectors for a real [[fiber-bundles/lie-group|Lie group]].

## Hecke action

For compact open \(K\leq G\), the fixed space \(V^K\) carries an action of the
[[harmonic-analysis/hecke-algebra-locally-compact-group-pair|Hecke algebra]]
\(\mathcal H(G,K)\). Much of nonarchimedean representation theory studies a
smooth representation through these fixed spaces as \(K\) varies.

## References

1. Joseph Bernstein and Andrei Zelevinsky, “Induced representations of
   reductive \(p\)-adic groups I,” *Annales scientifiques de l’École Normale
   Supérieure* 10 (1977), 441–472.
   [Numdam](https://www.numdam.org/item/ASENS_1977_4_10_4_441_0/).
2. Jayce R. Getz, *An Introduction to Automorphic Representations*, §§5 and
   10.9. [Author notes](https://sites.math.duke.edu/~jgetz/aut_reps.pdf).
