+++
id = "algebra-fields-galois/number-field-discriminant"
title = "Discriminant of a number field"
kind = "definition"
summary = "The trace-pairing discriminant of an integral basis, independent of that basis."
aliases = ["field discriminant", "absolute discriminant"]
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/integral-basis", "algebra-fields-galois/discriminant-field"]
+++

The **discriminant** \(D_K\) of a number field \(K\) is the [[algebra-fields-galois/discriminant-field|basis discriminant]] of any [[algebra-fields-galois/integral-basis|integral basis]] \((\omega_1,\ldots,\omega_n)\):
\[
D_K=\det\bigl(\operatorname{Tr}_{K/\mathbb Q}(\omega_i\omega_j)\bigr)_{i,j=1}^n.
\]
It is a nonzero integer independent of the chosen integral basis. The **absolute discriminant** is \(|D_K|\).

## Independence

An integral change of basis has determinant \(\pm1\). It changes the trace matrix to \(P^{\mathsf T}TP\), leaving its determinant unchanged. An arbitrary rational basis need not give the same number.

## Imaginary quadratic case

For \(K=\mathbb Q(\sqrt{-d})\), \(d>0\) square-free, the [[algebra-fields-galois/imaginary-quadratic-ring-of-integers|explicit integral basis]] gives
\[
D_K=\begin{cases}-d,&d\equiv3\pmod4,\\-4d,&d\equiv1,2\pmod4.\end{cases}
\]
Thus \(D_{\mathbb Q(i)}=-4\), while \(D_{\mathbb Q(\sqrt{-3})}=-3\).

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §2, “Discriminants,” and Definition 2.32.
