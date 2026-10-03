+++
id = "linear-algebra/proper-equivalence-binary-quadratic-forms"
title = "Proper equivalence of binary quadratic forms"
kind = "definition"
summary = "Equivalence under determinant-one integral changes of the two variables."
aliases = ["proper equivalence of quadratic forms", "proper form class"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/integral-binary-quadratic-form", "algebra-groups/special-linear-group-over-ring"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
Two [[linear-algebra/integral-binary-quadratic-form|integral binary quadratic forms]] \(f,g\) are **properly equivalent** if there is a matrix
\[
\gamma=\begin{pmatrix}r&s\\t&u\end{pmatrix}\in\operatorname{SL}_2(\mathbb Z)
\]
such that \(g(x,y)=f(rx+sy,tx+uy)\). Thus a proper form class is an orbit for determinant-one integral changes of variables. Allowing determinant \(-1\) as well gives a different, coarser equivalence relation.

## Preserved data

The discriminant changes by the square of the determinant of the substitution matrix, so proper equivalence preserves it. Primitivity is preserved because both the matrix and its inverse have integer entries. Positive definiteness is preserved by invertible real substitution.

## Quadratic ideals

For a negative fundamental discriminant \(D\), proper classes of primitive positive definite forms correspond to [[algebra-fields-galois/ideal-class-group|ideal classes]] of the quadratic field of discriminant \(D\). The construction sends \((a,b,c)\) to the ideal
\[
a\mathbb Z+\frac{-b+\sqrt D}{2}\mathbb Z.
\]
For nonfundamental discriminants the corresponding setting is the [[algebra-commutative/proper-ideal-of-order|proper invertible ideals]] of the quadratic order, rather than all ideals of its [[algebra-rings/maximal-order|maximal order]].

## References

1. Andrew V. Sutherland, *18.785 Number Theory*, Fall 2018, [Problem Set 7](https://math.mit.edu/classes/18.785/2018fa/ProblemSet7.pdf), Problem 4(b)–(c), for fundamental discriminants.
2. David A. Cox, *Primes of the Form x² + ny²*, [§7.B, Theorem 7.7](https://www.math.utoronto.ca/~ila/Cox-Primes_of_the_form_x2%2Bny2.pdf), general imaginary quadratic orders.
