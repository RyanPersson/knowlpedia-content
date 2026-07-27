+++
id = "operator-algebras/character-cstar-algebra"
title = "Character of a C*-algebra"
kind = "definition"
summary = "A nonzero multiplicative star-homomorphism from a C-star algebra to the complex numbers."
aliases = ["C*-character", "multiplicative state"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**character of \(A\)** is a nonzero
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]]
\(\chi:A\to\mathbb C\). Equivalently, it is a nonzero multiplicative complex
linear functional on \(A\); the \(C^*\)-structure then forces continuity and
\(\chi(a^*)=\overline{\chi(a)}\). Every character is positive and has norm
one, so it is a [[operator-algebras/state-cstar-algebra|state]]. When \(A\) is
unital, a character automatically satisfies \(\chi(1)=1\). Its kernel is a
maximal closed two-sided ideal, and \(A/\ker\chi\cong\mathbb C\).
The zero homomorphism is excluded.

## Existence and examples

For \(A=C_0(X)\), evaluation at \(x\in X\),
\(\chi_x(f)=f(x)\), is a character, and every character has this form. The
matrix algebra \(M_n(\mathbb C)\) has no characters for \(n>1\), because it is
simple and cannot have a one-dimensional quotient. More generally, characters
exist precisely when \(A\) has a quotient isomorphic to \(\mathbb C\).

## Multiplicativity and purity

Every character is a
[[operator-algebras/pure-state-cstar-algebra|pure state]]. Conversely, a pure
state need not be a
character: vector states on \(M_n(\mathbb C)\) are pure, but no nonzero state
there is multiplicative when \(n>1\). On a
[[operator-algebras/commutative-cstar-algebra|commutative \(C^*\)-algebra]],
however, the pure states are exactly the characters. These facts underlie the
construction of the character space
[Murphy, chapter on commutative \(C^*\)-algebras](https://doi.org/10.1016/C2009-0-22289-6).

## Terminology

**Warning.** This notion is not a group-representation character or a Lie
algebra weight. It is a scalar-valued algebra homomorphism. Some Banach-algebra
texts define “character” first as a nonzero multiplicative functional; for a
\(C^*\)-algebra that convention yields the same objects.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: the chapter on characters, pure states, and commutative \(C^*\)-algebras.
2. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: the introductory discussion of states and multiplicative functionals.
