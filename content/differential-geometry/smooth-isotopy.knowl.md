+++
id = "differential-geometry/smooth-isotopy"
title = "Smooth isotopy"
kind = "definition"
summary = "A smooth one-parameter family of smooth embeddings joining two given embeddings."
aliases = ["isotopy of embeddings"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(f_0,f_1:M\to N\) be [[fiber-bundles/smooth-embedding|smooth embeddings]] between [[fiber-bundles/smooth-manifold|smooth manifolds]]. A **smooth isotopy** from \(f_0\) to \(f_1\) is a [[differential-geometry/smooth-map-of-manifolds-with-boundary|smooth map in the manifold-with-boundary sense]] \(F:M\times[0,1]\to N\) such that \(F(x,0)=f_0(x)\), \(F(x,1)=f_1(x)\), and every time slice \(F_t(x)=F(x,t)\) is a smooth embedding. Thus both the dependence on \(t\) and the combined map \(F\) are smooth, while injectivity and the embedding condition are required slice by slice. An isotopy of diffeomorphisms analogously requires every \(F_t\) to be a diffeomorphism.

## Relation to homotopy

Every isotopy is a [[differential-geometry/smooth-homotopy|smooth homotopy]], but the converse need not hold: intermediate maps in a homotopy may develop self-intersections, lose rank, or cease to be invertible. Isotopy therefore records deformation within a geometrically constrained class rather than merely deformation through arbitrary continuous or smooth maps.

## Ambient isotopy

An ambient isotopy of \(N\) is a smooth family of diffeomorphisms \(\Phi_t:N\to N\) with \(\Phi_0=\operatorname{id}_N\). It carries an embedding \(f_0\) to \(f_t=\Phi_t\circ f_0\). The [[differential-geometry/isotopy-extension-theorem|isotopy extension theorem]] gives hypotheses under which an isotopy of embeddings extends to an ambient isotopy; see [Hirsch, Chapter 8](https://doi.org/10.1007/978-1-4684-9449-5).

## Conventions and examples

A rotation of the circle through a continuously varying angle is an isotopy of diffeomorphisms. A family of embedded knots is an isotopy of embeddings. Authors sometimes say “smooth isotopy” for any smooth homotopy; the intended slice condition must be checked from context.

## References

1. Morris W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics 33, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 8, isotopy and isotopy extension.
2. Victor Guillemin and Alan Pollack, *Differential Topology*, Prentice-Hall, 1974. [AMS record](https://bookstore.ams.org/chel-370-h). Relevant: isotopy and differential-topological deformation arguments.
