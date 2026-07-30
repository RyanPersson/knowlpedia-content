+++
id = "formal-groups/complete-filtered-lie-algebra-bch-group"
title = "BCH group of a complete filtered Lie algebra"
kind = "theorem"
summary = "The convergent BCH series turns a complete pronilpotent Lie algebra into a filtered group."
aliases = ["pronilpotent BCH group", "exponential group of a complete Lie algebra", "exp(g) for a pronilpotent Lie algebra"]
domains = ["formal-groups", "lie-groups"]
section_mode = "progressive"
+++

Let \(k\) be a field of characteristic zero and let
\((\mathfrak g,F^\bullet)\) be a
[[lie-groups/complete-filtered-lie-algebra|complete filtered Lie algebra]] with
\(\mathfrak g=F^1\mathfrak g\) and
\([F^p\mathfrak g,F^q\mathfrak g]\subseteq F^{p+q}\mathfrak g\).
The [[lie-groups/baker-campbell-hausdorff-formula|Baker–Campbell–Hausdorff
series]] converges in the filtration and defines
\[
x*y
=
\operatorname{BCH}(x,y)
=
x+y+\frac12[x,y]
+\frac1{12}[x,[x,y]]
+\frac1{12}[y,[y,x]]+\cdots.
\]
With this product, identity \(0\), and inverse \(x^{-1}=-x\), the set
underlying \(\mathfrak g\) is a group, denoted
\(\operatorname{BCH}(\mathfrak g)\) or \(\exp(\mathfrak g)\). Every
continuous filtration-preserving Lie-algebra homomorphism
\(f:\mathfrak g\to\mathfrak h\) is a homomorphism of the corresponding BCH
groups.

## Convergence and associativity

Every Lie monomial of bracket length \(n\) in \(x,y\in F^1\mathfrak g\) lies
in \(F^n\mathfrak g\). Modulo \(F^r\mathfrak g\), only finitely many terms of
the BCH series survive. These finite values are compatible as \(r\) varies,
and completeness supplies their unique inverse-limit value in
\(\mathfrak g\).

The formal identity
\[
\operatorname{BCH}(\operatorname{BCH}(x,y),z)
=
\operatorname{BCH}(x,\operatorname{BCH}(y,z))
\]
then proves associativity. This is a formal-algebraic argument; no norm,
analytic convergence, or ambient matrix exponential is required.

## Filtration on the group

Set \(F^n\operatorname{BCH}(\mathfrak g)=F^n\mathfrak g\) as sets. The BCH
formula gives
\[
[F^p\operatorname{BCH}(\mathfrak g),
F^q\operatorname{BCH}(\mathfrak g)]
\subseteq
F^{p+q}\operatorname{BCH}(\mathfrak g).
\]
Moreover,
\[
\operatorname{BCH}(\mathfrak g)/F^n
\cong
\operatorname{BCH}(\mathfrak g/F^n\mathfrak g),
\]
and the group on the right is nilpotent. Thus the construction is compatible
with all nilpotent truncations and exhibits the BCH group as their inverse
limit.

## Functorial form

The assignment
\[
\mathfrak g\longmapsto\operatorname{BCH}(\mathfrak g)
\]
is a functor from complete bracket-filtered Lie algebras over \(k\) to
complete filtered groups. In formulations using prounipotent affine group
schemes, exponential and logarithm give an equivalence between pronilpotent
Lie algebras and prounipotent groups over a characteristic-zero field.
For abstract groups, an inverse equivalence requires the corresponding
Malcev or unique-divisibility hypotheses; it is not an equivalence with all
complete filtered groups.

## Relation to finite-dimensional formal groups

An arbitrary finite-dimensional Lie algebra need not be nilpotent and does
not itself carry a filtration on which the full BCH series converges. Its
associated formal group is instead read order by order in formal coordinates:
equivalently, one may insert a formal parameter and apply this theorem to the
complete Lie algebra
\[
t\mathfrak g[[t]]
\supseteq t^2\mathfrak g[[t]]
\supseteq\cdots.
\]
The resulting formal BCH law is the local construction used in the
[[formal-groups/lie-algebra-formal-group-equivalence|equivalence between
finite-dimensional Lie algebras and formal groups]].

When \(\mathfrak g\) is nilpotent, its lower central series terminates and the
BCH expression truncates to a finite Lie polynomial. In that special case
the construction agrees with the usual exponential group of a nilpotent Lie
algebra.

## Characteristic warning

The rational coefficients in the BCH series require characteristic zero (or
a base in which all relevant denominators are invertible). In positive
characteristic, truncations of sufficiently small nilpotency class can still
work under additional denominator bounds, but the unrestricted statement
above is false.

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 1–3*, Springer, 1989. [Publisher record](https://doi.org/10.1007/978-3-540-64242-8). Relevant: Chapter II, §§6–7 on formal Lie series, complete algebras, and the Campbell–Hausdorff formula.
2. Jean-Pierre Serre, *Lie Algebras and Lie Groups*, Lecture Notes in Mathematics 1500, Springer, 1992. [Publisher record](https://doi.org/10.1007/978-3-540-70634-2). Relevant: Part II, Chapters IV–V.
3. Daniel Quillen, “Rational homotopy theory,” *Annals of Mathematics* 90 (1969), 205–295. [Journal record](https://doi.org/10.2307/1970725). Relevant: complete Lie algebras and the exponential correspondence in characteristic zero.
