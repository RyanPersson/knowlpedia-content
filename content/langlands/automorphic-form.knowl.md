+++
id = "langlands/automorphic-form"
title = "Automorphic form"
kind = "knowl"
summary = "A smooth, finite, moderate-growth function on an adelic automorphic quotient."
aliases = ["automorphic forms", "adelic automorphic form"]
domains = ["langlands", "number-theory", "representation-theory"]
prerequisites = ["langlands-letter/knowls/global-local-fields-completions", "algebraic-geometry-foundations/reductive-algebraic-group", "langlands-letter/knowls/adeles-restricted-product", "lie-groups/k-finite-vector", "lie-groups/universal-enveloping-algebra", "algebra-representation-theory/central-character"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(F\) be a
[[langlands-letter/knowls/global-local-fields-completions|global field]] and
\(G\) a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive
\(F\)-group]]. An
**automorphic form** on \(G\) is a complex-valued function on

\[
G(F)\backslash G(\mathbb A_F)
\]

where \(\mathbb A_F\) is the
[[langlands-letter/knowls/adeles-restricted-product|adele ring]], and that is
smooth, of moderate growth, right
[[lie-groups/k-finite-vector|finite under a maximal compact group]]
at the archimedean places, right fixed by some compact open subgroup at the
finite places, and finite under the center of the archimedean universal
[[lie-groups/universal-enveloping-algebra|enveloping algebra]]. A
[[algebra-representation-theory/central-character|central character]] may be
prescribed.

## Why the finiteness conditions appear

At a finite place, smoothness means local constancy, so a single automorphic
form is fixed by a sufficiently small compact open subgroup. At an
archimedean place, compact finiteness and infinitesimal-character finiteness
place the function in the algebraic representation-theoretic category of
\((\mathfrak g,K)\)-modules. Moderate growth controls its behavior on the
noncompact quotient.

Some authors build uniform moderate growth into the definition, while others
obtain it from the remaining conditions in their chosen setting. The precise
space should therefore be named when analytic estimates matter.

## Central and split-center conventions

If \(\omega\) is a character of \(Z_G(F)\backslash Z_G(\mathbb A_F)\), one
usually imposes

\[
f(zg)=\omega(z)f(g).
\]

Square-integrability, with the quotient measure compatibly normalized (often
from [[langlands/tamagawa-measure|Tamagawa measure]]), is then measured either
modulo the center or on the
kernel \(G(\mathbb A_F)^1\) of all adelic absolute-value characters. These
equivalent-looking presentations encode a real convention and should not be
silently interchanged.

## Constant terms

For a [[algebraic-geometry-foundations/parabolic-subgroup|parabolic subgroup]]
\(P=MN\), with [[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]]
\(M\) and [[algebraic-geometry-foundations/unipotent-radical|unipotent
radical]] \(N\), the
[[langlands/automorphic-constant-term|constant term]] of \(f\) along \(P\) is

\[
f_P(g)=
\int_{N(F)\backslash N(\mathbb A_F)} f(ng)\,dn.
\]

Its vanishing for every proper parabolic defines a
[[langlands/cuspidal-automorphic-representation|cuspidal]] automorphic form.
Nonzero constant terms lead to
[[langlands-letter/knowls/eisenstein-series|Eisenstein series]] and the
[[langlands/continuous-automorphic-spectrum|continuous]] or
[[langlands/residual-automorphic-spectrum|residual]] spectrum.

## From forms to representations

[[lie-groups/right-translation|Right translation]] by \(G(\mathbb A_F)\) acts on automorphic forms. Irreducible
subquotients of this action are
[[langlands/automorphic-representation|automorphic representations]]. Thus a
form is a vector, not an [[algebra-representation-theory/irreducible-representation|irreducible representation]]; Hecke eigenforms often
generate automorphic representations.

## References

1. A. Borel and H. Jacquet, “Automorphic forms and automorphic
   representations,” in *Automorphic Forms, Representations and
   \(L\)-Functions*, Proc. Sympos. Pure Math. 33, part 1, 1979, pp. 189–207.
2. Jayce Getz and Heekyoung Hahn, *An Introduction to Automorphic
   Representations*, Springer, 2024.
   [DOI](https://doi.org/10.1007/978-3-031-41153-3).
