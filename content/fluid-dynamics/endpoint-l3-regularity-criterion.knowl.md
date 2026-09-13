+++
id = "fluid-dynamics/endpoint-l3-regularity-criterion"
title = "Endpoint L-infinity-in-time L3 regularity criterion"
kind = "theorem"
summary = "An unforced three-dimensional Leray–Hopf solution bounded in L3 uniformly in time is regular at positive times."
aliases = ["Escauriaza–Seregin–Šverák criterion"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/leray-hopf-solution", "partial-differential-equations/regularity-criterion", "measure-theory/mixed-lebesgue-norm", "real-analysis/class-ck-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(u\) be an unforced three-dimensional [[fluid-dynamics/leray-hopf-solution|Leray–Hopf solution]] on \(\mathbb R^3\times(0,T)\). The **Escauriaza–Seregin–Šverák endpoint criterion** asserts that
\[
u\in L^\infty(0,T;L^3(\mathbb R^3))
\]
implies regularity at positive times, including absence of a singularity at the terminal time \(T\). In particular the velocity is [[real-analysis/class-ck-function|smooth]] in the interior positive-time region.

The hypothesis is a [[measure-theory/mixed-lebesgue-norm|mixed time-space norm]] in this [[partial-differential-equations/regularity-criterion|regularity criterion]].

## Reading the notation

The condition is the [[measure-theory/mixed-lebesgue-norm|mixed norm]] \(\operatorname*{ess\,sup}_{0<t<T}\|u(t)\|_{L^3_x}<\infty\). The original notation \(L_{3,\infty}\) refers here to spatial exponent three and time exponent infinity. It does not replace \(L^3_x\) by the weak Lorentz space \(L^{3,\infty}_x\). This is an unforced [[partial-differential-equations/regularity-criterion|criterion]] with its own solution hypotheses.

## References

- [Escauriaza, Seregin and Šverák, L3,infinity solutions and backward uniqueness (2003)](https://www.mathnet.ru/eng/rm609).
