+++
id = "algebraic-geometry-foundations/d-module"
title = "D-module"
kind = "definition"
summary = "A sheaf module over the sheaf of differential operators on a smooth variety or stack."
aliases = ["D-module", "D module"]
domains = ["algebraic-geometry-foundations", "langlands"]
section_mode = "progressive"
+++

Let \(X\) be a smooth algebraic variety in characteristic \(0\). A
**left \(D\)-module** on \(X\) is a sheaf \(\mathcal M\) of left modules over
the [[algebraic-geometry-foundations/sheaf-of-differential-operators|sheaf
\(\mathcal D_X\) of differential operators]] whose underlying
\(\mathcal O_X\)-module is quasi-coherent. Right \(D\)-modules are defined
similarly.

## Flat connections

An \(\mathcal O_X\)-coherent \(D\)-module is equivalently a vector bundle with
integrable connection. General \(D\)-modules allow singularities and
distribution-like objects, so they form a substantially larger category.

## Stacks and derived categories

For an algebraic stack such as
\(\operatorname{Bun}_G\), the category \(D\text{-}\operatorname{mod}(X)\) is
defined by descent from smooth charts and is treated as a stable derived
category in modern geometric Langlands. Functorial operations are derived and
require hypotheses on the maps.

## References

1. Alexander Beilinson and Joseph Bernstein, “A proof of Jantzen
   conjectures,” in *I. M. Gelfand Seminar*, Advances in Soviet Mathematics
   16 (1993), 1–50.
2. Masaki Kashiwara, “On the maximally overdetermined system of linear
   differential equations I,” *Publ. RIMS* 10 (1975), 563–579.
   [DOI](https://doi.org/10.2977/prims/1195191894).
