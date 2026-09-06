+++
id = "algebraic-geometry-foundations/d-module"
title = "D-module"
kind = "definition"
summary = "A quasi-coherent sheaf module over the sheaf of differential operators on a smooth algebraic variety."
aliases = ["D-module", "D module"]
domains = ["algebraic-geometry-foundations", "langlands"]
prerequisites = ["algebraic-geometry-foundations/sheaf-of-differential-operators", "algebraic-geometry-foundations/sheaf-of-modules"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a smooth algebraic variety in characteristic \(0\). A
**left \(D\)-module** on \(X\) is a sheaf \(\mathcal M\) of left modules over
the [[algebraic-geometry-foundations/sheaf-of-differential-operators|sheaf
\(\mathcal D_X\) of differential operators]] whose underlying
\(\mathcal O_X\)-module is quasi-coherent. Right \(D\)-modules are defined
similarly.

## Flat connections

An \(\mathcal O_X\)-coherent \(D\)-module is equivalently a finite-rank
locally free \(\mathcal O_X\)-module with an
[[algebraic-geometry-foundations/integrable-connection|integrable
connection]]. General \(D\)-modules need not be coherent over
\(\mathcal O_X\); they allow singularities and distribution-like objects.

## Stacks and derived categories

For a suitable [[algebraic-geometry-foundations/algebraic-stack|algebraic stack]] \(\mathcal X\), \(D\)-modules can be defined by
descent from smooth charts. In geometric Langlands,
\(D\text{-}\operatorname{mod}(\mathcal X)\) usually denotes a stable derived
category; its precise descent and functorial conventions must be fixed
separately from the variety-level definition above.

## References

1. Alexander Beilinson and Joseph Bernstein, “A proof of Jantzen
   conjectures,” in *I. M. Gelfand Seminar*, Advances in Soviet Mathematics
   16 (1993), 1–50.
2. Masaki Kashiwara, “On the maximally overdetermined system of linear
   differential equations I,” *Publ. RIMS* 10 (1975), 563–579.
   [DOI](https://doi.org/10.2977/prims/1195191894).
