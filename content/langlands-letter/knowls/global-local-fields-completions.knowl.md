+++
id = "langlands-letter/knowls/global-local-fields-completions"
title = "Global field"
kind = "definition"
summary = "A number field or a one-variable function field over a finite field."
aliases = ["global field", "global fields"]
domains = ["algebra-fields-galois", "langlands-letter"]
legacy_source_path = "langlands-letter/knowls/global-local-fields-completions.md"
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/number-field", "algebra-fields-galois/global-function-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **global field** is a field isomorphic either to a
[[algebra-fields-galois/number-field|number field]] or to a
[[algebra-fields-galois/global-function-field|global function field]].
Equivalently, it is a finite extension of \(\mathbb Q\) or of
\(\mathbb F_q(t)\) for some prime power \(q\).

## Places and completions

Every nontrivial [[algebra-fields-galois/place-of-global-field|place]] \(v\)
of a global field \(F\) determines a
[[algebra-fields-galois/completion-at-place|completion]] \(F_v\). These
completions are [[algebra-fields-galois/local-field|local fields]]. Thus the
arithmetic of one global field is studied simultaneously through all of its
localizations.

## The two cases

For a number field, the archimedean completions are \(\mathbb R\) or
\(\mathbb C\), and its nonarchimedean completions are finite extensions of
\(\mathbb Q_p\). A global function field has no archimedean places; all of its
completions have positive characteristic.

## Langlands role

Global automorphic objects live over \(F\) or its adele ring, while their
local components live over the fields \(F_v\). The number-field and
function-field versions of the Langlands program share this local--global
architecture even though their geometric tools differ.

## References

1. John W. S. Cassels and Albrecht Fröhlich, eds., *Algebraic Number
   Theory*, Academic Press, 1967.
2. Michael Rosen, *Number Theory in Function Fields*, Springer, 2002.
