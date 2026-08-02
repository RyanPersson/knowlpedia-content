+++
id = "supergeometry/super-vector-space"
title = "Super vector space"
kind = "definition"
summary = "A vector space decomposed into even and odd subspaces."
aliases = ["Z/2-graded vector space", "graded vector space with parity"]
domains = ["supergeometry", "linear-algebra"]
section_mode = "progressive"
+++

Let \(k\) be a field. A **super vector space** over \(k\) is a
\(\mathbb Z/2\)-graded vector space
\[
V=V_{\bar 0}\oplus V_{\bar 1}.
\]
Elements of \(V_{\bar 0}\) are **even**, elements of \(V_{\bar 1}\) are
**odd**, and a nonzero element in either summand is **homogeneous**. The
**parity** of a homogeneous element \(v\) is
\(|v|\in\mathbb Z/2\), determined by \(v\in V_{|v|}\).

## Maps and dimensions

A homogeneous [[linear-algebra/linear-map|linear map]] \(f:V\to W\) has parity
\(\epsilon\) when
\[
f(V_{\bar i})\subseteq W_{\bar i+\epsilon}.
\]
Thus even maps preserve parity and odd maps reverse it. Unless stated
otherwise, morphisms between super vector spaces are even maps; odd maps
belong to the [[supergeometry/super-internal-hom|graded internal Hom]] rather than the ordinary morphism set.

If both summands are finite-dimensional, the **graded dimension** is
\[
\dim_{\mathrm{gr}}V
=\dim V_{\bar0}\mid\dim V_{\bar1}.
\]
The ordered pair, not its difference, determines the dimensions of the two
summands. The **categorical superdimension**, namely the trace of the identity
computed with the [[supergeometry/koszul-sign-rule|Koszul sign rule]], is
\[
\operatorname{sdim}(V)
=\dim V_{\bar0}-\dim V_{\bar1}.
\]
Some authors call either invariant “superdimension,” so specifying “graded”
or “categorical” avoids an ambiguity.

## Examples

Every ordinary vector space becomes a purely even super vector space by
putting \(V_{\bar1}=0\). The [[algebra-modules/exterior-algebra|exterior
algebra]] \(\Lambda U\) is a super vector space when exterior degree is reduced
modulo \(2\):
\[
(\Lambda U)_{\bar0}=\bigoplus_j\Lambda^{2j}U,
\qquad
(\Lambda U)_{\bar1}=\bigoplus_j\Lambda^{2j+1}U.
\]

## Characteristic and terminology

The decomposition itself makes sense in every characteristic. Throughout the
super sign convention used in these knowls, \(k\) has characteristic different
from \(2\). In characteristic \(2\), the sign \((-1)^{|v||w|}\) cannot
distinguish commuting from anticommuting odd elements, and several standard
definitions need extra structure.

“Graded vector space” can refer to a grading by \(\mathbb Z\) or another group.
The adjective “super” specifically means a \(\mathbb Z/2\)-grading.

## References

1. V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction*,
   American Mathematical Society, 2004. [DOI
   record](https://doi.org/10.1090/cour/011). Relevant: Chapter 1.
2. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of
   Supersymmetry*, European Mathematical Society, 2011. [DOI
   record](https://doi.org/10.4171/097). Relevant: Chapter 1.
