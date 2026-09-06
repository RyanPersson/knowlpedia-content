+++
id = "noncommutative-geometry/tau-summable-spectral-triple"
title = "Tau-summable semifinite spectral triple"
kind = "definition"
summary = "A semifinite spectral triple whose resolvent has finite noncommutative lp norm with respect to the chosen trace."
aliases = ["semifinite p-summability", "tau-p-summable triple"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/semifinite-spectral-triple", "operator-algebras/faithful-normal-semifinite-trace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((\mathcal A,\mathcal N,D,\tau)\) be a [[noncommutative-geometry/semifinite-spectral-triple|semifinite spectral triple]], where \(\tau\) is a [[operator-algebras/faithful-normal-semifinite-trace|faithful normal semifinite trace]] on \(\mathcal N\), and let \(p>0\). The triple is **tau-\(p\)-summable** if
\[
(1+D^2)^{-1/2}\in L^p(\mathcal N,\tau),
\]
equivalently,
\[
\tau\!\left((1+D^2)^{-p/2}\right)<\infty.
\]
Here \(D\) is self-adjoint and affiliated with \(\mathcal N\), its algebra commutators are bounded, and its resolvent is tau-compact. Thus summability is measured by generalized singular values and \(\tau\), not by ordinary eigenvalue multiplicities. For a nonunital algebra, the local convention usually requires \(a(1+D^2)^{-1/2}\in L^p(\mathcal N,\tau)\) for every \(a\in\mathcal A\) instead.

## Equivalent decay formulation

Writing \(\mu_t\) for the generalized singular-value function, tau-\(p\)-summability is equivalent to
\[
\int_0^\infty \mu_t\!\left((1+D^2)^{-1/2}\right)^p\,dt<\infty.
\]
Weak tau-\(p\)-summability replaces \(L^p\) by the corresponding weak ideal and permits the borderline decay \(O(t^{-1/p})\). The strong and weak conditions are not interchangeable; the latter is the natural endpoint in many dimension-\(p\) examples.

## Examples and conventions

For \(\mathcal N=B(H)\) with the usual trace, \(L^p(\mathcal N,\tau)\) is the Schatten class, so the definition is ordinary \(p\)-summability. Finite trace alone does not make every affiliated resolvent \(p\)-summable: the displayed trace must still be finite.

Some authors call the triple \(p\)-summable when \((1+D^2)^{-s/2}\) is trace-class for every \(s>p\), reserving “\(p^+\)-summable” or “weakly \(p\)-summable” for the critical endpoint. Any assertion of [[noncommutative-geometry/metric-dimension|metric dimension]] should state which convention is in force.

## References

1. A. L. Carey, J. Phillips, A. Rennie, and F. A. Sukochev, “The Hochschild Class of the Chern Character for Semifinite Spectral Triples,” *Journal of Functional Analysis* 213 (2004), 111–153. [DOI record](https://doi.org/10.1016/j.jfa.2003.11.016). Relevant: §2 on semifinite spectral triples and \((p,\infty)\)-summability.
2. A. L. Carey, J. Phillips, A. Rennie, and F. A. Sukochev, “The Local Index Formula in Semifinite von Neumann Algebras I: Spectral Flow,” *Advances in Mathematics* 202 (2006), 451–516. [DOI record](https://doi.org/10.1016/j.aim.2005.03.011). Relevant: §2 on trace ideals, generalized singular values, and summability.
