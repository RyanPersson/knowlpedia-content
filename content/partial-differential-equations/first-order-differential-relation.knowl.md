+++
id = "partial-differential-equations/first-order-differential-relation"
title = "First-order differential relation"
kind = "definition"
summary = "A subset of a first jet bundle that specifies allowed values and first derivatives."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/jet-bundle", "fiber-bundles/section-of-a-fiber-bundle", "shared-foundations/subset"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **first-order differential relation** for sections of a smooth bundle \(E\to M\) is a [[shared-foundations/subset|subset]] \(\mathcal R\subset J^1E\) of its [[fiber-bundles/jet-bundle|first jet bundle]]. A solution is a smooth [[fiber-bundles/section-of-a-fiber-bundle|section]] \(s\) of \(E\) with \(j_x^1s\in\mathcal R\) for every \(x\in M\).

## Coordinate form

The relation prescribes allowed triples \((x,y,A)\) of base point, value, and derivative. Equalities and inequalities on these triples can both define relations.

## References

- [Massot, h-principle course, Chapters 1–2](https://www.imo.universite-paris-saclay.fr/~patrick.massot/enseignement/h-principe/poly.pdf).
