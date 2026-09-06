+++
id = "operator-algebras/type-i-composition-series"
title = "Type I composition series"
kind = "definition"
summary = "A transfinite ideal filtration whose successive quotients are continuous-trace C*-algebras."
aliases = ["composition series with continuous-trace quotients", "CCR composition series"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/closed-two-sided-ideal", "operator-algebras/continuous-trace-cstar-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **type I composition series** for a
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\) is an
ordinal-indexed increasing family \((I_\alpha)_{\alpha\leq\delta}\) of
[[operator-algebras/closed-two-sided-ideal|closed two-sided ideals]] such that
\(I_0=0\), \(I_\delta=A\), and
\[
I_\lambda=\overline{\bigcup_{\alpha<\lambda}I_\alpha}
\]
at every limit ordinal \(\lambda\leq\delta\), while every successor inclusion
is strict and \(I_{\alpha+1}/I_\alpha\) is a
[[operator-algebras/continuous-trace-cstar-algebra|continuous-trace \(C^*\)-algebra]].
The term records a structural filtration, not a finite
Jordan–Hölder series; both its ordinal length and its successive pieces can
depend on choices.

## Existence theorem

Every [[operator-algebras/type-i-cstar-algebra|type I \(C^*\)-algebra]]
admits such an ascending series.
The construction repeatedly passes to a quotient and selects a nonzero
continuous-trace ideal, then takes closures at limit stages. The process ends
because a strictly increasing chain of closed ideals cannot contain more
members than the [[shared-foundations/power-set|power set]] of the underlying algebra.

## How the filtration is used

Properties stable under ideals, quotients, extensions, and transfinite
inductive unions can often be proved for type I algebras by checking them on
the continuous-trace layers. Each layer has a Hausdorff spectrum and is locally
modeled by
[[operator-algebras/compact-operator-cstar-algebra|compact-operator algebras]],
so the series separates local geometric analysis from the possibly
non-Hausdorff gluing of the full
[[operator-algebras/primitive-ideal-space|primitive ideal space]].

## Conventions and scope

Some sources use “GCR composition series” for a filtration whose layers are
merely liminal, and then refine those layers further to continuous trace. The
stronger continuous-trace convention is used here. The word “composition” does
not assert that the layers are simple, unique, or of finite length.

## References

1. Jacques Dixmier, *C*-Algebras, North-Holland Mathematical Library 15, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15/suppl/C). Relevant: Chapter 4 and §10.5 on composition series and continuous-trace subquotients of type I algebras.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapter 6 on type I composition series.
