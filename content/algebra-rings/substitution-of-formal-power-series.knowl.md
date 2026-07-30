+++
id = "algebra-rings/substitution-of-formal-power-series"
title = "Substitution of formal power series"
kind = "construction"
summary = "Composition f(g_1,...,g_n) defined adically when each substituted series has zero constant term."
aliases = ["composition of formal power series", "formal power series substitution", "pointed formal substitution"]
domains = ["algebra-rings", "formal-groups"]
section_mode = "progressive"
+++

Let \(R\) be a commutative ring,
\(f\in R[[X_1,\ldots,X_n]]\), and
\[
g_i\in(Y_1,\ldots,Y_m)R[[Y_1,\ldots,Y_m]]
\qquad(1\leq i\leq n).
\]
The **substitution of formal power series** is
\[
f(g_1,\ldots,g_n)
:=
\sum_{\alpha\in\mathbb N^n}a_\alpha
g_1^{\alpha_1}\cdots g_n^{\alpha_n},
\qquad
f=\sum_\alpha a_\alpha X^\alpha.
\]
It is a well-defined element of \(R[[Y_1,\ldots,Y_m]]\): modulo
\((Y_1,\ldots,Y_m)^N\), only the terms with \(|\alpha|<N\) can contribute.

## Topological meaning

The vanishing constant terms make every \(g_i\) topologically nilpotent for
the augmentation-adic topology. Substitution is the unique continuous
\(R\)-algebra homomorphism
\[
R[[X_1,\ldots,X_n]]
\longrightarrow
R[[Y_1,\ldots,Y_m]],
\qquad X_i\longmapsto g_i.
\]
It can equivalently be constructed on every finite quotient and then passed
to the [[algebra-commutative/i-adic-completion|inverse limit]].

## Composition and pointed maps

Formal substitution is associative:
\[
f(g_1(h),\ldots,g_n(h))
=
\bigl(f(g_1,\ldots,g_n)\bigr)(h).
\]
The coordinate tuple \(g\) has zero constant term precisely when it sends the
formal origin to the formal origin. Consequently pointed maps between
[[formal-groups/formal-affine-space|formal affine spaces]] are represented by
such tuples, with composition given by substitution.

## Scope warning

Over a ring containing nilpotents, a series with nonzero nilpotent constant
term may also admit some substitutions. The zero-constant-term convention is
the clean, base-preserving pointed construction used for formal group laws; it
should not be misread as a classification of every possible continuous map
between arbitrary adic rings.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Appendix A, substitution and homomorphisms of power-series rings.
2. Nicolas Bourbaki, *Algebra II: Chapters 4–7*, Springer, 1990. Relevant: Chapter 4, formal series.
