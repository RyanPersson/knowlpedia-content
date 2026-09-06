+++
id = "noncommutative-geometry/even-fredholm-module"
title = "Even Fredholm module"
kind = "definition"
summary = "A Fredholm module on a graded Hilbert space whose representation is even and whose Fredholm operator is odd."
aliases = ["graded Fredholm module", "even bounded K-cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
prerequisites = ["noncommutative-geometry/fredholm-module", "functional-analysis/z2-graded-hilbert-space", "operator-algebras/graded-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a trivially graded complex \(C^*\)-algebra. An **even Fredholm module over \(A\)** is a [[noncommutative-geometry/fredholm-module|Fredholm module]] \((H,\pi,F)\) together with a [[functional-analysis/z2-graded-hilbert-space|\(\mathbb Z/2\)-grading]] operator \(\Gamma\) such that
\[
\Gamma=\Gamma^*,\qquad \Gamma^2=I,\qquad
\Gamma\pi(a)=\pi(a)\Gamma,\qquad \Gamma F=-F\Gamma
\]
for every \(a\in A\). Thus \(\pi\) is even and \(F\) is an [[operator-algebras/graded-operator|odd operator]]. In the unnormalized convention, the compact-defect conditions for \(F\) remain those of a Fredholm module. If \(A\) is itself graded, the commutation rule is replaced by the graded representation rule.

## Block form

Writing \(H=H^+\oplus H^-\) for the \(\pm1\) eigenspaces of \(\Gamma\), the operators have block form
\[
\pi(a)=
\begin{pmatrix}
\pi^+(a)&0\\
0&\pi^-(a)
\end{pmatrix},
\qquad
F=
\begin{pmatrix}
0&F^-\\
F^+&0
\end{pmatrix}.
\]
For a normalized module, \(F^-=(F^+)^*\) and the two off-diagonal operators are mutual inverses. Before normalization they are inverses modulo the locally compact defects specified in the Fredholm-module axioms. This is the form used to construct the [[noncommutative-geometry/even-index-pairing|even index pairing]].

## Structure and consequences

Even modules represent degree-zero classes in [[noncommutative-geometry/analytic-k-homology|analytic K-homology]]. Direct sum gives addition. Reversing the grading changes the sign of the represented class, subject to the accompanying standard convention for \(F\).

If an unbounded cycle has a grading that commutes with the algebra and anticommutes with its unbounded operator, its [[noncommutative-geometry/bounded-transform-spectral-triple|bounded transform]] is even. Thus the parity of an [[noncommutative-geometry/even-spectral-triple|even spectral triple]] survives passage to bounded K-homology.

## Examples and non-examples

Let \(M\) be a closed even-dimensional spin manifold. The spinor [[linear-algebra/hilbert-space|Hilbert space]] splits into positive and negative chirality, multiplication by \(C(M)\) preserves the split, and the bounded transform of the [[noncommutative-geometry/dirac-operator|Dirac operator]] interchanges the two summands. It therefore defines an even Fredholm module.

An [[noncommutative-geometry/odd-fredholm-module|ungraded Fredholm module]] is not automatically even: a grading \(\Gamma\) must exist and satisfy both displayed compatibility rules. In particular, a grading commuting with \(F\) fails the oddness axiom.

## References

1. [Alain Connes, *Noncommutative Geometry*, Chapter IV, Section 1 and Appendix A, Academic Press, 1994](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).
2. [Nigel Higson and John Roe, *Analytic K-Homology*, Chapter 8, Oxford University Press, 2000](https://doi.org/10.1093/oso/9780198511762.001.0001).
