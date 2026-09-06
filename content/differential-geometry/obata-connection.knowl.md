+++
id = "differential-geometry/obata-connection"
title = "Obata connection"
kind = "definition"
summary = "The unique torsion-free connection preserving the three complex structures of a hypercomplex manifold."
aliases = ["canonical connection of a hypercomplex manifold"]
domains = ["differential-geometry", "fiber-bundles"]
prerequisites = ["differential-geometry/hypercomplex-manifold", "fiber-bundles/connection-on-a-vector-bundle", "differential-geometry/integrable-almost-complex-structure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((M,I,J,K)\) be a [[differential-geometry/hypercomplex-manifold|hypercomplex manifold]]. Its **Obata connection** is the unique torsion-free [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla^{\mathrm{Ob}}\) on \(TM\) satisfying
\[
\nabla^{\mathrm{Ob}}I=\nabla^{\mathrm{Ob}}J=\nabla^{\mathrm{Ob}}K=0.
\]
Here \((\nabla_X I)Y=\nabla_X(IY)-I\nabla_XY\), and similarly for \(J,K\); torsion-free means \(\nabla_XY-\nabla_YX=[X,Y]\). Existence uses the [[differential-geometry/integrable-almost-complex-structure|integrability]] of the three complex structures, while preservation of the entire quaternionic triple forces uniqueness. Thus the connection is canonically determined by the hypercomplex structure and does not require a metric.

## Characterization and holonomy

Obata's construction gives an equivalence: an almost-hypercomplex triple admits a torsion-free connection preserving \(I,J,K\) exactly when the triple is hypercomplex. Parallel transport is therefore quaternionic-linear, and the holonomy of \(\nabla^{\mathrm{Ob}}\) is contained in \(GL(n,\mathbb H)\) when \(\dim_{\mathbb R}M=4n\).

## Relation to a compatible metric

The Obata connection is defined without a metric and generally is not a Levi-Civita connection. If a [[differential-geometry/hyperhermitian-manifold|hyper-Hermitian metric]] \(g\) has \(\nabla^{\mathrm{Ob}}g=0\), then uniqueness of the torsion-free metric connection identifies \(\nabla^{\mathrm{Ob}}\) with the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] of \(g\); the resulting metric is [[differential-geometry/hyperkahler-manifold|hyperkähler]]. On \(\mathbb H^n\) with its constant hypercomplex triple, the Obata connection is the ordinary flat connection.

## References

1. Morio Obata, “Affine Connections on Manifolds with Almost Complex, Quaternion or Hermitian Structure,” *Japanese Journal of Mathematics* 26 (1956), 43–77. [J-STAGE DOI record and full text](https://doi.org/10.4099/jjm1924.26.0_43).
2. Dominic D. Joyce, *Compact Manifolds with Special Holonomy*, Oxford University Press, 2000. [Oxford DOI record](https://doi.org/10.1093/oso/9780198506010.001.0001). Relevant: hypercomplex and hyperkähler geometry.
