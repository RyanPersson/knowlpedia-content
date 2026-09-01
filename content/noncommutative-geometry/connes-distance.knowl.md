+++
id = "noncommutative-geometry/connes-distance"
title = "Connes spectral distance"
kind = "definition"
summary = "The extended distance between states obtained by maximizing their difference over the spectral Lipschitz unit ball."
aliases = ["spectral distance", "Connes distance formula"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/spectral-triple", "operator-algebras/state-cstar-algebra", "noncommutative-geometry/lipschitz-seminorm-spectral-triple"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((\mathcal A,H,D)\) be a unital [[noncommutative-geometry/spectral-triple|spectral triple]], and let \(\varphi,\psi\) be [[operator-algebras/state-cstar-algebra|states]] on the \(C^*\)-completion of \(\mathcal A\). Their **Connes spectral distance** is
\[
d_D(\varphi,\psi)=
\sup\left\{
|\varphi(a)-\psi(a)|:
a=a^*,\quad a\in\mathcal A,
L_D(a)\leq1
\right\},
\]
where \(L_D\) is the [[noncommutative-geometry/lipschitz-seminorm-spectral-triple|spectral Lipschitz seminorm]]. The value may be \(+\infty\). It is an extended pseudometric in general and becomes an extended metric when the kernel of \(L_D\) on self-adjoint elements consists only of scalars and the algebra separates states.

## Why it is a distance

Symmetry and the [[real-analysis/triangle-inequality|triangle inequality]] follow from the [[real-analysis/absolute-value|absolute value]] and
linearity of states. If \(L_D(a)=0\), every scalar multiple of \(a\) remains
admissible. Hence two states differing on such an element are at infinite
distance. If all zero-seminorm self-adjoint elements are scalar, equality
\(d_D(\varphi,\psi)=0\) forces the states to agree on the dense algebra and
therefore on its completion.

Finiteness does not imply that \(d_D\) induces the
[[functional-analysis/weak-star-topology|weak-star topology]] on the
state space. In the compact quantum metric setting, one additionally asks
for the Lipschitz unit ball modulo scalars to be suitably totally bounded.

## Recovery of geodesic distance

For the canonical spin spectral triple of a connected closed Riemannian spin
manifold \(M\), evaluation at \(x\in M\) defines a pure state
\(\delta_x\). Because \(\lVert[\not D,f]\rVert\) is the [[real-analysis/supremum-norm|supremum norm]] of
\(df\), the dual formula for geodesic distance gives
\[
d_{\not D}(\delta_x,\delta_y)=d_{\mathrm{geo}}(x,y).
\]
Thus the operator \(D\) and its commutators recover the original metric on
points without referring to coordinates.

On the full state space of \(C(M)\), the same supremum gives the
Kantorovich–Rubinstein distance between
[[probability/probability-measure|probability measures]]. This extension
contains more metric information than the restriction to pure states.

## Conventions and scope

Using all \(a\in\mathcal A\) instead of only self-adjoint \(a\) gives the same
value for states when the seminorm is star-invariant, but the self-adjoint
formula makes reality explicit. Some authors impose \(\lVert a\rVert\leq1\)
as an extra cutoff in noncompact settings; that produces a bounded variant,
not the distance defined in the core.

**Warning.** [[functional-analysis/compact-resolvent|Compact resolvent]] alone
does not guarantee finite diameter or
weak-star metrizability. Degeneracies of the representation, a large
[[operator-algebras/commutant|commutant]] of \(D\), disconnected metric
components, or an insufficiently
small Lipschitz ball can yield zero or infinite distances.

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter VI, §1, especially the distance formula for the canonical commutative triple.
2. M. A. Rieffel, “Metrics on State Spaces,” *Documenta Mathematica* 4 (1999), 559–600. [DOI record](https://doi.org/10.4171/DM/68). Relevant: §§1–2 on state-space metrics defined by Lipschitz seminorms.
