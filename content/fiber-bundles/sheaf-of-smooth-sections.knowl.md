+++
id = "fiber-bundles/sheaf-of-smooth-sections"
title = "Sheaf of smooth sections"
kind = "definition"
summary = "The locally free sheaf assigning smooth local sections of a vector bundle to each open subset of its base."
aliases = ["section sheaf", "sheaf of sections of a vector bundle", "Gamma sheaf of a bundle"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(\mathbb F\in\{\mathbb R,\mathbb C\}\), and let
\(\pi:E\to M\) be a smooth finite-rank
[[fiber-bundles/vector-bundle|\(\mathbb F\)-vector bundle]]. Its **sheaf of smooth
sections**, denoted \(\mathcal E\) or \(\Gamma^\infty(-,E)\), assigns
\[
\mathcal E(U)=\Gamma^\infty(U,E|_U)
\]
to each open subset \(U\subseteq M\). Restriction of sections supplies the
restriction maps. Sections that agree on overlaps glue uniquely, and
smoothness is local, so this is a sheaf.

Pointwise scalar multiplication makes \(\mathcal E\) a
[[algebraic-geometry-foundations/sheaf-of-modules|sheaf of modules]] over
the sheaf \(C^\infty_M(\mathbb F)\), defined by
\[
C^\infty_M(\mathbb F)(U)=C^\infty(U,\mathbb F).
\]
For \(\mathbb F=\mathbb R\), this is
[[differential-geometry/sheaf-of-smooth-functions|\(C^\infty_M\)]]; for
\(\mathbb F=\mathbb C\), it is its complexification.

## Local freeness

If \(E|_U\cong U\times\mathbb F^r\), a local frame identifies
\[
\mathcal E|_U\cong
\bigl(C^\infty_M(\mathbb F)|_U\bigr)^{\oplus r}.
\]
Hence the section sheaf is a finite-rank
[[algebraic-geometry-foundations/locally-free-sheaf|locally free sheaf]].
Its stalk \(\mathcal E_x\) consists of germs of local sections near \(x\);
it is a free module of rank \(r\) over the local ring
\(C^\infty_{M,x}(\mathbb F)\), the stalk of
\(C^\infty_M(\mathbb F)\) at \(x\).

## Sheaf versus global module

The [[fiber-bundles/module-of-smooth-sections|module of global smooth
sections]] is the single module
\[
\mathcal E(M)=\Gamma^\infty(M,E)
\]
over \(C^\infty(M,\mathbb F)\). The sheaf \(\mathcal E\) includes sections over every
open set and their gluing data. Local freeness of \(\mathcal E\) does not
assert that \(\Gamma^\infty(M,E)\) is a free module.

A bundle morphism \(E\to F\) covering \(\operatorname{id}_M\) induces a
morphism \(\mathcal E\to\mathcal F\) of \(C^\infty_M\)-module sheaves by
postcomposition.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: vector bundles, local frames, and smooth sections.
2. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: vector bundles and their local trivializations.
