+++
id = "topology/locally-profinite-group"
title = "Locally profinite group"
kind = "definition"
summary = "A locally compact totally disconnected Hausdorff group, equivalently one with compact-open subgroups forming an identity basis."
aliases = ["locally profinite topological group", "totally disconnected locally compact group", "tdlc group", "t.d.l.c. group"]
domains = ["topology", "harmonic-analysis", "langlands"]
section_mode = "progressive"
+++

A **locally profinite group** is a Hausdorff
[[topology/topological-group|topological group]] that is
[[topology/locally-compact-group|locally compact]] and totally disconnected.

By van Dantzig's theorem, this is equivalent to requiring that the identity
have a neighborhood basis consisting of compact open subgroups.  A compact
locally profinite group is a profinite group.

## Examples

- The additive and multiplicative groups of a
  [[langlands-letter/knowls/global-local-fields-completions|nonarchimedean
  local field]] are
  locally profinite.
- If \(G\) is an
  [[algebraic-geometry-foundations/algebraic-group|algebraic group]] over
  such a field \(F\), then \(G(F)\) is
  locally profinite.
- Every discrete group is locally profinite: the
  [[algebra-groups/trivial-subgroup|trivial subgroup]] is compact and open.

## Representation theory

A representation on a discrete [[linear-algebra/vector-space|vector space]] is
[[harmonic-analysis/smooth-representation-totally-disconnected-group|smooth]]
exactly when every vector is fixed by some compact open subgroup.  Compact-open
fixed spaces define [[harmonic-analysis/admissible-representation-p-adic-group|admissibility]],
and compactly supported locally constant functions form the
[[harmonic-analysis/hecke-algebra-locally-compact-group-pair|Hecke algebra]].

## References

1. David van Dantzig, “Zur topologischen Algebra. III. Brouwersche und
   Cantorsche Gruppen,” *Compositio Mathematica* 3 (1936), 408–426.
   [Numdam](https://www.numdam.org/item/CM_1936__3__408_0/).
2. George W. Mackey, “Induced representations of locally compact groups I,”
   *Annals of Mathematics* 55 (1952), 101–139.
