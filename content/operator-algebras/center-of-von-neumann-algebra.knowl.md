+++
id = "operator-algebras/center-of-von-neumann-algebra"
title = "Center of a von Neumann algebra"
kind = "definition"
summary = "The commutative von Neumann subalgebra consisting of elements that commute with every element of the original algebra."
aliases = ["central algebra Z(M)"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]]. Its **center**
is
\[
Z(M)=\{z\in M:zx=xz\ \text{for every }x\in M\}
     =M\cap M'.
\]
Here \(M'\) is the [[operator-algebras/commutant|commutant]] of \(M\). The
center is a [[operator-algebras/commutative-von-neumann-algebra|commutative von Neumann algebra]] containing the scalar multiples of
\(1_M\). The algebra \(M\) is a **factor** precisely when
\(Z(M)=\mathbb C1_M\). Thus factoriality means trivial center, not
commutativity: a nontrivial commutative von Neumann algebra is a factor only
in the one-dimensional scalar case.

## Central projections and decomposition

A projection in \(Z(M)\) is a central projection. Each central projection
\(z\) splits the algebra as
\[
M\cong zM\oplus(1-z)M.
\]
Conversely, direct-sum decompositions of \(M\) arise from central projections.
More generally, the center supports the central, or factorial, decomposition
of a von Neumann algebra into factors; this is formulated as a direct integral
under standard separability hypotheses
[Kadison–Ringrose, vol. II, §6.5](https://doi.org/10.1090/gsm/016).

## Examples

For \(M=B(H)\) with \(H\ne\{0\}\), the center is
\(\mathbb C I_H\), so \(B(H)\) is a type I factor. If
\(M=L^\infty(X,\mu)\) acts by multiplication on \(L^2(X,\mu)\), then \(M\) is
commutative and \(Z(M)=M\). For a direct sum \(M_1\oplus M_2\), its center is
\(Z(M_1)\oplus Z(M_2)\); even when both summands are factors, their direct sum
is not a factor.

## Conventions and scope

The formula \(M\cap M'\) uses the commutant inside the specified ambient
\(B(H)\), but the resulting center is intrinsic to the abstract von Neumann
algebra. “Central algebra” sometimes refers to an algebra equipped with a
chosen map from another commutative algebra; that broader usage should not be
confused with \(Z(M)\). A factor may be of type I, II, or III, so “factor” is
not a synonym for “type I factor.”

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume II: Advanced Theory*, American Mathematical Society, 1997. [AMS record](https://doi.org/10.1090/gsm/016). Relevant: §6.5 on centers and factorial decomposition.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapters IV–V on factors and central decomposition.
