+++
id = "algebra-fields-galois/number-field"
title = "Number field"
kind = "definition"
summary = "A finite field extension of the rational numbers."
aliases = ["algebraic number field", "number fields"]
domains = ["algebra-fields-galois", "langlands"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/field-extension", "shared-foundations/rational-numbers"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **number field** is a finite
[[algebra-fields-galois/field-extension|field extension]]
\[
F/\mathbb Q
\]
of the [[shared-foundations/rational-numbers|rational numbers]]. Its degree is
the finite dimension \([F:\mathbb Q]\).

## Places and completions

The embeddings of \(F\) into \(\mathbb R\) and \(\mathbb C\) determine its
[[algebra-fields-galois/archimedean-local-field|archimedean places]]. Its
remaining places are nonarchimedean and lie above rational primes. Completing
at any [[algebra-fields-galois/place-of-global-field|place]] produces a
[[algebra-fields-galois/local-field|local field]].

## Position among global fields

Number fields are precisely the [[langlands-letter/knowls/global-local-fields-completions|global fields]]
of characteristic \(0\). The other global fields are the
[[algebra-fields-galois/global-function-field|global function fields]], which
have positive characteristic.

## References

1. Jürgen Neukirch, *Algebraic Number Theory*, Springer, 1999, Chapter I.
2. John W. S. Cassels and Albrecht Fröhlich, eds., *Algebraic Number
   Theory*, Academic Press, 1967.
