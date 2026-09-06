+++
id = "noncommutative-geometry/p-summable-fredholm-module"
title = "p-summable Fredholm module"
kind = "definition"
summary = "A Fredholm module whose algebra commutators belong to the Schatten ideal of order p."
aliases = ["finitely summable Fredholm module", "p-summable bounded K-cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/fredholm-module", "operator-algebras/involutive-algebra", "functional-analysis/schatten-class-operator"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(p>0\), and let \((H,\pi,F)\) be a normalized [[noncommutative-geometry/fredholm-module|Fredholm module]] over a complex [[operator-algebras/involutive-algebra|involutive algebra]] \(\mathcal A\), so \(F=F^*\), \(F^2=I\), and \([F,\pi(a)]\) is compact for every \(a\in\mathcal A\). The module is **\(p\)-summable** when
\[
[F,\pi(a)]\in\mathcal L^p(H)
\qquad\text{for every }a\in\mathcal A,
\]
where \(\mathcal L^p(H)\) is the [[functional-analysis/schatten-class-operator|Schatten ideal]]. Thus summability strengthens compactness by prescribing an \(\ell^p\) decay rate for the commutator singular values.

## Parity and the Chern character

Summability is compatible with either [[noncommutative-geometry/even-fredholm-module|even]] or [[noncommutative-geometry/odd-fredholm-module|odd]] parity. If \(n\) has the module's parity and \(n>p-1\), Hölder's inequality for Schatten ideals makes
the standard conditional-trace formula well defined:
\[
\phi_n(a_0,\ldots,a_n)
=\lambda_n\operatorname{Tr}_0\!\left(
\Gamma\pi(a_0)[F,\pi(a_1)]\cdots[F,\pi(a_n)]\right).
\]
Here \(\Gamma\) is the grading operator in the even case and \(I\) in the odd
case, \(\lambda_n\) is the chosen standard normalization constant, and
\[
\operatorname{Tr}_0(T)
=\tfrac12\operatorname{Tr}\!\bigl(F(FT+TF)\bigr).
\]
This cocycle represents the [[noncommutative-geometry/chern-character-fredholm-module|Chern character of the Fredholm module]]. By contrast, ordinary Schatten Hölder makes the displayed product itself trace class only when \(n\geq p\). The resulting class lies in [[noncommutative-geometry/periodic-cyclic-cohomology|periodic cyclic cohomology]] and pairs with \(K\)-theory to recover the Fredholm index.

## Algebra and topology matter

Summability is normally required on a specified dense smooth subalgebra \(\mathcal A\) of a represented \(C^*\)-algebra, not automatically on every element of its norm completion. The property can therefore change when the chosen smooth algebra changes. For a Banach or locally convex algebra one also requires the representation and commutator map to have the appropriate continuity.

If the condition holds at exponent \(p\), it holds at every exponent \(q>p\), because \(\mathcal L^p\subset\mathcal L^q\). The least viable exponent, when it exists, records the dimension-like decay of the cycle.

## Conventions and scope

For an unnormalized Fredholm module, authors may impose Schatten conditions on the self-adjointness and involutivity defects as well as on commutators; the core avoids this ambiguity by using a normalized representative. Some sources say “\(p\)-summable” when commutators lie only in the weak ideal \(\mathcal L^{p,\infty}\). Here \(p\)-summable means strict Schatten membership. When \(0<p<1\), \(\mathcal L^p\) is a quasi-Banach ideal, but the membership condition remains meaningful.

Do not confuse a \(p\)-summable Fredholm module with a [[noncommutative-geometry/p-summable-spectral-triple|\(p\)-summable spectral triple]]: bounded transformation relates the two notions, but the summability exponent of the resulting commutators requires a separate estimate.

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-maintained text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter IV, §1 on finitely summable Fredholm modules and their characters.
2. A. Connes, “Non-Commutative Differential Geometry,” *Publications Mathématiques de l'IHÉS* 62 (1985), 41–144. [DOI record](https://doi.org/10.1007/BF02698807). Relevant: §§II.1–II.3 on summable Fredholm modules and cyclic cocycles.
3. N. Higson and J. Roe, *Analytic K-Homology*, Oxford University Press, 2000. [Publisher record](https://doi.org/10.1093/oso/9780198511762.001.0001). Relevant: bounded Fredholm modules and analytic \(K\)-homology.
