+++
id = "langlands/local-langlands-correspondence-for-gln"
title = "Local Langlands correspondence for \\(\\mathrm{GL}_n\\)"
kind = "theorem"
summary = "The canonical bijection between irreducible smooth representations of GL_n and n-dimensional Frobenius-semisimple Weil–Deligne representations."
aliases = ["LLC for GL_n", "local Langlands theorem for the general linear group"]
domains = ["langlands", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(F\) be a nonarchimedean local field. There is a unique canonical
bijection

\[
\operatorname{rec}_{F,n}:
\operatorname{Irr}\bigl(\operatorname{GL}_n(F)\bigr)
\xrightarrow{\ \sim\ }
\operatorname{WD}_n(F)
\]

from irreducible smooth complex representations of
\(\operatorname{GL}_n(F)\) to isomorphism classes of \(n\)-dimensional
Frobenius-semisimple
[[langlands/weil-deligne-representation|Weil–Deligne representations]],
normalized so that \(n=1\) agrees with local class field theory and so that
standard local \(L\)- and \(\varepsilon\)-factors agree.

## Packet consequence

Every \(L\)-packet for \(\operatorname{GL}_n\) is a singleton. Thus the basic
local correspondence is an actual bijection rather than a finite-to-one map.

## Compatibility properties

The correspondence is compatible with twisting by characters and taking
contragredients. The determinant of the parameter corresponds, through local
class field theory, to the central character of the representation. Under the
Langlands classification, direct sums of Weil–Deligne parameters correspond
to the appropriate irreducible quotients of normalized parabolic inductions.

## Special classes

[[harmonic-analysis/supercuspidal-representation|Supercuspidal representations]] correspond to irreducible \(n\)-dimensional
representations of \(W_F\), necessarily with zero monodromy. Essentially
square-integrable representations correspond to indecomposable
Weil–Deligne representations. Unramified representations correspond to
parameters trivial on inertia with zero monodromy.

## Proof history

The theorem was proved through the work of Laumon–Rapoport–Stuhler and
Harris–Taylor, with Henniart establishing the numerical correspondence and a
characterization by local factors. Different constructions are known to agree
under the standard normalization.

## References

1. Michael Harris and Richard Taylor, *The Geometry and Cohomology of Some
   Simple Shimura Varieties*, Princeton University Press, 2001.
   [Publisher](https://press.princeton.edu/books/hardcover/9780691090924/the-geometry-and-cohomology-of-some-simple-shimura-varieties).
2. Guy Henniart, “Une preuve simple des conjectures de Langlands pour
   \(\mathrm{GL}(n)\) sur un corps \(p\)-adique,” *Inventiones Mathematicae*
   139 (2000), 439–455. [DOI](https://doi.org/10.1007/s002220050012).
3. Michael Harris, “On the local Langlands correspondence,” 2003.
   [arXiv](https://arxiv.org/abs/math/0304324).
