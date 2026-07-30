+++
id = "mathematical-physics/super-poincare-algebra"
title = "Super-Poincaré algebra"
kind = "definition"
summary = "The Lie superalgebra obtained by adjoining Lorentz transformations to a supertranslation algebra."
aliases = ["Poincare superalgebra"]
domains = ["mathematical-physics", "supergeometry", "lie-groups"]
section_mode = "progressive"
+++

Let
\(\mathfrak t=V_{\bar0}\oplus S_{\bar1}\) be a
[[mathematical-physics/supertranslation-algebra|supertranslation algebra]]
whose bracket
\(\Gamma:\operatorname{Sym}^2S\to V\) is
\(\mathfrak{so}(V,\eta)\)-equivariant. The associated
**super-Poincaré algebra** is
\[
\mathfrak{spoin}(V,S,\Gamma)
=\mathfrak{so}(V,\eta)\ltimes\mathfrak t.
\]
Its even part is the [[mathematical-physics/poincare-algebra|Poincaré
algebra]]
\[
\mathfrak{spoin}_{\bar0}
=\mathfrak{so}(V,\eta)\ltimes V,
\]
and its odd part is \(S\).

For \(A,B\in\mathfrak{so}(V,\eta)\), \(v,w\in V\), and \(s,t\in S\), the
nonzero brackets are
\[
[A,B]_{\mathfrak{so}},\qquad [A,v]=Av,\qquad
[A,s]=A\cdot s,\qquad [s,t]=\Gamma(s,t).
\]
Equivariance of \(\Gamma\) is precisely the mixed Jacobi identity involving a
Lorentz generator and two supercharges.

## Terminology and enrichments

In physics, “the supersymmetry algebra” often means a dimension- and
signature-specific extension of this algebra. Common enrichments include
multiple supercharge copies (\(\mathcal N>1\)), \(R\)-symmetry derivations,
central charges, and tensorial brane charges. These choices change the
algebra and must be stated explicitly.

The Lie superalgebra is infinitesimal data. Its integration to a global
[[supergeometry/lie-supergroup|Lie supergroup]] additionally requires a
compatible choice of global reduced Poincaré or spin-cover group, naturally
expressed as a
[[supergeometry/super-harish-chandra-pair|super Harish–Chandra pair]].

## References

1. J. Wess and J. Bagger, *Supersymmetry and Supergravity*, second edition, Princeton University Press, 1992. Relevant: Chapter 3.
2. D. S. Freed, *Five Lectures on Supersymmetry*, American Mathematical Society, 1999. [Publisher record](https://doi.org/10.1090/amsip/011). Relevant: Lectures 1–2.
