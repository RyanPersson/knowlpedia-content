+++
id = "lie-groups/even-and-odd-exterior-algebra"
title = "Even and odd exterior algebra"
kind = "definition"
summary = "The parity decomposition of an exterior algebra into its even-degree and odd-degree parts."
aliases = ["parity decomposition of the exterior algebra", "even exterior algebra", "odd exterior algebra"]
domains = ["lie-groups", "algebra-modules", "supergeometry"]
section_mode = "progressive"
+++

For a module \(V\), the [[algebra-modules/exterior-algebra|exterior algebra]] has a canonical parity decomposition
\[
\Lambda V=\Lambda^{\mathrm{even}}V\oplus\Lambda^{\mathrm{odd}}V,
\qquad
\Lambda^{\mathrm{even}}V=\bigoplus_{j\geq0}\Lambda^{2j}V,
\quad
\Lambda^{\mathrm{odd}}V=\bigoplus_{j\geq0}\Lambda^{2j+1}V.
\]
This makes \(\Lambda V\) a \(\mathbb Z/2\mathbb Z\)-graded algebra: wedge multiplication adds parities modulo two.

## Multiplication by parity

The multiplication rules are
\[
\Lambda^{\mathrm{even}}V\wedge\Lambda^{\mathrm{even}}V
\subseteq\Lambda^{\mathrm{even}}V,
\qquad
\Lambda^{\mathrm{even}}V\wedge\Lambda^{\mathrm{odd}}V
\subseteq\Lambda^{\mathrm{odd}}V,
\]
and
\[
\Lambda^{\mathrm{odd}}V\wedge\Lambda^{\mathrm{odd}}V
\subseteq\Lambda^{\mathrm{even}}V.
\]
Consequently, the even part is a subalgebra containing the unit, whereas the odd part is generally not a subalgebra.

For homogeneous elements \(a,b\) of parities \(|a|,|b|\in\mathbb Z/2\mathbb Z\), graded commutativity reads
\[
a\wedge b=(-1)^{|a||b|}b\wedge a.
\]
The full integer grading retains more information than parity, but parity is the grading used when \(\Lambda V\) is viewed as a superalgebra.

## Representations

An action on \(V\) by linear maps extends to the [[lie-groups/exterior-power-representation|exterior algebra]]. It preserves degree and hence preserves the even and odd summands. Thus
\[
\Lambda^{\mathrm{even}}V
\quad\text{and}\quad
\Lambda^{\mathrm{odd}}V
\]
are subrepresentations whenever \(V\) is a representation.

This parity decomposition resembles the even/odd grading of a [[differential-geometry/clifford-algebra|Clifford algebra]], but the products differ: exterior generators square to zero, while Clifford generators square to the value prescribed by a [[linear-algebra/quadratic-form|quadratic form]].

## Characteristic two

Over a base ring of characteristic \(2\), the sign \((-1)^{|a||b|}\) becomes invisible. The exterior algebra is nevertheless defined using the alternating relations \(v\wedge v=0\); parity still exists, but it cannot be recovered from signs alone.

## References

1. Nicolas Bourbaki, *Algebra I: Chapters 1–3*, Springer, 1989, Chapter III. [Publisher record](https://doi.org/10.1007/978-3-642-61698-3).
2. Pierre Deligne and John W. Morgan, “Notes on supersymmetry (following Joseph Bernstein),” in *Quantum Fields and Strings: A Course for Mathematicians*, American Mathematical Society, 1999. [Publisher record](https://bookstore.ams.org/qrld-1-1/).
