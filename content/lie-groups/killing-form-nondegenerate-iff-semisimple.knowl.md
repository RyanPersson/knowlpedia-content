+++
id = "lie-groups/killing-form-nondegenerate-iff-semisimple"
title = "Killing form nondegeneracy criterion"
kind = "knowl"
summary = "A finite-dimensional Lie algebra is semisimple iff its Killing form is nondegenerate."
aliases = ["killing-form-nondegenerate-iff-semisimple", "Killing form nondegeneracy criterion"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/killing-form-nondegenerate-iff-semisimple.md"
prerequisites = ["lie-groups/lie-algebra", "lie-groups/killing-form", "lie-groups/semisimple-lie-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathfrak g\) be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over a field of characteristic \(0\), and let \(B\) be its [[lie-groups/killing-form|Killing form]].

**Theorem (Cartan criterion via Killing form).**
\(\mathfrak g\) is [[lie-groups/semisimple-lie-algebra|semisimple]] if and only if the Killing form \(B\) is nondegenerate.

## Remarks

The proof uses [[lie-groups/cartans-criterion-semisimplicity|Cartan’s criterion]] to relate the solvable radical of \(\mathfrak g\) to traces in the adjoint representation. Thus nondegeneracy is not merely a consequence of the adjoint representation being faithful; it detects the absence of nonzero solvable ideals.
