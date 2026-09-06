+++
id = "differential-geometry/proper-injective-immersion-is-an-embedding"
title = "Proper injective immersion is an embedding"
kind = "theorem"
summary = "A proper injective smooth immersion between manifolds is a smooth embedding."
aliases = ["proper immersion embedding criterion"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/smooth-immersion", "differential-geometry/proper-smooth-map", "fiber-bundles/smooth-embedding", "topology/subspace-topology"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) and \(N\) be [[fiber-bundles/smooth-manifold|smooth manifolds]], and let \(f:M\to N\) be a [[fiber-bundles/smooth-immersion|smooth immersion]]. If \(f\) is injective and is a [[differential-geometry/proper-smooth-map|proper smooth map]], then \(f\) is a [[fiber-bundles/smooth-embedding|smooth embedding]]. Equivalently, \(f\) is a homeomorphism from \(M\) onto \(f(M)\) with the [[topology/subspace-topology|subspace topology]], in addition to having injective differential at every point. The result supplies the global topological condition missing from the local immersion hypothesis; injectivity alone does not force the inverse \(f(M)\to M\) to be continuous.

## Proof mechanism

A proper [[topology/continuous-map|continuous map]] between manifolds is closed. Since \(f\) is also injective, the induced bijection \(M\to f(M)\) is a closed map and hence a homeomorphism. The immersion condition then provides the required local smooth normal form. Thus properness solves the global topology problem, while immersion solves the local differential problem.

## Why properness matters

For irrational \(\alpha\), the map
\[
t\longmapsto(e^{it},e^{i\alpha t})
\]
from \(\mathbb R\) to the torus is an injective immersion with dense image, but it is not an embedding and is not proper. Points with parameters escaping to infinity can return arbitrarily close to the image of a fixed parameter, preventing continuity of the inverse on the image.

## Converse and scope

The converse is false: the inclusion \((0,1)\hookrightarrow\mathbb R\) is a smooth embedding but not proper. If \(M\) is compact, every continuous map \(M\to N\) is proper, so an injective immersion from a compact manifold is automatically an embedding.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 4, embeddings and proper maps.
2. Morris W. Hirsch, *Differential Topology*, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 1, immersions and embeddings.
