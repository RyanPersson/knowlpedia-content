+++
id = "algebra-fields-galois/imaginary-quadratic-ring-of-integers"
title = "Ring of integers of an imaginary quadratic field"
kind = "theorem"
summary = "The explicit integral basis according to the square-free parameter modulo four."
aliases = []
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/imaginary-quadratic-field", "algebra-fields-galois/ring-of-integers", "algebra-fields-galois/trace-field", "algebra-fields-galois/norm-field"]
+++

For the [[algebra-fields-galois/imaginary-quadratic-field|imaginary quadratic field]] \(K=\mathbb Q(\sqrt{-d})\), where \(d>0\) is square-free, the [[algebra-fields-galois/ring-of-integers|ring of integers]] is
\[
\mathcal O_K=\begin{cases}
\mathbb Z[(1+\sqrt{-d})/2],&d\equiv3\pmod4,\\
\mathbb Z[\sqrt{-d}],&d\equiv1,2\pmod4.
\end{cases}
\]
Square-freeness excludes \(d\equiv0\pmod4\).

## Why the half-integer occurs

An element of a quadratic field is integral exactly when its trace and norm are integers. Write it as \((a+b\sqrt{-d})/2\). These conditions force \(a,b\in\mathbb Z\) and \(a^2+db^2\equiv0\pmod4\). Either both are even, or both are odd and \(d\equiv3\pmod4\). This gives precisely the displayed rings.

## Examples

For \(d=1\) this is the Gaussian integer ring. For \(d=3\) it is the Eisenstein integer ring, which can equally be written \(\mathbb Z[(-1+\sqrt{-3})/2]\).

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), Introduction and §2, Remark 2.12.
