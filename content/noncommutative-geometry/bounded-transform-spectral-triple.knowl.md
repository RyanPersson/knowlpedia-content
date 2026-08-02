+++
id = "noncommutative-geometry/bounded-transform-spectral-triple"
title = "Bounded transform of a spectral triple"
kind = "definition"
summary = "The bounded operator obtained from a spectral triple's Dirac operator by the function x divided by the square root of one plus x squared."
aliases = ["bounded Fredholm transform", "bounded transform of an unbounded cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \((\mathcal A,H,D)\) be a [[noncommutative-geometry/spectral-triple|spectral triple]], with \(D\) densely defined and self-adjoint. Its **bounded transform** is the bounded self-adjoint contraction
\[
F_D=D(1+D^2)^{-1/2},
\]
defined by functional calculus. [[functional-analysis/compact-resolvent|Compact resolvent]] gives \(F_D^2-I=-(1+D^2)^{-1}\) compact, and the bounded-commutator axiom implies that \([F_D,a]\) is compact for every \(a\in\mathcal A\). Thus \((H,\pi,F_D)\) is a [[noncommutative-geometry/fredholm-module|Fredholm module]] in the compact-defect convention. If the spectral triple is even, its grading anticommutes with \(F_D\); otherwise the transform is odd.

## Why the transform is bounded

The scalar function
\[
f(x)=\frac{x}{\sqrt{1+x^2}}
\]
is real-valued and bounded by \(1\). The self-adjoint functional calculus therefore turns the generally unbounded \(D\) into a bounded self-adjoint operator. Its square tends to \(1\) at spectral infinity, while
\[
I-F_D^2=(1+D^2)^{-1}
\]
retains the compactness information. The transform preserves the sign of every nonzero spectral value but sends large magnitudes toward \(\pm1\).

The compactness of \([F_D,a]\) follows from the resolvent integral for \((1+D^2)^{-1/2}\) and the boundedness of \([D,a]\). This is the bounded-transform theorem of Baaj and Julg.

## K-homological role

The bounded transform forgets metric scale but retains the stable Fredholm data needed for [[noncommutative-geometry/analytic-k-homology|analytic K-homology]]. Homotopies satisfying the appropriate uniform unbounded-cycle hypotheses descend to operator homotopies of bounded cycles. The resulting class can then be paired with \(K\)-theory by the even or odd Fredholm index.

For a nonunital unbounded Kasparov cycle, compact resolvent is replaced by local compactness \(a(1+D^2)^{-1}\in K(H)\). The same formula then gives the local compact-defect conditions \(a(F_D^2-I)\in K(H)\).

## Example and distinction from the phase

For the spin [[noncommutative-geometry/dirac-operator|Dirac operator]] on a closed Riemannian spin manifold,
\[
D(1+D^2)^{-1/2}
\]
is an order-zero bounded operator and defines the manifold's analytic K-homology class. Its commutators with smooth functions are compact.

The bounded transform is not literally the phase \(\operatorname{sgn}(D)\). On \(\ker D\), both may be assigned \(0\), but on nonzero finite spectral values \(x/\sqrt{1+x^2}\neq\operatorname{sgn}(x)\). The two yield related normalized cycles only after an additional compact perturbation or kernel convention.

## References

1. [Saad Baaj and Pierre Julg, “Théorie bivariante de Kasparov et opérateurs non bornés dans les \(C^*\)-modules hilbertiens,” *Comptes rendus de l'Académie des sciences*, Série I 296 (1983), 875–878](https://zbmath.org/0551.46041).
2. [Alain Connes, *Noncommutative Geometry*, Appendix A, Theorem 15, Academic Press, 1994](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
