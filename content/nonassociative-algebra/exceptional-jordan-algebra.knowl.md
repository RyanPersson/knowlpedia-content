+++
id = "nonassociative-algebra/exceptional-jordan-algebra"
title = "Exceptional Jordan algebra"
kind = "definition"
summary = "The 27-dimensional Euclidean Jordan algebra of three-by-three Hermitian octonionic matrices, also called the Albert algebra."
aliases = ["exceptional Jordan algebra", "Albert algebra", "h_3(O)", "octonionic qutrit"]
domains = ["nonassociative-algebra", "mathematical-physics"]
section_mode = "progressive"
+++

The **exceptional Jordan algebra**, or real **Albert algebra**, is
\[
\mathfrak h_3(\mathbb O)
=\{X\in M_3(\mathbb O):X^*=X\},
\qquad
X\circ Y=\frac12(XY+YX).
\]
It is a 27-dimensional simple
[[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]]
with unit \(I_3\), and it is not special.

## Coordinates and dimension

An element has the form
\[
\begin{pmatrix}
\alpha&z&\bar y\\
\bar z&\beta&x\\
y&\bar x&\gamma
\end{pmatrix},
\qquad
\alpha,\beta,\gamma\in\mathbb R,\quad x,y,z\in\mathbb O.
\]
The three real diagonal coordinates and three octonionic off-diagonal entries
give dimension \(3+3\cdot8=27\). Although octonionic matrix multiplication is
not associative, a product of two matrices is unambiguous, and alternativity
is sufficient for the degree-three symmetrized product to obey the Jordan
identity.

## Rank and cubic norm

The Albert algebra has rank \(3\). Its Jordan trace is
\(\alpha+\beta+\gamma\), and it has a cubic Jordan determinant. Its
characteristic polynomial is
\[
t^3-\operatorname{tr}_J(X)t^2+s(X)t-\det_J(X).
\]

## Exceptional character and symmetry

It is **exceptional** because it cannot be embedded in \(A^+\) for any
associative algebra \(A\). Over \(\mathbb R\) it is the unique exceptional
simple Euclidean Jordan algebra. Other fields and other real forms admit
Albert algebras with different behavior, so this knowl concerns the compact
Euclidean real form.

Its [[nonassociative-algebra/automorphism-group-of-a-jordan-algebra|automorphism
group]] is the compact real form of \(F_4\), of dimension \(52\). The larger
determinant-preserving structure group is the real form \(E_{6(-26)}\).

## References

1. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-12622-6).
2. Pascual Jordan, John von Neumann, and Eugene Wigner, “On an Algebraic Generalization of the Quantum Mechanical Formalism,” *Annals of Mathematics* 35 (1934), 29–64. [JSTOR record](https://www.jstor.org/stable/1968117).
3. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv:2606.15235](https://arxiv.org/abs/2606.15235).
