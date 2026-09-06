+++
id = "operator-algebras/cyclic-separating-duality"
title = "Cyclic-separating duality"
kind = "theorem"
summary = "For a von Neumann algebra and its commutant, cyclicity for either algebra is equivalent to separation for the other."
aliases = ["commutant cyclic-separating theorem"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-algebra", "linear-algebra/hilbert-space", "operator-algebras/commutant"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]] on a
[[linear-algebra/hilbert-space|Hilbert space]], and let
\(M'\) be its [[operator-algebras/commutant|commutant]]. The
**cyclic-separating duality** says that, for every \(\xi\in H\),
\[
\xi\text{ is cyclic for }M
\quad\Longleftrightarrow\quad
\xi\text{ is separating for }M',
\]
and
\[
\xi\text{ is separating for }M
\quad\Longleftrightarrow\quad
\xi\text{ is cyclic for }M'.
\]
Here cyclic means \(\overline{M\xi}=H\), while separating means
\(x\xi=0\Rightarrow x=0\). The von Neumann hypothesis supplies
\(M''=M\), which is essential to the converse implications.

## Proof mechanism

If \(\xi\) is cyclic for \(M\) and \(y\in M'\) satisfies \(y\xi=0\), then
\(yx\xi=xy\xi=0\) for every \(x\in M\). Density of \(M\xi\) forces \(y=0\),
so \(\xi\) is separating for \(M'\).

Conversely, let \(p\) be the
[[linear-algebra/orthogonal-projection|orthogonal projection]] onto
\(\overline{M\xi}\). This subspace and its [[linear-algebra/orthogonal-complement|orthogonal complement]] are
invariant under every unitary in \(M\), hence \(p\in M'\). If \(\xi\) is
separating for \(M'\), then \((1-p)\xi=0\) implies \(p=1\), so
\(\overline{M\xi}=H\). Interchanging \(M\) and \(M'\), and using
\(M''=M\), proves the second equivalence.

## Examples and scope

For the multiplication algebra \(M=L^\infty(X,\mu)\) on \(L^2(X,\mu)\),
where \(\mu\) is a finite measure, the constant function \(1\) is both cyclic
and separating; here \(M'=M\). By contrast, if \(\dim H>1\), every nonzero
vector is cyclic for \(B(H)\), but no vector is separating for \(B(H)\).
The commutant \(B(H)'=\mathbb C1\) reverses those two properties exactly as
the duality predicts.

For an arbitrary concrete \(C^*\)-algebra \(A\subseteq B(H)\), cyclicity for
\(A\) still implies separation for \(A'\). The converse naturally concerns
the bicommutant \(A''\), not necessarily \(A\), because the projection
argument only places the relevant projection in \(A'\).

## References

1. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I: Elementary Theory*, American Mathematical Society, 1997 reprint. [AMS DOI record](https://doi.org/10.1090/gsm/015). Relevant: Proposition 5.5.11 on cyclic and separating vectors for commutants.
