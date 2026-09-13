+++
id = "partial-differential-equations/formal-and-holonomic-solution"
title = "Formal and holonomic solutions"
kind = "definition"
summary = "A formal solution assigns allowed jets; a holonomic one is the actual jet of a section."
aliases = ["formal solution", "holonomic solution"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/first-order-differential-relation", "fiber-bundles/section-of-a-fiber-bundle", "fiber-bundles/jet-bundle"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a [[partial-differential-equations/first-order-differential-relation|relation]] \(\mathcal R\subset J^1E\), a **formal solution** is a smooth [[fiber-bundles/section-of-a-fiber-bundle|section]] \(\sigma:M\to J^1E\) whose image lies in \(\mathcal R\). It is **holonomic** if \(\sigma=j^1s\) for a section \(s\) of \(E\), using its actual [[fiber-bundles/jet-bundle|first jet]].

## Compatibility

Locally a formal solution consists of values \(y(x)\) and assigned derivatives \(A(x)\). Holonomicity requires \(A=Dy\); pointwise membership in \(\mathcal R\) alone does not enforce this compatibility.

## References

- [Massot, h-principle course, Chapters 1–2](https://www.imo.universite-paris-saclay.fr/~patrick.massot/enseignement/h-principe/poly.pdf).
