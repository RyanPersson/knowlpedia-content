+++
id = "lie-groups/pbw-theorem"
title = "Poincaré–Birkhoff–Witt theorem"
kind = "theorem"
summary = "Ordered monomials in an ordered basis of a Lie algebra form a basis of its universal enveloping algebra."
aliases = ["PBW theorem", "symmetrization theorem"]
domains = ["lie-groups", "algebra"]
prerequisites = ["lie-groups/lie-algebra", "lie-groups/universal-enveloping-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a [[lie-groups/lie-algebra|Lie algebra]] over a field \(k\), and let \((x_i)_{i\in I}\) be a totally ordered basis. The **Poincaré–Birkhoff–Witt theorem** states that the ordered monomials
\[
1,\qquad x_{i_1}x_{i_2}\cdots x_{i_n}
\quad(n\geq1,\ i_1\leq i_2\leq\cdots\leq i_n)
\]
form a \(k\)-basis of the [[lie-groups/universal-enveloping-algebra|universal enveloping algebra]] \(U(\mathfrak g)\). In particular, the canonical Lie-algebra map \(\mathfrak g\to U(\mathfrak g)\) is injective, so \(\mathfrak g\) may be identified with its image in the associative algebra \(U(\mathfrak g)\).

## Filtration form

Filter \(U(\mathfrak g)\) by word length. Commuting two adjacent generators changes their product by \([x,y]\), which has lower filtration degree. Consequently the associated graded algebra is commutative, and PBW gives a canonical graded-algebra isomorphism
\[
\operatorname{Sym}(\mathfrak g)\xrightarrow{\;\sim\;}\operatorname{gr}U(\mathfrak g).
\]
This formulation is independent of the chosen ordered basis.

## Symmetrization in characteristic zero

When \(k\) has characteristic zero, the symmetrization map
\[
x_1\cdots x_n\longmapsto
\frac{1}{n!}\sum_{\sigma\in S_n}
x_{\sigma(1)}\cdots x_{\sigma(n)}
\]
is a canonical vector-space isomorphism \(\operatorname{Sym}(\mathfrak g)\to U(\mathfrak g)\). It is generally not an [[algebra-modules/algebra-homomorphism|algebra homomorphism]]: PBW identifies the associated graded multiplication, not the original noncommutative multiplication in \(U(\mathfrak g)\).

## Structural consequences

The theorem transfers polynomial-degree arguments from the symmetric algebra to \(U(\mathfrak g)\). It underlies the construction of central and Casimir elements, controls filtrations on \(U(\mathfrak g)\)-modules, and ensures that a Lie-algebra representation extends uniquely to an action of \(U(\mathfrak g)\). Over a general commutative base ring, a PBW statement requires additional hypotheses such as projectivity of the underlying module.

## References

1. J. Dixmier, *Enveloping Algebras*, Graduate Studies in Mathematics 11, American Mathematical Society, 1996. [DOI record](https://doi.org/10.1090/gsm/011). Relevant: §2.1 on PBW and the canonical filtration.
2. A. W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002. [DOI record](https://doi.org/10.1007/978-1-4757-2453-0). Relevant: Chapter V, §2.
