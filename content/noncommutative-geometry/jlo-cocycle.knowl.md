+++
id = "noncommutative-geometry/jlo-cocycle"
title = "Jaffe–Leśniewski–Osterwalder cocycle"
kind = "definition"
summary = "An entire cyclic cocycle constructed from heat kernels and Dirac commutators of a theta-summable spectral triple."
aliases = ["JLO cocycle", "entire Chern character", "heat-kernel Chern character"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/theta-summable-spectral-triple", "noncommutative-geometry/entire-cyclic-cohomology"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((\mathcal A,H,D,\gamma)\) be an even
[[noncommutative-geometry/theta-summable-spectral-triple|theta-summable spectral triple]].
Its **Jaffe–Leśniewski–Osterwalder cocycle** is the sequence of even cochains
\[
\Phi_{2n}(a_0,\ldots,a_{2n})
=\int_{\Delta_{2n}}\operatorname{Tr}\!\left(
\gamma a_0e^{-t_0D^2}[D,a_1]e^{-t_1D^2}\cdots
[D,a_{2n}]e^{-t_{2n}D^2}\right)\,dt,
\]
where \(\Delta_m=\{(t_0,\ldots,t_m):t_j\geq0,\ \sum_jt_j=1\}\). Theta
summability makes the integrand trace class and provides the growth estimates
for an entire cochain. The identities \((b+B)\Phi=0\) make \(\Phi\) an
[[noncommutative-geometry/entire-cyclic-cohomology|entire cyclic cocycle]],
whose class is
the entire Chern character of the triple.

## Why the formula converges

The heat factors distribute a total heat time of one among the commutators.
Hölder inequalities for trace ideals, together with
\(\operatorname{Tr}(e^{-tD^2})<\infty\), control the integrand near the faces
of the simplex. The simplex volume supplies factorial decay in the cochain
degree. These estimates establish the entire-growth condition, not merely
termwise finiteness.

## Cohomological meaning

The JLO class is invariant under suitable differentiable deformations of the
unbounded cycle. Under stronger summability hypotheses, it represents the
same periodic cyclic-cohomology class as the Chern character of the associated
bounded [[noncommutative-geometry/fredholm-module|Fredholm module]]. The heat-kernel formula is especially useful when no
finite degree alone captures the character.

## Odd case and conventions

For an [[noncommutative-geometry/odd-spectral-triple|odd spectral triple]] there is no grading operator \(\gamma\); the odd
JLO character is expressed by odd-degree cochains, equivalently through a
standard suspension construction. Normalizing constants and rescaling \(D\)
vary across sources, but they do not change the underlying cohomology class
when the corresponding conventions are used consistently.

## References

1. A. Jaffe, A. Leśniewski, and K. Osterwalder, “Quantum K-Theory. I. The Chern Character,” *Communications in Mathematical Physics* 118 (1988), 1–14. [DOI record](https://doi.org/10.1007/BF01218474). Relevant: the heat-kernel cocycle, entire estimates, and Chern character.
2. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-maintained text](https://www.alainconnes.org/docs/book94bigpdf.pdf). Relevant: chapter IV on theta-summable Fredholm modules and the JLO entire cocycle.
