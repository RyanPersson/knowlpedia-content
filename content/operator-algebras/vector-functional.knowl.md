+++
id = "operator-algebras/vector-functional"
title = "Vector functional on a von Neumann algebra"
kind = "definition"
summary = "A vector functional evaluates a concrete von Neumann algebra between two fixed Hilbert-space vectors."
aliases = ["matrix coefficient functional"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a concrete
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] on a
[[linear-algebra/hilbert-space|Hilbert space]] \(H\). For
\(\xi,\eta\in H\), the **vector functional**
\(\omega_{\xi,\eta}:M\to\mathbb C\) is
\[
\omega_{\xi,\eta}(x)=\langle x\xi,\eta\rangle .
\]
Here the [[linear-algebra/inner-product|inner product]] is taken to be linear
in its first variable. The functional is bounded and normal, and
\(\lVert\omega_{\xi,\eta}\rVert\leq\lVert\xi\rVert\lVert\eta\rVert\).
When \(\eta=\xi\), it is positive; if additionally \(\lVert\xi\rVert=1\) and
the representation is unital, it is a
[[operator-algebras/vector-state|vector state]].

## Relation to the predual

Every vector functional belongs to the
[[operator-algebras/predual|predual]] \(M_*\). Conversely, every
\(\omega\in M_*\) can be written as an absolutely convergent series
\[
\omega=\sum_{n=1}^{\infty}\omega_{\xi_n,\eta_n},
\qquad
\sum_n\lVert\xi_n\rVert^2<\infty,\quad
\sum_n\lVert\eta_n\rVert^2<\infty.
\]
Thus vector functionals linearly generate the predual, although a given
[[operator-algebras/normal-functional|normal functional]] need not be a
single vector functional in the chosen representation
[Kadison–Ringrose, §5.2](https://doi.org/10.1090/gsm/015).

## Concrete examples

For \(M=B(H)\),
\[
\omega_{\xi,\eta}(x)=\operatorname{Tr}(\theta_{\xi,\eta}x),
\]
where \(\theta_{\xi,\eta}\) is the rank-one
[[functional-analysis/schatten-class-operator|trace-class operator]] determined by the
same inner-product convention. Hence vector functionals are exactly the
predual functionals represented by rank-one trace-class operators. A
[[operator-algebras/normal-state|normal state]] with a
[[quantum-foundations/density-operator|density operator]] of rank greater than
one is not a vector state in the identity representation of \(B(H)\), but it
is a sum of positive vector functionals.

## Dependence on representation and conventions

Vector-functional status depends on the concrete representation
\(M\subseteq B(H)\), whereas normality is intrinsic to \(M\). In a standard
form, every positive normal functional is represented by a unique vector in
the [[operator-algebras/natural-positive-cone|natural positive cone]]. With
the alternative convention that the Hilbert-space inner product is linear in
the second variable, authors reverse the vector order in the notation so
that \(x\mapsto\omega_{\xi,\eta}(x)\) remains linear in \(x\).

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/015). Relevant: §5.2 on vector functionals, ultraweak continuity, and the predual of a concrete von Neumann algebra.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter III, §2 on normal functionals and concrete predual representations.
