+++
id = "algebra-fields-galois/local-field"
title = "Local field"
kind = "definition"
summary = "A nondiscrete locally compact topological field."
aliases = ["local fields", "locally compact nondiscrete field"]
domains = ["algebra-fields-galois", "topology", "langlands"]
prerequisites = ["topology/locally-compact-space", "algebra-fields-galois/nonarchimedean-local-field"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **local field** is a nondiscrete Hausdorff topological field whose underlying
space is [[topology/locally-compact-space|locally compact]].

Under this convention, the local fields are the
[[algebra-fields-galois/archimedean-local-field|archimedean local fields]]
\(\mathbb R\) and \(\mathbb C\), together with the
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local
fields]].

## Convention warning

Some authors reserve “local field” for the nonarchimedean cases. Statements in
harmonic analysis and the Langlands program should therefore say
“archimedean” or “nonarchimedean” whenever the distinction affects the
objects under discussion.

## Relation to global fields

The [[algebra-fields-galois/completion-at-place|completion]] \(F_v\) of a
[[langlands-letter/knowls/global-local-fields-completions|global field]] at a
place is a local field. Conversely, every local field arises as such a
completion, though not canonically from a unique global field.

## References

1. André Weil, *Basic Number Theory*, third edition, Springer, 1974,
   Chapter I.
2. Jean-Pierre Serre, *Local Fields*, Springer, 1979, Chapter I.
