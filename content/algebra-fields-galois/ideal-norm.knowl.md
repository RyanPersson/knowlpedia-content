+++
id = "algebra-fields-galois/ideal-norm"
title = "Absolute norm of an ideal"
kind = "definition"
summary = "The cardinality of the quotient by a nonzero integral ideal in a number ring."
aliases = ["ideal norm", "absolute ideal norm"]
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/ring-of-integers", "algebra-rings/ideal", "algebra-rings/quotient-ring"]
+++

For a nonzero [[algebra-rings/ideal|integral ideal]] \(\mathfrak a\subseteq\mathcal O_K\) in the [[algebra-fields-galois/ring-of-integers|ring of integers]] of a number field, its **absolute norm** is
\[
N\mathfrak a=|\mathcal O_K/\mathfrak a|=[\mathcal O_K:\mathfrak a].
\]
The quotient is finite; this index is taken for the additive groups. The unit ideal has norm one.

## Examples and distinction

For \(K=\mathbb Q\), \(N(n\mathbb Z)=|n|\) when \(n\ne0\). In a degree-\(r\) number field, \(N(n\mathcal O_K)=|n|^r\).

The ideal norm takes an ideal as input. The [[algebra-fields-galois/norm-field|field norm]] takes an element; they are related by \(N(\alpha\mathcal O_K)=|N_{K/\mathbb Q}(\alpha)|\) for nonzero integral \(\alpha\).

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), §4, ideal norm and lattice index.
