+++
id = "differential-geometry/twistor-space-quaternionic-manifold"
title = "Twistor space of a quaternionic manifold"
kind = "definition"
summary = "The sphere bundle whose fiber consists of the compatible complex structures in a quaternionic structure."
aliases = ["quaternionic twistor space", "twistor bundle"]
domains = ["differential-geometry", "fiber-bundles"]
prerequisites = ["differential-geometry/quaternionic-manifold", "fiber-bundles/sphere-bundle"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M^{4n},Q)\) be a [[differential-geometry/quaternionic-manifold|quaternionic manifold]]. Its **twistor space** is the [[fiber-bundles/sphere-bundle|sphere bundle]]
\[
\pi:Z=S(Q)\longrightarrow M
\]
whose fiber at \(x\) is
\[
Z_x=\{A\in Q_x:A^2=-\operatorname{id}_{T_xM}\}.
\]
The quaternionic algebra gives \(Q\) a canonical Euclidean metric and orientation, so \(Z_x\) is a two-sphere: after choosing a local admissible frame \((I,J,K)\), its points are \(aI+bJ+cK\) with \(a^2+b^2+c^2=1\). Although this description uses a frame, the bundle \(Z\) does not. Each point of \(Z\) records one complex structure compatible with \(Q\) at its base point.

## Canonical almost-complex structure

A quaternionic connection splits \(TZ\) into horizontal and vertical parts. On a horizontal vector over \((x,A)\), use \(A\); on the [[fiber-bundles/vertical-tangent-space|vertical tangent space]] of \(Z_x\cong\mathbb{CP}^1\), use its standard complex structure. These pieces define an [[differential-geometry/almost-complex-structure|almost-complex structure]] on \(Z\). For \(n\geq2\), it is independent of the chosen torsion-free quaternionic connection and is integrable.

## Examples and interpretation

The twistor space of quaternionic projective space \(\mathbb H P^n\) is \(\mathbb{CP}^{2n+1}\), with the projection arising from the inclusion of a complex line in the quaternionic line that it spans. For a [[differential-geometry/hypercomplex-manifold|hypercomplex manifold]], the global triple trivializes \(Q\), so \(Z\) is smoothly \(M\times S^2\); its canonical complex structure nevertheless mixes the two factors and is not generally the product complex structure.

The twistor space packages the rotating local complex structures of quaternionic geometry into one [[differential-geometry/complex-manifold|complex manifold]]. It should not be confused with the unit [[fiber-bundles/tangent-bundle|tangent bundle]]: its sphere fibers lie in \(Q\subseteq\operatorname{End}(TM)\), not in \(TM\).

## References

1. Simon Salamon, “Quaternionic Kähler Manifolds,” *Inventiones Mathematicae* 67 (1982), 143–171. [DOI record](https://doi.org/10.1007/BF01393378). Relevant: §§3–4, the twistor bundle and its integrable complex structure.
